#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../src"

python3 server.py&
LASTPID=$!
python3 test.py
kill $LASTPID
