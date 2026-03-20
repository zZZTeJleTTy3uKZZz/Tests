<a id="page-92"></a>
---
url: https://payloadcms.com/docs/rich-text/official-features
---

# Official Features

Below are all the Rich Text Features Payload offers. Everything is customizable; you can [create your own features](../rich-text/custom-features), modify ours and share them with the community.

## [Features Overview](/docs/rich-text/official-features#features-overview)

Feature Name |  Included by default |  Description   
---|---|---  
`**BoldFeature**` |  Yes |  Adds support for bold text formatting.   
`**ItalicFeature**` |  Yes |  Adds support for italic text formatting.   
`**UnderlineFeature**` |  Yes |  Adds support for underlined text formatting.   
`**StrikethroughFeature**` |  Yes |  Adds support for strikethrough text formatting.   
`**SubscriptFeature**` |  Yes |  Adds support for subscript text formatting.   
`**SuperscriptFeature**` |  Yes |  Adds support for superscript text formatting.   
`**InlineCodeFeature**` |  Yes |  Adds support for inline code formatting.   
`**ParagraphFeature**` |  Yes |  Provides entries in both the slash menu and toolbar dropdown for explicit paragraph creation or conversion.   
`**HeadingFeature**` |  Yes |  Adds Heading Nodes (by default, H1 - H6, but that can be customized)   
`**AlignFeature**` |  Yes |  Adds support for text alignment (left, center, right, justify)   
`**IndentFeature**` |  Yes |  Adds support for text indentation with toolbar buttons   
`**UnorderedListFeature**` |  Yes |  Adds support for unordered lists (ul)   
`**OrderedListFeature**` |  Yes |  Adds support for ordered lists (ol)   
`**ChecklistFeature**` |  Yes |  Adds support for interactive checklists   
`**LinkFeature**` |  Yes |  Allows you to create internal and external links   
`**RelationshipFeature**` |  Yes |  Allows you to create block-level (not inline) relationships to other documents   
`**BlockquoteFeature**` |  Yes |  Allows you to create block-level quotes   
`**UploadFeature**` |  Yes |  Allows you to create block-level upload nodes - this supports all kinds of uploads, not just images   
`**HorizontalRuleFeature**` |  Yes |  Adds support for horizontal rules / separators. Basically displays an `<hr>` element   
`**InlineToolbarFeature**` |  Yes |  Provides a floating toolbar which appears when you select text. This toolbar only contains actions relevant for selected text   
`**FixedToolbarFeature**` |  No |  Provides a persistent toolbar pinned to the top and always visible. Both inline and fixed toolbars can be enabled at the same time.   
`**BlocksFeature**` |  No |  Allows you to use Payload's [Blocks Field](../fields/blocks) directly inside your editor. In the feature props, you can specify the allowed blocks - just like in the Blocks field.   
`**TreeViewFeature**` |  No |  Provides a debug box under the editor, which allows you to see the current editor state live, the dom, as well as time travel. Very useful for debugging   
`**EXPERIMENTAL_TableFeature**` |  No |  Adds support for tables. This feature may be removed or receive breaking changes in the future - even within a stable lexical release, without needing a major release.   
`**TextStateFeature**` |  No |  Allows you to store key-value attributes within TextNodes and assign them inline styles.   
  
## [In depth](/docs/rich-text/official-features#in-depth)### [BoldFeature](/docs/rich-text/official-features#boldfeature)

  * Description: Adds support for bold text formatting, along with buttons to apply it in both fixed and inline toolbars.
  * Included by default: Yes
  * Markdown Support: `**bold**` or `__bold__`
  * Keyboard Shortcut: Ctrl/Cmd + B

### [ItalicFeature](/docs/rich-text/official-features#italicfeature)

  * Description: Adds support for italic text formatting, along with buttons to apply it in both fixed and inline toolbars.
  * Included by default: Yes
  * Markdown Support: `*italic*` or `_italic_`
  * Keyboard Shortcut: Ctrl/Cmd + I

### [UnderlineFeature](/docs/rich-text/official-features#underlinefeature)

  * Description: Adds support for underlined text formatting, along with buttons to apply it in both fixed and inline toolbars.
  * Included by default: Yes
  * Keyboard Shortcut: Ctrl/Cmd + U

