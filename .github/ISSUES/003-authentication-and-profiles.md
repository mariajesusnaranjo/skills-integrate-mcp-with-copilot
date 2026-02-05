---
title: Add authentication and user profiles
labels: enhancement, backend, auth, frontend
---

Implement user accounts and role-based access for students, admins, and staff.

Description
- Add user model with email, name, role (student/admin), and profile details.
- Implement authentication (JWT or session-based) and password handling.
- Protect admin endpoints (e.g., certificate generation, creating/editing activities).
- Provide endpoints for users to view their signups and activity history.

Acceptance criteria
- Users can register/login and have sessions or JWTs.
- Admin-only endpoints return 403 for non-admin users.
- Tests for auth flows and role enforcement.

Notes
- Consider using `fastapi-users` or a lightweight custom solution depending on scope.
