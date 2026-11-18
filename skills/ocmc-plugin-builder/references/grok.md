# Grok and xAI

Sources checked November 18, 2026. Choose the product surface before building.

| Surface | Documented MCP path |
| --- | --- |
| Grok chat | In Connectors, choose New Connector and Custom. Enter a reachable server URL and complete required authentication. Organization connectors follow the admin provisioning flow. [Custom MCP connectors](https://docs.x.ai/grok/connectors#custom-mcp-connectors), [tunneling and auth](https://docs.x.ai/grok/connectors/custom-mcp-tunneling), [team connector management](https://docs.x.ai/grok/connector-management) |
| Grok Build | Use a local stdio command or remote HTTP. The CLI documents user and project scopes, browser OAuth, configured headers, and `grok mcp doctor`. Its plugins and marketplaces are a separate distribution path for the coding agent. [Grok Build MCP servers](https://docs.x.ai/build/features/mcp-servers), [skills and plugins](https://docs.x.ai/build/features/skills-plugins-marketplaces) |
| Grok Bot | Its desktop Connect apps flow documents Remote HTTPS with optional headers and OAuth client inputs, or a Command that runs on the Bot computer. Verify organization connector policy first. [Connect apps](https://docs.x.ai/grok-bot/computer-and-apps), [enterprise policy](https://docs.x.ai/grok-bot/teams-and-enterprises) |
| xAI API | Remote MCP Tools are available through the SDK and Responses-compatible API over HTTP streaming or SSE. Configure the server URL, tool allowlist, and optional server authorization. The API guide marks `require_approval` and `connector_id` unavailable. Enforce authorization and consequential-write confirmation in your application or server. [Remote MCP Tools and examples](https://docs.x.ai/developers/tools/remote-mcp), [official Python SDK](https://github.com/xai-org/xai-sdk-python) |

For Grok Build, a documented remote development flow is the following. Use a disposable config scope and replace the placeholder with an owned fixture URL. Obtain authorization before registering a live connection.

```sh
grok mcp add --transport http example-catalog https://mcp.example.com/mcp
grok mcp doctor example-catalog
```

Then inspect the loaded tools with `/mcps` and exercise a harmless read. For the chat connector, inspect the server first and test discovery and auth in the actual account after connection is authorized. For the API, keep the xAI client credential distinct from the token sent to the MCP server. [Grok Build MCP docs](https://docs.x.ai/build/features/mcp-servers), [Grok connectors](https://docs.x.ai/grok/connectors), [API tool settings](https://docs.x.ai/developers/tools/remote-mcp)

Start with the shared [MCP SDK samples](mcp-core.md). xAI's docs MCP is a service-specific public example, and the remote tool API guide includes client examples. The public Grok docs checked here leave chat catalog submission, the exact custom OAuth registration contract, and an iframe widget bridge unspecified. Design for tool results and confirm any UI extension in the exact client before advertising it. [xAI docs MCP](https://docs.x.ai/developers/docs-mcp), [MCP extension client matrix](https://modelcontextprotocol.io/extensions/client-matrix)
