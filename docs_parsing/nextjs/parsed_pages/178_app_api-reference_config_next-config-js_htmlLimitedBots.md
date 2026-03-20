<a id="page-178"></a>
---
url: https://nextjs.org/docs/app/api-reference/config/next-config-js/htmlLimitedBots
---

[Configuration](/docs/app/api-reference/config)[next.config.js](/docs/app/api-reference/config/next-config-js)htmlLimitedBots

# htmlLimitedBots

Last updated February 20, 2026

The `htmlLimitedBots` config allows you to specify a list of user agents that should receive blocking metadata instead of [streaming metadata](/docs/app/api-reference/functions/generate-metadata#streaming-metadata).

next.config.ts

TypeScript

JavaScriptTypeScript
```
import type { NextConfig } from 'next'
     
    const config: NextConfig = {
      htmlLimitedBots: /MySpecialBot|MyAnotherSpecialBot|SimpleCrawler/,
    }
     
    export default config
```

## Default list

Next.js includes a default list of HTML limited bots, including:

  * Google crawlers (e.g. Mediapartners-Google, AdsBot-Google, Google-PageRenderer)
  * Bingbot
  * Twitterbot
  * Slackbot



See the full list [here](https://github.com/vercel/next.js/blob/canary/packages/next/src/shared/lib/router/utils/html-bots.ts).

Specifying a `htmlLimitedBots` config will override the Next.js' default list. However, this is advanced behavior, and the default should be sufficient for most cases.

next.config.ts

TypeScript

JavaScriptTypeScript
```
const config: NextConfig = {
      htmlLimitedBots: /MySpecialBot|MyAnotherSpecialBot|SimpleCrawler/,
    }
     
    export default config
```

## Disabling

To fully disable streaming metadata:

next.config.ts
```
import type { NextConfig } from 'next'
     
    const config: NextConfig = {
      htmlLimitedBots: /.*/,
    }
     
    export default config
```

## Version History

Version| Changes  
---|---  
15.2.0| `htmlLimitedBots` option introduced.  
  
Was this helpful?

supported.

Send
