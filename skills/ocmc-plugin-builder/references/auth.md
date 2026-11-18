# MCP authorization and Auth0

Sources checked November 18, 2026. Use the auth contract for the exact host, protocol era, and transport. Stdio normally gets secrets from its process environment through the host's configuration. A protected HTTP MCP endpoint uses OAuth when required by the chosen host. Public read-only tools can use anonymous access where appropriate. [Authorization specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization), [MCP authorization tutorial](https://modelcontextprotocol.io/docs/tutorials/security/authorization)

## Wire up the resource server and OAuth client

1. Give the resource server a stable canonical MCP URL. Publish RFC 9728 Protected Resource Metadata there at the appropriate well-known URI. Include `resource` and `authorization_servers`. For a protected HTTP request with no valid token, return `401` and a Bearer `WWW-Authenticate` challenge identifying `resource_metadata`.
2. At the authorization server, publish OAuth authorization server or OIDC discovery metadata. Check the issuer, authorization and token endpoints, PKCE `S256`, supported scopes, token endpoint authentication methods, and client-registration features. With the July 2026 revision, implement issuer binding and verify the OAuth response issuer according to advertised RFC 9207 support.
3. Choose a registration method the client and IdP share. Use a preregistered OAuth client, a hosted Client ID Metadata Document (CIMD), or Dynamic Client Registration (DCR), per the host and IdP. DCR is deprecated in the July 2026 MCP specification and still appears in client integrations. Keep client registrations bound to their issuer and the exact allowed callback.
4. For delegated user access, run authorization code with PKCE and use the canonical `resource` parameter on applicable authorization and token requests. Validate the token cryptographically or use issuer-supported introspection. Check issuer, audience, expiry, scopes, tenant, and object permissions before calling upstream. Use an upstream credential separately scoped to the upstream service.
5. At the protected HTTP boundary, return `403` for insufficient scope or permission. Include the prescribed Bearer challenge for scope step-up when applicable.

The [MCP authorization specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization), [2026 changes](https://blog.modelcontextprotocol.io/posts/2026-07-28/), and [MCP Apps authorization guide](https://apps.extensions.modelcontextprotocol.io/api/documents/authorization.html) cover this sequence. See the individual host guides for registration and callbacks.

## Choose a challenge path for mixed access

| Endpoint profile | Behavior before a protected operation |
| --- | --- |
| Fully protected remote endpoint | Challenge at the HTTP boundary. Discover, connect, and invoke with authorized access. |
| Mixed tools with Claude lazy authentication | Allow discovery and public tools. The protected call must receive the HTTP `401` challenge from the transport handler before the SDK dispatches it. [Claude lazy authentication](https://claude.com/docs/connectors/building/lazy-authentication) |
| Mixed tools with ChatGPT tool-level linking | Declare the tool's `securitySchemes` and publish protected resource metadata. For a protected call that needs linking, return the documented MCP error result with `_meta["mcp/www_authenticate"]` before any side effect. Let it reach the linking UI. [ChatGPT authentication](https://developers.openai.com/plugins/build/auth#triggering-authentication-ui) |
| Host without confirmed mixed access | Use a public read-only endpoint and a separate OAuth-protected endpoint if both access patterns are required. Verify the two connections on that host. |

Use explicit endpoint profiles when deployments need different challenges. Give each protected endpoint its own canonical resource URL, matching discovery metadata and intended token audience. Keep the same authorization rules in the underlying service. A global HTTP challenge in front of a ChatGPT mixed route prevents its tool-result challenge from reaching the host. Test anonymous discovery, anonymous reads, and the denied write path for each profile.

## Configure Auth0 where the host and tenant support it

Use this sequence with placeholders for planning. Before touching a live tenant, obtain authorization for the exact tenant and operation.

1. Register a Custom API as the resource server. Use the canonical MCP resource URI as the identifier and define the minimal scopes. Keep client application registration separate from the Custom API.
2. Enable Auth0's Resource Parameter Compatibility Profile and Include Issuer in Authorization Responses for the intended MCP setup. Confirm the resulting issuer, audience, and metadata using the tenant's actual documented behavior. Legacy examples may use Auth0's `audience` parameter.
3. Register the target MCP client manually or through compatible CIMD or DCR. Auth0 documents manual CIMD and dynamic CIMD, with feature availability depending on the tenant. Configure the target's redirect URLs, token endpoint authentication method, allowed grants, application access, and scopes. Avoid blanket tenant-wide DCR just to make one client connect.
4. Have the MCP resource server publish discovery metadata pointing to the actual issuer. Use issuer-scoped JWKS or introspection and verify the accepted audiences and scopes. Test one authorized request and each denial path with a test user in an authorized environment. Keep tenant identifiers, client secrets, and tokens out of example logs and shared config.

- [Auth0 authorization setup](https://auth0.com/ai/docs/mcp/get-started/authorization-for-your-mcp-server), [resource parameter guide](https://auth0.com/ai/docs/mcp/guides/resource-param-compatibility-profile), [client registration](https://auth0.com/ai/docs/mcp/guides/registering-your-mcp-client-application)
- [Auth0 sample apps](https://auth0.com/ai/docs/mcp/sample-apps), [Auth0 Inspector walkthrough](https://auth0.com/ai/docs/mcp/guides/test-your-mcp-server-with-mcp-inspector)
- [OpenAI MCP Kit Auth0 Python scaffold](https://github.com/openai/openai-mcpkit/blob/main/python-authenticated-mcp-server-scaffold/README.md#2-configure-auth0-authentication). Use it as a runnable reference for its stated setup. Reconcile older registration settings with the current host and tenant guides.

## Verify authorization end to end

Use a local fixture issuer and disposable keys to test discovery and token verification for missing, expired, wrong-issuer, wrong-audience, and under-scoped tokens. Keep a synthetic clock and accounts when expiry and data isolation matter. In an authorized provider test tenant, also exercise login and consent, the exact redirect, token exchange, one valid scoped call, denial, and reauthorization. Record fixture evidence and provider test evidence with the actual client, transport, and response. Redact codes, tokens, and secrets.
