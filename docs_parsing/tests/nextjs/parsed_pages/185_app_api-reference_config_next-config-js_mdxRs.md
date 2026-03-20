<a id="page-185"></a>
---
url: https://nextjs.org/docs/app/api-reference/config/next-config-js/mdxRs
---

[Configuration](/docs/app/api-reference/config)[next.config.js](/docs/app/api-reference/config/next-config-js)mdxRs

# mdxRs

This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).

Last updated February 20, 2026

For experimental use with `@next/mdx`. Compiles MDX files using the new Rust compiler.

next.config.js
```
const withMDX = require('@next/mdx')()
     
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      pageExtensions: ['ts', 'tsx', 'mdx'],
      experimental: {
        mdxRs: true,
      },
    }
     
    module.exports = withMDX(nextConfig)
```

Was this helpful?

supported.

Send
