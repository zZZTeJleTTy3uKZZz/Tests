<a id="page-8"></a>
---
url: https://payloadcms.com/docs/configuration/localization
---

# Localization

Localization is one of the most important features of a modern CMS. It allows you to manage content in multiple languages, then serve it to your users based on their requested language. This is similar to [I18n](./i18n), but instead of managing translations for your application's interface, you are managing translations for the data itself.

With Localization, you can begin to serve personalized content to your users based on their specific language preferences, such as a multilingual website or multi-site application. There are no limits to the number of locales you can add to your Payload project.

To configure Localization, use the `localization` key in your [Payload Config](./overview):

1

import { buildConfig } from 'payload'

2

3

export default buildConfig({

4

// ...

5

localization: {

6

7

// ...

8

},

9

})

## [Config Options](/docs/configuration/localization#config-options)

Add the `localization` property to your Payload Config to enable Localization project-wide. You'll need to provide a list of all locales that you'd like to support as well as set a few other options.

To configure locales, use the `localization.locales` property in your [Payload Config](./overview):

1

import { buildConfig } from 'payload'

2

3

export default buildConfig({

4

// ...

5

localization: {

6

locales: ['en', 'es', 'de'], // required

7

defaultLocale: 'en', // required

8

},

9

})

You can also define locales using full configuration objects:

1

import { buildConfig } from 'payload'

2

3

export default buildConfig({

4

collections: [

5

// collections go here

6

],

7

localization: {

8

locales: [

9

{

10

label: 'English',

11

code: 'en',

12

},

13

{

14

label: 'Arabic',

15

code: 'ar',

16

// opt-in to setting default text-alignment on Input fields to rtl (right-to-left)

17

// when current locale is rtl

18

rtl: true,

19

},

20

],

21

defaultLocale: 'en', // required

22

fallback: true, // defaults to true

23

},

24

})

**Tip:** Localization works very well alongside [I18n](../configuration/i18n).

The following options are available:

Option |  Description   
---|---  
`**locales**` |  Array of all the languages that you would like to support. More details  
`**defaultLocale**` |  Required string that matches one of the locale codes from the array provided. By default, if no locale is specified, documents will be returned in this locale.   
`**fallback**` |  Boolean enabling "fallback" locale functionality. If a document is requested in a locale, but a field does not have a localized value corresponding to the requested locale, then if this property is enabled, the document will automatically fall back to the fallback locale value. If this property is not enabled, the value will not be populated unless a fallback is explicitly provided in the request. True by default.   
`**filterAvailableLocales**` |  A function that is called with the array of `locales` and the `req`, it should return locales to show in admin UI selector. See more.   
  
### [Locales](/docs/configuration/localization#locales)

The locales array is a list of all the languages that you would like to support. This can be strings for each language code, or full configuration objects for more advanced options.

The locale codes do not need to be in any specific format. It's up to you to define how to represent your locales. Common patterns are to use two-letter ISO 639 language codes or four-letter language and country codes (ISO 3166‑1) such as `en-US`, `en-UK`, `es-MX`, etc.

#### [Locale Object](/docs/configuration/localization#locale-object)

Option |  Description   
---|---  
`**code**` * |  Unique code to identify the language throughout the APIs for `locale` and `fallbackLocale`  
`**label**` |  A string to use for the selector when choosing a language, or an object keyed on the i18n keys for different languages in use.   
`**rtl**` |  A boolean that when true will make the admin UI display in Right-To-Left.   
`**fallbackLocale**` |  The code for this language to fallback to when properties of a document are not present. This can be a single locale or array of locales.   
  
_* An asterisk denotes that a property is required._

#### [ Filter Available Options](/docs/configuration/localization#filter-available-options)

In some projects you may want to filter the available locales shown in the admin UI selector. You can do this by providing a `filterAvailableLocales` function in your Payload Config. This is called on the server side and is passed the array of locales. This means that you can determine what locales are visible in the localizer selection menu at the top of the admin panel. You could do this per user, or implement a function that scopes these to tenants and more. Here is an example using request headers in a multi-tenant application:

1

// ... rest of Payload config

2

localization: {

3

defaultLocale: 'en',

4

locales: ['en', 'es'],

5

filterAvailableLocales: async ({ req, locales }) => {

6

if (getTenantFromCookie(req.headers, 'text')) {

7

const fullTenant = await req.payload.findByID({

8

id: getTenantFromCookie(req.headers, 'text') as string,

9

collection: 'tenants',

10

req,

11

})

12

if (fullTenant && fullTenant.supportedLocales?.length) {

13

return locales.filter((locale) => {

14

return fullTenant.supportedLocales?.includes(locale.code as 'en' | 'es')

15

})

16

}

17

}

18

return locales

19

},

20

}

Since the filtering happens at the root level of the application and its result is not calculated every time you navigate to a new page, you may want to call `router.refresh` in a custom component that watches when values that affect the result change. In the example above, you would want to do this when `supportedLocales` changes on the tenant document.

## [Field Localization](/docs/configuration/localization#field-localization)

