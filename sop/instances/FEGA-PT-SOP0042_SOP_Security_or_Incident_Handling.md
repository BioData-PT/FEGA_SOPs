# FEGA SOP — Security/Incident Handling

| Metadata         | Value                        |
| ---------------- | ---------------------------- |
| Template ID      | `FEGA-SOP0005`               |
| Template version | `v1.0`                       |
| Topic            | Security & Incident Response |
| SOP type         | SOP                          |
| Node             | `-`                     |
| Instance version | `-`        |

## Document History

| Template version | Instance version      | Author(s)      | Description of changes | Date           |
| ---------------- | --------------------- | -------------- | ---------------------- | -------------- |
| `v1.0`           | `—`                   | Jorge Silva, Jorge Oliveira, Miguel Cisneiros | Initial release        | 16-12-2025     |
| `v1.0`           | `v1.0`                | Jorge Silva, Jorge Oliveira, Miguel Santos | Instatiate FEGA PT Node Security requirements and response      | 24-02-2026 |
| `v1.0`           | `{{InstanceVersion}}` | {{AuthorList}} | {{ChangeSummary}}      | {{DD-MM-YYYY}} |

## 1. Purpose

This SOP defines how FEGA-PT Node detects, triages, contains, eradicates, recovers from, and learns from security incidents affecting the Federated European Genome-phenome Archive (FEGA) services operated by the node. It ensures rapid risk reduction, correct notifications, evidence preservation, and consistent, auditable handling aligned with FEGA’s federated responsibilities. 

## 2. Scope

Applies to all security incidents impacting any FEGA-PT Node FEGA-facing component, including but not limited to:

* Node authentication/authorisation surfaces (AAI integration, identity providers, service accounts)
* Node ↔ Central EGA integration channels (e.g., messaging integration) 
* Submission pipeline (submitter inbox, ingest pipeline, metadata submission workflow) 
* Storage and distribution (archive storage, file database, backups, outbox/download solutions) 
* Cryptography and key management (Crypt4GH node key pairs; TLS certificates; secrets vaults) 
* Public/controlled metadata exposure (including prevention of personal metadata publication) 

Out of scope: incidents solely within Central EGA systems; however, FEGA-PT Node must coordinate when node incidents could propagate across federation or involve shared processes. 

## 3. Definitions and data categories

### 3.1 Security incident (operational)

A security incident is any event that results in, or presents a credible risk of, unauthorised access to, unauthorised disclosure of, loss of integrity of, or loss of availability of FEGA services or data handled by FEGA-PT Node.

### 3.2 FEGA-relevant data categories

Use these terms consistently in incident records:

* **Administrative Data**: operational data generated through running FEGA services (may include direct identifiers like names/emails). 
* **Non-personal Metadata**: descriptive metadata not identifying individuals; may be shared to Central for public discovery. 
* **Personal Metadata**: metadata that could identify individuals (e.g., demographics/ancestry); must not be shared to public catalogue or exchanged improperly. 
* **Research Data**: omics/genetic and health/phenotype data; special category personal data under GDPR context. 

## 4. Roles and responsibilities

### 4.1 Incident roles (must be assignable at any time)

* **Incident Commander (IC)**: owns decisions, timeline, and closures; ensures containment priority.
* **Security Lead / SOC liaison**: leads technical investigation, threat assessment, evidence collection.
* **Service Owner(s)** (per component): executes containment/recovery actions for their systems.
* **Helpdesk Liaison**: manages RT ticketing, user/DAC communications routing, and status updates.
* **DPO / Legal**: assesses notification obligations and approves external statements.
* **Central EGA Liaison**: coordinates cross-federation impact and required joint actions.

### 4.2 Federation coordination principle

Central EGA and FEGA nodes have distinct operational scopes; nodes run services for their jurisdictions and must coordinate through FEGA governance/operations where federation-level impact is possible. 

## 5. Severity levels and response targets

Assign severity at triage and revise as needed.

* **SEV-1 (Critical)**: confirmed or strongly suspected exposure of Research Data or Personal Metadata; active compromise; federation impact; ransomware; key compromise affecting confidentiality.
 
* **SEV-2 (High)**: likely compromise of Administrative Data; privilege escalation attempt; significant service disruption; confirmed malware without evidence of data access yet.
    
* **SEV-3 (Moderate)**: suspicious activity with limited scope; failed intrusion with credible risk; localised outage with no evidence of unauthorised access.
   
