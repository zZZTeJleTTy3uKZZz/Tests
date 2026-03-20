<a id="page-61"></a>
---
url: https://payloadcms.com/docs/queries/pagination
---

# Pagination

With Pagination you can limit the number of documents returned per page, and get a specific page of results. This is useful for creating paginated lists of documents within your application.

All paginated responses include documents nested within a `docs` array, and return top-level meta data related to pagination such as `totalDocs`, `limit`, `totalPages`, `page`, and more.

**Note:** Collection `find` queries are paginated automatically.

## [Options](/docs/queries/pagination#options)

All Payload APIs support the pagination controls below. With them, you can create paginated lists of documents within your application:

Control |  Default |  Description   
---|---|---  
`limit` |  `10` |  Limits the number of documents returned per page. More details.   
`pagination` |  `true` |  Set to `false` to disable pagination and return all documents.   
`page` |  `1` |  Get a specific page number.   
  
## [Local API](/docs/queries/pagination#local-api)

To specify pagination controls in the [Local API](../local-api/overview), you can use the `limit`, `page`, and `pagination` options in your query:
```
import type { Payload } from 'payload'
    
    
    const getPosts = async (payload: Payload) => {
      const posts = await payload.find({
        collection: 'posts',
        limit: 10,
        page: 2,
      })
    
    
      return posts
    }
```

## [REST API](/docs/queries/pagination#rest-api)

With the [REST API](../rest-api/overview), you can use the pagination controls below as query strings:
```
fetch('https://localhost:3000/api/posts?limit=10&page=2')
      .then((res) => res.json())
      .then((data) => console.log(data))
```

## [Response](/docs/queries/pagination#response)

All paginated responses include documents nested within a `docs` array, and return top-level meta data related to pagination.

The `find` operation includes the following properties in its response:

Property |  Description   
---|---  
`docs` |  Array of documents in the collection   
`totalDocs` |  Total available documents within the collection   
`limit` |  Limit query parameter - defaults to `10`  
`totalPages` |  Total pages available, based upon the `limit` queried for   
`page` |  Current page number   
`pagingCounter` |  `number` of the first doc on the current page   
`hasPrevPage` |  `true/false` if previous page exists   
`hasNextPage` |  `true/false` if next page exists   
`prevPage` |  `number` of previous page, `null` if it doesn't exist   
`nextPage` |  `number` of next page, `null` if it doesn't exist   
  
**Example response:**
```
{
      // Document Array 
      "docs": [
        {
          "title": "Page Title",
          "description": "Some description text",
          "priority": 1,
          "createdAt": "2020-10-17T01:19:29.858Z",
          "updatedAt": "2020-10-17T01:19:29.858Z",
          "id": "5f8a46a1dd05db75c3c64760"
        }
      ],
      // Metadata 
      "totalDocs": 6,
      "limit": 1,
      "totalPages": 6,
      "page": 1,
      "pagingCounter": 1,
      "hasPrevPage": false,
      "hasNextPage": true,
      "prevPage": null,
      "nextPage": 2
    }
```

## [Limit](/docs/queries/pagination#limit)

You can specify a `limit` to restrict the number of documents returned per page.

**Reminder:** By default, any query with `limit: 0` will automatically disable pagination.

#### [Performance benefits](/docs/queries/pagination#performance-benefits)

If you are querying for a specific document and can reliably expect only one document to match, you can set a limit of `1` (or another low number) to reduce the number of database lookups and improve performance.

For example, when querying a document by a unique field such as `slug`, you can set the limit to `1` since you know there will only be one document with that slug.

To do this, set the `limit` option in your query:
```
await payload.find({
      collection: 'posts',
      where: {
        slug: {
          equals: 'post-1',
        },
      },
      limit: 1,
    })
```

## [Disabling pagination](/docs/queries/pagination#disabling-pagination)

Disabling pagination can improve performance by reducing the overhead of pagination calculations and improve query speed.

For `find` operations within the Local API, you can disable pagination to retrieve all documents from a collection by passing `pagination: false` to the `find` local operation.

To do this, set `pagination: false` in your query:
```
import type { Payload } from 'payload'
    
    
    const getPost = async (payload: Payload) => {
      const posts = await payload.find({
        collection: 'posts',
        where: {
          title: { equals: 'My Post' },
        },
        pagination: false,
      })
    
    
      return posts
    }
```

[Next The Admin Panel](/docs/admin/overview)
