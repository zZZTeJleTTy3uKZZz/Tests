<a id="page-41"></a>
---
url: https://payloadcms.com/docs/access-control/collections
---

# Collection Access Control

Collection Access Control is [Access Control](../access-control/overview) used to restrict access to Documents within a [Collection](../getting-started/concepts#collections), as well as what they can and cannot see within the [Admin Panel](../admin/overview) as it relates to that Collection.

To add Access Control to a Collection, use the `access` property in your [Collection Config](../configuration/collections):
```
import type { CollectionConfig } from 'payload'
    
    
    export const CollectionWithAccessControl: CollectionConfig = {
      // ...
      access: {
        
        // ...
      },
    }
```

## [Config Options](/docs/access-control/collections#config-options)

Access Control is specific to the operation of the request.

To add Access Control to a Collection, use the `access` property in your [Collection Config](../configuration/collections):
```
import type { CollectionConfig } from 'payload';
    
    
    export const CollectionWithAccessControl: CollectionConfig = {
      // ...
      access: {
        create: () => {...},
        read: () => {...},
        update: () => {...},
        delete: () => {...},
    
    
        // Auth-enabled Collections only
        admin: () => {...},
        unlock: () => {...},
    
    
        // Version-enabled Collections only
        readVersions: () => {...},
      },
    }
```

The following options are available:

Function |  Allows/Denies Access   
---|---  
`**create**` |  Used in the `create` operation. More details.   
`**read**` |  Used in the `find` and `findByID` operations. More details.   
`**update**` |  Used in the `update` operation. More details.   
`**delete**` |  Used in the `delete` operation. More details.   
  
If a Collection supports [`Authentication`](../authentication/overview), the following additional options are available:

Function |  Allows/Denies Access   
---|---  
`**admin**` |  Used to restrict access to the [Admin Panel](../admin/overview). More details.   
`**unlock**` |  Used to restrict which users can access the `unlock` operation. More details.   
  
If a Collection supports [Versions](../versions/overview), the following additional options are available:

Function |  Allows/Denies Access   
---|---  
`**readVersions**` |  Used to control who can read versions, and who can't. Will automatically restrict the Admin UI version viewing access. More details.   
  
### [Create](/docs/access-control/collections#create)

Returns a boolean which allows/denies access to the `create` request.

To add create Access Control to a Collection, use the `create` property in the [Collection Config](../configuration/collections):
```
import type { CollectionConfig } from 'payload'
    
    
    export const CollectionWithCreateAccess: CollectionConfig = {
      // ...
      access: {
        create: ({ req: { user }, data }) => {
          return Boolean(user)
        },
      },
    }
```

The following arguments are provided to the `create` function:

Option |  Description   
---|---  
`**req**` |  The [Request](https://developer.mozilla.org/en-US/docs/Web/API/Request) object containing the currently authenticated `user`.   
`**data**` |  The data passed to create the document with.   
  
### [Read](/docs/access-control/collections#read)

Returns a boolean which allows/denies access to the `read` request.

To add read Access Control to a Collection, use the `read` property in the [Collection Config](../configuration/collections):
```
import type { CollectionConfig } from 'payload'
    
    
    export const CollectionWithReadAccess: CollectionConfig = {
      // ...
      access: {
        read: ({ req: { user } }) => {
          return Boolean(user)
        },
      },
    }
```

**Tip:** Return a [Query](../queries/overview) to limit the Documents to only those that match the constraint. This can be helpful to restrict users' access to specific Documents. [More details](../queries/overview).

As your application becomes more complex, you may want to define your function in a separate file and import them into your Collection Config:
```
import type { Access } from 'payload'
    import type { Page } from '@/payload-types'
    
    
    export const canReadPage: Access<Page> = ({ req: { user } }) => {
      // Allow authenticated users
      if (user) {
        return true
      }
    
    
      // By returning a Query, guest users can read public Documents
      // Note: this assumes you have a `isPublic` checkbox field on your Collection
      return {
        isPublic: {
          equals: true,
        },
      }
    }
```

The following arguments are provided to the `read` function:

Option |  Description   
---|---  
`**req**` |  The [Request](https://developer.mozilla.org/en-US/docs/Web/API/Request) object containing the currently authenticated `user`.   
`**id**` |  `id` of document requested, if within `findByID`.   
  
### [Update](/docs/access-control/collections#update)

Returns a boolean which allows/denies access to the `update` request.

To add update Access Control to a Collection, use the `update` property in the [Collection Config](../configuration/collections):
```
import type { CollectionConfig } from 'payload'
    
    
    export const CollectionWithUpdateAccess: CollectionConfig = {
      // ...
      access: {
        update: ({ req: { user } }) => {
          return Boolean(user)
        },
      },
    }
```

**Tip:** Return a [Query](../queries/overview) to limit the Documents to only those that match the constraint. This can be helpful to restrict users' access to specific Documents. [More details](../queries/overview).

As your application becomes more complex, you may want to define your function in a separate file and import them into your Collection Config:
```
import type { Access } from 'payload'
    import type { User } from '@/payload-types'
    
    
    export const canUpdateUser: Access<User> = ({ req: { user }, id }) => {
      // Allow users with a role of 'admin'
      if (user.roles && user.roles.some((role) => role === 'admin')) {
        return true
      }
    
    
      // allow any other users to update only oneself
      return user.id === id
    }
```

The following arguments are provided to the `update` function:

Option |  Description   
---|---  
`**req**` |  The [Request](https://developer.mozilla.org/en-US/docs/Web/API/Request) object containing the currently authenticated `user`.   
`**id**` |  `id` of document requested to update.   
`**data**` |  The data passed to update the document with.   
  
### [Delete](/docs/access-control/collections#delete)

Similarly to the Update function, returns a boolean or a [query constraint](../queries/overview) to limit which documents can be deleted by which users.

To add delete Access Control to a Collection, use the `delete` property in the [Collection Config](../configuration/collections):
```
import type { CollectionConfig } from 'payload'
    
    
    export const CollectionWithDeleteAccess: CollectionConfig = {
      // ...
      access: {
        delete: ({ req: { user } }) => {
          return Boolean(user)
        },
      },
    }
```

As your application becomes more complex, you may want to define your function in a separate file and import them into your Collection Config:
```
import type { Access } from 'payload'
    import type { Customer } from '@/payload-types'
    
    
    export const canDeleteCustomer: Access<Customer> = async ({ req, id }) => {
      if (!id) {
        // allow the admin UI to show controls to delete since it is indeterminate without the `id`
        return true
      }
    
    
      // Query another Collection using the `id`
      const result = await req.payload.find({
        collection: 'contracts',
        limit: 0,
        depth: 0,
        where: {
          customer: { equals: id },
        },
      })
    
    
      return result.totalDocs === 0
    }
```

The following arguments are provided to the `delete` function:

Option |  Description   
---|---  
`**req**` |  The [Request](https://developer.mozilla.org/en-US/docs/Web/API/Request) object with additional `user` property, which is the currently logged in user.   
`**id**` |  `id` of document requested to delete.   
  
### [Admin](/docs/access-control/collections#admin)

If the Collection is used to access the [Admin Panel](../admin/overview#the-admin-user-collection), the `Admin` Access Control function determines whether or not the currently logged in user can access the admin UI.

To add Admin Access Control to a Collection, use the `admin` property in the [Collection Config](../configuration/collections):
```
import type { CollectionConfig } from 'payload'
    
    
    export const CollectionWithAdminAccess: CollectionConfig = {
      // ...
      access: {
        admin: ({ req: { user } }) => {
          return Boolean(user)
        },
      },
    }
```

The following arguments are provided to the `admin` function:

Option |  Description   
---|---  
`**req**` |  The [Request](https://developer.mozilla.org/en-US/docs/Web/API/Request) object containing the currently authenticated `user`.   
  
### [Unlock](/docs/access-control/collections#unlock)

Determines which users can [unlock](../authentication/operations#unlock) other users who may be blocked from authenticating successfully due to [failing too many login attempts](../authentication/overview#config-options).

To add Unlock Access Control to a Collection, use the `unlock` property in the [Collection Config](../configuration/collections):
```
import type { CollectionConfig } from 'payload'
    
    
    export const CollectionWithUnlockAccess: CollectionConfig = {
      // ...
      access: {
        unlock: ({ req: { user } }) => {
          return Boolean(user)
        },
      },
    }
```

The following arguments are provided to the `unlock` function:

Option |  Description   
---|---  
`**req**` |  The [Request](https://developer.mozilla.org/en-US/docs/Web/API/Request) object containing the currently authenticated `user`.   
  
### [Read Versions](/docs/access-control/collections#read-versions)

If the Collection has [Versions](../versions/overview) enabled, the `readVersions` Access Control function determines whether or not the currently logged in user can access the version history of a Document.

To add Read Versions Access Control to a Collection, use the `readVersions` property in the [Collection Config](../configuration/collections):
```
import type { CollectionConfig } from 'payload'
    
    
    export const CollectionWithVersionsAccess: CollectionConfig = {
      // ...
      access: {
        readVersions: ({ req: { user } }) => {
          return Boolean(user)
        },
      },
    }
```

**Note:** Returning a [Query](../queries/overview) will apply the constraint to the [`versions` collection](../versions/overview#database-impact), not the original Collection.

The following arguments are provided to the `readVersions` function:

Option |  Description   
---|---  
`**req**` |  The [Request](https://developer.mozilla.org/en-US/docs/Web/API/Request) object containing the currently authenticated `user`.   
  
[Next Globals Access Control](/docs/access-control/globals)

#### Related Guides

  * [How to set up and customize Collections ](/posts/guides/how-to-set-up-and-customize-collections)
