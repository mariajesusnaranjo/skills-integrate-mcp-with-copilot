---
title: Add persistent storage / database
labels: enhancement, backend, database
---

Add a persistent database backend so activities and student records survive restarts.

Description
- Replace in-memory `activities` with a database-backed model (e.g. SQLite for local/dev, Postgres for production).
- Add models for `Activity`, `Student`, `Signup`, and optionally `Attendance`.
- Add simple migration strategy (Alembic or a lightweight migration script).

Acceptance criteria
- Activities and signups persist across server restarts.
- Migration steps are documented in `README.md`.
- Unit tests cover model CRUD operations.

Notes
- Keep the current FastAPI endpoints but adapt them to use the DB models.
