#!/usr/bin/env node

import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const transport = new StdioClientTransport({
  command: "node",
  args: ["/Users/tony/workspace/project/mcp/fesod-mcp/dist/cli.js"],
});

const client = new Client({
  name: "Fesod-client",
  version: "1.0.0",
});

console.log("正在连接 MCP 服务器...");
await client.connect(transport);
console.log("成功连接到 MCP 服务器!");

// 执行示例工具调用
try {
  // 列出所有组件
  console.log("\n--- 列出功能列表 ---");
  const components = await client.callTool({
    name: "list-api",
    arguments: {},
  });
  Array.isArray(components.content) && console.log(components.content[0].text);

  // 获取组件文档
  console.log("\n--- 获取功能文档 ---");
  const docs = await client.callTool({
    name: "get-api-doc",
    arguments: {
      name: "fill",
      lang: "en"
    },
  });
  Array.isArray(docs.content) && console.log(docs.content[0].text);

} catch (error) {
  console.error("测试过程中出错:", error);
} finally {
  // 关闭连接
  await client.close();
  console.log("\n测试完成，已断开与服务器的连接。");
}
