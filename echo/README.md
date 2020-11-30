# Echo

Echo is the simplest possible function, it returns it's input as output unchanged.

## Deploying

Run `deepmux upload` to upload function to the server.

Once the function finished processing you can test by calling it via HTTP API.

> Visit https://app.deepmux.com/api_key to get your API token.

```sh
curl -X POST \
     -H "X-Token: <YOUR API TOKEN>" \
     https://api.deepmux.com/v1/function/echo/run \
     --data "Hello!"
```
