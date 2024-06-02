#!/bin/sh

readonly image_tag="$1"
readonly image_repository="$2"

buildDir="detection"

docker build \
  --no-cache \
  --progress=plain \
  --tag "$image_repository":"$image_tag" \
  --file "Dockerfile" \
  "./$buildDir"

docker push "$image_repository":"$image_tag"
