# Keycloak User Group Memberships

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/keycloak-user-group-memberships/` | [List Keycloak User Group Memberships](#list-keycloak-user-group-memberships) |
| <span class="http-badge http-get">GET</span> | `/api/keycloak-user-group-memberships/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/keycloak-user-group-memberships/` | [Create](#create) |
| <span class="http-badge http-delete">DELETE</span> | `/api/keycloak-user-group-memberships/{uuid}/` | [Delete](#delete) |

---

### List Keycloak User Group Memberships


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/keycloak-user-group-memberships/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.keycloak_user_group_membership_state import KeycloakUserGroupMembershipState # (1)
    from waldur_api_client.api.keycloak_user_group_memberships import keycloak_user_group_memberships_list # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = keycloak_user_group_memberships_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`KeycloakUserGroupMembershipState`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/keycloak_user_group_membership_state.py)
    2.  **API Source:** [`keycloak_user_group_memberships_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/keycloak_user_group_memberships/keycloak_user_group_memberships_list.py)

=== "TypeScript"

    ```typescript
    import { keycloakUserGroupMembershipsList } from 'waldur-js-client';
    
    try {
      const response = await keycloakUserGroupMembershipsList({
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
    | `email` | string |  |
    | `first_name` | string |  |
    | `group_uuid` | string (uuid) |  |
    | `last_name` | string |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `role_uuid` | string (uuid) |  |
    | `scope_type` | string |  |
    | `scope_uuid` | string (uuid) |  |
    | `state` | array |  |
    | `username` | string |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `username` | string | Keycloak user username |
    | `email` | string (email) | User's email for notifications |
    | `first_name` | string |  |
    | `last_name` | string |  |
    | `group` | string (uri) |  |
    | `group_name` | string |  |
    | `group_role` | string |  |
    | `group_scope_type` | string |  |
    | `group_scope_name` | string | Get the name of the cluster or project |
    | `state` | any |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `last_checked` | string (date-time) |  |
    | `error_message` | string |  |
    | `error_traceback` | string |  |


=== "Authorization"

    Any signed-in user.
    
    Memberships of the role groups of the clusters and Rancher projects the caller can see (through a role on the cluster's project or organization); users with the staff or support flag see all of them, whatever their token's scopes.

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/keycloak-user-group-memberships/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.keycloak_user_group_memberships import keycloak_user_group_memberships_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = keycloak_user_group_memberships_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`keycloak_user_group_memberships_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/keycloak_user_group_memberships/keycloak_user_group_memberships_retrieve.py)

=== "TypeScript"

    ```typescript
    import { keycloakUserGroupMembershipsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await keycloakUserGroupMembershipsRetrieve({
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
    | `username` | string | Keycloak user username |
    | `email` | string (email) | User's email for notifications |
    | `first_name` | string |  |
    | `last_name` | string |  |
    | `group` | string (uri) |  |
    | `group_name` | string |  |
    | `group_role` | string |  |
    | `group_scope_type` | string |  |
    | `group_scope_name` | string | Get the name of the cluster or project |
    | `state` | any |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `last_checked` | string (date-time) |  |
    | `error_message` | string |  |
    | `error_traceback` | string |  |


=== "Authorization"

    Any signed-in user.
    
    Memberships of the role groups of the clusters and Rancher projects the caller can see (through a role on the cluster's project or organization); users with the staff or support flag see all of them, whatever their token's scopes.

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/keycloak-user-group-memberships/ \
      Authorization:"Token YOUR_API_TOKEN" \
      username="alice" \
      email="alice@example.com" \
      scope_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      role="https://api.example.com/api/role/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.keycloak_user_group_membership_request import KeycloakUserGroupMembershipRequest # (1)
    from waldur_api_client.api.keycloak_user_group_memberships import keycloak_user_group_memberships_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = KeycloakUserGroupMembershipRequest(
        username="alice",
        email="alice@example.com",
        scope_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        role="https://api.example.com/api/role/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    )
    response = keycloak_user_group_memberships_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`KeycloakUserGroupMembershipRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/keycloak_user_group_membership_request.py)
    2.  **API Source:** [`keycloak_user_group_memberships_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/keycloak_user_group_memberships/keycloak_user_group_memberships_create.py)

=== "TypeScript"

    ```typescript
    import { keycloakUserGroupMembershipsCreate } from 'waldur-js-client';
    
    try {
      const response = await keycloakUserGroupMembershipsCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "username": "alice",
        "email": "alice@example.com",
        "scope_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "role": "https://api.example.com/api/role/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
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
    | `username` | string | ✓ | Keycloak user username |
    | `email` | string (email) | ✓ | User's email for notifications |
    | `scope_uuid` | string (uuid) | ✓ | UUID of a cluster or a project in Rancher<br>_Constraints: write-only_ |
    | `role` | string (uri) | ✓ | <br>_Constraints: write-only_ |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `username` | string | Keycloak user username |
    | `email` | string (email) | User's email for notifications |
    | `first_name` | string |  |
    | `last_name` | string |  |
    | `group` | string (uri) |  |
    | `group_name` | string |  |
    | `group_role` | string |  |
    | `group_scope_type` | string |  |
    | `group_scope_name` | string | Get the name of the cluster or project |
    | `state` | any |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `last_checked` | string (date-time) |  |
    | `error_message` | string |  |
    | `error_traceback` | string |  |


=== "Authorization"

    Staff, or an owner of the organization, or a manager or administrator of the project, that holds the Rancher cluster of the role group: the cluster itself or the cluster of the Rancher project.

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/keycloak-user-group-memberships/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.keycloak_user_group_memberships import keycloak_user_group_memberships_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = keycloak_user_group_memberships_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`keycloak_user_group_memberships_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/keycloak_user_group_memberships/keycloak_user_group_memberships_destroy.py)

=== "TypeScript"

    ```typescript
    import { keycloakUserGroupMembershipsDestroy } from 'waldur-js-client';
    
    try {
      const response = await keycloakUserGroupMembershipsDestroy({
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

    Staff, or an owner of the organization, or a manager or administrator of the project, that holds the Rancher cluster of the role group: the cluster itself or the cluster of the Rancher project.

---
