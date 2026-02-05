---
title: Add bulk mailer and mailing-list management
labels: enhancement, backend, infra
---

Add mailing-list creation from CSVs and a bulk mail sender with HTML templates.

Description
- Allow admins to upload a CSV of (name,email) to create mailing lists (stored in a `mail` DB bind).
- Provide a bulk-mail UI to compose HTML emails (subject, body, button/link, images) and send them to selected lists.

Acceptance criteria
- CSV upload creates or updates a mailing list table.
- Bulk mail UI can send templated emails (preview before send).
- Logging of sent batches and basic retry/error reporting.

Notes
- Integrate with existing email helpers or configure an SMTP/provider in settings.
