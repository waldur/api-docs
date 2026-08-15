# Support Users

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/support-users/` | [List Support Users](#list-support-users) |
| <span class="http-badge http-get">GET</span> | `/api/support-users/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/support-users/` | [Create](#create) |
| <span class="http-badge http-put">PUT</span> | `/api/support-users/{uuid}/` | [Update](#update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/support-users/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-delete">DELETE</span> | `/api/support-users/{uuid}/` | [Delete](#delete) |
| **Other Actions** | | |
| <span class="http-badge http-get">GET</span> | `/api/support-users/{uuid}/connections/` | [Connections](#connections) |
| <span class="http-badge http-post">POST</span> | `/api/support-users/{uuid}/merge/` | [Merge](#merge) |

---
## Core CRUD


### List Support Users


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/support-users/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.support_user_o_enum import SupportUserOEnum # (1)
    from waldur_api_client.models.waldursupportactivebackendtype_enum import WALDURSUPPORTACTIVEBACKENDTYPEEnum # (2)
    from waldur_api_client.api.support_users import support_users_list # (3)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = support_users_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`SupportUserOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/support_user_o_enum.py)
    2.  **Model Source:** [`WALDURSUPPORTACTIVEBACKENDTYPEEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/waldursupportactivebackendtype_enum.py)
    3.  **API Source:** [`support_users_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_users/support_users_list.py)

=== "TypeScript"

    ```typescript
    import { supportUsersList } from 'waldur-js-client';
    
    try {
      const response = await supportUsersList({
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
    | `backend_id` | string |  |
    | `backend_name` | string | Helpdesk<br><br><br>_Enum: `basic`, `atlassian`, `zammad`, `smax`_ |
    | `is_active` | boolean |  |
    | `name` | string |  |
    | `o` | array | Ordering<br><br> |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `query` | string | Search by name, backend ID or linked user name/email |
    | `user` | integer |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `backend_id` | string |  |
    | `backend_name` | string |  |
    | `is_active` | boolean | Designates whether this user should be treated as active. Unselect this instead of deleting accounts. |
    | `user` | string (uri) |  |
    | `user_full_name` | string |  |
    | `user_email` | string |  |
    | `reported_issues_count` | integer |  |
    | `assigned_issues_count` | integer |  |
    | `comments_count` | integer |  |
    | `attachments_count` | integer |  |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/support-users/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.support_users import support_users_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = support_users_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`support_users_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_users/support_users_retrieve.py)

=== "TypeScript"

    ```typescript
    import { supportUsersRetrieve } from 'waldur-js-client';
    
    try {
      const response = await supportUsersRetrieve({
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
    | `name` | string |  |
    | `backend_id` | string |  |
    | `backend_name` | string |  |
    | `is_active` | boolean | Designates whether this user should be treated as active. Unselect this instead of deleting accounts. |
    | `user` | string (uri) |  |
    | `user_full_name` | string |  |
    | `user_email` | string |  |
    | `reported_issues_count` | integer |  |
    | `assigned_issues_count` | integer |  |
    | `comments_count` | integer |  |
    | `attachments_count` | integer |  |

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/support-users/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-support-user"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.support_user_request import SupportUserRequest # (1)
    from waldur_api_client.api.support_users import support_users_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = SupportUserRequest(
        name="my-awesome-support-user"
    )
    response = support_users_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`SupportUserRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/support_user_request.py)
    2.  **API Source:** [`support_users_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_users/support_users_create.py)

=== "TypeScript"

    ```typescript
    import { supportUsersCreate } from 'waldur-js-client';
    
    try {
      const response = await supportUsersCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "name": "my-awesome-support-user"
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
    | `backend_id` | string |  |  |
    | `backend_name` | string |  |  |
    | `is_active` | boolean |  | Designates whether this user should be treated as active. Unselect this instead of deleting accounts. |
    | `user` | string (uri) |  |  |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `backend_id` | string |  |
    | `backend_name` | string |  |
    | `is_active` | boolean | Designates whether this user should be treated as active. Unselect this instead of deleting accounts. |
    | `user` | string (uri) |  |
    | `user_full_name` | string |  |
    | `user_email` | string |  |
    | `reported_issues_count` | integer |  |
    | `assigned_issues_count` | integer |  |
    | `comments_count` | integer |  |
    | `attachments_count` | integer |  |

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/support-users/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-support-user"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.support_user_request import SupportUserRequest # (1)
    from waldur_api_client.api.support_users import support_users_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = SupportUserRequest(
        name="my-awesome-support-user"
    )
    response = support_users_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`SupportUserRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/support_user_request.py)
    2.  **API Source:** [`support_users_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_users/support_users_update.py)

=== "TypeScript"

    ```typescript
    import { supportUsersUpdate } from 'waldur-js-client';
    
    try {
      const response = await supportUsersUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "name": "my-awesome-support-user"
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
    | `backend_id` | string |  |  |
    | `backend_name` | string |  |  |
    | `is_active` | boolean |  | Designates whether this user should be treated as active. Unselect this instead of deleting accounts. |
    | `user` | string (uri) |  |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `backend_id` | string |  |
    | `backend_name` | string |  |
    | `is_active` | boolean | Designates whether this user should be treated as active. Unselect this instead of deleting accounts. |
    | `user` | string (uri) |  |
    | `user_full_name` | string |  |
    | `user_email` | string |  |
    | `reported_issues_count` | integer |  |
    | `assigned_issues_count` | integer |  |
    | `comments_count` | integer |  |
    | `attachments_count` | integer |  |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/support-users/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_support_user_request import PatchedSupportUserRequest # (1)
    from waldur_api_client.api.support_users import support_users_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedSupportUserRequest()
    response = support_users_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedSupportUserRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_support_user_request.py)
    2.  **API Source:** [`support_users_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_users/support_users_partial_update.py)

