---
title: Add authentication & admin roles
labels: enhancement, security
---

Introduce user accounts, authentication and admin role checks.

Description
- Add login/logout, password reset, user profiles, and an `is_admin` check for protected routes.
- Store users in a persistent DB (hashed passwords) and add a profile picture upload endpoint.

Acceptance criteria
- Users can register/login (or admin-created accounts) and admin-only pages are inaccessible to non-admins.
- Password reset flow (email token) implemented.

Notes
- Follow security best practices (bcrypt/argon2, CSRF, session management).
