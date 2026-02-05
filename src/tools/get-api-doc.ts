import type { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";
import { getApiDocumentation } from "../utils/components";

/** 获取组件文档 */
const registryTool = (server: McpServer) => {
  server.tool(
    "get-api-doc",
    `通过名称，获取 Fesod 特定功能api 功能的详细文档
适用场景：
1. 用户询问如何使用特定api或功能
2. 用户需要查看api、功能的 介绍，使用场景、示例代码等`,
    { name: z.string().describe("api或功能名称。例如：简单写入, 填充等"), lang: z.string().optional().describe("文档语言，默认为英文。(en: 英文, zh: 中文)") },
    async ({ name, lang }) => {
      const documentation = await getApiDocumentation(name, lang);
      return {
        content: [
          {
            type: "text",
            text: `${name} 的文档：${documentation}`,
          },
        ],
      };
    },
  );
}

export default registryTool;
