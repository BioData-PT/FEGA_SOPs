**SOP for withdrawing FEGA studies/datasets from the EGA website**

Current implementation

| Document Owner | Aina Jené - EGA-CRG Operations Manager |
|----------------|----------------------------------------|
| Version        | 1.0                                    |
| Effective date | 01-09-2024                             |

**Use cases**

1.  **<u>Study/Dataset Unreleased from the Website</u>**

    1.  When a study or dataset is released on the website but needs to
        be unreleased (withdrawn), follow the procedure below (Withdraw
        Study/Dataset).

2.  **<u>Study/Dataset Unreleased and Deprecated</u>**

    1.  When a study or dataset has been released but must be unreleased
        and deprecated (marked as obsolete) from both the website and
        databases, follow the procedure below (Withdraw and Deprecate
        Study/Dataset).

3.  **<u>Study/Dataset Deletion</u>**

    1.  Complete deletion of a study or dataset is not supported. Once a
        persistent identifier (PID) is assigned to an object, it cannot
        be fully removed from the database.

Current availability depending on use case:

| **Use Case** | **Website Search (indexation)** | **Website URL** | **Public Metadata API** | **Metadata object status** | **Submitter Portal** | **Can it be reused?** | **EGA database** |
|----|----|----|----|----|----|----|----|
| 1 | No | Yes | Yes | NOT RELEASED | Yes | Yes | Yes |
| 2 | No | Yes | Yes | DEPRECATED | Yes | No | Yes |
| 3 | \- | \- | \- | \- | \- | \- | \- |

***Note***

| *The table above reflects the current implementation. Please refer to [<u>this</u>](https://docs.google.com/document/d/1ypoae5qb0SNGn6U2OeW7LHQB6OGyp4fIyV2QZBITpug/edit?usp=sharing) document for updates regarding future changes.* |
|----|

**Purpose**

The purpose of this SOP is to provide clear guidelines and procedures
for withdrawing FEGA studies and datasets from the EGA website,
applicable to use cases 1 and 2. Following this SOP ensures that all
withdrawals are handled consistently, efficiently, and in compliance
with established protocols, thereby maintaining the integrity and
accuracy of the EGA database.

**Scope**

This SOP describes the process for withdrawing FEGA studies and datasets
from the EGA website. It does not cover the procedures for modifying or
updating existing studies and datasets, nor does it address the
submission of new studies and datasets.

**Procedure for Use Case 1 and 2**

1.  **Contact the CEGA Helpdesk Team**

> Send an email to fega-helpdesk@ega-archive.org with the following
> information:

1.  **Subject**:

    1.  For withdrawing a study, use:

> *\[Withdrawal request\] Study EGAS5XXXXXXXX*

2.  For withdrawing a dataset, use:

> *\[Withdrawal request\] Dataset EGAD5XXXXXXXX*

2.  **Body**:

> Clearly state your request and include the following information:

1.  **Withdrawal Options:**

> Indicate whether you want to:

1.  **Unrelease Study/Dataset (use case 1):** This will change the
    release status back to “not released,” making it no longer visible
    on the EGA website through the search bar. However, it will still be
    visible by URL.

2.  **Unrelease and Deprecate Study/Dataset (use case 2)**: This will
    change the release status back to “deprecated”, making it no longer
    visible on the EGA website through the search bar. However, it will
    still be visible by URL. Furthermore, the metadata object will be
    moved to a “historic” schema in the CEGA database. The object cannot
    be reused in the future, but CEGA will keep it for auditing
    purposes.

<!-- -->

2.  **Deprecation of Linked Objects**:

> If you choose to deprecate the study/dataset, specify if you also want
> to deprecate all linked objects (samples, experiments, runs,
> analysis). If you prefer to deprecate only a subset, please provide a
> list of IDs.

2.  **Helpdesk Processing**

> A Helpdesk officer will take the ticket generated from your email and
> initiate internal procedures to address your request.

3.  **Resolution Notification**

> Once the request is processed, the Helpdesk officer will notify you of
> the resolution.

**Basic Information:**

- If you request to unrelease and/or deprecate a study, CEGA will also
  unrelease and/or deprecate all datasets linked to that study. If you
  only want to unrelease and/or deprecate the study, ensure you re-link
  the datasets to a different study, as the EGA Metadata model does not
  support released datasets without an associated study.

- Deprecating a metadata object can be reversed by CEGA, but this is a
  manual process and may take some time. Double-check the list of
  objects you wish to deprecate to avoid unnecessary delays.

- For users with permissions to an unreleased and/or deprecated dataset,
  those permissions will be automatically revoked (applicable only for
  nodes using the DAC Portal).
