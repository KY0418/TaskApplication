#!/bin/bash

UpOrBuild="$1"

set -e

if [ "$UpOrBuild" = "up" ]; then
  docker compose up
elif [ "$UpOrBuild" = "build" ]; then
  docker compose build
elif [ "$UpOrBuild" = "build --no-cache" ]; then
  docker compose build --no-cache
fi

