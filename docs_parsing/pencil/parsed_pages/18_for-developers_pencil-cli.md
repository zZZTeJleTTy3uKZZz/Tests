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
