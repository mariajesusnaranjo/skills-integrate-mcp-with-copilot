---
title: Add SQLAlchemy models and Pydantic schemas
labels: refactor, backend
---

Migrate in-memory structures to SQLAlchemy models and add Pydantic schemas for validation.

Description
- Introduce `models.py` with SQLAlchemy models for activities, users, certificates, logs, events.
- Add `schemas.py` with Pydantic models for request validation (signup, CSV rows, forms metadata).

Acceptance criteria
- Data persisted in a configured SQL database (SQLite/MySQL/Postgres supported).
- Endpoints validate input using Pydantic and use models for DB operations.

Notes
- Enables migrations (Alembic) and more robust data handling.
