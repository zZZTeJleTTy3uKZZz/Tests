<a id="page-198"></a>
---
url: https://nextjs.org/docs/app/api-reference/config/next-config-js/sassOptions
---

[Configuration](/docs/app/api-reference/config)[next.config.js](/docs/app/api-reference/config/next-config-js)sassOptions

# sassOptions

Last updated February 20, 2026

`sassOptions` allow you to configure the Sass compiler.

next.config.ts

TypeScript

JavaScriptTypeScript
```
import type { NextConfig } from 'next'
     
    const sassOptions = {
      additionalData: `
        $var: red;
      `,
    }
     
    const nextConfig: NextConfig = {
      sassOptions: {
        ...sassOptions,
        implementation: 'sass-embedded',
      },
    }
     
    export default nextConfig
```

> **Good to know:**
> 
>   * `sassOptions` are not typed outside of `implementation` because Next.js does not maintain the other possible properties.
>   * The `functions` property for defining custom Sass functions is only supported with webpack. When using Turbopack, custom Sass functions are not available because Turbopack's Rust-based architecture cannot directly execute JavaScript functions passed through this option.
> 


Was this helpful?

supported.

Send
