<a id="page-98"></a>
---
url: https://nextjs.org/docs/app/api-reference/file-conventions/mdx-components
---

[API Reference](/docs/app/api-reference)[File-system conventions](/docs/app/api-reference/file-conventions)mdx-components.js

# mdx-components.js

Last updated February 20, 2026

The `mdx-components.js|tsx` file is **required** to use [`@next/mdx` with App Router](/docs/app/guides/mdx) and will not work without it. Additionally, you can use it to [customize styles](/docs/app/guides/mdx#using-custom-styles-and-components).

Use the file `mdx-components.tsx` (or `.js`) in the root of your project to define MDX Components. For example, at the same level as `pages` or `app`, or inside `src` if applicable.

mdx-components.tsx

TypeScript

JavaScriptTypeScript
```
import type { MDXComponents } from 'mdx/types'
     
    const components: MDXComponents = {}
     
    export function useMDXComponents(): MDXComponents {
      return components
    }
```

## Exports

### `useMDXComponents` function

The file must export a single function named `useMDXComponents`. This function does not accept any arguments.

mdx-components.tsx

TypeScript

JavaScriptTypeScript
```
import type { MDXComponents } from 'mdx/types'
     
    const components: MDXComponents = {}
     
    export function useMDXComponents(): MDXComponents {
      return components
    }
```

## Version History

Version| Changes  
---|---  
`v13.1.2`| MDX Components added  
  
## Learn more about MDX Components

### [MDXLearn how to configure MDX and use it in your Next.js apps.](/docs/app/guides/mdx)

Was this helpful?

supported.

Send
