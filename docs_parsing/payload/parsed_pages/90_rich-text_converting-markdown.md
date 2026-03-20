<a id="page-90"></a>
---
url: https://payloadcms.com/docs/rich-text/converting-markdown
---

# Converting Markdown

## [Richtext to Markdown](/docs/rich-text/converting-markdown#richtext-to-markdown)

If you have access to the Payload Config and the [lexical editor config](../rich-text/converters#retrieving-the-editor-config), you can convert the lexical editor state to Markdown with the following:
```
import type { SerializedEditorState } from '@payloadcms/richtext-lexical/lexical'
    
    
    import {
      convertLexicalToMarkdown,
      editorConfigFactory,
    } from '@payloadcms/richtext-lexical'
    
    
    // Your richtext data here
    const data: SerializedEditorState = {}
    
    
    const markdown = convertLexicalToMarkdown({
      data,
      editorConfig: await editorConfigFactory.default({
        config, // <= make sure you have access to your Payload Config
      }),
    })
```

### [Example - outputting Markdown from the Collection](/docs/rich-text/converting-markdown#example-outputting-markdown-from-the-collection)
```
import type { SerializedEditorState } from '@payloadcms/richtext-lexical/lexical'
    import type { CollectionConfig, RichTextField } from 'payload'
    
    
    import {
      convertLexicalToMarkdown,
      editorConfigFactory,
      lexicalEditor,
    } from '@payloadcms/richtext-lexical'
    
    
    const Pages: CollectionConfig = {
      slug: 'pages',
      fields: [
        {
          name: 'nameOfYourRichTextField',
          type: 'richText',
          editor: lexicalEditor(),
        },
        {
          name: 'markdown',
          type: 'textarea',
          admin: {
            hidden: true,
          },
          hooks: {
            afterRead: [
              ({ siblingData, siblingFields }) => {
                const data: SerializedEditorState =
                  siblingData['nameOfYourRichTextField']
    
    
                if (!data) {
                  return ''
                }
    
    
                const markdown = convertLexicalToMarkdown({
                  data,
                  editorConfig: editorConfigFactory.fromField({
                    field: siblingFields.find(
                      (field) =>
                        'name' in field && field.name === 'nameOfYourRichTextField',
                    ) as RichTextField,
                  }),
                })
    
    
                return markdown
              },
            ],
            beforeChange: [
              ({ siblingData }) => {
                // Ensure that the markdown field is not saved in the database
                delete siblingData['markdown']
                return null
              },
            ],
          },
        },
      ],
    }
```

## [Markdown to Richtext](/docs/rich-text/converting-markdown#markdown-to-richtext)

If you have access to the Payload Config and the [lexical editor config](../rich-text/converters#retrieving-the-editor-config), you can convert Markdown to the lexical editor state with the following:
```
import {
      convertMarkdownToLexical,
      editorConfigFactory,
    } from '@payloadcms/richtext-lexical'
    
    
    const lexicalJSON = convertMarkdownToLexical({
      editorConfig: await editorConfigFactory.default({
        config, // <= make sure you have access to your Payload Config
      }),
      markdown: '# Hello world\n\nThis is a **test**.',
    })
```

## [Converting MDX](/docs/rich-text/converting-markdown#converting-mdx)

Payload supports serializing and deserializing MDX content. While Markdown converters are stored on the features, MDX converters are stored on the blocks that you pass to the `BlocksFeature`.

### [Defining a Custom Block](/docs/rich-text/converting-markdown#defining-a-custom-block)

Here is an example of a `Banner` block.

This block:

  * Renders in the admin UI as a normal Lexical block with specific fields (e.g. type, content).
  * Converts to an MDX `Banner` component.
  * Can parse that MDX `Banner` back into a Lexical state.



![Shows the Banner field in a lexical editor and the MDX output](https://payloadcms.com/images/docs/mdx-example-light.png)

Banner field in a lexical editor and the MDX output
```
import type { SerializedEditorState } from '@payloadcms/richtext-lexical/lexical'
    import type { Block, CollectionConfig, RichTextField } from 'payload'
    
    
    import {
      BlocksFeature,
      convertLexicalToMarkdown,
      editorConfigFactory,
      lexicalEditor,
    } from '@payloadcms/richtext-lexical'
    
    
    const BannerBlock: Block = {
      slug: 'Banner',
      fields: [
        {
          name: 'type',
          type: 'select',
          defaultValue: 'info',
          options: [
            { label: 'Info', value: 'info' },
            { label: 'Warning', value: 'warning' },
            { label: 'Error', value: 'error' },
          ],
        },
        {
          name: 'content',
          type: 'richText',
          editor: lexicalEditor(),
        },
      ],
      jsx: {
        /**
         * Convert from Lexical -> MDX:
         * <Banner type="..." >child content</Banner>
         */
        export: ({ fields, lexicalToMarkdown }) => {
          const props: any = {}
          if (fields.type) {
            props.type = fields.type
          }
    
    
          return {
            children: lexicalToMarkdown({ editorState: fields.content }),
            props,
          }
        },
        /**
         * Convert from MDX -> Lexical:
         */
        import: ({ children, markdownToLexical, props }) => {
          return {
            type: props?.type,
            content: markdownToLexical({ markdown: children }),
          }
        },
      },
    }
    
    
    const Pages: CollectionConfig = {
      slug: 'pages',
      fields: [
        {
          name: 'nameOfYourRichTextField',
          type: 'richText',
          editor: lexicalEditor({
            features: ({ defaultFeatures }) => [
              ...defaultFeatures,
              BlocksFeature({
                blocks: [BannerBlock],
              }),
            ],
          }),
        },
        {
          name: 'markdown',
          type: 'textarea',
          hooks: {
            afterRead: [
              ({ siblingData, siblingFields }) => {
                const data: SerializedEditorState =
                  siblingData['nameOfYourRichTextField']
    
    
                if (!data) {
                  return ''
                }
    
    
                const markdown = convertLexicalToMarkdown({
                  data,
                  editorConfig: editorConfigFactory.fromField({
                    field: siblingFields.find(
                      (field) =>
                        'name' in field && field.name === 'nameOfYourRichTextField',
                    ) as RichTextField,
                  }),
                })
    
    
                return markdown
              },
            ],
            beforeChange: [
              ({ siblingData }) => {
                // Ensure that the markdown field is not saved in the database
                delete siblingData['markdown']
                return null
              },
            ],
          },
        },
      ],
    }
```

The conversion is done using the `jsx` property of the block. The `export` function is called when converting from lexical to MDX, and the `import` function is called when converting from MDX to lexical.

### [Export](/docs/rich-text/converting-markdown#export)

The `export` function takes the block field data and the `lexicalToMarkdown` function as arguments. It returns the following object:

Property |  Type |  Description   
---|---|---  
`children` |  string |  This will be in between the opening and closing tags of the block.   
`props` |  object |  This will be in the opening tag of the block.   
  
### [Import](/docs/rich-text/converting-markdown#import)

The `import` function provides data extracted from the MDX. It takes the following arguments:

Argument |  Type |  Description   
---|---|---  
`children` |  string |  This will be the text between the opening and closing tags of the block.   
`props` |  object |  These are the props passed to the block, parsed from the opening tag into an object.   
  
The returning object is equal to the block field data.

[Next Converting Plaintext](/docs/rich-text/converting-plaintext)
