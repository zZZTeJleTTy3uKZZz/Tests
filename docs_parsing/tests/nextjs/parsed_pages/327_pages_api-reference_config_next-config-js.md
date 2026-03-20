<a id="page-327"></a>
---
url: https://nextjs.org/docs/pages/api-reference/config/next-config-js
---

[API Reference](/docs/pages/api-reference)[Configuration](/docs/pages/api-reference/config)next.config.js Options

# next.config.js Options

Last updated February 20, 2026

Next.js can be configured through a `next.config.js` file in the root of your project directory (for example, by `package.json`) with a default export.

next.config.js
```
// @ts-check
     
    /** @type {import('next').NextConfig} */
    const nextConfig = {
      /* config options here */
    }
     
    module.exports = nextConfig
```

## ECMAScript Modules

`next.config.js` is a regular Node.js module, not a JSON file. It gets used by the Next.js server and build phases, and it's not included in the browser build.

If you need [ECMAScript modules](https://nodejs.org/api/esm.html), you can use `next.config.mjs`:

next.config.mjs
```
// @ts-check
     
    /**
     * @type {import('next').NextConfig}
     */
    const nextConfig = {
      /* config options here */
    }
     
    export default nextConfig
```

> **Good to know** : `next.config` with the `.cjs` or `.cts` extensions are currently **not** supported.

## Configuration as a Function

You can also use a function:

next.config.mjs
```
// @ts-check
     
    export default (phase, { defaultConfig }) => {
      /**
       * @type {import('next').NextConfig}
       */
      const nextConfig = {
        /* config options here */
      }
      return nextConfig
    }
```

### Async Configuration

Since Next.js 12.1.0, you can use an async function:

next.config.js
```
// @ts-check
     
    module.exports = async (phase, { defaultConfig }) => {
      /**
       * @type {import('next').NextConfig}
       */
      const nextConfig = {
        /* config options here */
      }
      return nextConfig
    }
```

### Phase

`phase` is the current context in which the configuration is loaded. You can see the [available phases](https://github.com/vercel/next.js/blob/5e6b008b561caf2710ab7be63320a3d549474a5b/packages/next/shared/lib/constants.ts#L19-L23). Phases can be imported from `next/constants`:

next.config.js
```
// @ts-check
     
    const { PHASE_DEVELOPMENT_SERVER } = require('next/constants')
     
    module.exports = (phase, { defaultConfig }) => {
      if (phase === PHASE_DEVELOPMENT_SERVER) {
        return {
          /* development only config options here */
        }
      }
     
      return {
        /* config options for all phases except development here */
      }
    }
```

## TypeScript

If you are using TypeScript in your project, you can use `next.config.ts` to use TypeScript in your configuration:

next.config.ts
```
import type { NextConfig } from 'next'
     
    const nextConfig: NextConfig = {
      /* config options here */
    }
     
    export default nextConfig
```

The commented lines are the place where you can put the configs allowed by `next.config.js`, which are [defined in this file](https://github.com/vercel/next.js/blob/canary/packages/next/src/server/config-shared.ts).

However, none of the configs are required, and it's not necessary to understand what each config does. Instead, search for the features you need to enable or modify in this section and they will show you what to do.

> Avoid using new JavaScript features not available in your target Node.js version. `next.config.js` will not be parsed by Webpack or Babel.

This page documents all the available configuration options:

## Unit Testing (experimental)

Starting in Next.js 15.1, the `next/experimental/testing/server` package contains utilities to help unit test `next.config.js` files.

The `unstable_getResponseFromNextConfig` function runs the [`headers`](/docs/app/api-reference/config/next-config-js/headers), [`redirects`](/docs/app/api-reference/config/next-config-js/redirects), and [`rewrites`](/docs/app/api-reference/config/next-config-js/rewrites) functions from `next.config.js` with the provided request information and returns `NextResponse` with the results of the routing.

> The response from `unstable_getResponseFromNextConfig` only considers `next.config.js` fields and does not consider proxy or filesystem routes, so the result in production may be different than the unit test.
```
import {
      getRedirectUrl,
      unstable_getResponseFromNextConfig,
    } from 'next/experimental/testing/server'
     
    const response = await unstable_getResponseFromNextConfig({
      url: 'https://nextjs.org/test',
      nextConfig: {
        async redirects() {
          return [{ source: '/test', destination: '/test2', permanent: false }]
        },
      },
    })
    expect(response.status).toEqual(307)
    expect(getRedirectUrl(response)).toEqual('https://nextjs.org/test2')
```

### [experimental.adapterPathConfigure a custom adapter for Next.js to hook into the build process with modifyConfig and buildComplete callbacks.](/docs/pages/api-reference/config/next-config-js/adapterPath)### [allowedDevOriginsUse `allowedDevOrigins` to configure additional origins that can request the dev server.](/docs/pages/api-reference/config/next-config-js/allowedDevOrigins)### [assetPrefixLearn how to use the assetPrefix config option to configure your CDN.](/docs/pages/api-reference/config/next-config-js/assetPrefix)### [basePathUse `basePath` to deploy a Next.js application under a sub-path of a domain.](/docs/pages/api-reference/config/next-config-js/basePath)### [bundlePagesRouterDependenciesEnable automatic dependency bundling for Pages Router](/docs/pages/api-reference/config/next-config-js/bundlePagesRouterDependencies)### [compressNext.js provides gzip compression to compress rendered content and static files, it only works with the server target. Learn more about it here.](/docs/pages/api-reference/config/next-config-js/compress)### [crossOriginUse the `crossOrigin` option to add a crossOrigin tag on the `script` tags generated by `next/script` and `next/head`.](/docs/pages/api-reference/config/next-config-js/crossOrigin)### [deploymentIdConfigure a deployment identifier used for version skew protection and cache busting.](/docs/pages/api-reference/config/next-config-js/deploymentId)### [devIndicatorsOptimized pages include an indicator to let you know if it's being statically optimized. You can opt-out of it here.](/docs/pages/api-reference/config/next-config-js/devIndicators)### [distDirSet a custom build directory to use instead of the default .next directory.](/docs/pages/api-reference/config/next-config-js/distDir)### [envLearn to add and access environment variables in your Next.js application at build time.](/docs/pages/api-reference/config/next-config-js/env)### [exportPathMapCustomize the pages that will be exported as HTML files when using `next export`.](/docs/pages/api-reference/config/next-config-js/exportPathMap)### [generateBuildIdConfigure the build id, which is used to identify the current build in which your application is being served.](/docs/pages/api-reference/config/next-config-js/generateBuildId)### [generateEtagsNext.js will generate etags for every page by default. Learn more about how to disable etag generation here.](/docs/pages/api-reference/config/next-config-js/generateEtags)### [headersAdd custom HTTP headers to your Next.js app.](/docs/pages/api-reference/config/next-config-js/headers)### [httpAgentOptionsNext.js will automatically use HTTP Keep-Alive by default. Learn more about how to disable HTTP Keep-Alive here.](/docs/pages/api-reference/config/next-config-js/httpAgentOptions)### [imagesCustom configuration for the next/image loader](/docs/pages/api-reference/config/next-config-js/images)### [isolatedDevBuildUse isolated directories for development builds to prevent conflicts with production builds.](/docs/pages/api-reference/config/next-config-js/isolatedDevBuild)### [onDemandEntriesConfigure how Next.js will dispose and keep in memory pages created in development.](/docs/pages/api-reference/config/next-config-js/onDemandEntries)### [optimizePackageImportsAPI Reference for optimizePackageImports Next.js Config Option](/docs/pages/api-reference/config/next-config-js/optimizePackageImports)### [outputNext.js automatically traces which files are needed by each page to allow for easy deployment of your application. Learn how it works here.](/docs/pages/api-reference/config/next-config-js/output)### [pageExtensionsExtend the default page extensions used by Next.js when resolving pages in the Pages Router.](/docs/pages/api-reference/config/next-config-js/pageExtensions)### [poweredByHeaderNext.js will add the `x-powered-by` header by default. Learn to opt-out of it here.](/docs/pages/api-reference/config/next-config-js/poweredByHeader)### [productionBrowserSourceMapsEnables browser source map generation during the production build.](/docs/pages/api-reference/config/next-config-js/productionBrowserSourceMaps)### [experimental.proxyClientMaxBodySizeConfigure the maximum request body size when using proxy.](/docs/pages/api-reference/config/next-config-js/proxyClientMaxBodySize)### [reactStrictModeThe complete Next.js runtime is now Strict Mode-compliant, learn how to opt-in](/docs/pages/api-reference/config/next-config-js/reactStrictMode)### [redirectsAdd redirects to your Next.js app.](/docs/pages/api-reference/config/next-config-js/redirects)### [rewritesAdd rewrites to your Next.js app.](/docs/pages/api-reference/config/next-config-js/rewrites)### [serverExternalPackagesOpt-out specific dependencies from the dependency bundling enabled by `bundlePagesRouterDependencies`.](/docs/pages/api-reference/config/next-config-js/serverExternalPackages)### [trailingSlashConfigure Next.js pages to resolve with or without a trailing slash.](/docs/pages/api-reference/config/next-config-js/trailingSlash)### [transpilePackagesAutomatically transpile and bundle dependencies from local packages (like monorepos) or from external dependencies (`node_modules`).](/docs/pages/api-reference/config/next-config-js/transpilePackages)### [turbopackConfigure Next.js with Turbopack-specific options](/docs/pages/api-reference/config/next-config-js/turbopack)### [typescriptNext.js reports TypeScript errors by default. Learn to opt-out of this behavior here.](/docs/pages/api-reference/config/next-config-js/typescript)### [urlImportsConfigure Next.js to allow importing modules from external URLs.](/docs/pages/api-reference/config/next-config-js/urlImports)### [useLightningcssEnable experimental support for Lightning CSS.](/docs/pages/api-reference/config/next-config-js/useLightningcss)### [webpackLearn how to customize the webpack config used by Next.js](/docs/pages/api-reference/config/next-config-js/webpack)### [webVitalsAttributionLearn how to use the webVitalsAttribution option to pinpoint the source of Web Vitals issues.](/docs/pages/api-reference/config/next-config-js/webVitalsAttribution)

Was this helpful?

supported.

Send
