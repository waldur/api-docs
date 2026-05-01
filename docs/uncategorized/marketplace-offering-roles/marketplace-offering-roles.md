# Marketplace Offering Roles

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-offering-roles/` | [List Marketplace Offering Roles](#list-marketplace-offering-roles) |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-offering-roles/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-offering-roles/` | [Create](#create) |
| <span class="http-badge http-put">PUT</span> | `/api/marketplace-offering-roles/{uuid}/` | [Update](#update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/marketplace-offering-roles/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-delete">DELETE</span> | `/api/marketplace-offering-roles/{uuid}/` | [Delete](#delete) |

---

### List Marketplace Offering Roles


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-offering-roles/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_offering_roles import marketplace_offering_roles_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_offering_roles_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`marketplace_offering_roles_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_roles/marketplace_offering_roles_list.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingRolesList } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingRolesList({
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
    | `content_type` | string |  |
    | `name` | string |  |
    | `offering_uuid` | string |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `name` | string |
    | `description` | string |
    | `content_type` | string |
    | `offering_uuid` | string |
    | `offering_name` | string |
    | `is_active` | boolean |
    | `permissions` | array of strings |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-offering-roles/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_offering_roles import marketplace_offering_roles_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_offering_roles_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_offering_roles_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_roles/marketplace_offering_roles_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingRolesRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingRolesRetrieve({
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
    | `name` | string |
    | `description` | string |
    | `content_type` | string |
    | `offering_uuid` | string |
    | `offering_name` | string |
    | `is_active` | boolean |
    | `permissions` | array of strings |

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-offering-roles/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-marketplace-offering-role"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.offering_role_request import OfferingRoleRequest # (1)
    from waldur_api_client.api.marketplace_offering_roles import marketplace_offering_roles_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = OfferingRoleRequest(
        name="my-awesome-marketplace-offering-role"
    )
    response = marketplace_offering_roles_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`OfferingRoleRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/offering_role_request.py)
    2.  **API Source:** [`marketplace_offering_roles_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_roles/marketplace_offering_roles_create.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingRolesCreate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingRolesCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "name": "my-awesome-marketplace-offering-role"
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
    | `description` | string |  |  |
    | `content_type_input` | any |  | Scope on create: 'resource' or 'resource_project'.<br>_Constraints: write-only_ |
    | `offering` | string (uuid) |  | Offering UUID — pin role to this single offering.<br>_Constraints: write-only_ |


=== "Responses"

    **`201`** - 
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `name` | string |
    | `description` | string |
    | `content_type` | string |
    | `offering_uuid` | string |
    | `offering_name` | string |
    | `is_active` | boolean |
    | `permissions` | array of strings |

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/marketplace-offering-roles/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-marketplace-offering-role"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.offering_role_request import OfferingRoleRequest # (1)
    from waldur_api_client.api.marketplace_offering_roles import marketplace_offering_roles_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = OfferingRoleRequest(
        name="my-awesome-marketplace-offering-role"
    )
    response = marketplace_offering_roles_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`OfferingRoleRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/offering_role_request.py)
    2.  **API Source:** [`marketplace_offering_roles_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_roles/marketplace_offering_roles_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingRolesUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingRolesUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "name": "my-awesome-marketplace-offering-role"
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
    | `description` | string |  |  |
    | `content_type_input` | any |  | Scope on create: 'resource' or 'resource_project'.<br>_Constraints: write-only_ |
    | `offering` | string (uuid) |  | Offering UUID — pin role to this single offering.<br>_Constraints: write-only_ |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `name` | string |
    | `description` | string |
    | `content_type` | string |
    | `offering_uuid` | string |
    | `offering_name` | string |
    | `is_active` | boolean |
    | `permissions` | array of strings |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/marketplace-offering-roles/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_offering_role_request import PatchedOfferingRoleRequest # (1)
    from waldur_api_client.api.marketplace_offering_roles import marketplace_offering_roles_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedOfferingRoleRequest()
    response = marketplace_offering_roles_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedOfferingRoleRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_offering_role_request.py)
    2.  **API Source:** [`marketplace_offering_roles_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_roles/marketplace_offering_roles_partial_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingRolesPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingRolesPartialUpdate({
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
    | `description` | string |  |  |
    | `content_type_input` | any |  | Scope on create: 'resource' or 'resource_project'.<br>_Constraints: write-only_ |
    | `offering` | string (uuid) |  | Offering UUID — pin role to this single offering.<br>_Constraints: write-only_ |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `name` | string |
    | `description` | string |
    | `content_type` | string |
    | `offering_uuid` | string |
    | `offering_name` | string |
    | `is_active` | boolean |
    | `permissions` | array of strings |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/marketplace-offering-roles/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_offering_roles import marketplace_offering_roles_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_offering_roles_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_offering_roles_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_roles/marketplace_offering_roles_destroy.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingRolesDestroy } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingRolesDestroy({
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
