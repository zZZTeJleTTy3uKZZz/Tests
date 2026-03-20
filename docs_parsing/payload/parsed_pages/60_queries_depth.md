<a id="page-60"></a>
---
url: https://payloadcms.com/docs/queries/depth
---

# Depth

Documents in Payload can have relationships to other Documents. This is true for both [Collections](../configuration/collections) as well as [Globals](../configuration/globals). When you query a Document, you can specify the depth at which to populate any of its related Documents either as full objects, or only their IDs.

Since Documents can be infinitely nested or recursively related, it's important to be able to control how deep your API populates. Depth can impact the performance of your queries by affecting the load on the database and the size of the response.

For example, when you specify a `depth` of `0`, the API response might look like this:
```
{
      "id": "5ae8f9bde69e394e717c8832",
      "title": "This is a great post",
      "author": "5f7dd05cd50d4005f8bcab17"
    }
```

But with a `depth` of `1`, the response might look like this:
```
{
      "id": "5ae8f9bde69e394e717c8832",
      "title": "This is a great post",
      "author": {
        "id": "5f7dd05cd50d4005f8bcab17",
        "name": "John Doe"
      }
    }
```

**Important:** Depth has no effect in the [GraphQL API](../graphql/overview), because there, depth is based on the shape of your queries.

## [Local API](/docs/queries/depth#local-api)

To specify depth in the [Local API](../local-api/overview), you can use the `depth` option in your query:
```
import type { Payload } from 'payload'
    
    
    const getPosts = async (payload: Payload) => {
      const posts = await payload.find({
        collection: 'posts',
        depth: 2,
      })
    
    
      return posts
    }
```

**Reminder:** This is the same for [Globals](../configuration/globals) using the `findGlobal` operation.

## [REST API](/docs/queries/depth#rest-api)

To specify depth in the [REST API](../rest-api/overview), you can use the `depth` parameter in your query:
```
fetch('https://localhost:3000/api/posts?depth=2')
      .then((res) => res.json())
      .then((data) => console.log(data))
```

**Reminder:** This is the same for [Globals](../configuration/globals) using the `/api/globals` endpoint.

## [Default Depth](/docs/queries/depth#default-depth)

If no depth is specified in the request, Payload will use its default depth for all requests. By default, this is set to `2`.

To change the default depth on the application level, you can use the `defaultDepth` option in your root Payload config:
```
import { buildConfig } from 'payload/config'
    
    
    export default buildConfig({
      // ...
      defaultDepth: 1,
      // ...
    })
```

## [Max Depth](/docs/queries/depth#max-depth)

Fields like the [Relationship Field](../fields/relationship) or the [Upload Field](../fields/upload) can also set a maximum depth. If exceeded, this will limit the population depth regardless of what the depth might be on the request.

To set a max depth for a field, use the `maxDepth` property in your field configuration:
```
{
      slug: 'posts',
      fields: [
        {
          name: 'author',
          type: 'relationship',
          relationTo: 'users',
          maxDepth: 2,
        }
      ]
    }
```

[Next Pagination](/docs/queries/pagination)
