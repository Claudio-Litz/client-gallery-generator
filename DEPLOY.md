
Deployment checklist

Files a tester or contributor will need after cloning

- A `.env` file created from `.env.template` with at least:
  - `DJANGO_SECRET_KEY` (set a strong secret)
  - `DJANGO_DEBUG=False` (for realistic behavior)
  - `DJANGO_ALLOWED_HOSTS` (e.g. `localhost,127.0.0.1` for local tests)
- Optional: Backblaze B2 credentials only if you want remote media testing:
  - `B2_KEY_ID`, `B2_APP_KEY`, `B2_BUCKET_NAME`, `B2_ENDPOINT_URL`
- Do NOT add or commit:
  - `.env` (keep private)
  - `Gallery/db.sqlite3` (local DB dumps)
  - `/media/` directory contents if they contain private images

Stop tracking the local sqlite (recommended before publishing)

```bash
git rm --cached Gallery/db.sqlite3
git commit -m "Remove tracked sqlite from repo"
```

Quick local test workflow (without Docker)

```bash
cp .env.template .env
# edit .env and set DJANGO_SECRET_KEY and DJANGO_ALLOWED_HOSTS
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python Gallery/manage.py migrate
python Gallery/manage.py createsuperuser   # optional
python Gallery/manage.py runserver
```

Quick local test workflow (with Docker Compose)

```bash
cp .env.template .env
# edit .env to set DJANGO_SECRET_KEY and DJANGO_ALLOWED_HOSTS
docker compose up --build
```

Notes for testers

- If `DJANGO_DEBUG=True` in the `.env` used for local testing, the site will run in development mode with local media storage.
- If you want to simulate production behavior, set `DJANGO_DEBUG=False` and provide `B2_*` keys or attach a storage backend; otherwise media uploads will still use local storage when running locally.

Security notes

- Do not commit `.env` or any secrets to the repository.
- Use a managed database (Postgres) for production; sqlite is for quick local tests only.
- Rotate any credentials accidentally committed and scrub history if necessary.

