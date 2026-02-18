# Offering Keycloak Groups

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/offering-keycloak-groups/` | [List Offering Keycloak Groups](#list-offering-keycloak-groups) |
| <span class="http-badge http-get">GET</span> | `/api/offering-keycloak-groups/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/offering-keycloak-groups/{uuid}/pull_members/` | [Pull members from Keycloak for a group](#pull-members-from-keycloak-for-a-group) |
| <span class="http-badge http-delete">DELETE</span> | `/api/offering-keycloak-groups/{uuid}/` | [Delete](#delete) |
| **Other Actions** | | |
| <span class="http-badge http-get">GET</span> | `/api/offering-keycloak-groups/remote_group_members/` | [List members of a remote Keycloak group](#list-members-of-a-remote-keycloak-group) |
| <span class="http-badge http-get">GET</span> | `/api/offering-keycloak-groups/remote_groups/` | [List remote Keycloak groups for an offering](#list-remote-keycloak-groups-for-an-offering) |
| <span class="http-badge http-get">GET</span> | `/api/offering-keycloak-groups/search_remote_users/` | [Search for users in remote Keycloak instance](#search-for-users-in-remote-keycloak-instance) |
| <span class="http-badge http-get">GET</span> | `/api/offering-keycloak-groups/sync_status/` | [Compare local and remote Keycloak group state](#compare-local-and-remote-keycloak-group-state) |
| <span class="http-badge http-post">POST</span> | `/api/offering-keycloak-groups/import_remote/` | [Import a remote Keycloak group as a local OfferingKeycloakGroup](#import-a-remote-keycloak-group-as-a-local-offeringkeycloakgroup) |
| <span class="http-badge http-post">POST</span> | `/api/offering-keycloak-groups/{uuid}/set_backend_id/` | [Set or unlink the backend_id (remote Keycloak group ID) for a local group](#set-or-unlink-the-backend_id-remote-keycloak-group-id-for-a-local-group) |
| <span class="http-badge http-post">POST</span> | `/api/offering-keycloak-groups/test_connection/` | [Test Keycloak connection for an offering](#test-keycloak-connection-for-an-offering) |

---
## Core CRUD


### List Offering Keycloak Groups


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/offering-keycloak-groups/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.offering_keycloak_groups import offering_keycloak_groups_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = offering_keycloak_groups_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`offering_keycloak_groups_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/offering_keycloak_groups/offering_keycloak_groups_list.py)

=== "TypeScript"

    ```typescript
    import { offeringKeycloakGroupsList } from 'waldur-js-client';
    
    try {
      const response = await offeringKeycloakGroupsList({
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
    | `offering_uuid` | string (uuid) |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `resource_uuid` | string (uuid) |  |
    | `role_uuid` | string (uuid) |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `name` | string |  |
    | `backend_id` | string |  |
    | `offering` | string (uri) |  |
    | `offering_uuid` | string (uuid) |  |
    | `offering_name` | string |  |
    | `role` | string (uri) |  |
    | `role_name` | string |  |
    | `role_scope_type` | string | Level this role applies at, e.g. 'cluster', 'project'. Empty means offering-wide. |
    | `resource` | string (uri) |  |
    | `resource_uuid` | string (uuid) |  |
    | `resource_name` | string |  |
    | `scope_id` | string | Sub-entity identifier within a resource, e.g. Rancher project ID within a cluster. |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/offering-keycloak-groups/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.offering_keycloak_groups import offering_keycloak_groups_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = offering_keycloak_groups_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`offering_keycloak_groups_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/offering_keycloak_groups/offering_keycloak_groups_retrieve.py)

