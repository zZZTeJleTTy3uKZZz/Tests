<a id="page-96"></a>
---
url: https://payloadcms.com/docs/rich-text/migration
---

# Lexical Migration

## [Migrating from Slate](/docs/rich-text/migration#migrating-from-slate)

While both Slate and Lexical save the editor state in JSON, the structure of the JSON is different. Payload provides a two-phase migration approach that allows you to safely migrate from Slate to Lexical:

  1. **Preview Phase** : Test the migration with an `afterRead` hook that converts data on-the-fly
  2. **Migration Phase** : Run a script to permanently migrate all data in the database

### [Phase 1: Preview & Test](/docs/rich-text/migration#phase-1-preview-and-test)

First, add the `SlateToLexicalFeature` to every richText field you want to migrate. By default, this feature converts your data from Slate to Lexical format on-the-fly through an `afterRead` hook. If the data is already in Lexical format, it passes through unchanged.

This allows you to test the migration without modifying your database. The on-the-fly conversion happens server-side through the `afterRead` hook, which means:

  * **In the Admin Panel** : Preview how your content will look in the Lexical editor
  * **In your API** : All read operations (REST, GraphQL, Local API) return converted Lexical data instead of Slate data
  * **In your application** : Your frontend receives Lexical data, allowing you to test if your app correctly handles the new format



You can verify that:

  * All content converts correctly
  * Custom nodes are handled properly
  * Formatting is preserved
  * Your application displays the Lexical data as expected
  * Any custom converters work as expected



**Example:**
```
import type { CollectionConfig } from 'payload'
    
    
    import { SlateToLexicalFeature } from '@payloadcms/richtext-lexical/migrate'
    import { lexicalEditor } from '@payloadcms/richtext-lexical'
    
    
    const Pages: CollectionConfig = {
      slug: 'pages',
      fields: [
        {
          name: 'content',
          type: 'richText',
          editor: lexicalEditor({
            features: ({ defaultFeatures }) => [
              ...defaultFeatures,
              SlateToLexicalFeature({}),
            ],
          }),
        },
      ],
    }
```

**Important** : In preview mode, if you save a document in the Admin Panel, it will overwrite the Slate data with the converted Lexical data in the database. Only save if you've verified the conversion is correct.

Each richText field has its own `SlateToLexicalFeature` instance because each field may require different converters. For example, one field might contain custom Slate nodes that need custom converters.

### [Phase 2: Running the Migration Script](/docs/rich-text/migration#phase-2-running-the-migration-script)

Once you've tested the migration in preview mode and verified the results, you can permanently migrate all data in your database.

#### [Why Run the Migration Script?](/docs/rich-text/migration#why-run-the-migration-script)

While the `SlateToLexicalFeature` works well for testing, running the migration script has important benefits:

  * **Performance** : The `afterRead` hook converts data on-the-fly, adding overhead to every read operation
  * **Database Consistency** : Direct database operations (e.g., `payload.db.find` instead of `payload.find`) bypass hooks and return unconverted Slate data
  * **Production Ready** : After migration, your data is fully converted and you can remove the migration feature

#### [Migration Prerequisites](/docs/rich-text/migration#migration-prerequisites)

**CRITICAL: This will permanently overwrite all Slate data. Follow these steps carefully:**

  1. **Backup Your Database** : Create a complete backup of your database before proceeding. If anything goes wrong without a backup, data recovery may not be possible.
  2. **Convert All richText Fields** : Update your config to use `lexicalEditor()` for all richText fields. The script only converts fields that:


  * Use the Lexical editor
  * Have `SlateToLexicalFeature` added
  * Contain Slate data in the database


  1. **Test the Preview** : Add `SlateToLexicalFeature` to every richText field (as shown in Phase 1) and thoroughly test in the Admin Panel. Build custom converters for any custom Slate nodes before proceeding.
  2. **Disable Hooks** : Once testing is complete, add `disableHooks: true` to all `SlateToLexicalFeature` instances:


```
SlateToLexicalFeature({ disableHooks: true })
```

This prevents the `afterRead` hook from running during migration, improving performance and ensuring clean data writes.

#### [Running the Migration](/docs/rich-text/migration#running-the-migration)

Create a migration script and run it:
```
import { getPayload } from 'payload'
    import config from '@payload-config'
    import { migrateSlateToLexical } from '@payloadcms/richtext-lexical/migrate'
    
    
    const payload = await getPayload({ config })
    
    
    await migrateSlateToLexical({ payload })
```

The migration will:

  * Process all collections and globals
  * Handle all locales (if localization is enabled)
  * Migrate both published and draft documents
  * Recursively process nested fields (arrays, blocks, tabs, groups)
  * Log progress for each collection and document
  * Collect and report any errors at the end



Depending on your database size, this may take considerable time. The script provides detailed progress updates as it runs.

### [Converting Custom Slate Nodes](/docs/rich-text/migration#converting-custom-slate-nodes)

If your Slate editor includes custom nodes, you'll need to create custom converters for them. A converter transforms a Slate node structure into its Lexical equivalent.

#### [How Converters Work](/docs/rich-text/migration#how-converters-work)

Each converter receives the Slate node and returns the corresponding Lexical node. The converter also specifies which Slate node types it handles via the `nodeTypes` array.

#### [Example: Simple Node Converter](/docs/rich-text/migration#example-simple-node-converter)

