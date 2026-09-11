# CampusGuard — Team Project Brief

> Course: **Software Engineering I** — 16 weeks / 32 hours / 2 credits
> Teams: **5 teams of 5–6** | Runs: **Week 4 → Week 16**
> License: **CC BY 4.0** — original case, free to reuse and adapt (including commercially) with attribution.

---

## Why this case is original

Many SE courses build their project around *SafeHome*, the home-security case from
Pressman & Maxim. That is someone else's intellectual property, and publishing it under
your own open licence is not coherent. **CampusGuard** is an original case,
structurally isomorphic to SafeHome but set in a domain students already inhabit:
getting through the door of their own dormitory.

## Background

The university runs electronic door locks across dormitories, laboratories and the
library, but they are independent systems with no unified control, and the security
centre can only review footage after the fact. The university wants one platform
covering **access control, anomaly detection, tiered alerting, and device maintenance**.

## Stakeholders

| Role | Concerns |
|---|---|
| Student | Smooth access, visitor passes, fault reporting |
| Dorm Manager | Building roster, late-return approval |
| Security Officer | Real-time alerts, dispatch |
| Maintenance Staff | Work-order intake and resolution |
| Administrator | Zones, devices, roles, permissions |
| Security Office (external) | Monthly statistics |
| Campus Clinic / Counselor (external) | Escalation for critical events |

## Functional requirements (20)

| ID | Requirement |
|---|---|
| FR-01 | Students enter authorised zones (dormitory, lab, library) with a campus card or phone pass |
| FR-02 | Authorisation depends on identity **and** time window (e.g. labs 08:00–22:00) |
| FR-03 | Readers detect **tailgating** (one tap, several people) and log an event |
| FR-04 | Unauthorised attempts are logged but **do not** auto-lock the door |
| FR-05 | Three consecutive failures at one reader raise a low-severity alert |
| FR-06 | A smoke detector trigger **releases** the electric locks in the affected zone |
| FR-07 | The security wall display shows a live alert list sorted by severity |
| FR-08 | Alerts carry three severities: **Info / Warning / Critical** |
| FR-09 | Officers can **Acknowledge**, **Dispatch** and **Resolve** an alert |
| FR-10 | An alert can be marked **False Alarm** and counts toward a device's false-alarm rate |
| FR-11 | Students can book a **visitor pass** (validity window + permitted zones) |
| FR-12 | Visitor passes expire automatically |
| FR-13 | Dorm managers can extend a student's access window (e.g. late return) |
| FR-14 | Students can report a faulty device; the system creates a work order |
| FR-15 | Maintenance staff accept, update and close work orders |
| FR-16 | The system supports **modes**: term / holiday / night / exam week, each with different rules |
| FR-17 | Controllers cache the authorisation list offline and sync events on reconnection |
| FR-18 | Administrators manage zones, devices, roles and permission groups |
| FR-19 | The student app shows the holder's last 30 days of access events |
| FR-20 | The system produces monthly access and alert statistics for the Security Office |

## Non-functional requirements (8)

| ID | Requirement |
|---|---|
| NFR-01 | Card tap to door release ≤ 1 second |
| NFR-02 | Device trigger to security-centre display ≤ 5 seconds |
| NFR-03 | Controllers operate offline for ≥ 72 hours |
| NFR-04 | Access logs retained ≥ 1 year; alert logs ≥ 3 years |
| NFR-05 | Student app supports Chinese and English |
| NFR-06 | Availability ≥ 99.5% during term |
| NFR-07 | Access data must not be used for purposes other than teaching and attendance |
| NFR-08 | Every permission change is written to an audit log |

## Deliberate ambiguities

The brief above is **intentionally incomplete** — that is the point. Real clients hand
you this much on the first call. Students are expected to interrogate it during
elicitation (Weeks 4–5):

1. Required accuracy and tolerated false-alarm rate for tailgating detection
2. The rules of **exam-week mode** are not stated at all
3. Whether visitor passes require real-name identity documents
4. The boundary of "purposes other than teaching and attendance" in NFR-07
5. How the system integrates with the existing campus card system
6. The maximum number of alerts shown simultaneously on the wall display
7. How "the affected zone" in FR-06 is defined — same floor? same building?

## Five core scenarios

| # | Scenario | Used for |
|---|---|---|
| S1 | Student taps into a dormitory (happy path) | Basic flow, sequence diagram |
| S2 | Tailgating: one tap, two people through | Exception flow, state machine, severity |
| S3 | Smoke trigger → locks release → clinic notified | Event-driven flow, external systems |
| S4 | Visitor pass booked → approved → used → expires | Lifecycle state machine, approval flow |
| S5 | Network loss → offline operation → event sync | Offline strategy, deployment view |

## Weekly mapping

| Week | Topic | CampusGuard task |
|:---:|---|---|
| W04 | Kickoff | Teams, repo, board, roles; first client interview |
| W05 | Elicitation | **Milestone review 1**: SRS v1 + client sign-off |
| W06 | Business process | Visitor-pass approval; alert handling |
| W07 | Use cases | Use-case diagram for the five roles |
| W08 | Use-case specs | Core specs + **client change request → impact analysis** |
| W09 | Domain model | `Person / Student / Zone / Device / AccessEvent / Alert / VisitorPass / WorkOrder` |
| W10 | Domain model | **Milestone review 2**: domain class diagram + glossary |
| W11 | Behaviour | Alert state machine: New → Ack → Dispatched → Resolved / False Alarm |
| W12 | Behaviour | Sequence diagrams for S1–S5 |
| W13 | Class model | Analysis → design classes; GRASP responsibility assignment |
| W14 | Class model | Design class diagram + Java skeleton |
| W15 | UI design | Two low-fidelity prototypes: student app (minimal) vs security wall display (dense) |
| W16 | Architecture + defence | Layered / deployment views + final pitch |

## Instructor note: three constraints the client withholds

Used with the "the client did not tell you everything" exercise in Week 4 — the client
stays silent about these until the second interview:

1. The system must integrate with the **existing campus card system, which exposes a
   read-only API** — no writes, no push, polling only.
2. For privacy compliance, access events **may not keep precise timestamps beyond 90
   days**; they must degrade to "date + time band". (This directly contradicts NFR-04 —
   good conflict-analysis material.)
3. **No new hardware budget.** Existing controllers must be reused, and their firmware
   does not support custom scripts. (This constrains the architecture and makes FR-17
   decisive.)

## Attribution

```
CampusGuard case study by Ren Zheng — Software Engineering I course project.
Licensed under CC BY 4.0. https://github.com/klausren/software-engineering-course
```
