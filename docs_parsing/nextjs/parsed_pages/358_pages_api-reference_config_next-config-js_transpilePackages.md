<a id="page-358"></a>
---
url: https://nextjs.org/docs/pages/api-reference/config/next-config-js/transpilePackages
---

[Configuration](/docs/pages/api-reference/config)[next.config.js Options](/docs/pages/api-reference/config/next-config-js)transpilePackages

# transpilePackages

Last updated February 20, 2026

Next.js can automatically transpile and bundle dependencies from local packages (like monorepos) or from external dependencies (`node_modules`). This replaces the `next-transpile-modules` package.

next.config.js
```
/** @type {import('next').NextConfig} */
    const nextConfig = {
      transpilePackages: ['package-name'],
    }
     
    module.exports = nextConfig
```

## Version History

Version| Changes  
---|---  
`v13.0.0`| `transpilePackages` added.  
  
Was this helpful?

supported.

Send
