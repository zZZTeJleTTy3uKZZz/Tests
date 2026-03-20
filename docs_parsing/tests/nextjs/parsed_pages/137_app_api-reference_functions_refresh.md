<a id="page-137"></a>
---
url: https://nextjs.org/docs/app/api-reference/functions/refresh
---

[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)refresh

# refresh

Last updated February 20, 2026

`refresh` allows you to refresh the client router from within a [Server Action](/docs/app/getting-started/updating-data).

## Usage

`refresh` can **only** be called from within Server Actions. It cannot be used in Route Handlers, Client Components, or any other context.

## Parameters
```
refresh(): void;
```

## Returns

`refresh` does not return a value.

## Examples

app/actions.ts

TypeScript

JavaScriptTypeScript
```
'use server'
     
    import { refresh } from 'next/cache'
     
    export async function createPost(formData: FormData) {
      const title = formData.get('title')
      const content = formData.get('content')
     
      // Create the post in your database
      const post = await db.post.create({
        data: { title, content },
      })
     
      refresh()
    }
```

### Error when used outside Server Actions

app/api/posts/route.ts

TypeScript

JavaScriptTypeScript
```
import { refresh } from 'next/cache'
     
    export async function POST() {
      // This will throw an error
      refresh()
    }
```

Was this helpful?

supported.

Send
