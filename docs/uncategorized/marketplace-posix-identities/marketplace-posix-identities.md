# Marketplace Posix Identities

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-posix-identities/` | [List Marketplace Posix Identities](#list-marketplace-posix-identities) |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-posix-identities/{uuid}/` | [Retrieve](#retrieve) |

---

### List Marketplace Posix Identities


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-posix-identities/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_posix_identities import marketplace_posix_identities_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_posix_identities_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`marketplace_posix_identities_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_posix_identities/marketplace_posix_identities_list.py)

=== "TypeScript"

    ```typescript
    import { marketplacePosixIdentitiesList } from 'waldur-js-client';
    
    try {
      const response = await marketplacePosixIdentitiesList({
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
    | `is_released` | boolean |  |
    | `offering_uuid` | string (uuid) | Offering UUID |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `pool_uuid` | string (uuid) | POSIX ID pool UUID |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `url` | string (uri) |
    | `uuid` | string (uuid) |
    | `created` | string (date-time) |
    | `uid` | integer (int64) |
    | `gid` | integer (int64) |
    | `released_at` | string (date-time) |
    | `pool_uuid` | string (uuid) |
    | `offering_uuid` | string (uuid) |
    | `offering_name` | string |
    | `consumer_type` | string |
    | `consumer_name` | string |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-posix-identities/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_posix_identities import marketplace_posix_identities_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_posix_identities_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_posix_identities_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_posix_identities/marketplace_posix_identities_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplacePosixIdentitiesRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplacePosixIdentitiesRetrieve({
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
    | `url` | string (uri) |
    | `uuid` | string (uuid) |
    | `created` | string (date-time) |
    | `uid` | integer (int64) |
    | `gid` | integer (int64) |
    | `released_at` | string (date-time) |
    | `pool_uuid` | string (uuid) |
    | `offering_uuid` | string (uuid) |
    | `offering_name` | string |
    | `consumer_type` | string |
    | `consumer_name` | string |

---
