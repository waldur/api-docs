# User Permissions

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/user-permissions/` | [List user permissions](#list-user-permissions) |
| <span class="http-badge http-get">GET</span> | `/api/user-permissions/{uuid}/` | [Get permission details](#get-permission-details) |
| **Other Actions** | | |
| <span class="http-badge http-post">POST</span> | `/api/user-permissions/{uuid}/restore/` | [Restore a revoked user role](#restore-a-revoked-user-role) |
| <span class="http-badge http-post">POST</span> | `/api/user-permissions/{uuid}/revoke/` | [Revoke a user role](#revoke-a-user-role) |

---
## Core CRUD


### List user permissions

Get a list of all permissions for the current user. Staff and support users can view all user permissions. The list can be filtered by user, scope, role, etc. By default only active grants are returned; staff and support can pass show_inactive=true to include revoked grants (the full history).


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/user-permissions/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.offering_permission_o_enum import OfferingPermissionOEnum # (1)
    from waldur_api_client.api.user_permissions import user_permissions_list # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = user_permissions_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`OfferingPermissionOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/offering_permission_o_enum.py)
    2.  **API Source:** [`user_permissions_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/user_permissions/user_permissions_list.py)

=== "TypeScript"

    ```typescript
    import { userPermissionsList } from 'waldur-js-client';
    
    try {
      const response = await userPermissionsList({
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
    | `created` | string (date-time) | Created after |
    | `created_before` | string (date-time) | Created before |
    | `expiration_time` | string (date-time) |  |
    | `full_name` | string | User full name contains |
    | `is_active` | boolean |  |
    | `modified` | string (date-time) | Modified after |
    | `modified_before` | string (date-time) | Modified before |
    | `native_name` | string |  |
    | `o` | array | Ordering<br><br> |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `role_name` | string | Role name contains |
    | `role_uuid` | string (uuid) | Role UUID |
    | `scope_name` | string | Scope name |
    | `scope_type` | string | Scope type |
    | `scope_uuid` | string | Scope UUID |
    | `show_inactive` | boolean | Staff/support only. Include revoked (inactive) role grants in addition to active ones. Ignored for other users, who only ever see their own active roles. |
    | `user` | string (uuid) |  |
    | `user_slug` | string | User slug contains |
    | `user_url` | string (uri) |  |
    | `username` | string |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `user_uuid` | string (uuid) |
    | `user_name` | string |
    | `user_slug` | string |
    | `created` | string (date-time) |
    | `expiration_time` | string (date-time) |
    | `is_active` | boolean |
    | `created_by_full_name` | string |
    | `created_by_username` | string |
    | `revoked_by_full_name` | string |
    | `revoked_by_username` | string |
    | `revoke_reason` | string |
    | `role_name` | string |
    | `role_description` | string |
    | `role_uuid` | string (uuid) |
    | `scope_type` | string |
    | `scope_uuid` | string (uuid) |
    | `scope_name` | string |
    | `scope_is_removed` | boolean |
    | `customer_uuid` | string (uuid) |
    | `customer_name` | string |
    | `resource_uuid` | string (uuid) |
    | `project_uuid` | string (uuid) |

---

### Get permission details

Retrieve the details of a specific user permission grant by its UUID.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/user-permissions/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.user_permissions import user_permissions_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = user_permissions_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`user_permissions_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/user_permissions/user_permissions_retrieve.py)

=== "TypeScript"

    ```typescript
    import { userPermissionsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await userPermissionsRetrieve({
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
    | `uuid` | string (uuid) |
    | `user_uuid` | string (uuid) |
    | `user_name` | string |
    | `user_slug` | string |
    | `created` | string (date-time) |
    | `expiration_time` | string (date-time) |
    | `is_active` | boolean |
    | `created_by_full_name` | string |
    | `created_by_username` | string |
    | `revoked_by_full_name` | string |
    | `revoked_by_username` | string |
    | `revoke_reason` | string |
    | `role_name` | string |
    | `role_description` | string |
    | `role_uuid` | string (uuid) |
    | `scope_type` | string |
    | `scope_uuid` | string (uuid) |
    | `scope_name` | string |
    | `scope_is_removed` | boolean |
    | `customer_uuid` | string (uuid) |
    | `customer_name` | string |
    | `resource_uuid` | string (uuid) |
    | `project_uuid` | string (uuid) |

---

## Other Actions


### Restore a revoked user role

Restores a previously revoked user role grant, reinstating the associated permissions immediately. Restoring a role whose scope (e.g. a project) has been soft-deleted is not allowed.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/user-permissions/a1b2c3d4-e5f6-7890-abcd-ef1234567890/restore/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.user_role_permission_action_request import UserRolePermissionActionRequest # (1)
    from waldur_api_client.api.user_permissions import user_permissions_restore # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = UserRolePermissionActionRequest()
    response = user_permissions_restore.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`UserRolePermissionActionRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/user_role_permission_action_request.py)
    2.  **API Source:** [`user_permissions_restore`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/user_permissions/user_permissions_restore.py)

=== "TypeScript"

    ```typescript
    import { userPermissionsRestore } from 'waldur-js-client';
    
    try {
      const response = await userPermissionsRestore({
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
    | `reason` | string |  |


=== "Responses"

    **`200`** - Role restored successfully.
    

---

### Revoke a user role

Revokes a specific user role grant, deactivating the associated permissions immediately.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/user-permissions/a1b2c3d4-e5f6-7890-abcd-ef1234567890/revoke/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.user_role_permission_action_request import UserRolePermissionActionRequest # (1)
    from waldur_api_client.api.user_permissions import user_permissions_revoke # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = UserRolePermissionActionRequest()
    response = user_permissions_revoke.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`UserRolePermissionActionRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/user_role_permission_action_request.py)
    2.  **API Source:** [`user_permissions_revoke`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/user_permissions/user_permissions_revoke.py)

=== "TypeScript"

    ```typescript
    import { userPermissionsRevoke } from 'waldur-js-client';
    
    try {
      const response = await userPermissionsRevoke({
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
    | `reason` | string |  |


=== "Responses"

    **`200`** - Role revoked successfully.
    

---
