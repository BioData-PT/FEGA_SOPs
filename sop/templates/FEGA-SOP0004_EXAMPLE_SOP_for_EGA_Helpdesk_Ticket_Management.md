# FEGA SOP — SOP for EGA Helpdesk Ticket Management

| Metadata         | Value                   |
| ---------------- | ----------------------- |
| Template ID      | `FEGA-SOP0004`          |
| Template version | `v1.1`                  |
| Topic            | Internal Node Processes |
| SOP type         | SOP                     |
| Node             | `-`                |
| Instance version | `-`   |

## Document History

| Template version | Instance version      | Author(s)                               | Description of changes | Date           |
| ---------------- | --------------------- | --------------------------------------- | ---------------------- | -------------- |
| `v1.0`           | `—`                   | Giselle Kerry - Senior Helpdesk Officer | Initial release        | 30-09-2019     |
| `v1.1`           | `-` | Jorge Oliveira, Jorge Silva, Miguel Cisneiros | Update template | 16-12-2025 |

## Purpose

This SOP defines the standardized workflow for managing Helpdesk tickets in Request Tracker (RT) for {{Node}}. It ensures consistent handling, clear ownership, timely communication, complete internal traceability, and compliance with applicable security and privacy requirements. The service objective is to provide a **first response** within the time estabilished in the Service Level Agreement of each node.

## Scope

This SOP applies to all Helpdesk staff handling tickets in RT for {{Node}}, across all queues under {{Queue}}. It covers ticket intake, triage, assignment, investigation, escalation, user communication, documentation, and closure.

## Definitions

**First response:** First meaningful Helpdesk reply addressing the user’s request (not an auto-ack).
**Update:** A user-visible message with progress, next action, and expected timeline.
**Internal note:** RT comment visible to staff only; must capture decisions, evidence, and cross-references.
**PII / sensitive data:** Any personal data, credentials, access tokens, or dataset-level sensitive attributes.

## Tools and Systems

* RT (Request Tracker): ticket management and audit trail
* Knowledge base / SOP repository: approved procedures and answers
* Approved communication channels: RT only for official user communication unless otherwise stated

## Ticket Taxonomy

### Required fields (must be set during triage)

* **Type:** {Access / Submission / Download / Metadata / Account / Policy / Incident / Other}
* **Priority:** {P1 / P2 / P3 / P4} (see matrix below)
* **Status:** {New / Open / Waiting on user / Waiting on dev / Waiting on third party / Resolved / Reopened}
* **Owner:** named individual (no unowned tickets beyond triage window)

### Priority matrix (rules)

* **P1 (Critical):** security incident suspicion; service-wide outage; deadline within 24h; data integrity risk
* **P2 (High):** blocking a submission/access; repeated failures; deadline within 3 working days
* **P3 (Normal):** standard requests; minor issues; non-blocking questions
* **P4 (Low):** informational requests; long-term planning; cosmetic issues

### Tags (standard)

Use consistent tags to enable reporting and coverage:

* `awaiting-user`, `awaiting-dev`, `holiday-priority`, `long-running`, `large-submission`, `access-request`, `incident-suspected`, `policy-question`, `duplicate`, `spam`

## RT Setup (minimum configuration)

Each Helpdesk Officer must configure RT to surface actionable work immediately:

1. **Home dashboard widgets** must include:

   * “Tickets owned by me in status Open”
   * “Tickets owned by me awaiting reply” (Waiting on user vs waiting on Helpdesk must be clearly distinguished)
   * “Unowned new tickets” (triage queue)
     
2. Create a saved search named: **`My — Needs Action`** with these rules:

   * Owner = me
   * Status IN (New, Open)
   * Exclude status “Waiting on user” unless user replied since last Helpdesk message
     
3. Enable notifications for:

   * User replies on owned tickets
   * @mentions / watchers
     
4. Verify at start of each week that the dashboard still reflects SLA-critical tickets.

## Procedure

### 1) Intake and Triage 

1. Open new/unowned tickets view.
2. Read the user’s last message and identify:

   * Request type and scope
   * Sensitive content (PII, credentials, access tokens)
   * Urgency (deadlines; blocked submissions)
3. If the ticket contains sensitive credentials:

   * Immediately add an internal note: “Sensitive data detected”
   * Ask user to remove/rotate credentials and re-send via approved method (do not quote credentials back)
4. Set required fields: Type, Priority, Status, Tags.
5. Assign an Owner (yourself or per assignment SOP).
6. Send **first response** (see templates) unless the ticket is clearly spam/duplicate.

**Triage output should include** an internal note with:

* Summary of issue in 1–3 lines
* What you will do next
* Any cross-references (prior tickets, datasets, accounts)

### 2) First Response Standard 

A compliant first response should include:

