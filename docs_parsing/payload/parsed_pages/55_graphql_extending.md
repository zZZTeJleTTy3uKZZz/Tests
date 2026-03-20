<a id="page-55"></a>
---
url: https://payloadcms.com/docs/graphql/extending
---

# Adding your own Queries and Mutations

You can add your own GraphQL queries and mutations to Payload, making use of all the types that Payload has defined for you.

To do so, add your queries and mutations to the main Payload Config as follows:

Config Path |  Description   
---|---  
`graphQL.queries` |  Function that returns an object containing keys to custom GraphQL queries   
`graphQL.mutations` |  Function that returns an object containing keys to custom GraphQL mutations   
  
The above properties each receive a function that is defined with the following arguments:

`**GraphQL**`

This is Payload's GraphQL dependency. You should not install your own copy of GraphQL as a dependency due to underlying restrictions based on how GraphQL works. Instead, you can use the Payload-provided copy via this argument.

`**payload**`

This is a copy of the currently running Payload instance, which provides you with existing GraphQL types for all of your Collections and Globals - among other things.

## [Return value](/docs/graphql/extending#return-value)

Both `graphQL.queries` and `graphQL.mutations` functions should return an object with properties equal to your newly written GraphQL queries and mutations.

## [Example](/docs/graphql/extending#example)

`payload.config.js`:
```
import { buildConfig } from 'payload'
    import myCustomQueryResolver from './graphQL/resolvers/myCustomQueryResolver'
    
    
    export default buildConfig({
      graphQL: {
        queries: (GraphQL, payload) => {
          return {
            MyCustomQuery: {
              type: new GraphQL.GraphQLObjectType({
                name: 'MyCustomQuery',
                fields: {
                  text: {
                    type: GraphQL.GraphQLString,
                  },
                  someNumberField: {
                    type: GraphQL.GraphQLFloat,
                  },
                },
              }),
              args: {
                argNameHere: {
                  type: new GraphQL.GraphQLNonNull(GraphQLString),
                },
              },
              resolve: myCustomQueryResolver,
            },
          }
        },
      },
    })
```

## [Resolver function](/docs/graphql/extending#resolver-function)

In your resolver, make sure you set `depth: 0` if you're returning data directly from the Local API so that GraphQL can correctly resolve queries to nested values such as relationship data.

Your function will receive four arguments you can make use of:

Example
```
;async (obj, args, context, info) => {}
```

`**obj**`

The previous object. Not very often used and usually discarded.

`**args**`

The available arguments from your query or mutation will be available to you here, these must be configured via the custom operation first.

`**context**`

An object containing the `req` and `res` objects that will provide you with the `payload`, `user` instances and more, like any other Payload API handler.

`**info**`

Contextual information about the currently running GraphQL operation. You can get schema information from this as well as contextual information about where this resolver function is being run.

## [Types](/docs/graphql/extending#types)

We've exposed a few types and utilities to help you extend the API further. Payload uses the GraphQL.js package for which you can view the full list of available types in the [official documentation](https://graphql.org/graphql-js/type/).

`**GraphQLJSON**` & `**GraphQLJSONObject**`
```
import { GraphQLJSON, GraphQLJSONObject } from '@payloadcms/graphql/types'
```

`**GraphQL**`

You can directly import the GraphQL package used by Payload, most useful for typing.
```
import { GraphQL } from '@payloadcms/graphql/types'
```

For queries, mutations and handlers make sure you use the `GraphQL` and `payload` instances provided via arguments.

`**buildPaginatedListType**`

This is a utility function that allows you to build a new GraphQL type for a paginated result similar to the Payload's generated schema. It takes in two arguments, the first for the name of this new schema type and the second for the GraphQL type to be used in the docs parameter.

Example
```
import { buildPaginatedListType } from '@payloadcms/graphql/types'
    
    
    export const getMyPosts = (GraphQL, payload) => {
      return {
        args: {},
        resolve: Resolver,
        // The name of your new type has to be unique
        type: buildPaginatedListType(
          'AuthorPosts',
          payload.collections['posts'].graphQL?.type,
        ),
      }
    }
```

`**payload.collections.slug.graphQL**`

If you want to extend more of the provided API then the `graphQL` object on your collection slug will contain additional types to help you re-use code for types, mutations and queries.
```
graphQL?: {
      type: GraphQLObjectType
      paginatedType: GraphQLObjectType
      JWT: GraphQLObjectType
      versionType: GraphQLObjectType
      whereInputType: GraphQLInputObjectType
      mutationInputType: GraphQLNonNull<any>
      updateMutationInputType: GraphQLNonNull<any>
    }
```

## [Best practices](/docs/graphql/extending#best-practices)

There are a few ways to structure your code, we recommend using a dedicated `graphql` directory so you can keep all of your logic in one place. You have total freedom of how you want to structure this but a common pattern is to group functions by type and with their resolver.

Example
```
src/graphql
    ---- queries/
         index.ts
        -- myCustomQuery/
           index.ts
           resolver.ts
    
    
    ---- mutations/
```

[Next GraphQL Schema](/docs/graphql/graphql-schema)
