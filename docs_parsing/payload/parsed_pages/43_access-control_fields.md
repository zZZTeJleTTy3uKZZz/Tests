<a id="page-43"></a>
---
url: https://payloadcms.com/docs/access-control/fields
---

# Field-level Access Control

Field Access Control is [Access Control](../access-control/overview) used to restrict access to specific [Fields](../fields/overview) within a Document.

To add Access Control to a Field, use the `access` property in your [Field Config](../fields/overview):
```
import type { Field } from 'payload'
    
    
    export const FieldWithAccessControl: Field = {
      // ...
      access: {
        
        // ...
      },
    }
```

**Note:** Field Access Control does not support returning [Query](../queries/overview) constraints like [Collection Access Control](./collections) does.

## [Config Options](/docs/access-control/fields#config-options)

Access Control is specific to the operation of the request.

To add Access Control to a Field, use the `access` property in the [Field Config](../fields/overview):
```
import type { CollectionConfig } from 'payload';
    
    
    export const Posts: CollectionConfig = {
      slug: 'posts',
      fields: [
        {
          name: 'title',
          type: 'text',
          access: {
            create: ({ req: { user } }) => { ... },
            read: ({ req: { user } }) => { ... },
            update: ({ req: { user } }) => { ... },
          },
        };
      ],
    };
```

The following options are available:

Function |  Purpose   
---|---  
`**create**` |  Allows or denies the ability to set a field's value when creating a new document. More details.   
`**read**` |  Allows or denies the ability to read a field's value. More details.   
`**update**` |  Allows or denies the ability to update a field's value More details.   
  
### [Create](/docs/access-control/fields#create)

Returns a boolean which allows or denies the ability to set a field's value when creating a new document. If `false` is returned, any passed values will be discarded.

**Available argument properties:**

Option |  Description   
---|---  
`**req**` |  The [Request](https://developer.mozilla.org/en-US/docs/Web/API/Request) object containing the currently authenticated `user`  
`**data**` |  The full data passed to create the document.   
`**siblingData**` |  Immediately adjacent field data passed to create the document.   
  
### [Read](/docs/access-control/fields#read)

Returns a boolean which allows or denies the ability to read a field's value. If `false`, the entire property is omitted from the resulting document.

**Available argument properties:**

Option |  Description   
---|---  
`**req**` |  The [Request](https://developer.mozilla.org/en-US/docs/Web/API/Request) object containing the currently authenticated `user`  
`**id**` |  `id` of the document being read   
`**doc**` |  The full document data.   
`**siblingData**` |  Immediately adjacent field data of the document being read.   
  
### [Update](/docs/access-control/fields#update)

Returns a boolean which allows or denies the ability to update a field's value. If `false` is returned, any passed values will be discarded.

If `false` is returned and you attempt to update the field's value, the operation will **not** throw an error however the field will be omitted from the update operation and the value will remain unchanged.

**Available argument properties:**

Option |  Description   
---|---  
`**req**` |  The [Request](https://developer.mozilla.org/en-US/docs/Web/API/Request) object containing the currently authenticated `user`  
`**id**` |  `id` of the document being updated   
`**data**` |  The full data passed to update the document.   
`**siblingData**` |  Immediately adjacent field data passed to update the document with.   
`**doc**` |  The full document data, before the update is applied.   
  
[Next Hooks Overview](/docs/hooks/overview)
