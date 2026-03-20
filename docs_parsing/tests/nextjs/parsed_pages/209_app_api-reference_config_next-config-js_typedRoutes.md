<a id="page-209"></a>
---
url: https://nextjs.org/docs/app/api-reference/config/next-config-js/typedRoutes
---

[Configuration](/docs/app/api-reference/config)[next.config.js](/docs/app/api-reference/config/next-config-js)typedRoutes

# typedRoutes

Last updated February 20, 2026

> **Note** : This option has been marked as stable, so you should use `typedRoutes` instead of `experimental.typedRoutes`.

Support for [statically typed links](/docs/app/api-reference/config/typescript#statically-typed-links). This feature requires using TypeScript in your project.

next.config.js
```
/** @type {import('next').NextConfig} */
    const nextConfig = {
      typedRoutes: true,
    }
     
    module.exports = nextConfig
```

Was this helpful?

supported.

Send
