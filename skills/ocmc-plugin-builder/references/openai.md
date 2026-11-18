# OpenAI

Sources checked November 18, 2026. OpenAI's older Apps SDK URLs now lead to the Plugins docs. Use the branch for ChatGPT, Codex, or the API. [Plugins developer docs](https://developers.openai.com/plugins)

## ChatGPT

Build a remote MCP server and connect it through ChatGPT Plugins. Use the current test workflow to register a custom server in a permitted workspace. A public HTTPS Streamable HTTP endpoint is the submission path. The documented Secure MCP Tunnel and development tunnels are testing options for private servers. Refresh the connection after descriptor or UI metadata changes, then check actual tool selection, auth, and results. [Build an MCP server](https://developers.openai.com/plugins/build/mcp-server), [connect and test](https://developers.openai.com/plugins/deploy/connect-chatgpt), [quickstart](https://developers.openai.com/plugins/quickstart)

### UI and metadata

Use the standard `App` bridge and `_meta.ui.resourceUri` first. The UI guide covers sample components, wiring, approval-gated input, display modes, files, and app-to-host interaction. Make the initial view tolerate missing arguments before the user approves the tool. [ChatGPT UI and component guide](https://developers.openai.com/plugins/build/chatgpt-ui)

| Placement | OpenAI considerations |
| --- | --- |
| Tool descriptor | Use documented `securitySchemes` and its compatibility mirror as needed. `_meta["openai/outputTemplate"]` is an optional compatibility alias. `_meta["openai/toolInvocation/invoking"]` and `_meta["openai/toolInvocation/invoked"]` set short progress text. Prefer standard `_meta.ui.visibility` for tool exposure. |
| UI resource contents | Use `_meta.ui.csp` for network and asset origins, and `_meta.ui.domain` for the component origin. A published plugin with UI needs its own domain value as documented. ChatGPT compatibility fields include `openai/widgetDescription`, `openai/widgetCSP`, and `openai/widgetDomain` under `_meta`. The legacy CSP field still supplies the `redirect_domains` allowlist for `window.openai.openExternal`. |
| Tool result | Use `content` for text and `structuredContent` for data visible to the model and UI. In ChatGPT, result `_meta` is forwarded to the component. Keep all three free of credentials. |
| Widget runtime | `window.openai` provides compatibility aliases and ChatGPT extensions such as `toolResponseMetadata`, `widgetState`, `setWidgetState`, and file helpers. Use standard bridge methods where they suffice. Feature-detect optional helpers and handle their absence. |

See the [complete ChatGPT metadata and bridge reference](https://developers.openai.com/plugins/reference) and [UI review guidance](https://developers.openai.com/plugins/plugin-guidelines).

### Authorization

For OAuth, apply the [MCP authorization flow](auth.md) and the ChatGPT auth guide. ChatGPT documents CIMD, DCR, and predefined OAuth clients. Take the exact CIMD URL and redirect URI from the connection's settings. Match the issuer settings and supported token endpoint auth methods. The CIMD flow documents `none` with PKCE and `private_key_jwt`. Check provider support before choosing. For a mixed public/private tool set, implement ChatGPT's `securitySchemes` and tool-result `_meta["mcp/www_authenticate"]` linking flow. Verify that the protected handler returns the challenge before any side effect and that the HTTP gateway lets the result reach ChatGPT. [ChatGPT authentication](https://developers.openai.com/plugins/build/auth)

## Codex and OpenAI plugin packages

- Configure Codex MCP using per-user or trusted project `config.toml`, or the `codex mcp` CLI. Verify stdio, remote HTTP, and the documented OAuth or bearer route in the selected Codex client. Keep credentials in the supported host mechanism. [Codex MCP](https://developers.openai.com/codex/mcp)
- For a portable package, use root `plugin.json` and the Agent Plugins `mcp.json` schema. The `@plugin-creator` scaffold uses the supported `.codex-plugin/plugin.json` compatibility layout. Preserve the actual manifest schema and use `extensions.com.openai` for OpenAI-specific settings in the portable layout. Validate the installed package separately from the MCP connection and ChatGPT UI. [Package your plugin](https://developers.openai.com/plugins/build/plugins), [convert a Claude Code plugin](https://developers.openai.com/plugins/guides/submit-claude-plugin)
- Review requested permissions, tool annotations, data handling, public endpoint, UI origins, support and privacy links, and test details before using the submission portal. Use the current package and remote server review rules for the intended distribution. [Plugin guidelines](https://developers.openai.com/plugins/plugin-guidelines), [remote server review](https://developers.openai.com/plugins/deploy/app-review), [submission guide](https://developers.openai.com/plugins/deploy/submission)

## OpenAI API

For a custom application, the Responses API can call a remote MCP server as a tool. Handle allowed tools, access tokens, and approval in the app workflow according to the API guide. If your application needs to render MCP Apps, implement a host bridge and sandbox for that surface. [Responses API connectors and remote MCP](https://developers.openai.com/api/docs/guides/tools-connectors-mcp), [MCP Apps host architecture](https://apps.extensions.modelcontextprotocol.io/api/documents/overview.html)

## Samples and kits

- Start with the `mcp_app_basics_node` example for a compact MCP App. The full sample repo has component gallery, authenticated Python, and more elaborate UI examples. [OpenAI examples](https://github.com/openai/openai-apps-sdk-examples), [MCP App basics example](https://github.com/openai/openai-apps-sdk-examples/tree/main/mcp_app_basics_node)
- OpenAI MCP Kit includes an authenticated Python starter with an Auth0 walkthrough. Check its versions and registration model against current docs before adapting it. [OpenAI MCP Kit](https://github.com/openai/openai-mcpkit), [Auth0 setup in the scaffold](https://github.com/openai/openai-mcpkit/blob/main/python-authenticated-mcp-server-scaffold/README.md#2-configure-auth0-authentication)
- Choose a task that fits the conversation and gives the user a clear result or next action. [What makes a great ChatGPT app](https://developers.openai.com/blog/what-makes-a-great-chatgpt-app)
