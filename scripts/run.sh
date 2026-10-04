#!usr/bin/env bash
set -euo pipefall
cd "$(dirname "$0")/.."
exec python3 src/server.py