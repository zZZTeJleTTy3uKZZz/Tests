<a id="page-76"></a>
---
url: https://payloadcms.com/docs/custom-components/edit-view
---

# Edit View

The Edit View is where users interact with individual [Collection](../configuration/collections) and [Global](../configuration/globals) Documents within the [Admin Panel](../admin/overview). The Edit View contains the actual form that submits the data to the server. This is where they can view, edit, and save their content. It contains controls for saving, publishing, and previewing the document, all of which can be customized to a high degree.

The Edit View can be swapped out in its entirety for a Custom View, or it can be injected with a number of Custom Components to add additional functionality or presentational elements without replacing the entire view.

**Note:** The Edit View is one of many [Document Views](./document-views) in the Payload Admin Panel. Each Document View is responsible for a different aspect of interacting with a single Document.

## [Custom Edit View](/docs/custom-components/edit-view#custom-edit-view)

To swap out the entire Edit View with a [Custom View](./custom-views), use the `views.edit.default` property in your [Collection Config](../configuration/collections) or [Global Config](../configuration/globals):
```
import { buildConfig } from 'payload'
    
    
    const config = buildConfig({
      // ...
      admin: {
        components: {
          views: {
            edit: {
              default: {
                Component: '/path/to/MyCustomEditViewComponent',
              },
            },
          },
        },
      },
    })
```

Here is an example of a custom Edit View:

#### [Server Component](/docs/custom-components/edit-view#server-component)
```
import React from 'react'
    import type { DocumentViewServerProps } from 'payload'
    
    
    export function MyCustomServerEditView(props: DocumentViewServerProps) {
      return <div>This is a custom Edit View (Server)</div>
    }
```

#### [Client Component](/docs/custom-components/edit-view#client-component)
```
'use client'
    import React from 'react'
    import type { DocumentViewClientProps } from 'payload'
    
    
    export function MyCustomClientEditView(props: DocumentViewClientProps) {
      return <div>This is a custom Edit View (Client)</div>
    }
```

