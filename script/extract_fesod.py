import os
from pathlib import Path
import json
from operate_markdown import read_markdown_to_string, get_meta, get_description_and_when_to_use

# 源文档repo根目录
root_origin_repo = '../.temp/fesod'
# 源中文文档根目录
root_origin_zh = '../.temp/fesod/website/i18n/zh-cn/docusaurus-plugin-content-docs/current'

en_origin_path = 'docs'
zh_origin_path = 'i18n/zh-cn/docusaurus-plugin-content-docs/current'

en_docs_path = '/docs/en'
zh_docs_path = '/docs/zh'

def extract_fesod():
    """提取fesod文档"""
    with open('../config.json', 'r', encoding='utf-8') as file:
        json_data = json.load(file)
        origin_root = json_data['script']['doc_root']['fesod']
        target_root = json_data['js']['doc_root']['fesod']

    target_root_path = Path(target_root)
    target_root_path.mkdir(parents=True, exist_ok=True)

    target_en_path = Path(os.path.join(target_root, 'docs/en'))
    target_en_path.mkdir(parents=True, exist_ok=True)

    target_zh_path = Path(os.path.join(target_root, 'docs/zh'))
    target_zh_path.mkdir(parents=True, exist_ok=True)

    origin_doc_en = Path(os.path.join(origin_root, en_origin_path))
    origin_doc_zh = Path(os.path.join(origin_root, zh_origin_path))

    # 循环遍历路径做成api文档
    def list_all_api_docs(lang='en'):
        directory = origin_doc_en if lang == 'en' else origin_doc_zh
        target_doc_path = target_en_path if lang == 'en' else target_zh_path

        # 遍历源根目录下的所有子文件夹
        for source_dir in Path(directory).iterdir():
            if source_dir.is_dir():
                # 获取子文件夹名称
                subfolder_name = source_dir.name
                print(f"处理文件夹: {subfolder_name}")

                # 创建对应的目标子文件夹
                target_dir = target_doc_path / subfolder_name
                target_dir.mkdir(parents=True, exist_ok=True)

                # 遍历子文件夹下的所有文件（包括子文件夹中的文件）
                for file_path in source_dir.rglob('*'):
                    if file_path.is_file():
                        filename = file_path.name
                        print(f'{lang}_文件名:{filename}')

                        if filename == '.DS_Store':
                            continue

                        # 构建目标文件路径, 将文件压缩在一级目录下
                        target_file_path = target_dir / filename
                        if file_path.parent.name != target_dir.name:
                           target_sub_dir = target_dir / file_path.parent.name
                           target_sub_dir.mkdir(parents=True, exist_ok=True)

                           target_file_path = target_sub_dir / filename

                        print(f"目标文件路径: {target_file_path}")

                        try:
                            # 读取Markdown文件
                            markdown_content = read_markdown_to_string(file_path)

                            # 写入到目标文件
                            with open(target_file_path, 'w', encoding='utf-8') as f:
                                f.write(markdown_content)
                        except Exception as e:
                            print(f"  处理文件失败 {file_path}: {e}")
            else:
                # 构建目标文件路径, 将文件压缩在一级目录下
                target_file_path = target_doc_path / source_dir.name
                print(f"目标文件路径: {target_file_path}")

                try:
                    # 读取Markdown文件
                    markdown_content = read_markdown_to_string(source_dir)

                    # 写入到目标文件
                    with open(target_file_path, 'w', encoding='utf-8') as f:
                        f.write(markdown_content)
                except Exception as e:
                    print(f"  处理文件失败 {source_dir}: {e}")

    def make_api_json():
        api_index = []
        # 遍历目标英文目录下的所有子文件夹
        for source_dir in Path(target_en_path).iterdir():
            # 遍历子文件夹下的所有文件（包括子文件夹中的文件）
            for file_path in source_dir.rglob('*'):
                # 遍历子文件夹下的所有文件（包括子文件夹中的文件）
                if file_path.is_file():
                    filename = file_path.name
                    module_name = file_path.parent.name
                    if filename == '.DS_Store':
                        continue

                    if module_name == 'en':
                        zh_doc_file = target_zh_path / filename
                    else:
                        zh_doc_file = Path(str(file_path).replace('/en', '/zh'))

                    zh_path_arr = str(zh_doc_file).split('/zh')

                    # 读取文件
                    en_content = read_markdown_to_string(file_path)
                    # 获取meta信息
                    en_meta = get_meta(en_content)
                    # 获取描述
                    en_description = get_description_and_when_to_use(en_content)

                    # 读取文中文件
                    zh_content = read_markdown_to_string(zh_doc_file)
                    # 获取中文meta信息
                    zh_meta = get_meta(zh_content)
                    # 获取中文描述
                    zh_description = get_description_and_when_to_use(zh_content)

                    en_atomId = ''
                    if 'keywords' in en_meta:
                        en_atomId = en_meta['keywords']

                    zh_atomId = ''
                    if 'keywords' in zh_meta:
                        zh_atomId = zh_meta['keywords']

                    match module_name:
                        case 'fill':
                            module_name = '(填充 fill)'
                        case 'write':
                            module_name = '(写入 write)'
                        case 'read':
                            module_name = '(读取 read)'

                    api_index.append({
                        "name": (en_meta['title'] + ' | ' + zh_meta['title'] if en_meta['title'] != zh_meta['title'] else en_meta['title']) + ', ' + module_name,
                        "dirName": zh_path_arr[1],
                        "description": en_description['description'] + ' | ' + zh_description['description'],
                        "whenToUse": en_description['when_to_use'] + ' | ' + zh_description['when_to_use'],
                        "keywords": list(set(en_atomId + zh_atomId)),
                        "module": module_name,
                    })

        json_path = os.path.join(target_root, 'api-index.json')
        # 写入到目标文件
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(api_index, f, ensure_ascii=False, indent=4)

    # 遍历英文文档
    list_all_api_docs('en')

    # 遍历中文文档
    list_all_api_docs('zh')

    make_api_json()


def main():
    extract_fesod()


if __name__ == '__main__':
    main()
