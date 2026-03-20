<a id="page-71"></a>
---
url: https://payloadcms.com/docs/custom-components/root-components
---

# Root Components

Root Components are those that affect the [Admin Panel](../admin/overview) at a high-level, such as the logo or the main nav. You can swap out these components with your own [Custom Components](./overview) to create a completely custom look and feel.

When combined with [Custom CSS](../admin/customizing-css), you can create a truly unique experience for your users, such as white-labeling the Admin Panel to match your brand.

To override Root Components, use the `admin.components` property at the root of your [Payload Config](../configuration/overview):
```
import { buildConfig } from 'payload'
    
    
    export default buildConfig({
      // ...
      admin: {
        components: {
          // ...
        },
      },
    })
```

## [Config Options](/docs/custom-components/root-components#config-options)

The following options are available:

Path |  Description   
---|---  
`actions` |  An array of Custom Components to be rendered _within_ the header of the Admin Panel, providing additional interactivity and functionality. More details.   
`afterDashboard` |  An array of Custom Components to inject into the built-in Dashboard, _after_ the default dashboard contents. More details.   
`afterLogin` |  An array of Custom Components to inject into the built-in Login, _after_ the default login form. More details.   
`afterNavLinks` |  An array of Custom Components to inject into the built-in Nav, _after_ the links. More details.   
`beforeDashboard` |  An array of Custom Components to inject into the built-in Dashboard, _before_ the default dashboard contents. More details.   
`beforeLogin` |  An array of Custom Components to inject into the built-in Login, _before_ the default login form. More details.   
`beforeNavLinks` |  An array of Custom Components to inject into the built-in Nav, _before_ the links themselves. More details.   
`graphics.Icon` |  The simplified logo used in contexts like the `Nav` component. More details.   
`graphics.Logo` |  The full logo used in contexts like the `Login` view. More details.   
`header` |  An array of Custom Components to be injected above the Payload header. More details.   
`logout.Button` |  The button displayed in the sidebar that logs the user out. More details.   
`Nav` |  Contains the sidebar / mobile menu in its entirety. More details.   
`settingsMenu` |  An array of Custom Components to inject into a popup menu accessible via a gear icon above the logout button. More details.   
`providers` |  Custom [React Context](https://react.dev/learn/scaling-up-with-reducer-and-context) providers that will wrap the entire Admin Panel. [More details](./custom-providers).   
`views` |  Override or create new views within the Admin Panel. [More details](./custom-views).   
  
_For details on how to build Custom Components, see_[ _Building Custom Components_](./overview#building-custom-components) _._

**Note:** You can also set [Collection Components](../configuration/collections#custom-components) and [Global Components](../configuration/globals#custom-components) in their respective configs.

## [Components](/docs/custom-components/root-components#components)### [actions](/docs/custom-components/root-components#actions)

Actions are rendered within the header of the Admin Panel. Actions are typically used to display buttons that add additional interactivity and functionality, although they can be anything you'd like.

To add an action, use the `actions` property in your `admin.components` config:
```
import { buildConfig } from 'payload'
    
    
    export default buildConfig({
      // ...
      admin: {
        components: {
          actions: ['/path/to/your/component'],
        },
      },
    })
```

Here is an example of a simple Action component:
```
export default function MyCustomAction() {
      return (
        <button onClick={() => alert('Hello, world!')}>
          This is a custom action component
        </button>
      )
    }
```

**Note:** You can also use add Actions to the [Edit View](./edit-view) and [List View](./list-view) in their respective configs.

### [beforeDashboard](/docs/custom-components/root-components#beforedashboard)

The `beforeDashboard` property allows you to inject Custom Components into the built-in Dashboard, before the default dashboard contents.

To add `beforeDashboard` components, use the `admin.components.beforeDashboard` property in your Payload Config:
```
import { buildConfig } from 'payload'
    
    
    export default buildConfig({
      // ...
      admin: {
        components: {
          beforeDashboard: ['/path/to/your/component'],
        },
      },
    })
```

Here is an example of a simple `beforeDashboard` component:
```
export default function MyBeforeDashboardComponent() {
      return <div>This is a custom component injected before the Dashboard.</div>
    }
```

**Note:** You can also set [Dashboard Widgets](../custom-components/dashboard) in the `admin.dashboard` property, or replace the entire [Dashboard View](../custom-components/dashboard) with your own.

### [afterDashboard](/docs/custom-components/root-components#afterdashboard)

Similar to `beforeDashboard`, the `afterDashboard` property allows you to inject Custom Components into the built-in Dashboard, _after_ the default dashboard contents.

To add `afterDashboard` components, use the `admin.components.afterDashboard` property in your Payload Config:
```
import { buildConfig } from 'payload'
    
    
    export default buildConfig({
      // ...
      admin: {
        components: {
          afterDashboard: ['/path/to/your/component'],
        },
      },
    })
```

Here is an example of a simple `afterDashboard` component:
```
export default function MyAfterDashboardComponent() {
      return <div>This is a custom component injected after the Dashboard.</div>
    }
```

**Note:** You can also set [Dashboard Widgets](../custom-components/dashboard) in the `admin.dashboard` property, or replace the entire [Dashboard View](../custom-components/dashboard) with your own.

### [beforeLogin](/docs/custom-components/root-components#beforelogin)

The `beforeLogin` property allows you to inject Custom Components into the built-in Login view, _before_ the default login form.

To add `beforeLogin` components, use the `admin.components.beforeLogin` property in your Payload Config:
```
import { buildConfig } from 'payload'
    
    
    export default buildConfig({
      // ...
      admin: {
        components: {
          beforeLogin: ['/path/to/your/component'],
        },
      },
    })
```

Here is an example of a simple `beforeLogin` component:
```
export default function MyBeforeLoginComponent() {
      return <div>This is a custom component injected before the Login form.</div>
    }
```

### [afterLogin](/docs/custom-components/root-components#afterlogin)

Similar to `beforeLogin`, the `afterLogin` property allows you to inject Custom Components into the built-in Login view, _after_ the default login form.

To add `afterLogin` components, use the `admin.components.afterLogin` property in your Payload Config:
```
import { buildConfig } from 'payload'
    
    
    export default buildConfig({
      // ...
      admin: {
        components: {
          afterLogin: ['/path/to/your/component'],
        },
      },
    })
```

Here is an example of a simple `afterLogin` component:
```
export default function MyAfterLoginComponent() {
      return <div>This is a custom component injected after the Login form.</div>
    }
```

### [beforeNavLinks](/docs/custom-components/root-components#beforenavlinks)

The `beforeNavLinks` property allows you to inject Custom Components into the built-in Nav Component, _before_ the nav links themselves.

To add `beforeNavLinks` components, use the `admin.components.beforeNavLinks` property in your Payload Config:
```
import { buildConfig } from 'payload'
    
    
    export default buildConfig({
      // ...
      admin: {
        components: {
          beforeNavLinks: ['/path/to/your/component'],
        },
      },
    })
```

Here is an example of a simple `beforeNavLinks` component:
```
export default function MyBeforeNavLinksComponent() {
      return <div>This is a custom component injected before the Nav links.</div>
    }
```

### [afterNavLinks](/docs/custom-components/root-components#afternavlinks)

Similar to `beforeNavLinks`, the `afterNavLinks` property allows you to inject Custom Components into the built-in Nav, _after_ the nav links.

To add `afterNavLinks` components, use the `admin.components.afterNavLinks` property in your Payload Config:
```
import { buildConfig } from 'payload'
    
    
    export default buildConfig({
      // ...
      admin: {
        components: {
          afterNavLinks: ['/path/to/your/component'],
        },
      },
    })
```

Here is an example of a simple `afterNavLinks` component:
```
export default function MyAfterNavLinksComponent() {
      return <p>This is a custom component injected after the Nav links.</p>
    }
```

### [settingsMenu](/docs/custom-components/root-components#settingsmenu)

The `settingsMenu` property allows you to inject Custom Components into a popup menu accessible via a gear icon in the navigation controls, positioned above the logout button. This is ideal for adding custom actions, utilities, or settings that are relevant at the admin level.

To add `settingsMenu` components, use the `admin.components.settingsMenu` property in your Payload Config:
```
import { buildConfig } from 'payload'
    
    
    export default buildConfig({
      // ...
      admin: {
        components: {
          settingsMenu: ['/path/to/your/component#ComponentName'],
        },
      },
    })
```

Here is an example of a simple `settingsMenu` component:
```
'use client'
    import { PopupList } from '@payloadcms/ui'
    
    
    export function MySettingsMenu() {
      return (
        <PopupList.ButtonGroup>
          <PopupList.Button onClick={() => console.log('Action triggered')}>
            Custom Action
          </PopupList.Button>
          <PopupList.Button onClick={() => window.open('/admin/custom-page')}>
            Custom Page
          </PopupList.Button>
        </PopupList.ButtonGroup>
      )
    }
```

You can pass multiple components to create organized groups of menu items:
```
import { buildConfig } from 'payload'
    
    
    export default buildConfig({
      // ...
      admin: {
        components: {
          settingsMenu: [
            '/components/SystemActions#SystemActions',
            '/components/DataManagement#DataManagement',
          ],
        },
      },
    })
```

### [Nav](/docs/custom-components/root-components#nav)

The `Nav` property contains the sidebar / mobile menu in its entirety. Use this property to completely replace the built-in Nav with your own custom navigation.

To add a custom nav, use the `admin.components.Nav` property in your Payload Config:
```
import { buildConfig } from 'payload'
    
    
    export default buildConfig({
      // ...
      admin: {
        components: {
          Nav: '/path/to/your/component',
        },
      },
    })
```

Here is an example of a simple `Nav` component:
```
import { Link } from '@payloadcms/ui'
    
    
    export default function MyCustomNav() {
      return (
        <nav>
          <ul>
            <li>
              <Link href="/dashboard">Dashboard</Link>
            </li>
          </ul>
        </nav>
      )
    }
```

### [graphics.Icon](/docs/custom-components/root-components#graphicsicon)

The `Icon` property is the simplified logo used in contexts like the `Nav` component. This is typically a small, square icon that represents your brand.

To add a custom icon, use the `admin.components.graphics.Icon` property in your Payload Config:
```
import { buildConfig } from 'payload'
    
    
    export default buildConfig({
      // ...
      admin: {
        components: {
          graphics: {
            Icon: '/path/to/your/component',
          },
        },
      },
    })
```

Here is an example of a simple `Icon` component:
```
export default function MyCustomIcon() {
      return <img src="/path/to/your/icon.png" alt="My Custom Icon" />
    }
```

### [graphics.Logo](/docs/custom-components/root-components#graphicslogo)

The `Logo` property is the full logo used in contexts like the `Login` view. This is typically a larger, more detailed representation of your brand.

To add a custom logo, use the `admin.components.graphics.Logo` property in your Payload Config:
```
import { buildConfig } from 'payload'
    
    
    export default buildConfig({
      // ...
      admin: {
        components: {
          graphics: {
            Logo: '/path/to/your/component',
          },
        },
      },
    })
```

Here is an example of a simple `Logo` component:
```
export default function MyCustomLogo() {
      return <img src="/path/to/your/logo.png" alt="My Custom Logo" />
    }
```

### [header](/docs/custom-components/root-components#header)

The `header` property allows you to inject Custom Components above the Payload header.

Examples of a custom header components might include an announcements banner, a notifications bar, or anything else you'd like to display at the top of the Admin Panel in a prominent location.

To add `header` components, use the `admin.components.header` property in your Payload Config:
```
import { buildConfig } from 'payload'
    
    
    export default buildConfig({
      // ...
      admin: {
        components: {
          header: ['/path/to/your/component'],
        },
      },
    })
```

Here is an example of a simple `header` component:
```
export default function MyCustomHeader() {
      return (
        <header>
          <h1>My Custom Header</h1>
        </header>
      )
    }
```

### [logout.Button](/docs/custom-components/root-components#logoutbutton)

The `logout.Button` property is the button displayed in the sidebar that should log the user out when clicked.

To add a custom logout button, use the `admin.components.logout.Button` property in your Payload Config:
```
import { buildConfig } from 'payload'
    
    
    export default buildConfig({
      // ...
      admin: {
        components: {
          logout: {
            Button: '/path/to/your/component',
          },
        },
      },
    })
```

Here is an example of a simple `logout.Button` component:
```
export default function MyCustomLogoutButton() {
      return <button onClick={() => alert('Logging out!')}>Log Out</button>
    }
```

[Next Swap in your own React Context providers](/docs/custom-components/custom-providers)
