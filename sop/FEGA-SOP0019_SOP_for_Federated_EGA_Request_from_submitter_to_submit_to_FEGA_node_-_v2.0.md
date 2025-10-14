# FEGA SOP - SOP for Federated EGA Helpdesk - FEGA Request from submitter to submit to FEGA node

| Metadata | Value |
| -- | -- |
| Template ID | `FEGA-SOP0019` |
| Template version | `v1.2` |
| Topic | SOP for Federated EGA Helpdesk |
| SOP type | SOP |
| Node | CEGA |
| Instance version | `—` |

## Document Overview

| Field | Value |
| -- | -- |
| Document Owner | Aina Jené - EGA-CRG Operations Manager |
| Version | 1.1 |
| Effective date | 31-05-2023 |

## Document History

| Template version | Instance version | Author(s) | Description of changes | Date |
| -- | -- | -- | -- | -- |
| `v1.0` | `—` | Aina Jené - EGA-CRG Operations Manager | Initial release | 31-05-2023 |
| `v1.1` | `—` | Jorge Silva - BioData.pt and UAVR | Template alignment for GitHub publishing | 14-10-2025 |
| `v1.2` | `—` | Jorge Silva - BioData.pt and UAVR | Clarified template vs instance; minor link adjustments | 14-10-2025 |

## Purpose

Provide helpdesk officers with a repeatable process to onboard submitters
requesting access to a FEGA node so that they can begin metadata and data
submissions.

## Scope

Use this SOP whenever a submitter completes the node-specific legal
arrangements (for example, a Data Processing Agreement) and requests
access to submit data through the FEGA pipelines. This SOP covers the
steps handled via the FEGA Helpdesk Portal until the submitter can log in
to the Submitter Portal for the node.

## Procedure

1.  The submitter contacts your FEGA helpdesk requesting access to submit
    to your node.

2.  Provide the submitter with the list of information required by your
    FEGA node to progress the request. *(Email template \#1 can be
    adapted)*.

3.  The submitter signs and returns the Data Processing Agreement and any
    related agreements required by your node.

    1.  Once legal approval is confirmed, send the registration guidance
        email. *(Email template \#2 can be adapted).*

4.  The submitter creates an account on the CEGA website, which CEGA will
    validate as part of their standard onboarding process.

5.  After the CEGA account is validated, the submitter contacts your FEGA
    helpdesk requesting the submitter role for your node.

6.  A helpdesk admin grants the submitter role to the user by following
    the SOP
    [Grant submitter role to FEGA user using the Helpdesk Portal](./FEGA-SOP0013_SOP_for_Federated_EGA_Helpdesk_-_Grant_submitter_role_to_FEGA_user_using_the_Helpdesk_Portal.md).

7.  Once the role is assigned, confirm to the user that they can now log
    into the Submitter Portal for your node and begin the submission.

    1.  *(Optional)* Send a confirmation email using template \#3.

#### Complete workflow

![ ](../docs/images/FEGA-SOP0019_image_1.png)

### Email Template \#1 - First set of information for new submitters

**Subject:** Guidance for submission to FEGA {node name}

Dear [Recipient Name],

Thank you for reaching out to our Helpdesk. We are happy to assist you with the process of uploading data into FEGA {node name}. To get started, please provide the following details:

1. **Legal and ethical compliance**

   - Contact your institution's Data Protection Officer (DPO).
   - Ensure the relevant ethics committee approval documents are ready for submission.
   - Completing the Data Processing Agreement (DPA) with FEGA {node name} is required.
   - While the DPO handles the legal tasks, we can already advance the technical steps.

2. **Data information**

   - Confirm the file types you will submit (for example FASTQ, BAM or VCF).
   - Provide an estimate of your total data volume (in GB or TB).

3. **Technical capabilities**

   - Let us know if you or your team have experience using the terminal or command-line tools.
   - Indicate whether a bioinformatician or IT specialist is available to assist with the uploads.

4. **Metadata requirements**

   - Let us know which metadata templates or guidance you require.
   - This typically includes sample information, study details, file descriptions and methodologies.

If you have any questions or need clarification, please let us know and we will happily guide you through the process.

Warm regards,

[Your Name]  \
[Helpdesk Team]  \
[Contact Information]

### Email Template \#2 - Account registration

**Subject:** Register in EGA

Dear [Recipient Name],

Thank you for providing your documentation. We are glad to inform you that the DPA was approved and we can now proceed with the next phase of the submission.

- If you are not yet registered in EGA, please do so at [https://ega-archive.org/register/](https://ega-archive.org/register/) so that you can upload the metadata for your submission.
- If you are already registered, please confirm the email address used for your registration so that FEGA {node name} can add you as a submitter.
- If you do not remember the registration email, visit [https://profile.ega-archive.org/](https://profile.ega-archive.org/).

Warm regards,

[Your Name]  \
[Helpdesk Team]  \
[Contact Information]

### Email Template \#3 - Confirmation of submitter access

**Subject:** Submitter role activated for FEGA {node name} - data submission

Dear [Recipient Name],

We are pleased to let you know that you have been assigned the FEGA {node name} submitter role.

You can now begin completing the metadata and uploading your data. Go to `https://submission.{fega}.ega-archive.org` and follow the guidance provided by your node.

Please inform us once you have completed these steps.

Warm regards,

[Your Name]  \
[Helpdesk Team]  \
[Contact Information]
