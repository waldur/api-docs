# Marketplace Project Estimated Cost Policies

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-project-estimated-cost-policies/` | [List Marketplace Project Estimated Cost Policies](#list-marketplace-project-estimated-cost-policies) |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-project-estimated-cost-policies/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-project-estimated-cost-policies/` | [Create](#create) |
| <span class="http-badge http-put">PUT</span> | `/api/marketplace-project-estimated-cost-policies/{uuid}/` | [Update](#update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/marketplace-project-estimated-cost-policies/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-delete">DELETE</span> | `/api/marketplace-project-estimated-cost-policies/{uuid}/` | [Delete](#delete) |
| **Other Actions** | | |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-project-estimated-cost-policies/actions/` | [List Marketplace Project Estimated Cost Policies Actions](#list-marketplace-project-estimated-cost-policies-actions) |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-project-estimated-cost-policies/{uuid}/history/at/` | [Get object state at a specific timestamp](#get-object-state-at-a-specific-timestamp) |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-project-estimated-cost-policies/{uuid}/history/` | [Get version history](#get-version-history) |

---
## Core CRUD


### List Marketplace Project Estimated Cost Policies


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-project-estimated-cost-policies/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.project_estimated_cost_policy_field_enum import ProjectEstimatedCostPolicyFieldEnum # (1)
    from waldur_api_client.api.marketplace_project_estimated_cost_policies import marketplace_project_estimated_cost_policies_list # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_project_estimated_cost_policies_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`ProjectEstimatedCostPolicyFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/project_estimated_cost_policy_field_enum.py)
    2.  **API Source:** [`marketplace_project_estimated_cost_policies_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_project_estimated_cost_policies/marketplace_project_estimated_cost_policies_list.py)

=== "TypeScript"

    ```typescript
    import { marketplaceProjectEstimatedCostPoliciesList } from 'waldur-js-client';
    
    try {
      const response = await marketplaceProjectEstimatedCostPoliciesList({
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
    | `customer_uuid` | string (uuid) |  |
    | `field` | array |  |
    | `has_resource` | boolean |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `project` | string (uri) |  |
    | `project_uuid` | string (uuid) |  |
    | `query` | string |  |
    | `resource` | string (uri) |  |
    | `resource_uuid` | string (uuid) |  |
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
    | `project_credit` | string |  |
    | `customer_credit` | string |  |
    | `resource` | string (uuid) |  |
    | `resource_name` | string |  |
    | `use_credit` | boolean |  |
    | `billing_price_estimate` | any |  |


=== "Authorization"

    Any signed-in user.
    
    Returns only objects the caller holds a role on; staff and support see all.

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-project-estimated-cost-policies/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.project_estimated_cost_policy_field_enum import ProjectEstimatedCostPolicyFieldEnum # (1)
    from waldur_api_client.api.marketplace_project_estimated_cost_policies import marketplace_project_estimated_cost_policies_retrieve # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_project_estimated_cost_policies_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ProjectEstimatedCostPolicyFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/project_estimated_cost_policy_field_enum.py)
    2.  **API Source:** [`marketplace_project_estimated_cost_policies_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_project_estimated_cost_policies/marketplace_project_estimated_cost_policies_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceProjectEstimatedCostPoliciesRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceProjectEstimatedCostPoliciesRetrieve({
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
    | `project_credit` | string |  |
    | `customer_credit` | string |  |
    | `resource` | string (uuid) |  |
    | `resource_name` | string |  |
    | `use_credit` | boolean |  |
    | `billing_price_estimate` | any |  |


=== "Authorization"

    Any signed-in user.
    
    Returns only objects the caller holds a role on; staff and support see all.

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-project-estimated-cost-policies/ \
      Authorization:"Token YOUR_API_TOKEN" \
      scope="https://api.example.com/api/scope/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      actions="string-value" \
      limit_cost=123
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.project_estimated_cost_policy_request import ProjectEstimatedCostPolicyRequest # (1)
    from waldur_api_client.api.marketplace_project_estimated_cost_policies import marketplace_project_estimated_cost_policies_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ProjectEstimatedCostPolicyRequest(
        scope="https://api.example.com/api/scope/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        actions="string-value",
        limit_cost=123
    )
    response = marketplace_project_estimated_cost_policies_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ProjectEstimatedCostPolicyRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/project_estimated_cost_policy_request.py)
    2.  **API Source:** [`marketplace_project_estimated_cost_policies_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_project_estimated_cost_policies/marketplace_project_estimated_cost_policies_create.py)

=== "TypeScript"

    ```typescript
    import { marketplaceProjectEstimatedCostPoliciesCreate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceProjectEstimatedCostPoliciesCreate({
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
    | `resource` | string (uuid) |  |  |
    | `use_credit` | boolean |  |  |


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
    | `project_credit` | string |  |
    | `customer_credit` | string |  |
    | `resource` | string (uuid) |  |
    | `resource_name` | string |  |
    | `use_credit` | boolean |  |
    | `billing_price_estimate` | any |  |


=== "Authorization"

    For the `scope` named in the request, the `CUSTOMER.OWNER` role on its customer.
    
    A request acting as staff always meets the permission and role requirements.

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/marketplace-project-estimated-cost-policies/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      scope="https://api.example.com/api/scope/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      actions="string-value" \
      limit_cost=123
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.project_estimated_cost_policy_request import ProjectEstimatedCostPolicyRequest # (1)
    from waldur_api_client.api.marketplace_project_estimated_cost_policies import marketplace_project_estimated_cost_policies_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ProjectEstimatedCostPolicyRequest(
        scope="https://api.example.com/api/scope/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        actions="string-value",
        limit_cost=123
    )
    response = marketplace_project_estimated_cost_policies_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ProjectEstimatedCostPolicyRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/project_estimated_cost_policy_request.py)
    2.  **API Source:** [`marketplace_project_estimated_cost_policies_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_project_estimated_cost_policies/marketplace_project_estimated_cost_policies_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceProjectEstimatedCostPoliciesUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceProjectEstimatedCostPoliciesUpdate({
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
    | `resource` | string (uuid) |  |  |
    | `use_credit` | boolean |  |  |


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
    | `project_credit` | string |  |
    | `customer_credit` | string |  |
    | `resource` | string (uuid) |  |
    | `resource_name` | string |  |
    | `use_credit` | boolean |  |
    | `billing_price_estimate` | any |  |


=== "Authorization"

    The `CUSTOMER.OWNER` role on the customer.
    
    A request acting as staff always meets the permission and role requirements.

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/marketplace-project-estimated-cost-policies/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_project_estimated_cost_policy_request import PatchedProjectEstimatedCostPolicyRequest # (1)
    from waldur_api_client.api.marketplace_project_estimated_cost_policies import marketplace_project_estimated_cost_policies_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedProjectEstimatedCostPolicyRequest()
    response = marketplace_project_estimated_cost_policies_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedProjectEstimatedCostPolicyRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_project_estimated_cost_policy_request.py)
    2.  **API Source:** [`marketplace_project_estimated_cost_policies_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_project_estimated_cost_policies/marketplace_project_estimated_cost_policies_partial_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceProjectEstimatedCostPoliciesPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceProjectEstimatedCostPoliciesPartialUpdate({
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
    | `resource` | string (uuid) |  |  |
    | `use_credit` | boolean |  |  |


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
    | `project_credit` | string |  |
    | `customer_credit` | string |  |
    | `resource` | string (uuid) |  |
    | `resource_name` | string |  |
    | `use_credit` | boolean |  |
    | `billing_price_estimate` | any |  |


=== "Authorization"

    The `CUSTOMER.OWNER` role on the customer.
    
    A request acting as staff always meets the permission and role requirements.

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/marketplace-project-estimated-cost-policies/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_project_estimated_cost_policies import marketplace_project_estimated_cost_policies_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_project_estimated_cost_policies_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_project_estimated_cost_policies_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_project_estimated_cost_policies/marketplace_project_estimated_cost_policies_destroy.py)

=== "TypeScript"

    ```typescript
    import { marketplaceProjectEstimatedCostPoliciesDestroy } from 'waldur-js-client';
    
    try {
      const response = await marketplaceProjectEstimatedCostPoliciesDestroy({
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


### List Marketplace Project Estimated Cost Policies Actions


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-project-estimated-cost-policies/actions/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_project_estimated_cost_policies import marketplace_project_estimated_cost_policies_actions_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_project_estimated_cost_policies_actions_retrieve.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`marketplace_project_estimated_cost_policies_actions_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_project_estimated_cost_policies/marketplace_project_estimated_cost_policies_actions_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceProjectEstimatedCostPoliciesActionsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceProjectEstimatedCostPoliciesActionsRetrieve({
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
      https://api.example.com/api/marketplace-project-estimated-cost-policies/a1b2c3d4-e5f6-7890-abcd-ef1234567890/history/at/ \
      Authorization:"Token YOUR_API_TOKEN" \
      timestamp=="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_project_estimated_cost_policies import marketplace_project_estimated_cost_policies_history_at_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_project_estimated_cost_policies_history_at_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        timestamp="string-value"
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_project_estimated_cost_policies_history_at_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_project_estimated_cost_policies/marketplace_project_estimated_cost_policies_history_at_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceProjectEstimatedCostPoliciesHistoryAtRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceProjectEstimatedCostPoliciesHistoryAtRetrieve({
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
      https://api.example.com/api/marketplace-project-estimated-cost-policies/a1b2c3d4-e5f6-7890-abcd-ef1234567890/history/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_project_estimated_cost_policies import marketplace_project_estimated_cost_policies_history_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_project_estimated_cost_policies_history_list.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`marketplace_project_estimated_cost_policies_history_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_project_estimated_cost_policies/marketplace_project_estimated_cost_policies_history_list.py)

=== "TypeScript"

    ```typescript
    import { marketplaceProjectEstimatedCostPoliciesHistoryList } from 'waldur-js-client';
    
    try {
      const response = await marketplaceProjectEstimatedCostPoliciesHistoryList({
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
    | `customer` | string (uri) |  |
    | `customer_uuid` | string (uuid) |  |
    | `has_resource` | boolean |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `project` | string (uri) |  |
    | `project_uuid` | string (uuid) |  |
    | `query` | string |  |
    | `resource` | string (uri) |  |
    | `resource_uuid` | string (uuid) |  |
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
