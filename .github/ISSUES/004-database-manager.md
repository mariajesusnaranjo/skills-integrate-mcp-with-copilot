---
title: Add admin database manager (browse/insert/update/delete)
labels: enhancement, admin
---

Provide an admin interface to browse and modify database tables across binds.

Description
- Implement a DB management UI restricted to admin users to list tables, view rows, insert/update/delete rows, and paginate results.
- Support multiple DB binds (main/forms/mail) via configuration.

Acceptance criteria
- Admin can select DB bind and table, view paginated rows, and perform insert/update/delete operations.
- Actions are audited in activity logs.

Notes
- Be careful with SQL injection — sanitize identifiers and restrict to admin-only access.
