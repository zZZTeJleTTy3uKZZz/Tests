<a id="page-42"></a>
---
url: https://payloadcms.com/docs/access-control/globals
---

# Globals Access Control

Global Access Control is [Access Control](../access-control/overview) used to restrict access to [Global](../configuration/globals) Documents, as well as what they can and cannot see within the [Admin Panel](../admin/overview) as it relates to that Global.

To add Access Control to a Global, use the `access` property in your [Global Config](../configuration/globals):
```
import type { GlobalConfig } from 'payload'
    
    
    export const GlobalWithAccessControl: GlobalConfig = {
      // ...
      access: {
        
        // ...
      },
    }
```

## [Config Options](/docs/access-control/globals#config-options)

Access Control is specific to the operation of the request.

To add Access Control to a [Global](../configuration/globals), use the `access` property in the [Global Config](../configuration/globals):
```
import { GlobalConfig } from 'payload'
    
    
    const GlobalWithAccessControl: GlobalConfig = {
      // ...
      access: {
        read: ({ req: { user } }) => {...},
        update: ({ req: { user } }) => {...},
    
    
        // Version-enabled Globals only
        readVersions: () => {...},
      },
    }
    
    
    export default Header
```

The following options are available:

Function |  Allows/Denies Access   
---|---  
`**read**` |  Used in the `findOne` Global operation. More details.   
`**update**` |  Used in the `update` Global operation. More details.   
  
If a Global supports [Versions](../versions/overview), the following additional options are available:

Function |  Allows/Denies Access   
---|---  
`**readVersions**` |  Used to control who can read versions, and who can't. Will automatically restrict the Admin UI version viewing access. More details.   
  
### [Read](/docs/access-control/globals#read)

Returns a boolean result or optionally a [query constraint](../queries/overview) which limits who can read this global based on its current properties.

To add read Access Control to a [Global](../configuration/globals), use the `access` property in the [Global Config](../configuration/globals):
```
import { GlobalConfig } from 'payload'
    
    
    const Header: GlobalConfig = {
      // ...
      access: {
        read: ({ req: { user } }) => {
          return Boolean(user)
        },
      },
    }
```

The following arguments are provided to the `read` function:

Option |  Description   
---|---  
`**req**` |  The [Request](https://developer.mozilla.org/en-US/docs/Web/API/Request) object containing the currently authenticated `user`.   
  
### [Update](/docs/access-control/globals#update)

Returns a boolean result or optionally a [query constraint](../queries/overview) which limits who can update this global based on its current properties.

To add update Access Control to a [Global](../configuration/globals), use the `access` property in the [Global Config](../configuration/globals):
```
import { GlobalConfig } from 'payload'
    
    
    const Header: GlobalConfig = {
      // ...
      access: {
        update: ({ req: { user }, data }) => {
          return Boolean(user)
        },
      },
    }
```

The following arguments are provided to the `update` function:

Option |  Description   
---|---  
`**req**` |  The [Request](https://developer.mozilla.org/en-US/docs/Web/API/Request) object containing the currently authenticated `user`.   
`**data**` |  The data passed to update the global with.   
  
### [Read Versions](/docs/access-control/globals#read-versions)

If the Global has [Versions](../versions/overview) enabled, the `readVersions` Access Control function determines whether or not the currently logged in user can access the version history of a Document.

To add Read Versions Access Control to a Global, use the `readVersions` property in the [Global Config](../configuration/globals):
```
import type { GlobalConfig } from 'payload'
    
    
    export const GlobalWithVersionsAccess: GlobalConfig = {
      // ...
      access: {
        readVersions: ({ req: { user } }) => {
          return Boolean(user)
        },
      },
    }
```

**Note:** Returning a [Query](../queries/overview) will apply the constraint to the [`versions` collection](../versions/overview#database-impact), not the original Global.

The following arguments are provided to the `readVersions` function:

Option |  Description   
---|---  
`**req**` |  The [Request](https://developer.mozilla.org/en-US/docs/Web/API/Request) object containing the currently authenticated `user`.   
  
[Next Field-level Access Control](/docs/access-control/fields)
