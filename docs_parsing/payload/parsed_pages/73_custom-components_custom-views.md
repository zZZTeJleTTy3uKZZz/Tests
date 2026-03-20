<a id="page-73"></a>
---
url: https://payloadcms.com/docs/custom-components/custom-views
---

# Customizing Views

Views are the individual pages that make up the [Admin Panel](../admin/overview), such as the Dashboard, [List View](./list-view), and [Edit View](./edit-view). One of the most powerful ways to customize the Admin Panel is to create Custom Views. These are [Custom Components](./overview) that can either replace built-in views or be entirely new.

There are four types of views within the Admin Panel:

  * Root Views
  * Collection Views
  * Global Views
  * [Document Views](./document-views)



To swap in your own Custom View, first determine the scope that corresponds to what you are trying to accomplish, consult the list of available components, then author your React component(s) accordingly.

## [Configuration](/docs/custom-components/custom-views#configuration)### [Replacing Views](/docs/custom-components/custom-views#replacing-views)

To customize views, use the `admin.components.views` property in your [Payload Config](../configuration/overview). This is an object with keys for each view you want to customize. Each key corresponds to the view you want to customize.

The exact list of available keys depends on the scope of the view you are customizing, depending on whether it's a Root View, Collection View, or Global View. Regardless of the scope, the principles are the same.

Here is an example of how to swap out a built-in view:
```
import { buildConfig } from 'payload'
    
    
    const config = buildConfig({
      // ...
      admin: {
        components: {
          views: {
            dashboard: {
              Component: '/path/to/MyCustomDashboard',
            },
          },
        },
      },
    })
```

**Note:** The dashboard is a special case, where in addition to replacing the default view, [you can add widgets modularly](../custom-components/dashboard).

For more granular control, pass a configuration object instead. Payload exposes the following properties for each view:

