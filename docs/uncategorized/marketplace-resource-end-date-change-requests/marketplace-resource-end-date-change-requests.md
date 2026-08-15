# Marketplace Resource End Date Change Requests

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-resource-end-date-change-requests/` | [List Marketplace Resource End Date Change Requests](#list-marketplace-resource-end-date-change-requests) |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-resource-end-date-change-requests/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-resource-end-date-change-requests/` | [Create](#create) |
| **Other Actions** | | |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-resource-end-date-change-requests/{uuid}/approve/` | [Approve resource end date change request and apply the date to the resource](#approve-resource-end-date-change-request-and-apply-the-date-to-the-resource) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-resource-end-date-change-requests/{uuid}/cancel/` | [Cancel resource end date change request. Only the creator can cancel](#cancel-resource-end-date-change-request-only-the-creator-can-cancel) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-resource-end-date-change-requests/{uuid}/reject/` | [Reject resource end date change request](#reject-resource-end-date-change-request) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-resource-end-date-change-requests/{uuid}/set_backend_id/` | [Set end date change request backend ID](#set-end-date-change-request-backend-id) |

---
## Core CRUD


### List Marketplace Resource End Date Change Requests


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-resource-end-date-change-requests/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.remote_project_update_request_state_enum import RemoteProjectUpdateRequestStateEnum # (1)
    from waldur_api_client.api.marketplace_resource_end_date_change_requests import marketplace_resource_end_date_change_requests_list # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_resource_end_date_change_requests_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`RemoteProjectUpdateRequestStateEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/remote_project_update_request_state_enum.py)
    2.  **API Source:** [`marketplace_resource_end_date_change_requests_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_end_date_change_requests/marketplace_resource_end_date_change_requests_list.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceEndDateChangeRequestsList } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceEndDateChangeRequestsList({
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
    | `offering_uuid` | string (uuid) | Offering UUID |
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
    | `requested_end_date` | string (date) | The requested new end date for the resource |
    | `current_end_date` | string (date) |  |
    | `comment` | string | Optional comment from the requester |
    | `created` | string (date-time) |  |
    | `created_by_uuid` | string (uuid) |  |
    | `created_by_full_name` | string |  |
    | `reviewed_at` | string (date-time) | Timestamp when the review was completed |
    | `reviewed_by_uuid` | string (uuid) |  |
    | `reviewed_by_full_name` | string |  |
    | `review_comment` | string | Optional comment provided during review |
    | `backend_id` | string | Identifier of this request in an external approval system. Empty means it has not been submitted there yet. |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-resource-end-date-change-requests/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_resource_end_date_change_requests import marketplace_resource_end_date_change_requests_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_resource_end_date_change_requests_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_resource_end_date_change_requests_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_end_date_change_requests/marketplace_resource_end_date_change_requests_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceEndDateChangeRequestsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceEndDateChangeRequestsRetrieve({
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
    | `requested_end_date` | string (date) | The requested new end date for the resource |
    | `current_end_date` | string (date) |  |
    | `comment` | string | Optional comment from the requester |
    | `created` | string (date-time) |  |
    | `created_by_uuid` | string (uuid) |  |
    | `created_by_full_name` | string |  |
    | `reviewed_at` | string (date-time) | Timestamp when the review was completed |
    | `reviewed_by_uuid` | string (uuid) |  |
    | `reviewed_by_full_name` | string |  |
    | `review_comment` | string | Optional comment provided during review |
    | `backend_id` | string | Identifier of this request in an external approval system. Empty means it has not been submitted there yet. |

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-resource-end-date-change-requests/ \
      Authorization:"Token YOUR_API_TOKEN" \
      resource="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      requested_end_date="2023-10-01"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.resource_end_date_change_request_create_request import ResourceEndDateChangeRequestCreateRequest # (1)
    from waldur_api_client.api.marketplace_resource_end_date_change_requests import marketplace_resource_end_date_change_requests_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ResourceEndDateChangeRequestCreateRequest(
        resource="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        requested_end_date="2023-10-01"
    )
    response = marketplace_resource_end_date_change_requests_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ResourceEndDateChangeRequestCreateRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/resource_end_date_change_request_create_request.py)
    2.  **API Source:** [`marketplace_resource_end_date_change_requests_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_end_date_change_requests/marketplace_resource_end_date_change_requests_create.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceEndDateChangeRequestsCreate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceEndDateChangeRequestsCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "resource": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "requested_end_date": "2023-10-01"
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
    | `resource` | string (uuid) | ✓ |  |
    | `requested_end_date` | string (date) | ✓ | The requested new end date for the resource |
    | `comment` | string |  | Optional comment from the requester |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `resource` | string (uuid) |  |
    | `requested_end_date` | string (date) | The requested new end date for the resource |
    | `comment` | string | Optional comment from the requester |
    | `uuid` | string (uuid) |  |
    | `state` | string |  |

---

## Other Actions


### Approve resource end date change request and apply the date to the resource

Approve resource end date change request and apply the date to the resource.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-resource-end-date-change-requests/a1b2c3d4-e5f6-7890-abcd-ef1234567890/approve/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.review_comment_request import ReviewCommentRequest # (1)
    from waldur_api_client.api.marketplace_resource_end_date_change_requests import marketplace_resource_end_date_change_requests_approve # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ReviewCommentRequest()
    response = marketplace_resource_end_date_change_requests_approve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ReviewCommentRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/review_comment_request.py)
    2.  **API Source:** [`marketplace_resource_end_date_change_requests_approve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_end_date_change_requests/marketplace_resource_end_date_change_requests_approve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceEndDateChangeRequestsApprove } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceEndDateChangeRequestsApprove({
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

### Cancel resource end date change request. Only the creator can cancel

Cancel resource end date change request. Only the creator can cancel.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-resource-end-date-change-requests/a1b2c3d4-e5f6-7890-abcd-ef1234567890/cancel/ \
      Authorization:"Token YOUR_API_TOKEN" \
      resource="https://api.example.com/api/resource/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      requested_end_date="2023-10-01"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.resource_end_date_change_request_request import ResourceEndDateChangeRequestRequest # (1)
    from waldur_api_client.api.marketplace_resource_end_date_change_requests import marketplace_resource_end_date_change_requests_cancel # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ResourceEndDateChangeRequestRequest(
        resource="https://api.example.com/api/resource/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        requested_end_date="2023-10-01"
    )
    response = marketplace_resource_end_date_change_requests_cancel.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ResourceEndDateChangeRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/resource_end_date_change_request_request.py)
    2.  **API Source:** [`marketplace_resource_end_date_change_requests_cancel`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_end_date_change_requests/marketplace_resource_end_date_change_requests_cancel.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceEndDateChangeRequestsCancel } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceEndDateChangeRequestsCancel({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "resource": "https://api.example.com/api/resource/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "requested_end_date": "2023-10-01"
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
    | `requested_end_date` | string (date) | ✓ | The requested new end date for the resource |
    | `comment` | string |  | Optional comment from the requester |
    | `review_comment` | string |  | Optional comment provided during review |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `detail` | string |

---

### Reject resource end date change request

Reject resource end date change request.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-resource-end-date-change-requests/a1b2c3d4-e5f6-7890-abcd-ef1234567890/reject/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.review_comment_request import ReviewCommentRequest # (1)
    from waldur_api_client.api.marketplace_resource_end_date_change_requests import marketplace_resource_end_date_change_requests_reject # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ReviewCommentRequest()
    response = marketplace_resource_end_date_change_requests_reject.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ReviewCommentRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/review_comment_request.py)
    2.  **API Source:** [`marketplace_resource_end_date_change_requests_reject`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_end_date_change_requests/marketplace_resource_end_date_change_requests_reject.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceEndDateChangeRequestsReject } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceEndDateChangeRequestsReject({
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

### Set end date change request backend ID

Records the identifier this request has in an external approval system, so that system can correlate its own record with the Waldur request when reporting a verdict.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-resource-end-date-change-requests/a1b2c3d4-e5f6-7890-abcd-ef1234567890/set_backend_id/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.resource_end_date_change_request_backend_id_request import ResourceEndDateChangeRequestBackendIDRequest # (1)
    from waldur_api_client.api.marketplace_resource_end_date_change_requests import marketplace_resource_end_date_change_requests_set_backend_id # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ResourceEndDateChangeRequestBackendIDRequest()
    response = marketplace_resource_end_date_change_requests_set_backend_id.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ResourceEndDateChangeRequestBackendIDRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/resource_end_date_change_request_backend_id_request.py)
    2.  **API Source:** [`marketplace_resource_end_date_change_requests_set_backend_id`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_end_date_change_requests/marketplace_resource_end_date_change_requests_set_backend_id.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceEndDateChangeRequestsSetBackendId } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceEndDateChangeRequestsSetBackendId({
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
    | `backend_id` | string |  | Identifier of this request in an external approval system. Empty means it has not been submitted there yet. |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `status` | string |

---
