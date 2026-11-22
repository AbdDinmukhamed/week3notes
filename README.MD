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

## Rollback

Argo CD deploys what is on the `main` branch, from the `k8s` folder.
To roll back, undo the commit that deployed the bad version, with a new commit:

    git log --oneline -- k8s/deployment.yaml
    git revert <commit>
    git push

Argo CD deploys the previous version within three minutes. Do not use
`kubectl rollout undo`: self-heal would put the bad version back.
