# Organization Groups

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/organization-groups/` | [List Organization Groups](#list-organization-groups) |
| <span class="http-badge http-get">GET</span> | `/api/organization-groups/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/organization-groups/` | [Create](#create) |
| <span class="http-badge http-put">PUT</span> | `/api/organization-groups/{uuid}/` | [Update](#update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/organization-groups/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-delete">DELETE</span> | `/api/organization-groups/{uuid}/` | [Delete](#delete) |

---

### List Organization Groups


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/organization-groups/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.organization_groups import organization_groups_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = organization_groups_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`organization_groups_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/organization_groups/organization_groups_list.py)

=== "TypeScript"

    ```typescript
    import { organizationGroupsList } from 'waldur-js-client';
    
    try {
      const response = await organizationGroupsList({
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
    | `name` | string | Name |
    | `name_exact` | string | Name (exact) |
    | `o` | string | Which field to use when ordering the results. |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `parent` | string (uuid) | Parent UUID |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `name` | string |  |
    | `parent_uuid` | string (uuid) | UUID of the parent organization group |
    | `parent_name` | string | Name of the parent organization group |
    | `parent` | string (uri) |  |
    | `customers_count` | integer | Number of customers in this organization group |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/organization-groups/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.organization_groups import organization_groups_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = organization_groups_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`organization_groups_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/organization_groups/organization_groups_retrieve.py)

=== "TypeScript"

    ```typescript
    import { organizationGroupsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await organizationGroupsRetrieve({
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
    | `parent_uuid` | string (uuid) | UUID of the parent organization group |
    | `parent_name` | string | Name of the parent organization group |
    | `parent` | string (uri) |  |
    | `customers_count` | integer | Number of customers in this organization group |

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/organization-groups/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-organization-group"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.organization_group_request import OrganizationGroupRequest # (1)
    from waldur_api_client.api.organization_groups import organization_groups_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = OrganizationGroupRequest(
        name="my-awesome-organization-group"
    )
    response = organization_groups_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`OrganizationGroupRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/organization_group_request.py)
    2.  **API Source:** [`organization_groups_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/organization_groups/organization_groups_create.py)

=== "TypeScript"

    ```typescript
    import { organizationGroupsCreate } from 'waldur-js-client';
    
    try {
      const response = await organizationGroupsCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "name": "my-awesome-organization-group"
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
    | `name` | string | ✓ |
    | `parent` | string (uri) |  |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `name` | string |  |
    | `parent_uuid` | string (uuid) | UUID of the parent organization group |
    | `parent_name` | string | Name of the parent organization group |
    | `parent` | string (uri) |  |
    | `customers_count` | integer | Number of customers in this organization group |

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/organization-groups/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-organization-group"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.organization_group_request import OrganizationGroupRequest # (1)
    from waldur_api_client.api.organization_groups import organization_groups_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = OrganizationGroupRequest(
        name="my-awesome-organization-group"
    )
    response = organization_groups_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`OrganizationGroupRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/organization_group_request.py)
    2.  **API Source:** [`organization_groups_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/organization_groups/organization_groups_update.py)

=== "TypeScript"

    ```typescript
    import { organizationGroupsUpdate } from 'waldur-js-client';
    
    try {
      const response = await organizationGroupsUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "name": "my-awesome-organization-group"
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
    | `name` | string | ✓ |
    | `parent` | string (uri) |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `name` | string |  |
    | `parent_uuid` | string (uuid) | UUID of the parent organization group |
    | `parent_name` | string | Name of the parent organization group |
    | `parent` | string (uri) |  |
    | `customers_count` | integer | Number of customers in this organization group |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/organization-groups/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_organization_group_request import PatchedOrganizationGroupRequest # (1)
    from waldur_api_client.api.organization_groups import organization_groups_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedOrganizationGroupRequest()
    response = organization_groups_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedOrganizationGroupRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_organization_group_request.py)
    2.  **API Source:** [`organization_groups_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/organization_groups/organization_groups_partial_update.py)

=== "TypeScript"

    ```typescript
    import { organizationGroupsPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await organizationGroupsPartialUpdate({
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
    | `name` | string |  |
    | `parent` | string (uri) |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `name` | string |  |
    | `parent_uuid` | string (uuid) | UUID of the parent organization group |
    | `parent_name` | string | Name of the parent organization group |
    | `parent` | string (uri) |  |
    | `customers_count` | integer | Number of customers in this organization group |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/organization-groups/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.organization_groups import organization_groups_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = organization_groups_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`organization_groups_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/organization_groups/organization_groups_destroy.py)

=== "TypeScript"

    ```typescript
    import { organizationGroupsDestroy } from 'waldur-js-client';
    
    try {
      const response = await organizationGroupsDestroy({
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