_For details on how to build Custom Views, including all available props, see_[ _Building Custom Views_](./custom-views#building-custom-views) _._

## [ Custom Components](/docs/custom-components/edit-view#custom-components)

In addition to swapping out the entire Edit View with a [Custom View](./custom-views), you can also override individual components. This allows you to customize specific parts of the Edit View without swapping out the entire view.

**Important:** Collection and Globals are keyed to a different property in the `admin.components` object and have slightly different options. Be sure to use the correct key for the entity you are working with.

#### [Collections](/docs/custom-components/edit-view#collections)

To override Edit View components for a Collection, use the `admin.components.edit` property in your [Collection Config](../configuration/collections):
```
import type { CollectionConfig } from 'payload'
    
    
    export const MyCollection: CollectionConfig = {
      // ...
      admin: {
        components: {
          edit: {
            // ...
          },
        },
      },
    }
```

The following options are available:

Path |  Description   
---|---  
`beforeDocumentControls` |  Inject custom components before the Save / Publish buttons. More details.   
`editMenuItems` |  Inject custom components within the 3-dot menu dropdown located in the document control bar. More details.   
`SaveButton` |  A button that saves the current document. More details.   
`SaveDraftButton` |  A button that saves the current document as a draft. More details.   
`PublishButton` |  A button that publishes the current document. More details.   
`UnpublishButton` |  A button that unpublishes the current document. More details.   
`PreviewButton` |  A button that previews the current document. More details.   
`Description` |  A description of the Collection. More details.   
`Status` |  A component that represents the status of the current document. More details.   
`Upload` |  A file upload component. More details.   
  
#### [Globals](/docs/custom-components/edit-view#globals)

To override Edit View components for Globals, use the `admin.components.elements` property in your [Global Config](../configuration/globals):
```
import type { GlobalConfig } from 'payload'
    
    
    export const MyGlobal: GlobalConfig = {
      // ...
      admin: {
        components: {
          elements: {
            // ...
          },
        },
      },
    }
```

The following options are available:

Path |  Description   
---|---  
`beforeDocumentControls` |  Inject custom components before the Save / Publish buttons. More details.   
`editMenuItems` |  Inject custom components within the 3-dot menu dropdown located in the document control bar. More details.   
`SaveButton` |  A button that saves the current document. More details.   
`SaveDraftButton` |  A button that saves the current document as a draft. More details.   
`PublishButton` |  A button that publishes the current document. More details.   
`UnpublishButton` |  A button that unpublishes the current document. More details.   
`PreviewButton` |  A button that previews the current document. More details.   
`Description` |  A description of the Global. More details.   
`Status` |  A component that represents the status of the global. More details.   
  
### [SaveButton](/docs/custom-components/edit-view#savebutton)

The `SaveButton` property allows you to render a custom Save Button in the Edit View.

To add a `SaveButton` component, use the `components.edit.SaveButton` property in your [Collection Config](../configuration/collections) or `components.elements.SaveButton` in your [Global Config](../configuration/globals):
```
import type { CollectionConfig } from 'payload'
    
    
    export const MyCollection: CollectionConfig = {
      // ...
      admin: {
        components: {
          edit: {
            SaveButton: '/path/to/MySaveButton',
          },
        },
      },
    }
```

Here's an example of a custom `SaveButton` component:

#### [Server Component](/docs/custom-components/edit-view#server-component)
```
import React from 'react'
    import { SaveButton } from '@payloadcms/ui'
    import type { SaveButtonServerProps } from 'payload'
    
    
    export function MySaveButton(props: SaveButtonServerProps) {
      return <SaveButton label="Save" />
    }
```

#### [Client Component](/docs/custom-components/edit-view#client-component)
```
'use client'
    import React from 'react'
    import { SaveButton } from '@payloadcms/ui'
    import type { SaveButtonClientProps } from 'payload'
    
    
    export function MySaveButton(props: SaveButtonClientProps) {
      return <SaveButton label="Save" />
    }
```

### [beforeDocumentControls](/docs/custom-components/edit-view#beforedocumentcontrols)

The `beforeDocumentControls` property allows you to render custom components just before the default document action buttons (like Save, Publish, or Preview). This is useful for injecting custom buttons, status indicators, or any other UI elements before the built-in controls.

To add `beforeDocumentControls` components, use the `components.edit.beforeDocumentControls` property in your [Collection Config](../configuration/collections) or `components.elements.beforeDocumentControls` in your [Global Config](../configuration/globals):

#### [Collections](/docs/custom-components/edit-view#collections)
```
export const MyCollection: CollectionConfig = {
      admin: {
        components: {
          edit: {
            beforeDocumentControls: ['/path/to/CustomComponent'],
          },
        },
      },
    }
```

#### [Globals](/docs/custom-components/edit-view#globals)
```
export const MyGlobal: GlobalConfig = {
      admin: {
        components: {
          elements: {
            beforeDocumentControls: ['/path/to/CustomComponent'],
          },
        },
      },
    }
```

Here's an example of a custom `beforeDocumentControls` component:

#### [Server Component](/docs/custom-components/edit-view#server-component)
```
import React from 'react'
    import type { BeforeDocumentControlsServerProps } from 'payload'
    
    
    export function MyCustomDocumentControlButton(
      props: BeforeDocumentControlsServerProps,
    ) {
      return <div>This is a custom beforeDocumentControl button (Server)</div>
    }
```

#### [Client Component](/docs/custom-components/edit-view#client-component)
```
'use client'
    import React from 'react'
    import type { BeforeDocumentControlsClientProps } from 'payload'
    
    
    export function MyCustomDocumentControlButton(
      props: BeforeDocumentControlsClientProps,
    ) {
      return <div>This is a custom beforeDocumentControl button (Client)</div>
    }
```

### [editMenuItems](/docs/custom-components/edit-view#editmenuitems)

The `editMenuItems` property allows you to inject custom components into the 3-dot menu dropdown located in the document controls bar. This dropdown contains default options including `Create New`, `Duplicate`, `Delete`, and other options when additional features are enabled. Any custom components you add will appear below these default items.

To add `editMenuItems`, use the `components.edit.editMenuItems` property in your [Collection Config](../configuration/collections):

#### [Config Example](/docs/custom-components/edit-view#config-example)
```
import type { CollectionConfig } from 'payload'
    
    
    export const Pages: CollectionConfig = {
      slug: 'pages',
      admin: {
        components: {
          edit: {
            editMenuItems: ['/path/to/CustomEditMenuItem'],
          },
        },
      },
    }
```

Here's an example of a custom `editMenuItems` component:

#### [Server Component](/docs/custom-components/edit-view#server-component)
```
import React from 'react'
    
    
    import type { EditMenuItemsServerProps } from 'payload'
    
    
    export const EditMenuItems = async (props: EditMenuItemsServerProps) => {
      const href = `/custom-action?id=${props.id}`
    
    
      return (
        <>
          <a href={href}>Custom Edit Menu Item</a>
          <a href={href}>
            Another Custom Edit Menu Item - add as many as you need!
          </a>
        </>
      )
    }
```

#### [Client Component](/docs/custom-components/edit-view#client-component)
```
'use client'
    
    
    import React from 'react'
    import { PopupList } from '@payloadcms/ui'
    
    
    import type { EditViewMenuItemClientProps } from 'payload'
    
    
    export const EditMenuItems = (props: EditViewMenuItemClientProps) => {
      const handleClick = () => {
        console.log('Custom button clicked!')
      }
    
    
      return (
        <PopupList.ButtonGroup>
          <PopupList.Button onClick={handleClick}>
            Custom Edit Menu Item
          </PopupList.Button>
          <PopupList.Button onClick={handleClick}>
            Another Custom Edit Menu Item - add as many as you need!
          </PopupList.Button>
        </PopupList.ButtonGroup>
      )
    }
```

**Styling:** Use Payload's built-in `PopupList.Button` to ensure your menu items automatically match the default dropdown styles. If you want a different look, you can customize the appearance by passing your own `className` to `PopupList.Button`, or use a completely custom button built with a standard HTML `button` element or any other component that fits your design preferences.

### [SaveDraftButton](/docs/custom-components/edit-view#savedraftbutton)

The `SaveDraftButton` property allows you to render a custom Save Draft Button in the Edit View.

To add a `SaveDraftButton` component, use the `components.edit.SaveDraftButton` property in your [Collection Config](../configuration/collections) or `components.elements.SaveDraftButton` in your [Global Config](../configuration/globals):
```
import type { CollectionConfig } from 'payload'
    
    
    export const MyCollection: CollectionConfig = {
      // ...
      admin: {
        components: {
          edit: {
            SaveDraftButton: '/path/to/MySaveDraftButton',
          },
        },
      },
    }
```

Here's an example of a custom `SaveDraftButton` component:

#### [Server Component](/docs/custom-components/edit-view#server-component)
```
import React from 'react'
    import { SaveDraftButton } from '@payloadcms/ui'
    import type { SaveDraftButtonServerProps } from 'payload'
    
    
    export function MySaveDraftButton(props: SaveDraftButtonServerProps) {
      return <SaveDraftButton />
    }
```

#### [Client Component](/docs/custom-components/edit-view#client-component)
```
'use client'
    import React from 'react'
    import { SaveDraftButton } from '@payloadcms/ui'
    import type { SaveDraftButtonClientProps } from 'payload'
    
    
    export function MySaveDraftButton(props: SaveDraftButtonClientProps) {
      return <SaveDraftButton />
    }
```

### [PublishButton](/docs/custom-components/edit-view#publishbutton)

The `PublishButton` property allows you to render a custom Publish Button in the Edit View.

To add a `PublishButton` component, use the `components.edit.PublishButton` property in your [Collection Config](../configuration/collections) or `components.elements.PublishButton` in your [Global Config](../configuration/globals):
```
import type { CollectionConfig } from 'payload'
    
    
    export const MyCollection: CollectionConfig = {
      // ...
      admin: {
        components: {
          edit: {
            PublishButton: '/path/to/MyPublishButton',
          },
        },
      },
    }
```

Here's an example of a custom `PublishButton` component:

#### [Server Component](/docs/custom-components/edit-view#server-component)
```
import React from 'react'
    import { PublishButton } from '@payloadcms/ui'
    import type { PublishButtonServerProps } from 'payload'
    
    
    export function MyPublishButton(props: PublishButtonServerProps) {
      return <PublishButton label="Publish" />
    }
```

#### [Client Component](/docs/custom-components/edit-view#client-component)
```
'use client'
    import React from 'react'
    import { PublishButton } from '@payloadcms/ui'
    
    
    export function MyPublishButton() {
      return <PublishButton label="Publish" />
    }
```

### [UnpublishButton](/docs/custom-components/edit-view#unpublishbutton)

The `UnpublishButton` property allows you to render a custom Unpublish Button in the Edit View.

To add an `UnpublishButton` component, use the `components.edit.UnpublishButton` property in your [Collection Config](../configuration/collections) or `components.elements.UnpublishButton` in your [Global Config](../configuration/globals):
```
import type { CollectionConfig } from 'payload'
    
    
    export const MyCollection: CollectionConfig = {
      // ...
      admin: {
        components: {
          edit: {
            UnpublishButton: '/path/to/MyUnpublishButton',
          },
        },
      },
    }
```

Here's an example of a custom `UnpublishButton` component:

#### [Server Component](/docs/custom-components/edit-view#server-component)
```
import React from 'react'
    import { UnpublishButton } from '@payloadcms/ui'
    import type { UnpublishButtonServerProps } from 'payload'
    
    
    export function MyUnpublishButton(props: UnpublishButtonServerProps) {
      return <UnpublishButton label="Unpublish" />
    }
```

#### [Client Component](/docs/custom-components/edit-view#client-component)
```
'use client'
    import React from 'react'
    import { UnpublishButton } from '@payloadcms/ui'
    
    
    export function MyUnpublishButton() {
      return <UnpublishButton label="Unpublish" />
    }
```

### [PreviewButton](/docs/custom-components/edit-view#previewbutton)

The `PreviewButton` property allows you to render a custom Preview Button in the Edit View.

To add a `PreviewButton` component, use the `components.edit.PreviewButton` property in your [Collection Config](../configuration/collections) or `components.elements.PreviewButton` in your [Global Config](../configuration/globals):
```
import type { CollectionConfig } from 'payload'
    
    
    export const MyCollection: CollectionConfig = {
      // ...
      admin: {
        components: {
          edit: {
            PreviewButton: '/path/to/MyPreviewButton',
          },
        },
      },
    }
```

Here's an example of a custom `PreviewButton` component:

#### [Server Component](/docs/custom-components/edit-view#server-component)
```
import React from 'react'
    import { PreviewButton } from '@payloadcms/ui'
    import type { PreviewButtonServerProps } from 'payload'
    
    
    export function MyPreviewButton(props: PreviewButtonServerProps) {
      return <PreviewButton />
    }
```

#### [Client Component](/docs/custom-components/edit-view#client-component)
```
'use client'
    import React from 'react'
    import { PreviewButton } from '@payloadcms/ui'
    import type { PreviewButtonClientProps } from 'payload'
    
    
    export function MyPreviewButton(props: PreviewButtonClientProps) {
      return <PreviewButton />
    }
```

### [Description](/docs/custom-components/edit-view#description)

The `Description` property allows you to render a custom description of the Collection or Global in the Edit View.

To add a `Description` component, use the `components.edit.Description` property in your [Collection Config](../configuration/collections) or `components.elements.Description` in your [Global Config](../configuration/globals):
```
import type { CollectionConfig } from 'payload'
    
    
    export const MyCollection: CollectionConfig = {
      // ...
      admin: {
        components: {
          Description: '/path/to/MyDescriptionComponent',
        },
      },
    }
```

**Note:** The `Description` component is shared between the Edit View and the [List View](./list-view).

Here's an example of a custom `Description` component:

#### [Server Component](/docs/custom-components/edit-view#server-component)
```
import React from 'react'
    import type { ViewDescriptionServerProps } from 'payload'
    
    
    export function MyDescriptionComponent(props: ViewDescriptionServerProps) {
      return <div>This is a custom description component (Server)</div>
    }
```

#### [Client Component](/docs/custom-components/edit-view#client-component)
```
'use client'
    import React from 'react'
    import type { ViewDescriptionClientProps } from 'payload'
    
    
    export function MyDescriptionComponent(props: ViewDescriptionClientProps) {
      return <div>This is a custom description component (Client)</div>
    }
```

### [Status](/docs/custom-components/edit-view#status)

The `Status` property allows you to render a component that represents the collection or global status in the Edit View.

To add an `Status` component, use the `components.edit.Status` property in your [Collection Config](../configuration/collections):
```
import type { CollectionConfig } from 'payload'
    
    
    export const MyCollection: CollectionConfig = {
      // ...
      admin: {
        components: {
          edit: {
            Status: '/path/to/MyStatusComponent',
          },
        },
      },
    }
```

### [Upload](/docs/custom-components/edit-view#upload)

The `Upload` property allows you to render a custom file upload component in the Edit View. This is only available for upload-enabled Collections.

To add an `Upload` component, use the `components.edit.Upload` property in your [Collection Config](../configuration/collections):
```
import type { CollectionConfig } from 'payload'
    
    
    export const Media: CollectionConfig = {
      slug: 'media',
      upload: true,
      admin: {
        components: {
          edit: {
            Upload: '/path/to/MyUploadComponent#MyUploadServer',
          },
        },
      },
    }
```

**Important:** Custom upload components must integrate with Payload's form system to work correctly. You cannot use a simple `<input type="file" />` as it won't connect to Payload's upload API. Instead, use Payload's built-in `<Upload>` component from `@payloadcms/ui` or properly integrate with form hooks like `useDocumentInfo()`.

Here's an example of a custom `Upload` component:

#### [Server Component](/docs/custom-components/edit-view#server-component)
```
import React from 'react'
    import type {
      PayloadServerReactComponent,
      SanitizedCollectionConfig,
    } from 'payload'
    import { CustomUploadClient } from './MyUploadComponent.client'
    
    
    export const MyUploadServer: PayloadServerReactComponent<
      SanitizedCollectionConfig['admin']['components']['edit']['Upload']
    > = (props) => {
      return (
        <div>
          <h2>Custom Upload Interface</h2>
          <CustomUploadClient {...props} />
        </div>
      )
    }
```

#### [Client Component](/docs/custom-components/edit-view#client-component)
```
'use client'
    import React from 'react'
    import { Upload, useDocumentInfo } from '@payloadcms/ui'
    
    
    export const CustomUploadClient = () => {
      const { collectionSlug, docConfig, initialState } = useDocumentInfo()
    
    
      return (
        <Upload
          collectionSlug={collectionSlug}
          initialState={initialState}
          uploadConfig={'upload' in docConfig ? docConfig.upload : undefined}
        />
      )
    }
```

For more details on customizing upload components, including examples with custom actions and drawers, see the [Upload documentation](../upload/overview#customizing-the-upload-ui).

[Next List View](/docs/custom-components/list-view)
