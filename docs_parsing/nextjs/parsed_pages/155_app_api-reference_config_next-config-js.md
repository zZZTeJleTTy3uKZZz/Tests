<a id="page-155"></a>
---
url: https://nextjs.org/docs/app/api-reference/config/next-config-js
---

[API Reference](/docs/app/api-reference)[Configuration](/docs/app/api-reference/config)next.config.js

# next.config.js

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

### [experimental.adapterPathConfigure a custom adapter for Next.js to hook into the build process with modifyConfig and onBuildComplete callbacks.](/docs/app/api-reference/config/next-config-js/adapterPath)### [allowedDevOriginsUse `allowedDevOrigins` to configure additional origins that can request the dev server.](/docs/app/api-reference/config/next-config-js/allowedDevOrigins)### [appDirEnable the App Router to use layouts, streaming, and more.](/docs/app/api-reference/config/next-config-js/appDir)### [assetPrefixLearn how to use the assetPrefix config option to configure your CDN.](/docs/app/api-reference/config/next-config-js/assetPrefix)### [authInterruptsLearn how to enable the experimental `authInterrupts` configuration option to use `forbidden` and `unauthorized`.](/docs/app/api-reference/config/next-config-js/authInterrupts)### [basePathUse `basePath` to deploy a Next.js application under a sub-path of a domain.](/docs/app/api-reference/config/next-config-js/basePath)### [browserDebugInfoInTerminalForward browser console logs and errors to your terminal during development.](/docs/app/api-reference/config/next-config-js/browserDebugInfoInTerminal)### [cacheComponentsLearn how to enable the cacheComponents flag in Next.js.](/docs/app/api-reference/config/next-config-js/cacheComponents)### [cacheHandlersConfigure custom cache handlers for use cache directives in Next.js.](/docs/app/api-reference/config/next-config-js/cacheHandlers)### [cacheLifeLearn how to set up cacheLife configurations in Next.js.](/docs/app/api-reference/config/next-config-js/cacheLife)### [compressNext.js provides gzip compression to compress rendered content and static files, it only works with the server target. Learn more about it here.](/docs/app/api-reference/config/next-config-js/compress)### [crossOriginUse the `crossOrigin` option to add a crossOrigin tag on the `script` tags generated by `next/script`.](/docs/app/api-reference/config/next-config-js/crossOrigin)### [cssChunkingUse the `cssChunking` option to control how CSS files are chunked in your Next.js application.](/docs/app/api-reference/config/next-config-js/cssChunking)### [deploymentIdConfigure a deployment identifier used for version skew protection and cache busting.](/docs/app/api-reference/config/next-config-js/deploymentId)### [devIndicatorsConfiguration options for the on-screen indicator that gives context about the current route you're viewing during development.](/docs/app/api-reference/config/next-config-js/devIndicators)### [distDirSet a custom build directory to use instead of the default .next directory.](/docs/app/api-reference/config/next-config-js/distDir)### [envLearn to add and access environment variables in your Next.js application at build time.](/docs/app/api-reference/config/next-config-js/env)### [expireTimeCustomize stale-while-revalidate expire time for ISR enabled pages.](/docs/app/api-reference/config/next-config-js/expireTime)### [exportPathMapCustomize the pages that will be exported as HTML files when using `next export`.](/docs/app/api-reference/config/next-config-js/exportPathMap)### [generateBuildIdConfigure the build id, which is used to identify the current build in which your application is being served.](/docs/app/api-reference/config/next-config-js/generateBuildId)### [generateEtagsNext.js will generate etags for every page by default. Learn more about how to disable etag generation here.](/docs/app/api-reference/config/next-config-js/generateEtags)### [headersAdd custom HTTP headers to your Next.js app.](/docs/app/api-reference/config/next-config-js/headers)### [htmlLimitedBotsSpecify a list of user agents that should receive blocking metadata.](/docs/app/api-reference/config/next-config-js/htmlLimitedBots)### [httpAgentOptionsNext.js will automatically use HTTP Keep-Alive by default. Learn more about how to disable HTTP Keep-Alive here.](/docs/app/api-reference/config/next-config-js/httpAgentOptions)### [imagesCustom configuration for the next/image loader](/docs/app/api-reference/config/next-config-js/images)### [cacheHandlerConfigure the Next.js cache used for storing and revalidating data to use any external service like Redis, Memcached, or others.](/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath)### [inlineCssEnable inline CSS support.](/docs/app/api-reference/config/next-config-js/inlineCss)### [isolatedDevBuildUse isolated build outputs for development server to prevent conflicts with production builds.](/docs/app/api-reference/config/next-config-js/isolatedDevBuild)### [loggingConfigure how data fetches are logged to the console when running Next.js in development mode.](/docs/app/api-reference/config/next-config-js/logging)### [mdxRsUse the new Rust compiler to compile MDX files in the App Router.](/docs/app/api-reference/config/next-config-js/mdxRs)### [onDemandEntriesConfigure how Next.js will dispose and keep in memory pages created in development.](/docs/app/api-reference/config/next-config-js/onDemandEntries)### [optimizePackageImportsAPI Reference for optimizePackageImports Next.js Config Option](/docs/app/api-reference/config/next-config-js/optimizePackageImports)### [outputNext.js automatically traces which files are needed by each page to allow for easy deployment of your application. Learn how it works here.](/docs/app/api-reference/config/next-config-js/output)### [pageExtensionsExtend the default page extensions used by Next.js when resolving pages in the Pages Router.](/docs/app/api-reference/config/next-config-js/pageExtensions)### [poweredByHeaderNext.js will add the `x-powered-by` header by default. Learn to opt-out of it here.](/docs/app/api-reference/config/next-config-js/poweredByHeader)### [productionBrowserSourceMapsEnables browser source map generation during the production build.](/docs/app/api-reference/config/next-config-js/productionBrowserSourceMaps)### [proxyClientMaxBodySizeConfigure the maximum request body size when using proxy.](/docs/app/api-reference/config/next-config-js/proxyClientMaxBodySize)### [reactCompilerEnable the React Compiler to automatically optimize component rendering.](/docs/app/api-reference/config/next-config-js/reactCompiler)### [reactMaxHeadersLengthThe maximum length of the headers that are emitted by React and added to the response.](/docs/app/api-reference/config/next-config-js/reactMaxHeadersLength)### [reactStrictModeThe complete Next.js runtime is now Strict Mode-compliant, learn how to opt-in](/docs/app/api-reference/config/next-config-js/reactStrictMode)### [redirectsAdd redirects to your Next.js app.](/docs/app/api-reference/config/next-config-js/redirects)### [rewritesAdd rewrites to your Next.js app.](/docs/app/api-reference/config/next-config-js/rewrites)### [sassOptionsConfigure Sass options.](/docs/app/api-reference/config/next-config-js/sassOptions)### [serverActionsConfigure Server Actions behavior in your Next.js application.](/docs/app/api-reference/config/next-config-js/serverActions)### [serverComponentsHmrCacheConfigure whether fetch responses in Server Components are cached across HMR refresh requests.](/docs/app/api-reference/config/next-config-js/serverComponentsHmrCache)### [serverExternalPackagesOpt-out specific dependencies from the Server Components bundling and use native Node.js `require`.](/docs/app/api-reference/config/next-config-js/serverExternalPackages)### [staleTimesLearn how to override the invalidation time of the Client Router Cache.](/docs/app/api-reference/config/next-config-js/staleTimes)### [staticGeneration*Learn how to configure static generation in your Next.js application.](/docs/app/api-reference/config/next-config-js/staticGeneration)### [taintEnable tainting Objects and Values.](/docs/app/api-reference/config/next-config-js/taint)### [trailingSlashConfigure Next.js pages to resolve with or without a trailing slash.](/docs/app/api-reference/config/next-config-js/trailingSlash)### [transpilePackagesAutomatically transpile and bundle dependencies from local packages (like monorepos) or from external dependencies (`node_modules`).](/docs/app/api-reference/config/next-config-js/transpilePackages)### [turbopackConfigure Next.js with Turbopack-specific options](/docs/app/api-reference/config/next-config-js/turbopack)### [turbopackFileSystemCacheLearn how to enable FileSystem Caching for Turbopack builds](/docs/app/api-reference/config/next-config-js/turbopackFileSystemCache)### [typedRoutesEnable support for statically typed links.](/docs/app/api-reference/config/next-config-js/typedRoutes)### [typescriptConfigure how Next.js handles TypeScript errors during production builds and specify a custom tsconfig file.](/docs/app/api-reference/config/next-config-js/typescript)### [urlImportsConfigure Next.js to allow importing modules from external URLs.](/docs/app/api-reference/config/next-config-js/urlImports)### [useLightningcssEnable experimental support for Lightning CSS.](/docs/app/api-reference/config/next-config-js/useLightningcss)### [viewTransitionEnable ViewTransition API from React in App Router](/docs/app/api-reference/config/next-config-js/viewTransition)### [webpackLearn how to customize the webpack config used by Next.js](/docs/app/api-reference/config/next-config-js/webpack)### [webVitalsAttributionLearn how to use the webVitalsAttribution option to pinpoint the source of Web Vitals issues.](/docs/app/api-reference/config/next-config-js/webVitalsAttribution)

Was this helpful?

supported.

Send
