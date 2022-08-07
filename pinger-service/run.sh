#!/bin/sh

export DOCKER_CONTAINER="${DOCKER_CONTAINER:=No}"
export INTERNAL_PORT="${INTERNAL_PORT:=8000}"
export WORKERS="${WORKERS:=2}"

echo "---------------------------------"
echo "Using environment:"
echo "    DOCKER_CONTAINER: $DOCKER_CONTAINER"
echo "    INTERNAL_PORT:    $INTERNAL_PORT"
echo "    WORKERS:          $WORKERS"
echo "---------------------------------"

uvicorn \
    service.main:app \
    --host 0.0.0.0 \
    --port $INTERNAL_PORT \
    --workers=$WORKERS
