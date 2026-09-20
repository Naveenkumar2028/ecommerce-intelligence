# Local Development Guide

This guide gives a repeatable workflow for running the ecommerce intelligence dashboard locally.

## 1. Prepare the environment

1. Clone the repository and move into the project directory.
2. Copy `.env.example` to `.env`.
3. Fill in only the provider and database values required by your local setup.
4. Keep secrets out of Git; `.env` should remain ignored.

## 2. Start the backend

Run the backend using the command documented in the repository README. Confirm that the health endpoint responds before opening the frontend.

```bash
curl -i http://localhost:8000/health
```

A successful response confirms that the API process is reachable. If it fails, check the terminal logs, port usage, and environment variables before debugging the UI.

## 3. Verify representative API routes

Use the API docs or the smoke test to verify a small set of routes:

```bash
curl -i http://localhost:8000/api/overview
curl -i http://localhost:8000/api/orders
```

When testing filtered orders, include a category value that exists in the loaded dataset and confirm that the response contains only matching records.

## 4. Start the frontend

Install the frontend dependencies, start the development server, and open the local URL printed by the toolchain. If the page loads but shows no data:

- confirm the frontend API base URL points to the backend;
- verify the backend is running on the expected port;
- inspect browser network errors for CORS or 404 responses;
- reload after changing environment variables.

## 5. Before sharing a demo

- Run `scripts/smoke_test.sh` against the local backend.
- Open the dashboard and verify the overview cards, charts, and order filters.
- Check that no secret values appear in logs or screenshots.
- Record any dataset or environment assumptions in the demo notes.

For deeper issue diagnosis, continue with `docs/data-quality-checklist.md` and the troubleshooting notes in the repository documentation.
