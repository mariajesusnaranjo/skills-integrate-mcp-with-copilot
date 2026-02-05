---
title: Add Docker setup and Alembic migrations
labels: infra, enhancement
---

Provide Docker development setup and database migrations.

Description
- Add `Dockerfile` and `docker-compose.yml` for local development.
- Install and configure Alembic for DB migrations and include an `app-entrypoint` script to run migrations on startup.

Acceptance criteria
- `docker-compose up` boots the app and runs migrations.
- Alembic is configured and initial revision created.

Notes
- Useful for reproducible development and deployment.
