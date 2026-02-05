import os
import re
from pathlib import Path
import yaml

# 匹配 <code ...>inner</code>，支持跨行
code_pattern = r'<code\s+([^>]*?)>\s*(.*?)\s*</code>'

# 匹配以三个连字符开始和结束的YAML front matter ^---\s*\n(.*?)\n---\s*\n?
front_matter_pattern = r'^---\s*\n(.*?)\n---\s*\n?'

def read_markdown_to_string(file_path):
    """
    读取markdown文件

    :param file_path: 文件路径
    :return: markdown字符串
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        return content
    except FileNotFoundError:
        print(f"错误：文件 {file_path} 未找到")
        return ""
    except Exception as e:
        print(f"读取文件时出错: {e}")
        return ""

def replace_code(markdown_text, replacement_func=None):
    """
    提取 <code> 标签中的 src、title 和 inner text，并替换整个标签。

    :param markdown_text: 原始 Markdown 字符串
    :param replacement_func: 自定义替换函数，接收 (src, title, inner) 返回替换字符串
            若为 None，则使用默认格式
    :return: 替换后的字符串
    """
    def default_replacer(src, title, inner, description, thumbnail):
        # 默认替换格式，你可以改成任何你需要的内容
        display_title = title if title else inner
        parts = src.strip().split('demos')
        # file_path = Path(src)
        display_path = parts[1]
        # 外部示例代码，需通过工具方法另外获取代码片段
        return f'''- {display_title}[外部示例代码]\n\t- description: {description}\n\t- src: {display_path}\n\t- thumbnail: {thumbnail}'''

    def match_handler(match):
        attrs_str = match.group(1)
        inner_text = match.group(2).strip()  # 去除首尾空白

        # 解析属性：只处理 key="value" 形式（双引号）
        attr_matches = re.findall(r'(\w+)\s*=\s*"([^"]*)"', attrs_str)
        attrs = dict(attr_matches)

        src = attrs.get('src', '')  # 必须有 src 才有意义，但即使没有也保留空
        title = attrs.get('title', '')
        description = attrs.get('description', '')
        thumbnail = attrs.get('thumbnail', '')
        # background 等其他属性可按需提取

        if replacement_func:
            return replacement_func(src, title, inner_text, description, thumbnail)
        else:
            return default_replacer(src, title, inner_text, description, thumbnail)

    result = re.sub(code_pattern, match_handler, markdown_text, flags=re.DOTALL | re.IGNORECASE)
    return result

def get_meta(content: str):
    """
    从 Markdown 内容中提取 YAML front matter（meta 信息）。

    参数:
        content (str): 完整的 Markdown 文件内容。

    返回:
        dict: 解析后的 meta 字典。如果没有 front matter，返回空字典 {}。
    """
    # 匹配以 --- 开始和结束的 YAML front matter
    match = re.match(front_matter_pattern, content, re.DOTALL)

    if not match:
        return {}

    yaml_content = match.group(1)
    try:
        meta = yaml.safe_load(yaml_content)
        # 如果 yaml.safe_load 返回 None（如空内容），返回空字典
        return meta if isinstance(meta, dict) else {}
    except yaml.YAMLError:
        # 如果 YAML 格式非法，视为无有效 meta
        return {}

def remove_meta(content: str) -> str:
    """
    移除Markdown文件中的YAML front matter元数据

    :param content: Markdown字符串
    :return: 删除front matter元数据后的字符串
    """
    # 使用正则表达式查找并移除front matter
    return re.sub(front_matter_pattern, '', content, flags=re.DOTALL)

def merge_markdown(origin_path:str, merge_path:str):
    """
    将两个markdown文件合并

    :param origin_content: 原始 Markdown 内容
    :param merge_content: 被合并的 Markdown 内容
    """
    origin_content = read_markdown_to_string(origin_path)
    merge_content = read_markdown_to_string(merge_path)

    if not origin_content and not merge_content:
        print("两个文件都为空或读取失败")
        return False

    # 移除被合并的文件的meta数据
    new_merge = remove_meta(merge_content)

    # 合并内容
    merged_content =  f'{origin_content.rstrip('\n')}\n\n{new_merge.lstrip('\n')}'

    return merged_content

def safe_delete_file(filepath: str) -> bool:
    """
    安全删除文件，可以选择备份到指定目录

    :param filepath: 要删除的文件路径
    :param backup_dir: 备份目录（可选）
    :returns:
        bool: 是否删除成功
    """
    try:
        delPath = Path(filepath)

        if not delPath.exists():
            print(f"文件 {filepath} 不存在，无需删除")
            return False

        # 删除文件
        file_size = delPath.stat().st_size
        delPath.unlink()
        print(f"✓ 已删除: {delPath.name} ({file_size} 字节)")
        return True
    except Exception as e:
        print(f"删除文件 {filepath} 时出错: {e}")
        return False

def get_description_and_when_to_use(md_content, when_to_use_prefixes=None):
    if when_to_use_prefixes is None:
        when_to_use_prefixes = ['何时使用', 'When to Use']

    clean_content = remove_meta(md_content)
    lines = clean_content.splitlines()

    # 找到第一个 ## 标题的位置
    start_idx = 0
    # 跳过开头空行
    while start_idx < len(lines) and not lines[start_idx].strip():
        start_idx += 1

    # 如果第一行是 # 标题，跳过它
    if start_idx < len(lines) and re.match(r'^#\s+', lines[start_idx]):
        start_idx += 1

    # 查找第一个 ## 标题
    first_h2_index = None
    for i in range(start_idx, len(lines)):
        if re.match(r'^##\s+', lines[i]):
            first_h2_index = i
            break

    # description: 从 start_idx 到 first_h2_index（若无则到末尾）
    end_idx = first_h2_index if first_h2_index is not None else len(lines)
    description_lines = lines[start_idx:end_idx]

    # 提取 when_to_use（同前）
    when_to_use_lines = []
    if first_h2_index is not None:
        h2_line = lines[first_h2_index]
        h2_text = h2_line.lstrip('#').strip()
        is_when_to_use = any(
            h2_text.lower().startswith(p.lower()) for p in when_to_use_prefixes
        )
        if is_when_to_use:
            next_h2_or_h1 = None
            for j in range(first_h2_index + 1, len(lines)):
                if re.match(r'^#{1,2}\s+', lines[j]):  # 下一个 # 或 ##
                    next_h2_or_h1 = j
                    break
            when_end = next_h2_or_h1 if next_h2_or_h1 else len(lines)
            when_to_use_lines = lines[first_h2_index + 1: when_end]

    def clean(lines):
        while lines and not lines[0].strip(): lines.pop(0)
        while lines and not lines[-1].strip(): lines.pop()
        return '\n'.join(lines)

    return {
        'description': clean(description_lines),
        'when_to_use': clean(when_to_use_lines)
    }