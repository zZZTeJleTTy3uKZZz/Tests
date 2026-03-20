<a id="page-44"></a>
---
url: https://payloadcms.com/docs/hooks/overview
---

# Hooks Overview

Hooks allow you to execute your own side effects during specific events of the Document lifecycle. They allow you to do things like mutate data, perform business logic, integrate with third-parties, or anything else, all during precise moments within your application.

With Hooks, you can transform Payload from a traditional CMS into a fully-fledged application framework. There are many use cases for Hooks, including:

  * Modify data before it is read or updated
  * Encrypt and decrypt sensitive data
  * Integrate with a third-party CRM like HubSpot or Salesforce
  * Send a copy of uploaded files to Amazon S3 or similar
  * Process orders through a payment provider like Stripe
  * Send emails when contact forms are submitted
  * Track data ownership or changes over time



There are four main types of Hooks in Payload:

  * Root Hooks
  * [Collection Hooks](../hooks/collections)
  * [Global Hooks](../hooks/globals)
  * [Field Hooks](../hooks/fields)



**Reminder:** Payload also ships a set of _React_ hooks that you can use in your frontend application. Although they share a common name, these are very different things and should not be confused. [More details](../admin/react-hooks).

## [Root Hooks](/docs/hooks/overview#root-hooks)

Root Hooks are not associated with any specific Collection, Global, or Field. They are useful for globally-oriented side effects, such as when an error occurs at the application level.

To add Root Hooks, use the `hooks` property in your [Payload Config](../configuration/overview):
```
import { buildConfig } from 'payload'
    
    
    export default buildConfig({
      // ...
      hooks: {
        afterError:[() => {...}]
      },
    })
```

The following options are available:

Option |  Description   
---|---  
`**afterError**` |  Runs after an error occurs in the Payload application.   
  
### [afterError](/docs/hooks/overview#aftererror)

The `afterError` Hook is triggered when an error occurs in the Payload application. This can be useful for logging errors to a third-party service, sending an email to the development team, logging the error to Sentry or DataDog, etc. The output can be used to transform the result object / status code.
```
import { buildConfig } from 'payload'
    
    
    export default buildConfig({
      // ...
      hooks: {
        afterError: [
          async ({ error }) => {
            // Do something
          },
        ],
      },
    })
```

The following arguments are provided to the `afterError` Hook:

Argument |  Description   
---|---  
`**error**` |  The error that occurred.   
`**context**` |  Custom context passed between Hooks. [More details](./context).   
`**graphqlResult**` |  The GraphQL result object, available if the hook is executed within a GraphQL context.   
`**req**` |  The `PayloadRequest` object that extends [Web Request](https://developer.mozilla.org/en-US/docs/Web/API/Request). Contains currently authenticated `user` and the Local API instance `payload`.   
`**collection**` |  The [Collection](../configuration/collections) in which this Hook is running against. This will be `undefined` if the hook is executed from a non-collection endpoint or GraphQL.   
`**result**` |  The formatted error result object, available if the hook is executed from a REST context.   
  
## [Awaited vs. non-blocking hooks](/docs/hooks/overview#awaited-vs-non-blocking-hooks)

Hooks can either block the request until they finish or run without blocking it. What matters is whether your hook returns a Promise.

Awaited (blocking): If your hook returns a Promise (for example, if it’s declared async), Payload will wait for it to resolve before continuing that lifecycle step. Use this when your hook needs to modify data or influence the response. Hooks that return Promises run in series at the same lifecycle stage.

Non-blocking (sometimes called “fire-and-forget”): If your hook does not return a Promise (returns nothing), Payload will not wait for it to finish. This can be useful for side-effects that don’t affect the outcome of the operation, but keep in mind that any work started this way might continue after the request has already completed.

**Declaring a function with async does not make it “synchronous.” The async keyword simply makes the function return a Promise automatically — which is why Payload then awaits it.**

**Tip:** If your hook executes a long-running task that doesn't affect the response in any way, consider offloading it to the job queue. That will free up the request to continue processing without waiting for the task to complete.

**Awaited**
```
const beforeChange = async ({ data }) => {
      const enriched = await fetchProfile(data.userId) // Payload waits here
      return { ...data, profile: enriched }
    }
```

**Non-blocking**
```
const afterChange = ({ doc }) => {
      // Trigger side-effect without blocking
      void pingAnalyticsService(doc.id)
      // No return → Payload does not wait
    }
```

## [Server-only Execution](/docs/hooks/overview#server-only-execution)

Hooks are only triggered on the server and are automatically excluded from the client-side bundle. This means that you can safely use sensitive business logic in your Hooks without worrying about exposing it to the client.

## [Performance](/docs/hooks/overview#performance)

Hooks are a powerful way to customize the behavior of your APIs, but some hooks are run very often and can add significant overhead to your requests if not optimized.

When building hooks, combine together as many of these strategies as possible to ensure your hooks are as performant as they can be.

For more performance tips, see the [Performance documentation](../performance/overview).

### [Writing efficient hooks](/docs/hooks/overview#writing-efficient-hooks)

Consider when hooks are run. One common pitfall is putting expensive logic in hooks that run very often.

For example, the `read` operation runs on every read request, so avoid putting expensive logic in a `beforeRead` or `afterRead` hook.
```
{
      hooks: {
        beforeRead: [
          async () => {
            // This runs on every read request - avoid expensive logic here
            await doSomethingExpensive()
            return data
          },
        ],
      },
    }
```

Instead, you might want to use a `beforeChange` or `afterChange` hook, which only runs when a document is created or updated.
```
{
      hooks: {
        beforeChange: [
          async ({ context }) => {
            // This is more acceptable here, although still should be mindful of performance
            await doSomethingExpensive()
            // ...
          },
        ]
      },
    }
```

### [Using Hook Context](/docs/hooks/overview#using-hook-context)

Use [Hook Context](./context) to avoid infinite loops or to prevent repeating expensive operations across multiple hooks in the same request.
```
{
      hooks: {
        beforeChange: [
          async ({ context }) => {
            const somethingExpensive = await doSomethingExpensive()
            context.somethingExpensive = somethingExpensive
            // ...
          },
        ],
      },
    }
```

To learn more, see the [Hook Context documentation](./context).

### [Offloading to the jobs queue](/docs/hooks/overview#offloading-to-the-jobs-queue)

If your hooks perform any long-running tasks that don't directly affect the request lifecycle, consider offloading them to the [jobs queue](../jobs-queue/overview). This will free up the request to continue processing without waiting for the task to complete.
```
{
      hooks: {
        afterChange: [
          async ({ doc, req }) => {
            // Offload to job queue
            await req.payload.jobs.queue(...)
            // ...
          },
        ],
      },
    }
```

To learn more, see the [Job Queue documentation](../jobs-queue/overview).

[Next Collection Hooks](/docs/hooks/collections)
