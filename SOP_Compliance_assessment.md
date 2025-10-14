# FEGA SOP Compliance Assessment

## Purpose

Establish a simple, repeatable way to assess whether Federated EGA (FEGA) SOPs are present, correct, and usable across nodes. The assessment supports consistency across the network, improves quality over time, and ensures node‑specific SOP instances align with their CEGA templates.

## Scope

Applies to SOPs maintained in this repository, both:
- Templates in `sop/templates` (CEGA/common)
- Node instances in `sop/instances` (e.g., FEGA‑PT)

The assessment covers document structure, metadata, links, images, cross‑referencing, numbering, and README index entries. It does not assess legal or policy compliance.

## Roles

- Node Maintainer: prepares and self‑assesses node instances; fixes issues.
- FEGA Operations (CEGA): maintains templates; reviews node submissions; approves/requests changes.
- Peer Reviewer (optional): a maintainer from another node who provides an additional check.

## Cadence

- On creation or update of any SOP template or instance (PR level).
- Quarterly spot‑checks for active nodes, or after major FEGA platform changes.

## How To Assess

1. Locate the SOP in the README index and open the file.
   - Templates: `README.md` > Templates table
   - Instances: `README.md` > Node Instances table
2. Run through the relevant checklist (Template or Instance).
3. Record findings in the PR or an issue. Request fixes when needed.
4. Approve when all mandatory items pass; track improvements for optional items.

## Checklist — All SOPs (templates and instances)

Mandatory
- Metadata table present and complete at the top (Template ID, Template version, Topic, SOP type, Node, Instance version).
- Document History table present with at least an initial release row and the current change.
- Section headings use `##` (e.g., `## Purpose`, `## Scope`, `## Procedure`).
- Internal image links resolve and render; images live under `docs/images/` and are referenced with a relative path from the SOP location.
- Internal cross‑links use in‑repo Markdown paths (avoid outdated Google Doc links unless explicitly kept by design).
- The SOP appears in the correct README table with an accurate identifier, versions, steps count, node, and “Last updated” date.

Recommended
- Clear, concise steps; consistent terminology across SOPs.
- Anchors/headings are stable and human‑readable for deep linking.

## Checklist — Templates (sop/templates)

Mandatory
- Template ID follows `FEGA-SOP####` (e.g., `FEGA-SOP0013`).
- `Node` is `CEGA` (or `Joint` where applicable), not node‑specific.
- Content is node‑agnostic; placeholders use `{fega}` or “{node name}” where needed.
- Version reflects template changes (e.g., v1.2) and is recorded in Document History.

Recommended
- Cross‑references to other templates use `sop/templates/...` relative paths.
- Examples and email templates are generic or clearly marked with placeholders.

## Checklist — Node Instances (sop/instances)

Mandatory
- Instance identifier follows node scheme (e.g., `FEGA-PT-SOP0013`).
- `Node` field matches the node (e.g., `FEGA-PT`).
- Instance version is set and tracked in Document History.
- No collision with CEGA template numbering in the template ID field (the template’s ID remains on the template, while the instance carries the node‑specific ID in its own metadata).
- Cross‑links to related SOPs point to the correct target (prefer in‑repo node instance; if intentionally referencing a template, link to `sop/templates/...`).

Recommended
- Node‑specific portal URLs (e.g., `helpdesk.{fega}.ega-archive.org`) are correct for the node.
- Any retained links to external guidance (e.g., CEGA help pages) are current and accessible.

## Scoring and Outcomes

Status definitions
- Compliant: All mandatory checks pass.
- Minor findings: Non‑blocking issues (typos, formatting) — merge with a follow‑up issue.
- Changes required: Blocking issues (broken links, missing metadata/history, numbering collisions) — fix before merge.

## Reporting Format (per SOP)

- SOP: file path and identifier shown in README
- Result: Compliant | Minor findings | Changes required
- Notes: brief bullets (e.g., “Fix image path at line 72”, “README shows wrong template version”)
- Reviewer: name/date

## Change Management

- All updates via PR; include a short summary of changes in the Document History table and update the README row.
- For template changes affecting instances, create a follow‑up issue to track nodes’ updates.

## Example Evidence (what to check/attach)

- File path(s): `sop/templates/...`, `sop/instances/...`
- README rows updated with correct identifiers and versions
- Screenshots of rendered images if paths were fixed
- Links clicked: cross‑links open the correct in‑repo SOP

## References

- Templates: `sop/templates/` (e.g., `sop/templates/FEGA-SOP0013_...md`)
- Node Instances: `sop/instances/` (e.g., `sop/instances/FEGA-PT-SOP0013_...md`)
- Index: `README.md`
