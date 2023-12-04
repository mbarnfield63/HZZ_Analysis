#!/bin/bash
set -e

host="$1"
port="$2"
shift 2
cmd="$@"

until nc -z -w 1 "$host" "$port"; do
  echo "Waiting for RabbitMQ to be ready..."
  sleep 1
done

echo "RabbitMQ is ready! Starting the application..."
exec $cmd
