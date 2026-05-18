# Marketplace Resource Limit Change Requests

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-resource-limit-change-requests/` | [List Marketplace Resource Limit Change Requests](#list-marketplace-resource-limit-change-requests) |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-resource-limit-change-requests/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-resource-limit-change-requests/` | [Create](#create) |
| **Other Actions** | | |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-resource-limit-change-requests/{uuid}/approve/` | [Approve resource limit change request and apply limits via marketplace order](#approve-resource-limit-change-request-and-apply-limits-via-marketplace-order) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-resource-limit-change-requests/{uuid}/cancel/` | [Cancel resource limit change request. Only the creator can cancel](#cancel-resource-limit-change-request-only-the-creator-can-cancel) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-resource-limit-change-requests/{uuid}/reject/` | [Reject resource limit change request](#reject-resource-limit-change-request) |

---
## Core CRUD


### List Marketplace Resource Limit Change Requests


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-resource-limit-change-requests/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.remote_project_update_request_state_enum import RemoteProjectUpdateRequestStateEnum # (1)
    from waldur_api_client.api.marketplace_resource_limit_change_requests import marketplace_resource_limit_change_requests_list # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_resource_limit_change_requests_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`RemoteProjectUpdateRequestStateEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/remote_project_update_request_state_enum.py)
    2.  **API Source:** [`marketplace_resource_limit_change_requests_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_limit_change_requests/marketplace_resource_limit_change_requests_list.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceLimitChangeRequestsList } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceLimitChangeRequestsList({
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
    | `created_by_uuid` | string (uuid) | Created by UUID |
    | `customer_uuid` | string (uuid) | Customer UUID |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `project_uuid` | string (uuid) | Project UUID |
    | `resource_uuid` | string (uuid) | Resource UUID |
    | `state` | array |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `state` | string |  |
    | `resource` | string (uri) |  |
    | `resource_uuid` | string (uuid) |  |
    | `resource_name` | string |  |
    | `project_uuid` | string (uuid) |  |
    | `project_name` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `offering_uuid` | string (uuid) |  |
    | `offering_name` | string |  |
    | `requested_limits` | any |  |
    | `current_limits` | object (free-form) |  |
    | `created` | string (date-time) |  |
    | `created_by_uuid` | string (uuid) |  |
    | `created_by_full_name` | string |  |
    | `reviewed_at` | string (date-time) | Timestamp when the review was completed |
    | `reviewed_by_uuid` | string (uuid) |  |
    | `reviewed_by_full_name` | string |  |
    | `review_comment` | string | Optional comment provided during review |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-resource-limit-change-requests/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_resource_limit_change_requests import marketplace_resource_limit_change_requests_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_resource_limit_change_requests_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_resource_limit_change_requests_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_limit_change_requests/marketplace_resource_limit_change_requests_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceLimitChangeRequestsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceLimitChangeRequestsRetrieve({
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
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `state` | string |  |
    | `resource` | string (uri) |  |
    | `resource_uuid` | string (uuid) |  |
    | `resource_name` | string |  |
    | `project_uuid` | string (uuid) |  |
    | `project_name` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `offering_uuid` | string (uuid) |  |
    | `offering_name` | string |  |
    | `requested_limits` | any |  |
    | `current_limits` | object (free-form) |  |
    | `created` | string (date-time) |  |
    | `created_by_uuid` | string (uuid) |  |
    | `created_by_full_name` | string |  |
    | `reviewed_at` | string (date-time) | Timestamp when the review was completed |
    | `reviewed_by_uuid` | string (uuid) |  |
    | `reviewed_by_full_name` | string |  |
    | `review_comment` | string | Optional comment provided during review |

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-resource-limit-change-requests/ \
      Authorization:"Token YOUR_API_TOKEN" \
      resource="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      requested_limits=null
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.resource_limit_change_request_create_request import ResourceLimitChangeRequestCreateRequest # (1)
    from waldur_api_client.api.marketplace_resource_limit_change_requests import marketplace_resource_limit_change_requests_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ResourceLimitChangeRequestCreateRequest(
        resource="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        requested_limits=null
    )
    response = marketplace_resource_limit_change_requests_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ResourceLimitChangeRequestCreateRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/resource_limit_change_request_create_request.py)
    2.  **API Source:** [`marketplace_resource_limit_change_requests_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_limit_change_requests/marketplace_resource_limit_change_requests_create.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceLimitChangeRequestsCreate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceLimitChangeRequestsCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "resource": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "requested_limits": null
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
    | `resource` | string (uuid) | ✓ |
    | `requested_limits` | any | ✓ |


=== "Responses"

    **`201`** - 
    
    | Field | Type |
    |---|---|
    | `resource` | string (uuid) |
    | `requested_limits` | any |
    | `uuid` | string (uuid) |
    | `state` | string |

---

## Other Actions


### Approve resource limit change request and apply limits via marketplace order

Approve resource limit change request and apply limits via marketplace order.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-resource-limit-change-requests/a1b2c3d4-e5f6-7890-abcd-ef1234567890/approve/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.review_comment_request import ReviewCommentRequest # (1)
    from waldur_api_client.api.marketplace_resource_limit_change_requests import marketplace_resource_limit_change_requests_approve # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ReviewCommentRequest()
    response = marketplace_resource_limit_change_requests_approve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ReviewCommentRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/review_comment_request.py)
    2.  **API Source:** [`marketplace_resource_limit_change_requests_approve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_limit_change_requests/marketplace_resource_limit_change_requests_approve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceLimitChangeRequestsApprove } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceLimitChangeRequestsApprove({
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
    | `comment` | string |  | Optional comment for review |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `order_uuid` | string (uuid) | UUID of the created or updated order |

---

### Cancel resource limit change request. Only the creator can cancel

Cancel resource limit change request. Only the creator can cancel.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-resource-limit-change-requests/a1b2c3d4-e5f6-7890-abcd-ef1234567890/cancel/ \
      Authorization:"Token YOUR_API_TOKEN" \
      resource="https://api.example.com/api/resource/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      requested_limits=null
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.resource_limit_change_request_request import ResourceLimitChangeRequestRequest # (1)
    from waldur_api_client.api.marketplace_resource_limit_change_requests import marketplace_resource_limit_change_requests_cancel # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ResourceLimitChangeRequestRequest(
        resource="https://api.example.com/api/resource/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        requested_limits=null
    )
    response = marketplace_resource_limit_change_requests_cancel.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ResourceLimitChangeRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/resource_limit_change_request_request.py)
    2.  **API Source:** [`marketplace_resource_limit_change_requests_cancel`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_limit_change_requests/marketplace_resource_limit_change_requests_cancel.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceLimitChangeRequestsCancel } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceLimitChangeRequestsCancel({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "resource": "https://api.example.com/api/resource/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "requested_limits": null
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
    | `resource` | string (uri) | ✓ |  |
    | `requested_limits` | any | ✓ |  |
    | `review_comment` | string |  | Optional comment provided during review |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `detail` | string |

---

### Reject resource limit change request

Reject resource limit change request.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-resource-limit-change-requests/a1b2c3d4-e5f6-7890-abcd-ef1234567890/reject/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.review_comment_request import ReviewCommentRequest # (1)
    from waldur_api_client.api.marketplace_resource_limit_change_requests import marketplace_resource_limit_change_requests_reject # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ReviewCommentRequest()
    response = marketplace_resource_limit_change_requests_reject.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ReviewCommentRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/review_comment_request.py)
    2.  **API Source:** [`marketplace_resource_limit_change_requests_reject`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_limit_change_requests/marketplace_resource_limit_change_requests_reject.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceLimitChangeRequestsReject } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceLimitChangeRequestsReject({
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
    | `comment` | string |  | Optional comment for review |


=== "Responses"

    **`200`** - No response body
    

---
