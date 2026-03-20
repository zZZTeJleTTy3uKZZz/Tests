<a id="page-72"></a>
---
url: https://payloadcms.com/docs/custom-components/custom-providers
---

# Swap in your own React Context providers

As you add more and more [Custom Components](./overview) to your [Admin Panel](../admin/overview), you may find it helpful to add additional [React Context](https://react.dev/learn/scaling-up-with-reducer-and-context)(s) to your app. Payload allows you to inject your own context providers where you can export your own custom hooks, etc.

To add a Custom Provider, use the `admin.components.providers` property in your [Payload Config](../configuration/overview):
```
import { buildConfig } from 'payload'
    
    
    export default buildConfig({
      // ...
      admin: {
        components: {
          providers: ['/path/to/MyProvider'], 
        },
      },
    })
```

Then build your Custom Provider as follows:
```
'use client'
    import React, { createContext, use } from 'react'
    
    
    const MyCustomContext = React.createContext(myCustomValue)
    
    
    export function MyProvider({ children }: { children: React.ReactNode }) {
      return <MyCustomContext value={myCustomValue}>{children}</MyCustomContext>
    }
    
    
    export const useMyCustomContext = () => use(MyCustomContext)
```

_For details on how to build Custom Components, see_[ _Building Custom Components_](./overview#building-custom-components) _._

**Reminder:** React Context exists only within Client Components. This means they must include the `use client` directive at the top of their files and cannot contain server-only code. To use a Server Component here, simply _wrap_ your Client Component with it.

[Next Customizing Views](/docs/custom-components/custom-views)
