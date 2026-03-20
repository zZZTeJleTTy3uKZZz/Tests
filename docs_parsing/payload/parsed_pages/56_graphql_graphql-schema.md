<a id="page-56"></a>
---
url: https://payloadcms.com/docs/graphql/graphql-schema
---

# GraphQL Schema

In Payload the schema is controlled by your collections and globals. All you need to do is run the generate command and the entire schema will be created for you.

## [Schema generation script](/docs/graphql/graphql-schema#schema-generation-script)

Install `@payloadcms/graphql` as a dev dependency:
```
pnpm add @payloadcms/graphql -D
```

Run the following command to generate the schema:
```
pnpm payload-graphql generate:schema
```

## [Custom Field Schemas](/docs/graphql/graphql-schema#custom-field-schemas)

For `array`, `block`, `group` and named `tab` fields, you can generate top level reusable interfaces. The following group field config:
```
{
      type: 'group',
      name: 'meta',
      interfaceName: 'SharedMeta', 
      fields: [
        {
          name: 'title',
          type: 'text',
        },
        {
          name: 'description',
          type: 'text',
        },
      ],
    }
```

will generate:
```
// A top level reusable type will be generated
    type SharedMeta {
      title: String
      description: String
    }
    
    
    // And will be referenced inside the generated schema
    type Collection1 {
      // ...other fields
      meta: SharedMeta
    }
```

The above example outputs all your definitions to a file relative from your Payload config as `./graphql/schema.graphql`. By default, the file will be output to your current working directory as `schema.graphql`.

### [Adding an npm script](/docs/graphql/graphql-schema#adding-an-npm-script)

**Important**

Payload needs to be able to find your config to generate your GraphQL schema.

Payload will automatically try and locate your config, but might not always be able to find it. For example, if you are working in a `/src` directory or similar, you need to tell Payload where to find your config manually by using an environment variable.

If this applies to you, create an npm script to make generating types easier:
```
// package.json
    
    
    {
      "scripts": {
        "generate:graphQLSchema": "cross-env PAYLOAD_CONFIG_PATH=src/payload.config.ts payload-graphql generate:schema"
      }
    }
```

Now you can run `pnpm generate:graphQLSchema` to easily generate your schema.

[Next Querying your Documents](/docs/queries/overview)
