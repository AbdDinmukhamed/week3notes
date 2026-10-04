# week3notes

## What it does

A small HTTP service on Python. It serves a hardcoded list of notes.
- `GET /` returns service info
- `GET /healthz` checks health, returns `ok`
- `GET /notes` returns number of notes 

## How to run it
```bash
./scripts/run.sh
```

## How to test it
```bash
./scripts/test.sh
```

## Which port it listens on
The service listens on the port `$PORT`. Default port is `8080`.
