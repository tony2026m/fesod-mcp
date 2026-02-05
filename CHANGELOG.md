# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-02-05

### Added
- 🎉 Initial release
- ✨ MCP server for Apache Fesod (Incubating) documentation query
- 📚 `list-api` tool - List all available Apache Fesod APIs and features
- 📖 `get-api-doc` tool - Get detailed API/feature documentation with usage examples
- 🌐 Multi-language support (English and Chinese documentation)
- 🎯 Built-in system prompts for Apache Fesod usage guidance
- 💾 Caching mechanism for improved performance (using node-cache)
- 🌐 Support for ES Module
- 📦 Ready for npx usage
- 🛠️ Documentation extraction script for custom Apache Fesod versions
- 🐍 Python scripts for automated documentation extraction from Apache Fesod repository

### Features
- Support for all Apache Fesod modules:
  - **Quickstart** (Simple Example, Guide, Installation)
  - **Read Operations** (Simple Read, POJO Read, Head Read, CSV Read, Extra Info Read, Exception Handling, Format Conversion, Spring Integration)
  - **Write Operations** (Simple Write, POJO Write, Head Write, CSV Write, Style Settings, Image Export, Extra Info Write, Formatting, Spring Integration)
  - **Fill Operations** (Data Filling)
  - **Help** (Core Classes, Annotations, Parameters, FAQ, Large Data Handling)
  - **Migration** (From FastExcel)
- Comprehensive API documentation with Java code examples
- Bilingual documentation (English/Chinese) with language selection
- Node.js >= 20.0.0 support
- Built on @modelcontextprotocol/sdk v1.25.3
- TypeScript support

### Technical Details
- Built with TypeScript 5.8.2
- Uses tsup for building
- Includes vfile-matter for markdown frontmatter parsing
- Zod for schema validation
- Python scripts (extract_fesod.py, operate_markdown.py) for document extraction from Apache Fesod repository
- Structured API index with metadata (name, description, module, whenToUse, keywords)

### Documentation Structure
- Extracted from Apache Fesod official documentation
- Supports both English (`/docs/en`) and Chinese (`/docs/zh`) documentation
- API index with comprehensive metadata for quick lookup
- Module-based organization (quickstart, read, write, fill, help, migration)

[0.1.0]: https://github.com/tony2026m/fesod-mcp/releases/tag/v0.1.0
