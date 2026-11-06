# Marketplace Offering Estimated Cost Policies

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-offering-estimated-cost-policies/` | [List Marketplace Offering Estimated Cost Policies](#list-marketplace-offering-estimated-cost-policies) |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-offering-estimated-cost-policies/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-offering-estimated-cost-policies/` | [Create](#create) |
| <span class="http-badge http-put">PUT</span> | `/api/marketplace-offering-estimated-cost-policies/{uuid}/` | [Update](#update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/marketplace-offering-estimated-cost-policies/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-delete">DELETE</span> | `/api/marketplace-offering-estimated-cost-policies/{uuid}/` | [Delete](#delete) |
| **Other Actions** | | |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-offering-estimated-cost-policies/actions/` | [List available actions for OfferingEstimatedCostPolicy](#list-available-actions-for-offeringestimatedcostpolicy) |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-offering-estimated-cost-policies/{uuid}/history/at/` | [Get object state at a specific timestamp](#get-object-state-at-a-specific-timestamp) |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-offering-estimated-cost-policies/{uuid}/history/` | [Get version history](#get-version-history) |

---
## Core CRUD


### List Marketplace Offering Estimated Cost Policies


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-offering-estimated-cost-policies/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.offering_estimated_cost_policy_field_enum import OfferingEstimatedCostPolicyFieldEnum # (1)
    from waldur_api_client.api.marketplace_offering_estimated_cost_policies import marketplace_offering_estimated_cost_policies_list # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_offering_estimated_cost_policies_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`OfferingEstimatedCostPolicyFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/offering_estimated_cost_policy_field_enum.py)
    2.  **API Source:** [`marketplace_offering_estimated_cost_policies_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_estimated_cost_policies/marketplace_offering_estimated_cost_policies_list.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingEstimatedCostPoliciesList } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingEstimatedCostPoliciesList({
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
    | `field` | array |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `scope` | string (uri) |  |
    | `scope_uuid` | string (uuid) |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `scope` | string (uri) |  |
    | `scope_name` | string |  |
    | `scope_uuid` | string (uuid) |  |
    | `actions` | string |  |
    | `created` | string (date-time) |  |
    | `created_by_full_name` | string |  |
    | `created_by_username` | string |  |
    | `has_fired` | boolean |  |
    | `fired_datetime` | string (date-time) |  |
    | `options` | object (free-form) | Fields for saving actions extra data. Keys are name of actions. |
    | `affected_resources_count` | integer |  |
    | `limit_cost` | integer |  |
    | `period` | any |  |
    | `period_name` | string |  |
    | `current_cost` | string (decimal) | The cost this policy compares against limit_cost right now: the period's invoice total, less the credit already applied and the credit still to be drawn, or the full cost for a policy that does not take credit into account. Do not re-derive it — only the server can simulate the pending draw, and a figure computed from the invoice alone will not match what the policy evaluates. |
    | `cost_breakdown` | any |  |
    | `eta_days` | integer | Days until the policy fires, or null when no projection exists. 0 means the threshold is already crossed and the policy is triggered — measured, not projected. Null must be rendered as no date, never as 'now': it is the common case, and it is also what an unprojectable or more-than-a-year-away policy reports. Nothing is projected beyond 365 days, because the rate comes from the current month's spend. |
    | `eta_date` | string (date) | eta_days as a calendar date, so clients do not each re-derive it. Null whenever eta_days is null; today when eta_days is 0. |
    | `trigger_status` | any |  |
    | `organization_groups` | array of string (uri)s |  |
    | `apply_to_all` | boolean | If True, policy applies to all customers. Mutually exclusive with organization_groups. |


=== "Authorization"

    Any signed-in user.
    
    Returns only objects the caller holds a role on; staff and support see all.

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-offering-estimated-cost-policies/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.offering_estimated_cost_policy_field_enum import OfferingEstimatedCostPolicyFieldEnum # (1)
    from waldur_api_client.api.marketplace_offering_estimated_cost_policies import marketplace_offering_estimated_cost_policies_retrieve # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_offering_estimated_cost_policies_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`OfferingEstimatedCostPolicyFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/offering_estimated_cost_policy_field_enum.py)
    2.  **API Source:** [`marketplace_offering_estimated_cost_policies_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_estimated_cost_policies/marketplace_offering_estimated_cost_policies_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingEstimatedCostPoliciesRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingEstimatedCostPoliciesRetrieve({
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
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `scope` | string (uri) |  |
    | `scope_name` | string |  |
    | `scope_uuid` | string (uuid) |  |
    | `actions` | string |  |
    | `created` | string (date-time) |  |
    | `created_by_full_name` | string |  |
    | `created_by_username` | string |  |
    | `has_fired` | boolean |  |
    | `fired_datetime` | string (date-time) |  |
    | `options` | object (free-form) | Fields for saving actions extra data. Keys are name of actions. |
    | `affected_resources_count` | integer |  |
    | `limit_cost` | integer |  |
    | `period` | any |  |
    | `period_name` | string |  |
    | `current_cost` | string (decimal) | The cost this policy compares against limit_cost right now: the period's invoice total, less the credit already applied and the credit still to be drawn, or the full cost for a policy that does not take credit into account. Do not re-derive it — only the server can simulate the pending draw, and a figure computed from the invoice alone will not match what the policy evaluates. |
    | `cost_breakdown` | any |  |
    | `eta_days` | integer | Days until the policy fires, or null when no projection exists. 0 means the threshold is already crossed and the policy is triggered — measured, not projected. Null must be rendered as no date, never as 'now': it is the common case, and it is also what an unprojectable or more-than-a-year-away policy reports. Nothing is projected beyond 365 days, because the rate comes from the current month's spend. |
    | `eta_date` | string (date) | eta_days as a calendar date, so clients do not each re-derive it. Null whenever eta_days is null; today when eta_days is 0. |
    | `trigger_status` | any |  |
    | `organization_groups` | array of string (uri)s |  |
    | `apply_to_all` | boolean | If True, policy applies to all customers. Mutually exclusive with organization_groups. |


=== "Authorization"

    Any signed-in user.
    
    Returns only objects the caller holds a role on; staff and support see all.

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-offering-estimated-cost-policies/ \
      Authorization:"Token YOUR_API_TOKEN" \
      scope="https://api.example.com/api/scope/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      actions="string-value" \
      limit_cost=123
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.offering_estimated_cost_policy_request import OfferingEstimatedCostPolicyRequest # (1)
    from waldur_api_client.api.marketplace_offering_estimated_cost_policies import marketplace_offering_estimated_cost_policies_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = OfferingEstimatedCostPolicyRequest(
        scope="https://api.example.com/api/scope/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        actions="string-value",
        limit_cost=123
    )
    response = marketplace_offering_estimated_cost_policies_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`OfferingEstimatedCostPolicyRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/offering_estimated_cost_policy_request.py)
    2.  **API Source:** [`marketplace_offering_estimated_cost_policies_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_estimated_cost_policies/marketplace_offering_estimated_cost_policies_create.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingEstimatedCostPoliciesCreate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingEstimatedCostPoliciesCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "scope": "https://api.example.com/api/scope/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "actions": "string-value",
        "limit_cost": 123
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
    | `scope` | string (uri) | ✓ |  |
    | `actions` | string | ✓ |  |
    | `options` | object (free-form) |  | Fields for saving actions extra data. Keys are name of actions. |
    | `limit_cost` | integer | ✓ |  |
    | `period` | any |  |  |
    | `organization_groups` | array of string (uri)s |  |  |
    | `apply_to_all` | boolean |  | If True, policy applies to all customers. Mutually exclusive with organization_groups. |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `scope` | string (uri) |  |
    | `scope_name` | string |  |
    | `scope_uuid` | string (uuid) |  |
    | `actions` | string |  |
    | `created` | string (date-time) |  |
    | `created_by_full_name` | string |  |
    | `created_by_username` | string |  |
    | `has_fired` | boolean |  |
    | `fired_datetime` | string (date-time) |  |
    | `options` | object (free-form) | Fields for saving actions extra data. Keys are name of actions. |
    | `affected_resources_count` | integer |  |
    | `limit_cost` | integer |  |
    | `period` | any |  |
    | `period_name` | string |  |
    | `current_cost` | string (decimal) | The cost this policy compares against limit_cost right now: the period's invoice total, less the credit already applied and the credit still to be drawn, or the full cost for a policy that does not take credit into account. Do not re-derive it — only the server can simulate the pending draw, and a figure computed from the invoice alone will not match what the policy evaluates. |
    | `cost_breakdown` | any |  |
    | `eta_days` | integer | Days until the policy fires, or null when no projection exists. 0 means the threshold is already crossed and the policy is triggered — measured, not projected. Null must be rendered as no date, never as 'now': it is the common case, and it is also what an unprojectable or more-than-a-year-away policy reports. Nothing is projected beyond 365 days, because the rate comes from the current month's spend. |
    | `eta_date` | string (date) | eta_days as a calendar date, so clients do not each re-derive it. Null whenever eta_days is null; today when eta_days is 0. |
    | `trigger_status` | any |  |
    | `organization_groups` | array of string (uri)s |  |
    | `apply_to_all` | boolean | If True, policy applies to all customers. Mutually exclusive with organization_groups. |


=== "Authorization"

    For the `scope` named in the request, the `CUSTOMER.OWNER` role on its customer.
    
    A request acting as staff always meets the permission and role requirements.

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/marketplace-offering-estimated-cost-policies/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      scope="https://api.example.com/api/scope/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      actions="string-value" \
      limit_cost=123
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.offering_estimated_cost_policy_request import OfferingEstimatedCostPolicyRequest # (1)
    from waldur_api_client.api.marketplace_offering_estimated_cost_policies import marketplace_offering_estimated_cost_policies_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = OfferingEstimatedCostPolicyRequest(
        scope="https://api.example.com/api/scope/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        actions="string-value",
        limit_cost=123
    )
    response = marketplace_offering_estimated_cost_policies_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`OfferingEstimatedCostPolicyRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/offering_estimated_cost_policy_request.py)
    2.  **API Source:** [`marketplace_offering_estimated_cost_policies_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_estimated_cost_policies/marketplace_offering_estimated_cost_policies_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingEstimatedCostPoliciesUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingEstimatedCostPoliciesUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "scope": "https://api.example.com/api/scope/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "actions": "string-value",
        "limit_cost": 123
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
    | `scope` | string (uri) | ✓ |  |
    | `actions` | string | ✓ |  |
    | `options` | object (free-form) |  | Fields for saving actions extra data. Keys are name of actions. |
    | `limit_cost` | integer | ✓ |  |
    | `period` | any |  |  |
    | `organization_groups` | array of string (uri)s |  |  |
    | `apply_to_all` | boolean |  | If True, policy applies to all customers. Mutually exclusive with organization_groups. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `scope` | string (uri) |  |
    | `scope_name` | string |  |
    | `scope_uuid` | string (uuid) |  |
    | `actions` | string |  |
    | `created` | string (date-time) |  |
    | `created_by_full_name` | string |  |
    | `created_by_username` | string |  |
    | `has_fired` | boolean |  |
    | `fired_datetime` | string (date-time) |  |
    | `options` | object (free-form) | Fields for saving actions extra data. Keys are name of actions. |
    | `affected_resources_count` | integer |  |
    | `limit_cost` | integer |  |
    | `period` | any |  |
    | `period_name` | string |  |
    | `current_cost` | string (decimal) | The cost this policy compares against limit_cost right now: the period's invoice total, less the credit already applied and the credit still to be drawn, or the full cost for a policy that does not take credit into account. Do not re-derive it — only the server can simulate the pending draw, and a figure computed from the invoice alone will not match what the policy evaluates. |
    | `cost_breakdown` | any |  |
    | `eta_days` | integer | Days until the policy fires, or null when no projection exists. 0 means the threshold is already crossed and the policy is triggered — measured, not projected. Null must be rendered as no date, never as 'now': it is the common case, and it is also what an unprojectable or more-than-a-year-away policy reports. Nothing is projected beyond 365 days, because the rate comes from the current month's spend. |
    | `eta_date` | string (date) | eta_days as a calendar date, so clients do not each re-derive it. Null whenever eta_days is null; today when eta_days is 0. |
    | `trigger_status` | any |  |
    | `organization_groups` | array of string (uri)s |  |
    | `apply_to_all` | boolean | If True, policy applies to all customers. Mutually exclusive with organization_groups. |


=== "Authorization"

    The `CUSTOMER.OWNER` role on the customer.
    
    A request acting as staff always meets the permission and role requirements.

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/marketplace-offering-estimated-cost-policies/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_offering_estimated_cost_policy_request import PatchedOfferingEstimatedCostPolicyRequest # (1)
    from waldur_api_client.api.marketplace_offering_estimated_cost_policies import marketplace_offering_estimated_cost_policies_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedOfferingEstimatedCostPolicyRequest()
    response = marketplace_offering_estimated_cost_policies_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedOfferingEstimatedCostPolicyRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_offering_estimated_cost_policy_request.py)
    2.  **API Source:** [`marketplace_offering_estimated_cost_policies_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_estimated_cost_policies/marketplace_offering_estimated_cost_policies_partial_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingEstimatedCostPoliciesPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingEstimatedCostPoliciesPartialUpdate({
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
    | `scope` | string (uri) |  |  |
    | `actions` | string |  |  |
    | `options` | object (free-form) |  | Fields for saving actions extra data. Keys are name of actions. |
    | `limit_cost` | integer |  |  |
    | `period` | any |  |  |
    | `organization_groups` | array of string (uri)s |  |  |
    | `apply_to_all` | boolean |  | If True, policy applies to all customers. Mutually exclusive with organization_groups. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `scope` | string (uri) |  |
    | `scope_name` | string |  |
    | `scope_uuid` | string (uuid) |  |
    | `actions` | string |  |
    | `created` | string (date-time) |  |
    | `created_by_full_name` | string |  |
    | `created_by_username` | string |  |
    | `has_fired` | boolean |  |
    | `fired_datetime` | string (date-time) |  |
    | `options` | object (free-form) | Fields for saving actions extra data. Keys are name of actions. |
    | `affected_resources_count` | integer |  |
    | `limit_cost` | integer |  |
    | `period` | any |  |
    | `period_name` | string |  |
    | `current_cost` | string (decimal) | The cost this policy compares against limit_cost right now: the period's invoice total, less the credit already applied and the credit still to be drawn, or the full cost for a policy that does not take credit into account. Do not re-derive it — only the server can simulate the pending draw, and a figure computed from the invoice alone will not match what the policy evaluates. |
    | `cost_breakdown` | any |  |
    | `eta_days` | integer | Days until the policy fires, or null when no projection exists. 0 means the threshold is already crossed and the policy is triggered — measured, not projected. Null must be rendered as no date, never as 'now': it is the common case, and it is also what an unprojectable or more-than-a-year-away policy reports. Nothing is projected beyond 365 days, because the rate comes from the current month's spend. |
    | `eta_date` | string (date) | eta_days as a calendar date, so clients do not each re-derive it. Null whenever eta_days is null; today when eta_days is 0. |
    | `trigger_status` | any |  |
    | `organization_groups` | array of string (uri)s |  |
    | `apply_to_all` | boolean | If True, policy applies to all customers. Mutually exclusive with organization_groups. |


=== "Authorization"

    The `CUSTOMER.OWNER` role on the customer.
    
    A request acting as staff always meets the permission and role requirements.

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/marketplace-offering-estimated-cost-policies/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_offering_estimated_cost_policies import marketplace_offering_estimated_cost_policies_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_offering_estimated_cost_policies_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_offering_estimated_cost_policies_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_estimated_cost_policies/marketplace_offering_estimated_cost_policies_destroy.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingEstimatedCostPoliciesDestroy } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingEstimatedCostPoliciesDestroy({
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
    


=== "Authorization"

    The `CUSTOMER.OWNER` role on the customer.
    
    A request acting as staff always meets the permission and role requirements.

---

## Other Actions


### List available actions for OfferingEstimatedCostPolicy

List available actions for OfferingEstimatedCostPolicy


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-offering-estimated-cost-policies/actions/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_offering_estimated_cost_policies import marketplace_offering_estimated_cost_policies_actions_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_offering_estimated_cost_policies_actions_retrieve.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`marketplace_offering_estimated_cost_policies_actions_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_estimated_cost_policies/marketplace_offering_estimated_cost_policies_actions_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingEstimatedCostPoliciesActionsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingEstimatedCostPoliciesActionsRetrieve({
      auth: "Token YOUR_API_TOKEN"
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Responses"

    **`200`** - 
    


=== "Authorization"

    Any signed-in user.

---

### Get object state at a specific timestamp

Returns the state of the object as it was at the specified timestamp. Only accessible by staff and support users.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-offering-estimated-cost-policies/a1b2c3d4-e5f6-7890-abcd-ef1234567890/history/at/ \
      Authorization:"Token YOUR_API_TOKEN" \
      timestamp=="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_offering_estimated_cost_policies import marketplace_offering_estimated_cost_policies_history_at_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_offering_estimated_cost_policies_history_at_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        timestamp="string-value"
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_offering_estimated_cost_policies_history_at_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_estimated_cost_policies/marketplace_offering_estimated_cost_policies_history_at_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingEstimatedCostPoliciesHistoryAtRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingEstimatedCostPoliciesHistoryAtRetrieve({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      query: {
        "timestamp": "string-value"
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

    | Name | Type | Required | Description |
    |---|---|---|---|
    | `timestamp` | string | ✓ | ISO 8601 timestamp to query the object state at |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `id` | integer | Version ID |
    | `revision_date` | string (date-time) | When this revision was created |
    | `revision_user` | object (free-form) | User who created this revision |
    | `revision_comment` | string | Comment describing the revision |
    | `serialized_data` | object (free-form) | Serialized model fields at this revision |
    
    ---
    
    **`400`** - 
    
    
    ---
    
    **`404`** - 
    


=== "Authorization"

    Staff or support only.

---

### Get version history

Returns the version history for this object. Only accessible by staff and support users.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-offering-estimated-cost-policies/a1b2c3d4-e5f6-7890-abcd-ef1234567890/history/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_offering_estimated_cost_policies import marketplace_offering_estimated_cost_policies_history_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_offering_estimated_cost_policies_history_list.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`marketplace_offering_estimated_cost_policies_history_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_estimated_cost_policies/marketplace_offering_estimated_cost_policies_history_list.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingEstimatedCostPoliciesHistoryList } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingEstimatedCostPoliciesHistoryList({
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
    | `created_after` | string | Filter versions created after this timestamp (ISO 8601) |
    | `created_before` | string | Filter versions created before this timestamp (ISO 8601) |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `scope` | string (uri) |  |
    | `scope_uuid` | string (uuid) |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `id` | integer | Version ID |
    | `revision_date` | string (date-time) | When this revision was created |
    | `revision_user` | object (free-form) | User who created this revision |
    | `revision_comment` | string | Comment describing the revision |
    | `serialized_data` | object (free-form) | Serialized model fields at this revision |


=== "Authorization"

    Staff or support only.

---