### [StrikethroughFeature](/docs/rich-text/official-features#strikethroughfeature)

  * Description: Adds support for strikethrough text formatting, along with buttons to apply it in both fixed and inline toolbars.
  * Included by default: Yes
  * Markdown Support: `~~strikethrough~~`

### [SubscriptFeature](/docs/rich-text/official-features#subscriptfeature)

  * Description: Adds support for subscript text formatting, along with buttons to apply it in both fixed and inline toolbars.
  * Included by default: Yes

### [SuperscriptFeature](/docs/rich-text/official-features#superscriptfeature)

  * Description: Adds support for superscript text formatting, along with buttons to apply it in both fixed and inline toolbars.
  * Included by default: Yes

### [InlineCodeFeature](/docs/rich-text/official-features#inlinecodefeature)

  * Description: Adds support for inline code formatting with distinct styling, along with buttons to apply it in both fixed and inline toolbars.
  * Included by default: Yes
  * Markdown Support: `code`

### [ParagraphFeature](/docs/rich-text/official-features#paragraphfeature)

  * Description: Provides entries in both the slash menu and toolbar dropdown for explicit paragraph creation or conversion.
  * Included by default: Yes

### [HeadingFeature](/docs/rich-text/official-features#headingfeature)

  * Description: Adds support for heading nodes (H1-H6) with toolbar dropdown and slash menu entries for each enabled heading size.
  * Included by default: Yes
  * Markdown Support: `#`, `##`, `###`, ..., at start of line.
  * Types:


```
type HeadingFeatureProps = {
      enabledHeadingSizes?: HeadingTagType[] // ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    }
```

  * Usage example:


```
HeadingFeature({
      enabledHeadingSizes: ['h1', 'h2', 'h3'], // Default: ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    })
```

### [AlignFeature](/docs/rich-text/official-features#alignfeature)

  * Description: Allows text alignment (left, center, right, justify), along with buttons to apply it in both fixed and inline toolbars.
  * Included by default: Yes
  * Keyboard Shortcut: Ctrl/Cmd + Shift + L/E/R/J (left/center/right/justify)

### [IndentFeature](/docs/rich-text/official-features#indentfeature)

  * Description: Adds support for text indentation, along with buttons to apply it in both fixed and inline toolbars.
  * Included by default: Yes
  * Keyboard Shortcut: Tab (increase), Shift + Tab (decrease)
  * Types:


```
type IndentFeatureProps = {
      /**
       * The nodes that should not be indented. "type"
       * property of the nodes you don't want to be indented.
       * These can be: "paragraph", "heading", "listitem",
       * "quote" or other indentable nodes if they exist.
       */
      disabledNodes?: string[]
      /**
       * If true, pressing Tab in the middle of a block such
       * as a paragraph or heading will not insert a tabNode.
       * Instead, Tab will only be used for block-level indentation.
       * @default false
       */
      disableTabNode?: boolean
    }
```

  * Usage example:


```
// Allow block-level indentation only
    IndentFeature({
      disableTabNode: true,
    })
```

### [UnorderedListFeature](/docs/rich-text/official-features#unorderedlistfeature)

  * Description: Adds support for unordered lists (bullet points) with toolbar dropdown and slash menu entries.
  * Included by default: Yes
  * Markdown Support: `-`, `*`, or `+` at start of line

### [OrderedListFeature](/docs/rich-text/official-features#orderedlistfeature)

  * Description: Adds support for ordered lists (numbered lists) with toolbar dropdown and slash menu entries.
  * Included by default: Yes
  * Markdown Support: `1.` at start of line

### [ChecklistFeature](/docs/rich-text/official-features#checklistfeature)

  * Description: Adds support for interactive checklists with toolbar dropdown and slash menu entries.
  * Included by default: Yes
  * Markdown Support: `- [ ]` (unchecked) or `- [x]` (checked)

### [LinkFeature](/docs/rich-text/official-features#linkfeature)

  * Description: Allows creation of internal and external links with toolbar buttons and automatic URL conversion.
  * Included by default: Yes
  * Markdown Support: `[anchor](url)`
  * Types:


