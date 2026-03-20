<a id="page-66"></a>
---
url: https://payloadcms.com/docs/admin/react-hooks
---

# React Hooks

Payload provides a variety of powerful [React Hooks](https://react.dev/reference/react-dom/hooks) that can be used within your own [Custom Components](../custom-components/overview), such as [Custom Fields](../fields/overview#custom-components). With them, you can interface with Payload itself to build just about any type of complex customization you can think of.

**Reminder:** All Custom Components are [React Server Components](https://react.dev/reference/rsc/server-components) by default. Hooks, on the other hand, are only available in client-side environments. To use hooks, [ensure your component is a client component](../custom-components/overview#client-components).

## [useField](/docs/admin/react-hooks#usefield)

The `useField` hook is used internally within all field components. It manages sending and receiving a field's state from its parent form. When you build a [Custom Field Component](../fields/overview#custom-components), you will be responsible for sending and receiving the field's `value` to and from the form yourself.

To do so, import the `useField` hook as follows:
```
'use client'
    import type { TextFieldClientComponent } from 'payload'
    import { useField } from '@payloadcms/ui'
    
    
    export const CustomTextField: TextFieldClientComponent = ({ path }) => {
      const { value, setValue } = useField({ path }) 
    
    
      return (
        <div>
          <p>{path}</p>
          <input
            onChange={(e) => {
              setValue(e.target.value)
            }}
            value={value}
          />
        </div>
      )
    }
```

The `useField` hook accepts the following arguments:

Property |  Description   
---|---  
`path` |  If you do not provide a `path`, `name` will be used instead. This is the path to the field in the form data.   
`validate` |  A validation function executed client-side _before_ submitting the form to the server. Different than [Field-level Validation](../fields/overview#validation) which runs strictly on the server.   
`disableFormData` |  If `true`, the field will not be included in the form data when the form is submitted.   
`hasRows` |  If `true`, the field will be treated as a field with rows. This is useful for fields like `array` and `blocks`.   
  
The `useField` hook returns the following object:
```
type FieldType<T> = {
      errorMessage?: string
      errorPaths?: string[]
      filterOptions?: FilterOptionsResult
      formInitializing: boolean
      formProcessing: boolean
      formSubmitted: boolean
      initialValue?: T
      path: string
      permissions: FieldPermissions
      readOnly?: boolean
      rows?: Row[]
      schemaPath: string
      setValue: (val: unknown, disableModifyingForm?: boolean) => void
      showError: boolean
      valid?: boolean
      value: T
    }
```

## [useFormFields](/docs/admin/react-hooks#useformfields)

There are times when a custom field component needs to have access to data from other fields, and you have a few options to do so. The `useFormFields` hook is a powerful and highly performant way to retrieve a form's field state, as well as to retrieve the `dispatchFields` method, which can be helpful for setting other fields form states.

**This hook is great for retrieving only certain fields from form state** because it ensures that it will only cause a rerender when the items that you ask for change.

Thanks to the awesome package [`use-context-selector`](https://github.com/dai-shi/use-context-selector), you can retrieve a specific field's state easily. This is ideal because you can ensure you have an up-to-date field state, and your component will only re-render when _that field's state_ changes.

You can pass a Redux-like selector into the hook, which will ensure that you retrieve only the field that you want. The selector takes an argument with type of `[fields: Fields, dispatch: React.Dispatch<Action>]]`.
```
'use client'
    import { useFormFields } from '@payloadcms/ui'
    
    
    const MyComponent: React.FC = () => {
      // Get only the `amount` field state, and only cause a rerender when that field changes
      const amount = useFormFields(([fields, dispatch]) => fields.amount)
    
    
      // Do the same thing as above, but to the `feePercentage` field
      const feePercentage = useFormFields(
        ([fields, dispatch]) => fields.feePercentage,
      )
    
    
      if (
        typeof amount?.value !== 'undefined' &&
        typeof feePercentage?.value !== 'undefined'
      ) {
        return <span>The fee is ${(amount.value * feePercentage.value) / 100}</span>
      }
    }
```

Be aware: in the example above, `MyComponent` may re-render if an ancestor component re-renders or if any of its props change (standard React behavior), but not because any fields other than `amount` or `feePercentage` changed.

## [useAllFormFields](/docs/admin/react-hooks#useallformfields)

**To retrieve more than one field** , you can use the `useAllFormFields` hook. Unlike the `useFormFields` hook, this hook does not accept a "selector", and it always returns an array with type of `[fields: Fields, dispatch: React.Dispatch<Action>]]`.

**Warning:** Your component will re-render when _any_ field changes, so use this hook only if you absolutely need to.

You can do lots of powerful stuff by retrieving the full form state, like using built-in helper functions to reduce field state to values only, or to retrieve sibling data by path.
```
'use client'
    import { useAllFormFields } from '@payloadcms/ui'
    import { reduceFieldsToValues, getSiblingData } from 'payload/shared'
    
    
    const ExampleComponent: React.FC = () => {
      // the `fields` const will be equal to all fields' state,
      // and the `dispatchFields` method is usable to send field state up to the form
      const [fields, dispatchFields] = useAllFormFields();
    
    
      // Pass in fields, and indicate if you'd like to "unflatten" field data.
      // The result below will reflect the data stored in the form at the given time
      const formData = reduceFieldsToValues(fields, true);
    
    
      // Pass in field state and a path,
      // and you will be sent all sibling data of the path that you've specified
      const siblingData = getSiblingData(fields, 'someFieldName');
    
    
      return (
        // return some JSX here if necessary
      )
    };
```

#### [Updating other fields' values](/docs/admin/react-hooks#updating-other-fields-values)

If you are building a Custom Component, then you should use `setValue` which is returned from the `useField` hook to programmatically set your field's value. But if you're looking to update _another_ field's value, you can use `dispatchFields` returned from `useAllFormFields`.

You can send the following actions to the `dispatchFields` function.

Action |  Description   
---|---  
`**ADD_ROW**` |  Adds a row of data (useful in array / block field data)   
`**DUPLICATE_ROW**` |  Duplicates a row of data (useful in array / block field data)   
`**MODIFY_CONDITION**` |  Updates a field's conditional logic result (true / false)   
`**MOVE_ROW**` |  Moves a row of data (useful in array / block field data)   
`**REMOVE**` |  Removes a field from form state   
`**REMOVE_ROW**` |  Removes a row of data from form state (useful in array / block field data)   
`**REPLACE_STATE**` |  Completely replaces form state   
`**UPDATE**` |  Update any property of a specific field's state   
  
To see types for each action supported within the `dispatchFields` hook, check out the Form types [here](https://github.com/payloadcms/payload/blob/main/packages/ui/src/forms/Form/types.ts).

## [useForm](/docs/admin/react-hooks#useform)

The `useForm` hook can be used to interact with the form itself, and sends back many methods that can be used to reactively fetch form state without causing rerenders within your components each time a field is changed. This is useful if you have action-based callbacks that your components fire, and need to interact with form state _based on a user action_.

**Warning:**

This hook is optimized to avoid causing rerenders when fields change, and as such, its `fields` property will be out of date. You should only leverage this hook if you need to perform actions against the form in response to your users' actions. Do not rely on its returned "fields" as being up-to-date. They will be removed from this hook's response in an upcoming version.

The `useForm` hook returns an object with the following properties:

Action| Description| Example  
---|---|---  
`**fields**`|  Deprecated. This property cannot be relied on as up-to-date.|   
`**submit**`|  Method to trigger the form to submit|   
`**dispatchFields**`|  Dispatch actions to the form field state|   
`**validateForm**`|  Trigger a validation of the form state|   
`**createFormData**`|  Create a `multipart/form-data` object from the current form's state|   
`**disabled**`|  Boolean denoting whether or not the form is disabled|   
`**getFields**`|  Gets all fields from state|   
`**getField**`|  Gets a single field from state by path|   
`**getData**`|  Returns the data stored in the form|   
`**getSiblingData**`|  Returns form sibling data for the given field path|   
`**setModified**`|  Set the form's `modified` state|   
`**setProcessing**`|  Set the form's `processing` state|   
`**setSubmitted**`|  Set the form's `submitted` state|   
`**formRef**`|  The ref from the form HTML element|   
`**reset**`|  Method to reset the form to its initial state|   
`**addFieldRow**`|  Method to add a row on an array or block field|   
`**removeFieldRow**`|  Method to remove a row from an array or block field|   
`**replaceFieldRow**`|  Method to replace a row from an array or block field|   
  
## [useDocumentForm](/docs/admin/react-hooks#usedocumentform)

The `useDocumentForm` hook works the same way as the useForm hook, but it always gives you access to the top-level `Form` of a document. This is useful if you need to access the document's `Form` context from within a child `Form`.

An example where this could happen would be custom components within lexical blocks, as lexical blocks initialize their own child `Form`.
```
'use client'
    
    
    import { useDocumentForm } from '@payloadcms/ui'
    
    
    const MyComponent: React.FC = () => {
      const { fields: parentDocumentFields } = useDocumentForm()
    
    
      return (
        <p>
          The document's Form has ${Object.keys(parentDocumentFields).length} fields
        </p>
      )
    }
```

## [useCollapsible](/docs/admin/react-hooks#usecollapsible)

The `useCollapsible` hook allows you to control parent collapsibles:

Property |  Description   
---|---  
`**isCollapsed**` |  State of the collapsible. `true` if open, `false` if collapsed.   
`**isVisible**` |  If nested, determine if the nearest collapsible is visible. `true` if no parent is closed, `false` otherwise.   
`**toggle**` |  Toggles the state of the nearest collapsible.   
`**isWithinCollapsible**` |  Determine when you are within another collapsible.   
  
**Example:**
```
'use client'
    import React from 'react'
    
    
    import { useCollapsible } from '@payloadcms/ui'
    
    
    const CustomComponent: React.FC = () => {
      const { isCollapsed, toggle } = useCollapsible()
    
    
      return (
        <div>
          <p className="field-type">I am {isCollapsed ? 'closed' : 'open'}</p>
          <button onClick={toggle} type="button">
            Toggle
          </button>
        </div>
      )
    }
```

## [useDocumentInfo](/docs/admin/react-hooks#usedocumentinfo)

The `useDocumentInfo` hook provides information about the current document being edited, including the following:

Property |  Description   
---|---  
`**action**` |  The URL attached to the action attribute on the underlying form element, which specifies where to send the form data when the form is submitted.   
`**apiURL**` |  The API URL for the current document.   
`**collectionSlug**` |  The slug of the collection if editing a collection document.   
`**currentEditor**` |  The user currently editing the document.   
`**docConfig**` |  Either the Collection or Global config of the document, depending on what is being edited.   
`**docPermissions**` |  The current document's permissions. Fallback to collection permissions when no id is present.   
`**documentIsLocked**` |  Whether the document is currently locked by another user. [More details](./locked-documents).   
`**getDocPermissions**` |  Method to retrieve document-level permissions.   
`**getDocPreferences**` |  Method to retrieve document-level user preferences. [More details](./preferences).   
`**globalSlug**` |  The slug of the global if editing a global document.   
`**hasPublishedDoc**` |  Whether the document has a published version.   
`**hasPublishPermission**` |  Whether the current user has permission to publish the document.   
`**hasSavePermission**` |  Whether the current user has permission to save the document.   
`**id**` |  If the doc is a collection, its ID will be returned.   
`**incrementVersionCount**` |  Method to increment the version count of the document.   
`**initialData**` |  The initial data of the document.   
`**isEditing**` |  Whether the document is being edited (as opposed to created).   
`**isInitializing**` |  Whether the document info is still initializing.   
`**isLocked**` |  Whether the document is locked. [More details](./locked-documents).   
`**lastUpdateTime**` |  Timestamp of the last update to the document.   
`**mostRecentVersionIsAutosaved**` |  Whether the most recent version is an autosaved version.   
`**preferencesKey**` |  The `preferences` key to use when interacting with document-level user preferences. [More details](./preferences).   
`**data**` |  The saved data of the document.   
`**setDocFieldPreferences**` |  Method to set preferences for a specific field. [More details](./preferences).   
`**setDocumentTitle**` |  Method to set the document title.   
`**setHasPublishedDoc**` |  Method to update whether the document has been published.   
`**title**` |  The title of the document.   
`**unlockDocument**` |  Method to unlock a document. [More details](./locked-documents).   
`**unpublishedVersionCount**` |  The number of unpublished versions of the document.   
`**updateDocumentEditor**` |  Method to update who is currently editing the document. [More details](./locked-documents).   
`**updateSavedDocumentData**` |  Method to update the saved document data.   
`**uploadStatus**` |  Status of any uploads in progress ('idle', 'uploading', or 'failed').   
`**versionCount**` |  The current version count of the document.   
  
**Example:**
```
'use client'
    import { useDocumentInfo } from '@payloadcms/ui'
    
    
    const LinkFromCategoryToPosts: React.FC = () => {
      const { id } = useDocumentInfo()
    
    
      // id will be undefined on the create form
      if (!id) {
        return null
      }
    
    
      return (
        <a
          href={`/admin/collections/posts?where[or][0][and][0][category][in][0]=[${id}]`}
        >
          View posts
        </a>
      )
    }
```

## [useListQuery](/docs/admin/react-hooks#uselistquery)

The `useListQuery` hook is used to subscribe to the data, current query, and other properties used within the List View. You can use this hook within any Custom Component rendered within the List View.
```
'use client'
    import { useListQuery } from '@payloadcms/ui'
    
    
    const MyComponent: React.FC = () => {
      const { data, query } = useListQuery()
    
    
      // ...
    }
```

The `useListQuery` hook returns an object with the following properties:

Property |  Description   
---|---  
`**data**` |  The data that is being displayed in the List View.   
`**defaultLimit**` |  The default limit of items to display in the List View.   
`**defaultSort**` |  The default sort order of items in the List View.   
`**handlePageChange**` |  A method to handle page changes in the List View.   
`**handlePerPageChange**` |  A method to handle per page changes in the List View.   
`**handleSearchChange**` |  A method to handle search changes in the List View.   
`**handleSortChange**` |  A method to handle sort changes in the List View.   
`**handleWhereChange**` |  A method to handle where changes in the List View.   
`**modified**` |  Whether the query has been changed from its [Query Preset](../query-presets/overview).   
`**query**` |  The current query that is being used to fetch the data in the List View.   
  
## [useSelection](/docs/admin/react-hooks#useselection)

The `useSelection` hook provides information on the selected rows in the List view as well as helper methods to simplify selection. The `useSelection` hook returns an object with the following properties:

Property |  Description   
---|---  
`**count**` |  The number of currently selected rows.   
`**getQueryParams**` |  A function that generates a query string based on the current selection state and optional additional filtering parameters.   
`**selectAll**` |  An enum value representing the selection range: `'allAvailable'`, `'allInPage'`, `'none'`, and `'some'`. The enum, `SelectAllStatus`, is exported for easier comparisons.   
`**selected**` |  A map of document id keys and boolean values representing their selection status.   
`**setSelection**` |  A function that toggles the selection status of a document row.   
`**toggleAll**` |  A function that toggles selection for all documents on the current page or selects all available documents when passed `true`.   
`**totalDocs**` |  The number of total documents in the collection.   
  
**Example:**
```
'use client'
    import { useSelection } from '@payloadcms/ui'
    
    
    const MyComponent: React.FC = () => {
      const { count, toggleAll, totalDocs } = useSelection()
    
    
      return (
        <>
          <span>
            Selected {count} out of {totalDocs} docs!
          </span>
          <button type="button" onClick={() => toggleAll(true)}>
            Toggle All Selections
          </button>
        </>
      )
    }
```

## [useLocale](/docs/admin/react-hooks#uselocale)

In any Custom Component you can get the selected locale object with the `useLocale` hook. `useLocale` gives you the full locale object, consisting of a `label`, `rtl`(right-to-left) property, and then `code`. Here is a simple example:
```
'use client'
    import { useLocale } from '@payloadcms/ui'
    
    
    const Greeting: React.FC = () => {
      const locale = useLocale()
    
    
      const trans = {
        en: 'Hello',
        es: 'Hola',
      }
    
    
      return <span> {trans[locale.code]} </span>
    }
```

## [useAuth](/docs/admin/react-hooks#useauth)

Useful to retrieve info about the currently logged in user as well as methods for interacting with it. It sends back an object with the following properties:

Property |  Description   
---|---  
`**user**` |  The currently logged in user   
`**logOut**` |  A method to log out the currently logged in user   
`**refreshCookie**` |  A method to trigger the silent refreshing of a user's auth token   
`**setToken**` |  Set the token of the user, to be decoded and used to reset the user and token in memory   
`**token**` |  The logged in user's token (useful for creating preview links, etc.)   
`**refreshPermissions**` |  Load new permissions (useful when content that affects permissions has been changed)   
`**permissions**` |  The permissions of the current user 
```
'use client'
    import { useAuth } from '@payloadcms/ui'
    import type { User } from '../payload-types.ts'
    
    
    const Greeting: React.FC = () => {
      const { user } = useAuth<User>()
    
    
      return <span>Hi, {user.email}!</span>
    }
```  
  
## [useConfig](/docs/admin/react-hooks#useconfig)

Used to retrieve the Payload [Client Config](../custom-components/overview#accessing-the-payload-config).
```
'use client'
    import { useConfig } from '@payloadcms/ui'
    
    
    const MyComponent: React.FC = () => {
      const { config } = useConfig()
    
    
      return <span>{config.serverURL}</span>
    }
```

If you need to retrieve a specific collection or global config by its slug, `getEntityConfig` is the most efficient way to do so:
```
'use client'
    import { useConfig } from '@payloadcms/ui'
    
    
    const MyComponent: React.FC = () => {
      const { getEntityConfig } = useConfig()
      const mediaConfig = getEntityConfig({ collectionSlug: 'media' })
    
    
      return (
        <span>The media collection has {mediaConfig.fields.length} fields.</span>
      )
    }
```

## [useEditDepth](/docs/admin/react-hooks#useeditdepth)

Sends back how many editing levels "deep" the current component is. Edit depth is relevant while adding new documents / editing documents in modal windows and other cases.
```
'use client'
    import { useEditDepth } from '@payloadcms/ui'
    
    
    const MyComponent: React.FC = () => {
      const editDepth = useEditDepth()
    
    
      return <span>My component is {editDepth} levels deep</span>
    }
```

## [usePreferences](/docs/admin/react-hooks#usepreferences)

Returns methods to set and get user preferences. More info can be found [here](../admin/preferences).

## [useTheme](/docs/admin/react-hooks#usetheme)

Returns the currently selected theme (`light`, `dark` or `auto`), a set function to update it and a boolean `autoMode`, used to determine if the theme value should be set automatically based on the user's device preferences.
```
'use client'
    import { useTheme } from '@payloadcms/ui'
    
    
    const MyComponent: React.FC = () => {
      const { autoMode, setTheme, theme } = useTheme()
    
    
      return (
        <>
          <span>
            The current theme is {theme} and autoMode is {autoMode}
          </span>
          <button
            type="button"
            onClick={() =>
              setTheme((prev) => (prev === 'light' ? 'dark' : 'light'))
            }
          >
            Toggle theme
          </button>
        </>
      )
    }
```

## [useTableColumns](/docs/admin/react-hooks#usetablecolumns)

Returns properties and methods to manipulate table columns:

Property |  Description   
---|---  
`**columns**` |  The current state of columns including their active status and configuration   
`**LinkedCellOverride**` |  A component override for linked cells in the table   
`**moveColumn**` |  A method to reorder columns. Accepts `{ fromIndex: number, toIndex: number }` as arguments   
`**resetColumnsState**` |  A method to reset columns back to their default configuration as defined in the collection config   
`**setActiveColumns**` |  A method to set specific columns to active state while preserving the existing column order. Accepts an array of column names to activate   
`**toggleColumn**` |  A method to toggle a single column's visibility. Accepts a column name as string 
```
'use client'
    import { useTableColumns } from '@payloadcms/ui'
    
    
    const MyComponent: React.FC = () => {
      const { setActiveColumns, resetColumnsState } = useTableColumns()
    
    
      const activateSpecificColumns = () => {
        // Only activates the id and createdAt columns
        // Other columns retain their current active/inactive state
        // The original column order is preserved
        setActiveColumns(['id', 'createdAt'])
      }
    
    
      const resetToDefaults = () => {
        // Resets to the default columns defined in the collection config
        resetColumnsState()
      }
    
    
      return (
        <div>
          <button type="button" onClick={activateSpecificColumns}>
            Activate Specific Columns
          </button>
          <button type="button" onClick={resetToDefaults}>
            Reset To Defaults
          </button>
        </div>
      )
    }
```  
  
## [useDocumentEvents](/docs/admin/react-hooks#usedocumentevents)

The `useDocumentEvents` hook provides a way of subscribing to cross-document events, such as updates made to nested documents within a drawer. This hook will report document events that are outside the scope of the document currently being edited. This hook provides the following:

Property |  Description   
---|---  
`**mostRecentUpdate**` |  An object containing the most recently updated document. It contains the `entitySlug`, `id` (if collection), and `updatedAt` properties   
`**reportUpdate**` |  A method used to report updates to documents. It accepts the same arguments as the `mostRecentUpdate` property.   
  
**Example:**
```
'use client'
    import { useDocumentEvents } from '@payloadcms/ui'
    
    
    const ListenForUpdates: React.FC = () => {
      const { mostRecentUpdate } = useDocumentEvents()
    
    
      return <span>{JSON.stringify(mostRecentUpdate)}</span>
    }
```

Right now the `useDocumentEvents` hook only tracks recently updated documents, but in the future it will track more document-related events as needed, such as document creation, deletion, etc.

## [useStepNav](/docs/admin/react-hooks#usestepnav)

The `useStepNav` hook provides a way to change the step-nav breadcrumb links in the app header.

Property |  Description   
---|---  
`**setStepNav**` |  A state setter function which sets the `stepNav` array.   
`**stepNav**` |  A `StepNavItem` array where each `StepNavItem` has a label and optionally a url.   
  
**Example:**
```
'use client'
    import { type StepNavItem, useStepNav } from '@payloadcms/ui'
    import { useEffect } from 'react'
    
    
    export const MySetStepNavComponent: React.FC<{
      nav: StepNavItem[]
    }> = ({ nav }) => {
      const { setStepNav } = useStepNav()
    
    
      useEffect(() => {
        setStepNav(nav)
      }, [setStepNav, nav])
    
    
      return null
    }
```

## [usePayloadAPI](/docs/admin/react-hooks#usepayloadapi)

The `usePayloadAPI` hook is a useful tool for making REST API requests to your Payload instance and handling responses reactively. It allows you to fetch and interact with data while automatically updating when parameters change.

This hook returns an array with two elements:

  1. An object containing the API response.
  2. A set of methods to modify request parameters.



**Example:**
```
'use client'
    import { usePayloadAPI } from '@payloadcms/ui'
    
    
    const MyComponent: React.FC = () => {
      // Fetch data from a collection item using its ID
      const [{ data, isError, isLoading }, { setParams }] = usePayloadAPI(
        '/api/posts/123',
        {
          initialParams: { depth: 1 },
        },
      )
    
    
      if (isLoading) return <p>Loading...</p>
      if (isError) return <p>Error occurred while fetching data.</p>
    
    
      return (
        <div>
          <h1>{data?.title}</h1>
          <button onClick={() => setParams({ cacheBust: Date.now() })}>
            Refresh Data
          </button>
        </div>
      )
    }
```

**Arguments:**

Property |  Description   
---|---  
`**url**` |  The API endpoint to fetch data from. Relative URLs will be prefixed with the Payload API route.   
`**options**` |  An object containing initial request parameters and initial state configuration.   
  
The `options` argument accepts the following properties:

Property |  Description   
---|---  
`**initialData**` |  Uses this data instead of making an initial request. If not provided, the request runs immediately.   
`**initialParams**` |  Defines the initial parameters to use in the request. Defaults to an empty object `{}`.   
  
**Returned Value:**

The first item in the returned array is an object containing the following properties:

Property |  Description   
---|---  
`**data**` |  The API response data.   
`**isError**` |  A boolean indicating whether the request failed.   
`**isLoading**` |  A boolean indicating whether the request is in progress.   
  
The second item is an object with the following methods:

Property |  Description   
---|---  
`**setParams**` |  Updates request parameters, triggering a refetch if needed.   
  
#### [Updating Data](/docs/admin/react-hooks#updating-data)

The `setParams` function can be used to update the request and trigger a refetch:
```
setParams({ depth: 2 })
```

This is useful for scenarios where you need to trigger another fetch regardless of the `url` argument changing.

## [useRouteTransition](/docs/admin/react-hooks#useroutetransition)

Route transitions are useful in showing immediate visual feedback to the user when navigating between pages. This is especially useful on slow networks when navigating to data heavy or process intensive pages.

By default, any instances of `Link` from `@payloadcms/ui` will trigger route transitions by default.
```
import { Link } from '@payloadcms/ui'
    
    
    const MyComponent = () => {
      return <Link href="/somewhere">Go Somewhere</Link>
    }
```

You can also trigger route transitions programmatically, such as when using `router.push` from `next/router`. To do this, wrap your function calls with the `startRouteTransition` method provided by the `useRouteTransition` hook.
```
'use client'
    import React, { useCallback } from 'react'
    import { useTransition } from '@payloadcms/ui'
    import { useRouter } from 'next/navigation'
    
    
    const MyComponent: React.FC = () => {
      const router = useRouter()
      const { startRouteTransition } = useRouteTransition()
    
    
      const redirectSomewhere = useCallback(() => {
        startRouteTransition(() => router.push('/somewhere'))
      }, [startRouteTransition, router])
    
    
      // ...
    }
```

[Next Customizing CSS & SCSS](/docs/admin/customizing-css)
