---
title: Add activity logs and admin dashboard stats
labels: enhancement, admin
---

Add logging of user/admin actions and a dashboard with basic stats.

Description
- Record user actions (logins, form submissions, mail sends, DB changes) into a `logs` table.
- Add a dashboard route to display counts (events, certificates generated, recent alerts) and recent activity entries.

Acceptance criteria
- Actions are recorded in a `logs` table with timestamps and user identifiers.
- Admin dashboard shows KPIs and recent activity.

Notes
- Useful for audits and troubleshooting.
