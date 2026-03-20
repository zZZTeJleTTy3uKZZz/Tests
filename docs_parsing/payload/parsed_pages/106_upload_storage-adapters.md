<a id="page-106"></a>
---
url: https://payloadcms.com/docs/upload/storage-adapters
---

# Storage Adapters

Payload offers additional storage adapters to handle file uploads. These adapters allow you to store files in different locations, such as Amazon S3, Vercel Blob Storage, Google Cloud Storage, and more.

Service |  Package   
---|---  
Vercel Blob |  [`@payloadcms/storage-vercel-blob`](https://github.com/payloadcms/payload/tree/main/packages/storage-vercel-blob)  
AWS S3 |  [`@payloadcms/storage-s3`](https://github.com/payloadcms/payload/tree/main/packages/storage-s3)  
Azure |  [`@payloadcms/storage-azure`](https://github.com/payloadcms/payload/tree/main/packages/storage-azure)  
Google Cloud Storage |  [`@payloadcms/storage-gcs`](https://github.com/payloadcms/payload/tree/main/packages/storage-gcs)  
Uploadthing |  [`@payloadcms/storage-uploadthing`](https://github.com/payloadcms/payload/tree/main/packages/storage-uploadthing)  
R2 |  [`@payloadcms/storage-r2`](https://github.com/payloadcms/payload/tree/main/packages/storage-r2)  
  
## [Vercel Blob Storage](/docs/upload/storage-adapters#vercel-blob-storage)

[`@payloadcms/storage-vercel-blob`](https://www.npmjs.com/package/@payloadcms/storage-vercel-blob)

### [Installation](/docs/upload/storage-adapters#vercel-blob-installation)
```
pnpm add @payloadcms/storage-vercel-blob
```

### [Usage](/docs/upload/storage-adapters#vercel-blob-usage)

  * Configure the `collections` object to specify which collections should use the Vercel Blob adapter. The slug _must_ match one of your existing collection slugs.
  * Ensure you have `BLOB_READ_WRITE_TOKEN` set in your Vercel environment variables. This is usually set by Vercel automatically after adding blob storage to your project.
  * When enabled, this package will automatically set `disableLocalStorage` to `true` for each collection.
  * When deploying to Vercel, server uploads are limited with 4.5MB. Set `clientUploads` to `true` to do uploads directly on the client.


```
import { vercelBlobStorage } from '@payloadcms/storage-vercel-blob'
    import { Media } from './collections/Media'
    import { MediaWithPrefix } from './collections/MediaWithPrefix'
    
    
    export default buildConfig({
      collections: [Media, MediaWithPrefix],
      plugins: [
        vercelBlobStorage({
          enabled: true, // Optional, defaults to true
          // Specify which collections should use Vercel Blob
          collections: {
            media: true,
            'media-with-prefix': {
              prefix: 'my-prefix',
            },
          },
          // Token provided by Vercel once Blob storage is added to your Vercel project
          token: process.env.BLOB_READ_WRITE_TOKEN,
        }),
      ],
    })
```

### [Configuration Options](/docs/upload/storage-adapters#vercel-blob-configuration)

Option |  Description |  Default   
---|---|---  
`enabled` |  Whether or not to enable the plugin |  `true`  
`collections` |  Collections to apply the Vercel Blob adapter to |   
`addRandomSuffix` |  Add a random suffix to the uploaded file name in Vercel Blob storage |  `false`  
`cacheControlMaxAge` |  Cache-Control max-age in seconds |  `365 * 24 * 60 * 60` (1 Year)   
`token` |  Vercel Blob storage read/write token |  `''`  
`clientUploads` |  Do uploads directly on the client to bypass limits on Vercel. |   
  
## [S3 Storage](/docs/upload/storage-adapters#s3-storage)

[`@payloadcms/storage-s3`](https://www.npmjs.com/package/@payloadcms/storage-s3)

### [Installation](/docs/upload/storage-adapters#s3-installation)
```
pnpm add @payloadcms/storage-s3
```

### [Usage](/docs/upload/storage-adapters#s3-usage)

  * Configure the `collections` object to specify which collections should use the S3 Storage adapter. The slug _must_ match one of your existing collection slugs.
  * The `config` object can be any [`S3ClientConfig`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/s3) object (from [`@aws-sdk/client-s3`](https://github.com/aws/aws-sdk-js-v3)). _This is highly dependent on your AWS setup_. Check the AWS documentation for more information.
  * When enabled, this package will automatically set `disableLocalStorage` to `true` for each collection.
  * When deploying to Vercel, server uploads are limited with 4.5MB. Set `clientUploads` to `true` to do uploads directly on the client. You must allow CORS PUT method for the bucket to your website.
  * Configure `signedDownloads` (either globally of per-collection in `collections`) to use [presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html) for files downloading. This can improve performance for large files (like videos) while still respecting your access control. Additionally, with `signedDownloads.shouldUseSignedURL` you can specify a condition whether Payload should use a presigned URL, if you want to use this feature only for specific files.


```
import { s3Storage } from '@payloadcms/storage-s3'
    import { Media } from './collections/Media'
    import { MediaWithPrefix } from './collections/MediaWithPrefix'
    
    
    export default buildConfig({
      collections: [Media, MediaWithPrefix],
      plugins: [
        s3Storage({
          collections: {
            media: true,
            'media-with-prefix': {
              prefix,
            },
            'media-with-presigned-downloads': {
              // Filter only mp4 files
              signedDownloads: {
                shouldUseSignedURL: ({ collection, filename, req }) => {
                  return filename.endsWith('.mp4')
                },
              },
            },
          },
          bucket: process.env.S3_BUCKET,
          config: {
            credentials: {
              accessKeyId: process.env.S3_ACCESS_KEY_ID,
              secretAccessKey: process.env.S3_SECRET_ACCESS_KEY,
            },
            region: process.env.S3_REGION,
            // ... Other S3 configuration
          },
        }),
      ],
    })
```

### [Configuration Options](/docs/upload/storage-adapters#s3-configuration)

See the [AWS SDK Package](https://github.com/aws/aws-sdk-js-v3) and [`S3ClientConfig`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/s3) object for guidance on AWS S3 configuration.

## [Azure Blob Storage](/docs/upload/storage-adapters#azure-blob-storage)

[`@payloadcms/storage-azure`](https://www.npmjs.com/package/@payloadcms/storage-azure)

### [Installation](/docs/upload/storage-adapters#azure-installation)
```
pnpm add @payloadcms/storage-azure
```

### [Usage](/docs/upload/storage-adapters#azure-usage)

  * Configure the `collections` object to specify which collections should use the Azure Blob adapter. The slug _must_ match one of your existing collection slugs.
  * When enabled, this package will automatically set `disableLocalStorage` to `true` for each collection.
  * When deploying to Vercel, server uploads are limited with 4.5MB. Set `clientUploads` to `true` to do uploads directly on the client. You must allow CORS PUT method to your website.


```
import { azureStorage } from '@payloadcms/storage-azure'
    import { Media } from './collections/Media'
    import { MediaWithPrefix } from './collections/MediaWithPrefix'
    
    
    export default buildConfig({
      collections: [Media, MediaWithPrefix],
      plugins: [
        azureStorage({
          collections: {
            media: true,
            'media-with-prefix': {
              prefix,
            },
          },
          allowContainerCreate:
            process.env.AZURE_STORAGE_ALLOW_CONTAINER_CREATE === 'true',
          baseURL: process.env.AZURE_STORAGE_ACCOUNT_BASEURL,
          connectionString: process.env.AZURE_STORAGE_CONNECTION_STRING,
          containerName: process.env.AZURE_STORAGE_CONTAINER_NAME,
        }),
      ],
    })
```

### [Configuration Options](/docs/upload/storage-adapters#azure-configuration)

Option |  Description |  Default   
---|---|---  
`enabled` |  Whether or not to enable the plugin |  `true`  
`collections` |  Collections to apply the Azure Blob adapter to |   
`allowContainerCreate` |  Whether or not to allow the container to be created if it does not exist |  `false`  
`baseURL` |  Base URL for the Azure Blob storage account |   
`connectionString` |  Azure Blob storage connection string |   
`containerName` |  Azure Blob storage container name |   
`clientUploads` |  Do uploads directly on the client to bypass limits on Vercel. |   
  
## [Google Cloud Storage](/docs/upload/storage-adapters#google-cloud-storage)

[`@payloadcms/storage-gcs`](https://www.npmjs.com/package/@payloadcms/storage-gcs)

### [Installation](/docs/upload/storage-adapters#gcs-installation)
```
pnpm add @payloadcms/storage-gcs
```

### [Usage](/docs/upload/storage-adapters#gcs-usage)

  * Configure the `collections` object to specify which collections should use the Google Cloud Storage adapter. The slug _must_ match one of your existing collection slugs.
  * When enabled, this package will automatically set `disableLocalStorage` to `true` for each collection.
  * When deploying to Vercel, server uploads are limited with 4.5MB. Set `clientUploads` to `true` to do uploads directly on the client. You must allow CORS PUT method for the bucket to your website.


```
import { gcsStorage } from '@payloadcms/storage-gcs'
    import { Media } from './collections/Media'
    import { MediaWithPrefix } from './collections/MediaWithPrefix'
    
    
    export default buildConfig({
      collections: [Media, MediaWithPrefix],
      plugins: [
        gcsStorage({
          collections: {
            media: true,
            'media-with-prefix': {
              prefix,
            },
          },
          bucket: process.env.GCS_BUCKET,
          options: {
            apiEndpoint: process.env.GCS_ENDPOINT,
            projectId: process.env.GCS_PROJECT_ID,
          },
        }),
      ],
    })
```

### [Configuration Options](/docs/upload/storage-adapters#gcs-configuration)

Option |  Description |  Default   
---|---|---  
`enabled` |  Whether or not to enable the plugin |  `true`  
`collections` |  Collections to apply the storage to |   
`bucket` |  The name of the bucket to use |   
`options` |  Google Cloud Storage client configuration. See [Docs](https://github.com/googleapis/nodejs-storage) |   
`acl` |  Access control list for files that are uploaded |  `Private`  
`clientUploads` |  Do uploads directly on the client to bypass limits on Vercel. |   
  
## [Uploadthing Storage](/docs/upload/storage-adapters#uploadthing-storage)

[`@payloadcms/storage-uploadthing`](https://www.npmjs.com/package/@payloadcms/storage-uploadthing)

### [Installation](/docs/upload/storage-adapters#uploadthing-installation)
```
pnpm add @payloadcms/storage-uploadthing
```

### [Usage](/docs/upload/storage-adapters#uploadthing-usage)

  * Configure the `collections` object to specify which collections should use uploadthing. The slug _must_ match one of your existing collection slugs and be an `upload` type.
  * Get a token from Uploadthing and set it as `token` in the `options` object.
  * `acl` is optional and defaults to `public-read`.
  * When deploying to Vercel, server uploads are limited with 4.5MB. Set `clientUploads` to `true` to do uploads directly on the client.


```
export default buildConfig({
      collections: [Media],
      plugins: [
        uploadthingStorage({
          collections: {
            media: true,
          },
          options: {
            token: process.env.UPLOADTHING_TOKEN,
            acl: 'public-read',
          },
        }),
      ],
    })
```

### [Configuration Options](/docs/upload/storage-adapters#uploadthing-configuration)

Option |  Description |  Default   
---|---|---  
`token` |  Token from Uploadthing. Required. |   
`acl` |  Access control list for files that are uploaded |  `public-read`  
`logLevel` |  Log level for Uploadthing |  `info`  
`fetch` |  Custom fetch function |  `fetch`  
`defaultKeyType` |  Default key type for file operations |  `fileKey`  
`clientUploads` |  Do uploads directly on the client to bypass limits on Vercel. |   
  
## [R2 Storage](/docs/upload/storage-adapters#r2-storage)

**Note** : The R2 Storage Adapter is in **beta** as some aspects of it may change on any minor releases.

[`@payloadcms/storage-r2`](https://www.npmjs.com/package/@payloadcms/storage-r2)

Use this adapter to store uploads in a Cloudflare R2 bucket via the Cloudflare Workers environment. If you're trying to connect to R2 using the S3 API then you should use the S3 adapter instead.

### [Installation](/docs/upload/storage-adapters#r2-installation)
```
pnpm add @payloadcms/storage-r2
```

### [Usage](/docs/upload/storage-adapters#r2-usage)

  * Configure the `collections` object to specify which collections should use r2. The slug _must_ match one of your existing collection slugs and be an `upload` type.
  * Pass in the R2 bucket binding to the `bucket` option, this should be done in the environment where Payload is running (e.g. Cloudflare Worker).
  * You can conditionally determine whether or not to enable the plugin with the `enabled` option.


```
export default buildConfig({
      collections: [Media],
      plugins: [
        r2Storage({
          collections: {
            media: true,
          },
          bucket: cloudflare.env.R2,
        }),
      ],
    })
```

## [Custom Storage Adapters](/docs/upload/storage-adapters#custom-storage-adapters)

If you need to create a custom storage adapter, you can use the [`@payloadcms/plugin-cloud-storage`](https://www.npmjs.com/package/@payloadcms/plugin-cloud-storage) package. This package is used internally by the storage adapters mentioned above.

### [Installation](/docs/upload/storage-adapters#custom-installation)

`pnpm add @payloadcms/plugin-cloud-storage`

### [Usage](/docs/upload/storage-adapters#custom-usage)

Reference any of the existing storage adapters for guidance on how this should be structured. Create an adapter following the `GeneratedAdapter` interface. Then, pass the adapter to the `cloudStorage` plugin.
```
export interface GeneratedAdapter {
      /**
       * Additional fields to be injected into the base
       * collection and image sizes
       */
      fields?: Field[]
      /**
       * Generates the public URL for a file
       */
      generateURL?: GenerateURL
      handleDelete: HandleDelete
      handleUpload: HandleUpload
      name: string
      onInit?: () => void
      staticHandler: StaticHandler
    }
```
```
import { buildConfig } from 'payload'
    import { cloudStoragePlugin } from '@payloadcms/plugin-cloud-storage'
    
    
    export default buildConfig({
      plugins: [
        cloudStorage({
          collections: {
            'my-collection-slug': {
              adapter: theAdapterToUse, // see docs for the adapter you want to use
            },
          },
        }),
      ],
      // The rest of your config goes here
    })
```

## [Plugin options](/docs/upload/storage-adapters#plugin-options)

This plugin is configurable to work across many different Payload collections. A `*` denotes that the property is required.

Option |  Type |  Description   
---|---|---  
`alwaysInsertFields` |  `boolean` |  When enabled, fields (like the prefix field) will always be inserted into the collection schema regardless of whether the plugin is enabled. This will be enabled by default in Payload v4. Default: `false`.   
`collections` * |  `Record<string, CollectionOptions>` |  Object with keys set to the slug of collections you want to enable the plugin for, and values set to collection-specific options.   
`enabled` |  `boolean` |  To conditionally enable/disable plugin. Default: `true`.   
  
## [Collection-specific options](/docs/upload/storage-adapters#collection-specific-options)

Option |  Type |  Description   
---|---|---  
`adapter` * |  [Adapter](https://github.com/payloadcms/payload/blob/main/packages/plugin-cloud-storage/src/types.ts#L49) |  Pass in the adapter that you'd like to use for this collection. You can also set this field to `null` for local development if you'd like to bypass cloud storage in certain scenarios and use local storage.   
`disableLocalStorage` |  `boolean` |  Choose to disable local storage on this collection. Defaults to `true`.   
`disablePayloadAccessControl` |  `true` |  Set to `true` to disable Payload's Access Control. More  
`generateFileURL` |  [GenerateFileURL](https://github.com/payloadcms/payload/blob/main/packages/plugin-cloud-storage/src/types.ts#L67) |  Override the generated file URL with one that you create.   
`prefix` |  `string` |  Set to `media/images` to upload files inside `media/images` folder in the bucket.   
  
## [Payload Access Control](/docs/upload/storage-adapters#payload-access-control)

Payload ships with [Access Control](../access-control/overview) that runs _even on statically served files_. The same `read` Access Control property on your `upload`-enabled collections is used, and it allows you to restrict who can request your uploaded files.

To preserve this feature, by default, this plugin _keeps all file URLs exactly the same_. Your file URLs won't be updated to point directly to your cloud storage source, as in that case, Payload's Access control will be completely bypassed and you would need public readability on your cloud-hosted files.

Instead, all uploads will still be reached from the default `/collectionSlug/staticURL/filename` path. This plugin will "pass through" all files that are hosted on your third-party cloud service—with the added benefit of keeping your existing Access Control in place.

If this does not apply to you (your upload collection has `read: () => true` or similar) you can disable this functionality by setting `disablePayloadAccessControl` to `true`. When this setting is in place, this plugin will update your file URLs to point directly to your cloud host.

## [Conditionally Enabling/Disabling](/docs/upload/storage-adapters#conditionally-enabling-disabling)

The proper way to conditionally enable/disable this plugin is to use the `enabled` property.
```
cloudStoragePlugin({
      enabled: process.env.MY_CONDITION === 'true',
      collections: {
        'my-collection-slug': {
          adapter: theAdapterToUse, // see docs for the adapter you want to use
        },
      },
    }),
```

[Next Folders](/docs/folders/overview)

#### Related Guides

  * [How to configure file storage in Payload with Vercel Blob, R2, and UploadThing ](/posts/guides/how-to-configure-file-storage-in-payload-with-vercel-blob-r2-and-uploadthing)
  * [How to set up Payload with Supabase for your Next.js app ](/posts/guides/setting-up-payload-with-supabase-for-your-nextjs-app-a-step-by-step-guide)
