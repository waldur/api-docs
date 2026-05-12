# Marketplace Offering Groups

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-offering-groups/` | [List Marketplace Offering Groups](#list-marketplace-offering-groups) |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-offering-groups/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-offering-groups/` | [Create](#create) |
| <span class="http-badge http-put">PUT</span> | `/api/marketplace-offering-groups/{uuid}/` | [Update](#update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/marketplace-offering-groups/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-delete">DELETE</span> | `/api/marketplace-offering-groups/{uuid}/` | [Delete](#delete) |

---

### List Marketplace Offering Groups


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-offering-groups/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.offering_group_field_enum import OfferingGroupFieldEnum # (1)
    from waldur_api_client.api.marketplace_offering_groups import marketplace_offering_groups_list # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_offering_groups_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`OfferingGroupFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/offering_group_field_enum.py)
    2.  **API Source:** [`marketplace_offering_groups_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_groups/marketplace_offering_groups_list.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingGroupsList } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingGroupsList({
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
    | `customer_uuid` | string (uuid) | Customer UUID |
    | `field` | array |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `title` | string |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `url` | string (uri) |
    | `uuid` | string (uuid) |
    | `created` | string (date-time) |
    | `title` | string |
    | `description` | string |
    | `icon` | string (uri) |
    | `customer` | string (uri) |
    | `customer_uuid` | string (uuid) |
    | `customer_name` | string |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-offering-groups/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.offering_group_field_enum import OfferingGroupFieldEnum # (1)
    from waldur_api_client.api.marketplace_offering_groups import marketplace_offering_groups_retrieve # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_offering_groups_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`OfferingGroupFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/offering_group_field_enum.py)
    2.  **API Source:** [`marketplace_offering_groups_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_groups/marketplace_offering_groups_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingGroupsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingGroupsRetrieve({
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

    | Name | Type |
    |---|---|
    | `field` | array |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `url` | string (uri) |
    | `uuid` | string (uuid) |
    | `created` | string (date-time) |
    | `title` | string |
    | `description` | string |
    | `icon` | string (uri) |
    | `customer` | string (uri) |
    | `customer_uuid` | string (uuid) |
    | `customer_name` | string |

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-offering-groups/ \
      Authorization:"Token YOUR_API_TOKEN" \
      title="string-value" \
      customer="https://api.example.com/api/customer/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.offering_group_request import OfferingGroupRequest # (1)
    from waldur_api_client.api.marketplace_offering_groups import marketplace_offering_groups_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = OfferingGroupRequest(
        title="string-value",
        customer="https://api.example.com/api/customer/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    )
    response = marketplace_offering_groups_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`OfferingGroupRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/offering_group_request.py)
    2.  **API Source:** [`marketplace_offering_groups_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_groups/marketplace_offering_groups_create.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingGroupsCreate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingGroupsCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "title": "string-value",
        "customer": "https://api.example.com/api/customer/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
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
    | `title` | string | ✓ |
    | `description` | string |  |
    | `icon` | string (binary) |  |
    | `customer` | string (uri) | ✓ |


=== "Responses"

    **`201`** - 
    
    | Field | Type |
    |---|---|
    | `url` | string (uri) |
    | `uuid` | string (uuid) |
    | `created` | string (date-time) |
    | `title` | string |
    | `description` | string |
    | `icon` | string (uri) |
    | `customer` | string (uri) |
    | `customer_uuid` | string (uuid) |
    | `customer_name` | string |

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/marketplace-offering-groups/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      title="string-value" \
      customer="https://api.example.com/api/customer/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.offering_group_request import OfferingGroupRequest # (1)
    from waldur_api_client.api.marketplace_offering_groups import marketplace_offering_groups_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = OfferingGroupRequest(
        title="string-value",
        customer="https://api.example.com/api/customer/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    )
    response = marketplace_offering_groups_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`OfferingGroupRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/offering_group_request.py)
    2.  **API Source:** [`marketplace_offering_groups_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_groups/marketplace_offering_groups_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingGroupsUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingGroupsUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "title": "string-value",
        "customer": "https://api.example.com/api/customer/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
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
    | `title` | string | ✓ |
    | `description` | string |  |
    | `icon` | string (binary) |  |
    | `customer` | string (uri) | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `url` | string (uri) |
    | `uuid` | string (uuid) |
    | `created` | string (date-time) |
    | `title` | string |
    | `description` | string |
    | `icon` | string (uri) |
    | `customer` | string (uri) |
    | `customer_uuid` | string (uuid) |
    | `customer_name` | string |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/marketplace-offering-groups/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_offering_group_request import PatchedOfferingGroupRequest # (1)
    from waldur_api_client.api.marketplace_offering_groups import marketplace_offering_groups_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedOfferingGroupRequest()
    response = marketplace_offering_groups_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedOfferingGroupRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_offering_group_request.py)
    2.  **API Source:** [`marketplace_offering_groups_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_groups/marketplace_offering_groups_partial_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingGroupsPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingGroupsPartialUpdate({
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
    | `title` | string |  |
    | `description` | string |  |
    | `icon` | string (binary) |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `url` | string (uri) |
    | `uuid` | string (uuid) |
    | `created` | string (date-time) |
    | `title` | string |
    | `description` | string |
    | `icon` | string (uri) |
    | `customer` | string (uri) |
    | `customer_uuid` | string (uuid) |
    | `customer_name` | string |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/marketplace-offering-groups/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_offering_groups import marketplace_offering_groups_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_offering_groups_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_offering_groups_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_groups/marketplace_offering_groups_destroy.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingGroupsDestroy } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingGroupsDestroy({
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
