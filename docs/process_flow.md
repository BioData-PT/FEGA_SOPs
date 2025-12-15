# Process flow: SOP0019 request through public release

Submitter request (SOP0019) → role granting (SOP0013) → submission validation (SOP0017) → pre-release checks (SOP0018) → dataset publication (SOP0016).

```mermaid
flowchart TD
  %% Intake and account setup
  A["Submitter requests FEGA node access<br>(SOP0019 step 1)"] --> B["Node sends required info list<br>(SOP0019 step 2, Email #1)"]
  B --> C["Submitter signs DPA/agreements<br>(SOP0019 step 3)"]
  C --> D["Node confirms legal OK<br>send registration guidance<br>(SOP0019 step 3.1, Email #2)"]
  D --> E["Submitter registers CEGA account<br>CEGA validates<br>(SOP0019 step 4)"]
  E --> F["Submitter requests submitter role<br>(SOP0019 step 5)"]

  %% Role granting
  F --> G["Helpdesk grants node submitter role<br>Helpdesk Portal<br>(SOP0013)"]
  G --> H["Confirm access, send submission instructions<br>(SOP0013 step 6-7, Email #3)"]

  %% Submission work
  H --> I["Submitter builds metadata<br>Study, DAC/Policy, samples, runs, datasets<br>Uploads files<br>(Submitter Portal)"]
  I --> J["Submitter finalises submission<br>(Submitter Portal)"]

  %% Validation
  J --> K["Helpdesk validates submission<br>Pending Submissions<br>Approve/Reject<br>(SOP0017)"]
  K -->|Reject| I
  K -->|Approve| L["Accession IDs issued"]

  %% Pre-release checks
  L --> M["Submitter authorises release date<br>(SOP0018 note 1)"]
  M --> N["Helpdesk pre-release checks<br>files archived, metadata/PII checklist,<br>DAC contacts/policy<br>(SOP0018)"]
  N -->|Issues| I

  %% Publication
  N --> O["Release dataset(s)<br>Helpdesk Portal<br>(SOP0016)"]
  O --> P["Study/Dataset public on EGA site<br>(SOP0016 outcome)"]
  P --> Q["Notify submitter/DAC of release<br>(SOP0018/SOP0016 comms)"]
```
