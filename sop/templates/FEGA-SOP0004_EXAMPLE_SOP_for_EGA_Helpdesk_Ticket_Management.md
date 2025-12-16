# FEGA SOP — SOP for EGA Helpdesk Ticket Management (CONCISE TEMPLATE)

| Metadata         | Value                   |
| ---------------- | ----------------------- |
| Template ID      | `FEGA-SOP0004`          |
| Template version | `v1.0`                  |
| Topic            | Internal Node Processes |
| SOP type         | SOP                     |
| Node             | {{Node}}                |
| Instance version | `{{InstanceVersion}}`   |

## Document History

| Template version | Instance version      | Author(s)                               | Description of changes | Date           |
| ---------------- | --------------------- | --------------------------------------- | ---------------------- | -------------- |
| `v1.0`           | `—`                   | Giselle Kerry - Senior Helpdesk Officer | Initial release        | 30-09-2019     |
| `v1.0`           | `{{InstanceVersion}}` | {{AuthorList}}                          | {{ChangeSummary}}      | {{DD-MM-YYYY}} |

## Purpose

Standardize handling of RT tickets for {{Node}} to ensure no user messages are missed and SLAs are met.

## Scope

Applies to all Helpdesk staff managing tickets in RT for {{Node}}. Read together with SOP `FEGA-SOP0003` (Ticket Assignment) and any Security/Incident SOP used by the node.

## Service Levels

Working hours: {{WorkingHours}} (Europe/Lisbon unless stated).
First response: within {{SLA_FirstResponse}} working hours from last user message.
Update cadence (open tickets): at least every {{SLA_UpdateCadence}} working hours.
No-reply closure: close after {{SLA_NoReplyCloseDays}} days since last user reply (after final reminder).

## Standard Status + Tags

Status (minimum): New, Open, Waiting on user, Waiting on dev, Resolved, Reopened.
Tags (minimum): `awaiting-user`, `awaiting-dev`, `long-running`, `holiday-priority`, `incident-suspected`, `large-submission`, `duplicate`, `spam`.

## Procedure

### 1) Triage (new/unowned)

1. Read last user message; classify Type and Priority (P1–P4).
2. Set Owner (per assignment SOP). No ticket remains unowned beyond triage.
3. If sensitive data (passwords/tokens) is present: do not quote it; instruct user to rotate/remove; proceed via approved secure channel.
4. Send first response (meaningful acknowledgement + next step + what info is needed).

### 2) Work (owned tickets)

1. Document actions/decisions in internal notes (what checked + outcome + next step).
2. Keep ticket status accurate:

   * Waiting on user → ask specific questions; tag `awaiting-user`
   * Waiting on dev → create/link JIRA; tag `awaiting-dev`
3. While open, update user at least every {{SLA_UpdateCadence}} working hours (even “no change”, with next date).

### 3) Cross-referencing development (JIRA)

If engineering work is required:

1. Create/link JIRA ID in RT (field or internal note).
2. State user-facing expectation (what is being done + update cadence).
3. Keep RT as the user communication channel; JIRA is internal tracking.

### 4) Escalation

Escalate immediately to Helpdesk Lead (and Security if applicable) when:

* P1/incident suspicion (`incident-suspected`)
* potential data exposure, suspicious access, or widespread outage
* deadlines/impact cannot be met without intervention
  Record escalation reason + evidence in internal notes.

### 5) Leave / coverage

If away ≥ 1 week:

1. Stop taking new tickets the week before where possible.
2. Before leave: add a final internal note to each open ticket (status + next step + links) and tag `holiday-priority`.

### 6) Resolution and closure

Resolve when fixed/answered, with a user message including verification steps.
No-reply closure:

1. Send final reminder warning closure.
2. Close after {{SLA_NoReplyCloseDays}} days since last user reply, with reopen instructions.

## Minimal message templates

First response: “We received your request about {{issue}}. Next we will {{action}}. Please provide {{minimal info}}. We will respond within {{SLA_FirstResponse}} working hours and update at least every {{SLA_UpdateCadence}} working hours while open.”

Waiting on dev: “This is tracked as {{JIRA_ID}}. Current blocker: {{blocker}}. Next update by {{date}} (or within {{SLA_UpdateCadence}} working hours).”

Final reminder: “If we do not hear back within {{X}} days, we will close this ticket. Reply to reopen.”
