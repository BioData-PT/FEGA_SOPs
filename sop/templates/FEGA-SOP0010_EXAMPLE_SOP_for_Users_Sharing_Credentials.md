# FEGA SOP - EXAMPLE SOP for Users Sharing Credentials

| Metadata | Value |
| -- | -- |
| Template ID | `FEGA-SOP0010` |
| Template version | `v1.0` |
| Topic | User-facing Processes |
| SOP type | SOP |
| Node | CEGA |
| Instance version | `—` |

## Document History

| Template version | Instance version | Author(s) | Description of changes | Date |
| -- | -- | -- | -- | -- |
| `v1.0` | `—` | Dona Shaju - Helpdesk Officer | Initial release | 02-04-2020 |

## Purpose

EGA services are strictly reserved for those that hold an EGA account as detailed [here](https://ega-archive.org/download/using_ega_account). This is to ensure that only authorised users can access and download data for which access has been granted by the appropriate Data Access Committee (DAC). Adhering to this SOP will mitigate the risk of data breaches caused by unauthorised data access.

## Scope

This SOP details the procedure to follow if the Helpdesk members find cases of a user sharing credentials in order to use EGA download services. EGA accounts are assigned on an individual basis for the exclusive use of the authorised EGA account holder. Log-in details must remain private and only be used by the EGA account holder.

## Procedure

There are known cases of users sharing their data access credentials in order to use EGA services to download data. In some cases, EGA knows which authorised user account has been shared. For example, the user states in the ticket that they are using someone else's account and provides the account name. In other cases, EGA knows that an account has been shared but doesn't know which account it is. For example, a user generally states they are using someone else's account but doesn't provide the account name. These two scenarios are dealt with using the following procedures:

### Users using credentials where authorised user is unknown

1. Helpdesk officer suspects that a user is using another authorised user's credentials, but cannot confirm which authorised user's account is being used. For example, the user says they are "downloading on behalf of a colleague" a log file is supplied which doesn't contain the authorised user's account information.

2. Helpdesk officer requests that the user provide the details of the authorised account they are using. Helpdesk officer should refrain from offering further assistance until the authorised account is confirmed.

3. If the authorised account details match the original user, the Helpdesk officer proceeds with assistance following standard EGA protocols.

4. If the authorised account details do not match the original user, the Helpdesk officer follows the procedure described in the "Users sharing credentials where authorised user is known" section.

### Users sharing credentials where authorised user is known

1. Helpdesk officer identifies and confirms that a user is using another authorised user's credentials. For example, the Helpdesk officer is provided a screenshot of the user's commands or a log file and can identify the account (email address) being used is different from the user's email address on the Helpdesk ticket.

2. Helpdesk officer adds the authorised user to the RT ticket and the corresponding DAC, and replies to the original user using RT **Article XXX**, and temporarily blocks the authorised user account pending response from the DAC.

3. If the DAC responds with approval for the original user, the Helpdesk officer will:

   1. Change password on authorised account and send to authorised user (so the original user doesn't have access to the account anymore).

   2. Create a new authorised account for the original user (based on approval of DAC).

   3. Ask the original user to use their own account now, and if they continue to have issues to contact HD again.

4. If the DAC responds and doesn't approve the original user:

   1. Change password on authorised account and send to authorised user (so the original user doesn't have access to the account anymore).

   2. Inform the original user that they have not been authorised to access the data.
