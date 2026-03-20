<a id="page-23"></a>
---
url: https://payloadcms.com/docs/fields/collapsible
---

# Collapsible Field

The Collapsible Field is presentational-only and only affects the Admin Panel. By using it, you can place fields within a nice layout component that can be collapsed / expanded.

![Shows a Collapsible field in the Payload Admin Panel](https://payloadcms.com/images/docs/fields/collapsible.png)

Admin Panel screenshot of a Collapsible field

To add a Collapsible Field, set the `type` to `collapsible` in your [Field Config](./overview):
```
import type { Field } from 'payload'
    
    
    export const MyCollapsibleField: Field = {
      // ...
      type: 'collapsible',
      fields: [
        // ...
      ],
    }
```

## [Config Options](/docs/fields/collapsible#config-options)

Option |  Description   
---|---  
`**label**` * |  A label to render within the header of the collapsible component. This can be a string, function or react component. Function/components receive `({ data, path })` as args.   
`**fields**` * |  Array of field types to nest within this Collapsible.   
`**admin**` |  Admin-specific configuration. More details.   
`**custom**` |  Extension point for adding custom data (e.g. for plugins)   
  
_* An asterisk denotes that a property is required._

## [ Admin Options](/docs/fields/collapsible#admin-options)

To customize the appearance and behavior of the Collapsible Field in the [Admin Panel](../admin/overview), you can use the `admin` option:
```
import type { Field } from 'payload'
    
    
    export const MyCollapsibleField: Field = {
      // ...
      admin: {
        
        // ...
      },
    }
```

The Collapsible Field inherits all of the default admin options from the base [Field Admin Config](./overview#admin-options), plus the following additional options:

Option |  Description   
---|---  
`**initCollapsed**` |  Set the initial collapsed state   
  
## [Example](/docs/fields/collapsible#example)
```
import type { CollectionConfig } from 'payload'
    
    
    export const ExampleCollection: CollectionConfig = {
      slug: 'example-collection',
      fields: [
        {
          label: ({ data }) => data?.title || 'Untitled',
          type: 'collapsible', // required
          fields: [
            // required
            {
              name: 'title',
              type: 'text',
              required: true,
            },
            {
              name: 'someTextField',
              type: 'text',
              required: true,
            },
          ],
        },
      ],
    }
```

[Next Date Field](/docs/fields/date)
