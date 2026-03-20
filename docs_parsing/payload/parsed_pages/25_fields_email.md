<a id="page-25"></a>
---
url: https://payloadcms.com/docs/fields/email
---

# Email Field

The Email Field enforces that the value provided is a valid email address.

![Shows an Email field in the Payload Admin Panel](https://payloadcms.com/images/docs/fields/email.png)

Admin Panel screenshot of an Email field

To create an Email Field, set the `type` to `email` in your [Field Config](./overview):
```
import type { Field } from 'payload'
    
    
    export const MyEmailField: Field = {
      // ...
      type: 'email', 
    }
```

## [Config Options](/docs/fields/email#config-options)

Option |  Description   
---|---  
`**name**` * |  To be used as the property name when stored and retrieved from the database. [More details](../fields/overview#field-names).   
`**label**` |  Text used as a field label in the Admin Panel or an object with keys for each language.   
`**unique**` |  Enforce that each entry in the Collection has a unique value for this field.   
`**index**` |  Build an [index](../database/indexes) for this field to produce faster queries. Set this field to `true` if your users will perform queries on this field's data often.   
`**validate**` |  Provide a custom validation function that will be executed on both the Admin Panel and the backend. [More details](../fields/overview#validation).   
`**saveToJWT**` |  If this field is top-level and nested in a config supporting [Authentication](../authentication/overview), include its data in the user JWT.   
`**hooks**` |  Provide Field Hooks to control logic for this field. [More details](../hooks/fields).   
`**access**` |  Provide Field Access Control to denote what users can see and do with this field's data. [More details](../access-control/fields).   
`**hidden**` |  Restrict this field's visibility from all APIs entirely. Will still be saved to the database, but will not appear in any API or the Admin Panel.   
`**defaultValue**` |  Provide data to be used for this field's default value. [More details](../fields/overview#default-values).   
`**localized**` |  Enable localization for this field. Requires [localization to be enabled](../configuration/localization) in the Base config.   
`**required**` |  Require this field to have a value.   
`**admin**` |  Admin-specific configuration. More details.   
`**custom**` |  Extension point for adding custom data (e.g. for plugins)   
`**typescriptSchema**` |  Override field type generation with providing a JSON schema   
`**virtual**` |  Provide `true` to disable field in the database, or provide a string path to [link the field with a relationship](../fields/relationship#linking-virtual-fields-with-relationships). See [Virtual Fields](/blog/learn-how-virtual-fields-can-help-solve-common-cms-challenges)  
  
_* An asterisk denotes that a property is required._

## [ Admin Options](/docs/fields/email#admin-options)

To customize the appearance and behavior of the Email Field in the [Admin Panel](../admin/overview), you can use the `admin` option:
```
import type { Field } from 'payload'
    
    
    export const MyEmailField: Field = {
      // ...
      admin: {
        
        // ...
      },
    }
```

The Email Field inherits all of the default admin options from the base [Field Admin Config](./overview#admin-options), plus the following additional options:

Property |  Description   
---|---  
`**placeholder**` |  Set this property to define a placeholder string for the field.   
`**autoComplete**` |  Set this property to a string that will be used for browser autocomplete.   
  
## [Example](/docs/fields/email#example)
```
import type { CollectionConfig } from 'payload'
    
    
    export const ExampleCollection: CollectionConfig = {
      slug: 'example-collection',
      fields: [
        {
          name: 'contact', // required
          type: 'email', // required
          label: 'Contact Email Address',
          required: true,
        },
      ],
    }
```

## [Custom Components](/docs/fields/email#custom-components)### [Field](/docs/fields/email#field)#### [Server Component](/docs/fields/email#server-component)
```
import type React from 'react'
    import { EmailField } from '@payloadcms/ui'
    import type { EmailFieldServerComponent } from 'payload'
    
    
    export const CustomEmailFieldServer: EmailFieldServerComponent = ({
      clientField,
      path,
      schemaPath,
      permissions,
    }) => {
      return (
        <EmailField
          field={clientField}
          path={path}
          schemaPath={schemaPath}
          permissions={permissions}
        />
      )
    }
```

#### [Client Component](/docs/fields/email#client-component)
```
'use client'
    import React from 'react'
    import { EmailField } from '@payloadcms/ui'
    import type { EmailFieldClientComponent } from 'payload'
    
    
    export const CustomEmailFieldClient: EmailFieldClientComponent = (props) => {
      return <EmailField {...props} />
    }
```

### [Label](/docs/fields/email#label)#### [Server Component](/docs/fields/email#server-component)
```
import React from 'react'
    import { FieldLabel } from '@payloadcms/ui'
    import type { EmailFieldLabelServerComponent } from 'payload'
    
    
    export const CustomEmailFieldLabelServer: EmailFieldLabelServerComponent = ({
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

#### [Client Component](/docs/fields/email#client-component)
```
'use client'
    import React from 'react'
    import { FieldLabel } from '@payloadcms/ui'
    import type { EmailFieldLabelClientComponent } from 'payload'
    
    
    export const CustomEmailFieldLabelClient: EmailFieldLabelClientComponent = ({
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

[Next Group Field](/docs/fields/group)

#### Related Guides

  * [How to set up Nodemailer and Resend email adapters in Payload ](/posts/guides/how-to-set-up-email-adapters-in-payload)
