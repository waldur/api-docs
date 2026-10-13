# Marketplace Metric Retention Policies

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-metric-retention-policies/` | [List Marketplace Metric Retention Policies](#list-marketplace-metric-retention-policies) |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-metric-retention-policies/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-metric-retention-policies/` | [Create](#create) |
| <span class="http-badge http-put">PUT</span> | `/api/marketplace-metric-retention-policies/{uuid}/` | [Update](#update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/marketplace-metric-retention-policies/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-delete">DELETE</span> | `/api/marketplace-metric-retention-policies/{uuid}/` | [Delete](#delete) |

---

### List Marketplace Metric Retention Policies


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-metric-retention-policies/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_metric_retention_policies import marketplace_metric_retention_policies_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_metric_retention_policies_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`marketplace_metric_retention_policies_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_metric_retention_policies/marketplace_metric_retention_policies_list.py)

=== "TypeScript"

    ```typescript
    import { marketplaceMetricRetentionPoliciesList } from 'waldur-js-client';
    
    try {
      const response = await marketplaceMetricRetentionPoliciesList({
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
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `raw_days` | integer |  |
    | `hourly_days` | integer |  |
    | `daily_days` | integer | Empty keeps daily roll-ups forever. |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-metric-retention-policies/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_metric_retention_policies import marketplace_metric_retention_policies_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_metric_retention_policies_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_metric_retention_policies_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_metric_retention_policies/marketplace_metric_retention_policies_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceMetricRetentionPoliciesRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceMetricRetentionPoliciesRetrieve({
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
    | `name` | string |  |
    | `raw_days` | integer |  |
    | `hourly_days` | integer |  |
    | `daily_days` | integer | Empty keeps daily roll-ups forever. |

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-metric-retention-policies/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-marketplace-metric-retention-policy"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.retention_policy_request import RetentionPolicyRequest # (1)
    from waldur_api_client.api.marketplace_metric_retention_policies import marketplace_metric_retention_policies_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = RetentionPolicyRequest(
        name="my-awesome-marketplace-metric-retention-policy"
    )
    response = marketplace_metric_retention_policies_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`RetentionPolicyRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/retention_policy_request.py)
    2.  **API Source:** [`marketplace_metric_retention_policies_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_metric_retention_policies/marketplace_metric_retention_policies_create.py)

=== "TypeScript"

    ```typescript
    import { marketplaceMetricRetentionPoliciesCreate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceMetricRetentionPoliciesCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "name": "my-awesome-marketplace-metric-retention-policy"
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
    | `name` | string | ✓ |  |
    | `raw_days` | integer |  |  |
    | `hourly_days` | integer |  |  |
    | `daily_days` | integer |  | Empty keeps daily roll-ups forever. |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `raw_days` | integer |  |
    | `hourly_days` | integer |  |
    | `daily_days` | integer | Empty keeps daily roll-ups forever. |

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/marketplace-metric-retention-policies/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-marketplace-metric-retention-policy"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.retention_policy_request import RetentionPolicyRequest # (1)
    from waldur_api_client.api.marketplace_metric_retention_policies import marketplace_metric_retention_policies_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = RetentionPolicyRequest(
        name="my-awesome-marketplace-metric-retention-policy"
    )
    response = marketplace_metric_retention_policies_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`RetentionPolicyRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/retention_policy_request.py)
    2.  **API Source:** [`marketplace_metric_retention_policies_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_metric_retention_policies/marketplace_metric_retention_policies_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceMetricRetentionPoliciesUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceMetricRetentionPoliciesUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "name": "my-awesome-marketplace-metric-retention-policy"
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
    | `raw_days` | integer |  |  |
    | `hourly_days` | integer |  |  |
    | `daily_days` | integer |  | Empty keeps daily roll-ups forever. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `raw_days` | integer |  |
    | `hourly_days` | integer |  |
    | `daily_days` | integer | Empty keeps daily roll-ups forever. |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/marketplace-metric-retention-policies/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_retention_policy_request import PatchedRetentionPolicyRequest # (1)
    from waldur_api_client.api.marketplace_metric_retention_policies import marketplace_metric_retention_policies_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedRetentionPolicyRequest()
    response = marketplace_metric_retention_policies_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedRetentionPolicyRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_retention_policy_request.py)
    2.  **API Source:** [`marketplace_metric_retention_policies_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_metric_retention_policies/marketplace_metric_retention_policies_partial_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceMetricRetentionPoliciesPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceMetricRetentionPoliciesPartialUpdate({
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
    | `name` | string |  |  |
    | `raw_days` | integer |  |  |
    | `hourly_days` | integer |  |  |
    | `daily_days` | integer |  | Empty keeps daily roll-ups forever. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `raw_days` | integer |  |
    | `hourly_days` | integer |  |
    | `daily_days` | integer | Empty keeps daily roll-ups forever. |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/marketplace-metric-retention-policies/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_metric_retention_policies import marketplace_metric_retention_policies_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_metric_retention_policies_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_metric_retention_policies_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_metric_retention_policies/marketplace_metric_retention_policies_destroy.py)

=== "TypeScript"

    ```typescript
    import { marketplaceMetricRetentionPoliciesDestroy } from 'waldur-js-client';
    
    try {
      const response = await marketplaceMetricRetentionPoliciesDestroy({
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
