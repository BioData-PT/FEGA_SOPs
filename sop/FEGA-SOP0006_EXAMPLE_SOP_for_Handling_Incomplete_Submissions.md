# FEGA SOP - EXAMPLE SOP for Handling Incomplete Submissions

| Metadata | Value |
| -- | -- |
| Template ID | `FEGA-SOP0006` |
| Template version | `—` |
| Topic | User-facing Processes |
| SOP type | SOP |
| Node | — |
| Instance version | `—` |

## Document History

| Template version | Instance version | Author(s) | Description of changes | Date |
| -- | -- | -- | -- | -- |
| `—` | `—` | — | Initial release | — |

<table style="width:96%;">
<colgroup>
<col style="width: 96%" />
</colgroup>
<thead>
<tr>
<th><h1 id="sop---handling-incomplete-submissions"><a
href="https://www.ebi.ac.uk/seqdb/confluence/pages/viewpage.action?pageId=13871828">SOP
-</a> Handling Incomplete Submissions</h1></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

| Document Owner | Giselle Kerry - EGA/EBI Helpdesk Lead and Project Coordinator |
|----|----|
| Version | 1.0 |
| Effective date | 22-09-2020 |
| Approvals | Dylan Spalding |
| Next revision due | 22-09-2021 |

## Purpose

**EGA Terminology**

