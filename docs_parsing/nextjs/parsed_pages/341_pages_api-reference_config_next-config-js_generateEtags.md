<a id="page-341"></a>
---
url: https://nextjs.org/docs/pages/api-reference/config/next-config-js/generateEtags
---

[Configuration](/docs/pages/api-reference/config)[next.config.js Options](/docs/pages/api-reference/config/next-config-js)generateEtags

# generateEtags

Last updated February 20, 2026

Next.js will generate [etags](https://en.wikipedia.org/wiki/HTTP_ETag) for every page by default. You may want to disable etag generation for HTML pages depending on your cache strategy.

Open `next.config.js` and disable the `generateEtags` option:

next.config.js
```
module.exports = {
      generateEtags: false,
    }
```

Was this helpful?

supported.

Send
