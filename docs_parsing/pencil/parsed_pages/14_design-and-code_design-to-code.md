<a id="page-14"></a>
---
url: https://docs.pencil.dev/design-and-code/design-to-code
---

# Design ↔ Code

One of Pencil’s most powerful features is seamless synchronization between your designs and codebase.

* * *

## Overview

Pencil enables a **two-way workflow** between design and code:

  * **Design → Code:** Generate components from Pencil designs
  * **Code → Design:** Import existing code into Pencil
  * **Sync:** Keep design and code in sync as both evolve

* * *

## Design → Code Workflow

### Basic Export to Code

  1. **Design in Pencil** \- Create your UI components, layouts, or screens
  2. **Save the`.pen` file** in your project workspace
  3. **Open AI prompt** \- Press `Cmd/Ctrl + K`
  4. **Ask for code generation:**
```
"Generate React code for this design"
         "Create a TypeScript component from this frame"
         "Export this as a Next.js page component"
```

### Example Prompts

**Component generation:**
```
Create a React component for this button
```
```
Generate TypeScript types for this form
```
```
Export this card as a reusable component
```

**Full pages:**
```
Generate a Next.js page from this design
```
```
Create a landing page component with Tailwind CSS
```
```
Export this dashboard as a React component
```

**With specific libraries:**
```
Generate code using Shadcn UI components
```
```
Create this form using React Hook Form
```
```
Export using Lucide icons instead of Material Icons
```

* * *

## Code → Design Workflow

### Importing Existing Code

If you have existing components in your codebase, Pencil can recreate them visually.

**Requirements:**

  * Keep the `.pen` file in the same workspace as your code
  * The AI agent can access both files

**Workflow:**

  1. **Open your`.pen` file**
  2. **Open AI prompt** \- Press `Cmd/Ctrl + K`
  3. **Ask to import code:**
```
Recreate the Button component from src/components/Button.tsx
```
```
Import the LoginForm from my codebase into this design
```
```
Add the Header component from src/layouts/Header.tsx
```

**What gets imported:**

  * Component structure and hierarchy
  * Layout and positioning
  * Styling (colors, typography, spacing)
  * Basic interactions

* * *

## Two-Way Sync

### Keeping Design and Code in Sync

The most powerful workflow combines both directions:

  1. **Start with code** \- Import existing components into Pencil
  2. **Design improvements** \- Make visual changes in Pencil
  3. **Update code** \- Ask AI to apply changes back to code
  4. **Iterate** \- Repeat as needed

* * *

## Variables & Design Tokens

### CSS Variables ↔ Pencil Variables

Create a synchronized design token system:

**Import CSS to Pencil:**

  1. Have a `globals.css` or similar file with CSS variables

  2. Ask the agent:
```
Create Pencil variables from my globals.css
```
```
Import design tokens from src/styles/tokens.css
```

**Export Pencil to CSS:**

  1. Define variables in Pencil

  2. Ask the agent:
```
Update globals.css with these Pencil variables
```
```
Sync these design tokens to my CSS
```

### Workflow Example
```
/* globals.css */
    :root {
      --color-primary: #3b82f6;
      --color-secondary: #64748b;
      --spacing-base: 1rem;
    }
```

**In Pencil:**

  1. “Create variables from globals.css”
  2. Update color-primary to #2563eb in Pencil
  3. “Sync variables back to globals.css”

**Result:**
```
/* globals.css - updated */
    :root {
      --color-primary: #2563eb;  /* Updated! */
      --color-secondary: #64748b;
      --spacing-base: 1rem;
    }
```

* * *

## Importing from Figma

You can bring design tokens from Figma into Pencil:

**Token Import:**

  1. Copy tokens from Figma

  2. Or take a screenshot of token tables

  3. Paste in Pencil or share with AI agent

  4. Ask:
```
Create Pencil variables from these Figma tokens
```

**Components:**

  * Copy elements from Figma
  * Paste into Pencil
  * **Note:** Images don’t copy - use SVG or re-import separately

* * *

## Best Practices

### File Organization

**Keep .pen files in your repo:**
```
my-project/
    ├── src/
    │   ├── components/
    │   └── styles/
    ├── design.pen           ← Design file
    └── package.json
```

**Benefits:**

  * AI agent can see both design and code
  * Version control tracks both together
  * Easy to keep in sync

### Workflow Recommendations

**Start new features:**

  1. Design in Pencil first
  2. Generate initial code
  3. Refine code implementation
  4. Update design if needed

**Update existing features:**

  1. Import component into Pencil
  2. Make design changes
  3. Sync changes back to code

**Design system maintenance:**

  1. Define variables in Pencil
  2. Sync to CSS
  3. Use variables in both design and code
  4. Update once, apply everywhere

* * *

## Code Generation Options

### Frameworks & Libraries

Pencil can generate code for:

  * **React** (JavaScript or TypeScript)
  * **Next.js**
  * **Vue**
  * **Svelte**
  * **Plain HTML/CSS**

**Styling:**

  * **Tailwind CSS** (recommended)
  * **CSS Modules**
  * **Styled Components**
  * **Plain CSS**

**Component Libraries:**

  * **Shadcn UI**
  * **Radix UI**
  * **Chakra UI**
  * **Material UI**
  * Custom components

### Specifying in Prompts

Be specific about your tech stack:
```
Generate Next.js 14 code with Tailwind CSS
```
```
Create a Vue component using TypeScript
```
```
Export as React with CSS Modules
```
```
Use Shadcn UI components for this layout
```

* * *

## Icon Libraries

### Built-in vs Code Libraries

**In Pencil:**

  * Built-in icons use Material Icons
  * Custom SVG paths supported

**For code generation:**

  * Specify your preferred library in prompts
  * Common options: Lucide, Heroicons, FontAwesome, React Icons

**Example:**
```
Generate this design using Lucide icons
```
```
Replace Material Icons with Heroicons in the code
```

* * *

## Limitations & Workarounds

### Current Limitations

**No auto-save:**

  * Save frequently with `Cmd/Ctrl + S`
  * Commit to Git often

**Export issues:**

  * If export fails with “process exited with code 1”, check Claude Code auth
  * Try running the export in a separate Claude Code session

**Canvas vs export mismatch:**

  * If exported code doesn’t match the canvas, report the issue
  * Try re-exporting or adjusting the design

### Workarounds

**Permissions:**

  * If Claude can’t access folders, update permissions
  * Accept permission prompts when they appear

**Complex components:**

  * Break down complex designs into smaller pieces
  * Export in stages
  * Combine in code

* * *

## Example Project Setup
```
# 1. Create project with design file
    mkdir my-app && cd my-app
    touch design.pen
    npm init -y
     
    # 2. Open in IDE
    code .
     
    # 3. Start Claude Code
    claude
     
    # 4. Open design.pen and start designing
    # 5. Use Cmd + K to generate code
```
