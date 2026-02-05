# REMS feature import — Issue Summary

This folder contains ready-to-open issue markdown files for adding REMS-like features to this repository.

Files added:
- `001-certificate-generation.md` — CSV-driven certificate generation and serving.
- `002-form-generator-db-backed.md` — Admin form generator and DB-backed registrations.
- `003-bulk-mailer.md` — Mailing-list creation and bulk HTML mail sending.
- `004-database-manager.md` — Admin DB manager for browsing and editing tables.
- `005-link-shortener.md` — Short URL creation via Short.io.
- `006-auth-and-roles.md` — User accounts, auth, and admin roles.
- `007-activity-logs-dashboard.md` — Activity logging and dashboard KPIs.
- `008-sqlalchemy-and-pydantic.md` — Move in-memory data to SQLAlchemy + validation.
- `009-image-font-assets.md` — Add certificate template and font assets.
- `010-docker-alembic.md` — Dockerfile, docker-compose, and Alembic migrations.
- `011-jinja2-admin-templates.md` — Server-rendered admin pages using SB Admin 2.

How to open these as real GitHub issues
1. Using GitHub CLI (recommended):

```bash
gh issue create --title "$(head -n1 .github/ISSUES/001-certificate-generation.md | sed 's/^title: //')" --body "$(sed -n '3,$p' .github/ISSUES/001-certificate-generation.md)" --label enhancement,backend
```

Repeat for each file (or script the creation). If you want, I can open them on your behalf — I need GitHub API access (a token) or repository write permissions. Reply to let me know.