=== "TypeScript"

    ```typescript
    import { supportUsersPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await supportUsersPartialUpdate({
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
    | `backend_id` | string |  |  |
    | `backend_name` | string |  |  |
    | `is_active` | boolean |  | Designates whether this user should be treated as active. Unselect this instead of deleting accounts. |
    | `user` | string (uri) |  |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `backend_id` | string |  |
    | `backend_name` | string |  |
    | `is_active` | boolean | Designates whether this user should be treated as active. Unselect this instead of deleting accounts. |
    | `user` | string (uri) |  |
    | `user_full_name` | string |  |
    | `user_email` | string |  |
    | `reported_issues_count` | integer |  |
    | `assigned_issues_count` | integer |  |
    | `comments_count` | integer |  |
    | `attachments_count` | integer |  |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/support-users/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.support_users import support_users_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = support_users_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`support_users_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_users/support_users_destroy.py)

=== "TypeScript"

    ```typescript
    import { supportUsersDestroy } from 'waldur-js-client';
    
    try {
      const response = await supportUsersDestroy({
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

## Other Actions


### Connections


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/support-users/a1b2c3d4-e5f6-7890-abcd-ef1234567890/connections/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.support_users import support_users_connections_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = support_users_connections_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`support_users_connections_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_users/support_users_connections_retrieve.py)

=== "TypeScript"

    ```typescript
    import { supportUsersConnectionsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await supportUsersConnectionsRetrieve({
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
    | `reported_issues` | array of objects |
    | `reported_issues.uuid` | string (uuid) |
    | `reported_issues.key` | string |
    | `reported_issues.type` | string |
    | `reported_issues.summary` | string |
    | `reported_issues.status` | string |
    | `reported_issues.created` | string (date-time) |
    | `reported_issues.modified` | string (date-time) |
    | `assigned_issues` | array of objects |
    | `assigned_issues.uuid` | string (uuid) |
    | `assigned_issues.key` | string |
    | `assigned_issues.type` | string |
    | `assigned_issues.summary` | string |
    | `assigned_issues.status` | string |
    | `assigned_issues.created` | string (date-time) |
    | `assigned_issues.modified` | string (date-time) |
    | `comments` | array of objects |
    | `comments.uuid` | string (uuid) |
    | `comments.description` | string |
    | `comments.is_public` | boolean |
    | `comments.created` | string (date-time) |
    | `comments.issue_key` | string |
    | `comments.issue_uuid` | string (uuid) |
    | `attachments` | array of objects |
    | `attachments.uuid` | string (uuid) |
    | `attachments.file_name` | string |
    | `attachments.created` | string (date-time) |
    | `attachments.issue_key` | string |
    | `attachments.issue_uuid` | string (uuid) |

---

### Merge


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/support-users/a1b2c3d4-e5f6-7890-abcd-ef1234567890/merge/ \
      Authorization:"Token YOUR_API_TOKEN" \
      source_users:='[]'
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.support_user_merge_request import SupportUserMergeRequest # (1)
    from waldur_api_client.api.support_users import support_users_merge # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = SupportUserMergeRequest(
        source_users=[]
    )
    response = support_users_merge.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`SupportUserMergeRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/support_user_merge_request.py)
    2.  **API Source:** [`support_users_merge`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_users/support_users_merge.py)

=== "TypeScript"

    ```typescript
    import { supportUsersMerge } from 'waldur-js-client';
    
    try {
      const response = await supportUsersMerge({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "source_users": []
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
    | `source_users` | array of string (uuid)s | ✓ | Support users to merge into this one. They will be deleted and their issues, comments and attachments re-pointed to this user. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `backend_id` | string |  |
    | `backend_name` | string |  |
    | `is_active` | boolean | Designates whether this user should be treated as active. Unselect this instead of deleting accounts. |
    | `user` | string (uri) |  |
    | `user_full_name` | string |  |
    | `user_email` | string |  |
    | `reported_issues_count` | integer |  |
    | `assigned_issues_count` | integer |  |
    | `comments_count` | integer |  |
    | `attachments_count` | integer |  |

---
