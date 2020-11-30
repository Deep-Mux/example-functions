# imagenet-classifier-pytorch

imagenet-classifier-pytorch is a ResNet18-based classifier for ImageNet dataset.

Function takes image data as input and returns the label for the top predicted class.

## Deploying

Run `deepmux upload` to upload function to the server.

Once the function finished processing you can test by calling it via HTTP API.

> Visit https://app.deepmux.com/api_key to get your API token.

```sh
curl -X POST \
     -H "X-Token: <YOUR API TOKEN>" \
     https://api.deepmux.com/v1/function/imagenet-classifier-pytorch/run \
     --data-binary "@data/balloon.jpg"
```
