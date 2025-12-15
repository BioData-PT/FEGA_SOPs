# FEGA SOP - SOP for Federated EGA Metadata Check and Release Protocol (FEGA Portugal)

| Metadata | Value |
| -- | -- |
| Template ID | `FEGA-PT-SOP0018` |
| Template version | `v2.2` |
| Topic | Joint CEGA/FEGA Node Processes |
| SOP type | SOP |
| Node | FEGA-PT |
| Instance version | `v1.0` |

## Document History

| Template version | Instance version | Author(s) | Description of changes | Date |
| -- | -- | -- | -- | -- |
| `v2.2` | `v1.0` | Jorge Miguel Silva - BioData.pt and UAVR | Initial FEGA Portugal instance; adapted URLs and SOP links for FEGA-PT | 15-12-2025 |

## Purpose

To ensure that all public metadata submitted to Central EGA (CEGA) for a Federated EGA (FEGA) study is correct and does not contain any personally identifiable or sensitive information. This information is displayed on the EGA website and is searchable by users to enable data discovery. The FEGA Portugal Helpdesk must conduct a metadata review prior to releasing the study by using the FEGA Helpdesk Portal. After this review has been successfully completed, the FEGA Portugal Helpdesk can release the study with previous approval from the authorised submitter.

## Scope

This SOP describes how FEGA Portugal Helpdesk shall complete a metadata review for sequencing datasets submitted to CEGA by the FEGA Portugal Submitter Portal (https://submission.portugal.ega-archive.org) as part of an FEGA study and is required before the study is released.

## Procedure

**FEGA PORTUGAL NODE:**

> Note: After [SOP0017](../templates/FEGA-SOP0017_SOP_for_Federated_EGA_Helpdesk_-_Validate_a_submission.md) validation is finalized and the authorized submitter has instructed the release of the dataset, the helpdesk should execute the following steps.

**Steps to complete by the FEGA Portugal node before checking the metadata and releasing the study:**

1. *Obtain the name of the submission from the submitter for the study that they want to release.*

2. *Verify that the data files have been archived correctly.*

3. *Follow this SOP to check the metadata through the FEGA Portugal Helpdesk Portal (helpdesk.portugal.ega-archive.org) and generate the EGA accession IDs (SOP: [Validate a submission](./FEGA-PT-SOP0017_Validate_a_submission.md))*

![ ](../../docs/images/FEGA-SOP0018_image_1.png)

4. *Pre-release check of Study, DAC, and Dataset descriptions*

   *Note: Each FEGA node must have their own list of items to check. For example, the FEGA node might want to check that sample metadata does not contain any personally identifiable information. Checklists might differ between different FEGA nodes. **The FEGA Portugal node's checklist is the one that must be reviewed in this step.***

   **Metadata checks include:**

   - **Study title** should be no more than 30 words and make sense to the user.

   - **Study description** should be 3-5 sentences and should provide further details about the study (why, how, what).

   - **Dataset title** should be no more than 30 words and should make sense to the user.

   - **Dataset description** should be 2-4 sentences and should provide further unique details about the specific dataset (why, how, what).

   - **Sample report** with public information in the metadata API and a sample count (equal to the number of rows).
     - For example, view public sample attributes given a Study Accession using the following (replace EGAS number with the study of interest): `https://metadata.ega-archive.org/studies/{id}`

   > Note: To see how to query metadata go to [https://ega-archive.org/discovery/metadata/public-metadata-api/](https://ega-archive.org/discovery/metadata/public-metadata-api/)

   - **File report** with: number of files, file name, file type and check if there's any phenotypic file.
     - To check this, access the API via `https://metadata.ega-archive.org/datasets/{id}/files`, replace ID with a dataset number e.g. EGAD00001000645.

   > Note: Before accepting the submission to generate the EGA accession IDs, the FEGA Portugal Helpdesk has to either approve the DAC registration, or verify the following information of an already registered DAC. To check this, access the API via `https://metadata.ega-archive.org/datasets/{id}/dacs`, replace ID with a dataset number e.g. EGAD00001000645.

   - **Email address of DAC** must be valid and institutional.

   - **DAC main contact** must be specified for the DAC.

5. *After the check has been completed and everything is correct, the FEGA Portugal node approves the submission to publish the EGA accession IDs for the submission.*

6. *Notify the user that the check was completed, and the data is ready for release. Check with the user for a release date. After the release, the Study and Dataset IDs will be public.*

**Release Study:**

7. *Follow the SOP to [Release the requested study and dataset](./FEGA-PT-SOP0016_Release_a_FEGA_dataset.md).*

8. *Notify the DAC/authorised submitter that their study has been released and is available to view on the EGA website.*
