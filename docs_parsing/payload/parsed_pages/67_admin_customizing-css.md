<a id="page-67"></a>
---
url: https://payloadcms.com/docs/admin/customizing-css
---

# Customizing CSS & SCSS

Customizing the Payload [Admin Panel](./overview) through CSS alone is one of the easiest and most powerful ways to customize the look and feel of the dashboard. To allow for this level of customization, Payload:

  1. Exposes a root-level stylesheet for you to inject custom selectors
  2. Provides a CSS library that can be easily overridden or extended
  3. Uses [BEM naming conventions](http://getbem.com) so that class names are globally accessible



To customize the CSS within the Admin UI, determine scope and change you'd like to make, and then add your own CSS or SCSS to the configuration as needed.

## [Global CSS](/docs/admin/customizing-css#global-css)

Global CSS refers to the CSS that is applied to the entire [Admin Panel](./overview). This is where you can have a significant impact to the look and feel of the Admin UI through just a few lines of code.

You can add your own global CSS through the root `custom.scss` file of your app. This file is loaded into the root of the Admin Panel and can be used to inject custom selectors or styles however needed.

Here is an example of how you might target the Dashboard View and change the background color:
```
.dashboard {
      background-color: red; 
    }
```

**Note:** If you are building [Custom Components](../custom-components/overview), it is best to import your own stylesheets directly into your components, rather than using the global stylesheet. You can continue to use the CSS library as needed.

### [Specificity rules](/docs/admin/customizing-css#specificity-rules)

All Payload CSS is encapsulated inside CSS layers under `@layer payload-default`. Any custom css will now have the highest possible specificity.

We have also provided a layer `@layer payload` if you want to use layers and ensure that your styles are applied after payload.

To override existing styles in a way that the previous rules of specificity would be respected you can use the default layer like so
```
@layer payload-default {
      // my styles within the Payload specificity
    }
```

## [Re-using Payload SCSS variables and utilities](/docs/admin/customizing-css#re-using-payload-scss-variables-and-utilities)

You can re-use Payload's SCSS variables and utilities in your own stylesheets by importing it from the UI package.
```
@import '~@payloadcms/ui/scss';
```

## [CSS Library](/docs/admin/customizing-css#css-library)

To make it as easy as possible for you to override default styles, Payload uses [BEM naming conventions](http://getbem.com/) for all CSS within the Admin UI. If you provide your own CSS, you can override any built-in styles easily, including targeting nested components and their various component states.

You can also override Payload's built-in [CSS Variables](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties). These variables are widely consumed by the Admin Panel, so modifying them has a significant impact on the look and feel of the Admin UI.

The following variables are defined and can be overridden:

  * [Breakpoints](https://github.com/payloadcms/payload/blob/main/packages/ui/src/scss/queries.scss)
  * [Colors](https://github.com/payloadcms/payload/blob/main/packages/ui/src/scss/colors.scss)
  * Base color shades (white to black by default)
  * Success / warning / error color shades
  * Theme-specific colors (background, input background, text color, etc.)
  * Elevation colors (used to determine how "bright" something should be when compared to the background)
  * [Sizing](https://github.com/payloadcms/payload/blob/main/packages/ui/src/scss/app.scss)
  * Horizontal gutter
  * Transition speeds
  * Font sizes
  * Etc.



For an up-to-date, comprehensive list of all available variables, please refer to the [Source Code](https://github.com/payloadcms/payload/blob/main/packages/ui/src/scss).

**Warning:** If you're overriding colors or theme elevations, make sure to consider how your changes will affect dark mode.

#### [Dark Mode](/docs/admin/customizing-css#dark-mode)

Colors are designed to automatically adapt to theme of the [Admin Panel](./overview). By default, Payload automatically overrides all `--theme-elevation` colors and inverts all success / warning / error shades to suit dark mode. We also update some base theme variables like `--theme-bg`, `--theme-text`, etc.

[Next Managing User Preferences](/docs/admin/preferences)

#### Related Guides

  * [How to theme the Payload admin panel with Tailwind CSS 4 ](/posts/guides/how-to-theme-the-payload-admin-panel-with-tailwind-css-4)
  * [How to setup Tailwind CSS and shadcn/ui in Payload ](/posts/guides/how-to-setup-tailwindcss-and-shadcn-ui-in-payload)
