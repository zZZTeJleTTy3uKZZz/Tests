<a id="page-337"></a>
---
url: https://nextjs.org/docs/pages/api-reference/config/next-config-js/distDir
---

[Configuration](/docs/pages/api-reference/config)[next.config.js Options](/docs/pages/api-reference/config/next-config-js)distDir

# distDir

Last updated February 20, 2026

You can specify a name to use for a custom build directory to use instead of `.next`.

Open `next.config.js` and add the `distDir` config:

next.config.js
```
module.exports = {
      distDir: 'build',
    }
```

Now if you run `next build` Next.js will use `build` instead of the default `.next` folder.

> `distDir` **should not** leave your project directory. For example, `../build` is an **invalid** directory.

Was this helpful?

supported.

Send
