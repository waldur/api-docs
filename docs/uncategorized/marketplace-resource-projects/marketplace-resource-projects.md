# Marketplace Resource Projects

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-resource-projects/` | [List Marketplace Resource Projects](#list-marketplace-resource-projects) |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-resource-projects/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-resource-projects/` | [Create](#create) |
| <span class="http-badge http-put">PUT</span> | `/api/marketplace-resource-projects/{uuid}/` | [Update](#update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/marketplace-resource-projects/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-delete">DELETE</span> | `/api/marketplace-resource-projects/{uuid}/` | [Delete](#delete) |
| **Permissions & Users** | | |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-resource-projects/{uuid}/list_users/` | [List users and their roles in a scope](#list-users-and-their-roles-in-a-scope) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-resource-projects/{uuid}/add_user/` | [Grant a role to a user](#grant-a-role-to-a-user) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-resource-projects/{uuid}/delete_user/` | [Revoke a role from a user](#revoke-a-role-from-a-user) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-resource-projects/{uuid}/update_user/` | [Update a user's role expiration](#update-a-users-role-expiration) |

---
## Core CRUD


### List Marketplace Resource Projects


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-resource-projects/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_resource_projects import marketplace_resource_projects_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_resource_projects_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`marketplace_resource_projects_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_projects/marketplace_resource_projects_list.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceProjectsList } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceProjectsList({
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
    | `name` | string |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `resource` | string (uri) | Resource URL |
    | `resource_uuid` | string (uuid) | Resource UUID |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `resource` | string (uuid) |  |
    | `name` | string |  |
    | `description` | string |  |
    | `backend_id` | string |  |
    | `state` | string |  |
    | `error_message` | string |  |
    | `limits` | any | Dictionary mapping component types to quota values. Same format as Resource.limits. |
    | `current_usages` | any | Dictionary mapping component types to current usage amounts. Populated by backend synchronization. |
    | `resource_uuid` | string (uuid) |  |
    | `resource_name` | string |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-resource-projects/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_resource_projects import marketplace_resource_projects_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_resource_projects_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_resource_projects_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_projects/marketplace_resource_projects_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceProjectsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceProjectsRetrieve({
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
    | `resource` | string (uuid) |  |
    | `name` | string |  |
    | `description` | string |  |
    | `backend_id` | string |  |
    | `state` | string |  |
    | `error_message` | string |  |
    | `limits` | any | Dictionary mapping component types to quota values. Same format as Resource.limits. |
    | `current_usages` | any | Dictionary mapping component types to current usage amounts. Populated by backend synchronization. |
    | `resource_uuid` | string (uuid) |  |
    | `resource_name` | string |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-resource-projects/ \
      Authorization:"Token YOUR_API_TOKEN" \
      resource="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      name="my-awesome-marketplace-resource-project"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.resource_project_request import ResourceProjectRequest # (1)
    from waldur_api_client.api.marketplace_resource_projects import marketplace_resource_projects_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ResourceProjectRequest(
        resource="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        name="my-awesome-marketplace-resource-project"
    )
    response = marketplace_resource_projects_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ResourceProjectRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/resource_project_request.py)
    2.  **API Source:** [`marketplace_resource_projects_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_projects/marketplace_resource_projects_create.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceProjectsCreate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceProjectsCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "resource": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "name": "my-awesome-marketplace-resource-project"
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
    | `name` | string | ✓ |  |
    | `description` | string |  |  |
    | `limits` | any |  | Dictionary mapping component types to quota values. Same format as Resource.limits. |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `resource` | string (uuid) |  |
    | `name` | string |  |
    | `description` | string |  |
    | `backend_id` | string |  |
    | `state` | string |  |
    | `error_message` | string |  |
    | `limits` | any | Dictionary mapping component types to quota values. Same format as Resource.limits. |
    | `current_usages` | any | Dictionary mapping component types to current usage amounts. Populated by backend synchronization. |
    | `resource_uuid` | string (uuid) |  |
    | `resource_name` | string |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/marketplace-resource-projects/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      resource="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      name="my-awesome-marketplace-resource-project"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.resource_project_request import ResourceProjectRequest # (1)
    from waldur_api_client.api.marketplace_resource_projects import marketplace_resource_projects_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ResourceProjectRequest(
        resource="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        name="my-awesome-marketplace-resource-project"
    )
    response = marketplace_resource_projects_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ResourceProjectRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/resource_project_request.py)
    2.  **API Source:** [`marketplace_resource_projects_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_projects/marketplace_resource_projects_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceProjectsUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceProjectsUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "resource": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "name": "my-awesome-marketplace-resource-project"
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
    | `resource` | string (uuid) | ✓ |  |
    | `name` | string | ✓ |  |
    | `description` | string |  |  |
    | `limits` | any |  | Dictionary mapping component types to quota values. Same format as Resource.limits. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `resource` | string (uuid) |  |
    | `name` | string |  |
    | `description` | string |  |
    | `backend_id` | string |  |
    | `state` | string |  |
    | `error_message` | string |  |
    | `limits` | any | Dictionary mapping component types to quota values. Same format as Resource.limits. |
    | `current_usages` | any | Dictionary mapping component types to current usage amounts. Populated by backend synchronization. |
    | `resource_uuid` | string (uuid) |  |
    | `resource_name` | string |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/marketplace-resource-projects/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_resource_project_request import PatchedResourceProjectRequest # (1)
    from waldur_api_client.api.marketplace_resource_projects import marketplace_resource_projects_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedResourceProjectRequest()
    response = marketplace_resource_projects_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedResourceProjectRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_resource_project_request.py)
    2.  **API Source:** [`marketplace_resource_projects_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_projects/marketplace_resource_projects_partial_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceProjectsPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceProjectsPartialUpdate({
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
    | `resource` | string (uuid) |  |  |
    | `name` | string |  |  |
    | `description` | string |  |  |
    | `limits` | any |  | Dictionary mapping component types to quota values. Same format as Resource.limits. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `resource` | string (uuid) |  |
    | `name` | string |  |
    | `description` | string |  |
    | `backend_id` | string |  |
    | `state` | string |  |
    | `error_message` | string |  |
    | `limits` | any | Dictionary mapping component types to quota values. Same format as Resource.limits. |
    | `current_usages` | any | Dictionary mapping component types to current usage amounts. Populated by backend synchronization. |
    | `resource_uuid` | string (uuid) |  |
    | `resource_name` | string |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/marketplace-resource-projects/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_resource_projects import marketplace_resource_projects_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_resource_projects_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_resource_projects_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_projects/marketplace_resource_projects_destroy.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceProjectsDestroy } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceProjectsDestroy({
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

## Permissions & Users


### List users and their roles in a scope

Retrieves a list of users who have a role within a specific scope (e.g., a project or an organization). The list can be filtered by user details or role.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-resource-projects/a1b2c3d4-e5f6-7890-abcd-ef1234567890/list_users/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.user_role_details_field_enum import UserRoleDetailsFieldEnum # (1)
    from waldur_api_client.models.user_role_details_o_enum import UserRoleDetailsOEnum # (2)
    from waldur_api_client.api.marketplace_resource_projects import marketplace_resource_projects_list_users_list # (3)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_resource_projects_list_users_list.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`UserRoleDetailsFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/user_role_details_field_enum.py)
    2.  **Model Source:** [`UserRoleDetailsOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/user_role_details_o_enum.py)
    3.  **API Source:** [`marketplace_resource_projects_list_users_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_projects/marketplace_resource_projects_list_users_list.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceProjectsListUsersList } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceProjectsListUsersList({
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
    | `field` | array | Fields to include in response |
    | `full_name` | string | User full name |
    | `native_name` | string | User native name |
    | `o` | array | Ordering fields |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `role` | string (uuid) | Role UUID or name |
    | `search_string` | string | Search string for user |
    | `user` | string (uuid) | User UUID |
    | `user_slug` | string | User slug |
    | `user_url` | string | User URL |
    | `username` | string | User username |


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

---

### Grant a role to a user

Assigns a specific role to a user within the current scope. An optional expiration time for the role can be set.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-resource-projects/a1b2c3d4-e5f6-7890-abcd-ef1234567890/add_user/ \
      Authorization:"Token YOUR_API_TOKEN" \
      role="string-value" \
      user="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.user_role_create_request import UserRoleCreateRequest # (1)
    from waldur_api_client.api.marketplace_resource_projects import marketplace_resource_projects_add_user # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = UserRoleCreateRequest(
        role="string-value",
        user="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = marketplace_resource_projects_add_user.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`UserRoleCreateRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/user_role_create_request.py)
    2.  **API Source:** [`marketplace_resource_projects_add_user`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_projects/marketplace_resource_projects_add_user.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceProjectsAddUser } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceProjectsAddUser({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
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


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Request Body (required)"

    | Field | Type | Required |
    |---|---|---|
    | `role` | string | ✓ |
    | `user` | string (uuid) | ✓ |
    | `expiration_time` | string (date-time) |  |


=== "Responses"

    **`201`** - 
    
    | Field | Type |
    |---|---|
    | `expiration_time` | string (date-time) |
    
    ---
    
    **`400`** - Validation error, for example when trying to add a user to a terminated project.
    

---

### Revoke a role from a user

Removes a specific role from a user within the current scope. This effectively revokes their permissions associated with that role.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-resource-projects/a1b2c3d4-e5f6-7890-abcd-ef1234567890/delete_user/ \
      Authorization:"Token YOUR_API_TOKEN" \
      role="string-value" \
      user="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.user_role_delete_request import UserRoleDeleteRequest # (1)
    from waldur_api_client.api.marketplace_resource_projects import marketplace_resource_projects_delete_user # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = UserRoleDeleteRequest(
        role="string-value",
        user="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = marketplace_resource_projects_delete_user.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`UserRoleDeleteRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/user_role_delete_request.py)
    2.  **API Source:** [`marketplace_resource_projects_delete_user`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_projects/marketplace_resource_projects_delete_user.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceProjectsDeleteUser } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceProjectsDeleteUser({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
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


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Request Body (required)"

    | Field | Type | Required |
    |---|---|---|
    | `role` | string | ✓ |
    | `user` | string (uuid) | ✓ |
    | `expiration_time` | string (date-time) |  |


=== "Responses"

    **`200`** - Role revoked successfully.
    

---

### Update a user's role expiration

Updates the expiration time for a user's existing role in the current scope. This is useful for extending or shortening the duration of a permission. To make a role permanent, set expiration_time to null.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-resource-projects/a1b2c3d4-e5f6-7890-abcd-ef1234567890/update_user/ \
      Authorization:"Token YOUR_API_TOKEN" \
      role="string-value" \
      user="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.user_role_update_request import UserRoleUpdateRequest # (1)
    from waldur_api_client.api.marketplace_resource_projects import marketplace_resource_projects_update_user # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = UserRoleUpdateRequest(
        role="string-value",
        user="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = marketplace_resource_projects_update_user.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`UserRoleUpdateRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/user_role_update_request.py)
    2.  **API Source:** [`marketplace_resource_projects_update_user`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_projects/marketplace_resource_projects_update_user.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceProjectsUpdateUser } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceProjectsUpdateUser({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
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


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Request Body (required)"

    | Field | Type | Required |
    |---|---|---|
    | `role` | string | ✓ |
    | `user` | string (uuid) | ✓ |
    | `expiration_time` | string (date-time) |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `expiration_time` | string (date-time) |

---
