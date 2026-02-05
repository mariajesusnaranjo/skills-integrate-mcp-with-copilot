---
title: Add Jinja2 admin templates (SB Admin 2)
labels: enhancement, frontend
---

Replace or augment the static UI with server-rendered Jinja2 admin templates for richer admin pages.

Description
- Add `templates/` using SB Admin 2 theme (navigation, dashboard, cards) and move admin pages to server-rendered templates.
- Provide partials for navigation/footer and reuse across pages.

Acceptance criteria
- Admin pages are rendered with Jinja2 and share a consistent theme.
- Navigation partials and footer exist and are included.

Notes
- Keep the existing static front-end for the public-facing signup page if desired.