```
type LinkFeatureServerProps = {
      /**
       * Disables the automatic creation of links
       * from URLs typed or pasted into the editor,
       * @default false
       */
      disableAutoLinks?: 'creationOnly' | true
      /**
       * A function or array defining additional
       * fields for the link feature.
       * These will be displayed in the link editor drawer.
       */
      fields?:
        | ((args: {
            config: SanitizedConfig
            defaultFields: FieldAffectingData[]
          }) => (Field | FieldAffectingData)[])
        | Field[]
      /**
       * Sets a maximum population depth for the internal
       * doc default field of link, regardless of the
       * remaining depth when the field is reached.
       */
      maxDepth?: number
    } & ExclusiveLinkCollectionsProps
    
    
    type ExclusiveLinkCollectionsProps =
      | {
          disabledCollections?: CollectionSlug[]
          enabledCollections?: never
        }
      | {
          disabledCollections?: never
          enabledCollections?: CollectionSlug[]
        }
```

  * Usage example:


```
LinkFeature({
      fields: ({ defaultFields }) => [
        ...defaultFields,
        {
          name: 'rel',
          type: 'select',
          options: ['noopener', 'noreferrer', 'nofollow'],
        },
      ],
      enabledCollections: ['pages', 'posts'], // Collections for internal links
      maxDepth: 2, // Population depth for internal links
      disableAutoLinks: false, // Allow auto-conversion of URLs
    })
```

### [RelationshipFeature](/docs/rich-text/official-features#relationshipfeature)

  * Description: Allows creation of block-level relationships to other documents with toolbar button and slash menu entry.
  * Included by default: Yes
  * Types:


```
type RelationshipFeatureProps = {
      /**
       * Sets a maximum population depth for this relationship,
       * regardless of the remaining depth when the respective
       * field is reached.
       */
      maxDepth?: number
    } & ExclusiveRelationshipFeatureProps
    
    
    type ExclusiveRelationshipFeatureProps =
      | {
          disabledCollections?: CollectionSlug[]
          enabledCollections?: never
        }
      | {
          disabledCollections?: never
          enabledCollections?: CollectionSlug[]
        }
```

  * Usage example:


```
RelationshipFeature({
      disabledCollections: ['users'], // Collections to exclude
      maxDepth: 2, // Population depth for relationships
    })
```

### [UploadFeature](/docs/rich-text/official-features#uploadfeature)

  * Description: Allows creation of upload/media nodes with toolbar button and slash menu entry, supports all file types.
  * Included by default: Yes
  * Types:


```
type UploadFeatureProps = {
      collections?: {
        [collection: UploadCollectionSlug]: {
          fields: Field[]
        }
      }
      /**
       * Sets a maximum population depth for this upload (not the fields for this upload), regardless of the remaining depth when the respective field is reached.
       * This behaves exactly like the maxDepth properties of relationship and upload fields.
       *
       * {@link ../getting-started/concepts#field-level-max-depth}
       */
      maxDepth?: number
    } & ExclusiveUploadFeatureProps
    
    
    type ExclusiveUploadFeatureProps =
      | {
          /**
           * The collections that should be disabled. Overrides the `enableRichTextRelationship` property in the collection config.
           * When this property is set, `enabledCollections` will not be available.
           **/
          disabledCollections?: UploadCollectionSlug[]
    
    
          // Ensures that enabledCollections is not available when disabledCollections is set
          enabledCollections?: never
        }
      | {
          // Ensures that disabledCollections is not available when enabledCollections is set
          disabledCollections?: never
    
    
          /**
           * The collections that should be enabled. Overrides the `enableRichTextRelationship` property in the collection config
           * When this property is set, `disabledCollections` will not be available.
           **/
          enabledCollections?: UploadCollectionSlug[]
        }
```

  * Usage example:


```
UploadFeature({
      collections: {
        uploads: {
          fields: [
            {
              name: 'caption',
              type: 'text',
              label: 'Caption',
            },
            {
              name: 'alt',
              type: 'text',
              label: 'Alt Text',
            },
          ],
        },
      },
      maxDepth: 1, // Population depth for uploads
      disabledCollections: ['specialUploads'], // Collections to exclude
    })
```

### [BlockquoteFeature](/docs/rich-text/official-features#blockquotefeature)

  * Description: Allows creation of blockquotes with toolbar button and slash menu entry.
  * Included by default: Yes
  * Markdown Support: `> quote text`

### [HorizontalRuleFeature](/docs/rich-text/official-features#horizontalrulefeature)

  * Description: Adds support for horizontal rules/separators with toolbar button and slash menu entry.
  * Included by default: Yes
  * Markdown Support: `---`

### [InlineToolbarFeature](/docs/rich-text/official-features#inlinetoolbarfeature)

  * Description: Provides a floating toolbar that appears when text is selected, containing formatting options relevant to selected text.
  * Included by default: Yes

