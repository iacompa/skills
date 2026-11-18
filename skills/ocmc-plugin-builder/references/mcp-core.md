# MCP core, apps, and testing

Sources checked November 18, 2026. Confirm the protocol era, matching SDK major, and connected client capabilities before selecting features.

## Protocol and starter selection

- Start with the MCP specification's tools, resources, and prompts. Use stable tool names, tight JSON Schema, explicit error results, and output that a human can understand in chat. Validate the actual effect in the handler. Tool annotations such as `readOnlyHint` and `destructiveHint` are UX hints. [MCP specification](https://modelcontextprotocol.io/specification/2026-07-28), [tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)
- For network access use Streamable HTTP over HTTPS in production. For same-machine integrations use stdio when the client supports it. Keep stdio protocol output on stdout and diagnostic logs on stderr. Check the client's legacy HTTP+SSE support only when an existing integration requires it. [Transport specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports)
- The July 2026 revision uses stateless requests, optional `server/discover`, and HTTP `Mcp-Method` and `Mcp-Name` routing headers where applicable. Older clients use `initialize` and may use MCP sessions. Use the SDK's compatibility path and test the version the target uses. [2026-07-28 release](https://blog.modelcontextprotocol.io/posts/2026-07-28/), [TypeScript protocol-era migration](https://ts.sdk.modelcontextprotocol.io/v2/migration/support-2026-07-28)
- Choose the SDK that fits the repo. Review official samples for the installed major. TypeScript v1 examples use `@modelcontextprotocol/sdk` and v2 splits the implementation into packages including `@modelcontextprotocol/server`, `@modelcontextprotocol/client`, and platform adapters. Match MCP Apps SDK peer dependencies before building. [TypeScript SDK and examples](https://github.com/modelcontextprotocol/typescript-sdk), [Python SDK and examples](https://github.com/modelcontextprotocol/python-sdk), [MCP Apps SDK](https://apps.extensions.modelcontextprotocol.io/api/)

## MCP Apps UI contract

| Placement | What to declare |
| --- | --- |
| Capability exchange | Check `io.modelcontextprotocol/ui` for the host and version. Verify how the actual host exposes the extension. |
| Tool definition | Set `_meta.ui.resourceUri` to the `ui://` resource. Set `_meta.ui.visibility` when exposure should differ for the model and the app. |
| UI resource | Return the HTML from `resources/read` with `text/html;profile=mcp-app`. Set relevant resource `_meta.ui` fields for CSP, origin, permissions, and border preferences. Keep permitted origins narrow. |
| Tool result | Return a useful text summary in `content`. Add schema-matching `structuredContent` for data. Use result metadata only for documented needs. Don’t place secrets in any widget payload. |

See the [MCP Apps specification](https://github.com/modelcontextprotocol/ext-apps/blob/main/specification/2026-01-26/apps.mdx) and [UI resource API](https://apps.extensions.modelcontextprotocol.io/api/interfaces/server-helpers.McpUiAppResourceConfig.html).

Use `App` from `@modelcontextprotocol/ext-apps` in the sandboxed view. Register input, result, and host-context event handlers before connecting. Let the bridge handle the `ui/initialize` handshake and use its methods for tool calls, context, and links according to host support. Keep write approval, object authorization, and retries in the server's workflow even when the app initiates the request. [MCP Apps overview](https://apps.extensions.modelcontextprotocol.io/api/documents/overview.html), [App class reference](https://apps.extensions.modelcontextprotocol.io/api/classes/app.App.html)

For a new UI, start from the official quickstart or `basic-server-vanillajs`. Use `basic-host` to exercise the view's lifecycle locally and the same server in each target to verify sandbox behavior. The repo also contains a Claude Code plugin with scaffold, migrate, and add-UI skills. [Quickstart](https://github.com/modelcontextprotocol/ext-apps/blob/main/docs/quickstart.md), [examples](https://github.com/modelcontextprotocol/ext-apps/tree/main/examples), [basic host](https://github.com/modelcontextprotocol/ext-apps/tree/main/examples/basic-host)

## Confirm and retry writes

When a write needs confirmation, bind the decision to the authenticated actor and exact proposed parameters. Use an authenticated approval flow the service can verify. For example, prepare a pending operation, show its effects to the user, and let them confirm or cancel. Expire outstanding approvals. Before commit, recheck ownership, scope, parameters, and approval state. Store the local effect and its receipt atomically under the idempotency key. For upstream writes, reuse a durable operation key with the provider's idempotency mechanism and reconcile through status when available. If the outcome stays ambiguous, leave the operation pending for reconciliation. Test a direct commit without approval, an expired proposal, a different account, and a repeated commit. Expect no effect in each denial case and one receipt for a successful operation.

## Inspect the protocol and then exercise the host

Use a reviewed Inspector release compatible with your Node version and target protocol. For reproducible checks, install it with an exact version and a reviewed lockfile, then run the local binary. If the binary is absent, document the missing dependency and prepare the pinned local installation. The guide documents web, CLI, and terminal modes. Bind the web UI to loopback and keep the Inspector's API token enabled. Review where it stores OAuth secrets before any authorized authenticated test. [Inspector guide](https://modelcontextprotocol.io/docs/tools/inspector), [release notes and Node compatibility](https://github.com/modelcontextprotocol/inspector/releases)

For an owned fixture, use the local binary and match the script, endpoint, tool name, and input to the fixture. These flags apply to the Inspector 2.16.0 example.

```sh
./node_modules/.bin/mcp-inspector --cli node ./dist/stdio.js --method tools/list
./node_modules/.bin/mcp-inspector --cli http://127.0.0.1:3001/mcp --transport http --method tools/list
./node_modules/.bin/mcp-inspector --cli http://127.0.0.1:3001/mcp --transport http --method tools/call --tool-name catalog_search --tool-arg query=canvas
```

1. Connect, check protocol-era behavior, list the tools, and exercise one valid and one invalid input. Read a resource and retrieve a prompt if either is in scope.
2. Check missing authentication, expiry, wrong audience, and insufficient scope when relevant. Check denied and repeated writes against a disposable fixture. See [MCP authorization](auth.md).
3. If the tool has a widget, confirm that its resource resolves, the bridge receives the result, and CSP, sizing, theme, and tool actions work. Disable the UI capability in a test client to inspect the fallback. The official reference host can help isolate widget bugs. [MCP Apps testing guide](https://github.com/modelcontextprotocol/ext-apps/blob/main/docs/testing-mcp-apps.md)
4. Repeat the targeted flow in the actual client. Capture client and SDK versions, transport, auth mode, reproduction steps, observed result, and blocked or skipped cases. An Inspector result establishes protocol behavior in Inspector.
5. Use a disposable test project or profile. Set a stop time before starting. On completion, denial, timeout, or cancellation, stop new calls and close connections and processes started for the fixture. Remove only the test entries and temporary resources created by the run. Test cancellation at an interrupted setup or discovery step if it can leave state behind.

## Choose distribution independently

An [Agent Skill](https://agentskills.io/specification) bundles instructions and references. An [Agent Plugins](https://agent-plugins.org/) package uses a root `plugin.json`, optional `mcp.json`, and `skills/` for clients that implement that standard. A connector registration points a specific host at a service. Claude Code native plugins and Claude Desktop MCPB packages have their own formats. Reuse tool contracts and skills across those forms, then validate each manifest, auth mechanism, and install path against the intended client.
