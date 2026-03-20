<a id="page-208"></a>
---
url: https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopackFileSystemCache
---

[Configuration](/docs/app/api-reference/config)[next.config.js](/docs/app/api-reference/config/next-config-js)turbopackFileSystemCache

# Turbopack FileSystem Caching

Last updated February 20, 2026

## Usage

Turbopack FileSystem Cache enables Turbopack to reduce work across `next dev` or `next build` commands. When enabled, Turbopack will save and restore data to the `.next` folder between builds, which can greatly speed up subsequent builds and dev sessions.

> **Good to know:** The FileSystem Cache feature is considered stable for development and experimental for production builds

next.config.ts

TypeScript

JavaScriptTypeScript
```
import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      experimental: {
        // Enable filesystem caching for `next dev`
        turbopackFileSystemCacheForDev: true,
        // Enable filesystem caching for `next build`
        turbopackFileSystemCacheForBuild: true,
      },
    }
     
    export default nextConfig
```

## Version Changes

Version| Changes  
---|---  
`v16.1.0`| FileSystem caching is enabled by default for development  
`v16.0.0`| Beta release with separate flags for build and dev  
`v15.5.0`| Persistent caching released as experimental on canary releases  
  
Was this helpful?

supported.

Send