Here's the built-in Upload converter as an example:
```
import type { SerializedUploadNode } from '@payloadcms/richtext-lexical'
    import type { SlateNodeConverter } from '@payloadcms/richtext-lexical'
    
    
    export const SlateUploadConverter: SlateNodeConverter = {
      converter({ slateNode }) {
        return {
          type: 'upload',
          fields: {
            ...slateNode.fields,
          },
          format: '',
          relationTo: slateNode.relationTo,
          type: 'upload',
          value: {
            id: slateNode.value?.id || '',
          },
          version: 1,
        } as const as SerializedUploadNode
      },
      nodeTypes: ['upload'],
    }
```

#### [Example: Node with Children](/docs/rich-text/migration#example-node-with-children)

For nodes that contain child nodes (like links), recursively convert the children:
```
import type { SerializedLinkNode } from '@payloadcms/richtext-lexical'
    import type { SlateNodeConverter } from '@payloadcms/richtext-lexical'
    import { convertSlateNodesToLexical } from '@payloadcms/richtext-lexical/migrate'
    
    
    export const SlateLinkConverter: SlateNodeConverter = {
      converter({ converters, slateNode }) {
        return {
          type: 'link',
          children: convertSlateNodesToLexical({
            canContainParagraphs: false,
            converters,
            parentNodeType: 'link',
            slateNodes: slateNode.children || [],
          }),
          direction: 'ltr',
          fields: {
            doc: slateNode.doc || null,
            linkType: slateNode.linkType || 'custom',
            newTab: slateNode.newTab || false,
            url: slateNode.url || '',
          },
          format: '',
          indent: 0,
          version: 2,
        } as const as SerializedLinkNode
      },
      nodeTypes: ['link'],
    }
```

#### [Converter API](/docs/rich-text/migration#converter-api)

Your converter function receives these parameters:
```
{
      slateNode: SlateNode,         // The Slate node to convert
      converters: SlateNodeConverter[], // All available converters (for recursive conversion)
      parentNodeType: string,        // The Lexical node type of the parent
      childIndex: number,            // Index of this node in parent's children array
    }
```

#### [Adding Custom Converters](/docs/rich-text/migration#adding-custom-converters)

You can add custom converters by passing an array of converters to the `converters` property of the `SlateToLexicalFeature` props:
```
import type { CollectionConfig } from 'payload'
    import { lexicalEditor } from '@payloadcms/richtext-lexical'
    import {
      SlateToLexicalFeature,
      defaultSlateConverters,
    } from '@payloadcms/richtext-lexical/migrate'
    import { MyCustomConverter } from './converters/MyCustomConverter'
    
    
    const Pages: CollectionConfig = {
      slug: 'pages',
      fields: [
        {
          name: 'content',
          type: 'richText',
          editor: lexicalEditor({
            features: ({ defaultFeatures }) => [
              ...defaultFeatures,
              SlateToLexicalFeature({
                converters: [...defaultSlateConverters, MyCustomConverter],
              }),
            ],
          }),
        },
      ],
    }
```

#### [Unknown Node Handling](/docs/rich-text/migration#unknown-node-handling)

If the migration encounters a Slate node without a converter, it:

  1. Logs a warning to the console
  2. Wraps it in an `unknownConverted` node that preserves the original data
  3. Continues migration without failing



This ensures your migration completes even if some converters are missing, allowing you to handle edge cases later.

The migration script automatically traverses all collections and fields, retrieves converters from the `SlateToLexicalFeature` on each field, and converts the data using those converters.

If you're manually calling `convertSlateToLexical`, you can pass converters directly:
```
import { convertSlateToLexical } from '@payloadcms/richtext-lexical/migrate'
    
    
    const lexicalData = convertSlateToLexical({
      slateData: mySlateData,
      converters: [...defaultSlateConverters, MyCustomConverter],
    })
```

## [Migrating lexical data from old version to new version](/docs/rich-text/migration#migrating-lexical-data-from-old-version-to-new-version)

Each lexical node has a `version` property which is saved in the database. Every time we make a breaking change to the node's data, we increment the version. This way, we can detect an old version and automatically convert old data to the new format once you open up the editor.

The problem is, this migration only happens when you open the editor, modify the richText field (so that the field's `setValue` function is called) and save the document. Until you do that for all documents, some documents will still have the old data.

To solve this, we export an `upgradeLexicalData` function which goes through every single document in your Payload app and re-saves it, if it has a lexical editor. This way, the data is automatically converted to the new format, and that automatic conversion gets applied to every single document in your app.

IMPORTANT: Take a backup of your entire database. If anything goes wrong and you do not have a backup, you are on your own and will not receive any support.
```
import { upgradeLexicalData } from '@payloadcms/richtext-lexical'
    
    
    await upgradeLexicalData({ payload })
```

## [Migrating from payload-plugin-lexical](/docs/rich-text/migration#migrating-from-payload-plugin-lexical)

Migrating from [payload-plugin-lexical](https://github.com/AlessioGr/payload-plugin-lexical) works similar to migrating from Slate.

Instead of a `SlateToLexicalFeature` there is a `LexicalPluginToLexicalFeature` you can use. And instead of `convertSlateToLexical` you can use `convertLexicalPluginToLexical`.

[Next Slate Editor](/docs/rich-text/slate)
