#! /bin/sh
set -e
if [ -f ./.env ]
then
  export $(cat ./.env | xargs)
fi
printenv
echo "env variables imported"

image_name="${IMAGE_NAME:-"el-flask-kustomize-test"}"
tag_name="${TAG_NAME:-"gunicorn"}"
use_tag="$image_name:${tag_name}-0.1"

DOCKERFILE="${DOCKERFILE_NAME}"
docker build -t "$use_tag" --file "./${DOCKERFILE}" .
if [[ -z "${ARTIFACT_REGISTRY_IMAGE}" ]]; then
  v="eu.gcr.io/${PROJECT_ID}/flask_test/${use_tag%:*}"
else
  v="${ARTIFACT_REGISTRY_IMAGE}"
fi
docker tag "${use_tag}" "${v}"
docker push "${v}"