Accessions for EGA Studies (EGAS) can be generated within the Submitter
Portal
([<u>https://ega-archive.org/submitter-portal</u>](https://ega-archive.org/submitter-portal))
prior to the data upload. This reserves the accession that can be used
for the journal publications. Dataset Accessions (EGAD) are one of the
last accessions created in a submission. Submitters would need to
complete the whole metadata submission process to receive the dataset
accession.

A **published study** at EGA is defined as a study registered at the EGA
that has been referenced in a publication usually through the study
accession (EGAS) or less frequently the dataset accession (EGAD).

An **incomplete submission** at EGA is when the study and the associated
dataset have not been released to the live EGA website
([<u>https://ega-archive.org</u>](https://ega-archive.org)), and are
therefore unavailable to search and not available to request.

It may be that components of the submission are incomplete, for example,

- No metadata has been registered

- Datasets may not have been registered

- The authorised submitter has not provided direct instruction to EGA
  Helpdesk to release the study live

## Scope

The original submitter, as part of the submission process, generates
datasets to which users then apply for access after a live release by
the Helpdesk team. In the scenario where the EGA generated accessions
have been used in a publication without prior release to the live
website end users will ask Helpdesk where the data is. The EGA Helpdesk
can identify if a study has been published or not by simply replacing
the EGASXXXXXXXXXX with the actual accession number in the URL -
[<u>https://ega-archive.org/studies/EGASXXXXXXXXXXX</u>](https://ega-archive.org/studies/EGASXXXXXXXXXXX) -
or by simply searching with the accession number in the EGA archive
search bar. In the case of an incomplete submission, the following SOP
should be followed:

## Procedure

1.  **Identify the submission account**

Identify the submission account associated with a study or dataset by
executing the following query:

*\<Provide internal query or method for querying to find the submission
account\>*

<span class="mark">Once the submission account is known, retrieve the
'Submission statements’ or ‘Submitters list' document to identify the
submission contacts.</span>

2.  **<span class="mark">Clarify the submission status</span>**

<span class="mark">Identify the current submission status through
various internal checks from the Helpdesk end. For example:</span>

- <span class="mark">Search RT for the submission account for any
  correspondence</span>

  - *<span class="mark">\<Provide internal search or method for
    searching\></span>*

- <span class="mark">Check whether data files been uploaded</span>

  - *<span class="mark">\<Provide internal query or method for
    querying\></span>*

- <span class="mark">Query databases for samples, file names, runs, or
  experiments</span>

  - *<span class="mark">\<Provide internal query or method for
    querying\></span>*

3.  **<span class="mark">Contact the authorised submitters</span>**

<span class="mark">Your contact should make clear that the study has
been published and therefore the submission should be completed as a
matter of priority. Point the submitter to the ongoing submission study
page and identify the components of the submission that need to be
completed, providing assistance where necessary. When creating the RT
ticket, please make sure that:</span>

- <span class="mark">You use “*Missing study/dataset on live*” in
  **ebi-ega-admin-keywords**</span>

- <span class="mark">You use “*Waiting on EGA action*” in
  **ebi-ega-status**</span>

- <span class="mark">You set a weekly reminder to follow up this
  submission</span>

<span class="mark">Article to use depending on the submission
process:</span>

- <span class="mark">All metadata registered, you can use RT **Article
  XXX.**</span>

- <span class="mark">Study, runs/analyses registered (no dataset), you
  can use RT **Article XXX**.</span>

<table style="width:96%;">
<colgroup>
<col style="width: 96%" />
</colgroup>
<thead>
<tr>
<th><p><mark>Dear ,</mark></p>
<p><mark>My name is XXX XXX and I am contacting you on behalf of the EGA
Helpdesk team.</mark></p>
<p><mark>It has been brought to our attention that study EGASXXXXXXX has
been included in the following publication/preprint: link</mark></p>
<p><mark>As far as I can see the submission is not completed, as the
dataset object is missing. Hence, we ask you to proceed with the
submission process and complete it so we can make your study
discoverable on our webpage.</mark></p>
<p><mark>I will be happy to assist you with anything that is
needed.</mark></p>
<p><mark>Kind regards,</mark></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- <span class="mark">Only study registered, you can use RT **Article
  XXX**.</span>

<table style="width:96%;">
<colgroup>
<col style="width: 96%" />
</colgroup>
<thead>
<tr>
<th><p><mark>Dear ,</mark></p>
<p><mark>My name is XXX XXX and I am contacting you on behalf of the EGA
Helpdesk team.</mark></p>
<p><mark>It has been brought to our attention that study EGASXXXXXXX has
been included in the following publication: link</mark></p>
<p><mark>As far as I can see only the study has been registered. Hence,
we ask you to proceed with the submission process and complete it so we
can archive your files and make your study discoverable on our
webpage.</mark></p>
<p><mark>I will be happy to assist you with anything that is
needed.</mark></p>
<p><mark>Kind regards,</mark></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span class="mark">Should the submitter team remain unresponsive or
decline the submission request (i.e. 2 failed contact attempts or more
than 3 months from the initial request), approach the corresponding
authors of the publication in a soft way, informing them about the
situation.</span>

- <span class="mark">Follow up message, you can use RT **Article
  XXX.**</span>

<table style="width:96%;">
<colgroup>
<col style="width: 96%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p><mark>Dear XXXXX,</mark></p>
<p><mark>On [insert date] we contacted you with regards to an incomplete
EGA submission, where the study accession EGASXXXXXXX is referred to in
a published paper. Could you please provide an update about the
submission process?</mark></p>
<p><mark>Thank you,</mark></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- <span class="mark">Corresponding author contact - soft way, you can
  use RT **Article XXX**</span>

<table style="width:96%;">
<colgroup>
<col style="width: 96%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p><mark>Dear XXXX,</mark></p>
<p><mark>My name is XXX XXX and I am contacting you on behalf of the EGA
Helpdesk team.</mark></p>
<p><mark>It has been brought to our attention that study EGASXXXXXXX has
been included in the following publication: link</mark></p>
<p><mark>However, the submission has not been completed and thus the
study is not discoverable on our webpage. We have contacted the
submitters responsible for this data, but the submission remains
incomplete. We can see that you are the senior author of the
publication, so we were wondering if you could please make sure that the
submission is completed as soon as possible.</mark></p>
<p><mark>I will be happy to assist you with anything that is
needed.</mark></p>
<p><mark>Kind regards,</mark></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

4.  **<span class="mark">Unresponsive submitters/authors</span>**

<span class="mark">If no response is received by the submission team or
authors (after 3 communications), escalate the situation to the EGA
management team (using the appropriate mailing list) and inform them of
the situation. Summarise the RT ticket and ask permission to contact the
corresponding Journal. In case that senior authors are personally known
by someone at EGA, a high level intervention may be the best way
forward. Only after this has failed would journals be notified.</span>

<span class="mark">If accepted by the EGA management team, warn the
submitter team and the publication authors about the imminent contact
with the Journal by using RT **Article XXX.**</span>
