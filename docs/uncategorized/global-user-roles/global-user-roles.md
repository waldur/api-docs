# Global User Roles

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/global-user-roles/` | [List Global User Roles](#list-global-user-roles) |
| <span class="http-badge http-get">GET</span> | `/api/global-user-roles/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/global-user-roles/` | [Grant a site-wide role](#grant-a-site-wide-role) |
| <span class="http-badge http-delete">DELETE</span> | `/api/global-user-roles/{uuid}/` | [Delete](#delete) |

---

### List Global User Roles


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/global-user-roles/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.global_user_roles import global_user_roles_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = global_user_roles_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`global_user_roles_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/global_user_roles/global_user_roles_list.py)

=== "TypeScript"

    ```typescript
    import { globalUserRolesList } from 'waldur-js-client';
    
    try {
      const response = await globalUserRolesList({
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
    | `created` | string (date-time) |  |
    | `expiration_time` | string (date-time) |  |
    | `role_name` | string |  |
    | `role_uuid` | string (uuid) |  |
    | `user_email` | string (email) |  |
    | `user_full_name` | string |  |
    | `user_username` | string | Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters |
    | `user_uuid` | string (uuid) |  |
    | `user_image` | string (uri) |  |
    | `created_by_full_name` | string |  |
    | `created_by_uuid` | string (uuid) |  |
    | `source` | string |  |


=== "Authorization"

    Staff only.

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/global-user-roles/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.global_user_roles import global_user_roles_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = global_user_roles_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`global_user_roles_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/global_user_roles/global_user_roles_retrieve.py)

=== "TypeScript"

    ```typescript
    import { globalUserRolesRetrieve } from 'waldur-js-client';
    
    try {
      const response = await globalUserRolesRetrieve({
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
    | `created` | string (date-time) |  |
    | `expiration_time` | string (date-time) |  |
    | `role_name` | string |  |
    | `role_uuid` | string (uuid) |  |
    | `user_email` | string (email) |  |
    | `user_full_name` | string |  |
    | `user_username` | string | Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters |
    | `user_uuid` | string (uuid) |  |
    | `user_image` | string (uri) |  |
    | `created_by_full_name` | string |  |
    | `created_by_uuid` | string (uuid) |  |
    | `source` | string |  |


=== "Authorization"

    Staff only.

---

### Grant a site-wide role

Staff assigns a global role to a user. The role's content type must be global. An optional expiration time can be set.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/global-user-roles/ \
      Authorization:"Token YOUR_API_TOKEN" \
      role="string-value" \
      user="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.global_user_role_create_request import GlobalUserRoleCreateRequest # (1)
    from waldur_api_client.api.global_user_roles import global_user_roles_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = GlobalUserRoleCreateRequest(
        role="string-value",
        user="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = global_user_roles_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`GlobalUserRoleCreateRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/global_user_role_create_request.py)
    2.  **API Source:** [`global_user_roles_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/global_user_roles/global_user_roles_create.py)

=== "TypeScript"

    ```typescript
    import { globalUserRolesCreate } from 'waldur-js-client';
    
    try {
      const response = await globalUserRolesCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "role": "string-value",
        "user": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `role` | string | ✓ |
    | `user` | string (uuid) | ✓ |
    | `expiration_time` | string (date-time) |  |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `expiration_time` | string (date-time) |  |
    | `role_name` | string |  |
    | `role_uuid` | string (uuid) |  |
    | `user_email` | string (email) |  |
    | `user_full_name` | string |  |
    | `user_username` | string | Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters |
    | `user_uuid` | string (uuid) |  |
    | `user_image` | string (uri) |  |
    | `created_by_full_name` | string |  |
    | `created_by_uuid` | string (uuid) |  |
    | `source` | string |  |


=== "Authorization"

    Staff only.

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/global-user-roles/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.global_user_roles import global_user_roles_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = global_user_roles_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`global_user_roles_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/global_user_roles/global_user_roles_destroy.py)

=== "TypeScript"

    ```typescript
    import { globalUserRolesDestroy } from 'waldur-js-client';
    
    try {
      const response = await globalUserRolesDestroy({
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

    Staff only.

---
