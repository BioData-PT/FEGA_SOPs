## FEGA Guidance on SOP Compliance Assessment

### Why a FEGA SOP Compliance Framework

SOP compliance ensures processes are consistent across FEGA nodes, can be implemented and assessed, and improve over time. A simple compliance cycle helps maintain trust and quality in the FEGA ecosystem:

1) SOPs and policies define how work is done; 2) leadership commitment sets priorities; 3) teams are trained; 4) SOPs are created/implemented; 5) compliance is assessed; 6) improvements are applied; then the cycle repeats.

### Variability across FEGA nodes

FEGA includes nodes at different levels of maturity. Some operate in accredited or production environments; others are building services. This guidance is pragmatic: it supports nodes at any level, from first contact with the FEGA SOP repository to regular compliance assessments and reporting.

### Getting started

1. Connect to the FEGA SOP GitHub repository and set up a branch for your node.
   - Repository: https://github.com/BioData-PT/FEGA_SOPs
   - Use feature branches for edits. Submit changes via pull requests.
   - Read the index in `README.md` and the SOP template in `sop/templates/FEGA-SOP0021_TEMPLATE_Federated_EGA_SOP_-_v1.1.md`.

2. Implement CEGA templates and create node instances
   - CEGA/common templates live in `sop/templates` (e.g., `FEGA-SOP0013`, `FEGA-SOP0019`).
   - Node instances live in `sop/instances` (e.g., `FEGA-PT-SOP0013`, `FEGA-PT-SOP0019`).
   - Keep templates node‑agnostic; add node specifics only in instances.

3. Train and enable your team
   - Ensure maintainers know the repository layout, naming, and linking conventions.
   - Encourage consistent sectioning (Purpose, Scope, Procedure) and clear steps.

4. Create and maintain SOPs
   - Start from the template. Fill metadata tables (Template ID/version, Node, Instance version) and document history.
   - Use in‑repo links for cross‑references and ensure images render (relative paths into `docs/images`).

5. Participate in compliance assessments
   - Run the checklists below before every PR. Peer review within FEGA is encouraged.

6. Continuous improvement
   - Use assessment findings to improve both templates and instances. Update history tables and README entries.

### Compliance checklists

All SOPs (templates and instances)
- Metadata table present and complete at the top.
- Document History includes the current change.
- Section headings use `##` (Purpose, Scope, Procedure).
- Images render with relative paths to `docs/images` from the file location.
- Cross‑links use in‑repo Markdown paths; avoid outdated external links unless intentional.
- The SOP appears correctly in `README.md` with identifier, versions, steps, node, and “Last updated”.

Templates (sop/templates)
- Template ID follows `FEGA-SOP####` and `Node` is `CEGA` (or `Joint`).
- Content is node‑agnostic; placeholders use `{fega}` or `{node name}`.
- Version bump recorded in Document History for template changes.

Node instances (sop/instances)
- Node identifier follows the node scheme (e.g., `FEGA-PT-SOP0013`).
- `Node` matches the instance (e.g., `FEGA-PT`) and instance version is set.
- No numbering collision with CEGA template IDs in the instance metadata.
- Cross‑links point to the right targets (prefer node instances; templates when appropriate).
- Node‑specific URLs (e.g., `helpdesk.{fega}.ega-archive.org`) are correct.

### Assessment outcomes

- Compliant: All mandatory checks pass.
- Minor findings: Non‑blocking issues — merge and open a follow‑up issue.
- Changes required: Blocking issues — fix before merging.

### Reporting format (per SOP)

- SOP: path and identifier as in README
- Result: Compliant | Minor findings | Changes required
- Notes: bullets indicating issues and fixes
- Reviewer/date

### References

- FEGA SOP repository: https://github.com/BioData-PT/FEGA_SOPs
- Templates: `sop/templates/`
- Node instances: `sop/instances/`
- Index: `README.md`
