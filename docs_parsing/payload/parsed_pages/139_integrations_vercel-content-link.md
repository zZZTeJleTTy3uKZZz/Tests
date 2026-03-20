<a id="page-139"></a>
---
url: https://payloadcms.com/docs/integrations/vercel-content-link
---

# Vercel Content Link

[Vercel Content Link](https://vercel.com/docs/workflow-collaboration/edit-mode#content-link) will allow your editors to navigate directly from the content rendered on your front-end to the fields in Payload that control it. This requires no changes to your front-end code and very few changes to your Payload Config.

![Versions](https://payloadcms.com/images/docs/vercel-visual-editing.jpg)

Vercel Content Link is an enterprise-only feature and only available for deployments hosted on Vercel. If you are an existing enterprise customer, [contact our sales team](/for-enterprise) for help with your integration.

## [How it works](/docs/integrations/vercel-content-link#how-it-works)

To power Vercel Content Link, Payload embeds Content Source Maps into its API responses. Content Source Maps are invisible, encoded JSON values that include a link back to the field in the CMS that generated the content. When rendered on the page, Vercel detects and decodes these values to display the Content Link interface.

For full details on how the encoding and decoding algorithm works, check out [`@vercel/stega`](https://www.npmjs.com/package/@vercel/stega).

## [Getting Started](/docs/integrations/vercel-content-link#getting-started)

Setting up Payload with Vercel Content Link is easy. First, install the `@payloadcms/plugin-csm` plugin into your project. This plugin requires an API key to install, [contact our sales team](/for-enterprise) if you don't already have one.
```
npm i @payloadcms/plugin-csm
```

Then in the `plugins` array of your Payload Config, call the plugin and enable any collections that require Content Source Maps.
```
import { buildConfig } from 'payload/config'
    import contentSourceMaps from '@payloadcms/plugin-csm'
    
    
    const config = buildConfig({
      collections: [
        {
          slug: 'pages',
          fields: [
            {
              name: 'slug',
              type: 'text',
            },
            {
              name: 'title',
              type: 'text',
            },
          ],
        },
      ],
      plugins: [
        contentSourceMaps({
          collections: ['pages'],
        }),
      ],
    })
    
    
    export default config
```

## [Enabling Content Source Maps](/docs/integrations/vercel-content-link#enabling-content-source-maps)

Now in your Next.js app, you need to add the `encodeSourceMaps` query parameter to your API requests. This will tell Payload to include the Content Source Maps in the API response.

**Note:** For performance reasons, this should only be done when in draft mode or on preview deployments.

#### [REST API](/docs/integrations/vercel-content-link#rest-api)

If you're using the REST API, include the `?encodeSourceMaps=true` search parameter.
```
if (isDraftMode || process.env.VERCEL_ENV === 'preview') {
      const res = await fetch(
        `${process.env.NEXT_PUBLIC_PAYLOAD_CMS_URL}/api/pages?encodeSourceMaps=true&where[slug][equals]=${slug}`,
      )
    }
```

#### [Local API](/docs/integrations/vercel-content-link#local-api)

If you're using the Local API, include the `encodeSourceMaps` via the `context` property.
```
if (isDraftMode || process.env.VERCEL_ENV === 'preview') {
      const res = await payload.find({
        collection: 'pages',
        where: {
          slug: {
            equals: slug,
          },
        },
        context: {
          encodeSourceMaps: true,
        },
      })
    }
```

And that's it! You are now ready to enter Edit Mode and begin visually editing your content.

## [Edit Mode](/docs/integrations/vercel-content-link#edit-mode)

To see Content Link on your site, you first need to visit any preview deployment on Vercel and login using the Vercel Toolbar. When Content Source Maps are detected on the page, a pencil icon will appear in the toolbar. Clicking this icon will enable Edit Mode, highlighting all editable fields on the page in blue.

![Versions](https://payloadcms.com/images/docs/vercel-toolbar.jpg)

## [Troubleshooting](/docs/integrations/vercel-content-link#troubleshooting)### [Date Fields](/docs/integrations/vercel-content-link#date-fields)

The plugin does not encode `date` fields by default, but for some cases like text that uses negative CSS letter-spacing, it may be necessary to split the encoded data out from the rendered text. This way you can safely use the cleaned data as expected.
```
import { vercelStegaSplit } from '@vercel/stega'
    const { cleaned, encoded } = vercelStegaSplit(text)
```

### [Blocks and array fields](/docs/integrations/vercel-content-link#blocks-and-array-fields)

All `blocks` and `array` fields by definition do not have plain text strings to encode. For this reason, they are automatically given an additional `_encodedSourceMap` property, which you can use to enable Content Link on entire _sections_ of your site.

You can then specify the editing container by adding the `data-vercel-edit-target` HTML attribute to any top-level element of your block.
```
<div data-vercel-edit-target>
      <span style={{ display: "none" }}>{_encodedSourceMap}</span>
      {children}
    </div>
```

[Next Building without a DB connection](/docs/production/building-without-a-db-connection)
