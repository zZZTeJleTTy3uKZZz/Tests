<a id="page-22"></a>
---
url: https://payloadcms.com/docs/fields/code
---

# Code Field

The Code Field saves a string in the database, but provides the [Admin Panel](../admin/overview) with a code editor styled interface.

![Shows a Code field in the Payload Admin Panel](https://payloadcms.com/images/docs/fields/code.png)

This field is using the `monaco-react` editor syntax highlighting.

To add a Code Field, set the `type` to `code` in your [Field Config](./overview):
```
import type { Field } from 'payload'
    
    
    export const MyBlocksField: Field = {
      // ...
      type: 'code', 
    }
```

## [Config Options](/docs/fields/code#config-options)

Option |  Description   
---|---  
`**name**` * |  To be used as the property name when stored and retrieved from the database. [More details](../fields/overview#field-names).   
`**label**` |  Text used as a field label in the Admin Panel or an object with keys for each language.   
`**unique**` |  Enforce that each entry in the Collection has a unique value for this field.   
`**index**` |  Build an [index](../database/indexes) for this field to produce faster queries. Set this field to `true` if your users will perform queries on this field's data often.   
`**minLength**` |  Used by the default validation function to ensure values are of a minimum character length.   
`**maxLength**` |  Used by the default validation function to ensure values are of a maximum character length.   
`**validate**` |  Provide a custom validation function that will be executed on both the Admin Panel and the backend. [More details](../fields/overview#validation).   
`**saveToJWT**` |  If this field is top-level and nested in a config supporting [Authentication](../authentication/overview), include its data in the user JWT.   
`**hooks**` |  Provide Field Hooks to control logic for this field. [More details](../hooks/fields).   
`**access**` |  Provide Field Access Control to denote what users can see and do with this field's data. [More details](../access-control/fields).   
`**hidden**` |  Restrict this field's visibility from all APIs entirely. Will still be saved to the database, but will not appear in any API or the Admin Panel.   
`**defaultValue**` |  Provide data to be used for this field's default value. [More details](../fields/overview#default-values).   
`**localized**` |  Enable localization for this field. Requires [localization to be enabled](../configuration/localization) in the Base config.   
`**required**` |  Require this field to have a value.   
`**admin**` |  Admin-specific configuration. See below for more detail.   
`**custom**` |  Extension point for adding custom data (e.g. for plugins)   
`**typescriptSchema**` |  Override field type generation with providing a JSON schema   
`**virtual**` |  Provide `true` to disable field in the database, or provide a string path to [link the field with a relationship](../fields/relationship#linking-virtual-fields-with-relationships). See [Virtual Fields](/blog/learn-how-virtual-fields-can-help-solve-common-cms-challenges)  
  
_* An asterisk denotes that a property is required._

## [ Admin Options](/docs/fields/code#admin-options)

To customize the appearance and behavior of the Code Field in the [Admin Panel](../admin/overview), you can use the `admin` option:
```
import type { Field } from 'payload'
    
    
    export const MyCodeField: Field = {
      // ...
      admin: {
        
        // ...
      },
    }
```

The Code Field inherits all of the default admin options from the base [Field Admin Config](./overview#admin-options), plus the following additional options:

Option |  Description   
---|---  
`**language**` |  This property can be set to any language listed [here](https://github.com/microsoft/monaco-editor/tree/main/src/basic-languages).   
`**editorOptions**` |  Options that can be passed to the monaco editor, [view the full list](https://microsoft.github.io/monaco-editor/typedoc/interfaces/editor.IDiffEditorConstructionOptions.html).   
  
## [Example](/docs/fields/code#example)

`collections/ExampleCollection.ts
```
import type { CollectionConfig } from 'payload'
    
    
    export const ExampleCollection: CollectionConfig = {
      slug: 'example-collection',
      fields: [
        {
          name: 'trackingCode', // required
          type: 'code', // required
          required: true,
          admin: {
            language: 'javascript',
          },
        },
      ],
    }
```

## [Custom Components](/docs/fields/code#custom-components)### [Field](/docs/fields/code#field)#### [Server Component](/docs/fields/code#server-component)
```
import type React from 'react'
    import { CodeField } from '@payloadcms/ui'
    import type { CodeFieldServerComponent } from 'payload'
    
    
    export const CustomCodeFieldServer: CodeFieldServerComponent = ({
      clientField,
      path,
      schemaPath,
      permissions,
    }) => {
      return (
        <CodeField
          field={clientField}
          path={path}
          schemaPath={schemaPath}
          permissions={permissions}
        />
      )
    }
```

#### [Client Component](/docs/fields/code#client-component)
```
'use client'
    import React from 'react'
    import { CodeField } from '@payloadcms/ui'
    import type { CodeFieldClientComponent } from 'payload'
    
    
    export const CustomCodeFieldClient: CodeFieldClientComponent = (props) => {
      return <CodeField {...props} />
    }
```

### [Label](/docs/fields/code#label)#### [Server Component](/docs/fields/code#server-component)
```
import React from 'react'
    import { FieldLabel } from '@payloadcms/ui'
    import type { CodeFieldLabelServerComponent } from 'payload'
    
    
    export const CustomCodeFieldLabelServer: CodeFieldLabelServerComponent = ({
      clientField,
      path,
    }) => {
      return (
        <FieldLabel
          label={clientField?.label || clientField?.name}
          path={path}
          required={clientField?.required}
        />
      )
    }
```

#### [Client Component](/docs/fields/code#client-component)
```
'use client'
    import React from 'react'
    import { FieldLabel } from '@payloadcms/ui'
    import type { CodeFieldLabelClientComponent } from 'payload'
    
    
    export const CustomCodeFieldLabelClient: CodeFieldLabelClientComponent = ({
      field,
      path,
    }) => {
      return (
        <FieldLabel
          label={field?.label || field?.name}
          path={path}
          required={field?.required}
        />
      )
    }
```

[Next Collapsible Field](/docs/fields/collapsible)
