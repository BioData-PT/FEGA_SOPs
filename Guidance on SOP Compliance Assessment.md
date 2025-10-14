## FEGA Guidance on SOP Compliance Assessment

This document provides FEGA‑specific guidance for assessing SOP compliance. It replaces prior GDI‑oriented text and aligns with this repository’s structure and practices.

### Purpose

Provide a repeatable approach for FEGA nodes to verify that SOPs are complete, current, and usable — and to drive continuous improvement across the network.

### Scope

Applies to SOPs maintained in this repository:
- Templates under `sop/templates` (CEGA/common)
- Node instances under `sop/instances` (e.g., FEGA‑PT)

### Repository and layout

- Repository: https://github.com/BioData-PT/FEGA_SOPs
- Index and navigation: `README.md`
- Template starting point: `sop/templates/FEGA-SOP0021_TEMPLATE_Federated_EGA_SOP_-_v1.1.md`
- Images: `docs/images/` (use relative paths from SOP files)

### Roles

- CEGA/FEGA Operations: owns and reviews templates; ensures consistency.
- Node maintainers: own node instances; keep them aligned with templates.
- Optional peer reviewer: an additional reviewer from another node.

### Cadence

- With every SOP change (template or instance) via PR.
- Periodic spot‑checks (e.g., quarterly) or after major platform updates.

### How to assess

1) Find the SOP entry in `README.md` and open the file.  
2) Confirm the README row is accurate (identifier, versions, steps, node, last updated).  
3) Run the relevant checklist (All, Template, Instance).  
4) Record findings in the PR or an issue.  
5) Approve when all mandatory items pass; track optional improvements.

### Checklist — All SOPs

Mandatory
- Metadata table present and complete (Template ID, Template version, Topic, SOP type, Node, Instance version).
- Document History includes an initial release and the current change.
- Headings use `##` (Purpose, Scope, Procedure).
- Images render; paths are relative (into `docs/images/`).
- Cross‑links use in‑repo Markdown paths; external links are intentional and current.
- The SOP appears correctly in `README.md` (identifier, versions, steps, node, date).

Recommended
- Clear steps, consistent terms; stable anchors for deep linking.

### Checklist — Templates (sop/templates)

Mandatory
- Template ID follows `FEGA-SOP####`; `Node` is `CEGA` (or `Joint`).
- Content is node‑agnostic; use placeholders like `{fega}` or `{node name}`.
- Version bumps recorded in Document History for template changes.

Recommended
- Cross‑references to other templates use `sop/templates/...` relative paths.
- Examples (e.g., emails) are generic or clearly marked with placeholders.

### Checklist — Node Instances (sop/instances)

Mandatory
- Instance identifier follows the node scheme (e.g., `FEGA-PT-SOP0013`).
- `Node` matches the instance (e.g., `FEGA-PT`) and instance version is set.
- No numbering collision with CEGA template IDs in instance metadata.
- Cross‑links point to the right SOPs (prefer node instance; link to templates when needed).
- Node‑specific URLs (e.g., `helpdesk.{fega}.ega-archive.org`) are correct.

Recommended
- Replace legacy Google Doc links with in‑repo markdown where possible.
- Ensure portal URLs and anchors reflect the node (e.g., `submission.portugal.ega-archive.org`).
- Maintain consistent naming with README (identifier and title).

### Outcomes

- Compliant: All mandatory checks pass.
- Minor findings: Non‑blocking; merge and raise a follow‑up issue.
- Changes required: Blocking; fix before merge.

### Reporting format (per SOP)

- SOP: file path and identifier (as listed in `README.md`)
- Result: Compliant | Minor findings | Changes required
- Notes: brief bullets (e.g., “Fix image path at line 72”)
- Reviewer/date

### Change management

- Make all updates via PRs. Summarize changes in the SOP’s Document History and update the README row.
- For template updates that impact instances, open a follow‑up issue so node maintainers can align their SOPs.
- Keep commit messages concise and specific to the SOP(s) touched.

### Example evidence

- File paths validated (e.g., `sop/templates/...`, `sop/instances/...`).
- README rows updated with correct identifiers, versions, and dates.
- Screenshots confirming images render after path changes.
- Click‑through of cross‑links to confirm they open the right SOPs.

### References

- Index: `README.md`  
- Templates: `sop/templates/`  
- Node instances: `sop/instances/`  
- FEGA compliance checklist (compact): `SOP_Compliance_assessment.md`
