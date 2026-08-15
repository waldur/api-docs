# Proposal Public Calls

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/proposal-public-calls/` | [List Proposal Public Calls](#list-proposal-public-calls) |
| <span class="http-badge http-get">GET</span> | `/api/proposal-public-calls/{uuid}/` | [Retrieve](#retrieve) |
| **Other Actions** | | |
| <span class="http-badge http-get">GET</span> | `/api/proposal-public-calls/{uuid}/check_eligibility/` | [Check if the current user is eligible to submit proposals to this call](#check-if-the-current-user-is-eligible-to-submit-proposals-to-this-call) |

---
## Core CRUD


### List Proposal Public Calls


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/proposal-public-calls/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.call_states import CallStates # (1)
    from waldur_api_client.models.protected_call_o_enum import ProtectedCallOEnum # (2)
    from waldur_api_client.models.public_call_field_enum import PublicCallFieldEnum # (3)
    from waldur_api_client.api.proposal_public_calls import proposal_public_calls_list # (4)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_public_calls_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`CallStates`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/call_states.py)
    2.  **Model Source:** [`ProtectedCallOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/protected_call_o_enum.py)
    3.  **Model Source:** [`PublicCallFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/public_call_field_enum.py)
    4.  **API Source:** [`proposal_public_calls_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_public_calls/proposal_public_calls_list.py)

=== "TypeScript"

    ```typescript
    import { proposalPublicCallsList } from 'waldur-js-client';
    
    try {
      const response = await proposalPublicCallsList({
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
    | `offerings.components.limit_amount` | integer |  |
    | `offerings.components.article_code` | string |  |
    | `offerings.components.max_value` | integer |  |
    | `offerings.components.min_value` | integer |  |
    | `offerings.components.max_available_limit` | integer |  |
    | `offerings.components.is_boolean` | boolean |  |
    | `offerings.components.default_limit` | integer |  |
    | `offerings.components.factor` | integer |  |
    | `offerings.components.is_builtin` | boolean |  |
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
    | `resource_templates.requested_offering_components.limit_amount` | integer |  |
    | `resource_templates.requested_offering_components.article_code` | string |  |
    | `resource_templates.requested_offering_components.max_value` | integer |  |
    | `resource_templates.requested_offering_components.min_value` | integer |  |
    | `resource_templates.requested_offering_components.max_available_limit` | integer |  |
    | `resource_templates.requested_offering_components.is_boolean` | boolean |  |
    | `resource_templates.requested_offering_components.default_limit` | integer |  |
    | `resource_templates.requested_offering_components.factor` | integer |  |
    | `resource_templates.requested_offering_components.is_builtin` | boolean |  |
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
    | `fixed_duration_in_days` | integer | Fixed duration in days that applies to all proposals in this call |
    | `backend_id` | string |  |
    | `external_url` | string (uri) |  |
    | `reviewer_identity_visible_to_submitters` | boolean | Whether proposal applicants can see reviewer identities. If False, reviewers appear as 'Reviewer 1', 'Reviewer 2', etc. |
    | `reviews_visible_to_submitters` | boolean | Whether proposal applicants can see review comments and scores. If False, applicants only see final approval/rejection status. |
    | `has_eligibility_restrictions` | boolean | Check if call has any eligibility restrictions configured. |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/proposal-public-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.public_call_field_enum import PublicCallFieldEnum # (1)
    from waldur_api_client.api.proposal_public_calls import proposal_public_calls_retrieve # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_public_calls_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PublicCallFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/public_call_field_enum.py)
    2.  **API Source:** [`proposal_public_calls_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_public_calls/proposal_public_calls_retrieve.py)

=== "TypeScript"

    ```typescript
    import { proposalPublicCallsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await proposalPublicCallsRetrieve({
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
    | `offerings.components.limit_amount` | integer |  |
    | `offerings.components.article_code` | string |  |
    | `offerings.components.max_value` | integer |  |
    | `offerings.components.min_value` | integer |  |
    | `offerings.components.max_available_limit` | integer |  |
    | `offerings.components.is_boolean` | boolean |  |
    | `offerings.components.default_limit` | integer |  |
    | `offerings.components.factor` | integer |  |
    | `offerings.components.is_builtin` | boolean |  |
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
    | `resource_templates.requested_offering_components.limit_amount` | integer |  |
    | `resource_templates.requested_offering_components.article_code` | string |  |
    | `resource_templates.requested_offering_components.max_value` | integer |  |
    | `resource_templates.requested_offering_components.min_value` | integer |  |
    | `resource_templates.requested_offering_components.max_available_limit` | integer |  |
    | `resource_templates.requested_offering_components.is_boolean` | boolean |  |
    | `resource_templates.requested_offering_components.default_limit` | integer |  |
    | `resource_templates.requested_offering_components.factor` | integer |  |
    | `resource_templates.requested_offering_components.is_builtin` | boolean |  |
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
    | `fixed_duration_in_days` | integer | Fixed duration in days that applies to all proposals in this call |
    | `backend_id` | string |  |
    | `external_url` | string (uri) |  |
    | `reviewer_identity_visible_to_submitters` | boolean | Whether proposal applicants can see reviewer identities. If False, reviewers appear as 'Reviewer 1', 'Reviewer 2', etc. |
    | `reviews_visible_to_submitters` | boolean | Whether proposal applicants can see review comments and scores. If False, applicants only see final approval/rejection status. |
    | `has_eligibility_restrictions` | boolean | Check if call has any eligibility restrictions configured. |

---

## Other Actions


### Check if the current user is eligible to submit proposals to this call

Check if the current user is eligible to submit proposals to this call.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/proposal-public-calls/a1b2c3d4-e5f6-7890-abcd-ef1234567890/check_eligibility/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.proposal_public_calls import proposal_public_calls_check_eligibility_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_public_calls_check_eligibility_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`proposal_public_calls_check_eligibility_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_public_calls/proposal_public_calls_check_eligibility_retrieve.py)

=== "TypeScript"

    ```typescript
    import { proposalPublicCallsCheckEligibilityRetrieve } from 'waldur-js-client';
    
    try {
      const response = await proposalPublicCallsCheckEligibilityRetrieve({
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
    | `is_eligible` | boolean |
    | `restrictions` | array of strings |

---
