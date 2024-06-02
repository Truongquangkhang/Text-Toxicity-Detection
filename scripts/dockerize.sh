#!/bin/sh

readonly image_tag="$1"
readonly image_repository="$2"

ls detection/vinai-phoBERT

docker build \
  --no-cache \
  --progress=plain \
  --tag "$image_repository":"$image_tag" \
  --file "Dockerfile" \
  "."

docker push "$image_repository":"$image_tag"
