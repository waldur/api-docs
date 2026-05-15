# Marketplace Project Order Auto Approvals

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-project-order-auto-approvals/` | [List Marketplace Project Order Auto Approvals](#list-marketplace-project-order-auto-approvals) |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-project-order-auto-approvals/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-project-order-auto-approvals/` | [Create](#create) |
| <span class="http-badge http-put">PUT</span> | `/api/marketplace-project-order-auto-approvals/{uuid}/` | [Update](#update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/marketplace-project-order-auto-approvals/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-delete">DELETE</span> | `/api/marketplace-project-order-auto-approvals/{uuid}/` | [Delete](#delete) |

---

### List Marketplace Project Order Auto Approvals


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-project-order-auto-approvals/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_project_order_auto_approvals import marketplace_project_order_auto_approvals_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_project_order_auto_approvals_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`marketplace_project_order_auto_approvals_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_project_order_auto_approvals/marketplace_project_order_auto_approvals_list.py)

=== "TypeScript"

    ```typescript
    import { marketplaceProjectOrderAutoApprovalsList } from 'waldur-js-client';
    
    try {
      const response = await marketplaceProjectOrderAutoApprovalsList({
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
    | `customer_uuid` | string (uuid) | Customer UUID |
    | `enabled` | boolean |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `project_uuid` | string (uuid) | Project UUID |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `project` | string (uri) |  |
    | `project_name` | string |  |
    | `project_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `monthly_cost_limit` | string (decimal) |  |
    | `enabled` | boolean |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `created_by_uuid` | string (uuid) |  |
    | `created_by_username` | string | Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters |
    | `created_by_full_name` | string |  |
    | `modified_by_uuid` | string (uuid) |  |
    | `modified_by_username` | string | Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters |
    | `modified_by_full_name` | string |  |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-project-order-auto-approvals/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_project_order_auto_approvals import marketplace_project_order_auto_approvals_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_project_order_auto_approvals_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_project_order_auto_approvals_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_project_order_auto_approvals/marketplace_project_order_auto_approvals_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceProjectOrderAutoApprovalsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceProjectOrderAutoApprovalsRetrieve({
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
    | `url` | string (uri) |  |
    | `project` | string (uri) |  |
    | `project_name` | string |  |
    | `project_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `monthly_cost_limit` | string (decimal) |  |
    | `enabled` | boolean |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `created_by_uuid` | string (uuid) |  |
    | `created_by_username` | string | Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters |
    | `created_by_full_name` | string |  |
    | `modified_by_uuid` | string (uuid) |  |
    | `modified_by_username` | string | Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters |
    | `modified_by_full_name` | string |  |

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-project-order-auto-approvals/ \
      Authorization:"Token YOUR_API_TOKEN" \
      project="https://api.example.com/api/project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      monthly_cost_limit="12.34"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.project_order_auto_approval_request import ProjectOrderAutoApprovalRequest # (1)
    from waldur_api_client.api.marketplace_project_order_auto_approvals import marketplace_project_order_auto_approvals_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ProjectOrderAutoApprovalRequest(
        project="https://api.example.com/api/project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        monthly_cost_limit="12.34"
    )
    response = marketplace_project_order_auto_approvals_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ProjectOrderAutoApprovalRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/project_order_auto_approval_request.py)
    2.  **API Source:** [`marketplace_project_order_auto_approvals_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_project_order_auto_approvals/marketplace_project_order_auto_approvals_create.py)

=== "TypeScript"

    ```typescript
    import { marketplaceProjectOrderAutoApprovalsCreate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceProjectOrderAutoApprovalsCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "project": "https://api.example.com/api/project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "monthly_cost_limit": "12.34"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Request Body (required)"

    | Field | Type | Required |
    |---|---|---|
    | `project` | string (uri) | ✓ |
    | `monthly_cost_limit` | string (decimal) | ✓ |
    | `enabled` | boolean |  |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `project` | string (uri) |  |
    | `project_name` | string |  |
    | `project_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `monthly_cost_limit` | string (decimal) |  |
    | `enabled` | boolean |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `created_by_uuid` | string (uuid) |  |
    | `created_by_username` | string | Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters |
    | `created_by_full_name` | string |  |
    | `modified_by_uuid` | string (uuid) |  |
    | `modified_by_username` | string | Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters |
    | `modified_by_full_name` | string |  |

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/marketplace-project-order-auto-approvals/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      project="https://api.example.com/api/project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      monthly_cost_limit="12.34"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.project_order_auto_approval_request import ProjectOrderAutoApprovalRequest # (1)
    from waldur_api_client.api.marketplace_project_order_auto_approvals import marketplace_project_order_auto_approvals_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ProjectOrderAutoApprovalRequest(
        project="https://api.example.com/api/project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        monthly_cost_limit="12.34"
    )
    response = marketplace_project_order_auto_approvals_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ProjectOrderAutoApprovalRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/project_order_auto_approval_request.py)
    2.  **API Source:** [`marketplace_project_order_auto_approvals_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_project_order_auto_approvals/marketplace_project_order_auto_approvals_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceProjectOrderAutoApprovalsUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceProjectOrderAutoApprovalsUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "project": "https://api.example.com/api/project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "monthly_cost_limit": "12.34"
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
    | `project` | string (uri) | ✓ |
    | `monthly_cost_limit` | string (decimal) | ✓ |
    | `enabled` | boolean |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `project` | string (uri) |  |
    | `project_name` | string |  |
    | `project_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `monthly_cost_limit` | string (decimal) |  |
    | `enabled` | boolean |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `created_by_uuid` | string (uuid) |  |
    | `created_by_username` | string | Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters |
    | `created_by_full_name` | string |  |
    | `modified_by_uuid` | string (uuid) |  |
    | `modified_by_username` | string | Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters |
    | `modified_by_full_name` | string |  |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/marketplace-project-order-auto-approvals/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_project_order_auto_approval_request import PatchedProjectOrderAutoApprovalRequest # (1)
    from waldur_api_client.api.marketplace_project_order_auto_approvals import marketplace_project_order_auto_approvals_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedProjectOrderAutoApprovalRequest()
    response = marketplace_project_order_auto_approvals_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedProjectOrderAutoApprovalRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_project_order_auto_approval_request.py)
    2.  **API Source:** [`marketplace_project_order_auto_approvals_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_project_order_auto_approvals/marketplace_project_order_auto_approvals_partial_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceProjectOrderAutoApprovalsPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceProjectOrderAutoApprovalsPartialUpdate({
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
    | `project` | string (uri) |  |
    | `monthly_cost_limit` | string (decimal) |  |
    | `enabled` | boolean |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `project` | string (uri) |  |
    | `project_name` | string |  |
    | `project_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `monthly_cost_limit` | string (decimal) |  |
    | `enabled` | boolean |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `created_by_uuid` | string (uuid) |  |
    | `created_by_username` | string | Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters |
    | `created_by_full_name` | string |  |
    | `modified_by_uuid` | string (uuid) |  |
    | `modified_by_username` | string | Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters |
    | `modified_by_full_name` | string |  |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/marketplace-project-order-auto-approvals/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_project_order_auto_approvals import marketplace_project_order_auto_approvals_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_project_order_auto_approvals_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_project_order_auto_approvals_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_project_order_auto_approvals/marketplace_project_order_auto_approvals_destroy.py)

=== "TypeScript"

    ```typescript
    import { marketplaceProjectOrderAutoApprovalsDestroy } from 'waldur-js-client';
    
    try {
      const response = await marketplaceProjectOrderAutoApprovalsDestroy({
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
