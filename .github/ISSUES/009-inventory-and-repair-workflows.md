---
title: Inventory / repair workflows for hardware clubs
labels: enhancement, domain-specific
---

Support inventory tracking and repair workflows for tech/repair clubs (inspired by BinaryHeart).

Description
- Add models for `Item`, `RepairRequest`, and inventory counts.
- Add endpoints and simple UI for logging donations, repairs, and re-donations.
- Track ownership and status changes across workflow stages.

Acceptance criteria
- Inventory items can be created/updated and have status lifecycle.
- Repair requests can be logged and tracked.
- Admin UI for managing inventory is available.

Notes
- Optional domain-specific feature; implement only if relevant to school clubs.