* **SEV-4 (Low)**: policy violations without system compromise (e.g., user credential sharing), minor misconfigurations, non-exploitable vulnerabilities.

## 6. Detection and reporting channels

### 6.1 Sources of detection

* Monitoring alerts (availability, auth anomalies, MQ anomalies, storage access patterns)
* Audit logs indicating unusual access-right changes or resource usage 
* Reports from users, submitters, DAC members, or Data Controllers
* Central EGA/FEGA operational communications

### 6.2 Reporting rule

Any staff member who suspects an incident must:

1. Create an RT **SEC-INCIDENT** ticket (or equivalent), marked **restricted**, and
2. Notify on-call/security contact immediately: fegaportugal@biodata.pt.

If a DAC suspects a breach, the handler must collect affected dataset identifiers, suspected timeframe, and suspected unauthorised users (if available) and treat as SEV-1/2 until proven otherwise. 

## 7. Standard incident workflow (mandatory steps)

### 7.1 Step 0 — Safety and containment-first mindset

If there is an active compromise in progress, prioritise stopping further damage over full diagnosis. Avoid actions that destroy evidence unless necessary to stop ongoing exfiltration.

### 7.2 Step 1 — Triage (first actions)

Within the severity SLA:

* Assign Incident Commander and record start time (use explicit timestamp: `DD-MM-YYYY HH:MM`).
* Classify affected data categories (Administrative / Personal Metadata / Research Data). 
* Identify affected components from the FEGA node stack (MQ, inbox, ingest, archive, file DB, outbox, portal/API, key management). 
* Start an **Incident Log** (append-only) documenting:

  * observed indicators
  * actions taken (who/when)
  * working hypotheses and evidence
* Decide initial severity; set next update time.

### 7.3 Step 2 — Evidence preservation (do before deep investigation)

* Preserve relevant logs and system state:

  * auth/identity logs, access-right changes, download/outbox logs
  * MQ connection/auth logs and message routing/shovel events (if applicable) 
  * storage access logs, integrity/checksum records, backup job logs
* Snapshot or image affected hosts/containers if feasible.
* Restrict evidence access to incident team; store securely.

### 7.4 Step 3 — Containment (limit blast radius)

Containment options may include revoking access, withdrawing/pausing distribution of datasets, disabling ingestion functions, or isolating systems from the network, depending on the incident. 

Minimum containment actions to consider by component:

* **Identity / accounts**: inform Central-EGA that the account has been compromised and must be suspended immediately.
* **Service accounts/secrets**: revoke compromised API keys or secrets.
* **RabbitMQ / federation link**: suspend federation/shovel links if compromise suspected. 
* **Inbox/ingest malicious file**: quarantine suspicious uploads; block submitter endpoint if abused; inform Central-EGA of the account behaviour and request account suspension. 
* **Outbox/download exfiltration**: shutdown the distribution system in case of data exfiltration; inform Central-EGA to deactivate account in case of cloud misuse.
* **Downloaded data misuse**: in case a user if found to upload downloaded data into unsecure external facilities (e.g., cloud), inform Central-EGA to suspend the user's account.
* **Storage integrity compromising**: isolate affected buckets/volumes; enforce read-only mode if necessary; validate backup integrity before restoration.
* **Cryptographic material**: if Crypt4GH private key compromise is suspected, treat as SEV-1 and initiate key rotation and re-encryption strategy. 

### 7.5 Step 4 — Eradication (remove root cause)

* Identify root cause class (credential compromise, vulnerable component, misconfiguration, insider misuse, malware).
* Apply remediations:

  * patch/upgrade affected services
  * remove malicious artefacts
  * revoke/replace credentials and certificates
  * correct IAM policies / ACLs (least privilege)
* Validate that the vector is closed with targeted verification (do not “scan the internet”; focus on your perimeter and affected systems).

### 7.6 Step 5 — Recovery (restore normal operation safely)

* Restore services in controlled order:

  1. identity/auth
  2. MQ integration
  3. ingest
  4. outbox/download
     
* Integrity checks:

  * validate hashes/checksums where available
  * validate that encryption and key separation requirements are maintained (keys not co-located with encrypted data; encrypted in transit and at rest)
    
* Monitor closely for recurrence; keep heightened logging until closure.

### 7.7 Step 6 — Closure criteria

Close the incident only when:

* containment is complete and verified,
* eradication actions are implemented,
* recovery is stable for 48 hours.
* notifications and documentation are complete,
* post-incident actions are assigned with owners and dates.

