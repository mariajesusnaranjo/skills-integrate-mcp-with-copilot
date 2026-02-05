---
title: Integrate link shortener (short.io)
labels: enhancement, integration
---

Add a route/UI to shorten URLs using an external provider (e.g., Short.io) and optionally store mappings.

Description
- Admin-facing form to generate short links with custom slug or auto-generated slug using Short.io API.
- Optionally store mapping in DB and provide analytics/click tracking.

Acceptance criteria
- Admin can create a short URL via the UI and receive a short link.
- Optionally view a list of created short links and basic click counts.

Notes
- Requires provider API key in configuration/env.
