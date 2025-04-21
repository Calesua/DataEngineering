#!/usr/bin/env bash
# wait-for-it.sh (reduced)
# This script waits for a service to be available before executing a command.
# Usage: wait-for-it.sh <host> <port> -- <command>

host="$1"
shift
port="$1"
shift

until nc -z "$host" "$port"; do
  echo "Esperando a $host:$port..."
  sleep 1
done

exec "$@"