## 8. Notification and communications

### 8.1 Who must be informed (decision tree)

* **Always inform**: Node leadership, DPO/legal, FEGA Central liaison.
* **Inform Central EGA / FEGA Operations** if:

  * any cross-node integration is impacted (MQ federation link, shared workflows), or
  * there is any risk of federation-wide trust impact.
    
* **Inform DAC/Data Controller** when:

  * Research Data or Personal Metadata may be involved, or
  * access logs show suspicious access patterns for specific datasets. 

### 8.2 Communications rules

* Use RT restricted ticket + approved secure channels; do not paste secrets.
* External statements regarding SEV-1 incidents must be approved by DPO/legal.

### 8.3 Minimal notification content (template)

Include:

* incident ID, start time (`DD-MM-YYYY HH:MM {{TZ}}`).
* severity, impacted components, and impacted data categories.
* known affected dataset accessions (if applicable).
* actions taken (containment).
* current risk assessment and next update time.

## 9. FEGA-specific incident playbooks (concise)

### 9.1 Compromised user or operator account (SEV-2 → SEV-1 if data accessed)

Contain:

* inform Central-EGA of the situation and request account suspension.
* review access-right changes and data access logs.
* if unauthorised dataset access suspected: pause outbox/download and notify DAC/Data Controller. 

Recover:

* re-enable with stronger assurance if feasible; add monitoring rule.

### 9.2 Suspected unauthorised dataset download / outbox abuse (SEV-1)

Contain:

* block distribution for impacted dataset(s).
* preserve download logs, access logs, storage logs.

Coordinate:

* notify DAC/Data Controller with dataset list and timeframe 

### 9.3 Crypt4GH private key compromise (SEV-1)

Contain:

* generate new node key pair.
  
  Eradicate/Recover:
  
* assess which files were decrypted using compromised key.
* plan re-encryption / re-keying strategy (prioritise most sensitive/high-risk datasets).

### 9.4 MQ / Central integration anomaly (SEV-2)

Contain:

* suspend federation/shovel links; rotate MQ credentials.

Investigate:
  
* connection history, message patterns.
  
Recover:

* restore link only after credential rotation + configuration review + monitoring enabled.

### 9.5 Personal metadata accidentally exposed in public catalogue (SEV-1)

Contain:

* inform Central-EGA and request dataset removal or modification, depending on the exposed data.

Investigate:
  
* determine pathway (metadata submission error, pipeline transform, human error).

Notify:
  
* DPO/legal + Data Controller; assess if formal notification required.

Prevent:
  
* add automated checks in metadata validation pipeline (block release until fixed).

### 9.6 Ransomware / destructive malware on archive storage (SEV-1)

Contain:

* isolate storage; disconnect affected hosts; preserve snapshots.

Recover:
  
* restore from verified clean backups; validate integrity and access control.

Post:

* credential rotation; segmentation review.

## 10. Auditability and minimum logging requirements

The node must maintain logs sufficient to reconstruct:

* changes to user access rights.
* dataset access events.
* operational actions. 

For FEGA node architecture, ensure log coverage across inbox/archive/outbox and MQ integration components. 

## 11. Post-incident review (mandatory)

Within 10 working days:

* produce a post-incident report containing:

  * timeline, root cause, impacted data categories, scope, and decisions
  * what worked / what failed
  * preventive actions with owners and due dates
    
* update risk register and monitoring rules
* update this SOP if gaps were found

## 12. Training and exercises

* Onboarding: all operators must complete a simulation exercise using SEV-1 scenario.
* Recurring: run at least byannually simulation + one technical recovery drill (restore + integrity validation).

## 13. Appendix A — Incident record (fields)

* Incident ID: `FEGA-PT Node-SEC-{{YYYY}}-{{NNN}}`
* Start time / end time (explicit)
* Severity history (with timestamps)
* Affected components (select from FEGA component list)
* Affected data categories (Administrative / Non-personal Metadata / Personal Metadata / Research Data) 
* Affected dataset accessions (if applicable)
* Containment actions (who/when)
* Evidence list and storage location
* Notifications (who/when/content summary)
* Recovery validation checklist
* Post-incident actions (owner, due date)

## 14. Appendix B — Contact list (placeholders)

* Security/on-call: fegaportugal@biodata.pt
* DPO/legal: dpo@biodata.pt
* Central EGA liaison: ega-operations-comm@ebi.ac.uk
