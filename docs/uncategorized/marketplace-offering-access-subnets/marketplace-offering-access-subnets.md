# Marketplace Offering Access Subnets

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-offering-access-subnets/` | [List resources](#list-resources) |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-offering-access-subnets/{uuid}/` | [Retrieve a resource](#retrieve-a-resource) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-offering-access-subnets/` | [Create](#create) |
| <span class="http-badge http-put">PUT</span> | `/api/marketplace-offering-access-subnets/{uuid}/` | [Update a resource](#update-a-resource) |
| <span class="http-badge http-patch">PATCH</span> | `/api/marketplace-offering-access-subnets/{uuid}/` | [Partially update a resource](#partially-update-a-resource) |
| <span class="http-badge http-delete">DELETE</span> | `/api/marketplace-offering-access-subnets/{uuid}/` | [Delete](#delete) |

---

### List resources

Returns a paginated list of resources accessible to the current user.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-offering-access-subnets/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_offering_access_subnets import marketplace_offering_access_subnets_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_offering_access_subnets_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`marketplace_offering_access_subnets_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_access_subnets/marketplace_offering_access_subnets_list.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingAccessSubnetsList } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingAccessSubnetsList({
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
    | `description` | string | Description |
    | `inet` | string | Inet |
    | `offering` | string (uri) | Offering URL |
    | `offering_uuid` | string (uuid) | Offering UUID |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `inet` | string |
    | `description` | string |
    | `offering` | string (uri) |
    | `offering_name` | string |

---

### Retrieve a resource

Returns details of a specific resource.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-offering-access-subnets/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_offering_access_subnets import marketplace_offering_access_subnets_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_offering_access_subnets_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_offering_access_subnets_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_access_subnets/marketplace_offering_access_subnets_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingAccessSubnetsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingAccessSubnetsRetrieve({
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
    | `inet` | string |
    | `description` | string |
    | `offering` | string (uri) |
    | `offering_name` | string |

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-offering-access-subnets/ \
      Authorization:"Token YOUR_API_TOKEN" \
      inet="string-value" \
      offering="https://api.example.com/api/offering/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.offering_access_subnet_request import OfferingAccessSubnetRequest # (1)
    from waldur_api_client.api.marketplace_offering_access_subnets import marketplace_offering_access_subnets_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = OfferingAccessSubnetRequest(
        inet="string-value",
        offering="https://api.example.com/api/offering/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    )
    response = marketplace_offering_access_subnets_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`OfferingAccessSubnetRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/offering_access_subnet_request.py)
    2.  **API Source:** [`marketplace_offering_access_subnets_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_access_subnets/marketplace_offering_access_subnets_create.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingAccessSubnetsCreate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingAccessSubnetsCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "inet": "string-value",
        "offering": "https://api.example.com/api/offering/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
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
    | `inet` | string | ✓ |
    | `description` | string |  |
    | `offering` | string (uri) | ✓ |


=== "Responses"

    **`201`** - 
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `inet` | string |
    | `description` | string |
    | `offering` | string (uri) |
    | `offering_name` | string |

---

### Update a resource

Updates the name, description, or end date of a resource. Requires appropriate permissions.


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/marketplace-offering-access-subnets/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      inet="string-value" \
      offering="https://api.example.com/api/offering/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.offering_access_subnet_request import OfferingAccessSubnetRequest # (1)
    from waldur_api_client.api.marketplace_offering_access_subnets import marketplace_offering_access_subnets_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = OfferingAccessSubnetRequest(
        inet="string-value",
        offering="https://api.example.com/api/offering/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    )
    response = marketplace_offering_access_subnets_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`OfferingAccessSubnetRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/offering_access_subnet_request.py)
    2.  **API Source:** [`marketplace_offering_access_subnets_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_access_subnets/marketplace_offering_access_subnets_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingAccessSubnetsUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingAccessSubnetsUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "inet": "string-value",
        "offering": "https://api.example.com/api/offering/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
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
    | `inet` | string | ✓ |
    | `description` | string |  |
    | `offering` | string (uri) | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `inet` | string |
    | `description` | string |
    | `offering` | string (uri) |
    | `offering_name` | string |

---

### Partially update a resource

Partially updates the name, description, or end date of a resource. Requires appropriate permissions.


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/marketplace-offering-access-subnets/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_offering_access_subnet_request import PatchedOfferingAccessSubnetRequest # (1)
    from waldur_api_client.api.marketplace_offering_access_subnets import marketplace_offering_access_subnets_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedOfferingAccessSubnetRequest()
    response = marketplace_offering_access_subnets_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedOfferingAccessSubnetRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_offering_access_subnet_request.py)
    2.  **API Source:** [`marketplace_offering_access_subnets_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_access_subnets/marketplace_offering_access_subnets_partial_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingAccessSubnetsPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingAccessSubnetsPartialUpdate({
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
    | `inet` | string |  |
    | `description` | string |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `inet` | string |
    | `description` | string |
    | `offering` | string (uri) |
    | `offering_name` | string |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/marketplace-offering-access-subnets/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_offering_access_subnets import marketplace_offering_access_subnets_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_offering_access_subnets_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_offering_access_subnets_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_access_subnets/marketplace_offering_access_subnets_destroy.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingAccessSubnetsDestroy } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingAccessSubnetsDestroy({
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
