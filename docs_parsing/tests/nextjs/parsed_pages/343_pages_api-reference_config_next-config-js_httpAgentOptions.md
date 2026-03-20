<a id="page-343"></a>
---
url: https://nextjs.org/docs/pages/api-reference/config/next-config-js/httpAgentOptions
---

[Configuration](/docs/pages/api-reference/config)[next.config.js Options](/docs/pages/api-reference/config/next-config-js)httpAgentOptions

# httpAgentOptions

Last updated February 20, 2026

In Node.js versions prior to 18, Next.js automatically polyfills `fetch()` with [undici](/docs/architecture/supported-browsers#polyfills) and enables [HTTP Keep-Alive](https://developer.mozilla.org/docs/Web/HTTP/Headers/Keep-Alive) by default.

To disable HTTP Keep-Alive for all `fetch()` calls on the server-side, open `next.config.js` and add the `httpAgentOptions` config:

next.config.js
```
module.exports = {
      httpAgentOptions: {
        keepAlive: false,
      },
    }
```

Was this helpful?

supported.

Send