Payload Localization works on a **field** level—not a document level. In addition to configuring the base Payload Config to support Localization, you need to specify each field that you would like to localize.

**Here is an example of how to enable Localization for a field:**

1

{

2

name: 'title',

3

type: 'text',

4

localized: true,

5

}

With the above configuration, the `title` field will now be saved in the database as an object of all locales instead of a single string.

All field types with a `name` property support the `localized` property—even the more complex field types like `array`s and `block`s.

**Note:** Enabling Localization for field types that support nested fields will automatically create localized "sets" of all fields contained within the field. For example, if you have a page layout using a blocks field type, you have the choice of either localizing the full layout, by enabling Localization on the top-level blocks field, or only certain fields within the layout.

**Important:** When converting an existing field to or from `localized: true` the data structure in the document will change for this field and so existing data for this field will be lost. Before changing the Localization setting on fields with existing data, you may need to consider a field migration strategy.

## [Status Localization](/docs/configuration/localization#status-localization)

Payload allows you to localize the `status` field for **draft enabled** collections and globals. This lets you manage publication status independently for each locale, ensures the admin UI always shows the status for the selected locale, and unpublish content in a single locale.

**Important:** This feature is **experimental** and currently in beta, you may encounter some limitations or bugs. Please test thoroughly before using in production.

**Two-Step Setup Required:** To enable localized status, you need to set **two** configuration options:

  1. Enable the experimental flag in your main config
  2. Enable it for specific collections or globals

### [Step 1: Enable Experimental Flag](/docs/configuration/localization#step-1-enable-experimental-flag)

First, enable the experimental flag in your main Payload config:

1

import { buildConfig } from 'payload'

2

3

export default buildConfig({

4

experimental: {

5

localizeStatus: true, // Required to enable the feature globally

6

},

7

// ... rest of your config

8

})

### [Step 2: Enable for Collections/Globals](/docs/configuration/localization#step-2-enable-for-collections-globals)

Then, enable it for specific collections or globals:

1

import type { CollectionConfig } from 'payload'

2

3

export const Posts: CollectionConfig = {

4

// ...

5

versions: {

6

drafts: {

7

localizeStatus: true, // Enable for this specific collection

8

},

9

},

10

}

When enabled, the `status` field will be stored as an object keyed by locales:

1

status: {

2

en: 'published',

3

es: 'draft',

4

de: 'published',

5

}

`localizeStatus` is disabled by default, in which case the `status` field returns a single string (`'draft'` or `'published'`) representing the latest document status across all locales.

## [Retrieving Localized Docs](/docs/configuration/localization#retrieving-localized-docs)

When retrieving documents, you can specify which locale you'd like to receive as well as which fallback locale should be used.

#### [REST API](/docs/configuration/localization#rest-api)

REST API locale functionality relies on URL query parameters.

`**?locale=**`

Specify your desired locale by providing the `locale` query parameter directly in the endpoint URL.

`**?fallback-locale=**`

Specify fallback locale to be used by providing the `fallback-locale` query parameter. This can be provided as either a valid locale as provided to your base Payload Config, or `'null'`, `'false'`, or `'none'` to disable falling back.

**Example:**

1

fetch('https://localhost:3000/api/pages?locale=es&fallback-locale=none');

#### [GraphQL API](/docs/configuration/localization#graphql-api)

In the GraphQL API, you can specify `locale` and `fallbackLocale` args to all relevant queries and mutations.

The `locale` arg will only accept valid locales, but locales will be formatted automatically as valid GraphQL enum  
values (dashes or special characters will be converted to underscores, spaces will be removed, etc.). If you are curious  
to see how locales are auto-formatted, you can use the [GraphQL playground](../graphql/overview#graphql-playground).

The `fallbackLocale` arg will accept valid locales, an array of locales, as well as `none` to disable falling back.

**Example:**

1

query {

2

Posts(locale: de, fallbackLocale: none) {

3

docs {

4

title

5

}

6

}

7

}

In GraphQL, specifying the locale at the top level of a query will automatically apply it throughout all nested relationship fields. You can override this behavior by re-specifying locale arguments in nested related document queries.

#### [Local API](/docs/configuration/localization#local-api)

You can specify `locale` as well as `fallbackLocale` within the Local API as well as properties on the `options` argument. The `locale` property will accept any valid locale, and the `fallbackLocale` property will accept any valid locale, array of locales, as well as `'null'`, `'false'`, `false`, and `'none'`.

**Example:**

1

const posts = await payload.find({

2

collection: 'posts',

3

locale: 'es',

4

fallbackLocale: false,

5

})

**Tip:** The REST and Local APIs can return all Localization data in one request by passing 'all' or '*' as the **locale** parameter. The response will be structured so that field values come back as the full objects keyed for each locale instead of the single, translated value.

[Next Environment Variables](/docs/configuration/environment-vars)

#### Community Help Threads

  * [Search on a localized field (i.e.: slug) with fallback ](/community-help/discord/search-on-a-localized-field-ie-slug-with-fallback)
