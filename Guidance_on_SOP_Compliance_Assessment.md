## FEGA Guidance on SOP Compliance Assessment

This document is a compliance assessment approach to the Federated EGA (FEGA).

### Purpose

Provide FEGA nodes with a detailed, repeatable way to verify that SOPs are complete, current, and usable — for both CEGA templates and node‑specific instances — and to drive continuous improvements.

### Scope

Applies to SOPs hosted in this repo:

- Templates: `sop/templates`
- Node instances: `sop/instances` (e.g., FEGA‑PT)

### Repository and layout

- Repository: <https://github.com/BioData-PT/FEGA_SOPs>
- Index and navigation: `README.md` (separate Templates and Node Instances tables)
- SOP template starting point: `sop/templates/FEGA-SOP0021_TEMPLATE_Federated_EGA_SOP_-_v1.1.md`
- Images: `docs/images/` (use relative paths from SOP files)

### Roles

- CEGA/FEGA Operations: owns templates; ensures consistency; reviews PRs.
- Node maintainers: own node instances; align with templates; propose improvements.
- Optional peer reviewer: adds a second check across nodes.

### Cadence

- On every SOP change via PR (template or instance).
- Periodic spot‑checks (e.g., quarterly) and after major platform updates.

### How to assess (step‑by‑step)

1. Locate entry in `README.md` and open the SOP. Confirm the README row is accurate (identifier, template version, node, instance version, steps, last updated).
2. Check metadata and history at the top of the SOP. Ensure Template ID, Template version, Node, Instance version are present and the Document History table includes the current change.
3. Verify structure: headings use `##` (Purpose, Scope, Procedure). Steps are concise and actionable. Anchors are stable and human‑readable.
4. Validate links and images: cross‑links are in‑repo; image paths resolve and render; images live under `docs/images/` and use correct relative paths from the file location (e.g., `../../docs/images/...` for files under `sop/templates` or `sop/instances`).
5. Numbering: templates use `FEGA-SOP####`; instances use node‑specific IDs (e.g., `FEGA-PT-SOP0013`). Avoid collisions between template IDs and instance identifiers.
6. Cross‑references: instances should link to local node instances when appropriate; link to templates only when referencing the generic version.
7. Decision and notes: determine Compliant | Minor findings | Changes required. Record notes in the PR (see Reporting format below).

### Checklist — All SOPs

Mandatory

- Metadata table present and complete (Template ID, Template version, Topic, SOP type, Node, Instance version).
- Document History includes an initial release and the current change.
- Headings use `##` (Purpose, Scope, Procedure). Steps are clear and unambiguous.
- Images render; paths are relative to `docs/images/` from the file location.
- Cross‑links use in‑repo Markdown paths; external links are intentional and current.
- README row is correct (identifier, versions, steps, node, date).

Recommended

- Consistent terminology with adjacent SOPs. Stable anchors for deep links.
- “Steps” count in README matches the Procedure.

### Checklist — Templates (sop/templates)

Mandatory

- Template ID follows `FEGA-SOP####`; `Node` is `CEGA` (or `Joint`).
- Content is node‑agnostic; use placeholders like `{fega}` or `{node name}`.
- Version bumps recorded in Document History for template changes.

Recommended

- Cross‑references to other templates use `sop/templates/...` relative paths.
- Examples (e.g., emails) are generic or marked with placeholders.

### Checklist — Node Instances (sop/instances)

Mandatory

- Instance identifier follows the node scheme (e.g., `FEGA-PT-SOP0013`).
- `Node` matches the instance (e.g., `FEGA-PT`) and instance version is set.
- No numbering collision with CEGA template IDs in instance metadata.
- Cross‑links point to the right SOPs (prefer node instance; link to templates when needed).
- Node‑specific URLs (e.g., `helpdesk.{fega}.ega-archive.org`, `submission.{fega}.ega-archive.org`) are correct.

Recommended

- Replace legacy Google Doc links with in‑repo markdown where possible.
- Ensure anchors and link texts are descriptive and current.
- Keep naming consistent with README (identifier and title).

### Outcomes

- Compliant: All mandatory checks pass.
- Minor findings: Non‑blocking; merge and raise a follow‑up issue.
- Changes required: Blocking; fix before merge.

### Reporting format (per SOP)

- SOP: file path and identifier (as listed in `README.md`)
- Result: Compliant | Minor findings | Changes required
- Notes: brief bullets (e.g., “Fix image path at line 72; update README steps from 6→7”).
- Reviewer/date

### Change management

- Make all updates via PRs. Summarize changes in the SOP’s Document History and update the README row.
- For template updates that impact instances, open a follow‑up issue so node maintainers can align their SOPs.
- Keep commit messages concise and specific to the SOP(s) touched.

