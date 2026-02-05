---
title: Add image and font assets for certificate templates
labels: enhancement, assets
---

Include template images and fonts used for server-side certificate generation.

Description
- Add a `members/` (or `assets/`) folder with sample certificate templates and Raleway fonts.
- Ensure code loads fonts from configurable paths and includes sample CSV headers file.

Acceptance criteria
- Certificate generator finds required template and font files at runtime.
- README documents where to place custom templates and fonts.

Notes
- Store large binary assets in LFS or provide download instructions if repo size is a concern.
