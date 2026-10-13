# Proposal Protected Calls

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/proposal-protected-calls/` | [List Proposal Protected Calls](#list-proposal-protected-calls) |
| <span class="http-badge http-get">GET</span> | `/api/proposal-protected-calls/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/proposal-protected-calls/` | [Create](#create) |
| <span class="http-badge http-post">POST</span> | `/api/proposal-protected-calls/{uuid}/create-manual-assignment/` | [Create manual assignment](#create-manual-assignment) |
| <span class="http-badge http-put">PUT</span> | `/api/proposal-protected-calls/{uuid}/` | [Update](#update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/proposal-protected-calls/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-delete">DELETE</span> | `/api/proposal-protected-calls/{uuid}/` | [Delete](#delete) |
| **Permissions & Users** | | |
| <span class="http-badge http-get">GET</span> | `/api/proposal-protected-calls/{uuid}/list_users/` | [List users and their roles in a scope](#list-users-and-their-roles-in-a-scope) |
| <span class="http-badge http-post">POST</span> | `/api/proposal-protected-calls/{uuid}/add_user/` | [Grant a role to a user](#grant-a-role-to-a-user) |
| <span class="http-badge http-post">POST</span> | `/api/proposal-protected-calls/{uuid}/delete_user/` | [Revoke a role from a user](#revoke-a-role-from-a-user) |
| <span class="http-badge http-post">POST</span> | `/api/proposal-protected-calls/{uuid}/update_user/` | [Update a user's role expiration](#update-a-users-role-expiration) |
| **Other Actions** | | |
| <span class="http-badge http-get">GET</span> | `/api/proposal-protected-calls/{uuid}/affinity-matrix/` | [Get affinity matrix for reviewer-proposal matching](#get-affinity-matrix-for-reviewer-proposal-matching) |
| <span class="http-badge http-get">GET</span> | `/api/proposal-protected-calls/available_compliance_checklists/` | [Get available compliance checklists for call creation/editing](#get-available-compliance-checklists-for-call-creationediting) |
| <span class="http-badge http-get">GET</span> | `/api/proposal-protected-calls/{uuid}/coi-configuration/` | [Get COI configuration for this call](#get-coi-configuration-for-this-call) |
| <span class="http-badge http-get">GET</span> | `/api/proposal-protected-calls/{uuid}/compliance_overview/` | [Compliance overview](#compliance-overview) |
| <span class="http-badge http-get">GET</span> | `/api/proposal-protected-calls/{uuid}/conflict-summary/` | [Get summary statistics of conflicts for this call](#get-summary-statistics-of-conflicts-for-this-call) |
| <span class="http-badge http-get">GET</span> | `/api/proposal-protected-calls/{uuid}/conflicts/` | [List all conflicts of interest detected for this call](#list-all-conflicts-of-interest-detected-for-this-call) |
| <span class="http-badge http-get">GET</span> | `/api/proposal-protected-calls/dashboard-stats/` | [Get call manager dashboard stats](#get-call-manager-dashboard-stats) |
| <span class="http-badge http-get">GET</span> | `/api/proposal-protected-calls/{uuid}/export-proposals/` | [Export proposals](#export-proposals) |
| <span class="http-badge http-get">GET</span> | `/api/proposal-protected-calls/{uuid}/export-reviews/` | [Export reviews](#export-reviews) |
| <span class="http-badge http-get">GET</span> | `/api/proposal-protected-calls/{uuid}/matching-configuration/` | [Get or update matching configuration for this call](#get-or-update-matching-configuration-for-this-call) |
| <span class="http-badge http-get">GET</span> | `/api/proposal-protected-calls/{uuid}/offerings/` | [List offerings for a call](#list-offerings-for-a-call) |
| <span class="http-badge http-get">GET</span> | `/api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-get">GET</span> | `/api/proposal-protected-calls/{uuid}/proposals/{proposal_uuid}/compliance-answers/` | [Get detailed compliance answers for a specific proposal (call managers only)](#get-detailed-compliance-answers-for-a-specific-proposal-call-managers-only) |
| <span class="http-badge http-get">GET</span> | `/api/proposal-protected-calls/{uuid}/proposed-assignments/` | [Get proposed reviewer-proposal assignments](#get-proposed-reviewer-proposal-assignments) |
| <span class="http-badge http-get">GET</span> | `/api/proposal-protected-calls/{uuid}/resource_templates/` | [List resource templates for a call](#list-resource-templates-for-a-call) |
| <span class="http-badge http-get">GET</span> | `/api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-get">GET</span> | `/api/proposal-protected-calls/{uuid}/reviewer-pool/` | [List reviewer pool members for a call](#list-reviewer-pool-members-for-a-call) |
| <span class="http-badge http-get">GET</span> | `/api/proposal-protected-calls/{uuid}/rounds/` | [List rounds for a call](#list-rounds-for-a-call) |
| <span class="http-badge http-get">GET</span> | `/api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-get">GET</span> | `/api/proposal-protected-calls/step_checklists/` | [Step checklists](#step-checklists) |
| <span class="http-badge http-get">GET</span> | `/api/proposal-protected-calls/{uuid}/suggestions/` | [List all reviewer suggestions for this call with affinity scores](#list-all-reviewer-suggestions-for-this-call-with-affinity-scores) |
| <span class="http-badge http-get">GET</span> | `/api/proposal-protected-calls/{uuid}/workflow_steps/` | [List workflow steps for a call](#list-workflow-steps-for-a-call) |
| <span class="http-badge http-get">GET</span> | `/api/proposal-protected-calls/{uuid}/workflow_steps/{obj_uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/proposal-protected-calls/{uuid}/activate/` | [Activate a call](#activate-a-call) |
| <span class="http-badge http-post">POST</span> | `/api/proposal-protected-calls/{uuid}/archive/` | [Archive a call](#archive-a-call) |
| <span class="http-badge http-post">POST</span> | `/api/proposal-protected-calls/{uuid}/attach_documents/` | [Attach documents to call](#attach-documents-to-call) |
| <span class="http-badge http-post">POST</span> | `/api/proposal-protected-calls/{uuid}/compute-affinities/` | [Compute affinity scores for all reviewer-proposal pairs](#compute-affinity-scores-for-all-reviewer-proposal-pairs) |
| <span class="http-badge http-post">POST</span> | `/api/proposal-protected-calls/{uuid}/detach_documents/` | [Detach documents from call](#detach-documents-from-call) |
| <span class="http-badge http-post">POST</span> | `/api/proposal-protected-calls/{uuid}/detect-conflicts/` | [Trigger automated COI detection for all reviewer-proposal pairs](#trigger-automated-coi-detection-for-all-reviewer-proposal-pairs) |
| <span class="http-badge http-post">POST</span> | `/api/proposal-protected-calls/{uuid}/duplicate/` | [Duplicate](#duplicate) |
| <span class="http-badge http-post">POST</span> | `/api/proposal-protected-calls/{uuid}/export_call/` | [Export call configuration](#export-call-configuration) |
| <span class="http-badge http-post">POST</span> | `/api/proposal-protected-calls/{uuid}/generate-assignments/` | [Generate assignments](#generate-assignments) |
| <span class="http-badge http-post">POST</span> | `/api/proposal-protected-calls/{uuid}/generate-suggestions/` | [Generate reviewer suggestions with configurable matching source](#generate-reviewer-suggestions-with-configurable-matching-source) |
| <span class="http-badge http-post">POST</span> | `/api/proposal-protected-calls/import_call/` | [Import call configuration](#import-call-configuration) |
| <span class="http-badge http-post">POST</span> | `/api/proposal-protected-calls/{uuid}/invite-by-email/` | [Invite by email](#invite-by-email) |
| <span class="http-badge http-post">POST</span> | `/api/proposal-protected-calls/{uuid}/reviewer-pool/` | [Invite reviewers to join the call's reviewer pool](#invite-reviewers-to-join-the-calls-reviewer-pool) |
| <span class="http-badge http-post">POST</span> | `/api/proposal-protected-calls/{uuid}/offerings/` | [Create offering for a call](#create-offering-for-a-call) |
| <span class="http-badge http-post">POST</span> | `/api/proposal-protected-calls/{uuid}/resource_templates/` | [Create resource template for a call](#create-resource-template-for-a-call) |
| <span class="http-badge http-post">POST</span> | `/api/proposal-protected-calls/{uuid}/review_proposal_compliance/` | [Mark proposal compliance as reviewed by call manager](#mark-proposal-compliance-as-reviewed-by-call-manager) |
| <span class="http-badge http-post">POST</span> | `/api/proposal-protected-calls/{uuid}/rounds-bulk-set/` | [Rounds bulk set](#rounds-bulk-set) |
| <span class="http-badge http-post">POST</span> | `/api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/close/` | [Close](#close) |
| <span class="http-badge http-post">POST</span> | `/api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/complete/` | [Complete](#complete) |
| <span class="http-badge http-post">POST</span> | `/api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/publish_results/` | [Publish results](#publish-results) |
| <span class="http-badge http-post">POST</span> | `/api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/record_adoption/` | [Record adoption](#record-adoption) |
| <span class="http-badge http-post">POST</span> | `/api/proposal-protected-calls/{uuid}/rounds/` | [Create a round for a call](#create-a-round-for-a-call) |
| <span class="http-badge http-post">POST</span> | `/api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/start_deciding/` | [Start deciding](#start-deciding) |
| <span class="http-badge http-post">POST</span> | `/api/proposal-protected-calls/{uuid}/send-all-assignments/` | [Send all draft assignment batches for this call](#send-all-draft-assignment-batches-for-this-call) |
| <span class="http-badge http-post">POST</span> | `/api/proposal-protected-calls/{uuid}/send-invitations/` | [Send invitations to all confirmed suggestions](#send-invitations-to-all-confirmed-suggestions) |
| <span class="http-badge http-post">POST</span> | `/api/proposal-protected-calls/{uuid}/workflow_steps/` | [Create or update a workflow step for a call](#create-or-update-a-workflow-step-for-a-call) |
| <span class="http-badge http-put">PUT</span> | `/api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/` | [Update](#update) |
| <span class="http-badge http-put">PUT</span> | `/api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/` | [Update](#update) |
| <span class="http-badge http-put">PUT</span> | `/api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/` | [Update](#update) |
| <span class="http-badge http-put">PUT</span> | `/api/proposal-protected-calls/{uuid}/workflow_steps/{obj_uuid}/` | [Update](#update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/proposal-protected-calls/{uuid}/coi-configuration/` | [Get COI configuration for this call](#get-coi-configuration-for-this-call) |
| <span class="http-badge http-patch">PATCH</span> | `/api/proposal-protected-calls/{uuid}/matching-configuration/` | [Get or update matching configuration for this call](#get-or-update-matching-configuration-for-this-call) |
| <span class="http-badge http-patch">PATCH</span> | `/api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/proposal-protected-calls/{uuid}/workflow_steps/{obj_uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-delete">DELETE</span> | `/api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/` | [Delete](#delete) |
| <span class="http-badge http-delete">DELETE</span> | `/api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/` | [Delete](#delete) |
| <span class="http-badge http-delete">DELETE</span> | `/api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/` | [Delete](#delete) |
| <span class="http-badge http-delete">DELETE</span> | `/api/proposal-protected-calls/{uuid}/workflow_steps/{obj_uuid}/` | [Delete](#delete) |

---
## Core CRUD


### List Proposal Protected Calls


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/proposal-protected-calls/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.call_states import CallStates # (1)
    from waldur_api_client.models.protected_call_field_enum import ProtectedCallFieldEnum # (2)
    from waldur_api_client.models.protected_call_o_enum import ProtectedCallOEnum # (3)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_list # (4)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`CallStates`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/call_states.py)
    2.  **Model Source:** [`ProtectedCallFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/protected_call_field_enum.py)
    3.  **Model Source:** [`ProtectedCallOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/protected_call_o_enum.py)
    4.  **API Source:** [`proposal_protected_calls_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_list.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsList } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsList({
      auth: "Token YOUR_API_TOKEN"
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Query Parameters"

    | Name | Type | Description |
    |---|---|---|
    | `customer` | string (uri) |  |
    | `customer_keyword` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `field` | array |  |
    | `has_active_round` | boolean |  |
    | `name` | string |  |
    | `o` | array | Ordering<br><br> |
    | `offering_uuid` | string (uuid) |  |
    | `offerings_provider_uuid` | string (uuid) |  |
    | `open_for_offering_uuid` | string (uuid) | Calls the offering can be requested through right now |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `slug` | string | Slug |
    | `state` | array |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `start_date` | string (date-time) |  |
    | `end_date` | string (date-time) |  |
    | `slug` | string | URL-friendly identifier. Only editable by staff users. |
    | `name` | string |  |
    | `description` | string |  |
    | `state` | any |  |
    | `manager` | string (uri) |  |
    | `manager_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `offerings` | array of objects |  |
    | `offerings.uuid` | string (uuid) |  |
    | `offerings.state` | any |  |
    | `offerings.offering` | string (uri) |  |
    | `offerings.offering_name` | string |  |
    | `offerings.offering_uuid` | string (uuid) |  |
    | `offerings.offering_type` | string |  |
    | `offerings.provider_name` | string |  |
    | `offerings.category_uuid` | string (uuid) |  |
    | `offerings.category_name` | string |  |
    | `offerings.call_managing_organisation` | string |  |
    | `offerings.attributes` | object (free-form) |  |
    | `offerings.plan` | string (uri) |  |
    | `offerings.plan_details` | any |  |
    | `offerings.options` | any |  |
    | `offerings.components` | array of objects |  |
    | `offerings.components.uuid` | string (uuid) |  |
    | `offerings.components.offering_uuid` | string (uuid) |  |
    | `offerings.components.billing_type` | string | <br>_Enum: `fixed`, `usage`, `limit`, `one`, `few`_ |
    | `offerings.components.type` | string | Unique internal name of the measured unit, for example floating_ip. |
    | `offerings.components.name` | string | Display name for the measured unit, for example, Floating IP. |
    | `offerings.components.description` | string |  |
    | `offerings.components.measured_unit` | string | Unit of measurement, for example, GB. |
    | `offerings.components.unit_factor` | integer | The conversion factor from backend units to measured_unit |
    | `offerings.components.limit_period` | any |  |
    | `offerings.components.limit_amount` | number (double) |  |
    | `offerings.components.limit_decimal_places` | integer | Number of decimal places accepted for this component's limit. 0 keeps the limit integer-only. |
    | `offerings.components.article_code` | string |  |
    | `offerings.components.max_value` | number (double) |  |
    | `offerings.components.min_value` | number (double) |  |
    | `offerings.components.max_available_limit` | number (double) |  |
    | `offerings.components.is_boolean` | boolean |  |
    | `offerings.components.default_limit` | number (double) |  |
    | `offerings.components.factor` | integer |  |
    | `offerings.components.is_builtin` | boolean | The API's older name for ``billed_per_plan``.  It used to ask the plugin registry whether this component's type is one the plugin declares, which left out the OpenStack per-volume-type quotas: they are created by the volume type sync rather than declared, so the API called them provider components while the billing resolver treated them as builtin. Reading the stored flag makes the two agree. |
    | `offerings.components.is_prepaid` | boolean |  |
    | `offerings.components.overage_component` | string (uuid) |  |
    | `offerings.components.min_prepaid_duration` | integer |  |
    | `offerings.components.max_prepaid_duration` | integer |  |
    | `offerings.components.prepaid_duration_step` | integer | Step size in months for the initial prepaid duration at order creation. If set, only multiples of this value (starting from min_prepaid_duration) are valid. Defaults to 1 (any value between min and max). |
    | `offerings.components.min_renewal_duration` | integer | Minimum number of months allowed for a renewal. |
    | `offerings.components.max_renewal_duration` | integer | Maximum number of months allowed for a renewal. |
    | `offerings.components.renewal_duration_step` | integer | Step size in months for renewal. Only multiples of this value (starting from min_renewal_duration) are valid. Defaults to 1. |
    | `offerings.require_purchase_order` | boolean | Whether a purchase order must accompany a resource request for this offering before the proposal can be submitted. Defaults to the offering's require_purchase_order_upload, and stays under the call manager's control afterwards. |
    | `offerings.created` | string (date-time) |  |
    | `rounds` | array of objects |  |
    | `rounds.uuid` | string (uuid) |  |
    | `rounds.slug` | string |  |
    | `rounds.name` | string |  |
    | `rounds.start_time` | string (date-time) |  |
    | `rounds.cutoff_time` | string (date-time) |  |
    | `rounds.status` | any |  |
    | `rounds.allocation_date` | string (date-time) |  |
    | `rounds.review_duration_in_days` | integer |  |
    | `rounds.lifecycle_state` | any | Where the round stands after its cut-off: evaluating, deciding, results_published or closed. Empty before the cut-off. |
    | `rounds.evaluation_started_at` | string (date-time) |  |
    | `rounds.deciding_started_at` | string (date-time) |  |
    | `rounds.results_published_at` | string (date-time) |  |
    | `rounds.closed_at` | string (date-time) |  |
    | `documents` | array of objects |  |
    | `documents.uuid` | string (uuid) |  |
    | `documents.file` | string (uri) | Documentation for call for proposals. |
    | `documents.file_name` | string |  |
    | `documents.file_size` | integer |  |
    | `documents.description` | string |  |
    | `documents.created` | string (date-time) |  |
    | `resource_templates` | array of objects |  |
    | `resource_templates.uuid` | string (uuid) |  |
    | `resource_templates.url` | string |  |
    | `resource_templates.name` | string |  |
    | `resource_templates.description` | string |  |
    | `resource_templates.attributes` | object (free-form) |  |
    | `resource_templates.limits` | object (free-form) |  |
    | `resource_templates.is_required` | boolean | If True, every proposal must include this resource type |
    | `resource_templates.requested_offering` | string (uri) |  |
    | `resource_templates.requested_offering_name` | string |  |
    | `resource_templates.requested_offering_uuid` | string (uuid) |  |
    | `resource_templates.requested_offering_plan` | any |  |
    | `resource_templates.requested_offering_type` | string |  |
    | `resource_templates.requested_offering_components` | array of objects |  |
    | `resource_templates.requested_offering_components.uuid` | string (uuid) |  |
    | `resource_templates.requested_offering_components.offering_uuid` | string (uuid) |  |
    | `resource_templates.requested_offering_components.billing_type` | string | <br>_Enum: `fixed`, `usage`, `limit`, `one`, `few`_ |
    | `resource_templates.requested_offering_components.type` | string | Unique internal name of the measured unit, for example floating_ip. |
    | `resource_templates.requested_offering_components.name` | string | Display name for the measured unit, for example, Floating IP. |
    | `resource_templates.requested_offering_components.description` | string |  |
    | `resource_templates.requested_offering_components.measured_unit` | string | Unit of measurement, for example, GB. |
    | `resource_templates.requested_offering_components.unit_factor` | integer | The conversion factor from backend units to measured_unit |
    | `resource_templates.requested_offering_components.limit_period` | any |  |
    | `resource_templates.requested_offering_components.limit_amount` | number (double) |  |
    | `resource_templates.requested_offering_components.limit_decimal_places` | integer | Number of decimal places accepted for this component's limit. 0 keeps the limit integer-only. |
    | `resource_templates.requested_offering_components.article_code` | string |  |
    | `resource_templates.requested_offering_components.max_value` | number (double) |  |
    | `resource_templates.requested_offering_components.min_value` | number (double) |  |
    | `resource_templates.requested_offering_components.max_available_limit` | number (double) |  |
    | `resource_templates.requested_offering_components.is_boolean` | boolean |  |
    | `resource_templates.requested_offering_components.default_limit` | number (double) |  |
    | `resource_templates.requested_offering_components.factor` | integer |  |
    | `resource_templates.requested_offering_components.is_builtin` | boolean | The API's older name for ``billed_per_plan``.  It used to ask the plugin registry whether this component's type is one the plugin declares, which left out the OpenStack per-volume-type quotas: they are created by the volume type sync rather than declared, so the API called them provider components while the billing resolver treated them as builtin. Reading the stored flag makes the two agree. |
    | `resource_templates.requested_offering_components.is_prepaid` | boolean |  |
    | `resource_templates.requested_offering_components.overage_component` | string (uuid) |  |
    | `resource_templates.requested_offering_components.min_prepaid_duration` | integer |  |
    | `resource_templates.requested_offering_components.max_prepaid_duration` | integer |  |
    | `resource_templates.requested_offering_components.prepaid_duration_step` | integer | Step size in months for the initial prepaid duration at order creation. If set, only multiples of this value (starting from min_prepaid_duration) are valid. Defaults to 1 (any value between min and max). |
    | `resource_templates.requested_offering_components.min_renewal_duration` | integer | Minimum number of months allowed for a renewal. |
    | `resource_templates.requested_offering_components.max_renewal_duration` | integer | Maximum number of months allowed for a renewal. |
    | `resource_templates.requested_offering_components.renewal_duration_step` | integer | Step size in months for renewal. Only multiples of this value (starting from min_renewal_duration) are valid. Defaults to 1. |
    | `resource_templates.created_by` | string (uri) |  |
    | `resource_templates.created_by_name` | string |  |
    | `resource_templates.created` | string (date-time) |  |
    | `fixed_duration_in_days` | integer |  |
    | `max_prepaid_duration_months` | integer | The longest prepaid subscription, in whole months, that fits inside fixed_duration_in_days measured from today; null when the call fixes no duration. |
    | `backend_id` | string |  |
    | `external_url` | string (uri) |  |
    | `reviewer_identity_visible_to_submitters` | boolean | Whether proposal applicants can see reviewer identities |
    | `reviews_visible_to_submitters` | boolean | Whether proposal applicants can see review comments and scores |
    | `has_eligibility_restrictions` | boolean | Check if call has any eligibility restrictions configured. |
    | `proposal_field_config` | object |  |
    | `proposal_field_config.field_project_summary` | string | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_config.field_description` | string | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_config.field_science_sub_domain` | string | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_config.field_supporting_documentation` | string | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `evaluation_start` | any | When a submitted proposal's evaluation starts: on submission, or for all proposals of a round together at its cut-off. Cannot be changed while the call has proposals submitted or in review. |
    | `publish_results` | any | When applicants learn the allocation decision: immediately, or for every proposal of a round together when a call manager publishes the round's results. Cannot be changed while decisions are held. |
    | `created_by` | string (uri) |  |
    | `reference_code` | string |  |
    | `compliance_checklist` | string (uuid) | Compliance checklist that proposals must complete before submission |
    | `compliance_checklist_name` | string |  |
    | `panel_chair` | string (uuid) |  |
    | `panel_chair_uuid` | string (uuid) |  |
    | `panel_chair_name` | string |  |
    | `proposal_slug_template` | string | Template for proposal slugs. Supports: {call_slug}, {round_slug}, {org_slug}, {year}, {month}, {counter}, {counter_padded}. Default: {round_slug}-{counter_padded} |
    | `user_email_patterns` | array of strings | List of email regex patterns. User must match one. |
    | `user_affiliations` | array of strings | List of allowed affiliations. User must have one. |
    | `user_identity_sources` | array of strings | List of allowed identity sources (identity providers). |
    | `user_nationalities` | array of strings | List of allowed nationality codes (ISO 3166-1 alpha-2). User must have one. |
    | `user_organization_types` | array of strings | List of allowed organization type URNs (SCHAC). User must match one. |
    | `user_assurance_levels` | array of strings | List of required assurance URIs (REFEDS). User must have ALL of these. |
    | `applicant_visibility_config` | any |  |
    | `proposal_field_metadata` | array of objects | Per-field state, permitted transitions and downstream consumers for the Project details step. |
    | `proposal_field_metadata.field` | string |  |
    | `proposal_field_metadata.state` | string | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_metadata.allowed_states` | array of strings |  |
    | `proposal_field_metadata.locked_reason` | string |  |
    | `proposal_field_metadata.usage` | array of strings |  |
    | `has_proposals` | boolean | Whether any proposal has been submitted to this call. Used by the frontend to gate slug-template and checklist fields. |
    | `order_author` | any | Whose name the orders for resources granted by this call carry. |
    | `order_author_user` | string (uuid) | The person orders are attributed to when the author is a named contact. Must hold a role on this call or on the organisation managing it. |
    | `order_author_user_uuid` | string (uuid) |  |
    | `order_author_user_name` | string |  |
    | `carry_over_drafts` | boolean | Whether a draft still open when its round's cut-off passes moves on to the call's next round instead of being cancelled. Without a later round the draft is cancelled either way. |
    | `undecided_at_round_completion` | any | What completing a round does with its proposals that still have no decision: refuse to complete the round, or reject them. A round may override it. |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.protected_call_field_enum import ProtectedCallFieldEnum # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_retrieve # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ProtectedCallFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/protected_call_field_enum.py)
    2.  **API Source:** [`proposal_protected_calls_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_retrieve.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsRetrieve({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Query Parameters"

    | Name | Type |
    |---|---|
    | `field` | array |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `start_date` | string (date-time) |  |
    | `end_date` | string (date-time) |  |
    | `slug` | string | URL-friendly identifier. Only editable by staff users. |
    | `name` | string |  |
    | `description` | string |  |
    | `state` | any |  |
    | `manager` | string (uri) |  |
    | `manager_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `offerings` | array of objects |  |
    | `offerings.uuid` | string (uuid) |  |
    | `offerings.state` | any |  |
    | `offerings.offering` | string (uri) |  |
    | `offerings.offering_name` | string |  |
    | `offerings.offering_uuid` | string (uuid) |  |
    | `offerings.offering_type` | string |  |
    | `offerings.provider_name` | string |  |
    | `offerings.category_uuid` | string (uuid) |  |
    | `offerings.category_name` | string |  |
    | `offerings.call_managing_organisation` | string |  |
    | `offerings.attributes` | object (free-form) |  |
    | `offerings.plan` | string (uri) |  |
    | `offerings.plan_details` | any |  |
    | `offerings.options` | any |  |
    | `offerings.components` | array of objects |  |
    | `offerings.components.uuid` | string (uuid) |  |
    | `offerings.components.offering_uuid` | string (uuid) |  |
    | `offerings.components.billing_type` | string | <br>_Enum: `fixed`, `usage`, `limit`, `one`, `few`_ |
    | `offerings.components.type` | string | Unique internal name of the measured unit, for example floating_ip. |
    | `offerings.components.name` | string | Display name for the measured unit, for example, Floating IP. |
    | `offerings.components.description` | string |  |
    | `offerings.components.measured_unit` | string | Unit of measurement, for example, GB. |
    | `offerings.components.unit_factor` | integer | The conversion factor from backend units to measured_unit |
    | `offerings.components.limit_period` | any |  |
    | `offerings.components.limit_amount` | number (double) |  |
    | `offerings.components.limit_decimal_places` | integer | Number of decimal places accepted for this component's limit. 0 keeps the limit integer-only. |
    | `offerings.components.article_code` | string |  |
    | `offerings.components.max_value` | number (double) |  |
    | `offerings.components.min_value` | number (double) |  |
    | `offerings.components.max_available_limit` | number (double) |  |
    | `offerings.components.is_boolean` | boolean |  |
    | `offerings.components.default_limit` | number (double) |  |
    | `offerings.components.factor` | integer |  |
    | `offerings.components.is_builtin` | boolean | The API's older name for ``billed_per_plan``.  It used to ask the plugin registry whether this component's type is one the plugin declares, which left out the OpenStack per-volume-type quotas: they are created by the volume type sync rather than declared, so the API called them provider components while the billing resolver treated them as builtin. Reading the stored flag makes the two agree. |
    | `offerings.components.is_prepaid` | boolean |  |
    | `offerings.components.overage_component` | string (uuid) |  |
    | `offerings.components.min_prepaid_duration` | integer |  |
    | `offerings.components.max_prepaid_duration` | integer |  |
    | `offerings.components.prepaid_duration_step` | integer | Step size in months for the initial prepaid duration at order creation. If set, only multiples of this value (starting from min_prepaid_duration) are valid. Defaults to 1 (any value between min and max). |
    | `offerings.components.min_renewal_duration` | integer | Minimum number of months allowed for a renewal. |
    | `offerings.components.max_renewal_duration` | integer | Maximum number of months allowed for a renewal. |
    | `offerings.components.renewal_duration_step` | integer | Step size in months for renewal. Only multiples of this value (starting from min_renewal_duration) are valid. Defaults to 1. |
    | `offerings.require_purchase_order` | boolean | Whether a purchase order must accompany a resource request for this offering before the proposal can be submitted. Defaults to the offering's require_purchase_order_upload, and stays under the call manager's control afterwards. |
    | `offerings.created` | string (date-time) |  |
    | `rounds` | array of objects |  |
    | `rounds.uuid` | string (uuid) |  |
    | `rounds.slug` | string |  |
    | `rounds.name` | string |  |
    | `rounds.start_time` | string (date-time) |  |
    | `rounds.cutoff_time` | string (date-time) |  |
    | `rounds.status` | any |  |
    | `rounds.allocation_date` | string (date-time) |  |
    | `rounds.review_duration_in_days` | integer |  |
    | `rounds.lifecycle_state` | any | Where the round stands after its cut-off: evaluating, deciding, results_published or closed. Empty before the cut-off. |
    | `rounds.evaluation_started_at` | string (date-time) |  |
    | `rounds.deciding_started_at` | string (date-time) |  |
    | `rounds.results_published_at` | string (date-time) |  |
    | `rounds.closed_at` | string (date-time) |  |
    | `documents` | array of objects |  |
    | `documents.uuid` | string (uuid) |  |
    | `documents.file` | string (uri) | Documentation for call for proposals. |
    | `documents.file_name` | string |  |
    | `documents.file_size` | integer |  |
    | `documents.description` | string |  |
    | `documents.created` | string (date-time) |  |
    | `resource_templates` | array of objects |  |
    | `resource_templates.uuid` | string (uuid) |  |
    | `resource_templates.url` | string |  |
    | `resource_templates.name` | string |  |
    | `resource_templates.description` | string |  |
    | `resource_templates.attributes` | object (free-form) |  |
    | `resource_templates.limits` | object (free-form) |  |
    | `resource_templates.is_required` | boolean | If True, every proposal must include this resource type |
    | `resource_templates.requested_offering` | string (uri) |  |
    | `resource_templates.requested_offering_name` | string |  |
    | `resource_templates.requested_offering_uuid` | string (uuid) |  |
    | `resource_templates.requested_offering_plan` | any |  |
    | `resource_templates.requested_offering_type` | string |  |
    | `resource_templates.requested_offering_components` | array of objects |  |
    | `resource_templates.requested_offering_components.uuid` | string (uuid) |  |
    | `resource_templates.requested_offering_components.offering_uuid` | string (uuid) |  |
    | `resource_templates.requested_offering_components.billing_type` | string | <br>_Enum: `fixed`, `usage`, `limit`, `one`, `few`_ |
    | `resource_templates.requested_offering_components.type` | string | Unique internal name of the measured unit, for example floating_ip. |
    | `resource_templates.requested_offering_components.name` | string | Display name for the measured unit, for example, Floating IP. |
    | `resource_templates.requested_offering_components.description` | string |  |
    | `resource_templates.requested_offering_components.measured_unit` | string | Unit of measurement, for example, GB. |
    | `resource_templates.requested_offering_components.unit_factor` | integer | The conversion factor from backend units to measured_unit |
    | `resource_templates.requested_offering_components.limit_period` | any |  |
    | `resource_templates.requested_offering_components.limit_amount` | number (double) |  |
    | `resource_templates.requested_offering_components.limit_decimal_places` | integer | Number of decimal places accepted for this component's limit. 0 keeps the limit integer-only. |
    | `resource_templates.requested_offering_components.article_code` | string |  |
    | `resource_templates.requested_offering_components.max_value` | number (double) |  |
    | `resource_templates.requested_offering_components.min_value` | number (double) |  |
    | `resource_templates.requested_offering_components.max_available_limit` | number (double) |  |
    | `resource_templates.requested_offering_components.is_boolean` | boolean |  |
    | `resource_templates.requested_offering_components.default_limit` | number (double) |  |
    | `resource_templates.requested_offering_components.factor` | integer |  |
    | `resource_templates.requested_offering_components.is_builtin` | boolean | The API's older name for ``billed_per_plan``.  It used to ask the plugin registry whether this component's type is one the plugin declares, which left out the OpenStack per-volume-type quotas: they are created by the volume type sync rather than declared, so the API called them provider components while the billing resolver treated them as builtin. Reading the stored flag makes the two agree. |
    | `resource_templates.requested_offering_components.is_prepaid` | boolean |  |
    | `resource_templates.requested_offering_components.overage_component` | string (uuid) |  |
    | `resource_templates.requested_offering_components.min_prepaid_duration` | integer |  |
    | `resource_templates.requested_offering_components.max_prepaid_duration` | integer |  |
    | `resource_templates.requested_offering_components.prepaid_duration_step` | integer | Step size in months for the initial prepaid duration at order creation. If set, only multiples of this value (starting from min_prepaid_duration) are valid. Defaults to 1 (any value between min and max). |
    | `resource_templates.requested_offering_components.min_renewal_duration` | integer | Minimum number of months allowed for a renewal. |
    | `resource_templates.requested_offering_components.max_renewal_duration` | integer | Maximum number of months allowed for a renewal. |
    | `resource_templates.requested_offering_components.renewal_duration_step` | integer | Step size in months for renewal. Only multiples of this value (starting from min_renewal_duration) are valid. Defaults to 1. |
    | `resource_templates.created_by` | string (uri) |  |
    | `resource_templates.created_by_name` | string |  |
    | `resource_templates.created` | string (date-time) |  |
    | `fixed_duration_in_days` | integer |  |
    | `max_prepaid_duration_months` | integer | The longest prepaid subscription, in whole months, that fits inside fixed_duration_in_days measured from today; null when the call fixes no duration. |
    | `backend_id` | string |  |
    | `external_url` | string (uri) |  |
    | `reviewer_identity_visible_to_submitters` | boolean | Whether proposal applicants can see reviewer identities |
    | `reviews_visible_to_submitters` | boolean | Whether proposal applicants can see review comments and scores |
    | `has_eligibility_restrictions` | boolean | Check if call has any eligibility restrictions configured. |
    | `proposal_field_config` | object |  |
    | `proposal_field_config.field_project_summary` | string | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_config.field_description` | string | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_config.field_science_sub_domain` | string | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_config.field_supporting_documentation` | string | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `evaluation_start` | any | When a submitted proposal's evaluation starts: on submission, or for all proposals of a round together at its cut-off. Cannot be changed while the call has proposals submitted or in review. |
    | `publish_results` | any | When applicants learn the allocation decision: immediately, or for every proposal of a round together when a call manager publishes the round's results. Cannot be changed while decisions are held. |
    | `created_by` | string (uri) |  |
    | `reference_code` | string |  |
    | `compliance_checklist` | string (uuid) | Compliance checklist that proposals must complete before submission |
    | `compliance_checklist_name` | string |  |
    | `panel_chair` | string (uuid) |  |
    | `panel_chair_uuid` | string (uuid) |  |
    | `panel_chair_name` | string |  |
    | `proposal_slug_template` | string | Template for proposal slugs. Supports: {call_slug}, {round_slug}, {org_slug}, {year}, {month}, {counter}, {counter_padded}. Default: {round_slug}-{counter_padded} |
    | `user_email_patterns` | array of strings | List of email regex patterns. User must match one. |
    | `user_affiliations` | array of strings | List of allowed affiliations. User must have one. |
    | `user_identity_sources` | array of strings | List of allowed identity sources (identity providers). |
    | `user_nationalities` | array of strings | List of allowed nationality codes (ISO 3166-1 alpha-2). User must have one. |
    | `user_organization_types` | array of strings | List of allowed organization type URNs (SCHAC). User must match one. |
    | `user_assurance_levels` | array of strings | List of required assurance URIs (REFEDS). User must have ALL of these. |
    | `applicant_visibility_config` | any |  |
    | `proposal_field_metadata` | array of objects | Per-field state, permitted transitions and downstream consumers for the Project details step. |
    | `proposal_field_metadata.field` | string |  |
    | `proposal_field_metadata.state` | string | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_metadata.allowed_states` | array of strings |  |
    | `proposal_field_metadata.locked_reason` | string |  |
    | `proposal_field_metadata.usage` | array of strings |  |
    | `has_proposals` | boolean | Whether any proposal has been submitted to this call. Used by the frontend to gate slug-template and checklist fields. |
    | `order_author` | any | Whose name the orders for resources granted by this call carry. |
    | `order_author_user` | string (uuid) | The person orders are attributed to when the author is a named contact. Must hold a role on this call or on the organisation managing it. |
    | `order_author_user_uuid` | string (uuid) |  |
    | `order_author_user_name` | string |  |
    | `carry_over_drafts` | boolean | Whether a draft still open when its round's cut-off passes moves on to the call's next round instead of being cancelled. Without a later round the draft is cancelled either way. |
    | `undecided_at_round_completion` | any | What completing a round does with its proposals that still have no decision: refuse to complete the round, or reject them. A round may override it. |

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/proposal-protected-calls/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-proposal-protected-call" \
      manager="https://api.example.com/api/manager/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.protected_call_request import ProtectedCallRequest # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ProtectedCallRequest(
        name="my-awesome-proposal-protected-call",
        manager="https://api.example.com/api/manager/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    )
    response = proposal_protected_calls_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ProtectedCallRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/protected_call_request.py)
    2.  **API Source:** [`proposal_protected_calls_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_create.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsCreate } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "name": "my-awesome-proposal-protected-call",
        "manager": "https://api.example.com/api/manager/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Request Body (required)"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `slug` | string |  | URL-friendly identifier. Only editable by staff users. |
    | `name` | string | ✓ |  |
    | `description` | string |  |  |
    | `manager` | string (uri) | ✓ |  |
    | `fixed_duration_in_days` | integer |  |  |
    | `backend_id` | string |  |  |
    | `external_url` | string (uri) |  |  |
    | `reviewer_identity_visible_to_submitters` | boolean |  | Whether proposal applicants can see reviewer identities |
    | `reviews_visible_to_submitters` | boolean |  | Whether proposal applicants can see review comments and scores |
    | `proposal_field_config` | object |  |  |
    | `proposal_field_config.field_project_summary` | string |  | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_config.field_description` | string |  | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_config.field_science_sub_domain` | string |  | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_config.field_supporting_documentation` | string |  | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `evaluation_start` | any |  | When a submitted proposal's evaluation starts: on submission, or for all proposals of a round together at its cut-off. Cannot be changed while the call has proposals submitted or in review. |
    | `publish_results` | any |  | When applicants learn the allocation decision: immediately, or for every proposal of a round together when a call manager publishes the round's results. Cannot be changed while decisions are held. |
    | `created_by` | string (uri) |  |  |
    | `reference_code` | string |  |  |
    | `compliance_checklist` | string (uuid) |  | Compliance checklist that proposals must complete before submission |
    | `panel_chair` | string (uuid) |  |  |
    | `proposal_slug_template` | string |  | Template for proposal slugs. Supports: {call_slug}, {round_slug}, {org_slug}, {year}, {month}, {counter}, {counter_padded}. Default: {round_slug}-{counter_padded} |
    | `user_email_patterns` | array of strings |  | List of email regex patterns. User must match one. |
    | `user_affiliations` | array of strings |  | List of allowed affiliations. User must have one. |
    | `user_identity_sources` | array of strings |  | List of allowed identity sources (identity providers). |
    | `user_nationalities` | array of strings |  | List of allowed nationality codes (ISO 3166-1 alpha-2). User must have one. |
    | `user_organization_types` | array of strings |  | List of allowed organization type URNs (SCHAC). User must match one. |
    | `user_assurance_levels` | array of strings |  | List of required assurance URIs (REFEDS). User must have ALL of these. |
    | `applicant_visibility_config` | any |  |  |
    | `order_author` | any |  | Whose name the orders for resources granted by this call carry. |
    | `order_author_user` | string (uuid) |  | The person orders are attributed to when the author is a named contact. Must hold a role on this call or on the organisation managing it. |
    | `carry_over_drafts` | boolean |  | Whether a draft still open when its round's cut-off passes moves on to the call's next round instead of being cancelled. Without a later round the draft is cancelled either way. |
    | `undecided_at_round_completion` | any |  | What completing a round does with its proposals that still have no decision: refuse to complete the round, or reject them. A round may override it. |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `start_date` | string (date-time) |  |
    | `end_date` | string (date-time) |  |
    | `slug` | string | URL-friendly identifier. Only editable by staff users. |
    | `name` | string |  |
    | `description` | string |  |
    | `state` | any |  |
    | `manager` | string (uri) |  |
    | `manager_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `offerings` | array of objects |  |
    | `offerings.uuid` | string (uuid) |  |
    | `offerings.state` | any |  |
    | `offerings.offering` | string (uri) |  |
    | `offerings.offering_name` | string |  |
    | `offerings.offering_uuid` | string (uuid) |  |
    | `offerings.offering_type` | string |  |
    | `offerings.provider_name` | string |  |
    | `offerings.category_uuid` | string (uuid) |  |
    | `offerings.category_name` | string |  |
    | `offerings.call_managing_organisation` | string |  |
    | `offerings.attributes` | object (free-form) |  |
    | `offerings.plan` | string (uri) |  |
    | `offerings.plan_details` | any |  |
    | `offerings.options` | any |  |
    | `offerings.components` | array of objects |  |
    | `offerings.components.uuid` | string (uuid) |  |
    | `offerings.components.offering_uuid` | string (uuid) |  |
    | `offerings.components.billing_type` | string | <br>_Enum: `fixed`, `usage`, `limit`, `one`, `few`_ |
    | `offerings.components.type` | string | Unique internal name of the measured unit, for example floating_ip. |
    | `offerings.components.name` | string | Display name for the measured unit, for example, Floating IP. |
    | `offerings.components.description` | string |  |
    | `offerings.components.measured_unit` | string | Unit of measurement, for example, GB. |
    | `offerings.components.unit_factor` | integer | The conversion factor from backend units to measured_unit |
    | `offerings.components.limit_period` | any |  |
    | `offerings.components.limit_amount` | number (double) |  |
    | `offerings.components.limit_decimal_places` | integer | Number of decimal places accepted for this component's limit. 0 keeps the limit integer-only. |
    | `offerings.components.article_code` | string |  |
    | `offerings.components.max_value` | number (double) |  |
    | `offerings.components.min_value` | number (double) |  |
    | `offerings.components.max_available_limit` | number (double) |  |
    | `offerings.components.is_boolean` | boolean |  |
    | `offerings.components.default_limit` | number (double) |  |
    | `offerings.components.factor` | integer |  |
    | `offerings.components.is_builtin` | boolean | The API's older name for ``billed_per_plan``.  It used to ask the plugin registry whether this component's type is one the plugin declares, which left out the OpenStack per-volume-type quotas: they are created by the volume type sync rather than declared, so the API called them provider components while the billing resolver treated them as builtin. Reading the stored flag makes the two agree. |
    | `offerings.components.is_prepaid` | boolean |  |
    | `offerings.components.overage_component` | string (uuid) |  |
    | `offerings.components.min_prepaid_duration` | integer |  |
    | `offerings.components.max_prepaid_duration` | integer |  |
    | `offerings.components.prepaid_duration_step` | integer | Step size in months for the initial prepaid duration at order creation. If set, only multiples of this value (starting from min_prepaid_duration) are valid. Defaults to 1 (any value between min and max). |
    | `offerings.components.min_renewal_duration` | integer | Minimum number of months allowed for a renewal. |
    | `offerings.components.max_renewal_duration` | integer | Maximum number of months allowed for a renewal. |
    | `offerings.components.renewal_duration_step` | integer | Step size in months for renewal. Only multiples of this value (starting from min_renewal_duration) are valid. Defaults to 1. |
    | `offerings.require_purchase_order` | boolean | Whether a purchase order must accompany a resource request for this offering before the proposal can be submitted. Defaults to the offering's require_purchase_order_upload, and stays under the call manager's control afterwards. |
    | `offerings.created` | string (date-time) |  |
    | `rounds` | array of objects |  |
    | `rounds.uuid` | string (uuid) |  |
    | `rounds.slug` | string |  |
    | `rounds.name` | string |  |
    | `rounds.start_time` | string (date-time) |  |
    | `rounds.cutoff_time` | string (date-time) |  |
    | `rounds.status` | any |  |
    | `rounds.allocation_date` | string (date-time) |  |
    | `rounds.review_duration_in_days` | integer |  |
    | `rounds.lifecycle_state` | any | Where the round stands after its cut-off: evaluating, deciding, results_published or closed. Empty before the cut-off. |
    | `rounds.evaluation_started_at` | string (date-time) |  |
    | `rounds.deciding_started_at` | string (date-time) |  |
    | `rounds.results_published_at` | string (date-time) |  |
    | `rounds.closed_at` | string (date-time) |  |
    | `documents` | array of objects |  |
    | `documents.uuid` | string (uuid) |  |
    | `documents.file` | string (uri) | Documentation for call for proposals. |
    | `documents.file_name` | string |  |
    | `documents.file_size` | integer |  |
    | `documents.description` | string |  |
    | `documents.created` | string (date-time) |  |
    | `resource_templates` | array of objects |  |
    | `resource_templates.uuid` | string (uuid) |  |
    | `resource_templates.url` | string |  |
    | `resource_templates.name` | string |  |
    | `resource_templates.description` | string |  |
    | `resource_templates.attributes` | object (free-form) |  |
    | `resource_templates.limits` | object (free-form) |  |
    | `resource_templates.is_required` | boolean | If True, every proposal must include this resource type |
    | `resource_templates.requested_offering` | string (uri) |  |
    | `resource_templates.requested_offering_name` | string |  |
    | `resource_templates.requested_offering_uuid` | string (uuid) |  |
    | `resource_templates.requested_offering_plan` | any |  |
    | `resource_templates.requested_offering_type` | string |  |
    | `resource_templates.requested_offering_components` | array of objects |  |
    | `resource_templates.requested_offering_components.uuid` | string (uuid) |  |
    | `resource_templates.requested_offering_components.offering_uuid` | string (uuid) |  |
    | `resource_templates.requested_offering_components.billing_type` | string | <br>_Enum: `fixed`, `usage`, `limit`, `one`, `few`_ |
    | `resource_templates.requested_offering_components.type` | string | Unique internal name of the measured unit, for example floating_ip. |
    | `resource_templates.requested_offering_components.name` | string | Display name for the measured unit, for example, Floating IP. |
    | `resource_templates.requested_offering_components.description` | string |  |
    | `resource_templates.requested_offering_components.measured_unit` | string | Unit of measurement, for example, GB. |
    | `resource_templates.requested_offering_components.unit_factor` | integer | The conversion factor from backend units to measured_unit |
    | `resource_templates.requested_offering_components.limit_period` | any |  |
    | `resource_templates.requested_offering_components.limit_amount` | number (double) |  |
    | `resource_templates.requested_offering_components.limit_decimal_places` | integer | Number of decimal places accepted for this component's limit. 0 keeps the limit integer-only. |
    | `resource_templates.requested_offering_components.article_code` | string |  |
    | `resource_templates.requested_offering_components.max_value` | number (double) |  |
    | `resource_templates.requested_offering_components.min_value` | number (double) |  |
    | `resource_templates.requested_offering_components.max_available_limit` | number (double) |  |
    | `resource_templates.requested_offering_components.is_boolean` | boolean |  |
    | `resource_templates.requested_offering_components.default_limit` | number (double) |  |
    | `resource_templates.requested_offering_components.factor` | integer |  |
    | `resource_templates.requested_offering_components.is_builtin` | boolean | The API's older name for ``billed_per_plan``.  It used to ask the plugin registry whether this component's type is one the plugin declares, which left out the OpenStack per-volume-type quotas: they are created by the volume type sync rather than declared, so the API called them provider components while the billing resolver treated them as builtin. Reading the stored flag makes the two agree. |
    | `resource_templates.requested_offering_components.is_prepaid` | boolean |  |
    | `resource_templates.requested_offering_components.overage_component` | string (uuid) |  |
    | `resource_templates.requested_offering_components.min_prepaid_duration` | integer |  |
    | `resource_templates.requested_offering_components.max_prepaid_duration` | integer |  |
    | `resource_templates.requested_offering_components.prepaid_duration_step` | integer | Step size in months for the initial prepaid duration at order creation. If set, only multiples of this value (starting from min_prepaid_duration) are valid. Defaults to 1 (any value between min and max). |
    | `resource_templates.requested_offering_components.min_renewal_duration` | integer | Minimum number of months allowed for a renewal. |
    | `resource_templates.requested_offering_components.max_renewal_duration` | integer | Maximum number of months allowed for a renewal. |
    | `resource_templates.requested_offering_components.renewal_duration_step` | integer | Step size in months for renewal. Only multiples of this value (starting from min_renewal_duration) are valid. Defaults to 1. |
    | `resource_templates.created_by` | string (uri) |  |
    | `resource_templates.created_by_name` | string |  |
    | `resource_templates.created` | string (date-time) |  |
    | `fixed_duration_in_days` | integer |  |
    | `max_prepaid_duration_months` | integer | The longest prepaid subscription, in whole months, that fits inside fixed_duration_in_days measured from today; null when the call fixes no duration. |
    | `backend_id` | string |  |
    | `external_url` | string (uri) |  |
    | `reviewer_identity_visible_to_submitters` | boolean | Whether proposal applicants can see reviewer identities |
    | `reviews_visible_to_submitters` | boolean | Whether proposal applicants can see review comments and scores |
    | `has_eligibility_restrictions` | boolean | Check if call has any eligibility restrictions configured. |
    | `proposal_field_config` | object |  |
    | `proposal_field_config.field_project_summary` | string | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_config.field_description` | string | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_config.field_science_sub_domain` | string | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_config.field_supporting_documentation` | string | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `evaluation_start` | any | When a submitted proposal's evaluation starts: on submission, or for all proposals of a round together at its cut-off. Cannot be changed while the call has proposals submitted or in review. |
    | `publish_results` | any | When applicants learn the allocation decision: immediately, or for every proposal of a round together when a call manager publishes the round's results. Cannot be changed while decisions are held. |
    | `created_by` | string (uri) |  |
    | `reference_code` | string |  |
    | `compliance_checklist` | string (uuid) | Compliance checklist that proposals must complete before submission |
    | `compliance_checklist_name` | string |  |
    | `panel_chair` | string (uuid) |  |
    | `panel_chair_uuid` | string (uuid) |  |
    | `panel_chair_name` | string |  |
    | `proposal_slug_template` | string | Template for proposal slugs. Supports: {call_slug}, {round_slug}, {org_slug}, {year}, {month}, {counter}, {counter_padded}. Default: {round_slug}-{counter_padded} |
    | `user_email_patterns` | array of strings | List of email regex patterns. User must match one. |
    | `user_affiliations` | array of strings | List of allowed affiliations. User must have one. |
    | `user_identity_sources` | array of strings | List of allowed identity sources (identity providers). |
    | `user_nationalities` | array of strings | List of allowed nationality codes (ISO 3166-1 alpha-2). User must have one. |
    | `user_organization_types` | array of strings | List of allowed organization type URNs (SCHAC). User must match one. |
    | `user_assurance_levels` | array of strings | List of required assurance URIs (REFEDS). User must have ALL of these. |
    | `applicant_visibility_config` | any |  |
    | `proposal_field_metadata` | array of objects | Per-field state, permitted transitions and downstream consumers for the Project details step. |
    | `proposal_field_metadata.field` | string |  |
    | `proposal_field_metadata.state` | string | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_metadata.allowed_states` | array of strings |  |
    | `proposal_field_metadata.locked_reason` | string |  |
    | `proposal_field_metadata.usage` | array of strings |  |
    | `has_proposals` | boolean | Whether any proposal has been submitted to this call. Used by the frontend to gate slug-template and checklist fields. |
    | `order_author` | any | Whose name the orders for resources granted by this call carry. |
    | `order_author_user` | string (uuid) | The person orders are attributed to when the author is a named contact. Must hold a role on this call or on the organisation managing it. |
    | `order_author_user_uuid` | string (uuid) |  |
    | `order_author_user_name` | string |  |
    | `carry_over_drafts` | boolean | Whether a draft still open when its round's cut-off passes moves on to the call's next round instead of being cancelled. Without a later round the draft is cancelled either way. |
    | `undecided_at_round_completion` | any | What completing a round does with its proposals that still have no decision: refuse to complete the round, or reject them. A round may override it. |

---

### Create manual assignment

Create a manual assignment batch for a specific reviewer. This allows call managers to manually assign proposals to reviewers.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/create-manual-assignment/ \
      Authorization:"Token YOUR_API_TOKEN" \
      reviewer_pool_entry_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      proposal_uuids:='[]'
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.create_manual_assignment_request import CreateManualAssignmentRequest # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_create_manual_assignment # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = CreateManualAssignmentRequest(
        reviewer_pool_entry_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        proposal_uuids=[]
    )
    response = proposal_protected_calls_create_manual_assignment.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`CreateManualAssignmentRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/create_manual_assignment_request.py)
    2.  **API Source:** [`proposal_protected_calls_create_manual_assignment`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_create_manual_assignment.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsCreateManualAssignment } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsCreateManualAssignment({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "reviewer_pool_entry_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "proposal_uuids": []
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Request Body (required)"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `reviewer_pool_entry_uuid` | string (uuid) | ✓ | UUID of the reviewer pool entry to assign proposals to |
    | `proposal_uuids` | array of string (uuid)s | ✓ | List of proposal UUIDs to assign to the reviewer |
    | `manager_notes` | string |  | Optional notes about this assignment |
    | `override_workload_limit` | boolean |  | Assign even if this takes the reviewer above their maximum number of open assignments. The override is logged.<br>_Constraints: default: `False`_ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `batch_uuid` | string (uuid) |  |
    | `items_created` | integer |  |
    | `skipped_proposals` | array of objects | Proposals that were skipped with reasons |
    | `skipped_proposals.proposal_uuid` | string (uuid) |  |
    | `skipped_proposals.proposal_name` | string |  |
    | `skipped_proposals.reason` | string |  |

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-proposal-protected-call" \
      manager="https://api.example.com/api/manager/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.protected_call_request import ProtectedCallRequest # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ProtectedCallRequest(
        name="my-awesome-proposal-protected-call",
        manager="https://api.example.com/api/manager/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    )
    response = proposal_protected_calls_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ProtectedCallRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/protected_call_request.py)
    2.  **API Source:** [`proposal_protected_calls_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_update.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsUpdate } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "name": "my-awesome-proposal-protected-call",
        "manager": "https://api.example.com/api/manager/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Request Body (required)"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `slug` | string |  | URL-friendly identifier. Only editable by staff users. |
    | `name` | string | ✓ |  |
    | `description` | string |  |  |
    | `manager` | string (uri) | ✓ |  |
    | `fixed_duration_in_days` | integer |  |  |
    | `backend_id` | string |  |  |
    | `external_url` | string (uri) |  |  |
    | `reviewer_identity_visible_to_submitters` | boolean |  | Whether proposal applicants can see reviewer identities |
    | `reviews_visible_to_submitters` | boolean |  | Whether proposal applicants can see review comments and scores |
    | `proposal_field_config` | object |  |  |
    | `proposal_field_config.field_project_summary` | string |  | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_config.field_description` | string |  | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_config.field_science_sub_domain` | string |  | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_config.field_supporting_documentation` | string |  | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `evaluation_start` | any |  | When a submitted proposal's evaluation starts: on submission, or for all proposals of a round together at its cut-off. Cannot be changed while the call has proposals submitted or in review. |
    | `publish_results` | any |  | When applicants learn the allocation decision: immediately, or for every proposal of a round together when a call manager publishes the round's results. Cannot be changed while decisions are held. |
    | `created_by` | string (uri) |  |  |
    | `reference_code` | string |  |  |
    | `compliance_checklist` | string (uuid) |  | Compliance checklist that proposals must complete before submission |
    | `panel_chair` | string (uuid) |  |  |
    | `proposal_slug_template` | string |  | Template for proposal slugs. Supports: {call_slug}, {round_slug}, {org_slug}, {year}, {month}, {counter}, {counter_padded}. Default: {round_slug}-{counter_padded} |
    | `user_email_patterns` | array of strings |  | List of email regex patterns. User must match one. |
    | `user_affiliations` | array of strings |  | List of allowed affiliations. User must have one. |
    | `user_identity_sources` | array of strings |  | List of allowed identity sources (identity providers). |
    | `user_nationalities` | array of strings |  | List of allowed nationality codes (ISO 3166-1 alpha-2). User must have one. |
    | `user_organization_types` | array of strings |  | List of allowed organization type URNs (SCHAC). User must match one. |
    | `user_assurance_levels` | array of strings |  | List of required assurance URIs (REFEDS). User must have ALL of these. |
    | `applicant_visibility_config` | any |  |  |
    | `order_author` | any |  | Whose name the orders for resources granted by this call carry. |
    | `order_author_user` | string (uuid) |  | The person orders are attributed to when the author is a named contact. Must hold a role on this call or on the organisation managing it. |
    | `carry_over_drafts` | boolean |  | Whether a draft still open when its round's cut-off passes moves on to the call's next round instead of being cancelled. Without a later round the draft is cancelled either way. |
    | `undecided_at_round_completion` | any |  | What completing a round does with its proposals that still have no decision: refuse to complete the round, or reject them. A round may override it. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `start_date` | string (date-time) |  |
    | `end_date` | string (date-time) |  |
    | `slug` | string | URL-friendly identifier. Only editable by staff users. |
    | `name` | string |  |
    | `description` | string |  |
    | `state` | any |  |
    | `manager` | string (uri) |  |
    | `manager_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `offerings` | array of objects |  |
    | `offerings.uuid` | string (uuid) |  |
    | `offerings.state` | any |  |
    | `offerings.offering` | string (uri) |  |
    | `offerings.offering_name` | string |  |
    | `offerings.offering_uuid` | string (uuid) |  |
    | `offerings.offering_type` | string |  |
    | `offerings.provider_name` | string |  |
    | `offerings.category_uuid` | string (uuid) |  |
    | `offerings.category_name` | string |  |
    | `offerings.call_managing_organisation` | string |  |
    | `offerings.attributes` | object (free-form) |  |
    | `offerings.plan` | string (uri) |  |
    | `offerings.plan_details` | any |  |
    | `offerings.options` | any |  |
    | `offerings.components` | array of objects |  |
    | `offerings.components.uuid` | string (uuid) |  |
    | `offerings.components.offering_uuid` | string (uuid) |  |
    | `offerings.components.billing_type` | string | <br>_Enum: `fixed`, `usage`, `limit`, `one`, `few`_ |
    | `offerings.components.type` | string | Unique internal name of the measured unit, for example floating_ip. |
    | `offerings.components.name` | string | Display name for the measured unit, for example, Floating IP. |
    | `offerings.components.description` | string |  |
    | `offerings.components.measured_unit` | string | Unit of measurement, for example, GB. |
    | `offerings.components.unit_factor` | integer | The conversion factor from backend units to measured_unit |
    | `offerings.components.limit_period` | any |  |
    | `offerings.components.limit_amount` | number (double) |  |
    | `offerings.components.limit_decimal_places` | integer | Number of decimal places accepted for this component's limit. 0 keeps the limit integer-only. |
    | `offerings.components.article_code` | string |  |
    | `offerings.components.max_value` | number (double) |  |
    | `offerings.components.min_value` | number (double) |  |
    | `offerings.components.max_available_limit` | number (double) |  |
    | `offerings.components.is_boolean` | boolean |  |
    | `offerings.components.default_limit` | number (double) |  |
    | `offerings.components.factor` | integer |  |
    | `offerings.components.is_builtin` | boolean | The API's older name for ``billed_per_plan``.  It used to ask the plugin registry whether this component's type is one the plugin declares, which left out the OpenStack per-volume-type quotas: they are created by the volume type sync rather than declared, so the API called them provider components while the billing resolver treated them as builtin. Reading the stored flag makes the two agree. |
    | `offerings.components.is_prepaid` | boolean |  |
    | `offerings.components.overage_component` | string (uuid) |  |
    | `offerings.components.min_prepaid_duration` | integer |  |
    | `offerings.components.max_prepaid_duration` | integer |  |
    | `offerings.components.prepaid_duration_step` | integer | Step size in months for the initial prepaid duration at order creation. If set, only multiples of this value (starting from min_prepaid_duration) are valid. Defaults to 1 (any value between min and max). |
    | `offerings.components.min_renewal_duration` | integer | Minimum number of months allowed for a renewal. |
    | `offerings.components.max_renewal_duration` | integer | Maximum number of months allowed for a renewal. |
    | `offerings.components.renewal_duration_step` | integer | Step size in months for renewal. Only multiples of this value (starting from min_renewal_duration) are valid. Defaults to 1. |
    | `offerings.require_purchase_order` | boolean | Whether a purchase order must accompany a resource request for this offering before the proposal can be submitted. Defaults to the offering's require_purchase_order_upload, and stays under the call manager's control afterwards. |
    | `offerings.created` | string (date-time) |  |
    | `rounds` | array of objects |  |
    | `rounds.uuid` | string (uuid) |  |
    | `rounds.slug` | string |  |
    | `rounds.name` | string |  |
    | `rounds.start_time` | string (date-time) |  |
    | `rounds.cutoff_time` | string (date-time) |  |
    | `rounds.status` | any |  |
    | `rounds.allocation_date` | string (date-time) |  |
    | `rounds.review_duration_in_days` | integer |  |
    | `rounds.lifecycle_state` | any | Where the round stands after its cut-off: evaluating, deciding, results_published or closed. Empty before the cut-off. |
    | `rounds.evaluation_started_at` | string (date-time) |  |
    | `rounds.deciding_started_at` | string (date-time) |  |
    | `rounds.results_published_at` | string (date-time) |  |
    | `rounds.closed_at` | string (date-time) |  |
    | `documents` | array of objects |  |
    | `documents.uuid` | string (uuid) |  |
    | `documents.file` | string (uri) | Documentation for call for proposals. |
    | `documents.file_name` | string |  |
    | `documents.file_size` | integer |  |
    | `documents.description` | string |  |
    | `documents.created` | string (date-time) |  |
    | `resource_templates` | array of objects |  |
    | `resource_templates.uuid` | string (uuid) |  |
    | `resource_templates.url` | string |  |
    | `resource_templates.name` | string |  |
    | `resource_templates.description` | string |  |
    | `resource_templates.attributes` | object (free-form) |  |
    | `resource_templates.limits` | object (free-form) |  |
    | `resource_templates.is_required` | boolean | If True, every proposal must include this resource type |
    | `resource_templates.requested_offering` | string (uri) |  |
    | `resource_templates.requested_offering_name` | string |  |
    | `resource_templates.requested_offering_uuid` | string (uuid) |  |
    | `resource_templates.requested_offering_plan` | any |  |
    | `resource_templates.requested_offering_type` | string |  |
    | `resource_templates.requested_offering_components` | array of objects |  |
    | `resource_templates.requested_offering_components.uuid` | string (uuid) |  |
    | `resource_templates.requested_offering_components.offering_uuid` | string (uuid) |  |
    | `resource_templates.requested_offering_components.billing_type` | string | <br>_Enum: `fixed`, `usage`, `limit`, `one`, `few`_ |
    | `resource_templates.requested_offering_components.type` | string | Unique internal name of the measured unit, for example floating_ip. |
    | `resource_templates.requested_offering_components.name` | string | Display name for the measured unit, for example, Floating IP. |
    | `resource_templates.requested_offering_components.description` | string |  |
    | `resource_templates.requested_offering_components.measured_unit` | string | Unit of measurement, for example, GB. |
    | `resource_templates.requested_offering_components.unit_factor` | integer | The conversion factor from backend units to measured_unit |
    | `resource_templates.requested_offering_components.limit_period` | any |  |
    | `resource_templates.requested_offering_components.limit_amount` | number (double) |  |
    | `resource_templates.requested_offering_components.limit_decimal_places` | integer | Number of decimal places accepted for this component's limit. 0 keeps the limit integer-only. |
    | `resource_templates.requested_offering_components.article_code` | string |  |
    | `resource_templates.requested_offering_components.max_value` | number (double) |  |
    | `resource_templates.requested_offering_components.min_value` | number (double) |  |
    | `resource_templates.requested_offering_components.max_available_limit` | number (double) |  |
    | `resource_templates.requested_offering_components.is_boolean` | boolean |  |
    | `resource_templates.requested_offering_components.default_limit` | number (double) |  |
    | `resource_templates.requested_offering_components.factor` | integer |  |
    | `resource_templates.requested_offering_components.is_builtin` | boolean | The API's older name for ``billed_per_plan``.  It used to ask the plugin registry whether this component's type is one the plugin declares, which left out the OpenStack per-volume-type quotas: they are created by the volume type sync rather than declared, so the API called them provider components while the billing resolver treated them as builtin. Reading the stored flag makes the two agree. |
    | `resource_templates.requested_offering_components.is_prepaid` | boolean |  |
    | `resource_templates.requested_offering_components.overage_component` | string (uuid) |  |
    | `resource_templates.requested_offering_components.min_prepaid_duration` | integer |  |
    | `resource_templates.requested_offering_components.max_prepaid_duration` | integer |  |
    | `resource_templates.requested_offering_components.prepaid_duration_step` | integer | Step size in months for the initial prepaid duration at order creation. If set, only multiples of this value (starting from min_prepaid_duration) are valid. Defaults to 1 (any value between min and max). |
    | `resource_templates.requested_offering_components.min_renewal_duration` | integer | Minimum number of months allowed for a renewal. |
    | `resource_templates.requested_offering_components.max_renewal_duration` | integer | Maximum number of months allowed for a renewal. |
    | `resource_templates.requested_offering_components.renewal_duration_step` | integer | Step size in months for renewal. Only multiples of this value (starting from min_renewal_duration) are valid. Defaults to 1. |
    | `resource_templates.created_by` | string (uri) |  |
    | `resource_templates.created_by_name` | string |  |
    | `resource_templates.created` | string (date-time) |  |
    | `fixed_duration_in_days` | integer |  |
    | `max_prepaid_duration_months` | integer | The longest prepaid subscription, in whole months, that fits inside fixed_duration_in_days measured from today; null when the call fixes no duration. |
    | `backend_id` | string |  |
    | `external_url` | string (uri) |  |
    | `reviewer_identity_visible_to_submitters` | boolean | Whether proposal applicants can see reviewer identities |
    | `reviews_visible_to_submitters` | boolean | Whether proposal applicants can see review comments and scores |
    | `has_eligibility_restrictions` | boolean | Check if call has any eligibility restrictions configured. |
    | `proposal_field_config` | object |  |
    | `proposal_field_config.field_project_summary` | string | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_config.field_description` | string | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_config.field_science_sub_domain` | string | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_config.field_supporting_documentation` | string | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `evaluation_start` | any | When a submitted proposal's evaluation starts: on submission, or for all proposals of a round together at its cut-off. Cannot be changed while the call has proposals submitted or in review. |
    | `publish_results` | any | When applicants learn the allocation decision: immediately, or for every proposal of a round together when a call manager publishes the round's results. Cannot be changed while decisions are held. |
    | `created_by` | string (uri) |  |
    | `reference_code` | string |  |
    | `compliance_checklist` | string (uuid) | Compliance checklist that proposals must complete before submission |
    | `compliance_checklist_name` | string |  |
    | `panel_chair` | string (uuid) |  |
    | `panel_chair_uuid` | string (uuid) |  |
    | `panel_chair_name` | string |  |
    | `proposal_slug_template` | string | Template for proposal slugs. Supports: {call_slug}, {round_slug}, {org_slug}, {year}, {month}, {counter}, {counter_padded}. Default: {round_slug}-{counter_padded} |
    | `user_email_patterns` | array of strings | List of email regex patterns. User must match one. |
    | `user_affiliations` | array of strings | List of allowed affiliations. User must have one. |
    | `user_identity_sources` | array of strings | List of allowed identity sources (identity providers). |
    | `user_nationalities` | array of strings | List of allowed nationality codes (ISO 3166-1 alpha-2). User must have one. |
    | `user_organization_types` | array of strings | List of allowed organization type URNs (SCHAC). User must match one. |
    | `user_assurance_levels` | array of strings | List of required assurance URIs (REFEDS). User must have ALL of these. |
    | `applicant_visibility_config` | any |  |
    | `proposal_field_metadata` | array of objects | Per-field state, permitted transitions and downstream consumers for the Project details step. |
    | `proposal_field_metadata.field` | string |  |
    | `proposal_field_metadata.state` | string | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_metadata.allowed_states` | array of strings |  |
    | `proposal_field_metadata.locked_reason` | string |  |
    | `proposal_field_metadata.usage` | array of strings |  |
    | `has_proposals` | boolean | Whether any proposal has been submitted to this call. Used by the frontend to gate slug-template and checklist fields. |
    | `order_author` | any | Whose name the orders for resources granted by this call carry. |
    | `order_author_user` | string (uuid) | The person orders are attributed to when the author is a named contact. Must hold a role on this call or on the organisation managing it. |
    | `order_author_user_uuid` | string (uuid) |  |
    | `order_author_user_name` | string |  |
    | `carry_over_drafts` | boolean | Whether a draft still open when its round's cut-off passes moves on to the call's next round instead of being cancelled. Without a later round the draft is cancelled either way. |
    | `undecided_at_round_completion` | any | What completing a round does with its proposals that still have no decision: refuse to complete the round, or reject them. A round may override it. |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_protected_call_request import PatchedProtectedCallRequest # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedProtectedCallRequest()
    response = proposal_protected_calls_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedProtectedCallRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_protected_call_request.py)
    2.  **API Source:** [`proposal_protected_calls_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_partial_update.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsPartialUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Request Body"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `slug` | string |  | URL-friendly identifier. Only editable by staff users. |
    | `name` | string |  |  |
    | `description` | string |  |  |
    | `fixed_duration_in_days` | integer |  |  |
    | `backend_id` | string |  |  |
    | `external_url` | string (uri) |  |  |
    | `reviewer_identity_visible_to_submitters` | boolean |  | Whether proposal applicants can see reviewer identities |
    | `reviews_visible_to_submitters` | boolean |  | Whether proposal applicants can see review comments and scores |
    | `proposal_field_config` | object |  |  |
    | `proposal_field_config.field_project_summary` | string |  | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_config.field_description` | string |  | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_config.field_science_sub_domain` | string |  | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_config.field_supporting_documentation` | string |  | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `evaluation_start` | any |  | When a submitted proposal's evaluation starts: on submission, or for all proposals of a round together at its cut-off. Cannot be changed while the call has proposals submitted or in review. |
    | `publish_results` | any |  | When applicants learn the allocation decision: immediately, or for every proposal of a round together when a call manager publishes the round's results. Cannot be changed while decisions are held. |
    | `created_by` | string (uri) |  |  |
    | `reference_code` | string |  |  |
    | `compliance_checklist` | string (uuid) |  | Compliance checklist that proposals must complete before submission |
    | `panel_chair` | string (uuid) |  |  |
    | `proposal_slug_template` | string |  | Template for proposal slugs. Supports: {call_slug}, {round_slug}, {org_slug}, {year}, {month}, {counter}, {counter_padded}. Default: {round_slug}-{counter_padded} |
    | `user_email_patterns` | array of strings |  | List of email regex patterns. User must match one. |
    | `user_affiliations` | array of strings |  | List of allowed affiliations. User must have one. |
    | `user_identity_sources` | array of strings |  | List of allowed identity sources (identity providers). |
    | `user_nationalities` | array of strings |  | List of allowed nationality codes (ISO 3166-1 alpha-2). User must have one. |
    | `user_organization_types` | array of strings |  | List of allowed organization type URNs (SCHAC). User must match one. |
    | `user_assurance_levels` | array of strings |  | List of required assurance URIs (REFEDS). User must have ALL of these. |
    | `applicant_visibility_config` | any |  |  |
    | `order_author` | any |  | Whose name the orders for resources granted by this call carry. |
    | `order_author_user` | string (uuid) |  | The person orders are attributed to when the author is a named contact. Must hold a role on this call or on the organisation managing it. |
    | `carry_over_drafts` | boolean |  | Whether a draft still open when its round's cut-off passes moves on to the call's next round instead of being cancelled. Without a later round the draft is cancelled either way. |
    | `undecided_at_round_completion` | any |  | What completing a round does with its proposals that still have no decision: refuse to complete the round, or reject them. A round may override it. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `start_date` | string (date-time) |  |
    | `end_date` | string (date-time) |  |
    | `slug` | string | URL-friendly identifier. Only editable by staff users. |
    | `name` | string |  |
    | `description` | string |  |
    | `state` | any |  |
    | `manager` | string (uri) |  |
    | `manager_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `offerings` | array of objects |  |
    | `offerings.uuid` | string (uuid) |  |
    | `offerings.state` | any |  |
    | `offerings.offering` | string (uri) |  |
    | `offerings.offering_name` | string |  |
    | `offerings.offering_uuid` | string (uuid) |  |
    | `offerings.offering_type` | string |  |
    | `offerings.provider_name` | string |  |
    | `offerings.category_uuid` | string (uuid) |  |
    | `offerings.category_name` | string |  |
    | `offerings.call_managing_organisation` | string |  |
    | `offerings.attributes` | object (free-form) |  |
    | `offerings.plan` | string (uri) |  |
    | `offerings.plan_details` | any |  |
    | `offerings.options` | any |  |
    | `offerings.components` | array of objects |  |
    | `offerings.components.uuid` | string (uuid) |  |
    | `offerings.components.offering_uuid` | string (uuid) |  |
    | `offerings.components.billing_type` | string | <br>_Enum: `fixed`, `usage`, `limit`, `one`, `few`_ |
    | `offerings.components.type` | string | Unique internal name of the measured unit, for example floating_ip. |
    | `offerings.components.name` | string | Display name for the measured unit, for example, Floating IP. |
    | `offerings.components.description` | string |  |
    | `offerings.components.measured_unit` | string | Unit of measurement, for example, GB. |
    | `offerings.components.unit_factor` | integer | The conversion factor from backend units to measured_unit |
    | `offerings.components.limit_period` | any |  |
    | `offerings.components.limit_amount` | number (double) |  |
    | `offerings.components.limit_decimal_places` | integer | Number of decimal places accepted for this component's limit. 0 keeps the limit integer-only. |
    | `offerings.components.article_code` | string |  |
    | `offerings.components.max_value` | number (double) |  |
    | `offerings.components.min_value` | number (double) |  |
    | `offerings.components.max_available_limit` | number (double) |  |
    | `offerings.components.is_boolean` | boolean |  |
    | `offerings.components.default_limit` | number (double) |  |
    | `offerings.components.factor` | integer |  |
    | `offerings.components.is_builtin` | boolean | The API's older name for ``billed_per_plan``.  It used to ask the plugin registry whether this component's type is one the plugin declares, which left out the OpenStack per-volume-type quotas: they are created by the volume type sync rather than declared, so the API called them provider components while the billing resolver treated them as builtin. Reading the stored flag makes the two agree. |
    | `offerings.components.is_prepaid` | boolean |  |
    | `offerings.components.overage_component` | string (uuid) |  |
    | `offerings.components.min_prepaid_duration` | integer |  |
    | `offerings.components.max_prepaid_duration` | integer |  |
    | `offerings.components.prepaid_duration_step` | integer | Step size in months for the initial prepaid duration at order creation. If set, only multiples of this value (starting from min_prepaid_duration) are valid. Defaults to 1 (any value between min and max). |
    | `offerings.components.min_renewal_duration` | integer | Minimum number of months allowed for a renewal. |
    | `offerings.components.max_renewal_duration` | integer | Maximum number of months allowed for a renewal. |
    | `offerings.components.renewal_duration_step` | integer | Step size in months for renewal. Only multiples of this value (starting from min_renewal_duration) are valid. Defaults to 1. |
    | `offerings.require_purchase_order` | boolean | Whether a purchase order must accompany a resource request for this offering before the proposal can be submitted. Defaults to the offering's require_purchase_order_upload, and stays under the call manager's control afterwards. |
    | `offerings.created` | string (date-time) |  |
    | `rounds` | array of objects |  |
    | `rounds.uuid` | string (uuid) |  |
    | `rounds.slug` | string |  |
    | `rounds.name` | string |  |
    | `rounds.start_time` | string (date-time) |  |
    | `rounds.cutoff_time` | string (date-time) |  |
    | `rounds.status` | any |  |
    | `rounds.allocation_date` | string (date-time) |  |
    | `rounds.review_duration_in_days` | integer |  |
    | `rounds.lifecycle_state` | any | Where the round stands after its cut-off: evaluating, deciding, results_published or closed. Empty before the cut-off. |
    | `rounds.evaluation_started_at` | string (date-time) |  |
    | `rounds.deciding_started_at` | string (date-time) |  |
    | `rounds.results_published_at` | string (date-time) |  |
    | `rounds.closed_at` | string (date-time) |  |
    | `documents` | array of objects |  |
    | `documents.uuid` | string (uuid) |  |
    | `documents.file` | string (uri) | Documentation for call for proposals. |
    | `documents.file_name` | string |  |
    | `documents.file_size` | integer |  |
    | `documents.description` | string |  |
    | `documents.created` | string (date-time) |  |
    | `resource_templates` | array of objects |  |
    | `resource_templates.uuid` | string (uuid) |  |
    | `resource_templates.url` | string |  |
    | `resource_templates.name` | string |  |
    | `resource_templates.description` | string |  |
    | `resource_templates.attributes` | object (free-form) |  |
    | `resource_templates.limits` | object (free-form) |  |
    | `resource_templates.is_required` | boolean | If True, every proposal must include this resource type |
    | `resource_templates.requested_offering` | string (uri) |  |
    | `resource_templates.requested_offering_name` | string |  |
    | `resource_templates.requested_offering_uuid` | string (uuid) |  |
    | `resource_templates.requested_offering_plan` | any |  |
    | `resource_templates.requested_offering_type` | string |  |
    | `resource_templates.requested_offering_components` | array of objects |  |
    | `resource_templates.requested_offering_components.uuid` | string (uuid) |  |
    | `resource_templates.requested_offering_components.offering_uuid` | string (uuid) |  |
    | `resource_templates.requested_offering_components.billing_type` | string | <br>_Enum: `fixed`, `usage`, `limit`, `one`, `few`_ |
    | `resource_templates.requested_offering_components.type` | string | Unique internal name of the measured unit, for example floating_ip. |
    | `resource_templates.requested_offering_components.name` | string | Display name for the measured unit, for example, Floating IP. |
    | `resource_templates.requested_offering_components.description` | string |  |
    | `resource_templates.requested_offering_components.measured_unit` | string | Unit of measurement, for example, GB. |
    | `resource_templates.requested_offering_components.unit_factor` | integer | The conversion factor from backend units to measured_unit |
    | `resource_templates.requested_offering_components.limit_period` | any |  |
    | `resource_templates.requested_offering_components.limit_amount` | number (double) |  |
    | `resource_templates.requested_offering_components.limit_decimal_places` | integer | Number of decimal places accepted for this component's limit. 0 keeps the limit integer-only. |
    | `resource_templates.requested_offering_components.article_code` | string |  |
    | `resource_templates.requested_offering_components.max_value` | number (double) |  |
    | `resource_templates.requested_offering_components.min_value` | number (double) |  |
    | `resource_templates.requested_offering_components.max_available_limit` | number (double) |  |
    | `resource_templates.requested_offering_components.is_boolean` | boolean |  |
    | `resource_templates.requested_offering_components.default_limit` | number (double) |  |
    | `resource_templates.requested_offering_components.factor` | integer |  |
    | `resource_templates.requested_offering_components.is_builtin` | boolean | The API's older name for ``billed_per_plan``.  It used to ask the plugin registry whether this component's type is one the plugin declares, which left out the OpenStack per-volume-type quotas: they are created by the volume type sync rather than declared, so the API called them provider components while the billing resolver treated them as builtin. Reading the stored flag makes the two agree. |
    | `resource_templates.requested_offering_components.is_prepaid` | boolean |  |
    | `resource_templates.requested_offering_components.overage_component` | string (uuid) |  |
    | `resource_templates.requested_offering_components.min_prepaid_duration` | integer |  |
    | `resource_templates.requested_offering_components.max_prepaid_duration` | integer |  |
    | `resource_templates.requested_offering_components.prepaid_duration_step` | integer | Step size in months for the initial prepaid duration at order creation. If set, only multiples of this value (starting from min_prepaid_duration) are valid. Defaults to 1 (any value between min and max). |
    | `resource_templates.requested_offering_components.min_renewal_duration` | integer | Minimum number of months allowed for a renewal. |
    | `resource_templates.requested_offering_components.max_renewal_duration` | integer | Maximum number of months allowed for a renewal. |
    | `resource_templates.requested_offering_components.renewal_duration_step` | integer | Step size in months for renewal. Only multiples of this value (starting from min_renewal_duration) are valid. Defaults to 1. |
    | `resource_templates.created_by` | string (uri) |  |
    | `resource_templates.created_by_name` | string |  |
    | `resource_templates.created` | string (date-time) |  |
    | `fixed_duration_in_days` | integer |  |
    | `max_prepaid_duration_months` | integer | The longest prepaid subscription, in whole months, that fits inside fixed_duration_in_days measured from today; null when the call fixes no duration. |
    | `backend_id` | string |  |
    | `external_url` | string (uri) |  |
    | `reviewer_identity_visible_to_submitters` | boolean | Whether proposal applicants can see reviewer identities |
    | `reviews_visible_to_submitters` | boolean | Whether proposal applicants can see review comments and scores |
    | `has_eligibility_restrictions` | boolean | Check if call has any eligibility restrictions configured. |
    | `proposal_field_config` | object |  |
    | `proposal_field_config.field_project_summary` | string | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_config.field_description` | string | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_config.field_science_sub_domain` | string | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_config.field_supporting_documentation` | string | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `evaluation_start` | any | When a submitted proposal's evaluation starts: on submission, or for all proposals of a round together at its cut-off. Cannot be changed while the call has proposals submitted or in review. |
    | `publish_results` | any | When applicants learn the allocation decision: immediately, or for every proposal of a round together when a call manager publishes the round's results. Cannot be changed while decisions are held. |
    | `created_by` | string (uri) |  |
    | `reference_code` | string |  |
    | `compliance_checklist` | string (uuid) | Compliance checklist that proposals must complete before submission |
    | `compliance_checklist_name` | string |  |
    | `panel_chair` | string (uuid) |  |
    | `panel_chair_uuid` | string (uuid) |  |
    | `panel_chair_name` | string |  |
    | `proposal_slug_template` | string | Template for proposal slugs. Supports: {call_slug}, {round_slug}, {org_slug}, {year}, {month}, {counter}, {counter_padded}. Default: {round_slug}-{counter_padded} |
    | `user_email_patterns` | array of strings | List of email regex patterns. User must match one. |
    | `user_affiliations` | array of strings | List of allowed affiliations. User must have one. |
    | `user_identity_sources` | array of strings | List of allowed identity sources (identity providers). |
    | `user_nationalities` | array of strings | List of allowed nationality codes (ISO 3166-1 alpha-2). User must have one. |
    | `user_organization_types` | array of strings | List of allowed organization type URNs (SCHAC). User must match one. |
    | `user_assurance_levels` | array of strings | List of required assurance URIs (REFEDS). User must have ALL of these. |
    | `applicant_visibility_config` | any |  |
    | `proposal_field_metadata` | array of objects | Per-field state, permitted transitions and downstream consumers for the Project details step. |
    | `proposal_field_metadata.field` | string |  |
    | `proposal_field_metadata.state` | string | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_metadata.allowed_states` | array of strings |  |
    | `proposal_field_metadata.locked_reason` | string |  |
    | `proposal_field_metadata.usage` | array of strings |  |
    | `has_proposals` | boolean | Whether any proposal has been submitted to this call. Used by the frontend to gate slug-template and checklist fields. |
    | `order_author` | any | Whose name the orders for resources granted by this call carry. |
    | `order_author_user` | string (uuid) | The person orders are attributed to when the author is a named contact. Must hold a role on this call or on the organisation managing it. |
    | `order_author_user_uuid` | string (uuid) |  |
    | `order_author_user_name` | string |  |
    | `carry_over_drafts` | boolean | Whether a draft still open when its round's cut-off passes moves on to the call's next round instead of being cancelled. Without a later round the draft is cancelled either way. |
    | `undecided_at_round_completion` | any | What completing a round does with its proposals that still have no decision: refuse to complete the round, or reject them. A round may override it. |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`proposal_protected_calls_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_destroy.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsDestroy } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsDestroy({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Responses"

    **`204`** - No response body
    

---

## Permissions & Users


### List users and their roles in a scope

Retrieves a list of users who have a role within a specific scope (e.g., a project or an organization). The list can be filtered by user details or role.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/list_users/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.user_role_details_field_enum import UserRoleDetailsFieldEnum # (1)
    from waldur_api_client.models.user_role_details_o_enum import UserRoleDetailsOEnum # (2)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_list_users_list # (3)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_list_users_list.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`UserRoleDetailsFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/user_role_details_field_enum.py)
    2.  **Model Source:** [`UserRoleDetailsOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/user_role_details_o_enum.py)
    3.  **API Source:** [`proposal_protected_calls_list_users_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_list_users_list.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsListUsersList } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsListUsersList({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Query Parameters"

    | Name | Type | Description |
    |---|---|---|
    | `field` | array | Fields to include in response |
    | `full_name` | string | User full name |
    | `native_name` | string | User native name |
    | `o` | array | Ordering fields |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `role` | array | Role UUID or name. Repeat to filter by several roles. |
    | `search_string` | string | Search string for user |
    | `user` | string (uuid) | User UUID |
    | `user_slug` | string | User slug |
    | `user_url` | string | User URL |
    | `username` | string | User username |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `expiration_time` | string (date-time) |  |
    | `role_name` | string |  |
    | `role_uuid` | string (uuid) |  |
    | `user_email` | string (email) |  |
    | `user_full_name` | string |  |
    | `user_username` | string | Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters |
    | `user_uuid` | string (uuid) |  |
    | `user_image` | string (uri) |  |
    | `created_by_full_name` | string |  |
    | `created_by_uuid` | string (uuid) |  |
    | `source` | string |  |

---

### Grant a role to a user

Assigns a specific role to a user within the current scope. An optional expiration time for the role can be set.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/add_user/ \
      Authorization:"Token YOUR_API_TOKEN" \
      role="string-value" \
      user="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.user_role_create_request import UserRoleCreateRequest # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_add_user # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = UserRoleCreateRequest(
        role="string-value",
        user="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = proposal_protected_calls_add_user.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`UserRoleCreateRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/user_role_create_request.py)
    2.  **API Source:** [`proposal_protected_calls_add_user`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_add_user.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsAddUser } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsAddUser({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "role": "string-value",
        "user": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Request Body (required)"

    | Field | Type | Required |
    |---|---|---|
    | `role` | string | ✓ |
    | `user` | string (uuid) | ✓ |
    | `expiration_time` | string (date-time) |  |


=== "Responses"

    **`201`** - 
    
    | Field | Type |
    |---|---|
    | `expiration_time` | string (date-time) |
    
    ---
    
    **`400`** - Validation error, for example when trying to add a user to a terminated project.
    

---

### Revoke a role from a user

Removes a specific role from a user within the current scope. This effectively revokes their permissions associated with that role.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/delete_user/ \
      Authorization:"Token YOUR_API_TOKEN" \
      role="string-value" \
      user="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.user_role_delete_request import UserRoleDeleteRequest # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_delete_user # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = UserRoleDeleteRequest(
        role="string-value",
        user="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = proposal_protected_calls_delete_user.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`UserRoleDeleteRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/user_role_delete_request.py)
    2.  **API Source:** [`proposal_protected_calls_delete_user`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_delete_user.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsDeleteUser } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsDeleteUser({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "role": "string-value",
        "user": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Request Body (required)"

    | Field | Type | Required |
    |---|---|---|
    | `role` | string | ✓ |
    | `user` | string (uuid) | ✓ |
    | `expiration_time` | string (date-time) |  |


=== "Responses"

    **`200`** - Role revoked successfully.
    

---

### Update a user's role expiration

Updates the expiration time for a user's existing role in the current scope. This is useful for extending or shortening the duration of a permission. To make a role permanent, set expiration_time to null.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/update_user/ \
      Authorization:"Token YOUR_API_TOKEN" \
      role="string-value" \
      user="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.user_role_update_request import UserRoleUpdateRequest # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_update_user # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = UserRoleUpdateRequest(
        role="string-value",
        user="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = proposal_protected_calls_update_user.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`UserRoleUpdateRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/user_role_update_request.py)
    2.  **API Source:** [`proposal_protected_calls_update_user`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_update_user.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsUpdateUser } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsUpdateUser({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "role": "string-value",
        "user": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Request Body (required)"

    | Field | Type | Required |
    |---|---|---|
    | `role` | string | ✓ |
    | `user` | string (uuid) | ✓ |
    | `expiration_time` | string (date-time) |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `expiration_time` | string (date-time) |

---

## Other Actions


### Get affinity matrix for reviewer-proposal matching

Get affinity matrix for reviewer-proposal matching.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/affinity-matrix/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.affinity_matrix_response_scope_enum import AffinityMatrixResponseScopeEnum # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_affinity_matrix_retrieve # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_affinity_matrix_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`AffinityMatrixResponseScopeEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/affinity_matrix_response_scope_enum.py)
    2.  **API Source:** [`proposal_protected_calls_affinity_matrix_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_affinity_matrix_retrieve.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsAffinityMatrixRetrieve } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsAffinityMatrixRetrieve({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Query Parameters"

    | Name | Type | Description |
    |---|---|---|
    | `scope` | string | Filter by reviewer source: 'pool' (accepted reviewers), 'suggestions' (suggested reviewers), or 'all' (both). Default: 'pool'<br>_Enum: `all`, `pool`, `suggestions`_ |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `count` | integer |
    | `results` | array of objects |
    | `results.uuid` | string (uuid) |
    | `results.reviewer_uuid` | string (uuid) |
    | `results.reviewer_name` | string |
    | `results.proposal_uuid` | string (uuid) |
    | `results.proposal_name` | string |
    | `results.affinity_score` | number (double) |
    | `results.keyword_score` | number (double) |
    | `results.text_score` | number (double) |
    | `results.has_conflict` | boolean |
    | `results.coi_type` | string |
    | `results.coi_severity` | string |
    | `results.coi_status` | string |
    | `results.source` | string |

---

### Get available compliance checklists for call creation/editing

Get available compliance checklists for call creation/editing.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/proposal-protected-calls/available_compliance_checklists/ \
      Authorization:"Token YOUR_API_TOKEN" \
      customer_uuid=="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.call_states import CallStates # (1)
    from waldur_api_client.models.protected_call_o_enum import ProtectedCallOEnum # (2)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_available_compliance_checklists_list # (3)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_available_compliance_checklists_list.sync(
        client=client,
        customer_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`CallStates`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/call_states.py)
    2.  **Model Source:** [`ProtectedCallOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/protected_call_o_enum.py)
    3.  **API Source:** [`proposal_protected_calls_available_compliance_checklists_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_available_compliance_checklists_list.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsAvailableComplianceChecklistsList } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsAvailableComplianceChecklistsList({
      auth: "Token YOUR_API_TOKEN",
      query: {
        "customer_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Query Parameters"

    | Name | Type | Required | Description |
    |---|---|---|---|
    | `checklist_type` | string |  | Filter by checklist type (default: proposal_compliance) |
    | `customer` | string (uri) |  |  |
    | `customer_keyword` | string |  |  |
    | `customer_uuid` | string | ✓ | Customer UUID to check permissions for. Required to verify user has CREATE_CALL permission on that customer's call managing organization. |
    | `has_active_round` | boolean |  |  |
    | `name` | string |  |  |
    | `o` | array |  | Ordering<br><br> |
    | `offering_uuid` | string (uuid) |  |  |
    | `offerings_provider_uuid` | string (uuid) |  |  |
    | `open_for_offering_uuid` | string (uuid) |  | Calls the offering can be requested through right now |
    | `page` | integer |  | A page number within the paginated result set. |
    | `page_size` | integer |  | Number of results to return per page. |
    | `slug` | string |  | Slug |
    | `state` | array |  |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `name` | string |
    | `description` | string |
    | `checklist_type` | string |
    | `questions_count` | integer |
    | `category_name` | string |
    | `category_uuid` | string (uuid) |

---

### Get COI configuration for this call

Get COI configuration for this call.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/coi-configuration/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_coi_configuration_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_coi_configuration_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`proposal_protected_calls_coi_configuration_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_coi_configuration_retrieve.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsCoiConfigurationRetrieve } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsCoiConfigurationRetrieve({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `call` | string (uri) |  |
    | `call_uuid` | string (uuid) |  |
    | `call_name` | string |  |
    | `coauthorship_lookback_years` | integer | Years to look back for co-authorship detection |
    | `coauthorship_threshold_papers` | integer | Minimum shared papers to trigger COI |
    | `institutional_lookback_years` | integer | Years to look back for former institution detection |
    | `include_same_department` | boolean | Detect same-department as COI |
    | `include_same_institution` | boolean | Detect same-institution as COI |
    | `recusal_required_types` | array of strings | COI types requiring automatic recusal |
    | `management_allowed_types` | array of strings | COI types allowing management plan |
    | `disclosure_only_types` | array of strings | COI types requiring disclosure only |
    | `auto_detect_coauthorship` | boolean | Enable automated co-authorship detection |
    | `auto_detect_institutional` | boolean | Enable automated institutional affiliation detection |
    | `auto_detect_named_personnel` | boolean | Enable detection of reviewer named in proposals |
    | `invitation_proposal_disclosure` | any | Level of proposal information disclosed in reviewer invitations |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Compliance overview

Get compliance overview for call manager showing all proposals and their compliance status.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/compliance_overview/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_compliance_overview_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_compliance_overview_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`proposal_protected_calls_compliance_overview_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_compliance_overview_retrieve.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsComplianceOverviewRetrieve } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsComplianceOverviewRetrieve({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `checklist` | any |
    | `proposals` | array of objects |
    | `proposals.uuid` | string (uuid) |
    | `proposals.name` | string |
    | `proposals.state` | string |
    | `proposals.created_by` | string |
    | `proposals.created_by_uuid` | string (uuid) |
    | `proposals.compliance` | any |

---

### Get summary statistics of conflicts for this call

Get summary statistics of conflicts for this call.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/conflict-summary/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_conflict_summary_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_conflict_summary_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`proposal_protected_calls_conflict_summary_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_conflict_summary_retrieve.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsConflictSummaryRetrieve } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsConflictSummaryRetrieve({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `total` | integer |
    | `by_status` | object (free-form) |
    | `by_severity` | object (free-form) |
    | `by_type` | object (free-form) |

---

### List all conflicts of interest detected for this call

List all conflicts of interest detected for this call.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/conflicts/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.call_states import CallStates # (1)
    from waldur_api_client.models.protected_call_o_enum import ProtectedCallOEnum # (2)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_conflicts_list # (3)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_conflicts_list.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`CallStates`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/call_states.py)
    2.  **Model Source:** [`ProtectedCallOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/protected_call_o_enum.py)
    3.  **API Source:** [`proposal_protected_calls_conflicts_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_conflicts_list.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsConflictsList } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsConflictsList({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Query Parameters"

    | Name | Type | Description |
    |---|---|---|
    | `customer` | string (uri) |  |
    | `customer_keyword` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `has_active_round` | boolean |  |
    | `name` | string |  |
    | `o` | array | Ordering<br><br> |
    | `offering_uuid` | string (uuid) |  |
    | `offerings_provider_uuid` | string (uuid) |  |
    | `open_for_offering_uuid` | string (uuid) | Calls the offering can be requested through right now |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `slug` | string | Slug |
    | `state` | array |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `reviewer` | string (uri) |  |
    | `reviewer_uuid` | string (uuid) |  |
    | `reviewer_name` | string |  |
    | `proposal` | string (uri) |  |
    | `proposal_uuid` | string (uuid) |  |
    | `proposal_name` | string |  |
    | `round_uuid` | string (uuid) |  |
    | `round_name` | string |  |
    | `call` | string (uri) |  |
    | `call_uuid` | string (uuid) |  |
    | `call_name` | string |  |
    | `coi_type` | any |  |
    | `coi_type_display` | string |  |
    | `severity` | any |  |
    | `severity_display` | string |  |
    | `detection_method` | any |  |
    | `detected_at` | string (date-time) |  |
    | `evidence_description` | string |  |
    | `evidence_data` | object (free-form) | Structured evidence: {"papers": [...], "affiliation_overlap": {...}} |
    | `status` | any |  |
    | `status_display` | string |  |
    | `reviewed_by` | string (uri) |  |
    | `reviewed_by_name` | string |  |
    | `reviewed_at` | string (date-time) |  |
    | `review_notes` | string |  |
    | `management_plan` | string | If waived, how is it managed |
    | `conflicting_user` | string (uri) | Specific person causing conflict |
    | `conflicting_user_name` | string |  |
    | `conflicting_organization` | string (uri) |  |
    | `conflicting_organization_name` | string |  |
    | `created` | string (date-time) |  |

---

### Get call manager dashboard stats

Returns counts for the call manager dashboard: pending assessments, active calls managed by the user, and reviews on calls they manage that are due within the next few days.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/proposal-protected-calls/dashboard-stats/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_dashboard_stats_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_dashboard_stats_retrieve.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`proposal_protected_calls_dashboard_stats_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_dashboard_stats_retrieve.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsDashboardStatsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsDashboardStatsRetrieve({
      auth: "Token YOUR_API_TOKEN"
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `pending_assessments` | integer |
    | `active_calls` | integer |
    | `reviews_due_soon` | integer |
    | `reviews_due_within_days` | integer |

---

### Export proposals

Download the call's proposals as CSV, one row per proposal, with one column per requested offering component. The column set is derived from the call, so it is the same for every row and between exports of the same call.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/export-proposals/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.proposal_states import ProposalStates # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_export_proposals # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_export_proposals.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ProposalStates`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/proposal_states.py)
    2.  **API Source:** [`proposal_protected_calls_export_proposals`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_export_proposals.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsExportProposals } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsExportProposals({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Query Parameters"

    | Name | Type | Description |
    |---|---|---|
    | `created_by_uuid` | string (uuid) | Limit the export to one applicant. |
    | `proposal_name` | string | Limit the export to proposals whose name contains this text — the list's search box. Named proposal_name because a bare `name` is read by the call's own filterset. |
    | `proposal_state` | array | Limit the export to proposals in these states. |
    | `round_uuid` | string (uuid) | Limit the export to one round. |


=== "Responses"

    **`200`** - 
    

---

### Export reviews

Download the call's reviews as CSV, one row per review. The reviewer's private comment is never included: the export is open to call managers, and the review API keeps that field from them.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/export-reviews/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.proposal_review_state_enum import ProposalReviewStateEnum # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_export_reviews # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_export_reviews.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ProposalReviewStateEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/proposal_review_state_enum.py)
    2.  **API Source:** [`proposal_protected_calls_export_reviews`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_export_reviews.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsExportReviews } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsExportReviews({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Query Parameters"

    | Name | Type | Description |
    |---|---|---|
    | `proposal_name` | string | Limit the export to proposals whose name contains this text — the list's search box. Named proposal_name because a bare `name` is read by the call's own filterset. |
    | `proposal_uuid` | string (uuid) | Limit the export to one proposal. |
    | `review_state` | array | Limit the export to reviews in these states. |
    | `reviewer_uuid` | string (uuid) | Limit the export to one reviewer. |
    | `round_uuid` | string (uuid) | Limit the export to one round. |


=== "Responses"

    **`200`** - 
    

---

### Get or update matching configuration for this call

Get or update matching configuration for this call.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/matching-configuration/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_matching_configuration_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_matching_configuration_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`proposal_protected_calls_matching_configuration_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_matching_configuration_retrieve.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsMatchingConfigurationRetrieve } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsMatchingConfigurationRetrieve({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `call_uuid` | string (uuid) |  |
    | `call_name` | string |  |
    | `affinity_method` | string | <br>_Enum: `keyword`, `tfidf`, `combined`_ |
    | `keyword_weight` | number (double) |  |
    | `text_weight` | number (double) |  |
    | `min_reviewers_per_proposal` | integer |  |
    | `max_reviewers_per_proposal` | integer |  |
    | `min_proposals_per_reviewer` | integer |  |
    | `max_proposals_per_reviewer` | integer |  |
    | `algorithm` | string | <br>_Enum: `minmax`, `fairflow`, `hungarian`_ |
    | `min_affinity_threshold` | number (double) | Minimum affinity score for FairFlow algorithm |
    | `use_reviewer_bids` | boolean |  |
    | `bid_weight` | number (double) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### List offerings for a call

List offerings for a call.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/offerings/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_offerings_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_offerings_list.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`proposal_protected_calls_offerings_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_offerings_list.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsOfferingsList } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsOfferingsList({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Query Parameters"

    | Name | Type | Description |
    |---|---|---|
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `state` | string | Filter by state |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `state` | any |  |
    | `offering` | string (uri) |  |
    | `offering_name` | string |  |
    | `offering_uuid` | string (uuid) |  |
    | `offering_type` | string |  |
    | `provider_name` | string |  |
    | `category_uuid` | string (uuid) |  |
    | `category_name` | string |  |
    | `call_managing_organisation` | string |  |
    | `attributes` | object (free-form) |  |
    | `plan` | string (uri) |  |
    | `plan_details` | any |  |
    | `options` | any |  |
    | `components` | array of objects |  |
    | `components.uuid` | string (uuid) |  |
    | `components.offering_uuid` | string (uuid) |  |
    | `components.billing_type` | string | <br>_Enum: `fixed`, `usage`, `limit`, `one`, `few`_ |
    | `components.type` | string | Unique internal name of the measured unit, for example floating_ip. |
    | `components.name` | string | Display name for the measured unit, for example, Floating IP. |
    | `components.description` | string |  |
    | `components.measured_unit` | string | Unit of measurement, for example, GB. |
    | `components.unit_factor` | integer | The conversion factor from backend units to measured_unit |
    | `components.limit_period` | any |  |
    | `components.limit_amount` | number (double) |  |
    | `components.limit_decimal_places` | integer | Number of decimal places accepted for this component's limit. 0 keeps the limit integer-only. |
    | `components.article_code` | string |  |
    | `components.max_value` | number (double) |  |
    | `components.min_value` | number (double) |  |
    | `components.max_available_limit` | number (double) |  |
    | `components.is_boolean` | boolean |  |
    | `components.default_limit` | number (double) |  |
    | `components.factor` | integer |  |
    | `components.is_builtin` | boolean | The API's older name for ``billed_per_plan``.  It used to ask the plugin registry whether this component's type is one the plugin declares, which left out the OpenStack per-volume-type quotas: they are created by the volume type sync rather than declared, so the API called them provider components while the billing resolver treated them as builtin. Reading the stored flag makes the two agree. |
    | `components.is_prepaid` | boolean |  |
    | `components.overage_component` | string (uuid) |  |
    | `components.min_prepaid_duration` | integer |  |
    | `components.max_prepaid_duration` | integer |  |
    | `components.prepaid_duration_step` | integer | Step size in months for the initial prepaid duration at order creation. If set, only multiples of this value (starting from min_prepaid_duration) are valid. Defaults to 1 (any value between min and max). |
    | `components.min_renewal_duration` | integer | Minimum number of months allowed for a renewal. |
    | `components.max_renewal_duration` | integer | Maximum number of months allowed for a renewal. |
    | `components.renewal_duration_step` | integer | Step size in months for renewal. Only multiples of this value (starting from min_renewal_duration) are valid. Defaults to 1. |
    | `require_purchase_order` | boolean | Whether a purchase order must accompany a resource request for this offering before the proposal can be submitted. Defaults to the offering's require_purchase_order_upload, and stays under the call manager's control afterwards. |
    | `created` | string (date-time) |  |
    | `url` | string |  |
    | `approved_by` | string (uri) |  |
    | `created_by` | string (uri) |  |
    | `created_by_name` | string |  |
    | `approved_by_name` | string |  |
    | `description` | string |  |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/proposal-protected-calls/string-value/offerings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_offerings_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_offerings_retrieve.sync(
        obj_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        uuid="string-value",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`proposal_protected_calls_offerings_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_offerings_retrieve.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsOfferingsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsOfferingsRetrieve({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "obj_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "uuid": "string-value"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `obj_uuid` | string | ✓ |
    | `uuid` | string | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `state` | any |  |
    | `offering` | string (uri) |  |
    | `offering_name` | string |  |
    | `offering_uuid` | string (uuid) |  |
    | `offering_type` | string |  |
    | `provider_name` | string |  |
    | `category_uuid` | string (uuid) |  |
    | `category_name` | string |  |
    | `call_managing_organisation` | string |  |
    | `attributes` | object (free-form) |  |
    | `plan` | string (uri) |  |
    | `plan_details` | any |  |
    | `options` | any |  |
    | `components` | array of objects |  |
    | `components.uuid` | string (uuid) |  |
    | `components.offering_uuid` | string (uuid) |  |
    | `components.billing_type` | string | <br>_Enum: `fixed`, `usage`, `limit`, `one`, `few`_ |
    | `components.type` | string | Unique internal name of the measured unit, for example floating_ip. |
    | `components.name` | string | Display name for the measured unit, for example, Floating IP. |
    | `components.description` | string |  |
    | `components.measured_unit` | string | Unit of measurement, for example, GB. |
    | `components.unit_factor` | integer | The conversion factor from backend units to measured_unit |
    | `components.limit_period` | any |  |
    | `components.limit_amount` | number (double) |  |
    | `components.limit_decimal_places` | integer | Number of decimal places accepted for this component's limit. 0 keeps the limit integer-only. |
    | `components.article_code` | string |  |
    | `components.max_value` | number (double) |  |
    | `components.min_value` | number (double) |  |
    | `components.max_available_limit` | number (double) |  |
    | `components.is_boolean` | boolean |  |
    | `components.default_limit` | number (double) |  |
    | `components.factor` | integer |  |
    | `components.is_builtin` | boolean | The API's older name for ``billed_per_plan``.  It used to ask the plugin registry whether this component's type is one the plugin declares, which left out the OpenStack per-volume-type quotas: they are created by the volume type sync rather than declared, so the API called them provider components while the billing resolver treated them as builtin. Reading the stored flag makes the two agree. |
    | `components.is_prepaid` | boolean |  |
    | `components.overage_component` | string (uuid) |  |
    | `components.min_prepaid_duration` | integer |  |
    | `components.max_prepaid_duration` | integer |  |
    | `components.prepaid_duration_step` | integer | Step size in months for the initial prepaid duration at order creation. If set, only multiples of this value (starting from min_prepaid_duration) are valid. Defaults to 1 (any value between min and max). |
    | `components.min_renewal_duration` | integer | Minimum number of months allowed for a renewal. |
    | `components.max_renewal_duration` | integer | Maximum number of months allowed for a renewal. |
    | `components.renewal_duration_step` | integer | Step size in months for renewal. Only multiples of this value (starting from min_renewal_duration) are valid. Defaults to 1. |
    | `require_purchase_order` | boolean | Whether a purchase order must accompany a resource request for this offering before the proposal can be submitted. Defaults to the offering's require_purchase_order_upload, and stays under the call manager's control afterwards. |
    | `created` | string (date-time) |  |
    | `url` | string |  |
    | `approved_by` | string (uri) |  |
    | `created_by` | string (uri) |  |
    | `created_by_name` | string |  |
    | `approved_by_name` | string |  |
    | `description` | string |  |

---

### Get detailed compliance answers for a specific proposal (call managers only)

Get detailed compliance answers for a specific proposal (call managers only).


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/proposals/a1b2c3d4-e5f6-7890-abcd-ef1234567890/compliance-answers/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.call_states import CallStates # (1)
    from waldur_api_client.models.protected_call_o_enum import ProtectedCallOEnum # (2)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_proposals_compliance_answers_list # (3)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_proposals_compliance_answers_list.sync(
        proposal_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`CallStates`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/call_states.py)
    2.  **Model Source:** [`ProtectedCallOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/protected_call_o_enum.py)
    3.  **API Source:** [`proposal_protected_calls_proposals_compliance_answers_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_proposals_compliance_answers_list.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsProposalsComplianceAnswersList } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsProposalsComplianceAnswersList({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "proposal_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required | Description |
    |---|---|---|---|
    | `proposal_uuid` | string | ✓ | UUID of the proposal |
    | `uuid` | string (uuid) | ✓ |  |


=== "Query Parameters"

    | Name | Type | Description |
    |---|---|---|
    | `customer` | string (uri) |  |
    | `customer_keyword` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `has_active_round` | boolean |  |
    | `name` | string |  |
    | `o` | array | Ordering<br><br> |
    | `offering_uuid` | string (uuid) |  |
    | `offerings_provider_uuid` | string (uuid) |  |
    | `open_for_offering_uuid` | string (uuid) | Calls the offering can be requested through right now |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `slug` | string | Slug |
    | `state` | array |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `question_description` | string |  |
    | `question_type` | string |  |
    | `question_required` | boolean |  |
    | `answer_data` | object (free-form) | Flexible answer storage for different question types |
    | `requires_review` | boolean | Internal flag - this answer requires additional review |
    | `user` | integer |  |
    | `user_name` | string |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Get proposed reviewer-proposal assignments

Get proposed reviewer-proposal assignments.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/proposed-assignments/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.call_states import CallStates # (1)
    from waldur_api_client.models.protected_call_o_enum import ProtectedCallOEnum # (2)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_proposed_assignments_list # (3)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_proposed_assignments_list.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`CallStates`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/call_states.py)
    2.  **Model Source:** [`ProtectedCallOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/protected_call_o_enum.py)
    3.  **API Source:** [`proposal_protected_calls_proposed_assignments_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_proposed_assignments_list.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsProposedAssignmentsList } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsProposedAssignmentsList({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Query Parameters"

    | Name | Type | Description |
    |---|---|---|
    | `customer` | string (uri) |  |
    | `customer_keyword` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `has_active_round` | boolean |  |
    | `name` | string |  |
    | `o` | array | Ordering<br><br> |
    | `offering_uuid` | string (uuid) |  |
    | `offerings_provider_uuid` | string (uuid) |  |
    | `open_for_offering_uuid` | string (uuid) | Calls the offering can be requested through right now |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `slug` | string | Slug |
    | `state` | array |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `call` | string (uri) |  |
    | `reviewer` | string (uri) |  |
    | `reviewer_uuid` | string (uuid) |  |
    | `reviewer_name` | string |  |
    | `proposal` | string (uri) |  |
    | `proposal_uuid` | string (uuid) |  |
    | `proposal_name` | string |  |
    | `affinity_score` | number (double) |  |
    | `algorithm_used` | any |  |
    | `rank` | integer | Assignment rank (1 = best match) |
    | `is_deployed` | boolean |  |
    | `deployed_at` | string (date-time) |  |
    | `deployed_by` | string (uri) |  |
    | `deployed_by_name` | string |  |
    | `created` | string (date-time) |  |

---

### List resource templates for a call

List resource templates for a call.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/resource_templates/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_resource_templates_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_resource_templates_list.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`proposal_protected_calls_resource_templates_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_resource_templates_list.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsResourceTemplatesList } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsResourceTemplatesList({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Query Parameters"

    | Name | Type | Description |
    |---|---|---|
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string |  |
    | `name` | string |  |
    | `description` | string |  |
    | `attributes` | object (free-form) |  |
    | `limits` | object (free-form) |  |
    | `is_required` | boolean | If True, every proposal must include this resource type |
    | `requested_offering` | string (uri) |  |
    | `requested_offering_name` | string |  |
    | `requested_offering_uuid` | string (uuid) |  |
    | `requested_offering_plan` | any |  |
    | `requested_offering_type` | string |  |
    | `requested_offering_components` | array of objects |  |
    | `requested_offering_components.uuid` | string (uuid) |  |
    | `requested_offering_components.offering_uuid` | string (uuid) |  |
    | `requested_offering_components.billing_type` | string | <br>_Enum: `fixed`, `usage`, `limit`, `one`, `few`_ |
    | `requested_offering_components.type` | string | Unique internal name of the measured unit, for example floating_ip. |
    | `requested_offering_components.name` | string | Display name for the measured unit, for example, Floating IP. |
    | `requested_offering_components.description` | string |  |
    | `requested_offering_components.measured_unit` | string | Unit of measurement, for example, GB. |
    | `requested_offering_components.unit_factor` | integer | The conversion factor from backend units to measured_unit |
    | `requested_offering_components.limit_period` | any |  |
    | `requested_offering_components.limit_amount` | number (double) |  |
    | `requested_offering_components.limit_decimal_places` | integer | Number of decimal places accepted for this component's limit. 0 keeps the limit integer-only. |
    | `requested_offering_components.article_code` | string |  |
    | `requested_offering_components.max_value` | number (double) |  |
    | `requested_offering_components.min_value` | number (double) |  |
    | `requested_offering_components.max_available_limit` | number (double) |  |
    | `requested_offering_components.is_boolean` | boolean |  |
    | `requested_offering_components.default_limit` | number (double) |  |
    | `requested_offering_components.factor` | integer |  |
    | `requested_offering_components.is_builtin` | boolean | The API's older name for ``billed_per_plan``.  It used to ask the plugin registry whether this component's type is one the plugin declares, which left out the OpenStack per-volume-type quotas: they are created by the volume type sync rather than declared, so the API called them provider components while the billing resolver treated them as builtin. Reading the stored flag makes the two agree. |
    | `requested_offering_components.is_prepaid` | boolean |  |
    | `requested_offering_components.overage_component` | string (uuid) |  |
    | `requested_offering_components.min_prepaid_duration` | integer |  |
    | `requested_offering_components.max_prepaid_duration` | integer |  |
    | `requested_offering_components.prepaid_duration_step` | integer | Step size in months for the initial prepaid duration at order creation. If set, only multiples of this value (starting from min_prepaid_duration) are valid. Defaults to 1 (any value between min and max). |
    | `requested_offering_components.min_renewal_duration` | integer | Minimum number of months allowed for a renewal. |
    | `requested_offering_components.max_renewal_duration` | integer | Maximum number of months allowed for a renewal. |
    | `requested_offering_components.renewal_duration_step` | integer | Step size in months for renewal. Only multiples of this value (starting from min_renewal_duration) are valid. Defaults to 1. |
    | `created_by` | string (uri) |  |
    | `created_by_name` | string |  |
    | `created` | string (date-time) |  |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/proposal-protected-calls/string-value/resource_templates/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_resource_templates_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_resource_templates_retrieve.sync(
        obj_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        uuid="string-value",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`proposal_protected_calls_resource_templates_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_resource_templates_retrieve.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsResourceTemplatesRetrieve } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsResourceTemplatesRetrieve({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "obj_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "uuid": "string-value"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `obj_uuid` | string | ✓ |
    | `uuid` | string | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string |  |
    | `name` | string |  |
    | `description` | string |  |
    | `attributes` | object (free-form) |  |
    | `limits` | object (free-form) |  |
    | `is_required` | boolean | If True, every proposal must include this resource type |
    | `requested_offering` | string (uri) |  |
    | `requested_offering_name` | string |  |
    | `requested_offering_uuid` | string (uuid) |  |
    | `requested_offering_plan` | any |  |
    | `requested_offering_type` | string |  |
    | `requested_offering_components` | array of objects |  |
    | `requested_offering_components.uuid` | string (uuid) |  |
    | `requested_offering_components.offering_uuid` | string (uuid) |  |
    | `requested_offering_components.billing_type` | string | <br>_Enum: `fixed`, `usage`, `limit`, `one`, `few`_ |
    | `requested_offering_components.type` | string | Unique internal name of the measured unit, for example floating_ip. |
    | `requested_offering_components.name` | string | Display name for the measured unit, for example, Floating IP. |
    | `requested_offering_components.description` | string |  |
    | `requested_offering_components.measured_unit` | string | Unit of measurement, for example, GB. |
    | `requested_offering_components.unit_factor` | integer | The conversion factor from backend units to measured_unit |
    | `requested_offering_components.limit_period` | any |  |
    | `requested_offering_components.limit_amount` | number (double) |  |
    | `requested_offering_components.limit_decimal_places` | integer | Number of decimal places accepted for this component's limit. 0 keeps the limit integer-only. |
    | `requested_offering_components.article_code` | string |  |
    | `requested_offering_components.max_value` | number (double) |  |
    | `requested_offering_components.min_value` | number (double) |  |
    | `requested_offering_components.max_available_limit` | number (double) |  |
    | `requested_offering_components.is_boolean` | boolean |  |
    | `requested_offering_components.default_limit` | number (double) |  |
    | `requested_offering_components.factor` | integer |  |
    | `requested_offering_components.is_builtin` | boolean | The API's older name for ``billed_per_plan``.  It used to ask the plugin registry whether this component's type is one the plugin declares, which left out the OpenStack per-volume-type quotas: they are created by the volume type sync rather than declared, so the API called them provider components while the billing resolver treated them as builtin. Reading the stored flag makes the two agree. |
    | `requested_offering_components.is_prepaid` | boolean |  |
    | `requested_offering_components.overage_component` | string (uuid) |  |
    | `requested_offering_components.min_prepaid_duration` | integer |  |
    | `requested_offering_components.max_prepaid_duration` | integer |  |
    | `requested_offering_components.prepaid_duration_step` | integer | Step size in months for the initial prepaid duration at order creation. If set, only multiples of this value (starting from min_prepaid_duration) are valid. Defaults to 1 (any value between min and max). |
    | `requested_offering_components.min_renewal_duration` | integer | Minimum number of months allowed for a renewal. |
    | `requested_offering_components.max_renewal_duration` | integer | Maximum number of months allowed for a renewal. |
    | `requested_offering_components.renewal_duration_step` | integer | Step size in months for renewal. Only multiples of this value (starting from min_renewal_duration) are valid. Defaults to 1. |
    | `created_by` | string (uri) |  |
    | `created_by_name` | string |  |
    | `created` | string (date-time) |  |

---

### List reviewer pool members for a call

List reviewer pool members for a call.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/reviewer-pool/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_reviewer_pool_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_reviewer_pool_list.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`proposal_protected_calls_reviewer_pool_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_reviewer_pool_list.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsReviewerPoolList } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsReviewerPoolList({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Query Parameters"

    | Name | Type | Description |
    |---|---|---|
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `call` | string (uri) |  |
    | `call_uuid` | string (uuid) |  |
    | `call_name` | string |  |
    | `reviewer` | string (uri) |  |
    | `reviewer_uuid` | string | Get reviewer profile UUID if available. |
    | `reviewer_name` | string | Get reviewer name from profile or invited_user. |
    | `reviewer_email` | string | Get email from profile, invited_user, or invited_email. |
    | `has_profile` | boolean | Check if reviewer has a profile. |
    | `invited_email` | string (email) | Email address for direct invitations |
    | `invited_user` | string (uri) | Waldur user if email matches existing account |
    | `invited_user_name` | string |  |
    | `invited_at` | string (date-time) |  |
    | `invitation_status` | any |  |
    | `invitation_status_display` | string |  |
    | `response_date` | string (date-time) |  |
    | `decline_reason` | string |  |
    | `max_assignments` | integer |  |
    | `current_assignments` | integer | Number of the reviewer's open assignments in this call: pending or accepted assignment items whose review is not finished, plus reviews in progress created without an assignment item. |
    | `expertise_match_score` | number (double) | Calculated affinity to call topics (0-1) |
    | `invited_by_name` | string |  |
    | `invitation_link` | string |  |
    | `invitation_expires_at` | string (date-time) |  |
    | `created` | string (date-time) |  |
    | `coi_count` | integer | Count total COIs for this reviewer in this call. |
    | `coi_by_severity` | object (free-form) | Count COIs by severity level. |
    | `reviews_pending` | integer | Legacy field - always returns 0.  Previously counted reviews in 'created' state, but that state has been removed. Reviews are now created directly in 'in_review' state. Kept for backwards compatibility with frontend. |
    | `reviews_in_progress` | integer | Count reviews in 'in_review' state. |
    | `reviews_completed` | integer | Count reviews in 'submitted' state. |
    | `override_reason` | string | Reason for manager override of invitation status. |
    | `overridden_by_name` | string |  |
    | `overridden_at` | string (date-time) |  |

---

### List rounds for a call

List rounds for a call.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/rounds/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_rounds_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_rounds_list.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`proposal_protected_calls_rounds_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_rounds_list.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsRoundsList } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsRoundsList({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Query Parameters"

    | Name | Type | Description |
    |---|---|---|
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `slug` | string |  |
    | `name` | string |  |
    | `start_time` | string (date-time) |  |
    | `cutoff_time` | string (date-time) |  |
    | `status` | any |  |
    | `allocation_date` | string (date-time) |  |
    | `review_duration_in_days` | integer |  |
    | `lifecycle_state` | any | Where the round stands after its cut-off: evaluating, deciding, results_published or closed. Empty before the cut-off. |
    | `evaluation_started_at` | string (date-time) |  |
    | `deciding_started_at` | string (date-time) |  |
    | `results_published_at` | string (date-time) |  |
    | `closed_at` | string (date-time) |  |
    | `url` | string |  |
    | `proposals` | array of objects |  |
    | `proposals.uuid` | string (uuid) |  |
    | `proposals.slug` | string |  |
    | `proposals.name` | string |  |
    | `proposals.state` | any |  |
    | `proposals.reviews` | array of anys | Return serialized reviews based on user permissions and visibility settings. - Staff, call managers, and reviewers see all reviews. - Submitters see submitted reviews if visibility is enabled. |
    | `proposals.approved_by_name` | string |  |
    | `proposals.created_by_name` | string |  |
    | `proposals.created` | string (date-time) |  |
    | `results_published_by_name` | string |  |
    | `held_decisions_count` | integer | Proposals of the round whose decision is recorded but not yet published. After publication, decisions that could not be carried out; publishing the results again retries them. Null for anyone who may not see held decisions. |
    | `has_proposals` | boolean | Whether the round holds any proposal, in any state. A round with proposals cannot be deleted. Unlike the proposals list, which leaves out what the viewer may not see, this counts every one. |
    | `results_forced_reason` | string | Why results were published while some proposals of the round still had no decision. |
    | `adopted_at` | string (date) | When the round's results were adopted. |
    | `adoption_note` | string |  |
    | `adoption_document` | string (uri) |  |
    | `undecided_at_round_completion` | any | Overrides the call's rule for proposals still without a decision when the round is completed. Empty: the call's rule applies. |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/proposal-protected-calls/string-value/rounds/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_rounds_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_rounds_retrieve.sync(
        obj_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        uuid="string-value",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`proposal_protected_calls_rounds_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_rounds_retrieve.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsRoundsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsRoundsRetrieve({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "obj_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "uuid": "string-value"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `obj_uuid` | string | ✓ |
    | `uuid` | string | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `slug` | string |  |
    | `name` | string |  |
    | `start_time` | string (date-time) |  |
    | `cutoff_time` | string (date-time) |  |
    | `status` | any |  |
    | `allocation_date` | string (date-time) |  |
    | `review_duration_in_days` | integer |  |
    | `lifecycle_state` | any | Where the round stands after its cut-off: evaluating, deciding, results_published or closed. Empty before the cut-off. |
    | `evaluation_started_at` | string (date-time) |  |
    | `deciding_started_at` | string (date-time) |  |
    | `results_published_at` | string (date-time) |  |
    | `closed_at` | string (date-time) |  |
    | `url` | string |  |
    | `proposals` | array of objects |  |
    | `proposals.uuid` | string (uuid) |  |
    | `proposals.slug` | string |  |
    | `proposals.name` | string |  |
    | `proposals.state` | any |  |
    | `proposals.reviews` | array of anys | Return serialized reviews based on user permissions and visibility settings. - Staff, call managers, and reviewers see all reviews. - Submitters see submitted reviews if visibility is enabled. |
    | `proposals.approved_by_name` | string |  |
    | `proposals.created_by_name` | string |  |
    | `proposals.created` | string (date-time) |  |
    | `results_published_by_name` | string |  |
    | `held_decisions_count` | integer | Proposals of the round whose decision is recorded but not yet published. After publication, decisions that could not be carried out; publishing the results again retries them. Null for anyone who may not see held decisions. |
    | `has_proposals` | boolean | Whether the round holds any proposal, in any state. A round with proposals cannot be deleted. Unlike the proposals list, which leaves out what the viewer may not see, this counts every one. |
    | `results_forced_reason` | string | Why results were published while some proposals of the round still had no decision. |
    | `adopted_at` | string (date) | When the round's results were adopted. |
    | `adoption_note` | string |  |
    | `adoption_document` | string (uri) |  |
    | `undecided_at_round_completion` | any | Overrides the call's rule for proposals still without a decision when the round is completed. Empty: the call's rule applies. |

---

### Step checklists

List checklists that can be attached to a workflow step (WORKFLOW_STEP-typed). Available to call managers so the workflow config UI can populate its checklist picker without staff-only access to the checklist admin API.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/proposal-protected-calls/step_checklists/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.call_states import CallStates # (1)
    from waldur_api_client.models.protected_call_o_enum import ProtectedCallOEnum # (2)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_step_checklists_list # (3)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_step_checklists_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`CallStates`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/call_states.py)
    2.  **Model Source:** [`ProtectedCallOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/protected_call_o_enum.py)
    3.  **API Source:** [`proposal_protected_calls_step_checklists_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_step_checklists_list.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsStepChecklistsList } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsStepChecklistsList({
      auth: "Token YOUR_API_TOKEN"
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Query Parameters"

    | Name | Type | Description |
    |---|---|---|
    | `customer` | string (uri) |  |
    | `customer_keyword` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `has_active_round` | boolean |  |
    | `name` | string |  |
    | `o` | array | Ordering<br><br> |
    | `offering_uuid` | string (uuid) |  |
    | `offerings_provider_uuid` | string (uuid) |  |
    | `open_for_offering_uuid` | string (uuid) | Calls the offering can be requested through right now |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `slug` | string | Slug |
    | `state` | array |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `name` | string |
    | `description` | string |
    | `checklist_type` | string |

---

### List all reviewer suggestions for this call with affinity scores

List all reviewer suggestions for this call with affinity scores.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/suggestions/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.call_states import CallStates # (1)
    from waldur_api_client.models.protected_call_o_enum import ProtectedCallOEnum # (2)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_suggestions_list # (3)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_suggestions_list.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`CallStates`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/call_states.py)
    2.  **Model Source:** [`ProtectedCallOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/protected_call_o_enum.py)
    3.  **API Source:** [`proposal_protected_calls_suggestions_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_suggestions_list.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsSuggestionsList } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsSuggestionsList({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Query Parameters"

    | Name | Type | Description |
    |---|---|---|
    | `customer` | string (uri) |  |
    | `customer_keyword` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `has_active_round` | boolean |  |
    | `name` | string |  |
    | `o` | array | Ordering<br><br> |
    | `offering_uuid` | string (uuid) |  |
    | `offerings_provider_uuid` | string (uuid) |  |
    | `open_for_offering_uuid` | string (uuid) | Calls the offering can be requested through right now |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `slug` | string | Slug |
    | `state` | array |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `call` | string (uri) |  |
    | `call_uuid` | string (uuid) |  |
    | `call_name` | string |  |
    | `reviewer` | string (uri) |  |
    | `reviewer_uuid` | string (uuid) |  |
    | `reviewer_name` | string |  |
    | `reviewer_email` | string (email) |  |
    | `reviewer_biography` | string | Professional biography / summary |
    | `affinity_score` | number (double) | Combined affinity score (0-1) |
    | `keyword_score` | number (double) | Keyword matching score |
    | `text_score` | number (double) | TF-IDF text similarity score |
    | `status` | string | <br>_Enum: `pending`, `confirmed`, `rejected`, `invited`_ |
    | `status_display` | string |  |
    | `reviewed_by` | string (uri) |  |
    | `reviewed_by_name` | string |  |
    | `reviewed_at` | string (date-time) |  |
    | `rejection_reason` | string |  |
    | `matched_keywords` | array of strings |  |
    | `top_matching_proposals` | array of objects |  |
    | `top_matching_proposals.uuid` | string (uuid) |  |
    | `top_matching_proposals.name` | string |  |
    | `top_matching_proposals.slug` | string |  |
    | `top_matching_proposals.affinity` | number (double) |  |
    | `top_matching_proposals.keyword_score` | number (double) |  |
    | `top_matching_proposals.text_score` | number (double) |  |
    | `top_matching_proposals.has_coi` | boolean |  |
    | `top_matching_proposals.coi_type` | string |  |
    | `top_matching_proposals.coi_severity` | string |  |
    | `source_type` | any | What content was used to generate this suggestion |
    | `source_type_display` | string |  |
    | `created` | string (date-time) |  |

---

### List workflow steps for a call

List workflow steps for a call.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/workflow_steps/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_workflow_steps_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_workflow_steps_list.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`proposal_protected_calls_workflow_steps_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_workflow_steps_list.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsWorkflowStepsList } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsWorkflowStepsList({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Query Parameters"

    | Name | Type | Description |
    |---|---|---|
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `step` | string | <br>_Enum: `administrative_check`, `technical_assessment`, `expert_review`, `panel_review`, `allocation_decision`, `award_response`_ |
    | `call_uuid` | string (uuid) |  |
    | `call_name` | string |  |
    | `is_enabled` | boolean | Whether this step is enabled. Disabled steps are skipped. |
    | `is_mandatory` | boolean |  |
    | `duration_in_days` | integer | Duration in days. Used to calculate deadlines. |
    | `checklist` | string (uuid) |  |
    | `checklist_name` | string |  |
    | `checklist_required` | boolean | When the step has a checklist, block completion until its required questions are answered. Set False to make the checklist advisory. |
    | `blind_review` | boolean | Evaluators cannot see each other's assessments. |
    | `requires_coi_confirmation` | boolean | Evaluator must confirm absence of conflict of interest. |
    | `min_reviewers` | integer | Minimum reviews required before step can complete. |
    | `min_score_threshold` | string (decimal) | Minimum average score required before this step can complete (a completion gate; it does not auto-reject lower scores). |
    | `applicant_visible` | boolean | Whether the applicant can see step details (not just status). |
    | `responsible_role` | any | Role expected to act on this step. |
    | `transition_mode` | any | How this step advances once a human completes it. 'Automatic' advances to the next step immediately; 'Manual' waits for a separate advance action. Neither auto-decides from review scores. |
    | `include_award_response` | boolean | Allocation decision: require applicant award response after decision. |
    | `allocation_time` | any | Allocation decision: when a granted proposal takes effect — immediately (on_decision) or on the round's allocation date (fixed_date). |
    | `display_order` | integer | Optional override of catalog ordering. |
    | `criteria` | array of objects |  |
    | `criteria.uuid` | string (uuid) |  |
    | `criteria.name` | string |  |
    | `criteria.order` | integer |  |
    | `notification_rules` | array of objects |  |
    | `notification_rules.uuid` | string (uuid) |  |
    | `notification_rules.trigger` | any |  |
    | `notification_rules.recipient` | any |  |
    | `notification_rules.days_before` | integer | Only for deadline_approaching: how many days before the step's deadline the reminder is sent. |
    | `notification_rules.is_enabled` | boolean |  |
    | `notification_rules.notified_proposal_roles` | array of strings |  |
    | `responsible_users` | array of objects |  |
    | `responsible_users.uuid` | string (uuid) |  |
    | `responsible_users.username` | string |  |
    | `responsible_users.full_name` | string |  |
    | `responsible_users.email` | string (email) |  |
    | `responsible_users.is_panel_chair` | boolean |  |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/proposal-protected-calls/string-value/workflow_steps/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_workflow_steps_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_workflow_steps_retrieve.sync(
        obj_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        uuid="string-value",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`proposal_protected_calls_workflow_steps_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_workflow_steps_retrieve.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsWorkflowStepsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsWorkflowStepsRetrieve({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "obj_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "uuid": "string-value"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `obj_uuid` | string | ✓ |
    | `uuid` | string | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `step` | string | <br>_Enum: `administrative_check`, `technical_assessment`, `expert_review`, `panel_review`, `allocation_decision`, `award_response`_ |
    | `call_uuid` | string (uuid) |  |
    | `call_name` | string |  |
    | `is_enabled` | boolean | Whether this step is enabled. Disabled steps are skipped. |
    | `is_mandatory` | boolean |  |
    | `duration_in_days` | integer | Duration in days. Used to calculate deadlines. |
    | `checklist` | string (uuid) |  |
    | `checklist_name` | string |  |
    | `checklist_required` | boolean | When the step has a checklist, block completion until its required questions are answered. Set False to make the checklist advisory. |
    | `blind_review` | boolean | Evaluators cannot see each other's assessments. |
    | `requires_coi_confirmation` | boolean | Evaluator must confirm absence of conflict of interest. |
    | `min_reviewers` | integer | Minimum reviews required before step can complete. |
    | `min_score_threshold` | string (decimal) | Minimum average score required before this step can complete (a completion gate; it does not auto-reject lower scores). |
    | `applicant_visible` | boolean | Whether the applicant can see step details (not just status). |
    | `responsible_role` | any | Role expected to act on this step. |
    | `transition_mode` | any | How this step advances once a human completes it. 'Automatic' advances to the next step immediately; 'Manual' waits for a separate advance action. Neither auto-decides from review scores. |
    | `include_award_response` | boolean | Allocation decision: require applicant award response after decision. |
    | `allocation_time` | any | Allocation decision: when a granted proposal takes effect — immediately (on_decision) or on the round's allocation date (fixed_date). |
    | `display_order` | integer | Optional override of catalog ordering. |
    | `criteria` | array of objects |  |
    | `criteria.uuid` | string (uuid) |  |
    | `criteria.name` | string |  |
    | `criteria.order` | integer |  |
    | `notification_rules` | array of objects |  |
    | `notification_rules.uuid` | string (uuid) |  |
    | `notification_rules.trigger` | any |  |
    | `notification_rules.recipient` | any |  |
    | `notification_rules.days_before` | integer | Only for deadline_approaching: how many days before the step's deadline the reminder is sent. |
    | `notification_rules.is_enabled` | boolean |  |
    | `notification_rules.notified_proposal_roles` | array of strings |  |
    | `responsible_users` | array of objects |  |
    | `responsible_users.uuid` | string (uuid) |  |
    | `responsible_users.username` | string |  |
    | `responsible_users.full_name` | string |  |
    | `responsible_users.email` | string (email) |  |
    | `responsible_users.is_panel_chair` | boolean |  |

---

### Activate a call

Activate a call.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/activate/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_activate # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_activate.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`proposal_protected_calls_activate`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_activate.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsActivate } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsActivate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `message` | string |

---

### Archive a call

Archive a call.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/archive/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_archive # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_archive.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`proposal_protected_calls_archive`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_archive.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsArchive } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsArchive({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `message` | string |

---

### Attach documents to call

Attach documents to call.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/attach_documents/ \
      Authorization:"Token YOUR_API_TOKEN" \
      documents:='[]'
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.call_attach_documents_request import CallAttachDocumentsRequest # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_attach_documents # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = CallAttachDocumentsRequest(
        documents=[]
    )
    response = proposal_protected_calls_attach_documents.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`CallAttachDocumentsRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/call_attach_documents_request.py)
    2.  **API Source:** [`proposal_protected_calls_attach_documents`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_attach_documents.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsAttachDocuments } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsAttachDocuments({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "documents": []
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Request Body (required)"

    | Field | Type | Required |
    |---|---|---|
    | `documents` | array of string (binary)s | ✓ |
    | `description` | string |  |


=== "Responses"

    **`200`** - No response body
    

---

### Compute affinity scores for all reviewer-proposal pairs

Compute affinity scores for all reviewer-proposal pairs.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/compute-affinities/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_compute_affinities # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_compute_affinities.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`proposal_protected_calls_compute_affinities`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_compute_affinities.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsComputeAffinities } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsComputeAffinities({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `computed_count` | integer |
    | `message` | string |

---

### Detach documents from call

Detach documents from call.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/detach_documents/ \
      Authorization:"Token YOUR_API_TOKEN" \
      documents:='[]'
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.call_detach_documents_request import CallDetachDocumentsRequest # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_detach_documents # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = CallDetachDocumentsRequest(
        documents=[]
    )
    response = proposal_protected_calls_detach_documents.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`CallDetachDocumentsRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/call_detach_documents_request.py)
    2.  **API Source:** [`proposal_protected_calls_detach_documents`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_detach_documents.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsDetachDocuments } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsDetachDocuments({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "documents": []
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Request Body (required)"

    | Field | Type | Required |
    |---|---|---|
    | `documents` | array of string (uuid)s | ✓ |


=== "Responses"

    **`200`** - No response body
    

---

### Trigger automated COI detection for all reviewer-proposal pairs

Trigger automated COI detection for all reviewer-proposal pairs.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/detect-conflicts/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.trigger_coi_detection_request import TriggerCOIDetectionRequest # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_detect_conflicts # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = TriggerCOIDetectionRequest()
    response = proposal_protected_calls_detect_conflicts.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`TriggerCOIDetectionRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/trigger_coi_detection_request.py)
    2.  **API Source:** [`proposal_protected_calls_detect_conflicts`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_detect_conflicts.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsDetectConflicts } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsDetectConflicts({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Request Body"

    | Field | Type | Required |
    |---|---|---|
    | `job_type` | any |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string | Return URL for the job detail endpoint. |
    | `uuid` | string (uuid) |  |
    | `call` | string (uri) |  |
    | `call_uuid` | string (uuid) |  |
    | `call_name` | string |  |
    | `job_type` | any |  |
    | `state` | any |  |
    | `total_pairs` | integer |  |
    | `processed_pairs` | integer |  |
    | `progress_percentage` | number (double) |  |
    | `conflicts_found` | integer |  |
    | `started_at` | string (date-time) |  |
    | `completed_at` | string (date-time) |  |
    | `error_message` | string |  |
    | `created` | string (date-time) |  |

---

### Duplicate

Duplicate a call. The new call inherits the source call's configuration (offerings, rounds, workflow steps, resource templates, role mappings, documents, and COI/matching/assignment/applicant-visibility settings) and starts in draft state. Proposals, reviews, team permissions, and reviewer-pool memberships are not copied.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/duplicate/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-proposal-protected-call"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.duplicate_call_request_request import DuplicateCallRequestRequest # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_duplicate # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = DuplicateCallRequestRequest(
        name="my-awesome-proposal-protected-call"
    )
    response = proposal_protected_calls_duplicate.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`DuplicateCallRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/duplicate_call_request_request.py)
    2.  **API Source:** [`proposal_protected_calls_duplicate`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_duplicate.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsDuplicate } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsDuplicate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "name": "my-awesome-proposal-protected-call"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Request Body (required)"

    | Field | Type | Required |
    |---|---|---|
    | `name` | string | ✓ |
    | `copy_documents` | boolean |  |
    | `copy_offerings` | boolean |  |
    | `copy_rounds` | boolean |  |
    | `copy_workflow_steps` | boolean |  |
    | `copy_resource_templates` | boolean |  |
    | `copy_role_mappings` | boolean |  |
    | `copy_applicant_visibility_config` | boolean |  |
    | `copy_proposal_field_config` | boolean |  |
    | `copy_coi_configuration` | boolean |  |
    | `copy_matching_configuration` | boolean |  |
    | `copy_assignment_configuration` | boolean |  |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `start_date` | string (date-time) |  |
    | `end_date` | string (date-time) |  |
    | `slug` | string | URL-friendly identifier. Only editable by staff users. |
    | `name` | string |  |
    | `description` | string |  |
    | `state` | any |  |
    | `manager` | string (uri) |  |
    | `manager_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `offerings` | array of objects |  |
    | `offerings.uuid` | string (uuid) |  |
    | `offerings.state` | any |  |
    | `offerings.offering` | string (uri) |  |
    | `offerings.offering_name` | string |  |
    | `offerings.offering_uuid` | string (uuid) |  |
    | `offerings.offering_type` | string |  |
    | `offerings.provider_name` | string |  |
    | `offerings.category_uuid` | string (uuid) |  |
    | `offerings.category_name` | string |  |
    | `offerings.call_managing_organisation` | string |  |
    | `offerings.attributes` | object (free-form) |  |
    | `offerings.plan` | string (uri) |  |
    | `offerings.plan_details` | any |  |
    | `offerings.options` | any |  |
    | `offerings.components` | array of objects |  |
    | `offerings.components.uuid` | string (uuid) |  |
    | `offerings.components.offering_uuid` | string (uuid) |  |
    | `offerings.components.billing_type` | string | <br>_Enum: `fixed`, `usage`, `limit`, `one`, `few`_ |
    | `offerings.components.type` | string | Unique internal name of the measured unit, for example floating_ip. |
    | `offerings.components.name` | string | Display name for the measured unit, for example, Floating IP. |
    | `offerings.components.description` | string |  |
    | `offerings.components.measured_unit` | string | Unit of measurement, for example, GB. |
    | `offerings.components.unit_factor` | integer | The conversion factor from backend units to measured_unit |
    | `offerings.components.limit_period` | any |  |
    | `offerings.components.limit_amount` | number (double) |  |
    | `offerings.components.limit_decimal_places` | integer | Number of decimal places accepted for this component's limit. 0 keeps the limit integer-only. |
    | `offerings.components.article_code` | string |  |
    | `offerings.components.max_value` | number (double) |  |
    | `offerings.components.min_value` | number (double) |  |
    | `offerings.components.max_available_limit` | number (double) |  |
    | `offerings.components.is_boolean` | boolean |  |
    | `offerings.components.default_limit` | number (double) |  |
    | `offerings.components.factor` | integer |  |
    | `offerings.components.is_builtin` | boolean | The API's older name for ``billed_per_plan``.  It used to ask the plugin registry whether this component's type is one the plugin declares, which left out the OpenStack per-volume-type quotas: they are created by the volume type sync rather than declared, so the API called them provider components while the billing resolver treated them as builtin. Reading the stored flag makes the two agree. |
    | `offerings.components.is_prepaid` | boolean |  |
    | `offerings.components.overage_component` | string (uuid) |  |
    | `offerings.components.min_prepaid_duration` | integer |  |
    | `offerings.components.max_prepaid_duration` | integer |  |
    | `offerings.components.prepaid_duration_step` | integer | Step size in months for the initial prepaid duration at order creation. If set, only multiples of this value (starting from min_prepaid_duration) are valid. Defaults to 1 (any value between min and max). |
    | `offerings.components.min_renewal_duration` | integer | Minimum number of months allowed for a renewal. |
    | `offerings.components.max_renewal_duration` | integer | Maximum number of months allowed for a renewal. |
    | `offerings.components.renewal_duration_step` | integer | Step size in months for renewal. Only multiples of this value (starting from min_renewal_duration) are valid. Defaults to 1. |
    | `offerings.require_purchase_order` | boolean | Whether a purchase order must accompany a resource request for this offering before the proposal can be submitted. Defaults to the offering's require_purchase_order_upload, and stays under the call manager's control afterwards. |
    | `offerings.created` | string (date-time) |  |
    | `rounds` | array of objects |  |
    | `rounds.uuid` | string (uuid) |  |
    | `rounds.slug` | string |  |
    | `rounds.name` | string |  |
    | `rounds.start_time` | string (date-time) |  |
    | `rounds.cutoff_time` | string (date-time) |  |
    | `rounds.status` | any |  |
    | `rounds.allocation_date` | string (date-time) |  |
    | `rounds.review_duration_in_days` | integer |  |
    | `rounds.lifecycle_state` | any | Where the round stands after its cut-off: evaluating, deciding, results_published or closed. Empty before the cut-off. |
    | `rounds.evaluation_started_at` | string (date-time) |  |
    | `rounds.deciding_started_at` | string (date-time) |  |
    | `rounds.results_published_at` | string (date-time) |  |
    | `rounds.closed_at` | string (date-time) |  |
    | `documents` | array of objects |  |
    | `documents.uuid` | string (uuid) |  |
    | `documents.file` | string (uri) | Documentation for call for proposals. |
    | `documents.file_name` | string |  |
    | `documents.file_size` | integer |  |
    | `documents.description` | string |  |
    | `documents.created` | string (date-time) |  |
    | `resource_templates` | array of objects |  |
    | `resource_templates.uuid` | string (uuid) |  |
    | `resource_templates.url` | string |  |
    | `resource_templates.name` | string |  |
    | `resource_templates.description` | string |  |
    | `resource_templates.attributes` | object (free-form) |  |
    | `resource_templates.limits` | object (free-form) |  |
    | `resource_templates.is_required` | boolean | If True, every proposal must include this resource type |
    | `resource_templates.requested_offering` | string (uri) |  |
    | `resource_templates.requested_offering_name` | string |  |
    | `resource_templates.requested_offering_uuid` | string (uuid) |  |
    | `resource_templates.requested_offering_plan` | any |  |
    | `resource_templates.requested_offering_type` | string |  |
    | `resource_templates.requested_offering_components` | array of objects |  |
    | `resource_templates.requested_offering_components.uuid` | string (uuid) |  |
    | `resource_templates.requested_offering_components.offering_uuid` | string (uuid) |  |
    | `resource_templates.requested_offering_components.billing_type` | string | <br>_Enum: `fixed`, `usage`, `limit`, `one`, `few`_ |
    | `resource_templates.requested_offering_components.type` | string | Unique internal name of the measured unit, for example floating_ip. |
    | `resource_templates.requested_offering_components.name` | string | Display name for the measured unit, for example, Floating IP. |
    | `resource_templates.requested_offering_components.description` | string |  |
    | `resource_templates.requested_offering_components.measured_unit` | string | Unit of measurement, for example, GB. |
    | `resource_templates.requested_offering_components.unit_factor` | integer | The conversion factor from backend units to measured_unit |
    | `resource_templates.requested_offering_components.limit_period` | any |  |
    | `resource_templates.requested_offering_components.limit_amount` | number (double) |  |
    | `resource_templates.requested_offering_components.limit_decimal_places` | integer | Number of decimal places accepted for this component's limit. 0 keeps the limit integer-only. |
    | `resource_templates.requested_offering_components.article_code` | string |  |
    | `resource_templates.requested_offering_components.max_value` | number (double) |  |
    | `resource_templates.requested_offering_components.min_value` | number (double) |  |
    | `resource_templates.requested_offering_components.max_available_limit` | number (double) |  |
    | `resource_templates.requested_offering_components.is_boolean` | boolean |  |
    | `resource_templates.requested_offering_components.default_limit` | number (double) |  |
    | `resource_templates.requested_offering_components.factor` | integer |  |
    | `resource_templates.requested_offering_components.is_builtin` | boolean | The API's older name for ``billed_per_plan``.  It used to ask the plugin registry whether this component's type is one the plugin declares, which left out the OpenStack per-volume-type quotas: they are created by the volume type sync rather than declared, so the API called them provider components while the billing resolver treated them as builtin. Reading the stored flag makes the two agree. |
    | `resource_templates.requested_offering_components.is_prepaid` | boolean |  |
    | `resource_templates.requested_offering_components.overage_component` | string (uuid) |  |
    | `resource_templates.requested_offering_components.min_prepaid_duration` | integer |  |
    | `resource_templates.requested_offering_components.max_prepaid_duration` | integer |  |
    | `resource_templates.requested_offering_components.prepaid_duration_step` | integer | Step size in months for the initial prepaid duration at order creation. If set, only multiples of this value (starting from min_prepaid_duration) are valid. Defaults to 1 (any value between min and max). |
    | `resource_templates.requested_offering_components.min_renewal_duration` | integer | Minimum number of months allowed for a renewal. |
    | `resource_templates.requested_offering_components.max_renewal_duration` | integer | Maximum number of months allowed for a renewal. |
    | `resource_templates.requested_offering_components.renewal_duration_step` | integer | Step size in months for renewal. Only multiples of this value (starting from min_renewal_duration) are valid. Defaults to 1. |
    | `resource_templates.created_by` | string (uri) |  |
    | `resource_templates.created_by_name` | string |  |
    | `resource_templates.created` | string (date-time) |  |
    | `fixed_duration_in_days` | integer |  |
    | `max_prepaid_duration_months` | integer | The longest prepaid subscription, in whole months, that fits inside fixed_duration_in_days measured from today; null when the call fixes no duration. |
    | `backend_id` | string |  |
    | `external_url` | string (uri) |  |
    | `reviewer_identity_visible_to_submitters` | boolean | Whether proposal applicants can see reviewer identities |
    | `reviews_visible_to_submitters` | boolean | Whether proposal applicants can see review comments and scores |
    | `has_eligibility_restrictions` | boolean | Check if call has any eligibility restrictions configured. |
    | `proposal_field_config` | object |  |
    | `proposal_field_config.field_project_summary` | string | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_config.field_description` | string | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_config.field_science_sub_domain` | string | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_config.field_supporting_documentation` | string | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `evaluation_start` | any | When a submitted proposal's evaluation starts: on submission, or for all proposals of a round together at its cut-off. Cannot be changed while the call has proposals submitted or in review. |
    | `publish_results` | any | When applicants learn the allocation decision: immediately, or for every proposal of a round together when a call manager publishes the round's results. Cannot be changed while decisions are held. |
    | `created_by` | string (uri) |  |
    | `reference_code` | string |  |
    | `compliance_checklist` | string (uuid) | Compliance checklist that proposals must complete before submission |
    | `compliance_checklist_name` | string |  |
    | `panel_chair` | string (uuid) |  |
    | `panel_chair_uuid` | string (uuid) |  |
    | `panel_chair_name` | string |  |
    | `proposal_slug_template` | string | Template for proposal slugs. Supports: {call_slug}, {round_slug}, {org_slug}, {year}, {month}, {counter}, {counter_padded}. Default: {round_slug}-{counter_padded} |
    | `user_email_patterns` | array of strings | List of email regex patterns. User must match one. |
    | `user_affiliations` | array of strings | List of allowed affiliations. User must have one. |
    | `user_identity_sources` | array of strings | List of allowed identity sources (identity providers). |
    | `user_nationalities` | array of strings | List of allowed nationality codes (ISO 3166-1 alpha-2). User must have one. |
    | `user_organization_types` | array of strings | List of allowed organization type URNs (SCHAC). User must match one. |
    | `user_assurance_levels` | array of strings | List of required assurance URIs (REFEDS). User must have ALL of these. |
    | `applicant_visibility_config` | any |  |
    | `proposal_field_metadata` | array of objects | Per-field state, permitted transitions and downstream consumers for the Project details step. |
    | `proposal_field_metadata.field` | string |  |
    | `proposal_field_metadata.state` | string | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_metadata.allowed_states` | array of strings |  |
    | `proposal_field_metadata.locked_reason` | string |  |
    | `proposal_field_metadata.usage` | array of strings |  |
    | `has_proposals` | boolean | Whether any proposal has been submitted to this call. Used by the frontend to gate slug-template and checklist fields. |
    | `order_author` | any | Whose name the orders for resources granted by this call carry. |
    | `order_author_user` | string (uuid) | The person orders are attributed to when the author is a named contact. Must hold a role on this call or on the organisation managing it. |
    | `order_author_user_uuid` | string (uuid) |  |
    | `order_author_user_name` | string |  |
    | `carry_over_drafts` | boolean | Whether a draft still open when its round's cut-off passes moves on to the call's next round instead of being cancelled. Without a later round the draft is cancelled either way. |
    | `undecided_at_round_completion` | any | What completing a round does with its proposals that still have no decision: refuse to complete the round, or reject them. A round may override it. |

---

### Export call configuration

Export the call's configuration as a portable document that import_call can recreate on another portal. Offerings, plans, checklists and roles are referenced by name. Proposals, reviews, reviewer pools, assignments and user references are never exported.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/export_call/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.call_export_parameters_request import CallExportParametersRequest # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_export_call # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = CallExportParametersRequest()
    response = proposal_protected_calls_export_call.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`CallExportParametersRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/call_export_parameters_request.py)
    2.  **API Source:** [`proposal_protected_calls_export_call`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_export_call.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsExportCall } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsExportCall({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Request Body"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `include_documents` | boolean |  | <br>_Constraints: default: `True`_ |
    | `include_rounds` | boolean |  | <br>_Constraints: default: `True`_ |
    | `include_offerings` | boolean |  | Requested offerings together with their resource templates.<br>_Constraints: default: `True`_ |
    | `include_workflow_steps` | boolean |  | Workflow steps with their notification rules and criteria.<br>_Constraints: default: `True`_ |
    | `include_field_configs` | boolean |  | Proposal field and applicant visibility configuration.<br>_Constraints: default: `True`_ |
    | `include_review_configs` | boolean |  | COI, reviewer matching and assignment configuration.<br>_Constraints: default: `True`_ |
    | `include_role_mappings` | boolean |  | <br>_Constraints: default: `True`_ |
    | `include_compliance_checklist` | boolean |  | <br>_Constraints: default: `True`_ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `call_uuid` | string (uuid) |  |
    | `call_name` | string |  |
    | `export_data` | object (free-form) |  |
    | `exported_sections` | array of strings |  |
    | `export_timestamp` | string (date-time) |  |
    | `warnings` | array of strings | Parts that could not be exported, such as unreadable documents. |

---

### Generate assignments

Generate assignment batches for reviewers. Uses the affinity matrix and COI records to assign reviewers to proposals.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/generate-assignments/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.generate_assignments_request import GenerateAssignmentsRequest # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_generate_assignments # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = GenerateAssignmentsRequest()
    response = proposal_protected_calls_generate_assignments.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`GenerateAssignmentsRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/generate_assignments_request.py)
    2.  **API Source:** [`proposal_protected_calls_generate_assignments`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_generate_assignments.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsGenerateAssignments } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsGenerateAssignments({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Request Body"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `proposal_uuids` | array of string (uuid)s |  | Specific proposal UUIDs to generate assignments for. If empty, generates for all submitted proposals needing reviewers. |
    | `reviewers_per_proposal` | integer |  | Number of reviewers to assign per proposal. If not specified, uses call's minimum_number_of_reviewers setting. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `batches_created` | integer |  |
    | `items_created` | integer |  |
    | `proposals_processed` | integer |  |
    | `skipped_proposals` | array of objects | Proposals that were skipped with reasons |
    | `skipped_proposals.proposal_uuid` | string (uuid) |  |
    | `skipped_proposals.proposal_name` | string |  |
    | `skipped_proposals.reason` | string |  |

---

### Generate reviewer suggestions with configurable matching source

Generate reviewer suggestions with configurable matching source.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/generate-suggestions/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.generate_suggestions_request_request import GenerateSuggestionsRequestRequest # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_generate_suggestions # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = GenerateSuggestionsRequestRequest()
    response = proposal_protected_calls_generate_suggestions.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`GenerateSuggestionsRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/generate_suggestions_request_request.py)
    2.  **API Source:** [`proposal_protected_calls_generate_suggestions`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_generate_suggestions.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsGenerateSuggestions } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsGenerateSuggestions({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Request Body"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `source` | any |  | What content to match reviewers against<br>_Constraints: default: `all_proposals`_ |
    | `proposal_uuids` | array of string (uuid)s |  | Specific proposal UUIDs to match against (for selected_proposals source) |
    | `keywords` | array of strings |  | Custom keywords to search for (for custom_keywords source) |
    | `keyword_search_mode` | any |  | How to search for custom keywords<br>_Constraints: default: `expertise_only`_ |
    | `min_affinity_threshold` | number (double) |  | Minimum affinity score for suggestions (0.0-1.0) |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `suggestions_created` | integer |
    | `reviewers_evaluated` | integer |
    | `source_used` | string |
    | `suggestions` | array of strings |

---

### Import call configuration

Create a draft call under the given call managing organisation from a document produced by export_call. References that cannot be resolved by name on this portal are skipped and reported in warnings. The import is atomic.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/proposal-protected-calls/import_call/ \
      Authorization:"Token YOUR_API_TOKEN" \
      manager="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      call_data:='{}'
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.call_import_parameters_request import CallImportParametersRequest # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_import_call # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = CallImportParametersRequest(
        manager="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        call_data={}
    )
    response = proposal_protected_calls_import_call.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`CallImportParametersRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/call_import_parameters_request.py)
    2.  **API Source:** [`proposal_protected_calls_import_call`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_import_call.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsImportCall } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsImportCall({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "manager": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "call_data": {}
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Request Body (required)"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `manager` | string (uuid) | ✓ | Call managing organisation that will own the imported call. |
    | `name` | string |  | Name for the imported call. Defaults to the exported name. |
    | `call_data` | object (free-form) | ✓ | Exported call document, as a mapping or a YAML string. |
    | `import_documents` | boolean |  | <br>_Constraints: default: `True`_ |
    | `import_rounds` | boolean |  | <br>_Constraints: default: `True`_ |
    | `import_offerings` | boolean |  | <br>_Constraints: default: `True`_ |
    | `import_workflow_steps` | boolean |  | <br>_Constraints: default: `True`_ |
    | `import_field_configs` | boolean |  | <br>_Constraints: default: `True`_ |
    | `import_review_configs` | boolean |  | <br>_Constraints: default: `True`_ |
    | `import_role_mappings` | boolean |  | <br>_Constraints: default: `True`_ |
    | `import_compliance_checklist` | boolean |  | <br>_Constraints: default: `True`_ |


=== "Responses"

    **`201`** - 
    
    | Field | Type |
    |---|---|
    | `call_uuid` | string (uuid) |
    | `call_name` | string |
    | `imported_sections` | array of strings |
    | `warnings` | array of strings |

---

### Invite by email

Invite a reviewer by email address. Creates an invitation that requires the reviewer to create and publish a profile before accepting.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/invite-by-email/ \
      Authorization:"Token YOUR_API_TOKEN" \
      email="alice@example.com"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.email_invitation_request import EmailInvitationRequest # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_invite_by_email # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = EmailInvitationRequest(
        email="alice@example.com"
    )
    response = proposal_protected_calls_invite_by_email.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`EmailInvitationRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/email_invitation_request.py)
    2.  **API Source:** [`proposal_protected_calls_invite_by_email`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_invite_by_email.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsInviteByEmail } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsInviteByEmail({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "email": "alice@example.com"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Request Body (required)"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `email` | string (email) | ✓ | Email address to send the invitation to |
    | `invitation_message` | string |  | Custom message to include in invitation email |
    | `max_assignments` | integer |  | <br>_Constraints: default: `5`_ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `call` | string (uri) |  |
    | `call_uuid` | string (uuid) |  |
    | `call_name` | string |  |
    | `reviewer` | string (uri) |  |
    | `reviewer_uuid` | string | Get reviewer profile UUID if available. |
    | `reviewer_name` | string | Get reviewer name from profile or invited_user. |
    | `reviewer_email` | string | Get email from profile, invited_user, or invited_email. |
    | `has_profile` | boolean | Check if reviewer has a profile. |
    | `invited_email` | string (email) | Email address for direct invitations |
    | `invited_user` | string (uri) | Waldur user if email matches existing account |
    | `invited_user_name` | string |  |
    | `invited_at` | string (date-time) |  |
    | `invitation_status` | any |  |
    | `invitation_status_display` | string |  |
    | `response_date` | string (date-time) |  |
    | `decline_reason` | string |  |
    | `max_assignments` | integer |  |
    | `current_assignments` | integer | Number of the reviewer's open assignments in this call: pending or accepted assignment items whose review is not finished, plus reviews in progress created without an assignment item. |
    | `expertise_match_score` | number (double) | Calculated affinity to call topics (0-1) |
    | `invited_by_name` | string |  |
    | `invitation_link` | string |  |
    | `invitation_expires_at` | string (date-time) |  |
    | `created` | string (date-time) |  |
    | `coi_count` | integer | Count total COIs for this reviewer in this call. |
    | `coi_by_severity` | object (free-form) | Count COIs by severity level. |
    | `reviews_pending` | integer | Legacy field - always returns 0.  Previously counted reviews in 'created' state, but that state has been removed. Reviews are now created directly in 'in_review' state. Kept for backwards compatibility with frontend. |
    | `reviews_in_progress` | integer | Count reviews in 'in_review' state. |
    | `reviews_completed` | integer | Count reviews in 'submitted' state. |
    | `override_reason` | string | Reason for manager override of invitation status. |
    | `overridden_by_name` | string |  |
    | `overridden_at` | string (date-time) |  |

---

### Invite reviewers to join the call's reviewer pool

Invite reviewers to join the call's reviewer pool.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/reviewer-pool/ \
      Authorization:"Token YOUR_API_TOKEN" \
      reviewer_uuids:='[]'
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.call_states import CallStates # (1)
    from waldur_api_client.models.protected_call_o_enum import ProtectedCallOEnum # (2)
    from waldur_api_client.models.reviewer_invitation_request import ReviewerInvitationRequest # (3)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_invite_reviewers # (4)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ReviewerInvitationRequest(
        reviewer_uuids=[]
    )
    response = proposal_protected_calls_invite_reviewers.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`CallStates`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/call_states.py)
    2.  **Model Source:** [`ProtectedCallOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/protected_call_o_enum.py)
    3.  **Model Source:** [`ReviewerInvitationRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/reviewer_invitation_request.py)
    4.  **API Source:** [`proposal_protected_calls_invite_reviewers`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_invite_reviewers.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsInviteReviewers } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsInviteReviewers({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "reviewer_uuids": []
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Query Parameters"

    | Name | Type | Description |
    |---|---|---|
    | `customer` | string (uri) |  |
    | `customer_keyword` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `has_active_round` | boolean |  |
    | `name` | string |  |
    | `o` | array | Ordering<br><br> |
    | `offering_uuid` | string (uuid) |  |
    | `offerings_provider_uuid` | string (uuid) |  |
    | `open_for_offering_uuid` | string (uuid) | Calls the offering can be requested through right now |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `slug` | string | Slug |
    | `state` | array |  |


=== "Request Body (required)"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `reviewer_uuids` | array of string (uuid)s | ✓ | List of reviewer profile UUIDs to invite |
    | `max_assignments` | integer |  | <br>_Constraints: default: `5`_ |
    | `invitation_message` | string |  | Custom message to include in invitation email |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `call` | string (uri) |  |
    | `call_uuid` | string (uuid) |  |
    | `call_name` | string |  |
    | `reviewer` | string (uri) |  |
    | `reviewer_uuid` | string | Get reviewer profile UUID if available. |
    | `reviewer_name` | string | Get reviewer name from profile or invited_user. |
    | `reviewer_email` | string | Get email from profile, invited_user, or invited_email. |
    | `has_profile` | boolean | Check if reviewer has a profile. |
    | `invited_email` | string (email) | Email address for direct invitations |
    | `invited_user` | string (uri) | Waldur user if email matches existing account |
    | `invited_user_name` | string |  |
    | `invited_at` | string (date-time) |  |
    | `invitation_status` | any |  |
    | `invitation_status_display` | string |  |
    | `response_date` | string (date-time) |  |
    | `decline_reason` | string |  |
    | `max_assignments` | integer |  |
    | `current_assignments` | integer | Number of the reviewer's open assignments in this call: pending or accepted assignment items whose review is not finished, plus reviews in progress created without an assignment item. |
    | `expertise_match_score` | number (double) | Calculated affinity to call topics (0-1) |
    | `invited_by_name` | string |  |
    | `invitation_link` | string |  |
    | `invitation_expires_at` | string (date-time) |  |
    | `created` | string (date-time) |  |
    | `coi_count` | integer | Count total COIs for this reviewer in this call. |
    | `coi_by_severity` | object (free-form) | Count COIs by severity level. |
    | `reviews_pending` | integer | Legacy field - always returns 0.  Previously counted reviews in 'created' state, but that state has been removed. Reviews are now created directly in 'in_review' state. Kept for backwards compatibility with frontend. |
    | `reviews_in_progress` | integer | Count reviews in 'in_review' state. |
    | `reviews_completed` | integer | Count reviews in 'submitted' state. |
    | `override_reason` | string | Reason for manager override of invitation status. |
    | `overridden_by_name` | string |  |
    | `overridden_at` | string (date-time) |  |

---

### Create offering for a call

Create offering for a call.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/offerings/ \
      Authorization:"Token YOUR_API_TOKEN" \
      offering="https://api.example.com/api/offering/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.requested_offering_request import RequestedOfferingRequest # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_offerings_set # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = RequestedOfferingRequest(
        offering="https://api.example.com/api/offering/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    )
    response = proposal_protected_calls_offerings_set.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`RequestedOfferingRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/requested_offering_request.py)
    2.  **API Source:** [`proposal_protected_calls_offerings_set`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_offerings_set.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsOfferingsSet } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsOfferingsSet({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "offering": "https://api.example.com/api/offering/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Request Body (required)"

    | Field | Type | Required |
    |---|---|---|
    | `offering` | string (uri) | ✓ |
    | `attributes` | object (free-form) |  |
    | `plan` | string (uri) |  |
    | `description` | string |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `state` | any |  |
    | `offering` | string (uri) |  |
    | `offering_name` | string |  |
    | `offering_uuid` | string (uuid) |  |
    | `offering_type` | string |  |
    | `provider_name` | string |  |
    | `category_uuid` | string (uuid) |  |
    | `category_name` | string |  |
    | `call_managing_organisation` | string |  |
    | `attributes` | object (free-form) |  |
    | `plan` | string (uri) |  |
    | `plan_details` | any |  |
    | `options` | any |  |
    | `components` | array of objects |  |
    | `components.uuid` | string (uuid) |  |
    | `components.offering_uuid` | string (uuid) |  |
    | `components.billing_type` | string | <br>_Enum: `fixed`, `usage`, `limit`, `one`, `few`_ |
    | `components.type` | string | Unique internal name of the measured unit, for example floating_ip. |
    | `components.name` | string | Display name for the measured unit, for example, Floating IP. |
    | `components.description` | string |  |
    | `components.measured_unit` | string | Unit of measurement, for example, GB. |
    | `components.unit_factor` | integer | The conversion factor from backend units to measured_unit |
    | `components.limit_period` | any |  |
    | `components.limit_amount` | number (double) |  |
    | `components.limit_decimal_places` | integer | Number of decimal places accepted for this component's limit. 0 keeps the limit integer-only. |
    | `components.article_code` | string |  |
    | `components.max_value` | number (double) |  |
    | `components.min_value` | number (double) |  |
    | `components.max_available_limit` | number (double) |  |
    | `components.is_boolean` | boolean |  |
    | `components.default_limit` | number (double) |  |
    | `components.factor` | integer |  |
    | `components.is_builtin` | boolean | The API's older name for ``billed_per_plan``.  It used to ask the plugin registry whether this component's type is one the plugin declares, which left out the OpenStack per-volume-type quotas: they are created by the volume type sync rather than declared, so the API called them provider components while the billing resolver treated them as builtin. Reading the stored flag makes the two agree. |
    | `components.is_prepaid` | boolean |  |
    | `components.overage_component` | string (uuid) |  |
    | `components.min_prepaid_duration` | integer |  |
    | `components.max_prepaid_duration` | integer |  |
    | `components.prepaid_duration_step` | integer | Step size in months for the initial prepaid duration at order creation. If set, only multiples of this value (starting from min_prepaid_duration) are valid. Defaults to 1 (any value between min and max). |
    | `components.min_renewal_duration` | integer | Minimum number of months allowed for a renewal. |
    | `components.max_renewal_duration` | integer | Maximum number of months allowed for a renewal. |
    | `components.renewal_duration_step` | integer | Step size in months for renewal. Only multiples of this value (starting from min_renewal_duration) are valid. Defaults to 1. |
    | `require_purchase_order` | boolean | Whether a purchase order must accompany a resource request for this offering before the proposal can be submitted. Defaults to the offering's require_purchase_order_upload, and stays under the call manager's control afterwards. |
    | `created` | string (date-time) |  |
    | `url` | string |  |
    | `approved_by` | string (uri) |  |
    | `created_by` | string (uri) |  |
    | `created_by_name` | string |  |
    | `approved_by_name` | string |  |
    | `description` | string |  |

---

### Create resource template for a call

Create resource template for a call.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/resource_templates/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-proposal-protected-call" \
      requested_offering="https://api.example.com/api/requested-offering/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.call_resource_template_request import CallResourceTemplateRequest # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_resource_templates_set # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = CallResourceTemplateRequest(
        name="my-awesome-proposal-protected-call",
        requested_offering="https://api.example.com/api/requested-offering/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    )
    response = proposal_protected_calls_resource_templates_set.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`CallResourceTemplateRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/call_resource_template_request.py)
    2.  **API Source:** [`proposal_protected_calls_resource_templates_set`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_resource_templates_set.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsResourceTemplatesSet } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsResourceTemplatesSet({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "name": "my-awesome-proposal-protected-call",
        "requested_offering": "https://api.example.com/api/requested-offering/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Request Body (required)"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `name` | string | ✓ |  |
    | `description` | string |  |  |
    | `attributes` | object (free-form) |  |  |
    | `limits` | object (free-form) |  |  |
    | `is_required` | boolean |  | If True, every proposal must include this resource type |
    | `requested_offering` | string (uri) | ✓ |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string |  |
    | `name` | string |  |
    | `description` | string |  |
    | `attributes` | object (free-form) |  |
    | `limits` | object (free-form) |  |
    | `is_required` | boolean | If True, every proposal must include this resource type |
    | `requested_offering` | string (uri) |  |
    | `requested_offering_name` | string |  |
    | `requested_offering_uuid` | string (uuid) |  |
    | `requested_offering_plan` | any |  |
    | `requested_offering_type` | string |  |
    | `requested_offering_components` | array of objects |  |
    | `requested_offering_components.uuid` | string (uuid) |  |
    | `requested_offering_components.offering_uuid` | string (uuid) |  |
    | `requested_offering_components.billing_type` | string | <br>_Enum: `fixed`, `usage`, `limit`, `one`, `few`_ |
    | `requested_offering_components.type` | string | Unique internal name of the measured unit, for example floating_ip. |
    | `requested_offering_components.name` | string | Display name for the measured unit, for example, Floating IP. |
    | `requested_offering_components.description` | string |  |
    | `requested_offering_components.measured_unit` | string | Unit of measurement, for example, GB. |
    | `requested_offering_components.unit_factor` | integer | The conversion factor from backend units to measured_unit |
    | `requested_offering_components.limit_period` | any |  |
    | `requested_offering_components.limit_amount` | number (double) |  |
    | `requested_offering_components.limit_decimal_places` | integer | Number of decimal places accepted for this component's limit. 0 keeps the limit integer-only. |
    | `requested_offering_components.article_code` | string |  |
    | `requested_offering_components.max_value` | number (double) |  |
    | `requested_offering_components.min_value` | number (double) |  |
    | `requested_offering_components.max_available_limit` | number (double) |  |
    | `requested_offering_components.is_boolean` | boolean |  |
    | `requested_offering_components.default_limit` | number (double) |  |
    | `requested_offering_components.factor` | integer |  |
    | `requested_offering_components.is_builtin` | boolean | The API's older name for ``billed_per_plan``.  It used to ask the plugin registry whether this component's type is one the plugin declares, which left out the OpenStack per-volume-type quotas: they are created by the volume type sync rather than declared, so the API called them provider components while the billing resolver treated them as builtin. Reading the stored flag makes the two agree. |
    | `requested_offering_components.is_prepaid` | boolean |  |
    | `requested_offering_components.overage_component` | string (uuid) |  |
    | `requested_offering_components.min_prepaid_duration` | integer |  |
    | `requested_offering_components.max_prepaid_duration` | integer |  |
    | `requested_offering_components.prepaid_duration_step` | integer | Step size in months for the initial prepaid duration at order creation. If set, only multiples of this value (starting from min_prepaid_duration) are valid. Defaults to 1 (any value between min and max). |
    | `requested_offering_components.min_renewal_duration` | integer | Minimum number of months allowed for a renewal. |
    | `requested_offering_components.max_renewal_duration` | integer | Maximum number of months allowed for a renewal. |
    | `requested_offering_components.renewal_duration_step` | integer | Step size in months for renewal. Only multiples of this value (starting from min_renewal_duration) are valid. Defaults to 1. |
    | `created_by` | string (uri) |  |
    | `created_by_name` | string |  |
    | `created` | string (date-time) |  |

---

### Mark proposal compliance as reviewed by call manager

Mark proposal compliance as reviewed by call manager.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/review_proposal_compliance/ \
      Authorization:"Token YOUR_API_TOKEN" \
      proposal_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.call_compliance_review_request import CallComplianceReviewRequest # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_review_proposal_compliance # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = CallComplianceReviewRequest(
        proposal_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = proposal_protected_calls_review_proposal_compliance.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`CallComplianceReviewRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/call_compliance_review_request.py)
    2.  **API Source:** [`proposal_protected_calls_review_proposal_compliance`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_review_proposal_compliance.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsReviewProposalCompliance } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsReviewProposalCompliance({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "proposal_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Request Body (required)"

    | Field | Type | Required |
    |---|---|---|
    | `proposal_uuid` | string (uuid) | ✓ |
    | `review_notes` | string |  |


=== "Responses"

    **`200`** - 
    

---

### Rounds bulk set

Create multiple rounds on a call at a fixed cadence. Spacing is controlled by ``cadence`` (monthly/quarterly/biannual/yearly/custom). Each round's ``cutoff_time`` is derived as ``start_time + submission_window_days``. Fixed-date allocation is not supported in bulk mode.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/rounds-bulk-set/ \
      Authorization:"Token YOUR_API_TOKEN" \
      start_time="2023-10-01T12:00:00Z" \
      cadence="monthly" \
      submission_window_days=123 \
      number_of_rounds=123
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.bulk_round_create_request_request import BulkRoundCreateRequestRequest # (1)
    from waldur_api_client.models.call_states import CallStates # (2)
    from waldur_api_client.models.protected_call_o_enum import ProtectedCallOEnum # (3)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_rounds_bulk_set # (4)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = BulkRoundCreateRequestRequest(
        start_time="2023-10-01T12:00:00Z",
        cadence="monthly",
        submission_window_days=123,
        number_of_rounds=123
    )
    response = proposal_protected_calls_rounds_bulk_set.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`BulkRoundCreateRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/bulk_round_create_request_request.py)
    2.  **Model Source:** [`CallStates`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/call_states.py)
    3.  **Model Source:** [`ProtectedCallOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/protected_call_o_enum.py)
    4.  **API Source:** [`proposal_protected_calls_rounds_bulk_set`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_rounds_bulk_set.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsRoundsBulkSet } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsRoundsBulkSet({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "start_time": "2023-10-01T12:00:00Z",
        "cadence": "monthly",
        "submission_window_days": 123,
        "number_of_rounds": 123
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Query Parameters"

    | Name | Type | Description |
    |---|---|---|
    | `customer` | string (uri) |  |
    | `customer_keyword` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `has_active_round` | boolean |  |
    | `name` | string |  |
    | `o` | array | Ordering<br><br> |
    | `offering_uuid` | string (uuid) |  |
    | `offerings_provider_uuid` | string (uuid) |  |
    | `open_for_offering_uuid` | string (uuid) | Calls the offering can be requested through right now |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `slug` | string | Slug |
    | `state` | array |  |


=== "Request Body (required)"

    | Field | Type | Required |
    |---|---|---|
    | `start_time` | string (date-time) | ✓ |
    | `review_duration_in_days` | integer |  |
    | `cadence` | string | ✓ |
    | `custom_interval_months` | integer |  |
    | `submission_window_days` | integer | ✓ |
    | `number_of_rounds` | integer | ✓ |


=== "Responses"

    **`201`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `slug` | string |  |
    | `name` | string |  |
    | `start_time` | string (date-time) |  |
    | `cutoff_time` | string (date-time) |  |
    | `status` | any |  |
    | `allocation_date` | string (date-time) |  |
    | `review_duration_in_days` | integer |  |
    | `lifecycle_state` | any | Where the round stands after its cut-off: evaluating, deciding, results_published or closed. Empty before the cut-off. |
    | `evaluation_started_at` | string (date-time) |  |
    | `deciding_started_at` | string (date-time) |  |
    | `results_published_at` | string (date-time) |  |
    | `closed_at` | string (date-time) |  |
    | `url` | string |  |
    | `proposals` | array of objects |  |
    | `proposals.uuid` | string (uuid) |  |
    | `proposals.slug` | string |  |
    | `proposals.name` | string |  |
    | `proposals.state` | any |  |
    | `proposals.reviews` | array of anys | Return serialized reviews based on user permissions and visibility settings. - Staff, call managers, and reviewers see all reviews. - Submitters see submitted reviews if visibility is enabled. |
    | `proposals.approved_by_name` | string |  |
    | `proposals.created_by_name` | string |  |
    | `proposals.created` | string (date-time) |  |
    | `results_published_by_name` | string |  |
    | `held_decisions_count` | integer | Proposals of the round whose decision is recorded but not yet published. After publication, decisions that could not be carried out; publishing the results again retries them. Null for anyone who may not see held decisions. |
    | `has_proposals` | boolean | Whether the round holds any proposal, in any state. A round with proposals cannot be deleted. Unlike the proposals list, which leaves out what the viewer may not see, this counts every one. |
    | `results_forced_reason` | string | Why results were published while some proposals of the round still had no decision. |
    | `adopted_at` | string (date) | When the round's results were adopted. |
    | `adoption_note` | string |  |
    | `adoption_document` | string (uri) |  |
    | `undecided_at_round_completion` | any | Overrides the call's rule for proposals still without a decision when the round is completed. Empty: the call's rule applies. |

---

### Close


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/proposal-protected-calls/string-value/rounds/a1b2c3d4-e5f6-7890-abcd-ef1234567890/close/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-proposal-protected-call" \
      manager="https://api.example.com/api/manager/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.protected_call_request import ProtectedCallRequest # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_rounds_close # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ProtectedCallRequest(
        name="my-awesome-proposal-protected-call",
        manager="https://api.example.com/api/manager/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    )
    response = proposal_protected_calls_rounds_close.sync(
        obj_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        uuid="string-value",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ProtectedCallRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/protected_call_request.py)
    2.  **API Source:** [`proposal_protected_calls_rounds_close`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_rounds_close.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsRoundsClose } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsRoundsClose({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "obj_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "uuid": "string-value"
      },
      body: {
        "name": "my-awesome-proposal-protected-call",
        "manager": "https://api.example.com/api/manager/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `obj_uuid` | string | ✓ |
    | `uuid` | string | ✓ |


=== "Request Body (required)"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `slug` | string |  | URL-friendly identifier. Only editable by staff users. |
    | `name` | string | ✓ |  |
    | `description` | string |  |  |
    | `manager` | string (uri) | ✓ |  |
    | `fixed_duration_in_days` | integer |  |  |
    | `backend_id` | string |  |  |
    | `external_url` | string (uri) |  |  |
    | `reviewer_identity_visible_to_submitters` | boolean |  | Whether proposal applicants can see reviewer identities |
    | `reviews_visible_to_submitters` | boolean |  | Whether proposal applicants can see review comments and scores |
    | `proposal_field_config` | object |  |  |
    | `proposal_field_config.field_project_summary` | string |  | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_config.field_description` | string |  | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_config.field_science_sub_domain` | string |  | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `proposal_field_config.field_supporting_documentation` | string |  | <br>_Enum: `hidden`, `optional`, `required`_ |
    | `evaluation_start` | any |  | When a submitted proposal's evaluation starts: on submission, or for all proposals of a round together at its cut-off. Cannot be changed while the call has proposals submitted or in review. |
    | `publish_results` | any |  | When applicants learn the allocation decision: immediately, or for every proposal of a round together when a call manager publishes the round's results. Cannot be changed while decisions are held. |
    | `created_by` | string (uri) |  |  |
    | `reference_code` | string |  |  |
    | `compliance_checklist` | string (uuid) |  | Compliance checklist that proposals must complete before submission |
    | `panel_chair` | string (uuid) |  |  |
    | `proposal_slug_template` | string |  | Template for proposal slugs. Supports: {call_slug}, {round_slug}, {org_slug}, {year}, {month}, {counter}, {counter_padded}. Default: {round_slug}-{counter_padded} |
    | `user_email_patterns` | array of strings |  | List of email regex patterns. User must match one. |
    | `user_affiliations` | array of strings |  | List of allowed affiliations. User must have one. |
    | `user_identity_sources` | array of strings |  | List of allowed identity sources (identity providers). |
    | `user_nationalities` | array of strings |  | List of allowed nationality codes (ISO 3166-1 alpha-2). User must have one. |
    | `user_organization_types` | array of strings |  | List of allowed organization type URNs (SCHAC). User must match one. |
    | `user_assurance_levels` | array of strings |  | List of required assurance URIs (REFEDS). User must have ALL of these. |
    | `applicant_visibility_config` | any |  |  |
    | `order_author` | any |  | Whose name the orders for resources granted by this call carry. |
    | `order_author_user` | string (uuid) |  | The person orders are attributed to when the author is a named contact. Must hold a role on this call or on the organisation managing it. |
    | `carry_over_drafts` | boolean |  | Whether a draft still open when its round's cut-off passes moves on to the call's next round instead of being cancelled. Without a later round the draft is cancelled either way. |
    | `undecided_at_round_completion` | any |  | What completing a round does with its proposals that still have no decision: refuse to complete the round, or reject them. A round may override it. |


=== "Responses"

    **`200`** - 
    

---

### Complete

Close a round whose results have been published. Refused while a decision of the round is still held because its release failed (the refusal carries held_decisions_count; publish the results again to retry it). Every proposal of the round must have a decision. What happens to those that have none follows the round's undecided_at_round_completion, or else the call's: refuse (the refusal carries undecided_count) or reject each at its current step, listed in rejected_proposals. A rejection that fails is listed in failed_proposals and the round stays open; completing again retries it.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/proposal-protected-calls/string-value/rounds/a1b2c3d4-e5f6-7890-abcd-ef1234567890/complete/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_rounds_complete # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_rounds_complete.sync(
        obj_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        uuid="string-value",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`proposal_protected_calls_rounds_complete`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_rounds_complete.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsRoundsComplete } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsRoundsComplete({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "obj_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "uuid": "string-value"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `obj_uuid` | string | ✓ |
    | `uuid` | string | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `slug` | string |  |
    | `name` | string |  |
    | `start_time` | string (date-time) |  |
    | `cutoff_time` | string (date-time) |  |
    | `status` | any |  |
    | `allocation_date` | string (date-time) |  |
    | `review_duration_in_days` | integer |  |
    | `lifecycle_state` | any | Where the round stands after its cut-off: evaluating, deciding, results_published or closed. Empty before the cut-off. |
    | `evaluation_started_at` | string (date-time) |  |
    | `deciding_started_at` | string (date-time) |  |
    | `results_published_at` | string (date-time) |  |
    | `closed_at` | string (date-time) |  |
    | `url` | string |  |
    | `proposals` | array of objects |  |
    | `proposals.uuid` | string (uuid) |  |
    | `proposals.slug` | string |  |
    | `proposals.name` | string |  |
    | `proposals.state` | any |  |
    | `proposals.reviews` | array of anys | Return serialized reviews based on user permissions and visibility settings. - Staff, call managers, and reviewers see all reviews. - Submitters see submitted reviews if visibility is enabled. |
    | `proposals.approved_by_name` | string |  |
    | `proposals.created_by_name` | string |  |
    | `proposals.created` | string (date-time) |  |
    | `results_published_by_name` | string |  |
    | `held_decisions_count` | integer | Proposals of the round whose decision is recorded but not yet published. After publication, decisions that could not be carried out; publishing the results again retries them. Null for anyone who may not see held decisions. |
    | `has_proposals` | boolean | Whether the round holds any proposal, in any state. A round with proposals cannot be deleted. Unlike the proposals list, which leaves out what the viewer may not see, this counts every one. |
    | `results_forced_reason` | string | Why results were published while some proposals of the round still had no decision. |
    | `adopted_at` | string (date) | When the round's results were adopted. |
    | `adoption_note` | string |  |
    | `adoption_document` | string (uri) |  |
    | `undecided_at_round_completion` | any | Overrides the call's rule for proposals still without a decision when the round is completed. Empty: the call's rule applies. |
    | `rejected_proposals` | array of objects | Proposals without a decision that completing the round rejected. |
    | `rejected_proposals.uuid` | string (uuid) |  |
    | `rejected_proposals.name` | string |  |
    | `failed_proposals` | array of objects | Proposals without a decision whose rejection failed. The round stays open; completing it again retries them. |
    | `failed_proposals.uuid` | string (uuid) |  |
    | `failed_proposals.name` | string |  |
    
    ---
    
    **`400`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `detail` | string |  |
    | `held_decisions_count` | integer | Decisions of the round whose release failed at publication and that were never announced. Present when completing is refused because of them; publish the results again to retry them. |
    | `undecided_count` | integer | Proposals of the round without a decision. Present when completing is refused because of them under the refuse rule. |

---

### Publish results

Publish all allocation decisions of an ended round at once: announce every held decision to its applicant and carry it out. Refused while a proposal of the round has no decision, unless forced with a reason; that refusal carries undecided_count. A decision that cannot be carried out stays held and is listed in failed_proposals; publishing again retries it.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/proposal-protected-calls/string-value/rounds/a1b2c3d4-e5f6-7890-abcd-ef1234567890/publish_results/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.publish_round_results_request import PublishRoundResultsRequest # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_rounds_publish_results # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PublishRoundResultsRequest()
    response = proposal_protected_calls_rounds_publish_results.sync(
        obj_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        uuid="string-value",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PublishRoundResultsRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/publish_round_results_request.py)
    2.  **API Source:** [`proposal_protected_calls_rounds_publish_results`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_rounds_publish_results.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsRoundsPublishResults } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsRoundsPublishResults({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "obj_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "uuid": "string-value"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `obj_uuid` | string | ✓ |
    | `uuid` | string | ✓ |


=== "Request Body"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `force` | boolean |  | Publish although some proposals of the round have no decision.<br>_Constraints: default: `False`_ |
    | `reason` | string |  | Why results are published early. Required with force.<br>_Constraints: default: ``_ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `slug` | string |  |
    | `name` | string |  |
    | `start_time` | string (date-time) |  |
    | `cutoff_time` | string (date-time) |  |
    | `status` | any |  |
    | `allocation_date` | string (date-time) |  |
    | `review_duration_in_days` | integer |  |
    | `lifecycle_state` | any | Where the round stands after its cut-off: evaluating, deciding, results_published or closed. Empty before the cut-off. |
    | `evaluation_started_at` | string (date-time) |  |
    | `deciding_started_at` | string (date-time) |  |
    | `results_published_at` | string (date-time) |  |
    | `closed_at` | string (date-time) |  |
    | `url` | string |  |
    | `proposals` | array of objects |  |
    | `proposals.uuid` | string (uuid) |  |
    | `proposals.slug` | string |  |
    | `proposals.name` | string |  |
    | `proposals.state` | any |  |
    | `proposals.reviews` | array of anys | Return serialized reviews based on user permissions and visibility settings. - Staff, call managers, and reviewers see all reviews. - Submitters see submitted reviews if visibility is enabled. |
    | `proposals.approved_by_name` | string |  |
    | `proposals.created_by_name` | string |  |
    | `proposals.created` | string (date-time) |  |
    | `results_published_by_name` | string |  |
    | `held_decisions_count` | integer | Proposals of the round whose decision is recorded but not yet published. After publication, decisions that could not be carried out; publishing the results again retries them. Null for anyone who may not see held decisions. |
    | `has_proposals` | boolean | Whether the round holds any proposal, in any state. A round with proposals cannot be deleted. Unlike the proposals list, which leaves out what the viewer may not see, this counts every one. |
    | `results_forced_reason` | string | Why results were published while some proposals of the round still had no decision. |
    | `adopted_at` | string (date) | When the round's results were adopted. |
    | `adoption_note` | string |  |
    | `adoption_document` | string (uri) |  |
    | `undecided_at_round_completion` | any | Overrides the call's rule for proposals still without a decision when the round is completed. Empty: the call's rule applies. |
    | `failed_proposals` | array of objects | Proposals whose held decision could not be carried out. They stay held; publishing the round's results again retries them. |
    | `failed_proposals.uuid` | string (uuid) |  |
    | `failed_proposals.name` | string |  |
    
    ---
    
    **`400`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `detail` | string |  |
    | `undecided_count` | integer | Proposals of the round without a decision. Present when publishing is refused because of them; publish with force and a reason to go ahead anyway. |

---

### Record adoption

Record that the round's results were adopted: the date, a note and optionally the adopting document.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/proposal-protected-calls/string-value/rounds/a1b2c3d4-e5f6-7890-abcd-ef1234567890/record_adoption/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_rounds_record_adoption # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_rounds_record_adoption.sync(
        obj_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        uuid="string-value",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`proposal_protected_calls_rounds_record_adoption`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_rounds_record_adoption.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsRoundsRecordAdoption } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsRoundsRecordAdoption({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "obj_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "uuid": "string-value"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `obj_uuid` | string | ✓ |
    | `uuid` | string | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `slug` | string |  |
    | `name` | string |  |
    | `start_time` | string (date-time) |  |
    | `cutoff_time` | string (date-time) |  |
    | `status` | any |  |
    | `allocation_date` | string (date-time) |  |
    | `review_duration_in_days` | integer |  |
    | `lifecycle_state` | any | Where the round stands after its cut-off: evaluating, deciding, results_published or closed. Empty before the cut-off. |
    | `evaluation_started_at` | string (date-time) |  |
    | `deciding_started_at` | string (date-time) |  |
    | `results_published_at` | string (date-time) |  |
    | `closed_at` | string (date-time) |  |
    | `url` | string |  |
    | `proposals` | array of objects |  |
    | `proposals.uuid` | string (uuid) |  |
    | `proposals.slug` | string |  |
    | `proposals.name` | string |  |
    | `proposals.state` | any |  |
    | `proposals.reviews` | array of anys | Return serialized reviews based on user permissions and visibility settings. - Staff, call managers, and reviewers see all reviews. - Submitters see submitted reviews if visibility is enabled. |
    | `proposals.approved_by_name` | string |  |
    | `proposals.created_by_name` | string |  |
    | `proposals.created` | string (date-time) |  |
    | `results_published_by_name` | string |  |
    | `held_decisions_count` | integer | Proposals of the round whose decision is recorded but not yet published. After publication, decisions that could not be carried out; publishing the results again retries them. Null for anyone who may not see held decisions. |
    | `has_proposals` | boolean | Whether the round holds any proposal, in any state. A round with proposals cannot be deleted. Unlike the proposals list, which leaves out what the viewer may not see, this counts every one. |
    | `results_forced_reason` | string | Why results were published while some proposals of the round still had no decision. |
    | `adopted_at` | string (date) | When the round's results were adopted. |
    | `adoption_note` | string |  |
    | `adoption_document` | string (uri) |  |
    | `undecided_at_round_completion` | any | Overrides the call's rule for proposals still without a decision when the round is completed. Empty: the call's rule applies. |

---

### Create a round for a call

Create a round for a call.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/rounds/ \
      Authorization:"Token YOUR_API_TOKEN" \
      start_time="2023-10-01T12:00:00Z" \
      cutoff_time="2023-10-01T12:00:00Z"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.protected_round_request import ProtectedRoundRequest # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_rounds_set # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ProtectedRoundRequest(
        start_time="2023-10-01T12:00:00Z",
        cutoff_time="2023-10-01T12:00:00Z"
    )
    response = proposal_protected_calls_rounds_set.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ProtectedRoundRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/protected_round_request.py)
    2.  **API Source:** [`proposal_protected_calls_rounds_set`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_rounds_set.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsRoundsSet } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsRoundsSet({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "start_time": "2023-10-01T12:00:00Z",
        "cutoff_time": "2023-10-01T12:00:00Z"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Request Body (required)"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `start_time` | string (date-time) | ✓ |  |
    | `cutoff_time` | string (date-time) | ✓ |  |
    | `allocation_date` | string (date-time) |  |  |
    | `review_duration_in_days` | integer |  |  |
    | `undecided_at_round_completion` | any |  | Overrides the call's rule for proposals still without a decision when the round is completed. Empty: the call's rule applies. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `slug` | string |  |
    | `name` | string |  |
    | `start_time` | string (date-time) |  |
    | `cutoff_time` | string (date-time) |  |
    | `status` | any |  |
    | `allocation_date` | string (date-time) |  |
    | `review_duration_in_days` | integer |  |
    | `lifecycle_state` | any | Where the round stands after its cut-off: evaluating, deciding, results_published or closed. Empty before the cut-off. |
    | `evaluation_started_at` | string (date-time) |  |
    | `deciding_started_at` | string (date-time) |  |
    | `results_published_at` | string (date-time) |  |
    | `closed_at` | string (date-time) |  |
    | `url` | string |  |
    | `proposals` | array of objects |  |
    | `proposals.uuid` | string (uuid) |  |
    | `proposals.slug` | string |  |
    | `proposals.name` | string |  |
    | `proposals.state` | any |  |
    | `proposals.reviews` | array of anys | Return serialized reviews based on user permissions and visibility settings. - Staff, call managers, and reviewers see all reviews. - Submitters see submitted reviews if visibility is enabled. |
    | `proposals.approved_by_name` | string |  |
    | `proposals.created_by_name` | string |  |
    | `proposals.created` | string (date-time) |  |
    | `results_published_by_name` | string |  |
    | `held_decisions_count` | integer | Proposals of the round whose decision is recorded but not yet published. After publication, decisions that could not be carried out; publishing the results again retries them. Null for anyone who may not see held decisions. |
    | `has_proposals` | boolean | Whether the round holds any proposal, in any state. A round with proposals cannot be deleted. Unlike the proposals list, which leaves out what the viewer may not see, this counts every one. |
    | `results_forced_reason` | string | Why results were published while some proposals of the round still had no decision. |
    | `adopted_at` | string (date) | When the round's results were adopted. |
    | `adoption_note` | string |  |
    | `adoption_document` | string (uri) |  |
    | `undecided_at_round_completion` | any | Overrides the call's rule for proposals still without a decision when the round is completed. Empty: the call's rule applies. |

---

### Start deciding

Move an ended round from evaluating to deciding: its proposals have been evaluated and go to the decision body.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/proposal-protected-calls/string-value/rounds/a1b2c3d4-e5f6-7890-abcd-ef1234567890/start_deciding/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_rounds_start_deciding # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_rounds_start_deciding.sync(
        obj_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        uuid="string-value",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`proposal_protected_calls_rounds_start_deciding`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_rounds_start_deciding.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsRoundsStartDeciding } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsRoundsStartDeciding({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "obj_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "uuid": "string-value"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `obj_uuid` | string | ✓ |
    | `uuid` | string | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `slug` | string |  |
    | `name` | string |  |
    | `start_time` | string (date-time) |  |
    | `cutoff_time` | string (date-time) |  |
    | `status` | any |  |
    | `allocation_date` | string (date-time) |  |
    | `review_duration_in_days` | integer |  |
    | `lifecycle_state` | any | Where the round stands after its cut-off: evaluating, deciding, results_published or closed. Empty before the cut-off. |
    | `evaluation_started_at` | string (date-time) |  |
    | `deciding_started_at` | string (date-time) |  |
    | `results_published_at` | string (date-time) |  |
    | `closed_at` | string (date-time) |  |
    | `url` | string |  |
    | `proposals` | array of objects |  |
    | `proposals.uuid` | string (uuid) |  |
    | `proposals.slug` | string |  |
    | `proposals.name` | string |  |
    | `proposals.state` | any |  |
    | `proposals.reviews` | array of anys | Return serialized reviews based on user permissions and visibility settings. - Staff, call managers, and reviewers see all reviews. - Submitters see submitted reviews if visibility is enabled. |
    | `proposals.approved_by_name` | string |  |
    | `proposals.created_by_name` | string |  |
    | `proposals.created` | string (date-time) |  |
    | `results_published_by_name` | string |  |
    | `held_decisions_count` | integer | Proposals of the round whose decision is recorded but not yet published. After publication, decisions that could not be carried out; publishing the results again retries them. Null for anyone who may not see held decisions. |
    | `has_proposals` | boolean | Whether the round holds any proposal, in any state. A round with proposals cannot be deleted. Unlike the proposals list, which leaves out what the viewer may not see, this counts every one. |
    | `results_forced_reason` | string | Why results were published while some proposals of the round still had no decision. |
    | `adopted_at` | string (date) | When the round's results were adopted. |
    | `adoption_note` | string |  |
    | `adoption_document` | string (uri) |  |
    | `undecided_at_round_completion` | any | Overrides the call's rule for proposals still without a decision when the round is completed. Empty: the call's rule applies. |

---

### Send all draft assignment batches for this call

Send all draft assignment batches for this call.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/send-all-assignments/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.send_all_assignment_batches_request import SendAllAssignmentBatchesRequest # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_send_all_assignments # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = SendAllAssignmentBatchesRequest()
    response = proposal_protected_calls_send_all_assignments.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`SendAllAssignmentBatchesRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/send_all_assignment_batches_request.py)
    2.  **API Source:** [`proposal_protected_calls_send_all_assignments`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_send_all_assignments.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsSendAllAssignments } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsSendAllAssignments({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Request Body"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `batch_uuids` | array of string (uuid)s |  | Specific batch UUIDs to send. If empty, sends all draft batches. |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `batches_sent` | integer |
    | `skipped` | integer |

---

### Send invitations to all confirmed suggestions

Send invitations to all confirmed suggestions.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/send-invitations/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_send_invitations # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_send_invitations.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`proposal_protected_calls_send_invitations`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_send_invitations.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsSendInvitations } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsSendInvitations({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `invitations_sent` | integer |

---

### Create or update a workflow step for a call

Create or update a workflow step for a call.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/workflow_steps/ \
      Authorization:"Token YOUR_API_TOKEN" \
      step="administrative_check"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.call_workflow_step_request import CallWorkflowStepRequest # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_workflow_steps_set # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = CallWorkflowStepRequest(
        step="administrative_check"
    )
    response = proposal_protected_calls_workflow_steps_set.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`CallWorkflowStepRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/call_workflow_step_request.py)
    2.  **API Source:** [`proposal_protected_calls_workflow_steps_set`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_workflow_steps_set.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsWorkflowStepsSet } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsWorkflowStepsSet({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "step": "administrative_check"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Request Body (required)"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `step` | string | ✓ | <br>_Enum: `administrative_check`, `technical_assessment`, `expert_review`, `panel_review`, `allocation_decision`, `award_response`_ |
    | `is_enabled` | boolean |  | Whether this step is enabled. Disabled steps are skipped. |
    | `duration_in_days` | integer |  | Duration in days. Used to calculate deadlines. |
    | `checklist` | string (uuid) |  |  |
    | `checklist_required` | boolean |  | When the step has a checklist, block completion until its required questions are answered. Set False to make the checklist advisory. |
    | `blind_review` | boolean |  | Evaluators cannot see each other's assessments. |
    | `requires_coi_confirmation` | boolean |  | Evaluator must confirm absence of conflict of interest. |
    | `min_reviewers` | integer |  | Minimum reviews required before step can complete. |
    | `min_score_threshold` | string (decimal) |  | Minimum average score required before this step can complete (a completion gate; it does not auto-reject lower scores). |
    | `applicant_visible` | boolean |  | Whether the applicant can see step details (not just status). |
    | `responsible_role` | any |  | Role expected to act on this step. |
    | `transition_mode` | any |  | How this step advances once a human completes it. 'Automatic' advances to the next step immediately; 'Manual' waits for a separate advance action. Neither auto-decides from review scores. |
    | `include_award_response` | boolean |  | Allocation decision: require applicant award response after decision. |
    | `allocation_time` | any |  | Allocation decision: when a granted proposal takes effect — immediately (on_decision) or on the round's allocation date (fixed_date). |
    | `display_order` | integer |  | Optional override of catalog ordering. |
    | `criteria` | array of objects |  |  |
    | `criteria.name` | string | ✓ |  |
    | `criteria.order` | integer |  |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `step` | string | <br>_Enum: `administrative_check`, `technical_assessment`, `expert_review`, `panel_review`, `allocation_decision`, `award_response`_ |
    | `call_uuid` | string (uuid) |  |
    | `call_name` | string |  |
    | `is_enabled` | boolean | Whether this step is enabled. Disabled steps are skipped. |
    | `is_mandatory` | boolean |  |
    | `duration_in_days` | integer | Duration in days. Used to calculate deadlines. |
    | `checklist` | string (uuid) |  |
    | `checklist_name` | string |  |
    | `checklist_required` | boolean | When the step has a checklist, block completion until its required questions are answered. Set False to make the checklist advisory. |
    | `blind_review` | boolean | Evaluators cannot see each other's assessments. |
    | `requires_coi_confirmation` | boolean | Evaluator must confirm absence of conflict of interest. |
    | `min_reviewers` | integer | Minimum reviews required before step can complete. |
    | `min_score_threshold` | string (decimal) | Minimum average score required before this step can complete (a completion gate; it does not auto-reject lower scores). |
    | `applicant_visible` | boolean | Whether the applicant can see step details (not just status). |
    | `responsible_role` | any | Role expected to act on this step. |
    | `transition_mode` | any | How this step advances once a human completes it. 'Automatic' advances to the next step immediately; 'Manual' waits for a separate advance action. Neither auto-decides from review scores. |
    | `include_award_response` | boolean | Allocation decision: require applicant award response after decision. |
    | `allocation_time` | any | Allocation decision: when a granted proposal takes effect — immediately (on_decision) or on the round's allocation date (fixed_date). |
    | `display_order` | integer | Optional override of catalog ordering. |
    | `criteria` | array of objects |  |
    | `criteria.uuid` | string (uuid) |  |
    | `criteria.name` | string |  |
    | `criteria.order` | integer |  |
    | `notification_rules` | array of objects |  |
    | `notification_rules.uuid` | string (uuid) |  |
    | `notification_rules.trigger` | any |  |
    | `notification_rules.recipient` | any |  |
    | `notification_rules.days_before` | integer | Only for deadline_approaching: how many days before the step's deadline the reminder is sent. |
    | `notification_rules.is_enabled` | boolean |  |
    | `notification_rules.notified_proposal_roles` | array of strings |  |
    | `responsible_users` | array of objects |  |
    | `responsible_users.uuid` | string (uuid) |  |
    | `responsible_users.username` | string |  |
    | `responsible_users.full_name` | string |  |
    | `responsible_users.email` | string (email) |  |
    | `responsible_users.is_panel_chair` | boolean |  |

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/proposal-protected-calls/string-value/offerings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      offering="https://api.example.com/api/offering/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.requested_offering_request import RequestedOfferingRequest # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_offerings_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = RequestedOfferingRequest(
        offering="https://api.example.com/api/offering/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    )
    response = proposal_protected_calls_offerings_update.sync(
        obj_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        uuid="string-value",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`RequestedOfferingRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/requested_offering_request.py)
    2.  **API Source:** [`proposal_protected_calls_offerings_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_offerings_update.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsOfferingsUpdate } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsOfferingsUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "obj_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "uuid": "string-value"
      },
      body: {
        "offering": "https://api.example.com/api/offering/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `obj_uuid` | string | ✓ |
    | `uuid` | string | ✓ |


=== "Request Body (required)"

    | Field | Type | Required |
    |---|---|---|
    | `offering` | string (uri) | ✓ |
    | `attributes` | object (free-form) |  |
    | `plan` | string (uri) |  |
    | `description` | string |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `state` | any |  |
    | `offering` | string (uri) |  |
    | `offering_name` | string |  |
    | `offering_uuid` | string (uuid) |  |
    | `offering_type` | string |  |
    | `provider_name` | string |  |
    | `category_uuid` | string (uuid) |  |
    | `category_name` | string |  |
    | `call_managing_organisation` | string |  |
    | `attributes` | object (free-form) |  |
    | `plan` | string (uri) |  |
    | `plan_details` | any |  |
    | `options` | any |  |
    | `components` | array of objects |  |
    | `components.uuid` | string (uuid) |  |
    | `components.offering_uuid` | string (uuid) |  |
    | `components.billing_type` | string | <br>_Enum: `fixed`, `usage`, `limit`, `one`, `few`_ |
    | `components.type` | string | Unique internal name of the measured unit, for example floating_ip. |
    | `components.name` | string | Display name for the measured unit, for example, Floating IP. |
    | `components.description` | string |  |
    | `components.measured_unit` | string | Unit of measurement, for example, GB. |
    | `components.unit_factor` | integer | The conversion factor from backend units to measured_unit |
    | `components.limit_period` | any |  |
    | `components.limit_amount` | number (double) |  |
    | `components.limit_decimal_places` | integer | Number of decimal places accepted for this component's limit. 0 keeps the limit integer-only. |
    | `components.article_code` | string |  |
    | `components.max_value` | number (double) |  |
    | `components.min_value` | number (double) |  |
    | `components.max_available_limit` | number (double) |  |
    | `components.is_boolean` | boolean |  |
    | `components.default_limit` | number (double) |  |
    | `components.factor` | integer |  |
    | `components.is_builtin` | boolean | The API's older name for ``billed_per_plan``.  It used to ask the plugin registry whether this component's type is one the plugin declares, which left out the OpenStack per-volume-type quotas: they are created by the volume type sync rather than declared, so the API called them provider components while the billing resolver treated them as builtin. Reading the stored flag makes the two agree. |
    | `components.is_prepaid` | boolean |  |
    | `components.overage_component` | string (uuid) |  |
    | `components.min_prepaid_duration` | integer |  |
    | `components.max_prepaid_duration` | integer |  |
    | `components.prepaid_duration_step` | integer | Step size in months for the initial prepaid duration at order creation. If set, only multiples of this value (starting from min_prepaid_duration) are valid. Defaults to 1 (any value between min and max). |
    | `components.min_renewal_duration` | integer | Minimum number of months allowed for a renewal. |
    | `components.max_renewal_duration` | integer | Maximum number of months allowed for a renewal. |
    | `components.renewal_duration_step` | integer | Step size in months for renewal. Only multiples of this value (starting from min_renewal_duration) are valid. Defaults to 1. |
    | `require_purchase_order` | boolean | Whether a purchase order must accompany a resource request for this offering before the proposal can be submitted. Defaults to the offering's require_purchase_order_upload, and stays under the call manager's control afterwards. |
    | `created` | string (date-time) |  |
    | `url` | string |  |
    | `approved_by` | string (uri) |  |
    | `created_by` | string (uri) |  |
    | `created_by_name` | string |  |
    | `approved_by_name` | string |  |
    | `description` | string |  |

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/proposal-protected-calls/string-value/resource_templates/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-proposal-protected-call" \
      requested_offering="https://api.example.com/api/requested-offering/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.call_resource_template_request import CallResourceTemplateRequest # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_resource_templates_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = CallResourceTemplateRequest(
        name="my-awesome-proposal-protected-call",
        requested_offering="https://api.example.com/api/requested-offering/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    )
    response = proposal_protected_calls_resource_templates_update.sync(
        obj_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        uuid="string-value",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`CallResourceTemplateRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/call_resource_template_request.py)
    2.  **API Source:** [`proposal_protected_calls_resource_templates_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_resource_templates_update.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsResourceTemplatesUpdate } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsResourceTemplatesUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "obj_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "uuid": "string-value"
      },
      body: {
        "name": "my-awesome-proposal-protected-call",
        "requested_offering": "https://api.example.com/api/requested-offering/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `obj_uuid` | string | ✓ |
    | `uuid` | string | ✓ |


=== "Request Body (required)"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `name` | string | ✓ |  |
    | `description` | string |  |  |
    | `attributes` | object (free-form) |  |  |
    | `limits` | object (free-form) |  |  |
    | `is_required` | boolean |  | If True, every proposal must include this resource type |
    | `requested_offering` | string (uri) | ✓ |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string |  |
    | `name` | string |  |
    | `description` | string |  |
    | `attributes` | object (free-form) |  |
    | `limits` | object (free-form) |  |
    | `is_required` | boolean | If True, every proposal must include this resource type |
    | `requested_offering` | string (uri) |  |
    | `requested_offering_name` | string |  |
    | `requested_offering_uuid` | string (uuid) |  |
    | `requested_offering_plan` | any |  |
    | `requested_offering_type` | string |  |
    | `requested_offering_components` | array of objects |  |
    | `requested_offering_components.uuid` | string (uuid) |  |
    | `requested_offering_components.offering_uuid` | string (uuid) |  |
    | `requested_offering_components.billing_type` | string | <br>_Enum: `fixed`, `usage`, `limit`, `one`, `few`_ |
    | `requested_offering_components.type` | string | Unique internal name of the measured unit, for example floating_ip. |
    | `requested_offering_components.name` | string | Display name for the measured unit, for example, Floating IP. |
    | `requested_offering_components.description` | string |  |
    | `requested_offering_components.measured_unit` | string | Unit of measurement, for example, GB. |
    | `requested_offering_components.unit_factor` | integer | The conversion factor from backend units to measured_unit |
    | `requested_offering_components.limit_period` | any |  |
    | `requested_offering_components.limit_amount` | number (double) |  |
    | `requested_offering_components.limit_decimal_places` | integer | Number of decimal places accepted for this component's limit. 0 keeps the limit integer-only. |
    | `requested_offering_components.article_code` | string |  |
    | `requested_offering_components.max_value` | number (double) |  |
    | `requested_offering_components.min_value` | number (double) |  |
    | `requested_offering_components.max_available_limit` | number (double) |  |
    | `requested_offering_components.is_boolean` | boolean |  |
    | `requested_offering_components.default_limit` | number (double) |  |
    | `requested_offering_components.factor` | integer |  |
    | `requested_offering_components.is_builtin` | boolean | The API's older name for ``billed_per_plan``.  It used to ask the plugin registry whether this component's type is one the plugin declares, which left out the OpenStack per-volume-type quotas: they are created by the volume type sync rather than declared, so the API called them provider components while the billing resolver treated them as builtin. Reading the stored flag makes the two agree. |
    | `requested_offering_components.is_prepaid` | boolean |  |
    | `requested_offering_components.overage_component` | string (uuid) |  |
    | `requested_offering_components.min_prepaid_duration` | integer |  |
    | `requested_offering_components.max_prepaid_duration` | integer |  |
    | `requested_offering_components.prepaid_duration_step` | integer | Step size in months for the initial prepaid duration at order creation. If set, only multiples of this value (starting from min_prepaid_duration) are valid. Defaults to 1 (any value between min and max). |
    | `requested_offering_components.min_renewal_duration` | integer | Minimum number of months allowed for a renewal. |
    | `requested_offering_components.max_renewal_duration` | integer | Maximum number of months allowed for a renewal. |
    | `requested_offering_components.renewal_duration_step` | integer | Step size in months for renewal. Only multiples of this value (starting from min_renewal_duration) are valid. Defaults to 1. |
    | `created_by` | string (uri) |  |
    | `created_by_name` | string |  |
    | `created` | string (date-time) |  |

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/proposal-protected-calls/string-value/rounds/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      start_time="2023-10-01T12:00:00Z" \
      cutoff_time="2023-10-01T12:00:00Z"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.protected_round_request import ProtectedRoundRequest # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_rounds_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ProtectedRoundRequest(
        start_time="2023-10-01T12:00:00Z",
        cutoff_time="2023-10-01T12:00:00Z"
    )
    response = proposal_protected_calls_rounds_update.sync(
        obj_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        uuid="string-value",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ProtectedRoundRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/protected_round_request.py)
    2.  **API Source:** [`proposal_protected_calls_rounds_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_rounds_update.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsRoundsUpdate } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsRoundsUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "obj_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "uuid": "string-value"
      },
      body: {
        "start_time": "2023-10-01T12:00:00Z",
        "cutoff_time": "2023-10-01T12:00:00Z"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `obj_uuid` | string | ✓ |
    | `uuid` | string | ✓ |


=== "Request Body (required)"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `start_time` | string (date-time) | ✓ |  |
    | `cutoff_time` | string (date-time) | ✓ |  |
    | `allocation_date` | string (date-time) |  |  |
    | `review_duration_in_days` | integer |  |  |
    | `undecided_at_round_completion` | any |  | Overrides the call's rule for proposals still without a decision when the round is completed. Empty: the call's rule applies. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `slug` | string |  |
    | `name` | string |  |
    | `start_time` | string (date-time) |  |
    | `cutoff_time` | string (date-time) |  |
    | `status` | any |  |
    | `allocation_date` | string (date-time) |  |
    | `review_duration_in_days` | integer |  |
    | `lifecycle_state` | any | Where the round stands after its cut-off: evaluating, deciding, results_published or closed. Empty before the cut-off. |
    | `evaluation_started_at` | string (date-time) |  |
    | `deciding_started_at` | string (date-time) |  |
    | `results_published_at` | string (date-time) |  |
    | `closed_at` | string (date-time) |  |
    | `url` | string |  |
    | `proposals` | array of objects |  |
    | `proposals.uuid` | string (uuid) |  |
    | `proposals.slug` | string |  |
    | `proposals.name` | string |  |
    | `proposals.state` | any |  |
    | `proposals.reviews` | array of anys | Return serialized reviews based on user permissions and visibility settings. - Staff, call managers, and reviewers see all reviews. - Submitters see submitted reviews if visibility is enabled. |
    | `proposals.approved_by_name` | string |  |
    | `proposals.created_by_name` | string |  |
    | `proposals.created` | string (date-time) |  |
    | `results_published_by_name` | string |  |
    | `held_decisions_count` | integer | Proposals of the round whose decision is recorded but not yet published. After publication, decisions that could not be carried out; publishing the results again retries them. Null for anyone who may not see held decisions. |
    | `has_proposals` | boolean | Whether the round holds any proposal, in any state. A round with proposals cannot be deleted. Unlike the proposals list, which leaves out what the viewer may not see, this counts every one. |
    | `results_forced_reason` | string | Why results were published while some proposals of the round still had no decision. |
    | `adopted_at` | string (date) | When the round's results were adopted. |
    | `adoption_note` | string |  |
    | `adoption_document` | string (uri) |  |
    | `undecided_at_round_completion` | any | Overrides the call's rule for proposals still without a decision when the round is completed. Empty: the call's rule applies. |

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/proposal-protected-calls/string-value/workflow_steps/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      step="administrative_check"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.call_workflow_step_request import CallWorkflowStepRequest # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_workflow_steps_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = CallWorkflowStepRequest(
        step="administrative_check"
    )
    response = proposal_protected_calls_workflow_steps_update.sync(
        obj_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        uuid="string-value",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`CallWorkflowStepRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/call_workflow_step_request.py)
    2.  **API Source:** [`proposal_protected_calls_workflow_steps_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_workflow_steps_update.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsWorkflowStepsUpdate } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsWorkflowStepsUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "obj_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "uuid": "string-value"
      },
      body: {
        "step": "administrative_check"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `obj_uuid` | string | ✓ |
    | `uuid` | string | ✓ |


=== "Request Body (required)"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `step` | string | ✓ | <br>_Enum: `administrative_check`, `technical_assessment`, `expert_review`, `panel_review`, `allocation_decision`, `award_response`_ |
    | `is_enabled` | boolean |  | Whether this step is enabled. Disabled steps are skipped. |
    | `duration_in_days` | integer |  | Duration in days. Used to calculate deadlines. |
    | `checklist` | string (uuid) |  |  |
    | `checklist_required` | boolean |  | When the step has a checklist, block completion until its required questions are answered. Set False to make the checklist advisory. |
    | `blind_review` | boolean |  | Evaluators cannot see each other's assessments. |
    | `requires_coi_confirmation` | boolean |  | Evaluator must confirm absence of conflict of interest. |
    | `min_reviewers` | integer |  | Minimum reviews required before step can complete. |
    | `min_score_threshold` | string (decimal) |  | Minimum average score required before this step can complete (a completion gate; it does not auto-reject lower scores). |
    | `applicant_visible` | boolean |  | Whether the applicant can see step details (not just status). |
    | `responsible_role` | any |  | Role expected to act on this step. |
    | `transition_mode` | any |  | How this step advances once a human completes it. 'Automatic' advances to the next step immediately; 'Manual' waits for a separate advance action. Neither auto-decides from review scores. |
    | `include_award_response` | boolean |  | Allocation decision: require applicant award response after decision. |
    | `allocation_time` | any |  | Allocation decision: when a granted proposal takes effect — immediately (on_decision) or on the round's allocation date (fixed_date). |
    | `display_order` | integer |  | Optional override of catalog ordering. |
    | `criteria` | array of objects |  |  |
    | `criteria.name` | string | ✓ |  |
    | `criteria.order` | integer |  |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `step` | string | <br>_Enum: `administrative_check`, `technical_assessment`, `expert_review`, `panel_review`, `allocation_decision`, `award_response`_ |
    | `call_uuid` | string (uuid) |  |
    | `call_name` | string |  |
    | `is_enabled` | boolean | Whether this step is enabled. Disabled steps are skipped. |
    | `is_mandatory` | boolean |  |
    | `duration_in_days` | integer | Duration in days. Used to calculate deadlines. |
    | `checklist` | string (uuid) |  |
    | `checklist_name` | string |  |
    | `checklist_required` | boolean | When the step has a checklist, block completion until its required questions are answered. Set False to make the checklist advisory. |
    | `blind_review` | boolean | Evaluators cannot see each other's assessments. |
    | `requires_coi_confirmation` | boolean | Evaluator must confirm absence of conflict of interest. |
    | `min_reviewers` | integer | Minimum reviews required before step can complete. |
    | `min_score_threshold` | string (decimal) | Minimum average score required before this step can complete (a completion gate; it does not auto-reject lower scores). |
    | `applicant_visible` | boolean | Whether the applicant can see step details (not just status). |
    | `responsible_role` | any | Role expected to act on this step. |
    | `transition_mode` | any | How this step advances once a human completes it. 'Automatic' advances to the next step immediately; 'Manual' waits for a separate advance action. Neither auto-decides from review scores. |
    | `include_award_response` | boolean | Allocation decision: require applicant award response after decision. |
    | `allocation_time` | any | Allocation decision: when a granted proposal takes effect — immediately (on_decision) or on the round's allocation date (fixed_date). |
    | `display_order` | integer | Optional override of catalog ordering. |
    | `criteria` | array of objects |  |
    | `criteria.uuid` | string (uuid) |  |
    | `criteria.name` | string |  |
    | `criteria.order` | integer |  |
    | `notification_rules` | array of objects |  |
    | `notification_rules.uuid` | string (uuid) |  |
    | `notification_rules.trigger` | any |  |
    | `notification_rules.recipient` | any |  |
    | `notification_rules.days_before` | integer | Only for deadline_approaching: how many days before the step's deadline the reminder is sent. |
    | `notification_rules.is_enabled` | boolean |  |
    | `notification_rules.notified_proposal_roles` | array of strings |  |
    | `responsible_users` | array of objects |  |
    | `responsible_users.uuid` | string (uuid) |  |
    | `responsible_users.username` | string |  |
    | `responsible_users.full_name` | string |  |
    | `responsible_users.email` | string (email) |  |
    | `responsible_users.is_panel_chair` | boolean |  |

---

### Get COI configuration for this call

Get COI configuration for this call.


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/coi-configuration/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_call_coi_configuration_request import PatchedCallCOIConfigurationRequest # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_coi_configuration_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedCallCOIConfigurationRequest()
    response = proposal_protected_calls_coi_configuration_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedCallCOIConfigurationRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_call_coi_configuration_request.py)
    2.  **API Source:** [`proposal_protected_calls_coi_configuration_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_coi_configuration_partial_update.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsCoiConfigurationPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsCoiConfigurationPartialUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Request Body"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `coauthorship_lookback_years` | integer |  | Years to look back for co-authorship detection |
    | `coauthorship_threshold_papers` | integer |  | Minimum shared papers to trigger COI |
    | `institutional_lookback_years` | integer |  | Years to look back for former institution detection |
    | `include_same_department` | boolean |  | Detect same-department as COI |
    | `include_same_institution` | boolean |  | Detect same-institution as COI |
    | `recusal_required_types` | array of strings |  | COI types requiring automatic recusal |
    | `management_allowed_types` | array of strings |  | COI types allowing management plan |
    | `disclosure_only_types` | array of strings |  | COI types requiring disclosure only |
    | `auto_detect_coauthorship` | boolean |  | Enable automated co-authorship detection |
    | `auto_detect_institutional` | boolean |  | Enable automated institutional affiliation detection |
    | `auto_detect_named_personnel` | boolean |  | Enable detection of reviewer named in proposals |
    | `invitation_proposal_disclosure` | any |  | Level of proposal information disclosed in reviewer invitations |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `call` | string (uri) |  |
    | `call_uuid` | string (uuid) |  |
    | `call_name` | string |  |
    | `coauthorship_lookback_years` | integer | Years to look back for co-authorship detection |
    | `coauthorship_threshold_papers` | integer | Minimum shared papers to trigger COI |
    | `institutional_lookback_years` | integer | Years to look back for former institution detection |
    | `include_same_department` | boolean | Detect same-department as COI |
    | `include_same_institution` | boolean | Detect same-institution as COI |
    | `recusal_required_types` | array of strings | COI types requiring automatic recusal |
    | `management_allowed_types` | array of strings | COI types allowing management plan |
    | `disclosure_only_types` | array of strings | COI types requiring disclosure only |
    | `auto_detect_coauthorship` | boolean | Enable automated co-authorship detection |
    | `auto_detect_institutional` | boolean | Enable automated institutional affiliation detection |
    | `auto_detect_named_personnel` | boolean | Enable detection of reviewer named in proposals |
    | `invitation_proposal_disclosure` | any | Level of proposal information disclosed in reviewer invitations |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Get or update matching configuration for this call

Get or update matching configuration for this call.


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/proposal-protected-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/matching-configuration/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_matching_configuration_request import PatchedMatchingConfigurationRequest # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_matching_configuration_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedMatchingConfigurationRequest()
    response = proposal_protected_calls_matching_configuration_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedMatchingConfigurationRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_matching_configuration_request.py)
    2.  **API Source:** [`proposal_protected_calls_matching_configuration_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_matching_configuration_partial_update.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsMatchingConfigurationPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsMatchingConfigurationPartialUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Request Body"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `affinity_method` | string |  | <br>_Enum: `keyword`, `tfidf`, `combined`_ |
    | `keyword_weight` | number (double) |  |  |
    | `text_weight` | number (double) |  |  |
    | `min_reviewers_per_proposal` | integer |  |  |
    | `max_reviewers_per_proposal` | integer |  |  |
    | `min_proposals_per_reviewer` | integer |  |  |
    | `max_proposals_per_reviewer` | integer |  |  |
    | `algorithm` | string |  | <br>_Enum: `minmax`, `fairflow`, `hungarian`_ |
    | `min_affinity_threshold` | number (double) |  | Minimum affinity score for FairFlow algorithm |
    | `use_reviewer_bids` | boolean |  |  |
    | `bid_weight` | number (double) |  |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `call_uuid` | string (uuid) |  |
    | `call_name` | string |  |
    | `affinity_method` | string | <br>_Enum: `keyword`, `tfidf`, `combined`_ |
    | `keyword_weight` | number (double) |  |
    | `text_weight` | number (double) |  |
    | `min_reviewers_per_proposal` | integer |  |
    | `max_reviewers_per_proposal` | integer |  |
    | `min_proposals_per_reviewer` | integer |  |
    | `max_proposals_per_reviewer` | integer |  |
    | `algorithm` | string | <br>_Enum: `minmax`, `fairflow`, `hungarian`_ |
    | `min_affinity_threshold` | number (double) | Minimum affinity score for FairFlow algorithm |
    | `use_reviewer_bids` | boolean |  |
    | `bid_weight` | number (double) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/proposal-protected-calls/string-value/offerings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_requested_offering_request import PatchedRequestedOfferingRequest # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_offerings_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedRequestedOfferingRequest()
    response = proposal_protected_calls_offerings_partial_update.sync(
        obj_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        uuid="string-value",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedRequestedOfferingRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_requested_offering_request.py)
    2.  **API Source:** [`proposal_protected_calls_offerings_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_offerings_partial_update.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsOfferingsPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsOfferingsPartialUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "obj_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "uuid": "string-value"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `obj_uuid` | string | ✓ |
    | `uuid` | string | ✓ |


=== "Request Body"

    | Field | Type | Required |
    |---|---|---|
    | `attributes` | object (free-form) |  |
    | `plan` | string (uri) |  |
    | `description` | string |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `state` | any |  |
    | `offering` | string (uri) |  |
    | `offering_name` | string |  |
    | `offering_uuid` | string (uuid) |  |
    | `offering_type` | string |  |
    | `provider_name` | string |  |
    | `category_uuid` | string (uuid) |  |
    | `category_name` | string |  |
    | `call_managing_organisation` | string |  |
    | `attributes` | object (free-form) |  |
    | `plan` | string (uri) |  |
    | `plan_details` | any |  |
    | `options` | any |  |
    | `components` | array of objects |  |
    | `components.uuid` | string (uuid) |  |
    | `components.offering_uuid` | string (uuid) |  |
    | `components.billing_type` | string | <br>_Enum: `fixed`, `usage`, `limit`, `one`, `few`_ |
    | `components.type` | string | Unique internal name of the measured unit, for example floating_ip. |
    | `components.name` | string | Display name for the measured unit, for example, Floating IP. |
    | `components.description` | string |  |
    | `components.measured_unit` | string | Unit of measurement, for example, GB. |
    | `components.unit_factor` | integer | The conversion factor from backend units to measured_unit |
    | `components.limit_period` | any |  |
    | `components.limit_amount` | number (double) |  |
    | `components.limit_decimal_places` | integer | Number of decimal places accepted for this component's limit. 0 keeps the limit integer-only. |
    | `components.article_code` | string |  |
    | `components.max_value` | number (double) |  |
    | `components.min_value` | number (double) |  |
    | `components.max_available_limit` | number (double) |  |
    | `components.is_boolean` | boolean |  |
    | `components.default_limit` | number (double) |  |
    | `components.factor` | integer |  |
    | `components.is_builtin` | boolean | The API's older name for ``billed_per_plan``.  It used to ask the plugin registry whether this component's type is one the plugin declares, which left out the OpenStack per-volume-type quotas: they are created by the volume type sync rather than declared, so the API called them provider components while the billing resolver treated them as builtin. Reading the stored flag makes the two agree. |
    | `components.is_prepaid` | boolean |  |
    | `components.overage_component` | string (uuid) |  |
    | `components.min_prepaid_duration` | integer |  |
    | `components.max_prepaid_duration` | integer |  |
    | `components.prepaid_duration_step` | integer | Step size in months for the initial prepaid duration at order creation. If set, only multiples of this value (starting from min_prepaid_duration) are valid. Defaults to 1 (any value between min and max). |
    | `components.min_renewal_duration` | integer | Minimum number of months allowed for a renewal. |
    | `components.max_renewal_duration` | integer | Maximum number of months allowed for a renewal. |
    | `components.renewal_duration_step` | integer | Step size in months for renewal. Only multiples of this value (starting from min_renewal_duration) are valid. Defaults to 1. |
    | `require_purchase_order` | boolean | Whether a purchase order must accompany a resource request for this offering before the proposal can be submitted. Defaults to the offering's require_purchase_order_upload, and stays under the call manager's control afterwards. |
    | `created` | string (date-time) |  |
    | `url` | string |  |
    | `approved_by` | string (uri) |  |
    | `created_by` | string (uri) |  |
    | `created_by_name` | string |  |
    | `approved_by_name` | string |  |
    | `description` | string |  |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/proposal-protected-calls/string-value/resource_templates/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_call_resource_template_request import PatchedCallResourceTemplateRequest # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_resource_templates_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedCallResourceTemplateRequest()
    response = proposal_protected_calls_resource_templates_partial_update.sync(
        obj_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        uuid="string-value",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedCallResourceTemplateRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_call_resource_template_request.py)
    2.  **API Source:** [`proposal_protected_calls_resource_templates_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_resource_templates_partial_update.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsResourceTemplatesPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsResourceTemplatesPartialUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "obj_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "uuid": "string-value"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `obj_uuid` | string | ✓ |
    | `uuid` | string | ✓ |


=== "Request Body"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `name` | string |  |  |
    | `description` | string |  |  |
    | `attributes` | object (free-form) |  |  |
    | `limits` | object (free-form) |  |  |
    | `is_required` | boolean |  | If True, every proposal must include this resource type |
    | `requested_offering` | string (uri) |  |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string |  |
    | `name` | string |  |
    | `description` | string |  |
    | `attributes` | object (free-form) |  |
    | `limits` | object (free-form) |  |
    | `is_required` | boolean | If True, every proposal must include this resource type |
    | `requested_offering` | string (uri) |  |
    | `requested_offering_name` | string |  |
    | `requested_offering_uuid` | string (uuid) |  |
    | `requested_offering_plan` | any |  |
    | `requested_offering_type` | string |  |
    | `requested_offering_components` | array of objects |  |
    | `requested_offering_components.uuid` | string (uuid) |  |
    | `requested_offering_components.offering_uuid` | string (uuid) |  |
    | `requested_offering_components.billing_type` | string | <br>_Enum: `fixed`, `usage`, `limit`, `one`, `few`_ |
    | `requested_offering_components.type` | string | Unique internal name of the measured unit, for example floating_ip. |
    | `requested_offering_components.name` | string | Display name for the measured unit, for example, Floating IP. |
    | `requested_offering_components.description` | string |  |
    | `requested_offering_components.measured_unit` | string | Unit of measurement, for example, GB. |
    | `requested_offering_components.unit_factor` | integer | The conversion factor from backend units to measured_unit |
    | `requested_offering_components.limit_period` | any |  |
    | `requested_offering_components.limit_amount` | number (double) |  |
    | `requested_offering_components.limit_decimal_places` | integer | Number of decimal places accepted for this component's limit. 0 keeps the limit integer-only. |
    | `requested_offering_components.article_code` | string |  |
    | `requested_offering_components.max_value` | number (double) |  |
    | `requested_offering_components.min_value` | number (double) |  |
    | `requested_offering_components.max_available_limit` | number (double) |  |
    | `requested_offering_components.is_boolean` | boolean |  |
    | `requested_offering_components.default_limit` | number (double) |  |
    | `requested_offering_components.factor` | integer |  |
    | `requested_offering_components.is_builtin` | boolean | The API's older name for ``billed_per_plan``.  It used to ask the plugin registry whether this component's type is one the plugin declares, which left out the OpenStack per-volume-type quotas: they are created by the volume type sync rather than declared, so the API called them provider components while the billing resolver treated them as builtin. Reading the stored flag makes the two agree. |
    | `requested_offering_components.is_prepaid` | boolean |  |
    | `requested_offering_components.overage_component` | string (uuid) |  |
    | `requested_offering_components.min_prepaid_duration` | integer |  |
    | `requested_offering_components.max_prepaid_duration` | integer |  |
    | `requested_offering_components.prepaid_duration_step` | integer | Step size in months for the initial prepaid duration at order creation. If set, only multiples of this value (starting from min_prepaid_duration) are valid. Defaults to 1 (any value between min and max). |
    | `requested_offering_components.min_renewal_duration` | integer | Minimum number of months allowed for a renewal. |
    | `requested_offering_components.max_renewal_duration` | integer | Maximum number of months allowed for a renewal. |
    | `requested_offering_components.renewal_duration_step` | integer | Step size in months for renewal. Only multiples of this value (starting from min_renewal_duration) are valid. Defaults to 1. |
    | `created_by` | string (uri) |  |
    | `created_by_name` | string |  |
    | `created` | string (date-time) |  |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/proposal-protected-calls/string-value/rounds/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_protected_round_request import PatchedProtectedRoundRequest # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_rounds_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedProtectedRoundRequest()
    response = proposal_protected_calls_rounds_partial_update.sync(
        obj_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        uuid="string-value",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedProtectedRoundRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_protected_round_request.py)
    2.  **API Source:** [`proposal_protected_calls_rounds_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_rounds_partial_update.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsRoundsPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsRoundsPartialUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "obj_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "uuid": "string-value"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `obj_uuid` | string | ✓ |
    | `uuid` | string | ✓ |


=== "Request Body"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `start_time` | string (date-time) |  |  |
    | `cutoff_time` | string (date-time) |  |  |
    | `allocation_date` | string (date-time) |  |  |
    | `review_duration_in_days` | integer |  |  |
    | `undecided_at_round_completion` | any |  | Overrides the call's rule for proposals still without a decision when the round is completed. Empty: the call's rule applies. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `slug` | string |  |
    | `name` | string |  |
    | `start_time` | string (date-time) |  |
    | `cutoff_time` | string (date-time) |  |
    | `status` | any |  |
    | `allocation_date` | string (date-time) |  |
    | `review_duration_in_days` | integer |  |
    | `lifecycle_state` | any | Where the round stands after its cut-off: evaluating, deciding, results_published or closed. Empty before the cut-off. |
    | `evaluation_started_at` | string (date-time) |  |
    | `deciding_started_at` | string (date-time) |  |
    | `results_published_at` | string (date-time) |  |
    | `closed_at` | string (date-time) |  |
    | `url` | string |  |
    | `proposals` | array of objects |  |
    | `proposals.uuid` | string (uuid) |  |
    | `proposals.slug` | string |  |
    | `proposals.name` | string |  |
    | `proposals.state` | any |  |
    | `proposals.reviews` | array of anys | Return serialized reviews based on user permissions and visibility settings. - Staff, call managers, and reviewers see all reviews. - Submitters see submitted reviews if visibility is enabled. |
    | `proposals.approved_by_name` | string |  |
    | `proposals.created_by_name` | string |  |
    | `proposals.created` | string (date-time) |  |
    | `results_published_by_name` | string |  |
    | `held_decisions_count` | integer | Proposals of the round whose decision is recorded but not yet published. After publication, decisions that could not be carried out; publishing the results again retries them. Null for anyone who may not see held decisions. |
    | `has_proposals` | boolean | Whether the round holds any proposal, in any state. A round with proposals cannot be deleted. Unlike the proposals list, which leaves out what the viewer may not see, this counts every one. |
    | `results_forced_reason` | string | Why results were published while some proposals of the round still had no decision. |
    | `adopted_at` | string (date) | When the round's results were adopted. |
    | `adoption_note` | string |  |
    | `adoption_document` | string (uri) |  |
    | `undecided_at_round_completion` | any | Overrides the call's rule for proposals still without a decision when the round is completed. Empty: the call's rule applies. |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/proposal-protected-calls/string-value/workflow_steps/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_call_workflow_step_request import PatchedCallWorkflowStepRequest # (1)
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_workflow_steps_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedCallWorkflowStepRequest()
    response = proposal_protected_calls_workflow_steps_partial_update.sync(
        obj_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        uuid="string-value",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedCallWorkflowStepRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_call_workflow_step_request.py)
    2.  **API Source:** [`proposal_protected_calls_workflow_steps_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_workflow_steps_partial_update.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsWorkflowStepsPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsWorkflowStepsPartialUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "obj_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "uuid": "string-value"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `obj_uuid` | string | ✓ |
    | `uuid` | string | ✓ |


=== "Request Body"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `is_enabled` | boolean |  | Whether this step is enabled. Disabled steps are skipped. |
    | `duration_in_days` | integer |  | Duration in days. Used to calculate deadlines. |
    | `checklist` | string (uuid) |  |  |
    | `checklist_required` | boolean |  | When the step has a checklist, block completion until its required questions are answered. Set False to make the checklist advisory. |
    | `blind_review` | boolean |  | Evaluators cannot see each other's assessments. |
    | `requires_coi_confirmation` | boolean |  | Evaluator must confirm absence of conflict of interest. |
    | `min_reviewers` | integer |  | Minimum reviews required before step can complete. |
    | `min_score_threshold` | string (decimal) |  | Minimum average score required before this step can complete (a completion gate; it does not auto-reject lower scores). |
    | `applicant_visible` | boolean |  | Whether the applicant can see step details (not just status). |
    | `responsible_role` | any |  | Role expected to act on this step. |
    | `transition_mode` | any |  | How this step advances once a human completes it. 'Automatic' advances to the next step immediately; 'Manual' waits for a separate advance action. Neither auto-decides from review scores. |
    | `include_award_response` | boolean |  | Allocation decision: require applicant award response after decision. |
    | `allocation_time` | any |  | Allocation decision: when a granted proposal takes effect — immediately (on_decision) or on the round's allocation date (fixed_date). |
    | `display_order` | integer |  | Optional override of catalog ordering. |
    | `criteria` | array of objects |  |  |
    | `criteria.name` | string | ✓ |  |
    | `criteria.order` | integer |  |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `step` | string | <br>_Enum: `administrative_check`, `technical_assessment`, `expert_review`, `panel_review`, `allocation_decision`, `award_response`_ |
    | `call_uuid` | string (uuid) |  |
    | `call_name` | string |  |
    | `is_enabled` | boolean | Whether this step is enabled. Disabled steps are skipped. |
    | `is_mandatory` | boolean |  |
    | `duration_in_days` | integer | Duration in days. Used to calculate deadlines. |
    | `checklist` | string (uuid) |  |
    | `checklist_name` | string |  |
    | `checklist_required` | boolean | When the step has a checklist, block completion until its required questions are answered. Set False to make the checklist advisory. |
    | `blind_review` | boolean | Evaluators cannot see each other's assessments. |
    | `requires_coi_confirmation` | boolean | Evaluator must confirm absence of conflict of interest. |
    | `min_reviewers` | integer | Minimum reviews required before step can complete. |
    | `min_score_threshold` | string (decimal) | Minimum average score required before this step can complete (a completion gate; it does not auto-reject lower scores). |
    | `applicant_visible` | boolean | Whether the applicant can see step details (not just status). |
    | `responsible_role` | any | Role expected to act on this step. |
    | `transition_mode` | any | How this step advances once a human completes it. 'Automatic' advances to the next step immediately; 'Manual' waits for a separate advance action. Neither auto-decides from review scores. |
    | `include_award_response` | boolean | Allocation decision: require applicant award response after decision. |
    | `allocation_time` | any | Allocation decision: when a granted proposal takes effect — immediately (on_decision) or on the round's allocation date (fixed_date). |
    | `display_order` | integer | Optional override of catalog ordering. |
    | `criteria` | array of objects |  |
    | `criteria.uuid` | string (uuid) |  |
    | `criteria.name` | string |  |
    | `criteria.order` | integer |  |
    | `notification_rules` | array of objects |  |
    | `notification_rules.uuid` | string (uuid) |  |
    | `notification_rules.trigger` | any |  |
    | `notification_rules.recipient` | any |  |
    | `notification_rules.days_before` | integer | Only for deadline_approaching: how many days before the step's deadline the reminder is sent. |
    | `notification_rules.is_enabled` | boolean |  |
    | `notification_rules.notified_proposal_roles` | array of strings |  |
    | `responsible_users` | array of objects |  |
    | `responsible_users.uuid` | string (uuid) |  |
    | `responsible_users.username` | string |  |
    | `responsible_users.full_name` | string |  |
    | `responsible_users.email` | string (email) |  |
    | `responsible_users.is_panel_chair` | boolean |  |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/proposal-protected-calls/string-value/offerings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_offerings_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_offerings_destroy.sync(
        obj_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        uuid="string-value",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`proposal_protected_calls_offerings_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_offerings_destroy.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsOfferingsDestroy } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsOfferingsDestroy({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "obj_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "uuid": "string-value"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `obj_uuid` | string | ✓ |
    | `uuid` | string | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `state` | any |  |
    | `offering` | string (uri) |  |
    | `offering_name` | string |  |
    | `offering_uuid` | string (uuid) |  |
    | `offering_type` | string |  |
    | `provider_name` | string |  |
    | `category_uuid` | string (uuid) |  |
    | `category_name` | string |  |
    | `call_managing_organisation` | string |  |
    | `attributes` | object (free-form) |  |
    | `plan` | string (uri) |  |
    | `plan_details` | any |  |
    | `options` | any |  |
    | `components` | array of objects |  |
    | `components.uuid` | string (uuid) |  |
    | `components.offering_uuid` | string (uuid) |  |
    | `components.billing_type` | string | <br>_Enum: `fixed`, `usage`, `limit`, `one`, `few`_ |
    | `components.type` | string | Unique internal name of the measured unit, for example floating_ip. |
    | `components.name` | string | Display name for the measured unit, for example, Floating IP. |
    | `components.description` | string |  |
    | `components.measured_unit` | string | Unit of measurement, for example, GB. |
    | `components.unit_factor` | integer | The conversion factor from backend units to measured_unit |
    | `components.limit_period` | any |  |
    | `components.limit_amount` | number (double) |  |
    | `components.limit_decimal_places` | integer | Number of decimal places accepted for this component's limit. 0 keeps the limit integer-only. |
    | `components.article_code` | string |  |
    | `components.max_value` | number (double) |  |
    | `components.min_value` | number (double) |  |
    | `components.max_available_limit` | number (double) |  |
    | `components.is_boolean` | boolean |  |
    | `components.default_limit` | number (double) |  |
    | `components.factor` | integer |  |
    | `components.is_builtin` | boolean | The API's older name for ``billed_per_plan``.  It used to ask the plugin registry whether this component's type is one the plugin declares, which left out the OpenStack per-volume-type quotas: they are created by the volume type sync rather than declared, so the API called them provider components while the billing resolver treated them as builtin. Reading the stored flag makes the two agree. |
    | `components.is_prepaid` | boolean |  |
    | `components.overage_component` | string (uuid) |  |
    | `components.min_prepaid_duration` | integer |  |
    | `components.max_prepaid_duration` | integer |  |
    | `components.prepaid_duration_step` | integer | Step size in months for the initial prepaid duration at order creation. If set, only multiples of this value (starting from min_prepaid_duration) are valid. Defaults to 1 (any value between min and max). |
    | `components.min_renewal_duration` | integer | Minimum number of months allowed for a renewal. |
    | `components.max_renewal_duration` | integer | Maximum number of months allowed for a renewal. |
    | `components.renewal_duration_step` | integer | Step size in months for renewal. Only multiples of this value (starting from min_renewal_duration) are valid. Defaults to 1. |
    | `require_purchase_order` | boolean | Whether a purchase order must accompany a resource request for this offering before the proposal can be submitted. Defaults to the offering's require_purchase_order_upload, and stays under the call manager's control afterwards. |
    | `created` | string (date-time) |  |
    | `url` | string |  |
    | `approved_by` | string (uri) |  |
    | `created_by` | string (uri) |  |
    | `created_by_name` | string |  |
    | `approved_by_name` | string |  |
    | `description` | string |  |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/proposal-protected-calls/string-value/resource_templates/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_resource_templates_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_resource_templates_destroy.sync(
        obj_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        uuid="string-value",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`proposal_protected_calls_resource_templates_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_resource_templates_destroy.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsResourceTemplatesDestroy } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsResourceTemplatesDestroy({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "obj_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "uuid": "string-value"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `obj_uuid` | string | ✓ |
    | `uuid` | string | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string |  |
    | `name` | string |  |
    | `description` | string |  |
    | `attributes` | object (free-form) |  |
    | `limits` | object (free-form) |  |
    | `is_required` | boolean | If True, every proposal must include this resource type |
    | `requested_offering` | string (uri) |  |
    | `requested_offering_name` | string |  |
    | `requested_offering_uuid` | string (uuid) |  |
    | `requested_offering_plan` | any |  |
    | `requested_offering_type` | string |  |
    | `requested_offering_components` | array of objects |  |
    | `requested_offering_components.uuid` | string (uuid) |  |
    | `requested_offering_components.offering_uuid` | string (uuid) |  |
    | `requested_offering_components.billing_type` | string | <br>_Enum: `fixed`, `usage`, `limit`, `one`, `few`_ |
    | `requested_offering_components.type` | string | Unique internal name of the measured unit, for example floating_ip. |
    | `requested_offering_components.name` | string | Display name for the measured unit, for example, Floating IP. |
    | `requested_offering_components.description` | string |  |
    | `requested_offering_components.measured_unit` | string | Unit of measurement, for example, GB. |
    | `requested_offering_components.unit_factor` | integer | The conversion factor from backend units to measured_unit |
    | `requested_offering_components.limit_period` | any |  |
    | `requested_offering_components.limit_amount` | number (double) |  |
    | `requested_offering_components.limit_decimal_places` | integer | Number of decimal places accepted for this component's limit. 0 keeps the limit integer-only. |
    | `requested_offering_components.article_code` | string |  |
    | `requested_offering_components.max_value` | number (double) |  |
    | `requested_offering_components.min_value` | number (double) |  |
    | `requested_offering_components.max_available_limit` | number (double) |  |
    | `requested_offering_components.is_boolean` | boolean |  |
    | `requested_offering_components.default_limit` | number (double) |  |
    | `requested_offering_components.factor` | integer |  |
    | `requested_offering_components.is_builtin` | boolean | The API's older name for ``billed_per_plan``.  It used to ask the plugin registry whether this component's type is one the plugin declares, which left out the OpenStack per-volume-type quotas: they are created by the volume type sync rather than declared, so the API called them provider components while the billing resolver treated them as builtin. Reading the stored flag makes the two agree. |
    | `requested_offering_components.is_prepaid` | boolean |  |
    | `requested_offering_components.overage_component` | string (uuid) |  |
    | `requested_offering_components.min_prepaid_duration` | integer |  |
    | `requested_offering_components.max_prepaid_duration` | integer |  |
    | `requested_offering_components.prepaid_duration_step` | integer | Step size in months for the initial prepaid duration at order creation. If set, only multiples of this value (starting from min_prepaid_duration) are valid. Defaults to 1 (any value between min and max). |
    | `requested_offering_components.min_renewal_duration` | integer | Minimum number of months allowed for a renewal. |
    | `requested_offering_components.max_renewal_duration` | integer | Maximum number of months allowed for a renewal. |
    | `requested_offering_components.renewal_duration_step` | integer | Step size in months for renewal. Only multiples of this value (starting from min_renewal_duration) are valid. Defaults to 1. |
    | `created_by` | string (uri) |  |
    | `created_by_name` | string |  |
    | `created` | string (date-time) |  |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/proposal-protected-calls/string-value/rounds/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_rounds_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_rounds_destroy.sync(
        obj_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        uuid="string-value",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`proposal_protected_calls_rounds_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_rounds_destroy.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsRoundsDestroy } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsRoundsDestroy({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "obj_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "uuid": "string-value"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `obj_uuid` | string | ✓ |
    | `uuid` | string | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `slug` | string |  |
    | `name` | string |  |
    | `start_time` | string (date-time) |  |
    | `cutoff_time` | string (date-time) |  |
    | `status` | any |  |
    | `allocation_date` | string (date-time) |  |
    | `review_duration_in_days` | integer |  |
    | `lifecycle_state` | any | Where the round stands after its cut-off: evaluating, deciding, results_published or closed. Empty before the cut-off. |
    | `evaluation_started_at` | string (date-time) |  |
    | `deciding_started_at` | string (date-time) |  |
    | `results_published_at` | string (date-time) |  |
    | `closed_at` | string (date-time) |  |
    | `url` | string |  |
    | `proposals` | array of objects |  |
    | `proposals.uuid` | string (uuid) |  |
    | `proposals.slug` | string |  |
    | `proposals.name` | string |  |
    | `proposals.state` | any |  |
    | `proposals.reviews` | array of anys | Return serialized reviews based on user permissions and visibility settings. - Staff, call managers, and reviewers see all reviews. - Submitters see submitted reviews if visibility is enabled. |
    | `proposals.approved_by_name` | string |  |
    | `proposals.created_by_name` | string |  |
    | `proposals.created` | string (date-time) |  |
    | `results_published_by_name` | string |  |
    | `held_decisions_count` | integer | Proposals of the round whose decision is recorded but not yet published. After publication, decisions that could not be carried out; publishing the results again retries them. Null for anyone who may not see held decisions. |
    | `has_proposals` | boolean | Whether the round holds any proposal, in any state. A round with proposals cannot be deleted. Unlike the proposals list, which leaves out what the viewer may not see, this counts every one. |
    | `results_forced_reason` | string | Why results were published while some proposals of the round still had no decision. |
    | `adopted_at` | string (date) | When the round's results were adopted. |
    | `adoption_note` | string |  |
    | `adoption_document` | string (uri) |  |
    | `undecided_at_round_completion` | any | Overrides the call's rule for proposals still without a decision when the round is completed. Empty: the call's rule applies. |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/proposal-protected-calls/string-value/workflow_steps/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.proposal_protected_calls import proposal_protected_calls_workflow_steps_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_protected_calls_workflow_steps_destroy.sync(
        obj_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        uuid="string-value",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`proposal_protected_calls_workflow_steps_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_protected_calls/proposal_protected_calls_workflow_steps_destroy.py)

=== "TypeScript"

    ```typescript
    import { proposalProtectedCallsWorkflowStepsDestroy } from 'waldur-js-client';
    
    try {
      const response = await proposalProtectedCallsWorkflowStepsDestroy({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "obj_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "uuid": "string-value"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `obj_uuid` | string | ✓ |
    | `uuid` | string | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `step` | string | <br>_Enum: `administrative_check`, `technical_assessment`, `expert_review`, `panel_review`, `allocation_decision`, `award_response`_ |
    | `call_uuid` | string (uuid) |  |
    | `call_name` | string |  |
    | `is_enabled` | boolean | Whether this step is enabled. Disabled steps are skipped. |
    | `is_mandatory` | boolean |  |
    | `duration_in_days` | integer | Duration in days. Used to calculate deadlines. |
    | `checklist` | string (uuid) |  |
    | `checklist_name` | string |  |
    | `checklist_required` | boolean | When the step has a checklist, block completion until its required questions are answered. Set False to make the checklist advisory. |
    | `blind_review` | boolean | Evaluators cannot see each other's assessments. |
    | `requires_coi_confirmation` | boolean | Evaluator must confirm absence of conflict of interest. |
    | `min_reviewers` | integer | Minimum reviews required before step can complete. |
    | `min_score_threshold` | string (decimal) | Minimum average score required before this step can complete (a completion gate; it does not auto-reject lower scores). |
    | `applicant_visible` | boolean | Whether the applicant can see step details (not just status). |
    | `responsible_role` | any | Role expected to act on this step. |
    | `transition_mode` | any | How this step advances once a human completes it. 'Automatic' advances to the next step immediately; 'Manual' waits for a separate advance action. Neither auto-decides from review scores. |
    | `include_award_response` | boolean | Allocation decision: require applicant award response after decision. |
    | `allocation_time` | any | Allocation decision: when a granted proposal takes effect — immediately (on_decision) or on the round's allocation date (fixed_date). |
    | `display_order` | integer | Optional override of catalog ordering. |
    | `criteria` | array of objects |  |
    | `criteria.uuid` | string (uuid) |  |
    | `criteria.name` | string |  |
    | `criteria.order` | integer |  |
    | `notification_rules` | array of objects |  |
    | `notification_rules.uuid` | string (uuid) |  |
    | `notification_rules.trigger` | any |  |
    | `notification_rules.recipient` | any |  |
    | `notification_rules.days_before` | integer | Only for deadline_approaching: how many days before the step's deadline the reminder is sent. |
    | `notification_rules.is_enabled` | boolean |  |
    | `notification_rules.notified_proposal_roles` | array of strings |  |
    | `responsible_users` | array of objects |  |
    | `responsible_users.uuid` | string (uuid) |  |
    | `responsible_users.username` | string |  |
    | `responsible_users.full_name` | string |  |
    | `responsible_users.email` | string (email) |  |
    | `responsible_users.is_panel_chair` | boolean |  |

---