### Example evidence

- File paths validated (e.g., `sop/templates/...`, `sop/instances/...`).
- README rows updated with correct identifiers, versions, steps, dates.
- Screenshots confirming images render after path changes.
- Click‑through of cross‑links to confirm they open the right SOPs.

### Implement Node-specific FEGA SOPs

*While FEGA-wide SOPs (templates) cover processes that are the same for all nodes (see above in point 2), node-specific SOPs are required to accommodate the node-to-node variability in operations, services, infrastructure, resources, pre-existing processes or other local requirements. Node-specific SOPs are based on FEGA templates to provide a necessary basic alignment for node-specific SOPs describing the same process.*

   1. To ensure that the most up-to-date version of the SOP is being used, node-specific SOPs can be accessed through the GitHub folder:
   [https://github.com/BioData-PT/FEGA_SOPs/tree/main/sop/instances](https://github.com/BioData-PT/FEGA_SOPs/tree/main/sop/instances)
   2. Follow the SOP creation guidance in this repository to create and adapt node-specific SOPs to your node's requirements, all the way to the SOP being released on the GitHub repository.

### Regular Review of SOPs

*It is important to ensure that the SOPs reflect how the process is carried out, and therefore, they need to be reviewed regularly to ensure that they are up-to-date.*

   1. As SOPs are being used on a routine basis, it is good practice to note any discrepancies or deviations from the SOP and request modifications as appropriate to reflect the current processes. Modification requests can be made by raising an issue in the [FEGA SOPs GitHub repository](https://github.com/BioData-PT/FEGA_SOPs).
   2. All SOPs have to be reviewed at least once a year.
   3. \[e.g. "action" step\] Implement an SOP tracking system to ensure that each FEGA-wide template and node-specific SOP is reviewed at least once a year.

### Review of Training Processes & Staff Training Records

*All SOPs should be clear and precise, easy to follow. Nevertheless, it is good practice to train all staff in those SOPs which they follow as part of their job. This ensures that processes are fully understood and carried out consistently, minimising person-to-person variability. By documenting such training in Staff Training Records, diligence is demonstrated, and the records count as evidence for the efforts aiming for SOP compliance.*

   1. Staff training can be provided in person, online or via a video.  
   2. After creation of an SOP, training should be provided, ideally by someone involved in the SOP’s creation, e.g. a co-author or reviewer. Staff previously trained in an SOP can also provide training to those new to the process.  
   3. The nodes should document the training on a spreadsheet/table, one per staff member. Annex 1 shows an example of such a spreadsheet/table.  
   4. Each member of staff involved with FEGA is responsible for maintaining their own training records to ensure they remain up-to-date.
   5. Training records should be reviewed by a more senior member of staff (e.g. line manager) at least once a year to identify any potential gaps or training needs.  
   6. A formal SOP compliance assessment should also review these training records.

### SOP compliance assessment

*A compliance assessment is a systematic evaluation of processes and is key to the continued improvement of a service or (a set of) processes. This is crucial to maintain a high level of standard, to ensure alignment with defined quality standards, policies or relevant regulations, and to support the ambition to deliver the best possible service, striving for excellence. The compliance assessment can cover a range of aspects as listed below. Depending on the complexity of the system to be audited, the scope of an assessment can be kept broad or focus specifically on certain areas within the system (e.g. Helpdesk processes, or staff training records).*

   1. Each node is responsible for locally carrying out self-assessments of the node's processes.
   2. The compliance assessment should be performed at least once per year. Alternatively, it could be broken down into more frequent, shorter assessments, each focused on a particular aspect (a particular process or topic), it's up to the node to structure those systematically to cover the processes as broadly as possible to cover the node's processes.
   3. All compliance assessments need to be documented (1) which aspects and/or processes were assessed, (2) what the findings were, noting all discrepancies and non-compliances. Annex 2 provides a checklist detailing important aspects to be monitored as part of the assessment.
   4. The assessment should check that all relevant SOPs have been implemented at the node & the latest version of the SOP is being used.
   5. Review all (crucial) processes carried out at the node and check (1) that there is an SOP available to describe this process, (2) this SOP is implemented at the node, (3) the way the process is carried out as described in the SOP. (4) If the SOP requires additional documentation (spreadsheets or checklists) to be completed during the process, verify that these are completed/recorded and securely stored. (5) Check that all staff involved in the process have been trained in the relevant SOPs.

### Assessment Follow-up: Report and Action Plan

*The compliance assessment described above needs to be documented (see 6.3), based on the notes / documentation produced during the compliance assessment. The notes made during the assessment are being reviewed and summarised in a report, which will include an action plan, if necessary. To document the node's continued engagement with the FEGA Compliance Framework, these reports should be deposited on the FEGA shared drive.*
*Annex 3 shows the template for such a report and action plan. It covers the following aspects:*

   1. It captures (1) the node, (2) the date of the compliance assessment, (3) the name of the assessor, (4) the name of the person completing the report (ideally the same person as the assessor), (5) the signature of the person completing the report, and (6) the date of the signature.
   2. It provides further details about the compliance assessment’s focus, relating to point 6.2: (1) there is a tickbox to indicate that it was a major (annual) compliance assessment across the entire range of the node’s activities. If the node opted for more frequent but focused compliance assessment, there is a tickbox to indicate that it was a minor compliance assessment and (2) options to specify the focus of the compliance assessment.  
   3. There is a box to list all SOPs which were referred to during the assessment.  
   4. The remainder of the report form captures the findings of the compliance assessment.  
   5. Occasionally, a compliance assessment may not observe any deviations or non-compliances when the actual activities are compared to the formal SOPs. This can be captured by the tickbox "The assessment was satisfactory, no corrective actions are needed."
   6. The table captures individual observations and an evaluation of risks any potential deviations or non-compliances could pose, also if any corrective or preventive actions are needed to avoid such non-compliances or how to improve the process or system. The table provides fields to capture the following aspects of the observation:  
   7. The process (step) or activity which was assessed.  
   8. The relevant SOP(s) for this activity.  
   9. Under “Observation / Discrepancy”, any observations should be captured: this could be (1) a description of the discrepancy that was observed between the actual activity and the process described in the SOP, (2) no discrepancies observed or (3) no relevant SOP available for this activity.  
   10. Severity indicates the level of impact this non-compliance may have (1) high (for example if the non-compliance would affect data protection, security, or significantly affects the quality of the service provided), (2) medium (leading to minor mistakes that can be easily rectified), (3) low (an observation on how a process can be improved).  
   11. The “Comments” field provides additional space to elaborate further on the observation or context.  
   12. “Risks” should be captured if the non-compliance would affect the quality of service, data protection/security risks, or lead to any other significant impact.  
   13. Any recommendations based on the observation should be recorded under “Recommended Mitigation / Corrective Actions”. This could include suggestions such as additional training for staff, requesting a new SOP, revising existing SOP, escalating the issue if severe, or rectifying any mistakes made.  
   14. If Action Items are suggested in 7.13, define (1) who should be responsible for implementing the action & (2) the expected timeline for the action to be completed by.  
   15. Once the action is completed, the date of completion is recorded in the field “Completion Date (to be completed when actioned)”.

### Annex 1 — Staff Training Records

**Name:** .......................   **Job Title:** .......................   **Start Date:** .......................

| Name of Process | SOP accession | SOP version | Comment | Training Start Date | Competency Date | Trainer's Initials | Trainee's Initials |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Helpdesk Ticket Management | FEGA-SOP0004 | v1.0 | *(example)* | DD/MM/YYYY | DD/MM/YYYY | XY | ABC |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

### Annex 2 — Compliance Assessment Checklist

#### Governance & repository access

| Done? | Prompt |
| :--- | :--- |
| | Are the relevant staff members part of the [FEGA SOPs GitHub repository](https://github.com/BioData-PT/FEGA_SOPs) so that they can interact with it (request, review or create SOPs)? |
| | Has the node created a new branch for the FEGA SOPs repository? |
| | Has your node nominated a member for the FEGA Operations Committee (OC)? |
| | Has your node nominated a member for the FEGA Security & Data Protection Committee (SDPC)? |

#### SOP implementation

| Done? | Prompt |
| :--- | :--- |
| | Have all relevant FEGA-wide SOP templates been implemented at the node? |
| | Has the node implemented relevant node-specific SOPs? |
| | Are you using the most up-to-date version of the SOPs? |

#### Training

| Done? | Prompt |
| :--- | :--- |
| | Are you providing training to the staff when they are new to SOPs? |
| | Are you providing training to the staff after an SOP has been updated? |
| | Are everyone's training records up-to-date? |

#### During an SOP compliance assessment

| Done? | Prompt |
| :--- | :--- |
| | Choose the frequency of compliance assessments (a broad scope annually or more focused, several times per year)? |
| | Schedule assessments & choose the topic for each assessment. |
| | During the assessment, choose a set of processes relating to the topic, then follow the activities step by step and compare them to the description of the process in the SOP. |
| | Make notes of any discrepancies. |

#### After the assessment

| Done? | Prompt |
| :--- | :--- |
| | Refer to the notes from the assessment and complete the Compliance Assessment Report & Action Plan. |
