import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";

import listApi from "./list-api";
import getApiDoc from "./get-api-doc";

export default function registryTools(server: McpServer) {
  [listApi, getApiDoc].forEach((registryFn) => {
    registryFn(server)
  })
}
