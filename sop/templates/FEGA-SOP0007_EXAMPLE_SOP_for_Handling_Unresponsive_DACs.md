# FEGA SOP - EXAMPLE SOP for Handling Unresponsive DACs

| Metadata | Value |
| -- | -- |
| Template ID | `FEGA-SOP0007` |
| Template version | `v1.0` |
| Topic | User-facing Processes |
| SOP type | SOP |
| Node | CEGA |
| Instance version | `—` |

## Document History

| Template version | Instance version | Author(s) | Description of changes | Date |
| -- | -- | -- | -- | -- |
| `v1.0` | `—` | Giselle Kerry - EGA/EBI Helpdesk Lead and Project Coordinator | Initial release | 22-09-2020 |

## Purpose

The EGA has more than 1,000 Data Access Committees (DACs). Over time it is inevitable that some DACs may become "unresponsive", meaning that a DAC fails to communicate with a requestor within a reasonable time frame - usually two weeks. There are caveats to the two week time frame, for example during the months of July, August, and December when DAC members may be on leave. In such cases, we should make allowance for a delayed response. Where we deem a DAC to be unresponsive, EGA should be as proactive as possible in order to try and locate and communicate with the "unresponsive DAC".

## Scope

This SOP describes the steps that the Helpdesk team should take in order to work with unresponsive DACs.

## Procedure

1. On receipt of a requestor claiming that a DAC is being unresponsive, check when they last emailed the DAC. If they state it was less than two weeks ago, inform them it is our policy in the first instance to allow the DAC two weeks to reply.

2. Once the two week grace period has lapsed, the following steps should be taken:

   1. Identify all members of the unresponsive DAC using the following query:

      *\<Provide internal query or method for querying to find members of the unresponsive DAC\>*

   2. Once you have the email addresses of the DAC members, first check for activity within RT to see when the DAC members last emailed in.

      1. If you can see that they are active, you can reply to a thread and ask about a user's request to check that they have received it.

      2. If you cannot see any signs of activity, send an email through RT using **Article 855** to all of the DAC contacts and all of the Submission contacts, making sure that all of the contacts are set as "requestors". **Set a reminder** to follow up with them again in 2 weeks if you have not heard from them. Also suggest to the requestor that they send another email to the DAC at this time point.

3. If there is no response after 4 weeks since the initial request (meaning, at least two follow-ups through RT), email ega_dac_response@ebi.ac.uk to make them aware of the situation and point to all relevant correspondence, including the RT ticket number. After agreement from them, follow up with **Article 877**. Email the user to which the DAC was unresponsive and update them on progress so far, and be sure to ask if they have heard anything from the DAC.

4. If there is no response after 6 weeks since the initial request, use RT **Article 856**, set a reminder to follow-up, and update the requestor.

5. If there is no response after 8 weeks since the initial request, contact the authorised submitter(s) and their institution, organisation, or department (usually this will be a generic email address) and ask for the DAC responsibility to be reassigned. Use RT **Article 995**, set a reminder to follow up the ticket, and update the requestor.

6. If there is no response after 10 weeks since the initial request, email the legal department (or representative) and DPO of the submitter's organisation and use the following RT **Article 996**, set a reminder to follow up the ticket, and update the requestor. Also, email ega_dac_response@ebi.ac.uk informing them that an email to the institutional legal department has been sent.

7. If there is no response after 12 weeks since the initial request, email ega_dac_response@ebi.ac.uk informing about the completion of the SOP, and withdraw the dataset following the appropriate SOP. Inform the initial requester, DAC, submitter, institution and/or legal department indicating that the dataset has been withdrawn. If the dataset or study are referenced in a published paper, email the journal and inform the data is no longer available.

### Email Templates

#### Article 855

> Dear ,
>
> It has been brought to our attention that on (date) a user has made an attempt to contact you regarding an application to access the dataset(s) that fall under the governance of your DAC:
>
> (dataset accession links)
>
> Unfortunately, to date, the user states that they have not yet had a response regarding their inquiry.
>
> Can we confirm you have received such a request, and if so have you responded to the request?
>
> If you have not yet responded to the original request, can we ask that you do so at your earliest convenience?
>
> I would appreciate it if you could acknowledge receipt of this email and should you need any assistance with this process please don't hesitate to ask.
>
> Thank you.
>
> Kind regards,

