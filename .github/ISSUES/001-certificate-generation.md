---
title: Add certificate generation & serving
labels: enhancement, backend
---

Implement CSV-driven certificate generation and serving.

Description
- Add a `certificates` module that accepts a CSV upload and a certificate template.
- Use Pillow to render text onto templates and save generated certificate images under `src/static/certificates/`.
- Add a route to serve generated certificates and an admin UI to manage generation jobs.

Acceptance criteria
- Upload CSV + template produces per-row certificate images.
- Generated certificates are stored in `src/static/certificates/<event>/` and can be downloaded.
- Unit tests for template rendering and CSV parsing.

Notes
- See REMS `certificates` blueprint for reference implementation.
