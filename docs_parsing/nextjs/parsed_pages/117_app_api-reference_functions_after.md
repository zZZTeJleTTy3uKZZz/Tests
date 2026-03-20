<a id="page-117"></a>
---
url: https://nextjs.org/docs/app/api-reference/functions/after
---

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)after

# after

Last updated February 20, 2026

`after` allows you to schedule work to be executed after a response (or prerender) is finished. This is useful for tasks and other side effects that should not block the response, such as logging and analytics.

It can be used in [Server Components](/docs/app/getting-started/server-and-client-components) (including [`generateMetadata`](/docs/app/api-reference/functions/generate-metadata)), [Server Functions](/docs/app/getting-started/updating-data), [Route Handlers](/docs/app/api-reference/file-conventions/route), and [Proxy](/docs/app/api-reference/file-conventions/proxy).

The function accepts a callback that will be executed after the response (or prerender) is finished:

app/layout.tsx

TypeScript

JavaScriptTypeScript
```
import { after } from 'next/server'
    // Custom logging function
    import { log } from '@/app/utils'
     
    export default function Layout({ children }: { children: React.ReactNode }) {
      after(() => {
        // Execute after the layout is rendered and sent to the user
        log()
      })
      return <>{children}</>
    }
```

> **Good to know:** `after` is not a [Dynamic API](/docs/app/guides/caching#dynamic-rendering) and calling it does not cause a route to become dynamic. If it's used within a static page, the callback will execute at build time, or whenever a page is revalidated.

## Reference

### Parameters

  * A callback function which will be executed after the response (or prerender) is finished.



### Duration

`after` will run for the platform's default or configured max duration of your route. If your platform supports it, you can configure the timeout limit using the [`maxDuration`](/docs/app/api-reference/file-conventions/route-segment-config#maxduration) route segment config.

## Good to know

  * `after` will be executed even if the response didn't complete successfully. Including when an error is thrown or when `notFound` or `redirect` is called.
  * You can use React `cache` to deduplicate functions called inside `after`.
  * `after` can be nested inside other `after` calls, for example, you can create utility functions that wrap `after` calls to add additional functionality.



## Examples

### With request APIs

Whether you can use request APIs like [`cookies`](/docs/app/api-reference/functions/cookies) and [`headers`](/docs/app/api-reference/functions/headers) inside `after` depends on where `after` is called from.

#### In Route Handlers and Server Functions

You can call `cookies` and `headers` directly inside the `after` callback when used in [Route Handlers](/docs/app/api-reference/file-conventions/route) and [Server Functions](/docs/app/getting-started/updating-data). This is useful for logging activity after a mutation or API request. For example:

app/api/route.ts

TypeScript

JavaScriptTypeScript
```
import { after } from 'next/server'
    import { logUserAction } from '@/app/utils'
     
    export async function POST(request: Request) {
      // Perform mutation
      // ...
     
      // Log user activity for analytics
     
      return new Response(JSON.stringify({ status: 'success' }), {
        status: 200,
        headers: { 'Content-Type': 'application/json' },
      })
    }
```

#### In Server Components (pages and layouts)

[Server Components](/docs/app/getting-started/server-and-client-components) (including pages, layouts, and `generateMetadata`) **cannot** use `cookies`, `headers`, or other [Dynamic APIs](/docs/app/guides/caching#dynamic-rendering) inside `after`. This is because Next.js needs to know which part of the component tree accesses request data to support [Partial Prerendering](/docs/app/glossary#partial-prerendering-ppr) and [Cache Components](/docs/app/getting-started/cache-components), but `after` runs after React's rendering lifecycle.

If you need request data inside an `after` callback in a Server Component, read it beforehand and pass the values in:

app/page.tsx

TypeScript

JavaScriptTypeScript
```
import { after } from 'next/server'
    import { cookies, headers } from 'next/headers'
    import { logUserAction } from '@/app/utils'
     
    export default async function Page() {
      // Read request data before `after` — this is allowed
      // These calls will be read during the component's rendering lifecycle
     
        // Use the values read above
        logUserAction({ sessionCookie, userAgent })
      })
     
      return <h1>My Page</h1>
    }
```

Calling `cookies()` or `headers()` inside the `after` callback in a Server Component will throw a runtime error.

#### With Cache Components

When using [Cache Components](/docs/app/getting-started/cache-components), components that access request data like `cookies` or `headers` must be wrapped in [`<Suspense>`](https://react.dev/reference/react/Suspense) so the rest of the page can be prerendered into a static shell.

You can combine this pattern with `after` by reading request data in a dynamic component and passing it into `after`:

app/page.tsx

TypeScript

JavaScriptTypeScript
```
import { Suspense } from 'react'
    import { after } from 'next/server'
    import { cookies } from 'next/headers'
    import { logUserAction } from '@/app/utils'
     
    export default function Page() {
      return (
        <>
          <h1>Part of the static shell</h1>
          <Suspense fallback={<p>Loading...</p>}>
            <DynamicContent />
          </Suspense>
        </>
      )
    }
     
    async function DynamicContent() {
     
      // Schedule work after the response is sent
     
      return <p>Your session: {sessionCookie}</p>
    }
```

In this example, `<h1>` and the `<Suspense>` fallback are included in the static shell. `DynamicContent` reads the cookie during rendering and passes it into `after` via closure. Since `cookies()` is called _outside_ the `after` callback (during the component's render), this works correctly.

## Platform Support

Deployment Option| Supported  
---|---  
[Node.js server](/docs/app/getting-started/deploying#nodejs-server)| Yes  
[Docker container](/docs/app/getting-started/deploying#docker)| Yes  
[Static export](/docs/app/getting-started/deploying#static-export)| No  
[Adapters](/docs/app/getting-started/deploying#adapters)| Platform-specific  
  
Learn how to [configure `after`](/docs/app/guides/self-hosting#after) when self-hosting Next.js.

Reference: supporting `after` for serverless platforms

Using `after` in a serverless context requires waiting for asynchronous tasks to finish after the response has been sent. In Next.js and Vercel, this is achieved using a primitive called `waitUntil(promise)`, which extends the lifetime of a serverless invocation until all promises passed to [`waitUntil`](https://vercel.com/docs/functions/functions-api-reference#waituntil) have settled.

If you want your users to be able to run `after`, you will have to provide your implementation of `waitUntil` that behaves in an analogous way.

When `after` is called, Next.js will access `waitUntil` like this:
```

```

Which means that `globalThis[Symbol.for('@next/request-context')]` is expected to contain an object like this:
```

```

Here is an example of the implementation.
```

```

## Version History

Version| Changes  
---|---  
`v15.1.0`| `after` became stable.  
`v15.0.0-rc`| `unstable_after` introduced.  
  
Was this helpful?

supported.

Send
