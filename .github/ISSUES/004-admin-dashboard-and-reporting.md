---
title: Add admin dashboard & reporting
labels: enhancement, frontend, backend
---

Provide an admin UI to manage activities, view signups, and export reports.

Description
- Create an admin web UI (could be a simple SPA under `/static/admin/`) to list activities, see participants, and kick off certificate generation.
- Add API endpoints for exporting reports (CSV/PDF) and basic metrics (counts per activity, waitlists).

Acceptance criteria
- Admin UI accessible to admin users only.
- Reports can be generated and downloaded.
- Basic metrics endpoint returns activity counts.

Notes
- This pairs with DB and auth work; start after those are in place.
