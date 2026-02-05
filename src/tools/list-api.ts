import type { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";

import { loadApisList } from "../utils/components";

/** 列出所有可用的 Fesod API */
const registryTool = (server: McpServer) => {
  server.tool(
    "list-api", `当用户根据业务需求进行Excel操作的开发，需要使用 Fesod 框架操作Excel时使用此工具。
此工具仅返回框架可用的功能(API)列表。
调用此工具后，你必须根据你的业务需求、来选择符合你业务需求的功能api，完成Excel操作代码的编写
功能列表元素数据结构：
\`ts
export interface ComponentData {
  // api功能名称
  name: string;
  // api文件名称
  dirName: string;
  // api功能描述
  description: string;
  // 所属模块
  module: string;
  // 使用场景
  whenToUse: string;
  // 关键词
  keywords: string[];
}
\`
`,
      async () => {
      const apis = await loadApisList();
      return {
        content: [
          {
            type: "text",
            text: `以下是Fesod可用的功能：${JSON.stringify(apis)}`,
          },
        ],
      };
    });
}

export default registryTool;