* Acknowledgement of the exact issue (paraphrase)
* What information is missing (if any) and why it’s needed
* The next step and expected timeline
* Any immediate workaround (if safe)
* If escalation needed: say so and provide update cadence

### 3) Investigation and Work (Open tickets)

1. Reproduce/verify the issue using available logs/tools (do not request unnecessary data).
2. Record findings as internal notes:

   * What was checked
   * Evidence (error codes, timestamps, environment)
   * Conclusion and next action
3. If the issue requires engineering work:

   * Set status to “Waiting on dev” and tag `awaiting-dev`

### 4) Requesting Information from the User (Waiting on user)

Only request what is necessary. Prefer structured requests.

1. Ask for missing details using a checklist format.
2. Set status to “Waiting on user” and tag `awaiting-user`.
3. If user does not respond:

   * Send Reminder 1 after {{X}} days
   * Send Reminder 2 (final) after {{X}} days
   * Close after {{X}} days (see “No Reply Closure”)

### 5) Escalation Rules

Escalate immediately to Helpdesk Lead (and Security Officer where relevant) if:

* P1 criteria met
* Repeated user reports indicate broader impact
* Potential data exposure or suspicious access
* Legal/policy concerns (consent, authorization, GDPR-related queries)
  Escalation must include:
* A short incident-style summary
* Impact assessment (who/what is affected)
* Evidence collected
* Recommended next action

### 6) Duplicates, Spam, and Misrouted Tickets

**Duplicate:** Link to the canonical ticket; note why; resolve duplicate with a user message pointing to the main ticket. Tag `duplicate`.
**Spam:** Do not engage beyond minimal closure. Tag `spam`, resolve/close per policy.
**Misrouted:** Re-queue or transfer per assignment SOP; inform the user.

### 7) Leave / Coverage Management

If you will be unavailable for ≥ 1 week:

1. Two working days before leave, stop taking new tickets unless directed by Lead.
2. For each open ticket you own:

   * Add a final internal note with current status, next action, and relevant links
   * Ensure tags are correct
3. The day before leave:

   * Tag remaining open tickets with `holiday-priority`
   * Notify Lead of high-risk tickets (P1/P2) and any deadlines

### 8) Resolution and Closure

A ticket may be resolved when:

* The user confirms the issue is fixed, OR
* The Helpdesk provides a complete answer and no further action is required, OR
* “No reply closure” conditions are met

Before resolving, send a final user-facing message summarizing:

   * What was done
   * Outcome

### 9) No Reply Closure (mandatory steps)

1. Send a final reminder (“We will close in X days if no response”).
2. After {{X}} days since last user reply:

   * Resolve the ticket with a closure note
   * Include how to reopen or submit a new ticket
3. Never close P1/P2 tickets without Lead approval unless explicitly permitted by policy.

## Communication Templates (copy/paste)

### A) First response (general)

Subject: Re: {{TicketSubject}}
Message:
“Thanks for your message. To confirm, you are experiencing {{short paraphrase}}.
Next, I will {{next action}}. If you can share the following details, I can proceed faster: {{minimal checklist}}.
We aim to respond within {{X}} working hours and will update you at least every {{X}} working hours while this is in progress.”

### B) Waiting on dev update

“Quick update: this is now tracked internally as {{ISSUE_ID}}. At the moment we are waiting for {{blocking item}}. I will update you again by {{date}} (or within {{X}} working hours).”

### C) Need more info (structured)

“To proceed, please reply with:

1. {{item}}
2. {{item}}
3. {{item}}
   If any of this contains sensitive data, please do not include credentials in plain text; use {{approved method}}.”

### D) Resolution message

“We have {{action taken}} and this should resolve {{issue}}. Please try {{verification step}}. If the problem persists, reply to this ticket with {{what to include}} and we will continue.”

### E) Final reminder / no reply closure warning

“We have not heard back from you. If we do not receive a response within {{X}} days, we will close this ticket. You can reply at any time to reopen it.”

## Quality Assurance and Metrics

* Weekly review by Helpdesk Lead:

  * Tickets breaching first-response SLA
  * Tickets without owner > {{MaxUnownedHours}} hours
  * Tickets without internal notes explaining status
  * Long-running tickets without reminders/next dates
* Monthly metrics:

  * Median first-response time
  * Resolution time by category
  * Reopen rate
  * Top recurring issue types (feed into KB improvements)

## Security and Privacy Requirements

* Never request or repeat passwords, access tokens, or secret keys in RT messages.
* Minimize PII: request only what is required for support.
* If the ticket suggests a potential incident:

  * Tag `incident-suspected`
  * Escalate immediately per escalation rules
  * Follow the Security/Incident SOP

## Records and Auditability

RT is the system of record. All actions must be traceable via:

* Ticket history

## Training and Review

* New Helpdesk staff must complete onboarding using this SOP and process 3 tickets under supervision.
* SOP review frequency: every {{X}} months, or after any major process/tool change.
