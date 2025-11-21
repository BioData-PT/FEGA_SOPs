# FEGA SOP - SOP for Federated EGA Helpdesk - Grant submitter role to FEGA user using the Helpdesk Portal

| Metadata | Value |
| -- | -- |
| Template ID | `FEGA-SOP0013` |
| Template version | `v1.2` |
| Topic | SOP for Federated EGA Helpdesk |
| SOP type | SOP |
| Node | CEGA |
| Instance version | `—` |

## Document History

| Template version | Instance version | Author(s) | Description of changes | Date |
| -- | -- | -- | -- | -- |
| `v1.0` | `—` | Aina Jené - EGA-CRG Operations Manager | Initial release | 31-05-2023 |
| `v1.1` | `—` | Jorge Silva - BioData.pt and UAVR | Template alignment for GitHub publishing | 14-10-2025 |
| `v1.2` | `—` | Jorge Silva - BioData.pt and UAVR | Clarified template vs instance; minor link adjustments | 14-10-2025 |

## Purpose

This SOP describes how a FEGA Helpdesk officer can grant the submitter
role to a FEGA user via the Helpdesk Portal. This allows the user to
access the Submitter Portal for their node. If you don’t know how to get
access to your FEGA Helpdesk node for the first time, please follow
[<u>this</u>](./FEGA-SOP0014_SOP_for_Federated_EGA_Helpdesk_-_How_to_obtain_Helpdesk_role_for_the_first_time.md)
SOP.

## Scope

These instructions apply to all FEGA nodes that manage roles through the
FEGA Helpdesk Portal.

## Procedure

1.  *Ensure the user requesting submitter access has registered an EGA
    account by filling in the [<u>EGA registration
    form</u>](https://ega-archive.org/register/).*

2.  *Wait for CEGA Helpdesk to validate the account. Only validated
    accounts can be granted additional roles.*

3.  *A FEGA Helpdesk admin logs in to their FEGA Helpdesk Portal
    (`helpdesk.{fega}.ega-archive.org`) and opens the **ROLES** section.*

![ ](../../docs/images/FEGA-SOP0013_image_4.png)

4.  *Search for the user created in step 1. Make sure to enter the full
    username or email address. The suggestion box might not appear.*

![ ](../../docs/images/FEGA-SOP0013_image_2.png)

5.  *Select the submitter role for your node (`{fega} submitters`) and
    click **UPDATE ROLE** to apply the change.*

![ ](../../docs/images/FEGA-SOP0013_image_3.png)

6.  *Confirm the role assignment with the user. They can now access the
    Submitter Portal for your node.*

![ ](../../docs/images/FEGA-SOP0013_image_1.png)

7.    *Send an email to the submitter giving instructions on how to start the metadata submission on the EGA portal, following the specification of your node. If your submission portal is provided by Central EGA, you can use a similar email to the following:*

Subject: Instructions for submitting your metadata to EGA

Dear [Name],

Thank you for contacting the [Node name] FEGA helpdesk regarding your submission to the European Genome-phenome Archive (EGA).

Below you can find a short overview of how to submit your study metadata using the EGA Submitter Portal, together with official guidance materials.

1. Access the EGA Submitter Portal

* Open the EGA Submitter Portal specific to your country in your browser, e.g. [<u>https://submission.portugal.ega-archive.org/<u>](https://submission.portugal.ega-archive.org/)

2. Create a new study

* In the portal, create a new “Study” record.
* Fill in the study title, abstract/description, and relevant keywords.
* Indicate the type of study and the organism(s) as requested in the form.

3. Register Data Access Committee (DAC) and Data Access Policy

* Create or select an existing Data Access Committee that will oversee access requests.
* Create or link the appropriate Data Access Policy describing under which conditions data can be accessed and used.
* Make sure the information in the policy is consistent with your ethics approval and consent forms.

4. Add sample-level metadata

* Register all samples associated with your study (e.g. one record per individual or specimen).
* Provide the required attributes (e.g. sample ID, organism, tissue, sex, disease status, etc.) according to the EGA templates.
* Ensure that internal IDs used in your lab or project are consistently mapped to the EGA sample IDs.

5. Add experiments/runs and datasets

* Create experiment (or analysis) entries that describe how the data were generated (e.g. sequencing platform, library strategy).
* Link experiments/runs to the corresponding samples.
* Group runs/analyses into one or more “Datasets” that your DAC will control for access.

6. Validate and submit

* Use the validation options in the Submitter Portal to check for missing or inconsistent fields.
* Once the metadata pass validation, submit them for EGA curation.
* After your metadata are approved, you will receive further instructions or confirmation regarding the data file upload and finalisation of the submission.

Learning resources

* Video tutorial (step-by-step walkthrough of the portal):
  [https://www.youtube.com/watch?v=eDTNIE8Ex0g](https://www.youtube.com/watch?v=eDTNIE8Ex0g)
* EGA blog post introducing the new Submitter Portal and its main features:
  [https://blog.ega-archive.org/new-submitter-portal](https://blog.ega-archive.org/new-submitter-portal)

If you encounter any issues during the process (e.g. metadata validation errors, questions about required fields, or problems linking samples/experiments), please send us screenshots or error messages and we will be happy to assist you.

Best regards,
[Your name]
[Node name] FEGA Helpdesk
[Contact email]


8.    *