Property |  Description   
---|---  
`Component` * |  Pass in the component path that should be rendered when a user navigates to this route.   
`path` * |  Any valid URL path or array of paths that [`path-to-regexp`](https://www.npmjs.com/package/path-to-regex) understands. Must begin with a forward slash (`/`).   
`exact` |  Boolean. When true, will only match if the path matches the `usePathname()` exactly.   
`strict` |  When true, a path that has a trailing slash will only match a `location.pathname` with a trailing slash. This has no effect when there are additional URL segments in the pathname.   
`sensitive` |  When true, will match if the path is case sensitive.   
`meta` |  Page metadata overrides to apply to this view within the Admin Panel. [More details](../admin/metadata).   
  
_* An asterisk denotes that a property is required._

### [ Adding New Views](/docs/custom-components/custom-views#adding-new-views)

To add a _new_ view to the [Admin Panel](../admin/overview), simply add your own key to the `views` object. This is true for all view scopes.

New views require at least the `Component` and `path` properties:
```
import { buildConfig } from 'payload'
    
    
    const config = buildConfig({
      // ...
      admin: {
        components: {
          views: {
            myCustomView: {
              Component: '/path/to/MyCustomView#MyCustomViewComponent',
              path: '/my-custom-view',
            },
          },
        },
      },
    })
```

**Note:** Routes are cascading, so unless explicitly given the `exact` property, they will match on URLs that simply _start_ with the route's path. This is helpful when creating catch-all routes in your application. Alternatively, define your nested route _before_ your parent route.

## [Building Custom Views](/docs/custom-components/custom-views#building-custom-views)

Custom Views are simply [Custom Components](./overview) rendered at the page-level. Custom Views can either replace existing views or add entirely new ones. The process is generally the same regardless of the type of view you are customizing.

To understand how to build Custom Views, first review the [Building Custom Components](./overview#building-custom-components) guide. Once you have a Custom Component ready, you can use it as a Custom View.
```
import type { CollectionConfig } from 'payload'
    
    
    export const MyCollectionConfig: CollectionConfig = {
      // ...
      admin: {
        components: {
          views: {
            edit: {
              Component: '/path/to/MyCustomView', 
            },
          },
        },
      },
    }
```

### [Default Props](/docs/custom-components/custom-views#default-props)

Your Custom Views will be provided with the following props:

Prop |  Description   
---|---  
`initPageResult` |  An object containing `req`, `payload`, `permissions`, etc.   
`clientConfig` |  The Client Config object. [More details](./overview#accessing-the-payload-config).   
`importMap` |  The import map object.   
`params` |  An object containing the [Dynamic Route Parameters](https://nextjs.org/docs/app/building-your-application/routing/dynamic-routes).   
`searchParams` |  An object containing the [Search Parameters](https://developer.mozilla.org/docs/Learn/Common_questions/What_is_a_URL#parameters).   
`doc` |  The document being edited. Only available in Document Views. [More details](./document-views).   
`i18n` |  The [i18n](../configuration/i18n) object.   
`payload` |  The [Payload](../local-api/overview) class.   
  
**Note:** Some views may receive additional props, such as Collection Views and Global Views. See the relevant section for more details.

Here is an example of a Custom View component:
```
import type { AdminViewServerProps } from 'payload'
    
    
    import { Gutter } from '@payloadcms/ui'
    import React from 'react'
    
    
    export function MyCustomView(props: AdminViewServerProps) {
      return (
        <Gutter>
          <h1>Custom Default Root View</h1>
          <p>This view uses the Default Template.</p>
        </Gutter>
      )
    }
```

**Tip:** For consistent layout and navigation, you may want to wrap your Custom View with one of the built-in [Templates](./overview#templates).

### [View Templates](/docs/custom-components/custom-views#view-templates)

Your Custom Root Views can optionally use one of the templates that Payload provides. The most common of these is the Default Template which provides the basic layout and navigation.

Here is an example of how to use the Default Template in your Custom View:
```
import type { AdminViewServerProps } from 'payload'
    
    
    import { DefaultTemplate } from '@payloadcms/next/templates'
    import { Gutter } from '@payloadcms/ui'
    import React from 'react'
    
    
    export function MyCustomView({
      initPageResult,
      params,
      searchParams,
    }: AdminViewServerProps) {
      return (
        <DefaultTemplate
          i18n={initPageResult.req.i18n}
          locale={initPageResult.locale}
          params={params}
          payload={initPageResult.req.payload}
          permissions={initPageResult.permissions}
          searchParams={searchParams}
          user={initPageResult.req.user || undefined}
          visibleEntities={initPageResult.visibleEntities}
        >
          <Gutter>
            <h1>Custom Default Root View</h1>
            <p>This view uses the Default Template.</p>
          </Gutter>
        </DefaultTemplate>
      )
    }
```

### [Securing Custom Views](/docs/custom-components/custom-views#securing-custom-views)

All Custom Views are public by default. It's up to you to secure your custom views. If your view requires a user to be logged in or to have certain access rights, you should handle that within your view component yourself.

Here is how you might secure a Custom View:
```
import type { AdminViewServerProps } from 'payload'
    
    
    import { Gutter } from '@payloadcms/ui'
    import React from 'react'
    
    
    export function MyCustomView({ initPageResult }: AdminViewServerProps) {
      const {
        req: { user },
      } = initPageResult
    
    
      if (!user) {
        return <p>You must be logged in to view this page.</p>
      }
    
    
      return (
        <Gutter>
          <h1>Custom Default Root View</h1>
          <p>This view uses the Default Template.</p>
        </Gutter>
      )
    }
```

## [Root Views](/docs/custom-components/custom-views#root-views)

Root Views are the main views of the [Admin Panel](../admin/overview). These are views that are scoped directly under the `/admin` route, such as the Dashboard or Account views.

To swap out Root Views with your own, or to create entirely new ones, use the `admin.components.views` property at the root of your [Payload Config](../configuration/overview):
```
import { buildConfig } from 'payload'
    
    
    const config = buildConfig({
      // ...
      admin: {
        components: {
          views: {
            dashboard: {
              Component: '/path/to/Dashboard',
            },
            // Other options include:
            // - account
            // - [key: string]
            // See below for more details
          },
        },
      },
    })
```

_For details on how to build Custom Views, including all available props, see_ _Building Custom Views_ _._

The following options are available:

Property |  Description   
---|---  
`account` |  The Account view is used to show the currently logged in user's Account page.   
`dashboard` |  The main landing page of the Admin Panel.   
`[key]` |  Any other key can be used to add a completely new Root View. More details.   
  
## [Collection Views](/docs/custom-components/custom-views#collection-views)

Collection Views are views that are scoped under the `/collections` route, such as the Collection List and Document Edit views.

To swap out Collection Views with your own, or to create entirely new ones, use the `admin.components.views` property of your [Collection Config](../configuration/collections):
```
import type { CollectionConfig } from 'payload'
    
    
    export const MyCollectionConfig: CollectionConfig = {
      // ...
      admin: {
        components: {
          views: {
            edit: {
              default: {
                Component: '/path/to/MyCustomCollectionView',
              },
            },
            // Other options include:
            // - list
            // - [key: string]
            // See below for more details
          },
        },
      },
    }
```

**Reminder:** The `edit` key is comprised of various nested views, known as Document Views, that relate to the same Collection Document. [More details](./document-views).

The following options are available:

Property |  Description   
---|---  
`edit` |  The Edit View corresponds to a single Document for any given Collection and consists of various nested views. [More details](./document-views).   
`list` |  The List View is used to show a list of Documents for any given Collection. More details.   
`[key]` |  Any other key can be used to add a completely new Collection View. More details.   
  
_For details on how to build Custom Views, including all available props, see_ _Building Custom Views_ _._

## [ Global Views](/docs/custom-components/custom-views#global-views)

Global Views are views that are scoped under the `/globals` route, such as the Edit View.

To swap out Global Views with your own or create entirely new ones, use the `admin.components.views` property in your [Global Config](../configuration/globals):
```
import type { SanitizedGlobalConfig } from 'payload'
    
    
    export const MyGlobalConfig: SanitizedGlobalConfig = {
      // ...
      admin: {
        components: {
          views: {
            edit: {
              default: {
                Component: '/path/to/MyCustomGlobalView',
              },
            },
            // Other options include:
            // - [key: string]
            // See below for more details
          },
        },
      },
    }
```

**Reminder:** The `edit` key is comprised of various nested views, known as Document Views, that relate to the same Global Document. [More details](./document-views).

The following options are available:

Property |  Description   
---|---  
`edit` |  The Edit View represents a single Document for any given Global and consists of various nested views. [More details](./document-views).   
`[key]` |  Any other key can be used to add a completely new Global View. More details.   
  
_For details on how to build Custom Views, including all available props, see_ _Building Custom Views_ _._

[ Next Dashboard Widgets](/docs/custom-components/dashboard)

#### Related Guides

  * [How to build flexible layouts with Payload blocks ](/posts/guides/how-to-build-flexible-layouts-with-payload-blocks)