#### Article 877

> Dear ,
>
> Further to my email dated (date), regarding your non-response to a user regarding an application to access the dataset/s that fall under the governance of you DAC:
>
> (dataset accessions)
>
> We have yet to have a response for you and would like to again inquire if there is anything we can do to assist you in your role as DAC contact.
>
> Apologies if the role of the DAC has not been clearly defined at the point of your submission. Please see the link below for the roles and responsibility of a DAC:
> [https://ega-archive.org/submission/data_access_committee](https://ega-archive.org/submission/data_access_committee)
>
> I have set another reminder on this ticket for two weeks time, and will contact you again to see if I can be of any further assistance.
>
> Kind regards,

#### Article 856

> Dear ,
>
> It has been brought to our attention that a user has made an attempt to contact you regarding an application to access the dataset(s) that fall under the governance of your DAC:
>
> (dataset accession links)
>
> Can I remind you that you are a contact for (Insert DAC accession), the entity responsible for governing access to the dataset(s) submitted to the EGA.
>
> The roles and responsibility of a DAC are defined here:
>
> [https://ega-archive.org/submission/data_access_committee](https://ega-archive.org/submission/data_access_committee)
>
> Please be advised, that continued failure to respond to applications may be escalated to the Journal where your study is published (insert PubMed ID), since the data is effectively unavailable, and may also result in the study being removed from the EGA website.
>
> I have set a reminder on this ticket for two weeks' time. If no response is registered, the EGA will consider proceeding with the above measures.
>
> Kind regards,

#### Article 995

> Dear ,
>
> It has been brought to our attention that a user has made an attempt to contact the DAC you assigned for your dataset \<EGADXXX\>.
>
> \<Add DAC link\>
>
> After several failed attempts to contact the DAC, we are contacting you to ask you to reassign the responsibility of the DAC, and add a new contact for the DAC that will manage the data access requests.
>
> To add a new contact of the DAC, please send us the name, Institution name, and institutional email and we will add them for you.
>
> Please be advised, that continued failure to respond to applications may be escalated to the Journal where your study is published \<insert PubMed ID\>, since the data is effectively unavailable, and may also result in the study being removed from the EGA website.
>
> I have set a reminder on this ticket for two weeks' time. If no response is registered, the EGA will proceed with the above measures.
>
> Kind regards,

#### Article 996

> Dear ,
>
> We are contacting you from the European Genome-phenome Archive (EGA). We are a service for permanent archiving and sharing of all types of personally identifiable genetic and phenotypic data resulting from biomedical research projects.
>
> Some time ago, we archived data generated by individuals employed by your Institution after entering into a Data Processing Agreement which names EGA as a Data Processor and your Institution as the Data Controller. Additionally, the submitting individuals created a Data Access Committee (DAC) whose members are responsible for reviewing and approving access requests for the data at the EGA. All data stored at EGA is controlled access data, and all data access requests must be reviewed and approved by the DAC before EGA can share it.
>
> For 10 weeks we have tried and failed to make contact with the DAC members and the submitters requesting that they respond to data access requests, effectively resulting in the archived data being unavailable for sharing. As you can appreciate, this is a major concern as the data have been published and are meant to be available to share \<PubMedID\>.
>
> Below you can find the information of the unresponsive DAC and the individuals who initially submitted the dataset.
>
> \<Add contact information DAC\>
>
> \<Add contact information submitter\>
>
> \<Add DAC link\>
>
> \<Add dataset link\>
>
> After several failed attempts to contact them, we are contacting you to request that you reassign the responsibility of the DAC to at least one individual from your Institution who has the authority to review and approve data access requests.
>
> To reassign the contact of the DAC, please send us the name, Institution name, and institutional email and we will add them for you.
>
> Please be advised that continued failure to respond to applications may result in the study being removed from the EGA website. Additional measures may be implemented, including escalation to the Journal where the EGA study is published \<insert PubMed ID\>.
>
> I have set a reminder on this ticket for two weeks' time. If no response is registered, the EGA will consider proceeding with the above measures.
>
> Kind regards,
