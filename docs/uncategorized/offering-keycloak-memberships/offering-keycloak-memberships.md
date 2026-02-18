# Offering Keycloak Memberships

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/offering-keycloak-memberships/` | [List Offering Keycloak Memberships](#list-offering-keycloak-memberships) |
| <span class="http-badge http-get">GET</span> | `/api/offering-keycloak-memberships/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/offering-keycloak-memberships/` | [Create](#create) |
| <span class="http-badge http-delete">DELETE</span> | `/api/offering-keycloak-memberships/{uuid}/` | [Delete](#delete) |

---

### List Offering Keycloak Memberships


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/offering-keycloak-memberships/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.offering_keycloak_memberships import offering_keycloak_memberships_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = offering_keycloak_memberships_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`offering_keycloak_memberships_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/offering_keycloak_memberships/offering_keycloak_memberships_list.py)

=== "TypeScript"

    ```typescript
    import { offeringKeycloakMembershipsList } from 'waldur-js-client';
    
    try {
      const response = await offeringKeycloakMembershipsList({
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
    | `offering_uuid` | string (uuid) |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `resource_uuid` | string (uuid) |  |
    | `role_uuid` | string (uuid) |  |
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
    | `group_role_name` | string |  |
    | `group_offering_uuid` | string (uuid) |  |
    | `group_offering_name` | string |  |
    | `group_resource_name` | string |  |
    | `group_resource_uuid` | string (uuid) |  |
    | `group_scope_id` | string | Sub-entity identifier within a resource, e.g. Rancher project ID within a cluster. |
    | `group_role_scope_type` | string | Level this role applies at, e.g. 'cluster', 'project'. Empty means offering-wide. |
    | `group_role_scope_type_label` | string | Human-readable label for scope_type shown to end users, e.g. 'Rancher Project', 'Cluster Namespace'. Falls back to capitalized scope_type if empty. |
    | `user` | string (uri) |  |
    | `state` | any |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `last_checked` | string (date-time) |  |
    | `error_message` | string |  |
    | `error_traceback` | string |  |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/offering-keycloak-memberships/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.offering_keycloak_memberships import offering_keycloak_memberships_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = offering_keycloak_memberships_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`offering_keycloak_memberships_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/offering_keycloak_memberships/offering_keycloak_memberships_retrieve.py)

=== "TypeScript"

    ```typescript
    import { offeringKeycloakMembershipsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await offeringKeycloakMembershipsRetrieve({
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
    | `group_role_name` | string |  |
    | `group_offering_uuid` | string (uuid) |  |
    | `group_offering_name` | string |  |
    | `group_resource_name` | string |  |
    | `group_resource_uuid` | string (uuid) |  |
    | `group_scope_id` | string | Sub-entity identifier within a resource, e.g. Rancher project ID within a cluster. |
    | `group_role_scope_type` | string | Level this role applies at, e.g. 'cluster', 'project'. Empty means offering-wide. |
    | `group_role_scope_type_label` | string | Human-readable label for scope_type shown to end users, e.g. 'Rancher Project', 'Cluster Namespace'. Falls back to capitalized scope_type if empty. |
    | `user` | string (uri) |  |
    | `state` | any |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `last_checked` | string (date-time) |  |
    | `error_message` | string |  |
    | `error_traceback` | string |  |

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/offering-keycloak-memberships/ \
      Authorization:"Token YOUR_API_TOKEN" \
      username="alice" \
      email="alice@example.com" \
      offering="https://api.example.com/api/offering/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      role="https://api.example.com/api/role/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.offering_keycloak_membership_request import OfferingKeycloakMembershipRequest # (1)
    from waldur_api_client.api.offering_keycloak_memberships import offering_keycloak_memberships_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = OfferingKeycloakMembershipRequest(
        username="alice",
        email="alice@example.com",
        offering="https://api.example.com/api/offering/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        role="https://api.example.com/api/role/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    )
    response = offering_keycloak_memberships_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`OfferingKeycloakMembershipRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/offering_keycloak_membership_request.py)
    2.  **API Source:** [`offering_keycloak_memberships_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/offering_keycloak_memberships/offering_keycloak_memberships_create.py)

=== "TypeScript"

    ```typescript
    import { offeringKeycloakMembershipsCreate } from 'waldur-js-client';
    
    try {
      const response = await offeringKeycloakMembershipsCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "username": "alice",
        "email": "alice@example.com",
        "offering": "https://api.example.com/api/offering/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
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
    | `offering` | string (uri) | ✓ | <br>_Constraints: write-only_ |
    | `role` | string (uri) | ✓ | <br>_Constraints: write-only_ |
    | `resource` | string (uri) |  | <br>_Constraints: write-only_ |
    | `scope_id` | string |  | <br>_Constraints: write-only, default: ``_ |
    | `user` | string (uri) |  |  |


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
    | `group_role_name` | string |  |
    | `group_offering_uuid` | string (uuid) |  |
    | `group_offering_name` | string |  |
    | `group_resource_name` | string |  |
    | `group_resource_uuid` | string (uuid) |  |
    | `group_scope_id` | string | Sub-entity identifier within a resource, e.g. Rancher project ID within a cluster. |
    | `group_role_scope_type` | string | Level this role applies at, e.g. 'cluster', 'project'. Empty means offering-wide. |
    | `group_role_scope_type_label` | string | Human-readable label for scope_type shown to end users, e.g. 'Rancher Project', 'Cluster Namespace'. Falls back to capitalized scope_type if empty. |
    | `user` | string (uri) |  |
    | `state` | any |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `last_checked` | string (date-time) |  |
    | `error_message` | string |  |
    | `error_traceback` | string |  |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/offering-keycloak-memberships/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.offering_keycloak_memberships import offering_keycloak_memberships_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = offering_keycloak_memberships_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`offering_keycloak_memberships_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/offering_keycloak_memberships/offering_keycloak_memberships_destroy.py)

=== "TypeScript"

    ```typescript
    import { offeringKeycloakMembershipsDestroy } from 'waldur-js-client';
    
    try {
      const response = await offeringKeycloakMembershipsDestroy({
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
