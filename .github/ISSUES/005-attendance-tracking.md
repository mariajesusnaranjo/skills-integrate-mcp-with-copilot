---
title: Add attendance tracking & mobile check-in
labels: enhancement, mobile, backend
---

Track attendance for activities and support mobile check-ins.

Description
- Add attendance records tied to `Activity`, `Student`, and `date`.
- Provide endpoints for marking attendance and for mobile clients to check in.
- Consider QR-code based check-in for events.

Acceptance criteria
- Attendance records are stored and retrievable by date/activity.
- Mobile or web check-in endpoint exists with basic validation.
- Tests for attendance recording.

Notes
- Requires DB and auth work to ensure student identity for check-ins.
