---
title: Add form generator with DB-backed registrations
labels: enhancement, backend
---

Add a form generator that creates event-specific registration tables and stores responses.

Description
- Implement an admin UI to define event forms (fields, types, team/individual), create a new DB table for responses (separate `forms` DB bind recommended).
- Provide public registration pages that write into the event table and an admin view to list/download CSVs of responses.

Acceptance criteria
- Admin can create/delete event forms with configurable fields.
- Public registration pages save responses to a `forms` database.
- Admin can export responses as CSV.

Notes
- Reference REMS `forms` blueprint and `FormGeneratorSchema` for validation patterns.
