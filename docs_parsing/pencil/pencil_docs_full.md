# Полная документация Pencil

## Оглавление

- [Pencil Documentation](#page-1)
- **Getting Started**
  - [Installation](#page-2)
  - [Authentication](#page-3)
  - [AI Integration](#page-4)
- **Core Concepts**
  - [.pen Files](#page-5)
  - [Design as Code](#page-6)
  - [Pencil Interface](#page-7)
  - [Variables](#page-8)
  - [Components](#page-9)
  - [Slots](#page-10)
  - [Design Libraries](#page-11)
  - [Import and Export](#page-12)
  - [Keyboard Shortcuts](#page-13)
- **Design and Code**
  - [Design ↔ Code](#page-14)
  - [Styles and UI Kits](#page-15)
- [Troubleshooting](#page-16)
- **For Developers**
  - [The .pen Format](#page-17)
  - [Pencil CLI](#page-18)

---

<a id="page-1"></a>
---
url: https://docs.pencil.dev/
---

# Pencil Documentation

## Quick Links

  * [Getting Started](https://docs.pencil.dev/getting-started/installation) \- Your first steps with Pencil
  * [Core Concepts](https://docs.pencil.dev/core-concepts/pen-files) \- Understanding .pen files and components
  * [Design and Code](https://docs.pencil.dev/design-and-code/design-to-code) \- Syncing design with your codebase
  * [Troubleshooting](https://docs.pencil.dev/troubleshooting) \- Common issues and solutions
  * [For Developers](https://docs.pencil.dev/for-developers/the-pen-format) \- Technical information

## What is Pencil?

Pencil is a powerful vector design tool that integrates directly into your development environment. Unlike traditional design tools that run in separate applications or browser tabs, Pencil lives right inside your IDE alongside your code.

## Why Pencil?

Pencil bridges the gap between design and development by putting both in the same environment. Design components, sync them with your code, and let AI assistants help you maintain consistency between design and implementation.


---

<a id="page-2"></a>
---
url: https://docs.pencil.dev/getting-started/installation
---

# Installation

Pencil is available as an IDE extension and a standalone desktop application. Choose the option that best fits your workflow.

* * *

## VS Code Extension

### Installation

  1. Open VS Code
  2. Go to Extensions (Cmd/Ctrl + Shift + X)
  3. Search for “Pencil”
  4. Click **Install**

### Verification

  1. Create a new file with a `.pen` extension (e.g., `test.pen`)
  2. Open the file
  3. Look for the Pencil icon in the top-right corner of the editor

If you don’t see the icon:

  * Open Command Palette (Cmd/Ctrl + Shift + P)
  * Search for “Pencil” to see available commands
  * Check that the extension is enabled in your Extensions panel

* * *

## Cursor Extension

### Installation

  1. Open Cursor
  2. Go to Extensions
  3. Search for “Pencil”
  4. Click **Install**

### Verification

Same as VS Code - create a `.pen` file and verify the Pencil icon appears.

### Common Issues

**Extension doesn’t connect:**

  * Ensure Claude Code is logged in (`claude` CLI)
  * Complete the activation process
  * Check that Pencil MCP server is connected

**Don’t see the prompt editor/prompt box:**

  * Check activation/login status
  * Restart Cursor
  * Reinstall the extension if issues persist

**“You need Cursor Pro” message:**

  * This may occur depending on Cursor’s plan/tooling restrictions
  * Check your Cursor subscription status

* * *

## Desktop Application

### macOS

**Download:**

  * Get the latest `.dmg` from the Pencil website or releases page
  * Drag Pencil to your Applications folder
  * Launch Pencil

**First Launch:**

  * macOS may ask you to verify the app (right-click → Open if you see a security warning)
  * Complete the activation process
  * Login to Claude Code if you plan to use AI features

### Linux

**Supported:**

  * Pencil runs on Linux
  * Download the appropriate package for your distribution

**Known Issues:**

  * Some Wayland/Hyprland UI issues may occur
  * X11 environments are more stable

**Installation:**
```
# Example for .deb package
    sudo dpkg -i pencil-*.deb
     
    # Example for .AppImage
    chmod +x pencil-*.AppImage
    ./pencil-*.AppImage
```

### Windows

**Desktop App:**

  * Pencil runs on Windows
  * Windows users can also use the VS Code or Cursor extension

**Extension (Windows):**

  * Follow the VS Code or Cursor installation instructions above
  * Works the same as on macOS/Linux

* * *

## Claude Code CLI

Pencil’s AI features require Claude Code to be installed and authenticated.

### Installation
```
# Install Claude Code CLI
    npm install -g @anthropic-ai/claude-code-cli
     
    # Or using the official installer
    curl https://claude.ai/cli/install.sh | sh
```

### Authentication
```
# Login to Claude Code
    claude
     
    # Follow the browser authentication flow
```

### Verification
```
# Check that you're logged in
    claude --version
```

* * *

## MCP Server

The Pencil MCP (Model Context Protocol) server runs automatically when you use Pencil. It provides AI assistants with tools to read and manipulate `.pen` files.

### Automatic Setup

  * The MCP server starts when you open Pencil
  * It runs locally on your machine
  * No additional configuration needed for basic use

### Verification

**In Cursor:**

  * Open Settings → Tools & MCP
  * Verify Pencil appears in the MCP server list

**In Codex CLI:**

  1. Run Pencil first
  2. Open Codex
  3. Run `/mcp`
  4. Pencil should appear in the MCP list

* * *

## Post-Installation

After installing Pencil:

  1. **Complete activation** \- You’ll need to activate Pencil with your email
  2. **Login to Claude Code** \- Required for AI features
  3. **Open the welcome file** \- Right-click canvas → Open Welcome File
  4. **Create your first design** \- See how to [create a .pen file](https://docs.pencil.dev/core-concepts/pen-files)

* * *

## Updating Pencil

### VS Code/Cursor Extension

Extensions update automatically by default. To manually update:

  1. Go to Extensions
  2. Find Pencil
  3. Click **Update** if available

### Desktop App

  * The app will notify you when updates are available
  * Download and install the latest version from the website

* * *

## Troubleshooting Installation

**Extension installed but doesn’t connect:**

  * Verify Claude Code is logged in
  * Complete the activation process
  * Restart your IDE

**Activation email not received:**

  * Check spam/junk folder
  * Try a different email address
  * Reinstall the extension

**“Invalid API key” or “Please run /login”:**

  * Run `claude` CLI and complete authentication
  * Ensure no conflicting auth configurations (environment keys, custom providers)

See the full [Troubleshooting guide](https://docs.pencil.dev/troubleshooting) for more issues and solutions.


---

<a id="page-3"></a>
---
url: https://docs.pencil.dev/getting-started/authentication
---

# Authentication

Pencil requires both activation (to use Pencil itself) and Claude Code authentication (for AI features).

* * *

## Pencil Activation

### First-Time Activation

When you first launch Pencil or install the extension, you’ll be prompted to activate:

  1. **Enter your email** when prompted
  2. **Check your email** for the activation code
  3. **Enter the code** in Pencil to complete activation

### Activation Issues

**Activation email not received:**

  * Check your spam/junk folder
  * Try using a different email address
  * Wait a few minutes - emails may be delayed

**“Invite for your email address was not found. Please join the waitlist.”**

  * This can occur during activation
  * Try reinstalling the Cursor/VS Code extension
  * Contact support if the issue persists

**Repeatedly prompted for activation:**

  * This is a known issue in some versions
  * Try restarting your IDE
  * Reinstall the extension if it continues

**Activation stuck during migration:**

  * Reinstall the extension
  * Clear extension data and try again

* * *

## Claude Code Authentication

Pencil’s AI features require Claude Code to be installed and authenticated.

### Login via CLI

The recommended method is using the Claude Code CLI:
```
# Start Claude Code
    claude
     
    # Follow the browser authentication flow
```

This will:

  1. Open your browser
  2. Ask you to login with your Anthropic account
  3. Save your authentication credentials locally

### Verification

To verify you’re logged in:
```
# Check Claude Code status
    claude --version
```

Or start Pencil and look for:

  * No “Claude Code not connected” warnings
  * AI prompt panel works (Cmd/Ctrl + K)

* * *

## Common Authentication Issues

### ”Claude Code isn’t connected / not logged in”

**Solution:**

  1. Open a terminal in your project directory
  2. Run `claude` to authenticate
  3. Return to Pencil and try again

### ”Invalid API key” or “Please run /login”

**Causes:**

  * Claude Code authentication is incomplete
  * Multiple authentication methods conflict (console login + environment keys + custom provider config)
  * Credentials expired or invalid

**Solution:**

  1. Run `claude` CLI and complete authentication
  2. Check for conflicting auth configurations:
     * Remove `ANTHROPIC_API_KEY` environment variables if using CLI auth
     * Clear custom provider configs if not needed
  3. Try a clean Claude Code login session

### ”Claude CLI works, but Pencil still says I’m not logged in”

**Causes:**

  * Using third-party/custom providers with conflicting auth setup
  * Extension not recognizing CLI auth

**Solution:**

  * Ensure a clean Claude Code login session (no custom providers)
  * Restart your IDE after authenticating
  * Check that no conflicting environment variables are set

* * *

## Authentication Methods

### Recommended: Claude CLI

The simplest and most reliable method:

  * Run `claude` in your terminal
  * Login via browser
  * All Pencil features work automatically

### Alternative: API Keys

If you’re using custom authentication:

  * Set `ANTHROPIC_API_KEY` environment variable
  * Note: May conflict with CLI authentication
  * Not recommended for typical usage

* * *

## Working Flow for Authentication

A commonly successful workflow:

  1. **Install Pencil** (extension or desktop app)
  2. **Complete Pencil activation** (email code)
  3. **Install Claude Code CLI**
  4. **Authenticate Claude Code** (`claude` command)
  5. **Create a`.pen` file** in your project
  6. **Start working** \- both Pencil and AI features should work

* * *

## Permissions & Access

### Folder Access

**Issue:** “Pencil / Claude can’t access other folders”

**Cause:**

  * Folder permission restrictions
  * OS security settings

**Solution:**

  * Accept access prompts when they appear
  * Update folder permissions in system settings
  * Run your IDE/Pencil with appropriate permissions

### Missing Permission Prompts

**Issue:** “Claude requested permission to write somewhere, but I never saw a prompt”

**Workaround:**

  * Run the operation outside Pencil in a separate Claude Code session
  * Check system notification settings
  * Verify IDE permissions

* * *

## Security & Privacy

### MCP Server

  * The Pencil MCP server runs **locally** on your machine
  * No design data is sent to remote servers (except when using AI features, which send prompts to Claude)
  * The repository is currently private (no public documentation yet)

### Tool Definitions

You can inspect available MCP tools:

  * **In Cursor:** Settings → Tools & MCP
  * **In VS Code:** Check MCP configuration
  * Tool definitions show what the AI can do with your designs

* * *

## Still Having Issues?

If you’re still experiencing authentication problems:

  1. Check the [Troubleshooting guide](https://docs.pencil.dev/troubleshooting)
  2. Ensure you’re using the latest version of Pencil and Claude Code
  3. Try reinstalling both Pencil and Claude Code CLI


---

<a id="page-4"></a>
---
url: https://docs.pencil.dev/getting-started/ai-integration
---

# AI Integration

Pencil’s deep integration with AI assistants via the Model Context Protocol (MCP) enables powerful design automation and workflows.

* * *

## Supported AI Assistants

Pencil works with multiple AI tools through MCP:

  * **Claude Code** (CLI and IDE)
  * **Claude Desktop**
  * **Cursor** (AI-powered IDE)
  * **Windsurf IDE** (Codeium)
  * **Codex CLI** (OpenAI)
  * **Antigravity IDE**
  * **OpenCode CLI**

* * *

## MCP (Model Context Protocol)

### What is MCP?

MCP is a protocol that gives AI assistants tools to interact with your design files. Think of it as an API that lets AI read and modify `.pen` files programmatically.

### How It Works

  1. **Pencil MCP Server runs locally** \- No cloud dependency for design operations
  2. **AI assistants connect** via MCP when Pencil is running
  3. **AI can use tools** to read, modify, and generate designs
  4. **You stay in control** \- AI suggests, you approve

### Security & Privacy

  * **Local-only:** MCP server runs on your machine
  * **No remote access:** Design files stay local
  * **Repository is private:** Source code not yet public
  * **Tool inspection:** View available tools in IDE settings

* * *

## Using Claude Code

### Setup

**Prerequisites:**

  1. Install Claude Code CLI
  2. Authenticate: `claude`
  3. Have Pencil running
  4. Open a `.pen` file

### Pencil in Antigravity (or VSCode) with Claude Code panel

### Basic Workflow

  1. **Open AI prompt panel:** Press `Cmd/Ctrl + K`
  2. **Ask for design help:**
```
"Create a login form with email and password"
         "Add a navigation bar to this page"
         "Design a card component for my design system"
```

  3. **AI uses MCP tools** to modify your `.pen` file
  4. **See changes** reflected in the canvas immediately

### Example Prompts

**Creating designs:**

  * “Design a dashboard with sidebar and main content area”
  * “Create a pricing table with 3 tiers”
  * “Add a hero section with heading and CTA button”

**Modifying designs:**

  * “Change all primary buttons to blue”
  * “Make the sidebar narrower”
  * “Add spacing between these elements”

**Design systems:**

  * “Create a button component with variants”
  * “Generate a color palette based on #3b82f6”
  * “Build a typography scale”

**Code integration:**

  * “Generate React code for this component”
  * “Import the Header from my codebase”
  * “Create Tailwind config from these variables”

* * *

## Using Cursor

### Setup

  1. Install Pencil extension in Cursor
  2. Complete activation
  3. Authenticate Claude Code
  4. Verify MCP connection: Settings → Tools & MCP

### Using Pencil Extension in Cursor

### Cursor-Specific Features

**Inline editing:**

  * Select elements in Pencil
  * Use Cursor’s AI chat to modify
  * Changes apply to `.pen` file

**Codebase awareness:**

  * Cursor can see both your code and designs
  * Ask to sync components between them
  * Maintain consistency automatically

### Common Issues

**“Need Cursor Pro”:**

  * Some features may require Cursor Pro subscription
  * Check Cursor’s pricing for current limitations

**Prompt panel missing:**

  * Check activation/login status
  * Restart Cursor
  * Verify MCP connection in settings

* * *

## Using Codex CLI

### Setup

  1. **Run Pencil first** \- Start the desktop app or IDE extension
  2. **Open Codex** in your terminal
  3. **Verify MCP connection:**
```
/mcp
```

  4. **Pencil should appear** in the MCP server list

### Working with Codex

**Design prompts in terminal:**
```
# In Codex CLI
    > Create a button component in design.pen
    > Add a hero section to the landing page
    > Generate a color scheme based on blue
```

**Benefits:**

  * Command-line workflow
  * Scriptable design generation
  * Integrate with build tools

### Known Issues

**Codex config.toml modifications:**

  * Pencil may modify or duplicate the config
  * Issue is acknowledged and under investigation
  * Backup your config before first use

* * *

## MCP Tools Available

When AI assistants connect to Pencil via MCP, they get access to these tools:

### Design Tools

**batch_design:**

  * Create, modify, and manipulate design elements
  * Insert, copy, update, replace, move, delete operations
  * Generate and place images

**batch_get:**

  * Read design components and hierarchy
  * Search for elements by patterns
  * Inspect component structure

### Analysis Tools

**get_screenshot:**

  * Render design previews
  * Verify visual output
  * Compare before/after

**snapshot_layout:**

  * Analyze layout structure
  * Detect positioning issues
  * Find overlapping elements

**get_editor_state:**

  * Current editor context
  * Selection information
  * Active file details

### Variables & Theming

**get_variables / set_variables:**

  * Read design tokens
  * Update theme values
  * Sync with CSS

### And More

View all available tools:

  * **Cursor:** Settings → Tools & MCP
  * **VS Code:** Check MCP configuration
  * **Codex:** Run `/mcp` and inspect Pencil tools

* * *

## Advanced Workflows

### Automated Design Generation

**Style guides:** Ask AI to follow specific design systems:
```
"Create a dashboard using Material Design principles"
    "Design a landing page with modern, minimal aesthetics"
    "Build components following our design system in design-system.pen"
```

**Batch operations:**
```
"Create 5 variations of this button component"
    "Generate a complete form with all input types"
    "Design an entire landing page with hero, features, pricing, and footer"
```

### Design System Management

**Consistency enforcement:**
```
"Ensure all buttons use the primary color variable"
    "Update all headings to use the typography scale"
    "Apply 8px spacing grid to all elements"
```

**Component library:**
```
"Create a complete button component with all variants"
    "Generate form input components (text, select, checkbox, radio)"
    "Build a card component with image, title, description, and actions"
```

### Code-Design Workflows

**Import existing app:**
```
"Recreate all components from src/components in Pencil"
    "Import the design system from our Tailwind config"
    "Analyze the codebase and create matching designs"
```

**Sync changes:**
```
"Update all React components to match the Pencil designs"
    "Apply the new color scheme to both design and code"
    "Sync typography variables between CSS and Pencil"
```

* * *

## Best Practices

### Effective Prompting

**Be specific:**

  * ❌ “Make it better”
  * ✅ “Increase the button padding to 16px and change color to blue”

**Provide context:**

  * ❌ “Add a form”
  * ✅ “Add a login form with email, password, remember me checkbox, and submit button”

**Reference design systems:**

  * “Use our existing button component”
  * “Follow the spacing scale from our variables”
  * “Match the style of the header component”

### Iterative Design

  1. **Start broad:** “Create a dashboard layout”
  2. **Refine:** “Add a sidebar with navigation items”
  3. **Detail:** “Style the nav items with hover states”
  4. **Polish:** “Adjust spacing to match 8px grid”

### Verification

After AI makes changes:

  1. **Review visually** in the canvas
  2. **Check structure** in layers panel
  3. **Test interactions** if applicable
  4. **Ask for screenshots** to verify complex layouts

* * *

## Troubleshooting AI Integration

### Connection Issues

**“Claude Code not connected”:**

  1. Ensure Claude Code is logged in: `claude`
  2. Restart Pencil
  3. Open terminal in project directory and run `claude`

**MCP server not appearing:**

  1. Verify Pencil is running
  2. Check IDE MCP settings
  3. Restart both Pencil and the AI assistant

### Permission Issues

**“Can’t access folders”:**

  * Accept permission prompts
  * Check system folder permissions
  * Run IDE/Pencil with proper permissions

**“Permission prompt never appeared”:**

  * Try operation in separate Claude Code session
  * Check notification settings
  * Verify IDE permissions

### AI Output Issues

**“Invalid API key”:**

  * Re-authenticate Claude Code: `claude`
  * Check for conflicting auth configs
  * Clear environment variables

**AI makes unexpected changes:**

  * Be more specific in prompts
  * Ask AI to explain before applying
  * Use version control to revert if needed

* * *

## Example Session
```
# 1. Start Pencil and Claude Code
    claude
    
    # 2. Open design.pen in IDE
    
    # 3. Press Cmd + K and start designing
    User: "Create a modern landing page hero section"
    AI: [Creates hero with heading, subheading, CTA buttons]
    
    User: "Add a features section with 3 columns"
    AI: [Adds features section below hero]
    
    User: "Use our primary color variable for the CTA buttons"
    AI: [Updates buttons to use color variable]
    
    User: "Generate React code for this entire page"
    AI: [Exports to React component with Tailwind CSS]
    
    # 4. Review and refine
    # 5. Commit to Git
    git add design.pen src/pages/landing.tsx
    git commit -m "Add landing page design and implementation"
```


---

<a id="page-5"></a>
---
url: https://docs.pencil.dev/core-concepts/pen-files
---

# .pen Files

Looking to read or write .pen files programmatically? See the [developer documentation](https://docs.pencil.dev/for-developers/the-pen-format).

## What are .pen files?

`.pen` files are Pencil’s design file format:

  * **JSON-based** \- Structured, readable data format
  * **Version-control friendly** \- Works with Git like any code file
  * **Portable** \- Share files across teams and platforms

## Working with .pen files

**Creating:**

  * In IDE: Create a new file with `.pen` extension
  * In Desktop: File → New or Cmd/Ctrl + N

**Opening:**

  * Double-click `.pen` files
  * Open in IDE like any other file
  * Pencil activates automatically

**Saving:**

  * Cmd/Ctrl + S to save
  * **Note:** Auto-save is not yet available - save frequently!
  * Use Git commits for version history

**Best Practices:**

  * Save frequently (no auto-save yet)
  * Commit to Git regularly for version history
  * Keep `.pen` files in your project workspace alongside code
  * Use descriptive names: `dashboard.pen`, `components.pen`


---

<a id="page-6"></a>
---
url: https://docs.pencil.dev/core-concepts/design-as-code
---

# Design as Code

## Collaboration & Version Control

  * Commit `.pen` files like code files
  * View diffs in Git (text-based format)
  * Branch and merge designs with code

**Best Practices:**

  * Frequent commits
  * Descriptive commit messages


---

<a id="page-7"></a>
---
url: https://docs.pencil.dev/core-concepts/pencil-interface
---

# Pencil Interface

## Infinite Canvas

The canvas gives you an unlimited workspace to freely explore and develop your designs. It builds on principles you already know from professional design tools, so it should feel familiar right away.

**To move around, hold spacebar and drag**. To zoom in or out, use your trackpad or hold Cmd/Ctrl and scroll.

### Navigation Shortcuts

Mastering shortcuts helps you work and navigate the canvas faster.

  * **Spacebar + Drag** \- Pan canvas
  * **Shift + Scroll** \- Horizontal pan
  * **Cmd/Ctrl + 0** \- Zoom to fit
  * **Cmd/Ctrl + 1** \- Zoom to 100%

## Frames

Frames are containers for your designs.

  * Group related elements
  * Define screen boundaries
  * **Cmd/Ctrl + Option/Alt + G** \- Create frame from selection

### Selection & Highlighting

Click and drag to select elements on the canvas. Selected elements are highlighted with colored bounding boxes that indicate their type.

**Blue** bounding boxes appear around regular elements like frames, shapes, and text.

**Magenta and violet** bounding boxes appear around components — reusable elements.

  * Magenta marks the component origin, which serves as the source of truth. Any changes you make here are applied across all instances automatically.

  * Violet marks instances of components.

### Selection Shortcuts

  * **Click** \- Select element
  * **Cmd/Ctrl + Click** \- Direct select (deepest element)
  * **Shift + Click** \- Add to selection
  * **Cmd/Ctrl + A** \- Select all

## Layers Panel

The layers panel sits on the left side of the screen and lists every element on the canvas. It gives you a clear view of your design hierarchy, making it easy to browse, edit, and organize elements in complex nested structures.

  * Rename a layer by double-clicking it in the panel.
  * Click the “Layers” icon to toggle the panel.

## Properties Panel

The properties panel appears on the right side of the screen when you select one or more elements on the canvas. It lets you view and edit properties like alignment, layout, appearance, fill, stroke, effects, and more.

  * Export selections as PNG, JPEG, WEBP, and PDF.
  * Click the icon in the top right corner to minimize it.

## AI Chat

Pencil’s AI chat is the interface for vibe-designing. You can ask it to design something from scratch or edit existing designs on the canvas.

The chat panel is built into the desktop app. When using the Pencil extension in your IDE, use your IDE’s built-in chat to work with the AI agent instead.

  * Any selections you make on the canvas are automatically added to the context.
  * Click “New chat” to start fresh and clear the context window.

## Undo / Redo

  * Use Cmd + Z (Ctrl + Z) to undo changes
  * Use Cmd + Shift + Z (Ctrl + Shift + Z) to redo changes
  * Undo and Redo may be more limited than in standard design editors

**Best Practices:**

  * Save frequently and use Git commits before major changes
  * Save often (Cmd/Ctrl + S)
  * Use Git history to revert if needed


---

<a id="page-8"></a>
---
url: https://docs.pencil.dev/core-concepts/variables
---

# Variables

## What are Variables?

Variables in Pencil work similar to CSS custom properties or design tokens.

You define HEX codes for colors, numbers for spacing, border radii, and sizes, or strings for font names — once. Then you use them throughout your design.

When you change a variable in the variables panel, it updates everywhere it’s used.

## Creating Variables

**Manually** — Define variables directly in Pencil and set values for different themes. Click the variables icon in the toolbar to open the panel.

**From CSS** — Ask the AI agent to create variables from your `globals.css`. It automatically extracts colors, spacing, and fonts.

**From Figma** — Paste a screenshot of the variables table and ask the AI to set them up in Pencil. You can also simply copy and paste individual token values from Figma.

## Using Variables

**Apply to elements** — Instead of hardcoding values, reference variables. When a variable changes, every element using it updates automatically.

**Theming** — Add a new column in the variables panel to create themes like light and dark mode. Switch between themes in the properties panel to see how your designs adapt.

## Sync with Code

You can keep variables in sync between Pencil and your codebase. Ask the AI assistant to update CSS variables based on your Pencil file, or import CSS changes back into Pencil. This enables a two-way design-to-code workflow.


---

<a id="page-9"></a>
---
url: https://docs.pencil.dev/core-concepts/components
---

# Components

## Why Use Components

Components let you maintain consistency across your designs. Edit the main component once and every instance updates automatically.

Components serve as the foundation for building design systems.

## Creating Components

Any standard design element — a frame, shape, or text — can be converted into a reusable component.

  1. Select the element
  2. Press **Cmd/Ctrl + Option/Alt + K** or click the “Create component” button at the top of the properties panel
  3. The element is now your component origin, marked with a magenta bounding box when selected

For more complex structures, you can create nested components.

## Using Components

Simply copy the component origin on the canvas to create an instance.

A component instance is marked with a violet bounding box when selected.

Click the “Go to component” button in the properties panel to quickly navigate back to the origin.


---

<a id="page-10"></a>
---
url: https://docs.pencil.dev/core-concepts/slots
---

# Slots

Slots are designated areas within a component where elements can be dropped in. They let you define flexible, customizable regions in your components.

## Create a Slot

  1. Create a frame and turn it into a component — press **Cmd/Ctrl + Option/Alt + K** or click the “Create component” button at the top of the properties panel
  2. Style it to your liking
  3. Click the “Make a slot” button at the top of the properties panel

  * Only empty frames in component origins can be turned into slots.
  * Slots are marked with diagonal lines on the canvas, indicating the area where elements can be dropped.

### Suggested Slot Components

Other components in the same .pen file can be marked as “suggested slot components”.

For example, a `table` component’s slot can suggest `table-row` as the intended content. Suggested slot components give both human and AI designers guidance about what belongs in a given slot.

To mark a component as suggested:

  1. Select the layer with a slot in the component origin
  2. Click the `+` button on the “Slots” line at the top of the properties panel
  3. Select the components you’d like to define as suggested

## Drop Elements into Slots

Once you have a component with a slot, you can populate it with elements.

  1. Create a component instance
  2. Drag and drop or copy and paste an element into the slot


---

<a id="page-11"></a>
---
url: https://docs.pencil.dev/core-concepts/design-libraries
---

# Design Libraries

Design libraries are collections of reusable components that can be imported into other .pen files. When you make changes to a component in a library file, those changes are reflected everywhere the component is used.

## Create a Design Library

  1. Create a new .pen file
  2. Populate it with components
  3. In the layers panel on the left, click the “Libraries” icon, then click “Turn this file into a library” at the bottom

Design library files use the `.lib.pen` suffix.

Once a file is marked as a design library, it cannot be undone.

## Import a Library Into a File

  1. In the layers panel on the left, click the “Libraries” icon
  2. Select the library you want to import to this file — you can also choose from the default libraries

## Use Design Library Assets

  1. In the layers panel on the left, click the “Assets” icon
  2. Scroll through the grid to find your desired asset or search it by name
  3. Drag and drop or click it to place it onto the canvas


---

<a id="page-12"></a>
---
url: https://docs.pencil.dev/core-concepts/import-and-export
---

# Import & Export

## Importing

**Images:**

  * **Drag and drop** \- Works reliably on all platforms
  * **File menu** \- May have issues on macOS, use drag-drop instead
  * Supported file formats: PNG, JPEG, SVG

**From Figma:**

  * Copy Frames directly from Figma
  * Paste in Pencil
  * **Note:** Images don’t copy from Figma, use SVG or re-import

**Icons:**

  * Built-in: Material Icons library
  * Custom: SVG paths supported
  * For code generation: Specify icon library in prompts (Lucide, Heroicons)

## Exporting

**Design to Code:**

  * Use AI agent to export designs to React/code
  * Press Cmd/Ctrl + K and ask to generate code

**Images:**

  * Export frames as PNG/SVG
  * Right-click frame → Export


---

<a id="page-13"></a>
---
url: https://docs.pencil.dev/core-concepts/keyboard-shortcuts
---

# Keyboard Shortcuts

Master these shortcuts to speed up your Pencil workflow.

* * *

## AI & Prompts

Shortcut| Action  
---|---  
`Cmd/Ctrl + K`| Open prompt panel (AI assistant)  
  
* * *

## Selection

Shortcut| Action  
---|---  
Click| Select element  
`Cmd/Ctrl + Click`| Direct select (deepest element under cursor)  
`Shift + Click`| Add to selection  
`Cmd/Ctrl + A`| Select all  
`Shift + Enter`| Select parent of current element  
`Cmd/Ctrl + Enter`| Select parent (alternate shortcut)  
  
* * *

## Components

Shortcut| Action  
---|---  
`Cmd/Ctrl + Option/Alt + K`| Convert element to reusable component  
  
**Note:** After converting to a component, you may need to deselect and reselect to see the updated purple highlight.

* * *

## Object organization

Shortcut| Action  
---|---  
`Cmd/Ctrl + G`| Group selected elements  
`Cmd/Ctrl + Option/Alt + G`| Create frame from selection  
  
* * *

## Editing

Shortcut| Action  
---|---  
`Cmd/Ctrl + D`| Duplicate selected element(s)  
`Cmd/Ctrl + C`| Copy  
`Cmd/Ctrl + V`| Paste  
`Cmd/Ctrl + X`| Cut  
`Delete/Backspace`| Delete selected element(s)  
  
* * *

## Canvas Navigation

Shortcut| Action  
---|---  
`Spacebar + Drag`| Pan canvas  
`Shift + Scroll`| Horizontal pan  
`Cmd/Ctrl + Scroll`| Zoom in/out  
`Cmd/Ctrl + 0`| Zoom to fit all  
`Cmd/Ctrl + 1`| Zoom to 100%  
`Cmd/Ctrl + 2`| Zoom to 200%  
  
* * *

## File Operations

Shortcut| Action  
---|---  
`Cmd/Ctrl + S`| Save file  
`Cmd/Ctrl + N`| New file  
`Cmd/Ctrl + O`| Open file  
  
* * *

## IDE Integration

Shortcut| Action  
---|---  
`Cmd/Ctrl + Shift + P`| Command Palette (access Pencil commands)  
  
* * *

## Tips for Efficiency

### Navigation Without Layers Panel

Combine shortcuts to quickly navigate complex designs:

  1. **Find nested element:**

     * `Cmd/Ctrl + Click` on the element you want
  2. **Move up the hierarchy:**

     * `Shift + Enter` to select parent
     * Repeat to keep moving up
  3. **Back to specific element:**

     * `Cmd/Ctrl + Click` again

### Component Workflow

  1. **Create design element** (shapes, text, etc.)
  2. **Group if needed:** `Cmd/Ctrl + G`
  3. **Convert to component:** `Cmd/Ctrl + Option/Alt + K`
  4. **Deselect and reselect** to verify purple highlight
  5. **Duplicate instances:** `Cmd/Ctrl + D`

### Quick Design Iteration

  1. **Open AI prompt:** `Cmd/Ctrl + K`
  2. **Ask for changes** to your design
  3. **Save frequently:** `Cmd/Ctrl + S` (no auto-save yet!)

* * *

## Context Menus

Right-click on the canvas or elements for context-specific options:

**Canvas right-click:**

  * Open Welcome File
  * Create new frame
  * Paste

**Element right-click:**

  * Copy / Paste
  * Delete
  * Group / Frame
  * Convert to component
  * Export

* * *

## Customization

Currently, keyboard shortcuts are not customizable. The default shortcuts are designed to match common design tool conventions (Figma, Sketch) and IDE standards.


---

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


---

<a id="page-15"></a>
---
url: https://docs.pencil.dev/design-and-code/styles-and-ui-kits
---

# Styles and UI Kits

## UI kits

Pencil includes pre-built design kits:

  * **Shadcn UI** \- Popular React component library
  * **Halo** \- Modern design system
  * **Lunaris** \- Design system
  * **Nitro** \- Design system

These provide ready-to-use components for common UI patterns.

## Variables and Design Kits Tutorial


---

<a id="page-16"></a>
---
url: https://docs.pencil.dev/troubleshooting
---

# Troubleshooting

* * *

## Installation & Setup

### Extension installed but doesn’t connect

**Symptoms:**

  * Pencil extension is installed but not functioning
  * No Pencil icon in the editor
  * Can’t open `.pen` files

**Solutions:**

  1. Verify Claude Code is logged in: `claude`
  2. Complete the activation process (check email for code)
  3. Check that Pencil MCP server is connected (Settings → MCP)
  4. Create a `.pen` file and try opening it
  5. Restart your IDE
  6. Reinstall the extension if issues persist

### Don’t see the Pencil icon

**Try this:**

  1. Create a `.pen` file (e.g., `test.pen`)
  2. Open the file
  3. Check extension version in Extensions panel
  4. Open Command Palette (`Cmd/Ctrl + Shift + P`) and search for “Pencil”
  5. Verify the extension is enabled

* * *

## Authentication & Activation

### Not receiving activation email

**Solutions:**

  1. Check spam/junk folder
  2. Wait a few minutes (emails may be delayed)
  3. Try a different email address
  4. Reinstall the extension if activation gets stuck

### ”Invite for your email address was not found”

**This can happen during activation:**

  1. Reinstall the Cursor/VS Code extension
  2. Try activation again
  3. Contact support if it continues

### Repeatedly prompted for activation

**Known issue in some versions:**

  * Restart your IDE
  * Complete activation once more
  * Reinstall extension if it continues

### Claude Code connection issues

**“Claude Code isn’t connected / not logged in”:**

**Working flow:**

  1. Open terminal in your project directory
  2. Run `claude` and complete authentication
  3. Return to Pencil
  4. Try opening/editing a `.pen` file

**“Invalid API key” or “Please run /login”:**

**Causes:**

  * Incomplete authentication
  * Conflicting auth methods (CLI + env variables + custom providers)
  * Expired credentials

**Solutions:**

  1. Run `claude` CLI and authenticate
  2. Check for conflicts:
     * Remove `ANTHROPIC_API_KEY` env variables if using CLI
     * Clear custom provider configs
  3. Try a clean login session
  4. Restart IDE after authenticating

**Claude CLI works but Pencil says not logged in:**

  * Ensure no third-party/custom providers conflict
  * Try a clean Claude Code session
  * Restart your IDE
  * Check for environment variable conflicts

* * *

## IDE-Specific Issues

### Cursor

**Don’t see prompt editor/prompt box:**

  * Check activation/login status
  * Restart Cursor
  * Verify MCP connection in settings
  * Reinstall extension if needed

**“You need Cursor Pro”:**

  * Some features may require Cursor Pro subscription
  * Check Cursor’s current plan restrictions
  * Try basic features without Pro

### VS Code

**Extension not activating:**

  * Ensure you have a `.pen` file open
  * Check that extension is enabled
  * Look for errors in Developer Tools Console
  * Try reinstalling

* * *

## Welcome File & Onboarding

### Didn’t get the welcome file

**Solution:**

  1. Right-click anywhere on the canvas
  2. Choose **Open Welcome File**
  3. It may open in a separate window

### Best way to add Pencil to a new project

**Recommended flow:**

  1. Create a file like `design.pen` in your workspace
  2. Open it in your IDE (Cursor/VS Code)
  3. Activate Pencil
  4. Keep the `.pen` file with your code so AI can see both

* * *

## Canvas & Interface

### Can’t navigate nested elements

**Use keyboard shortcuts:**

  * `Cmd/Ctrl + Click` \- Direct select (deepest element)
  * `Shift + Enter` \- Select parent
  * `Cmd/Ctrl + Enter` \- Select parent (alternate)

**Or use layers panel:**

  * Available in the interface
  * Shows full hierarchy
  * Click to select elements

### Selection boxes confusing

**Color meanings:**

  * **Blue** \- Regular element
  * **Purple/magenta** \- Reusable component/symbol

### Converting to component doesn’t show purple box

**After converting with`Cmd/Ctrl + Option/Alt + K`:**

  1. Deselect the element
  2. Reselect it
  3. Purple highlight should now appear

* * *

## Importing & Exporting

### Image import fails on macOS

**Issue:**

  * Using File menu dropdown may fail

**Solution:**

  * Use drag-and-drop instead
  * Works reliably on all platforms

### Images don’t paste from Figma

**Known limitation:**

  * Images are not supported when copy-pasting from Figma
  * Use SVG or re-import images separately

### Export to Claude Code fails

**“Process exited with code 1”:**

**Causes:**

  * Claude Code configuration issue
  * Authentication problem
  * Permission issue

**Solutions:**

  1. Check Claude Code authentication: `claude`
  2. Verify permissions
  3. Try exporting in a separate Claude Code session
  4. Check environment variables

### Exported output doesn’t match canvas

**Known issue:**

  * Visual mismatch between canvas and export
  * May indicate a bug

**Workarounds:**

  1. Take a screenshot of the canvas for reference
  2. Try re-exporting
  3. Adjust the design and export again
  4. Report the specific case for investigation

* * *

## MCP & AI Integration

### MCP server issues

**Is the MCP server local or remote?**

  * The MCP server runs **locally**
  * No cloud dependency for design operations

**Verify MCP connection:**

  * **Cursor:** Settings → Tools & MCP
  * **VS Code:** Check MCP configuration
  * **Codex:** Run `/mcp` \- Pencil should appear

### Codex config.toml modifications

**Issue:**

  * Pencil may modify or duplicate Codex config

**Workaround:**

  * Backup your `config.toml` before first use
  * Issue is acknowledged and under investigation

### AI can’t access folders

**“Pencil / Claude can’t access other folders”:**

**Solutions:**

  * Check folder permission restrictions
  * Accept access prompts when they appear
  * Update permissions in system settings
  * Run IDE/Pencil with appropriate permissions

### Permission prompt never appeared

**Workaround:**

  * Run the operation outside Pencil in a separate session
  * Check system notification settings
  * Verify IDE has necessary permissions

* * *

## Saving & Version Control

### No auto-save

**Current status:**

  * Auto-save is not yet available
  * Planned for future release

**Workarounds:**

  * Save frequently with `Cmd/Ctrl + S`
  * Use Git commits for version history
  * Set a reminder to save regularly

### Limited undo/redo

**Current limitations:**

  * Undo/redo may be more limited than standard design editors

**Best practices:**

  * Save before major changes
  * Commit to Git frequently
  * Use Git history to revert if needed
  * Make incremental changes

### No real-time collaboration

**Current status:**

  * Real-time multiplayer not available
  * Collaboration via Git only

**Workflow:**

  * Use Git branches for parallel work
  * Pull, edit, commit, push, create PR
  * Review designs in pull requests

* * *

## Performance & UI

### Wayland/Hyprland UI issues (Linux)

**Known issue:**

  * Some UI issues on Wayland/Hyprland

**Workarounds:**

  * Use X11 environment if possible
  * Report specific issues for investigation
  * Desktop app may have better compatibility

* * *

## Platform-Specific

### Windows desktop app

**Status:**

  * Not currently available
  * Windows users should use VS Code or Cursor extension

**Alternatives:**

  * Install VS Code extension
  * Install Cursor extension
  * Both work the same as on macOS/Linux

### Linux desktop app

**Status:**

  * Available for Linux
  * Some Wayland/Hyprland issues may occur

**Recommendations:**

  * X11 environments more stable
  * Try desktop app first
  * Fall back to IDE extension if needed

* * *

## Getting More Help

### Still having issues?

  1. **Review relevant docs:**
     * [Installation](https://docs.pencil.dev/getting-started/installation)
     * [Authentication](https://docs.pencil.dev/getting-started/authentication)
     * [AI Integration](https://docs.pencil.dev/getting-started/ai-integration)
  2. **Update everything:**
     * Latest Pencil version
     * Latest Claude Code CLI
     * Latest IDE version
  3. **Try reinstalling:**
     * Uninstall extension
     * Clear extension data
     * Reinstall fresh
  4. **Contact support** with:
     * Your platform (macOS/Windows/Linux)
     * Pencil version
     * IDE and version
     * Exact error message
     * Steps to reproduce

* * *

## Reporting Bugs

When reporting issues, include:

**Environment:**

  * OS and version
  * IDE (VS Code/Cursor/Desktop) and version
  * Pencil version
  * Claude Code CLI version

**Issue details:**

  * What you were trying to do
  * What happened instead
  * Exact error messages
  * Steps to reproduce

**Helpful extras:**

  * Screenshots
  * Console logs (if applicable)
  * Minimal `.pen` file that reproduces the issue

* * *

## Common Error Messages

Error| Likely Cause| Solution  
---|---|---  
”Claude Code not connected”| Not logged in| Run `claude` CLI  
”Invalid API key”| Auth conflict| Clear env vars, re-auth  
”Process exited with code 1”| Export/auth issue| Check Claude Code config  
”Need Cursor Pro”| Plan restriction| Check Cursor subscription  
”Invite not found”| Activation issue| Reinstall extension  
”Can’t access folder”| Permissions| Update folder permissions  
  
* * *

## Prevention Tips

**Avoid common issues:**

  1. Save frequently (no auto-save yet)
  2. Keep Claude Code authenticated
  3. Keep `.pen` files in project workspace
  4. Commit to Git regularly
  5. Update Pencil and Claude Code regularly
  6. Accept permission prompts
  7. Use supported workflows (don’t try to manually edit `.pen` files)

* * *

Most issues can be resolved by ensuring Claude Code is properly authenticated and Pencil is up to date. When in doubt, try restarting your IDE and re-authenticating Claude Code.


---

<a id="page-17"></a>
---
url: https://docs.pencil.dev/for-developers/the-pen-format
---

# The .pen Format

Pencil documents are stored in .pen files. This documentation is for developers who would like to read or write .pen files.

**The following sections provide a birds-eye view of the .pen format. For the authoritative, exhaustive reference of all the supported features, please consult theTypeScript schema at the end of this page.**

This is a live documentation, and we reserve the right to introduce breaking changes in the .pen format.

## Overview

  * .pen files contain a JSON structure, that describes an _object tree_ , not unlike HTML or SVG.
  * Each object in the document is a graphical entity on Pencil’s infinite two-dimensional canvas.
  * The objects must have an `id` property that uniquely identifies them within the document, and a `type` field from one of the possible object types (like `rectangle`, `frame`, `text`, etc. – consult the TypeScript schema for the exhaustive list of supported types).

## Layout

  * The top-level objects in a document are placed on an infinite two-dimensional canvas. They must have `x` and `y` properties that describe the location of their top-left corner.
  * Objects nested under other objects are positioned relative to their parents’ top-left corner.
  * A parent object can take over the sizing and positioning of its children using a flexbox-style layout system via properties like `layout`, `justifyContent` and `alignItems`.
  * Child objects can choose to fill their parent, or use a fixed `width` and/or `height`.
  * Parent objects can choose to fit the size of their children, or use a fixed `width` and/or `height`.

## Graphics

  * The graphical appearance of objects is controlled by the `fill`, `stroke` and `effect` properties.
  * A fill can be a solid `color`, a `gradient` (linear, radial or angular), an `image` or a `mesh_gradient`.
  * An object can have multiple fills, which are painted on top of each other the same order they appear in the document.
  * An object can have a single stroke, but the stroke can have multiple fills.
  * An object can have multiple effects, which are applied in the same order they appear in the document.

## Components and Instances

A key difference between Pencil documents and HTML or SVG is that Pencil documents allow reusing existing chunks of the object tree at different places. This enables the building of reusable components, that can be used as concise building blocks for more complicated structures.

### Components

When an object is marked with the property `reusable: true`, it becomes a _reusable component_ :
```
{
      "id": "foo",
      "type": "rectangle",
      "reusable": true, // <- this object is now a reusable component
      "x": 0, "y": 0, "width": 100, "height": 100,
      "fill": "#FF0000"
    }
```

### Instances

The object type `ref` is used to create an _instance_ of such components:
```
{
      "id": "bar",
      "type": "ref",
      "ref": "foo", // <- this object is an instance of the component "foo"
      "x": 120, "y": 0
    }
```

Here `foo` is a 100x100 red (`#FF0000`) square, and a reusable component. `bar` is an instance of `foo`, so it is also a 100x100 red square.

### Overrides

Instances can override properties from their component definition:
```
{
      "id": "baz",
      "type": "ref",
      "ref": "foo",
      "x": 240, "y": 0,
      "fill": "#0000FF"
    }
```

Even though `baz` is an instance of `foo`, it overrides the inherited `fill` property with a different one. So it’s going to be a 100x100 _blue_ (`#0000FF`) square!

### Nesting

An instance replicates everything under the component root:
```
{
      "id": "round-button",
      "type": "frame",
      "reusable": true,
      "cornerRadius": 9999,
      "children": [
        {
          "id": "label",
          "type": "text",
          "content": "Submit",
          "fill": "#000000"
          ...
        }
      ]
    }
     
    {
      "id": "red-round-button",
      "type": "ref",
      "ref": "round-button",
      "fill": "#FF0000"
    }
```

Here `red-round-button` will have an identical `"Submit"` label as `round-button`. But this label, too, can be customized using the `descendants` property:
```
{
      "id": "red-round-button",
      "type": "ref",
      "ref": "round-button",
      "fill": "#FF0000",
      "descendants": {
        "label": { // <- "label" is the `id` of the object under "red-round-button" that we want to customize
          "text": "Cancel",
          "fill": "#FFFFFF"
        }
      }
    }
```

Now the red button’s label will be white, and say `"Cancel"`.

Components can be built from instances of other components:
```
{
      "id": "alert",
      "type": "frame",
      "reusable": true,
      "children": [
        {
          "id": "message",
          "type": "text",
          "content": "This is an alert!",
          "fill": "#000000"
          ...
        },
        {
          "id": "ok-button",
          "type": "ref",
          "ref": "round-button",
          "descendants": {
            "label": {
              "text": "OK"
            }
          }
        },
        {
          "id": "cancel-button",
          "type": "ref",
          "ref": "round-button",
          "descendants": {
            "label": {
              "text": "Cancel"
            }
          }
        }
      ]
    }
```

And children of nested instances can be customized by prefixing their IDs with the containing instance’s ID and a slash in the `descendants` map:
```
{
      "id": "save-alert",
      "type": "ref",
      "ref": "alert",
      "descendants": {
        "message": {
          "content": "You have unsaved changes. Do you want to save them?"
        },
        "ok-button/label": { // <- we're customizing the "label" under "ok-button"
          "content": "Save"
        },
        "cancel-button/label": { // <- we're customizing the "label" under "cancel-button"
          "content": "Discard Changes",
          "fill": "#FF0000"
        }
      }
    }
```

In addition to customization, an object inside an instance can be completely replaced with new object:
```
{
      "id": "icon-button",
      "type": "ref",
      "ref": "round-button",
      "descendants": {
        "label": {
          "id": "icon",
          "type": "icon_font", // <- the presence of the `type` property indicates that this is an object replacement
          "iconFontFamily": "lucide",
          "icon": "check"
        }
      }
    }
```

Alternatively to 1:1 replacement, an object can be kept as is, and we can replace only its `children` with new objects:
```
{
      "id": "sidebar"
      "type": "frame",
      "reusable": true,
      "children": [
        {
          "id": "header",
          "type": "frame",
          "fill": "#FF0000"
        },
        {
          "id": "content",
          "type": "frame",
          "fill": "#00FF00"
        },
        {
          "id": "footer",
          "type": "frame",
          "fill": "#0000FF"
        }
      ]
    }
     
    {
      "id": "menu-sidebar"
      "type": "ref",
      "ref": "sidebar",
      "descendants": {
        "content": {
          "children": [ // <- the children of "content" are replaced with some "round-button" instances
            {
              "id": "home-button",
              "type": "ref",
              "ref": "round-button",
              "descendants": {
                "label": {
                  "text": "Home"
                }
              }
            },
            {
              "id": "settings-button",
              "type": "ref",
              "ref": "round-button",
              "descendants": {
                "label": {
                  "text": "Settings"
                }
              }
            },
            {
              "id": "help-button",
              "type": "ref",
              "ref": "round-button",
              "descendants": {
                "label": {
                  "text": "Help"
                }
              }
            }
          ]
        }
      }
    }
```

This children replacement mechanism is ideal for container-style components, like panels, cards, windows, sidebars, etc.

### Slots

When a frame inside a component is intended to have its children replaced (e.g. the content holder frame inside a panel), it can be marked with the `slot` property:
```
{
      "id": "sidebar"
      "type": "frame",
      "reusable": true,
      "children": [
        {
          "id": "header",
          "type": "frame",
          "fill": "#FF0000"
        },
        {
          "id": "content",
          "type": "frame",
          "fill": "#00FF00",
          "slot": [ // <- "content" is marked as a slot, which is intended to be populated with "round-button" or "icon-button" instances
            "round-button",
            "icon-button"
          ]
        },
        {
          "id": "footer",
          "type": "frame",
          "fill": "#0000FF"
        }
      ]
    }
```

Pencil displays such slots with a special effect, and lets users insert instances of the suggested components (i.e. `round-button` or `icon-button` above) with a single click.

## Variables and Themes

Pencil supports extracting commonly used colors and numeric values (padding, corner radius, opacity, etc.) into document-wide variables:
```
{
      "variables": {
        "color.background": {
          "type": "color",
          "value": "#FFFFFF"
        },
        "color.text": {
          "type": "color",
          "value": "#333333"
        },
        "text.title": {
          "type": "number",
          "value": 72
        }
      },
      "children": [
        {
          "id": "landing-page",
          "type": "frame",
          "fill": "$color.background",
          "children": [
            {
              "id": "welcome-label",
              "type": "text",
              "fill": "$color.text",
              "fontSize": "$text.title",
              "content": "Welcome!"
            }
          ]
        }
      ]
    }
```

Pencil also implements a powerful theming system, whereby variables can dynamically change their values depending on the theme configuration of each object:
```
{
      "variables": {
        "color.background": {
          "type": "color",
          "value": [ // <- when a variable has multiple values, the value that wins during evaluation is the _last_ one whose theme is satisfied
            { "value": "#FFFFFF", "theme": { "mode": "light" } },
            { "value": "#000000", "theme": { "mode": "dark" } }
          ]
        },
        "color.text": {
          "type": "color",
          "value": [
            { "value": "#333333", "theme": { "mode": "light" } },
            { "value": "#AAAAAA", "theme": { "mode": "dark" } }
          ]
        },
        "text.title": {
          "type": "number",
          "value": [
            { "value": 72, "theme": { "spacing": "regular" } },
            { "value": 36, "theme": { "spacing": "condensed" } }
          ]
        }
      },
      "themes": { // <- the default value of each theme axis is the first value, so the default theme is { "mode": "light", "spacing": "regular" }
        "mode": ["light", "dark"],
        "spacing": ["regular", "condensed"]
      },
      "children": [
        {
          "id": "landing-page-light",
          "type": "frame",
          "fill": "$color.background", // #FFFFFF
          "children": [
            {
              "id": "welcome-label",
              "type": "text",
              "fill": "$color.text", // #333333
              "fontSize": "$text.title", // 72
              "content": "Welcome!"
            }
          ]
        },
        {
          "id": "landing-page-dark",
          "type": "frame",
          "theme": { "mode": "dark" }, // <- everything under this frame is using "mode": "dark"
          "fill": "$color.background", // #000000
          "children": [
            {
              "id": "welcome-label",
              "type": "text",
              "fill": "$color.text", // #AAAAAA
              "fontSize": "$text.title", // 72
              "content": "Welcome!"
            }
          ]
        },
        {
          "id": "landing-page-dark-condensed",
          "type": "frame",
          "fill": "$color.background", // #000000
          "theme": { "mode": "dark", "spacing": "condensed" }, // <- everything under this frame is using { "mode": "dark", "spacing": "condensed" }
          "children": [
            {
              "id": "welcome-label",
              "type": "text",
              "fill": "$color.text", // #AAAAAA
              "fontSize": "$text.title", // 36
              "content": "Welcome!"
            }
          ]
        },
      ]
    }
```

## TypeScript Schema
```
/** Each key must be an existing theme axis, and each value must be one of the possible values for that axis. E.g. { 'device': 'phone' } */
    export interface Theme {
      [key: string]: string;
    }
     
    /** To bind a variable to a property, set the property to the dollar-prefixed name of the variable! */
    export type Variable = string;
     
    export type NumberOrVariable = number | Variable;
     
    /** Colors can be 8-digit RGBA hex strings (e.g. #AABBCCDD), 6-digit RGB hex strings (e.g. #AABBCC) or 3-digit RGB hex strings (e.g. #ABC which means #AABBCC). */
    export type Color = string;
     
    export type ColorOrVariable = Color | Variable;
     
    export type BooleanOrVariable = boolean | Variable;
     
    export type StringOrVariable = string | Variable;
     
    export interface Layout {
      /** Enable flex layout. None means all children are absolutely positioned and will not be affected by layout properties. Frames default to horizontal, groups default to none. */
      layout?: "none" | "vertical" | "horizontal";
      /** The gap between children in the main axis direction. Defaults to 0. */
      gap?: NumberOrVariable;
      layoutIncludeStroke?: boolean;
      /** The Inside padding along the edge of the container */
      padding?:
        | /** The inside padding to all sides */ NumberOrVariable
        | /** The inside horizontal and vertical padding */ [
            NumberOrVariable,
            NumberOrVariable,
          ]
        | /** Top, Right, Bottom, Left padding */ [
            NumberOrVariable,
            NumberOrVariable,
            NumberOrVariable,
            NumberOrVariable,
          ];
      /** Control the justify alignment of the children along the main axis. Defaults to 'start'. */
      justifyContent?:
        | "start"
        | "center"
        | "end"
        | "space_between"
        | "space_around";
      /** Control the alignment of children along the cross axis. Defaults to 'start'. */
      alignItems?: "start" | "center" | "end";
    }
     
    /** SizingBehavior controls the dynamic layout size.
    - fit_content: Use the combined size of all children for the container size. Fallback is used when there are no children.
    - fill_container: Use the parent size for the container size. Fallback is used when the parent has no layout.
    Optional number in parentheses (e.g., 'fit_content(100)') specifies the fallback size. */
    export type SizingBehavior = string;
     
    /** Position is relative to the parent object's position. X increases rightwards, Y increases downwards.
    IMPORTANT: x and y are IGNORED when parent uses flexbox layout. */
    export interface Position {
      x?: number;
      y?: number;
    }
     
    export interface Size {
      width?: NumberOrVariable | SizingBehavior;
      height?: NumberOrVariable | SizingBehavior;
    }
     
    export interface CanHaveRotation {
      /** Rotation is represented in degrees, measured counter-clockwise. */
      rotation?: NumberOrVariable;
    }
     
    export type BlendMode =
      | "normal"
      | "darken"
      | "multiply"
      | "linearBurn"
      | "colorBurn"
      | "light"
      | "screen"
      | "linearDodge"
      | "colorDodge"
      | "overlay"
      | "softLight"
      | "hardLight"
      | "difference"
      | "exclusion"
      | "hue"
      | "saturation"
      | "color"
      | "luminosity";
     
    export type Fill =
      | ColorOrVariable
      | {
          type: "color";
          enabled?: BooleanOrVariable;
          blendMode?: BlendMode;
          color: ColorOrVariable;
        }
      | {
          type: "gradient";
          enabled?: BooleanOrVariable;
          blendMode?: BlendMode;
          gradientType?: "linear" | "radial" | "angular";
          opacity?: NumberOrVariable;
          /** Normalized to bounding box (default: 0.5,0.5). */
          center?: Position;
          /** Normalized to bounding box (default: 1,1). Linear: height sets gradient length, width is ignored. Radial/Angular: sets ellipse diameters. */
          size?: { width?: NumberOrVariable; height?: NumberOrVariable };
          /** Rotation in degrees, counterclockwise (0° up, 90° left, 180° down). */
          rotation?: NumberOrVariable;
          colors?: { color: ColorOrVariable; position: NumberOrVariable }[];
        }
      /** Image fill. Url needs to be a relative from the pen file, for example `../../file.png` or `./image.jpg` */
      | {
          type: "image";
          enabled?: BooleanOrVariable;
          blendMode?: BlendMode;
          opacity?: NumberOrVariable;
          url: string;
          mode?: "stretch" | "fill" | "fit";
        }
      /** Grid of colors with bezier-interpolated edges. Row-major order. Adjust the points and handles to create complex gradients. Keep the points on the edges at their default position. */
      | {
          type: "mesh_gradient";
          enabled?: BooleanOrVariable;
          blendMode?: BlendMode;
          opacity?: NumberOrVariable;
          columns?: number;
          rows?: number;
          /** Color per vertex. */
          colors?: ColorOrVariable[];
          /** columns * rows points in [0,1] normalized coordinates. */
          points?: (
            | /** Position with auto-generated handles. */ [number, number]
            | /** Position with optional bezier handles (relative offsets). Omitted handles are auto-generated. */ {
                position: [number, number];
                leftHandle?: [number, number];
                rightHandle?: [number, number];
                topHandle?: [number, number];
                bottomHandle?: [number, number];
              }
          )[];
        };
     
    export type Fills = Fill | Fill[];
     
    export interface Stroke {
      align?: "inside" | "center" | "outside";
      thickness?:
        | NumberOrVariable
        | {
            top?: NumberOrVariable;
            right?: NumberOrVariable;
            bottom?: NumberOrVariable;
            left?: NumberOrVariable;
          };
      join?: "miter" | "bevel" | "round";
      miterAngle?: NumberOrVariable;
      cap?: "none" | "round" | "square";
      dashPattern?: number[];
      fill?: Fills;
    }
     
    export type Effect =
      /** 'blur' type blurs the entire layer content */
      | { enabled?: BooleanOrVariable; type: "blur"; radius?: NumberOrVariable }
      /** 'background_blur' type blurs the background content behind the layer */
      | {
          enabled?: BooleanOrVariable;
          type: "background_blur";
          radius?: NumberOrVariable;
        }
      /** The drop shadow effect can be an inner or outer shadow, with adjustable offset, spread, blur, color and blend mode. */
      | {
          type: "shadow";
          enabled?: BooleanOrVariable;
          shadowType?: "inner" | "outer";
          offset?: { x: NumberOrVariable; y: NumberOrVariable };
          spread?: NumberOrVariable;
          blur?: NumberOrVariable;
          color?: ColorOrVariable;
          blendMode?: BlendMode;
        };
     
    export type Effects = Effect | Effect[];
     
    export interface CanHaveGraphics {
      stroke?: Stroke;
      fill?: Fills;
      effect?: Effects;
    }
     
    export interface CanHaveEffects {
      effect?: Effects;
    }
     
    /** Entities have unique identifiers. */
    export interface Entity extends Position, CanHaveRotation {
      /** A unique string that MUST NOT contain slash (/) characters. If omitted, a unique ID will be generated automatically. */
      id: string;
      /** Optional name for the entity, used for display and identification purposes */
      name?: string;
      /** Optional context information about this object. */
      context?: string;
      /** Objects are not reusable by default. If an object is made reusable by setting this property to `true`, the object can be duplicated using `ref` objects. */
      reusable?: boolean;
      theme?: Theme;
      enabled?: BooleanOrVariable;
      opacity?: NumberOrVariable;
      flipX?: BooleanOrVariable;
      flipY?: BooleanOrVariable;
      metadata?: { type: string; [key: string]: any };
    }
     
    export interface Rectangleish extends Entity, Size, CanHaveGraphics {
      cornerRadius?:
        | NumberOrVariable
        | [NumberOrVariable, NumberOrVariable, NumberOrVariable, NumberOrVariable];
    }
     
    /** A rectangle is defined by its position and size. The position corresponds to the top-left corner. */
    export interface Rectangle extends Rectangleish {
      type: "rectangle";
    }
     
    /** An ellipse is defined by its bounding rectangle's position and size. */
    export interface Ellipse extends Entity, Size, CanHaveGraphics {
      type: "ellipse";
      /** Inner-to-outer radius ratio for ring shapes. 0 = solid, 1 = fully hollow. Default: 0. */
      innerRadius?: NumberOrVariable;
      /** Arc start angle in degrees, counter-clockwise from the right. Default: 0. */
      startAngle?: NumberOrVariable;
      /** Arc length in degrees from startAngle. Positive = counter-clockwise, negative = clockwise. Range: -360 to 360. Default: 360 (full ellipse). */
      sweepAngle?: NumberOrVariable;
    }
     
    /** A line is defined by its bounding rectangle's position and size. */
    export interface Line extends Entity, Size, CanHaveGraphics {
      type: "line";
    }
     
    /** A regular polygon is defined by its bounding rectangle's position and size. */
    export interface Polygon extends Entity, Size, CanHaveGraphics {
      type: "polygon";
      polygonCount?: NumberOrVariable;
      cornerRadius?: NumberOrVariable;
    }
     
    export interface Path extends Entity, Size, CanHaveGraphics {
      /** fillRule is used to determine which parts of the path are considered inside the shape to be filled. Default is 'nonzero'. */
      fillRule?: "nonzero" | "evenodd";
      /** SVG Path */
      geometry?: string;
      type: "path";
    }
     
    export interface TextStyle {
      fontFamily?: StringOrVariable;
      fontSize?: NumberOrVariable;
      fontWeight?: StringOrVariable;
      letterSpacing?: NumberOrVariable;
      fontStyle?: StringOrVariable;
      underline?: BooleanOrVariable;
      /** A multiplier that gets applied to the font size to determine spacing between lines. If not specified, uses the font's built-in line height. */
      lineHeight?: NumberOrVariable;
      textAlign?: "left" | "center" | "right" | "justify";
      textAlignVertical?: "top" | "middle" | "bottom";
      strikethrough?: BooleanOrVariable;
      href?: string;
    }
     
    export type TextContent = StringOrVariable | TextStyle[];
     
    export interface Text extends Entity, Size, CanHaveGraphics, TextStyle {
      type: "text";
      content?: TextContent;
      /** textGrowth controls how the text box dimensions behave. It must be set before width or height can be used — without textGrowth, the width and height properties are ignored.
    'auto': The text box automatically grows to fit the text content. Text does not wrap. Width and height adjust dynamically.
    'fixed-width': The width is fixed and text wraps within it. The height grows automatically to fit the wrapped content.
    'fixed-width-height': Both width and height are fixed. Text wraps and may be overflow if it exceeds the bounds.
    IMPORTANT: Never set width or height without also setting textGrowth. If you want to control the size of a text box, you must set textGrowth first. */
      textGrowth?: "auto" | "fixed-width" | "fixed-width-height";
    }
     
    export interface CanHaveChildren {
      children?: Child[];
    }
     
    /** A frame is a rectangle that can have children. */
    export interface Frame extends Rectangleish, CanHaveChildren, Layout {
      type: "frame";
      /** Visually clip content that overflows the frame bounds. Default is false. */
      clip?: BooleanOrVariable;
      placeholder?: boolean;
      /** The presence of this property indicates that this frame is a "slot" - which means that it is intended be customized with children in instances of the parent component. Each element of the array is an ID of a "recommended" reusable component, one which fits semantically as a child here (e.g. inside a menu bar, the content slot would recommend IDs of various menu item components). */
      slot?: string[];
    }
     
    export interface Group extends Entity, CanHaveChildren, CanHaveEffects, Layout {
      type: "group";
      width?: SizingBehavior;
      height?: SizingBehavior;
    }
     
    export interface Note extends Entity, Size, TextStyle {
      type: "note";
      content?: TextContent;
    }
     
    export interface Prompt extends Entity, Size, TextStyle {
      type: "prompt";
      content?: TextContent;
      model?: StringOrVariable;
    }
     
    export interface Context extends Entity, Size, TextStyle {
      type: "context";
      content?: TextContent;
    }
     
    /** Icon from a font */
    export interface IconFont extends Entity, Size, CanHaveEffects {
      type: "icon_font";
      /** Name of the icon in the icon font */
      iconFontName?: StringOrVariable;
      /** Icon font to use. Valid fonts are 'lucide', 'feather', 'Material Symbols Outlined', 'Material Symbols Rounded', 'Material Symbols Sharp', 'phosphor' */
      iconFontFamily?: StringOrVariable;
      /** Variable font weight, only valid for icon fonts with variable weight. Values from 100 to 700. */
      weight?: NumberOrVariable;
      fill?: Fills;
    }
     
    /** References allow reusing other objects in different places. */
    export interface Ref extends Entity {
      type: "ref";
      /** The `ref` property must be another object's ID. */
      ref: string;
      /** This can be used to customize the properties of descendant objects except the `children` property. */
      descendants?: {
        [
          key: string /** Each key is an ID path pointing to a descendant object. */
        ]: {} /** Descendant objects can be customized in two manners:
    - Property overrides: only the customized properties are present with their new values. In this case, the `id`, `type` and `children` properties must not be specified!
    - Object replacement: in this case, this object must be a completely new node tree, that will replace the original descendant of the referenced component. This is useful for adding custom content to instances of container-type components (cards, windows, panels, etc). */;
      };
      [key: string]: any;
    }
     
    export type Child =
      | Frame
      | Group
      | Rectangle
      | Ellipse
      | Line
      | Path
      | Polygon
      | Text
      | Note
      | Prompt
      | Context
      | IconFont
      | Ref;
     
    export type IdPath = string;
     
    export interface Document {
      version: string;
      themes?: { [key: string /** RegEx: [^:]+ */]: string[] };
      imports?: {
        [
          key: string
        ]: string /** Each value is a path to an imported .pen file, from which variables and reusable components are made available in the current file. The key is a short alias for the imported file. */;
      };
      variables?: {
        [key: string /** RegEx: [^:]+ */]:
          | {
              type: "boolean";
              value:
                | BooleanOrVariable
                | { value: BooleanOrVariable; theme?: Theme }[];
            }
          | {
              type: "color";
              value: ColorOrVariable | { value: ColorOrVariable; theme?: Theme }[];
            }
          | {
              type: "number";
              value:
                | NumberOrVariable
                | { value: NumberOrVariable; theme?: Theme }[];
            }
          | {
              type: "string";
              value:
                | StringOrVariable
                | { value: StringOrVariable; theme?: Theme }[];
            };
      };
      children: (
        | Frame
        | Group
        | Rectangle
        | Ellipse
        | Line
        | Polygon
        | Path
        | Text
        | Note
        | Context
        | Prompt
        | IconFont
        | Ref
      )[];
    }
```


---

<a id="page-18"></a>
---
url: https://docs.pencil.dev/for-developers/pencil-cli
---

# Pencil CLI

This feature is experimental and only available in the desktop app. Options and configuration may change.

Running Pencil from the terminal for batch operations is now possible. We are documenting this very early, so you can try it, but please note that this is still under heavy development and the options and the config might change. This allows you to take the generative pipeline to the next-level and start building your own AI design agency.

## Running `pencil` from Terminal

![Running multiple Pencil agent windows from CLI](https://docs.pencil.dev/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fpencil-cli.88c4f22b.png&w=3840&q=75&dpl=dpl_78EpAuSgmGDn3KUwfChZTSm6jsJg)

  * on Mac and Linux you can add `pencil` command to PATH
  * Go to File -> **Install`pencil` command into PATH**
  * Reset your terminal and you should be able to run `pencil`

```
pencil --agent-config config.json
```

## Agent Config Example

Running multiple Pencil prompts at the same time via agent config from Terminal. This will open multiple Pencil windows with the defined files and start prompt in them. Important: it’s key that you create an empty .pen files ahead of time. It currently can’t create files.

Parameters:

  * file: path to file, absolute or relative from the place where you run pencil
  * prompt: the prompt you want to run in the chat
  * model: available models, might change as we update the app
  * attachments: an array of files that you want to attach to the prompt, could be multiple text files like .md or images (.jpg, .png)

**config.json**
```
[
      {
        "file": "./run1/file1.pen",
        "prompt": "design a SaaS analytics dashboard for a startup that tracks user engagement metrics, with a sidebar navigation, KPI cards, charts, and a data table",
        "model": "claude-4.5-haiku",
        "attachments": ["spec-design.md", "image-inspiration.png"]
      },
      {
        "file": "./run1/file2.pen",
        "prompt": "design a SaaS analytics dashboard for a startup that tracks user engagement metrics, with a sidebar navigation, KPI cards, charts, and a data table",
        "model": "claude-4.5-sonnet",
        "attachments": ["spec-design.md", "image-inspiration.png"]
      },
      {
        "file": "./run1/file3.pen",
        "prompt": "design a SaaS analytics dashboard for a startup that tracks user engagement metrics, with a sidebar navigation, KPI cards, charts, and a data table",
        "model": "claude-4.6-opus",
        "attachments": ["spec-design.md", "image-inspiration.png"]
     
      },
      {
        "file": "./run1/file4.pen",
        "prompt": "design a landing page for a premium architectural firm showcasing luxury residential projects, with bold typography, full-bleed imagery, and a project gallery",
        "model": "claude-4.5-haiku"
      },
      {
        "file": "./run1/file5.pen",
        "prompt": "design a landing page for a premium architectural firm showcasing luxury residential projects, with bold typography, full-bleed imagery, and a project gallery",
        "model": "claude-4.5-sonnet"
      },
      {
        "file": "./run1/file6.pen",
        "prompt": "design a landing page for a premium architectural firm showcasing luxury residential projects, with bold typography, full-bleed imagery, and a project gallery",
        "model": "claude-4.6-opus"
      }
    ]
```

## Headless optimized version coming soon

  * Currently you need to have a desktop app installed to use pencil from CLI, but soon that’s going to change
  * We are working on the headless pencil-cli version that’s optimized for agentic running or server-side use cases
  * This version has minimal footprint and allows you to manipulate the .pen files directly from CLI
  * It will be distributed as an npm package
  * More info coming soon


---

