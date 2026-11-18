# Meta Muse

Sources checked November 18, 2026. Identify whether the target is Muse's personal agent, the Muse Code coding agent, Meta AI's connector program, or a Muse model in a custom application. [Meta developer overview](https://dev.meta.ai/docs/overview)

## Muse personal agent

- For a reviewed directory listing, use the Muse Connector Platform. Meta's guidelines accept MCP or API documentation. Prepare the supported use cases, endpoint, auth and scopes, data handling, privacy and support URLs, error and rate-limit behavior, tool schemas, demo, and dedicated test access as required. Follow the portal's secure intake path when authorized. [Connector Platform](https://platform.muse.ai/), [guidelines and submission criteria](https://platform.muse.ai/docs), [developer terms](https://platform.muse.ai/terms)
- Document the effect of each tool as Read, Write, or Sensitive Write. Classify a mixed tool as Write and require fresh user approval for sensitive writes. Preserve workflow state through account linking. If the design needs a confirmation handoff, confirm during onboarding that the handoff is supported, then let Muse resume, finish the task, and show the result. Check the status of an ambiguous write before retrying it. Use the classification in the review materials. The public guidelines describe wire annotations as forthcoming. [Connector guidelines and Cedar Stays example](https://platform.muse.ai/docs)
- The public guide discusses OAuth, API keys, and integration credentials. It leaves the exact redirect, client registration, and MCP revision contract unspecified. Ask for or verify the portal's actual requirements before choosing a shared registration method. The personal Custom Connector documented by Meta is a separate flow mediated by Muse. Its public instructions leave direct arbitrary MCP URL registration unspecified. [Connector guidelines](https://platform.muse.ai/docs), [personal Custom Connectors](https://www.meta.com/help/superintelligence/1687253048996149/)

Use ordinary tool results for the personal agent. The sources checked for this guide do not document a Muse widget iframe, MCP Apps rendering contract, or `window.openai` equivalent. Use the official Cedar Stays example for review behavior and the shared [MCP SDK samples](mcp-core.md) for a server scaffold. [Connector guidelines](https://platform.muse.ai/docs), [MCP extension client matrix](https://modelcontextprotocol.io/extensions/client-matrix)

## Muse Code

Muse Code documents local stdio and remote Streamable HTTP MCP via `mcp_servers` in its settings. Set the configuration scope and use `/mcp` to inspect the connection and tool list. A required server can fail startup. Set `mode` to `optional` when the workflow can proceed without that server. Check the installed version for trusted project `.mcp.json` and CLI registration commands. [Configuration](https://dev.meta.ai/docs/muse-code/configuration), [MCP servers](https://dev.meta.ai/docs/muse-code/extending#mcp), [changelog](https://dev.meta.ai/docs/muse-code/changelog)

```json
{
  "mcp_servers": {
    "example-catalog": {
      "transport": "streamable_http",
      "url": "https://mcp.example.com/mcp"
    }
  }
}
```

For remote OAuth, Muse Code documents browser and headless sign-in, token refresh, `muse mcp login example-catalog`, and `muse mcp logout example-catalog`. Match the real client registration against the chosen provider. The documented opt-out for automatic client registration is `mcp_oauth_dynamic_client_registration: false`. [Muse Code remote MCP sign-in](https://dev.meta.ai/docs/muse-code/extending#mcp-oauth)

For a skill, use a supported skill root such as project `.agents/skills/<name>/SKILL.md` and check it with `muse skills validate <skill-directory>`. Meta's Wearables toolkit demonstrates native plugin packaging across coding agents, including Muse Code. Meta's Agentic Tools repo contains a first-party MCP and skills example for its Social Technologies developer platform. Use those examples for their documented targets. [Muse Code skills and plugins](https://dev.meta.ai/docs/muse-code/extending#skills), [Meta Wearables toolkit](https://github.com/meta/meta-wearables-webapp), [Meta Agentic Tools](https://github.com/meta/agentic-tools)

## Other Meta surfaces

- The Meta AI Connectors developer preview describes guided or MCP onboarding and OAuth account linking for selected developers. Check its eligibility and contract when Meta AI is the target. [Meta AI Connectors](https://dev.meta.ai/products/connectors)
- The Meta Model API documents application-managed function calling. If building a Muse-powered host, use an MCP client in the application where needed, and own the consent, transport, and output presentation. [Model API tool calling](https://dev.meta.ai/docs/tool-calling)
