<a id="page-36"></a>
---
url: https://payloadcms.com/docs/fields/text
---

# Text Field

The Text Field is one of the most commonly used fields. It saves a string to the database and provides the [Admin Panel](../admin/overview) with a simple text input.

![Shows a text field and read-only text field in the Payload Admin Panel](https://payloadcms.com/images/docs/fields/text.png)

Admin Panel screenshot of a Text field and read-only Text field

To add a Text Field, set the `type` to `text` in your [Field Config](./overview):
```
import type { Field } from 'payload'
    
    
    export const MyTextField: Field = {
      // ...
      type: 'text', 
    }
```

## [Config Options](/docs/fields/text#config-options)

Option |  Description   
---|---  
`**name**` * |  To be used as the property name when stored and retrieved from the database. [More details](../fields/overview#field-names).   
`**label**` |  Text used as a field label in the Admin Panel or an object with keys for each language.   
`**unique**` |  Enforce that each entry in the Collection has a unique value for this field.   
`**minLength**` |  Used by the default validation function to ensure values are of a minimum character length.   
`**maxLength**` |  Used by the default validation function to ensure values are of a maximum character length.   
`**validate**` |  Provide a custom validation function that will be executed on both the Admin Panel and the backend. [More details](../fields/overview#validation).   
`**index**` |  Build an [index](../database/indexes) for this field to produce faster queries. Set this field to `true` if your users will perform queries on this field's data often.   
`**saveToJWT**` |  If this field is top-level and nested in a config supporting [Authentication](../authentication/overview), include its data in the user JWT.   
`**hooks**` |  Provide Field Hooks to control logic for this field. [More details](../hooks/fields).   
`**access**` |  Provide Field Access Control to denote what users can see and do with this field's data. [More details](../access-control/fields).   
`**hidden**` |  Restrict this field's visibility from all APIs entirely. Will still be saved to the database, but will not appear in any API or the Admin Panel.   
`**defaultValue**` |  Provide data to be used for this field's default value. [More details](../fields/overview#default-values).   
`**localized**` |  Enable localization for this field. Requires [localization to be enabled](../configuration/localization) in the Base config.   
`**required**` |  Require this field to have a value.   
`**admin**` |  Admin-specific configuration. More details.   
`**custom**` |  Extension point for adding custom data (e.g. for plugins)   
`**hasMany**` |  Makes this field an ordered array of text instead of just a single text.   
`**minRows**` |  Minimum number of texts in the array, if `hasMany` is set to true.   
`**maxRows**` |  Maximum number of texts in the array, if `hasMany` is set to true.   
`**typescriptSchema**` |  Override field type generation with providing a JSON schema   
`**virtual**` |  Provide `true` to disable field in the database, or provide a string path to [link the field with a relationship](../fields/relationship#linking-virtual-fields-with-relationships). See [Virtual Fields](/blog/learn-how-virtual-fields-can-help-solve-common-cms-challenges)  
  
_* An asterisk denotes that a property is required._

## [ Admin Options](/docs/fields/text#admin-options)

To customize the appearance and behavior of the Text Field in the [Admin Panel](../admin/overview), you can use the `admin` option:
```
import type { Field } from 'payload'
    
    
    export const MyTextField: Field = {
      // ...
      admin: {
        
        // ...
      },
    }
```

The Text Field inherits all of the default admin options from the base [Field Admin Config](./overview#admin-options), plus the following additional options:

Option |  Description   
---|---  
`**placeholder**` |  Set this property to define a placeholder string in the text input.   
`**autoComplete**` |  Set this property to a string that will be used for browser autocomplete.   
`**rtl**` |  Override the default text direction of the Admin Panel for this field. Set to `true` to force right-to-left text direction.   
  
## [Example](/docs/fields/text#example)
```
import type { CollectionConfig } from 'payload'
    
    
    export const ExampleCollection: CollectionConfig = {
      slug: 'example-collection',
      fields: [
        {
          name: 'pageTitle', // required
          type: 'text', // required
          required: true,
        },
      ],
    }
```

## [Custom Components](/docs/fields/text#custom-components)### [Field](/docs/fields/text#field)#### [Server Component](/docs/fields/text#server-component)
```
import type React from 'react'
    import { TextField } from '@payloadcms/ui'
    import type { TextFieldServerComponent } from 'payload'
    
    
    export const CustomTextFieldServer: TextFieldServerComponent = ({
      clientField,
      path,
      schemaPath,
      permissions,
    }) => {
      return (
        <TextField
          field={clientField}
          path={path}
          schemaPath={schemaPath}
          permissions={permissions}
        />
      )
    }
```

#### [Client Component](/docs/fields/text#client-component)
```
'use client'
    import React from 'react'
    import { TextField } from '@payloadcms/ui'
    import type { TextFieldClientComponent } from 'payload'
    
    
    export const CustomTextFieldClient: TextFieldClientComponent = (props) => {
      return <TextField {...props} />
    }
```

### [Label](/docs/fields/text#label)#### [Server Component](/docs/fields/text#server-component)
```
import React from 'react'
    import { FieldLabel } from '@payloadcms/ui'
    import type { TextFieldLabelServerComponent } from 'payload'
    
    
    export const CustomTextFieldLabelServer: TextFieldLabelServerComponent = ({
      clientField,
      path,
      required,
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

#### [Client Component](/docs/fields/text#client-component)
```
'use client'
    import React from 'react'
    import { FieldLabel } from '@payloadcms/ui'
    import type { TextFieldLabelClientComponent } from 'payload'
    
    
    export const CustomTextFieldLabelClient: TextFieldLabelClientComponent = ({
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

## [Slug Field](/docs/fields/text#slug-field)

The slug field is experimental and may change, or even be removed, in future releases. Use at your own risk.

One common use case for the Text Field is to create a "slug" for a document. A slug is a unique, indexed, URL-friendly string that identifies a particular document, often used to construct the URL of a webpage.

Payload provides a built-in Slug Field so you don't have to built one from scratch. This field automatically generates a slug based on the value of another field, such as a title or name field. It provides UI to lock and unlock the field to protect its value, as well as to re-generate the slug on-demand.

To add a Slug Field, import the `slugField` into your field schema:
```
import { slugField } from 'payload'
    import type { CollectionConfig } from 'payload'
    
    
    export const ExampleCollection: CollectionConfig = {
      // ...
      fields: [
        // ...
        
        slugField(),
        
      ],
    }
```

The slug field exposes a few top-level config options for easy customization:

Option |  Description   
---|---  
`name` |  To be used as the slug field's name. Defaults to `slug`.   
`overrides` |  A function that receives the default fields so you can override on a granular level. See example below. More details.   
`checkboxName` |  To be used as the name for the `generateSlug` checkbox field. Defaults to `generateSlug`.   
`useAsSlug` |  The name of the top-level field to use when generating the slug. This field must exist in the same collection. Defaults to `title`.   
`localized` |  Enable localization on the `slug` and `generateSlug` fields. Defaults to `false`.   
`position` |  The position of the slug field. [More details](./overview#admin-options).   
`required` |  Require the slug field. Defaults to `true`.   
`slugify` |  Override the default slugify function. More details.   
  
### [Slug Overrides](/docs/fields/text#slug-overrides)

If the above options aren't sufficient for your use case, you can use the `overrides` function to customize the slug field at a granular level. The `overrides` function receives the default fields that make up the slug field, and you can modify them to any extent you need.
```
import { slugField } from 'payload'
    import type { CollectionConfig } from 'payload'
    
    
    export const ExampleCollection: CollectionConfig = {
      // ...
      fields: [
        // ...
        
        slugField({
          overrides: (defaultField) => {
            defaultField.fields[1].label = 'Custom Slug Label'
            return defaultField
          },
        }),
        
      ],
    }
```

### [Custom Slugify Function](/docs/fields/text#custom-slugify-function)

You can also override the default slugify function of the slug field. This is necessary if the slug requires special treatment, such as character encoding, additional language support, etc.

This functions receives the value of the `useAsSlug` field as `valueToSlugify` and must return a string.

For example, if you wanted to use the [`slugify`](https://www.npmjs.com/package/slugify) package, you could do something like this:
```
import type { CollectionConfig } from 'payload'
    import { slugField } from 'payload'
    import slugify from 'slugify'
    
    
    export const MyCollection: CollectionConfig = {
      // ...
      fields: [
        // ...
        slugField({
          slugify: ({ valueToSlugify }) =>
            slugify(valueToSlugify, {
              // ...additional `slugify` options here
            }),
        }),
      ],
    }
```

The following args are provided to the custom `slugify` function:

Argument |  Type |  Description   
---|---|---  
`valueToSlugify` |  `string` |  The value of the field specified in `useAsSlug`.   
`data` |  `object` |  The full document data being saved.   
`req` |  `PayloadRequest` |  The Payload request object.   
  
[Next Textarea Field](/docs/fields/textarea)
