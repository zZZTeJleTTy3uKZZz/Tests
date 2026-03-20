<a id="page-175"></a>
---
url: https://nextjs.org/docs/app/api-reference/config/next-config-js/generateBuildId
---

[Configuration](/docs/app/api-reference/config)[next.config.js](/docs/app/api-reference/config/next-config-js)generateBuildId

# generateBuildId

Last updated February 20, 2026

Next.js generates an ID during `next build` to identify which version of your application is being served. The same build should be used and boot up multiple containers.

If you are rebuilding for each stage of your environment, you will need to generate a consistent build ID to use between containers. Use the `generateBuildId` command in `next.config.js`:

next.config.js
```
module.exports = {
      generateBuildId: async () => {
        // This could be anything, using the latest git hash
        return process.env.GIT_HASH
      },
    }
```

Was this helpful?

supported.

Send
