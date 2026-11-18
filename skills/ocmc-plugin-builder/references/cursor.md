# Cursor

Public documentation checked November 18, 2026.

## Choose the integration

| Goal | Cursor route |
| --- | --- |
| Connect tools or data in an editor workspace | Add a server in Customize or use `.cursor/mcp.json` for the project and `~/.cursor/mcp.json` for the user. Cursor documents stdio, Streamable HTTP, and SSE. [MCP configuration](https://cursor.com/docs/mcp) |
| Render an interactive result in Cursor IDE chat | Build a standard MCP App. Cursor introduced app rendering in 2.6. [MCP Apps in Cursor](https://cursor.com/docs/mcp#mcp-apps), [2.6 changelog](https://cursor.com/changelog/2-6) |
| Use tools in the terminal | Cursor CLI reads the editor’s MCP configuration. Test tool discovery with `agent mcp list` and `agent mcp list-tools <identifier>`. [CLI MCP reference](https://cursor.com/docs/cli/mcp) |
| Connect a Cloud Agent | Configure the server in the MCP menu on cursor.com/agents or have a team admin manage shared servers. Custom servers use HTTP or stdio. Stdio runs inside the cloud VM. Cloud OAuth is per-user and has its own sign-in. [Cloud Agent MCP tools](https://cursor.com/docs/cloud-agent/capabilities#mcp-tools), [Cursor sign-in FAQ](https://cursor.com/docs/mcp#faq) |
| Distribute a skill or MCP bundle | Install a standalone Agent Skill in `.cursor/skills/` or `~/.cursor/skills/`. Bundle skills and MCP servers in an Agent Plugin, or use a Cursor Plugin for Cursor-specific rules, subagents, commands, hooks, or variables. [Skill directories](https://cursor.com/docs/skills#skill-directories), [Plugin author guide](https://cursor.com/docs/plugins) |

Cursor's published capability list includes tools, prompts, resources, roots, elicitation, and MCP Apps. Keep UI rendering in CLI, Agents Window, and Cloud Agent surfaces unverified until tested on the requested surface. [Cursor capabilities](https://cursor.com/docs/mcp#protocol-and-extension-support)

## Configure and test a server

Use Streamable HTTP for a new remote server and stdio for a project-local process. This example assumes a built local server at `dist/server.js` and a separately running loopback HTTP fixture. Include the entries you intend to test. [Cursor configuration and interpolation](https://cursor.com/docs/mcp#using-mcpjson)

```json
{
  "mcpServers": {
    "catalog-local": {
      "type": "stdio",
      "command": "node",
      "args": ["${workspaceFolder}/dist/server.js"]
    },
    "catalog-http-fixture": {
      "url": "http://127.0.0.1:3000/mcp"
    }
  }
}
```

Use `${env:NAME}` for local environment interpolation in supported fields. For stdio, Cursor also documents `envFile`. Extensions can register a server programmatically with `vscode.cursor.mcp.registerServer()` when an editor extension is part of the design. [Configuration interpolation](https://cursor.com/docs/mcp#config-interpolation), [Cursor extension API](https://cursor.com/docs/extension-api)

## OAuth and Auth0

Cursor documents authorization code with PKCE, resource discovery via OAuth protected resource metadata (RFC 9728), and resource indicators (RFC 8707). For DCR it registers as a public client. When the provider requires a preregistered client, use the remote server's `auth.CLIENT_ID`. Add `auth.CLIENT_SECRET` only when the provider requires a confidential client. Cursor can discover scopes when omitted or request the explicit `auth.scopes`. For a CIMD-only provider, verify compatibility before choosing that route. [Cursor authentication](https://cursor.com/docs/mcp#authentication), [Static OAuth configuration](https://cursor.com/docs/mcp#static-oauth-for-remote-servers)

Register the exact redirect URIs allowed by the target surface. Use `http://localhost:8787/callback` for a static desktop integration and `https://www.cursor.com/agents/mcp/oauth/callback` for web and Cursor Agents. With DCR, Cursor desktop registers both and can send the web callback. Treat the chosen IdP's client and redirect policy as a prerequisite. [Cursor callback documentation](https://cursor.com/docs/mcp#static-redirect-url)

For Auth0, follow its MCP resource server and client registration guides, then apply the Cursor callback and registration mode to the tenant configuration. Check Auth0's Resource Parameter Compatibility Profile if the token audience differs from the MCP resource. This static client example uses an environment-provided public client ID and an illustrative scope. [Auth0 for MCP](https://auth0.com/ai/docs/mcp/overview), [Resource and audience troubleshooting](https://support.auth0.com/center/s/article/mcp-audience-error-with-auth0), [Auth0 Inspector guide](https://auth0.com/ai/docs/mcp/guides/test-your-mcp-server-with-mcp-inspector)

```json
{
  "mcpServers": {
    "catalog-oauth": {
      "url": "https://mcp.example.com/mcp",
      "auth": {
        "CLIENT_ID": "${env:CATALOG_MCP_CLIENT_ID}",
        "scopes": ["catalog:read"]
      }
    }
  }
}
```

## Widget metadata and bridge

Set tool `_meta.ui.resourceUri` to the registered `ui://` HTML resource and serve it with MIME type `text/html;profile=mcp-app`. Bundle the view's scripts and styles. Use the MCP Apps JSON-RPC bridge, for example the `App` class in `@modelcontextprotocol/ext-apps`, to consume tool results and request host actions. Keep ChatGPT-specific `window.openai` calls in the ChatGPT adapter. Use the extension spec for resource `_meta.ui.csp` and permissions. Return useful standard MCP content for tool-only clients. [MCP Apps overview and metadata](https://modelcontextprotocol.io/extensions/apps/overview), [Official SDK and examples](https://github.com/modelcontextprotocol/ext-apps), [ChatGPT UI extensions](https://developers.openai.com/plugins/build/chatgpt-ui)

Cursor IDE 3.30 documents app-initiated calls to visible tools on the app's own server without an approval prompt. Enforce permissions and required confirmation server-side before performing writes. Test render, follow-up tool calls, and plain output separately. [Cursor IDE release notes](https://prod.cursor.com/docs/release-notes/ide), [React example](https://github.com/modelcontextprotocol/ext-apps/blob/main/examples/basic-server-react/README.md)

## Package and distribute

- Start with Cursor's advanced MCP starter or inspect its official plugins. For an Agent Plugin, use a root `plugin.json` and the standard manifest schema. For a Cursor Plugin, use `.cursor-plugin/plugin.json` and an optional `mcp.json` at the plugin root. [Cursor plugin template](https://github.com/cursor/plugin-template), [Official Cursor plugins](https://github.com/cursor/plugins), [Agent Plugins manifest](https://agent-plugins.org/plugin-authors/manifest), [Cursor manifest reference](https://cursor.com/docs/reference/plugins)
- For bundled stdio paths, Cursor expands `${CURSOR_PLUGIN_ROOT}` and `${CLAUDE_PLUGIN_ROOT}` in `command`, `args`, `env` values, and `cwd`. Use Cursor-specific configuration when a package relies on the standard `${PLUGIN_ROOT}` or `${PLUGIN_DATA}` substitutions. Native plugin variables use the manifest's `variables` schema and `${VAR}` placeholders. Set values through the authorized dashboard flow. [Cursor plugin MCP configuration](https://cursor.com/docs/reference/plugins#mcp-servers), [Variables](https://cursor.com/docs/reference/plugins#variables)
- If local imports are permitted, place the plugin folder under `~/.cursor/plugins/local/`, reload Cursor, and check Customize. Enterprise admins control local imports. Use the template's `node scripts/validate-template.mjs` when working from that template. [Local plugin testing](https://cursor.com/docs/plugins#test-plugins-locally), [Template validation](https://github.com/cursor/plugin-template)
- For distribution, use a private team marketplace when appropriate. A public marketplace submission uses an open-source Git repository, a valid manifest and component paths, a README, local test evidence, and manual review. If authorized to submit, follow the checklist and publish form. For a standalone MCP install link, encode only credential-free configuration. [Submission checklist](https://cursor.com/docs/reference/plugins#submission-checklist), [Publish form](https://cursor.com/marketplace/publish), [MCP install links](https://cursor.com/docs/mcp/install-links)

## Verification order

1. Run MCP Inspector against the fixture. Verify discovery, a valid call, invalid input, and any associated resource output. [MCP Inspector guide](https://modelcontextprotocol.io/docs/tools/inspector)
2. Install the fixture in the intended Cursor surface. Confirm the server and tools in Customize, invoke the read-only test tool in chat, and inspect **Output → MCP Logs** on failure. Use the CLI discovery commands when that surface matters. For Cloud Agent, verify reachability from the VM and per-user sign-in independently of the IDE plugin test. [Cursor troubleshooting](https://cursor.com/docs/mcp#faq), [CLI MCP reference](https://cursor.com/docs/cli/mcp), [Cloud Agent MCP tools](https://cursor.com/docs/cloud-agent/capabilities#mcp-tools)
3. For OAuth, exercise sign-in, consent, expiry or reconnect, and a denied scope on the authorized target. Record the Cursor build, surface, transport, registration mode, and render result.