=== "TypeScript"

    ```typescript
    import { offeringKeycloakGroupsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await offeringKeycloakGroupsRetrieve({
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
    | `name` | string |  |
    | `backend_id` | string |  |
    | `offering` | string (uri) |  |
    | `offering_uuid` | string (uuid) |  |
    | `offering_name` | string |  |
    | `role` | string (uri) |  |
    | `role_name` | string |  |
    | `role_scope_type` | string | Level this role applies at, e.g. 'cluster', 'project'. Empty means offering-wide. |
    | `resource` | string (uri) |  |
    | `resource_uuid` | string (uuid) |  |
    | `resource_name` | string |  |
    | `scope_id` | string | Sub-entity identifier within a resource, e.g. Rancher project ID within a cluster. |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Pull members from Keycloak for a group


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/offering-keycloak-groups/a1b2c3d4-e5f6-7890-abcd-ef1234567890/pull_members/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.offering_keycloak_groups import offering_keycloak_groups_pull_members # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = offering_keycloak_groups_pull_members.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`offering_keycloak_groups_pull_members`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/offering_keycloak_groups/offering_keycloak_groups_pull_members.py)

=== "TypeScript"

    ```typescript
    import { offeringKeycloakGroupsPullMembers } from 'waldur-js-client';
    
    try {
      const response = await offeringKeycloakGroupsPullMembers({
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
    | `created` | integer |
    | `updated` | integer |
    | `total_remote` | integer |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/offering-keycloak-groups/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.offering_keycloak_groups import offering_keycloak_groups_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = offering_keycloak_groups_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`offering_keycloak_groups_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/offering_keycloak_groups/offering_keycloak_groups_destroy.py)

=== "TypeScript"

    ```typescript
    import { offeringKeycloakGroupsDestroy } from 'waldur-js-client';
    
    try {
      const response = await offeringKeycloakGroupsDestroy({
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


### List members of a remote Keycloak group


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/offering-keycloak-groups/remote_group_members/ \
      Authorization:"Token YOUR_API_TOKEN" \
      group_id=="string-value" \
      offering_uuid=="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.offering_keycloak_groups import offering_keycloak_groups_remote_group_members_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = offering_keycloak_groups_remote_group_members_list.sync(
        client=client,
        group_id="string-value",
        offering_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`offering_keycloak_groups_remote_group_members_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/offering_keycloak_groups/offering_keycloak_groups_remote_group_members_list.py)

=== "TypeScript"

    ```typescript
    import { offeringKeycloakGroupsRemoteGroupMembersList } from 'waldur-js-client';
    
    try {
      const response = await offeringKeycloakGroupsRemoteGroupMembersList({
      auth: "Token YOUR_API_TOKEN",
      query: {
        "group_id": "string-value",
        "offering_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Query Parameters"

    | Name | Type | Required | Description |
    |---|---|---|---|
    | `group_id` | string | ✓ | Keycloak group ID |
    | `offering_uuid` | string | ✓ | UUID of the offering |
    | `page` | integer |  | A page number within the paginated result set. |
    | `page_size` | integer |  | Number of results to return per page. |
    | `resource_uuid` | string (uuid) |  |  |
    | `role_uuid` | string (uuid) |  |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `id` | string |
    | `username` | string |
    | `email` | string |
    | `first_name` | string |
    | `last_name` | string |

---

### List remote Keycloak groups for an offering


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/offering-keycloak-groups/remote_groups/ \
      Authorization:"Token YOUR_API_TOKEN" \
      offering_uuid=="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.offering_keycloak_groups import offering_keycloak_groups_remote_groups_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = offering_keycloak_groups_remote_groups_list.sync(
        client=client,
        offering_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`offering_keycloak_groups_remote_groups_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/offering_keycloak_groups/offering_keycloak_groups_remote_groups_list.py)

=== "TypeScript"

    ```typescript
    import { offeringKeycloakGroupsRemoteGroupsList } from 'waldur-js-client';
    
    try {
      const response = await offeringKeycloakGroupsRemoteGroupsList({
      auth: "Token YOUR_API_TOKEN",
      query: {
        "offering_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Query Parameters"

    | Name | Type | Required | Description |
    |---|---|---|---|
    | `offering_uuid` | string | ✓ | UUID of the offering |
    | `page` | integer |  | A page number within the paginated result set. |
    | `page_size` | integer |  | Number of results to return per page. |
    | `resource_uuid` | string (uuid) |  |  |
    | `role_uuid` | string (uuid) |  |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `id` | string |
    | `name` | string |
    | `path` | string |
    | `sub_group_count` | integer |

---

### Search for users in remote Keycloak instance


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/offering-keycloak-groups/search_remote_users/ \
      Authorization:"Token YOUR_API_TOKEN" \
      offering_uuid=="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      q=="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.offering_keycloak_groups import offering_keycloak_groups_search_remote_users_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = offering_keycloak_groups_search_remote_users_list.sync(
        client=client,
        offering_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        q="string-value"
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`offering_keycloak_groups_search_remote_users_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/offering_keycloak_groups/offering_keycloak_groups_search_remote_users_list.py)

=== "TypeScript"

    ```typescript
    import { offeringKeycloakGroupsSearchRemoteUsersList } from 'waldur-js-client';
    
    try {
      const response = await offeringKeycloakGroupsSearchRemoteUsersList({
      auth: "Token YOUR_API_TOKEN",
      query: {
        "offering_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "q": "string-value"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Query Parameters"

    | Name | Type | Required | Description |
    |---|---|---|---|
    | `offering_uuid` | string | ✓ | UUID of the offering |
    | `page` | integer |  | A page number within the paginated result set. |
    | `page_size` | integer |  | Number of results to return per page. |
    | `q` | string | ✓ | Search query for username, email, or name |
    | `resource_uuid` | string (uuid) |  |  |
    | `role_uuid` | string (uuid) |  |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `id` | string |
    | `username` | string |
    | `email` | string |
    | `first_name` | string |
    | `last_name` | string |

---

### Compare local and remote Keycloak group state


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/offering-keycloak-groups/sync_status/ \
      Authorization:"Token YOUR_API_TOKEN" \
      offering_uuid=="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.offering_keycloak_groups import offering_keycloak_groups_sync_status_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = offering_keycloak_groups_sync_status_retrieve.sync(
        client=client,
        offering_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`offering_keycloak_groups_sync_status_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/offering_keycloak_groups/offering_keycloak_groups_sync_status_retrieve.py)

=== "TypeScript"

    ```typescript
    import { offeringKeycloakGroupsSyncStatusRetrieve } from 'waldur-js-client';
    
    try {
      const response = await offeringKeycloakGroupsSyncStatusRetrieve({
      auth: "Token YOUR_API_TOKEN",
      query: {
        "offering_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Query Parameters"

    | Name | Type | Required | Description |
    |---|---|---|---|
    | `offering_uuid` | string | ✓ | UUID of the offering |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `local_only` | array of strings |
    | `remote_only` | array of strings |
    | `synced` | array of objects |
    | `synced.local_name` | string |
    | `synced.remote_name` | string |
    | `synced.backend_id` | string |

---

### Import a remote Keycloak group as a local OfferingKeycloakGroup


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/offering-keycloak-groups/import_remote/ \
      Authorization:"Token YOUR_API_TOKEN" \
      offering_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      role_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      remote_group_id="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.import_remote_group_request import ImportRemoteGroupRequest # (1)
    from waldur_api_client.api.offering_keycloak_groups import offering_keycloak_groups_import_remote # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ImportRemoteGroupRequest(
        offering_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        role_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        remote_group_id="string-value"
    )
    response = offering_keycloak_groups_import_remote.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ImportRemoteGroupRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/import_remote_group_request.py)
    2.  **API Source:** [`offering_keycloak_groups_import_remote`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/offering_keycloak_groups/offering_keycloak_groups_import_remote.py)

=== "TypeScript"

    ```typescript
    import { offeringKeycloakGroupsImportRemote } from 'waldur-js-client';
    
    try {
      const response = await offeringKeycloakGroupsImportRemote({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "offering_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "role_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "remote_group_id": "string-value"
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
    | `offering_uuid` | string (uuid) | ✓ |
    | `role_uuid` | string (uuid) | ✓ |
    | `remote_group_id` | string | ✓ |
    | `resource_uuid` | string (uuid) |  |
    | `scope_id` | string |  |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `name` | string |  |
    | `backend_id` | string |  |
    | `offering` | string (uri) |  |
    | `offering_uuid` | string (uuid) |  |
    | `offering_name` | string |  |
    | `role` | string (uri) |  |
    | `role_name` | string |  |
    | `role_scope_type` | string | Level this role applies at, e.g. 'cluster', 'project'. Empty means offering-wide. |
    | `resource` | string (uri) |  |
    | `resource_uuid` | string (uuid) |  |
    | `resource_name` | string |  |
    | `scope_id` | string | Sub-entity identifier within a resource, e.g. Rancher project ID within a cluster. |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Set or unlink the backend_id (remote Keycloak group ID) for a local group


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/offering-keycloak-groups/a1b2c3d4-e5f6-7890-abcd-ef1234567890/set_backend_id/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.set_backend_id_request import SetBackendIdRequest # (1)
    from waldur_api_client.api.offering_keycloak_groups import offering_keycloak_groups_set_backend_id # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = SetBackendIdRequest()
    response = offering_keycloak_groups_set_backend_id.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`SetBackendIdRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/set_backend_id_request.py)
    2.  **API Source:** [`offering_keycloak_groups_set_backend_id`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/offering_keycloak_groups/offering_keycloak_groups_set_backend_id.py)

=== "TypeScript"

    ```typescript
    import { offeringKeycloakGroupsSetBackendId } from 'waldur-js-client';
    
    try {
      const response = await offeringKeycloakGroupsSetBackendId({
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
    | `backend_id` | string |  |
    | `resource_uuid` | string (uuid) |  |
    | `scope_id` | string |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `name` | string |  |
    | `backend_id` | string |  |
    | `offering` | string (uri) |  |
    | `offering_uuid` | string (uuid) |  |
    | `offering_name` | string |  |
    | `role` | string (uri) |  |
    | `role_name` | string |  |
    | `role_scope_type` | string | Level this role applies at, e.g. 'cluster', 'project'. Empty means offering-wide. |
    | `resource` | string (uri) |  |
    | `resource_uuid` | string (uuid) |  |
    | `resource_name` | string |  |
    | `scope_id` | string | Sub-entity identifier within a resource, e.g. Rancher project ID within a cluster. |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Test Keycloak connection for an offering


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/offering-keycloak-groups/test_connection/ \
      Authorization:"Token YOUR_API_TOKEN" \
      offering_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.offering_uuid_request import OfferingUUIDRequest # (1)
    from waldur_api_client.api.offering_keycloak_groups import offering_keycloak_groups_test_connection # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = OfferingUUIDRequest(
        offering_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = offering_keycloak_groups_test_connection.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`OfferingUUIDRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/offering_uuid_request.py)
    2.  **API Source:** [`offering_keycloak_groups_test_connection`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/offering_keycloak_groups/offering_keycloak_groups_test_connection.py)

=== "TypeScript"

    ```typescript
    import { offeringKeycloakGroupsTestConnection } from 'waldur-js-client';
    
    try {
      const response = await offeringKeycloakGroupsTestConnection({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "offering_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `offering_uuid` | string (uuid) | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `status` | string |
    | `groups_count` | integer |
    | `groups` | array of strings |

---
