# @tony2026m/fesod-mcp

[![npm version](https://img.shields.io/npm/v/@tony2026m/fesod-mcp.svg)](https://www.npmjs.com/package/@tony2026m/fesod-mcp)
[![license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Node.js version](https://img.shields.io/badge/node-%3E%3D20.0.0-brightgreen.svg)](https://nodejs.org/)

> An MCP (Model Context Protocol) service for Apache Fesod API query | 一个减少 Apache Fesod 库在 Excel 操作代码实现时产生幻觉的 MCP 服务

## 📖 简介

`@tony2026m/fesod-mcp` 是一个专为 Apache Fesod (Incubating) Excel 操作库设计的 MCP 服务器，提供：

- 🔍 **API 列表查询** - 快速浏览 Apache Fesod 所有可用的功能和 API
- 📚 **功能文档查询** - 获取详细的功能使用文档、API 说明和使用场景
- 💡 **代码示例获取** - 提供实际可运行的 Java 代码示例
- 🌐 **多语言支持** - 支持中英文文档查询（默认英文）
- 🎯 **系统提示词** - 内置专业的 Apache Fesod 使用指导
- ⚡ **缓存机制** - 提供高性能的文档查询体验

## 什么是 Apache Fesod？

**Apache Fesod (Incubating)** 是一款高性能且内存高效的 Java 库，用于读写电子表格文件（Excel），旨在简化开发并确保可靠性。

### 主要特性

- **高性能读写** - 专注于性能优化，能够高效处理大规模电子表格数据
- **简单易用** - 提供简单直观的 API，易于集成到项目中
- **流式操作** - 支持流式读取，有效规避一次性加载海量数据的瓶颈

## 什么时候需要自行提取文档？

1. 你想使用最新版本的 Apache Fesod 文档
2. 你想使用特定版本的 Apache Fesod 文档

### 提取 Apache Fesod 文档

```bash
# 克隆 Apache Fesod 仓库
git clone https://github.com/apache/fesod.git ./.temp/fesod --depth 1 --branch main --single-branch --filter=blob:none

# 在当前目录执行提取文档命令
npx @tony2026m/fesod-mcp extract [fesod repo path]  # 默认提取路径为 ./.temp/fesod
```

## 🚀 快速开始

### 作为 MCP 服务器使用（推荐）

在 Cursor 或其他支持 MCP 的 AI 编辑器中配置：

```json
{
  "mcpServers": {
    "Fesod": {
      "command": "npx",
      "args": ["@tony2026m/fesod-mcp"]
    }
  }
}
```

或者使用本地安装：

```bash
npm install -g @tony2026m/fesod-mcp
```

然后配置：

```json
{
  "mcpServers": {
    "Fesod": {
      "command": "fesod-mcp"
    }
  }
}
```

### 直接运行

```bash
# 使用 npx（无需安装）
npx @tony2026m/fesod-mcp

# 或全局安装后运行
npm install -g @tony2026m/fesod-mcp
fesod-mcp
```

## 🛠️ 可用工具

MCP 服务器提供以下工具：

### 1. `list-api`
列出所有可用的 Apache Fesod 功能和 API

**使用场景：**
- 当用户进行 Java 开发，需要使用 Apache Fesod 进行 Excel 操作时
- 查看框架提供的所有功能模块和 API

**返回数据结构：**
```typescript
{
  name: string;        // api功能名称
  dirName: string;     // api文件名称
  description: string; // api功能描述
  module: string;      // 所属模块
  whenToUse: string;   // 使用场景
  keywords: string[];  // 关键词
}
```

### 2. `get-api-doc`
获取特定功能或 API 的详细文档

**参数：**
- `name` - API 或功能名称（如 "简单写入"、"填充"、"简单读取" 等）
- `lang` - 文档语言（可选，默认 "en"）
  - `en` - 英文文档
  - `zh` - 中文文档

**使用场景：**
- 用户询问如何使用特定 API 或功能
- 需要查看 API 的介绍、使用场景、示例代码等

## 📚 支持的功能模块

本 MCP 服务涵盖 Apache Fesod 的所有核心功能：

- **快速开始 (quickstart)**: 简单示例、安装指南
- **读取功能 (read)**: 简单读取、POJO 读取、表头读取、CSV 读取、额外信息读取、异常处理、格式转换、与 Spring 集成等
- **写入功能 (write)**: 简单写入、POJO 写入、表头写入、CSV 写入、样式设置、图片导出、额外信息写入、格式化、与 Spring 集成等
- **填充功能 (fill)**: 数据填充
- **帮助文档 (help)**: 核心类介绍、注解说明、参数说明、常见问题、大数据量处理等
- **迁移指南 (migration)**: 从 FastExcel 迁移

## 📦 系统要求

- Node.js >= 20.0.0
- 支持 MCP 协议的客户端（如 Cursor、Claude Desktop 等）

## 🔧 开发

```bash
# 克隆仓库
git clone https://github.com/tony2026m/fesod-mcp.git
cd fesod-mcp

# 安装依赖
pnpm install

# 开发模式
pnpm dev

# 构建
pnpm build

# 测试
pnpm test

# 使用 MCP Inspector 调试
pnpm inspector
```

## 📄 许可证

MIT License - 详见 [LICENSE](./LICENSE) 文件

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 👨‍💻 作者

**tony2026m**
- Email: mly7758@163.com

## 🙏 致谢

本项目基于 [Apache Fesod (Incubating)](https://fesod.apache.org/) 官方文档构建。

## 🔗 相关链接

- [Apache Fesod 官网](https://fesod.apache.org/)
- [Apache Fesod GitHub](https://github.com/apache/fesod)
- [Maven 中心仓库](https://mvnrepository.com/artifact/org.apache.fesod/fesod-sheet)

## 📝 更新日志

查看 [CHANGELOG.md](./CHANGELOG.md) 了解版本历史。