### [FixedToolbarFeature](/docs/rich-text/official-features#fixedtoolbarfeature)

  * Description: Provides a persistent toolbar pinned to the top of the editor that's always visible.
  * Included by default: No
  * Types:


```
type FixedToolbarFeatureProps = {
      /**
       * @default false
       * If this is enabled, the toolbar will apply
       * to the focused editor, not the editor with
       * the FixedToolbarFeature.
       */
      applyToFocusedEditor?: boolean
      /**
       * Custom configurations for toolbar groups
       * Key is the group key (e.g. 'format', 'indent', 'align')
       * Value is a partial ToolbarGroup object that will
       * be merged with the default configuration
       */
      customGroups?: CustomGroups
      /**
       * @default false
       * If there is a parent editor with a fixed toolbar,
       * this will disable the toolbar for this editor.
       */
      disableIfParentHasFixedToolbar?: boolean
    }
```

  * Usage example:


```
FixedToolbarFeature({
      applyToFocusedEditor: false, // Apply to focused editor
      customGroups: {
        format: {
          // Custom configuration for format group
        },
      },
    })
```

### [BlocksFeature](/docs/rich-text/official-features#blocksfeature)

  * Description: Allows use of Payload's [Blocks Field](../fields/blocks) directly in the editor with toolbar buttons and slash menu entries for each block type. Supports both block-level and inline blocks.
  * Included by default: No



For complete documentation including custom block components, the pre-built CodeBlock, and rendering blocks on the frontend, see the dedicated [Blocks documentation](../rich-text/blocks).

### [TreeViewFeature](/docs/rich-text/official-features#treeviewfeature)

  * Description: Provides a debug panel below the editor showing the editor's internal state, DOM tree, and time travel debugging.
  * Included by default: No

### [EXPERIMENTAL_TableFeature](/docs/rich-text/official-features#experimental-tablefeature)

  * Description: Adds support for tables with toolbar button and slash menu entry for creation and editing.
  * Included by default: No

### [TextStateFeature](/docs/rich-text/official-features#textstatefeature)

  * Description: Allows storing key-value attributes in text nodes with inline styles and toolbar dropdown for style selection.
  * Included by default: No
  * Types:


```
type TextStateFeatureProps = {
      /**
       * The keys of the top-level object (stateKeys) represent the attributes that the textNode can have (e.g., color).
       * The values of the top-level object (stateValues) represent the values that the attribute can have (e.g., red, blue, etc.).
       * Within the stateValue, you can define inline styles and labels.
       */
      state: { [stateKey: string]: StateValues }
    }
    
    
    type StateValues = {
      [stateValue: string]: {
        css: StyleObject
        label: string
      }
    }
    
    
    type StyleObject = {
      [K in keyof PropertiesHyphenFallback]?:
        | Extract<PropertiesHyphenFallback[K], string>
        | undefined
    }
```

  * Usage example:


```
// We offer default colors that have good contrast and look good in dark and light mode.
    import { defaultColors, TextStateFeature } from '@payloadcms/richtext-lexical'
    
    
    TextStateFeature({
      // prettier-ignore
      state: {
        color: {
          ...defaultColors,
          // fancy gradients!
          galaxy: { label: 'Galaxy', css: { background: 'linear-gradient(to right, #0000ff, #ff0000)', color: 'white' } },
          sunset: { label: 'Sunset', css: { background: 'linear-gradient(to top, #ff5f6d, #6a3093)' } },
        },
        // You can have both colored and underlined text at the same time.
        // If you don't want that, you should group them within the same key.
        // (just like I did with defaultColors and my fancy gradients)
        underline: {
          'solid': { label: 'Solid', css: { 'text-decoration': 'underline', 'text-underline-offset': '4px' } },
           // You'll probably want to use the CSS light-dark() utility.
          'yellow-dashed': { label: 'Yellow Dashed', css: { 'text-decoration': 'underline dashed', 'text-decoration-color': 'light-dark(#EAB308,yellow)', 'text-underline-offset': '4px' } },
        },
      },
    }),
```

This is what the example above will look like:

![Example usage in light and dark mode for TextStateFeature with defaultColors and some custom styles](https://payloadcms.com/images/docs/text-state-feature.png)

[Next Blocks](/docs/rich-text/blocks)
