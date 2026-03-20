<a id="page-360"></a>
---
url: https://nextjs.org/docs/pages/api-reference/config/next-config-js/typescript
---

[Configuration](/docs/pages/api-reference/config)[next.config.js Options](/docs/pages/api-reference/config/next-config-js)typescript

# typescript

Last updated February 20, 2026

Configure TypeScript behavior with the `typescript` option in `next.config.js`:

next.config.js
```
module.exports = {
      typescript: {
        ignoreBuildErrors: false,
        tsconfigPath: 'tsconfig.json',
      },
    }
```

## Options

Option| Type| Default| Description  
---|---|---|---  
`ignoreBuildErrors`| `boolean`| `false`| Allow production builds to complete even with TypeScript errors.  
`tsconfigPath`| `string`| `'tsconfig.json'`| Path to a custom `tsconfig.json` file.  
  
## `ignoreBuildErrors`

Next.js fails your **production build** (`next build`) when TypeScript errors are present in your project.

If you'd like Next.js to dangerously produce production code even when your application has errors, you can disable the built-in type checking step.

If disabled, be sure you are running type checks as part of your build or deploy process, otherwise this can be very dangerous.

next.config.js
```
module.exports = {
      typescript: {
        // !! WARN !!
        // Dangerously allow production builds to successfully complete even if
        // your project has type errors.
        // !! WARN !!
        ignoreBuildErrors: true,
      },
    }
```

## `tsconfigPath`

Use a different TypeScript configuration file for builds or tooling:

next.config.js
```
module.exports = {
      typescript: {
        tsconfigPath: 'tsconfig.build.json',
      },
    }
```

See the [TypeScript configuration](/docs/app/api-reference/config/typescript#custom-tsconfig-path) page for more details.

Was this helpful?

supported.

Send
