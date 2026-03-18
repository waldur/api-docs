# Project End Date Change Requests

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/project-end-date-change-requests/` | [List Project End Date Change Requests](#list-project-end-date-change-requests) |
| <span class="http-badge http-get">GET</span> | `/api/project-end-date-change-requests/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/project-end-date-change-requests/` | [Create](#create) |
| **Other Actions** | | |
| <span class="http-badge http-post">POST</span> | `/api/project-end-date-change-requests/{uuid}/approve/` | [Approve project end date change request](#approve-project-end-date-change-request) |
| <span class="http-badge http-post">POST</span> | `/api/project-end-date-change-requests/{uuid}/cancel/` | [Cancel project end date change request. Only the creator can cancel](#cancel-project-end-date-change-request-only-the-creator-can-cancel) |
| <span class="http-badge http-post">POST</span> | `/api/project-end-date-change-requests/{uuid}/reject/` | [Reject project end date change request](#reject-project-end-date-change-request) |

---
## Core CRUD


### List Project End Date Change Requests


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/project-end-date-change-requests/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.remote_project_update_request_state_enum import RemoteProjectUpdateRequestStateEnum # (1)
    from waldur_api_client.api.project_end_date_change_requests import project_end_date_change_requests_list # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = project_end_date_change_requests_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`RemoteProjectUpdateRequestStateEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/remote_project_update_request_state_enum.py)
    2.  **API Source:** [`project_end_date_change_requests_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/project_end_date_change_requests/project_end_date_change_requests_list.py)

=== "TypeScript"

    ```typescript
    import { projectEndDateChangeRequestsList } from 'waldur-js-client';
    
    try {
      const response = await projectEndDateChangeRequestsList({
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
    | `state` | array |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `state` | string |  |
    | `project` | string (uri) |  |
    | `project_uuid` | string (uuid) |  |
    | `project_name` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `requested_end_date` | string (date) | The requested new end date for the project |
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
      https://api.example.com/api/project-end-date-change-requests/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.project_end_date_change_requests import project_end_date_change_requests_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = project_end_date_change_requests_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`project_end_date_change_requests_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/project_end_date_change_requests/project_end_date_change_requests_retrieve.py)

=== "TypeScript"

    ```typescript
    import { projectEndDateChangeRequestsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await projectEndDateChangeRequestsRetrieve({
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
    | `project` | string (uri) |  |
    | `project_uuid` | string (uuid) |  |
    | `project_name` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `requested_end_date` | string (date) | The requested new end date for the project |
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
      https://api.example.com/api/project-end-date-change-requests/ \
      Authorization:"Token YOUR_API_TOKEN" \
      project="https://api.example.com/api/project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      requested_end_date="2023-10-01"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.project_end_date_change_request_create_request import ProjectEndDateChangeRequestCreateRequest # (1)
    from waldur_api_client.api.project_end_date_change_requests import project_end_date_change_requests_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ProjectEndDateChangeRequestCreateRequest(
        project="https://api.example.com/api/project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        requested_end_date="2023-10-01"
    )
    response = project_end_date_change_requests_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ProjectEndDateChangeRequestCreateRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/project_end_date_change_request_create_request.py)
    2.  **API Source:** [`project_end_date_change_requests_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/project_end_date_change_requests/project_end_date_change_requests_create.py)

=== "TypeScript"

    ```typescript
    import { projectEndDateChangeRequestsCreate } from 'waldur-js-client';
    
    try {
      const response = await projectEndDateChangeRequestsCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "project": "https://api.example.com/api/project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
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
    | `project` | string (uri) | ✓ |  |
    | `requested_end_date` | string (date) | ✓ | The requested new end date for the project |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `project` | string (uri) |  |
    | `requested_end_date` | string (date) | The requested new end date for the project |
    | `uuid` | string (uuid) |  |
    | `state` | string |  |

---

## Other Actions


### Approve project end date change request

Approve project end date change request


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/project-end-date-change-requests/a1b2c3d4-e5f6-7890-abcd-ef1234567890/approve/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.review_comment_request import ReviewCommentRequest # (1)
    from waldur_api_client.api.project_end_date_change_requests import project_end_date_change_requests_approve # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ReviewCommentRequest()
    response = project_end_date_change_requests_approve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ReviewCommentRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/review_comment_request.py)
    2.  **API Source:** [`project_end_date_change_requests_approve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/project_end_date_change_requests/project_end_date_change_requests_approve.py)

=== "TypeScript"

    ```typescript
    import { projectEndDateChangeRequestsApprove } from 'waldur-js-client';
    
    try {
      const response = await projectEndDateChangeRequestsApprove({
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

### Cancel project end date change request. Only the creator can cancel

Cancel project end date change request. Only the creator can cancel.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/project-end-date-change-requests/a1b2c3d4-e5f6-7890-abcd-ef1234567890/cancel/ \
      Authorization:"Token YOUR_API_TOKEN" \
      project="https://api.example.com/api/project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      requested_end_date="2023-10-01"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.project_end_date_change_request_request import ProjectEndDateChangeRequestRequest # (1)
    from waldur_api_client.api.project_end_date_change_requests import project_end_date_change_requests_cancel # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ProjectEndDateChangeRequestRequest(
        project="https://api.example.com/api/project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        requested_end_date="2023-10-01"
    )
    response = project_end_date_change_requests_cancel.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ProjectEndDateChangeRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/project_end_date_change_request_request.py)
    2.  **API Source:** [`project_end_date_change_requests_cancel`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/project_end_date_change_requests/project_end_date_change_requests_cancel.py)

=== "TypeScript"

    ```typescript
    import { projectEndDateChangeRequestsCancel } from 'waldur-js-client';
    
    try {
      const response = await projectEndDateChangeRequestsCancel({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "project": "https://api.example.com/api/project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
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
    | `project` | string (uri) | ✓ |  |
    | `requested_end_date` | string (date) | ✓ | The requested new end date for the project |
    | `review_comment` | string |  | Optional comment provided during review |


=== "Responses"

    **`200`** - No response body
    

---

### Reject project end date change request

Reject project end date change request


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/project-end-date-change-requests/a1b2c3d4-e5f6-7890-abcd-ef1234567890/reject/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.review_comment_request import ReviewCommentRequest # (1)
    from waldur_api_client.api.project_end_date_change_requests import project_end_date_change_requests_reject # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ReviewCommentRequest()
    response = project_end_date_change_requests_reject.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ReviewCommentRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/review_comment_request.py)
    2.  **API Source:** [`project_end_date_change_requests_reject`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/project_end_date_change_requests/project_end_date_change_requests_reject.py)

=== "TypeScript"

    ```typescript
    import { projectEndDateChangeRequestsReject } from 'waldur-js-client';
    
    try {
      const response = await projectEndDateChangeRequestsReject({
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
