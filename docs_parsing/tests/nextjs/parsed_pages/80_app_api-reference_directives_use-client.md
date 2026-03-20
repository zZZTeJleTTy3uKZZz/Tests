<a id="page-80"></a>
---
url: https://nextjs.org/docs/app/api-reference/directives/use-client
---

[API Reference](/docs/app/api-reference)[Directives](/docs/app/api-reference/directives)use client

# use client

Last updated February 20, 2026

The `'use client'` directive declares an entry point for the components to be rendered on the **client side** and should be used when creating interactive user interfaces (UI) that require client-side JavaScript capabilities, such as state management, event handling, and access to browser APIs. This is a React feature.

> **Good to know:**
> 
> You do not need to add the `'use client'` directive to every file that contains Client Components. You only need to add it to the files whose components you want to render directly within Server Components. The `'use client'` directive defines the client-server [boundary](https://nextjs.org/docs/app/building-your-application/rendering#network-boundary), and the components exported from such a file serve as entry points to the client.

## Usage

To declare an entry point for the Client Components, add the `'use client'` directive **at the top of the file** , before any imports:

app/components/counter.tsx

TypeScript

JavaScriptTypeScript
```
import { useState } from 'react'
     
    export default function Counter() {
      const [count, setCount] = useState(0)
     
      return (
        <div>
          <p>Count: {count}</p>
          <button onClick={() => setCount(count + 1)}>Increment</button>
        </div>
      )
    }
```

When using the `'use client'` directive, the props of the Client Components must be [serializable](https://react.dev/reference/rsc/use-client#serializable-types). This means the props need to be in a format that React can serialize when sending data from the server to the client.

app/components/counter.tsx

TypeScript

JavaScriptTypeScript
```
'use client'
     
    export default function Counter({
    }) {
      return (
        <div>
          <button onClick={onClick}>Increment</button>
        </div>
      )
    }
```

## Nesting Client Components within Server Components

Combining Server and Client Components allows you to build applications that are both performant and interactive:

  1. **Server Components** : Use for static content, data fetching, and SEO-friendly elements.
  2. **Client Components** : Use for interactive elements that require state, effects, or browser APIs.
  3. **Component composition** : Nest Client Components within Server Components as needed for a clear separation of server and client logic.



In the following example:

  * `Header` is a Server Component handling static content.
  * `Counter` is a Client Component enabling interactivity within the page.



app/page.tsx

TypeScript

JavaScriptTypeScript
```
import Header from './header'
     
    export default function Page() {
      return (
        <div>
          <Header />
        </div>
      )
    }
```

## Reference

See the [React documentation](https://react.dev/reference/rsc/use-client) for more information on `'use client'`.

Was this helpful?

supported.

Send
