# Marketplace Posix Id Pools

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-posix-id-pools/` | [List Marketplace Posix Id Pools](#list-marketplace-posix-id-pools) |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-posix-id-pools/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-posix-id-pools/` | [Create](#create) |
| <span class="http-badge http-put">PUT</span> | `/api/marketplace-posix-id-pools/{uuid}/` | [Update](#update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/marketplace-posix-id-pools/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-delete">DELETE</span> | `/api/marketplace-posix-id-pools/{uuid}/` | [Delete](#delete) |
| **Other Actions** | | |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-posix-id-pools/{uuid}/repoint_preview/` | [Preview re-pointing existing accounts onto this pool](#preview-re-pointing-existing-accounts-onto-this-pool) |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-posix-id-pools/{uuid}/stats/` | [Pool utilization statistics](#pool-utilization-statistics) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-posix-id-pools/{uuid}/repoint/` | [Re-point existing accounts onto this pool](#re-point-existing-accounts-onto-this-pool) |

---
## Core CRUD


### List Marketplace Posix Id Pools


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-posix-id-pools/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.posix_id_pool_field_enum import PosixIdPoolFieldEnum # (1)
    from waldur_api_client.api.marketplace_posix_id_pools import marketplace_posix_id_pools_list # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_posix_id_pools_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`PosixIdPoolFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/posix_id_pool_field_enum.py)
    2.  **API Source:** [`marketplace_posix_id_pools_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_posix_id_pools/marketplace_posix_id_pools_list.py)

=== "TypeScript"

    ```typescript
    import { marketplacePosixIdPoolsList } from 'waldur-js-client';
    
    try {
      const response = await marketplacePosixIdPoolsList({
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
    | `offering_uuid` | string (uuid) | Offering UUID |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `service_provider_uuid` | string (uuid) | Service provider UUID |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `description` | string |  |
    | `service_provider` | string (uuid) |  |
    | `offering` | string (uuid) |  |
    | `min_uid` | integer (int64) |  |
    | `max_uid` | integer (int64) |  |
    | `next_uid` | integer |  |
    | `min_gid` | integer (int64) |  |
    | `max_gid` | integer (int64) |  |
    | `next_gid` | integer |  |
    | `min_group_gid` | integer (int64) | First GID of the range reserved for provider project groups. Without it, project groups draw from the GID range. |
    | `max_group_gid` | integer (int64) | Last GID of the range reserved for project groups. |
    | `next_group_gid` | integer |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `scope` | string |  |
    | `uid_used` | integer |  |
    | `gid_used` | integer |  |
    | `group_gid_used` | integer |  |
    | `uid_utilization` | number (double) |  |
    | `gid_utilization` | number (double) |  |
    | `group_gid_utilization` | number (double) |  |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-posix-id-pools/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.posix_id_pool_field_enum import PosixIdPoolFieldEnum # (1)
    from waldur_api_client.api.marketplace_posix_id_pools import marketplace_posix_id_pools_retrieve # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_posix_id_pools_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PosixIdPoolFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/posix_id_pool_field_enum.py)
    2.  **API Source:** [`marketplace_posix_id_pools_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_posix_id_pools/marketplace_posix_id_pools_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplacePosixIdPoolsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplacePosixIdPoolsRetrieve({
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
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `description` | string |  |
    | `service_provider` | string (uuid) |  |
    | `offering` | string (uuid) |  |
    | `min_uid` | integer (int64) |  |
    | `max_uid` | integer (int64) |  |
    | `next_uid` | integer |  |
    | `min_gid` | integer (int64) |  |
    | `max_gid` | integer (int64) |  |
    | `next_gid` | integer |  |
    | `min_group_gid` | integer (int64) | First GID of the range reserved for provider project groups. Without it, project groups draw from the GID range. |
    | `max_group_gid` | integer (int64) | Last GID of the range reserved for project groups. |
    | `next_group_gid` | integer |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `scope` | string |  |
    | `uid_used` | integer |  |
    | `gid_used` | integer |  |
    | `group_gid_used` | integer |  |
    | `uid_utilization` | number (double) |  |
    | `gid_utilization` | number (double) |  |
    | `group_gid_utilization` | number (double) |  |

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-posix-id-pools/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.posix_id_pool_request import PosixIdPoolRequest # (1)
    from waldur_api_client.api.marketplace_posix_id_pools import marketplace_posix_id_pools_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PosixIdPoolRequest()
    response = marketplace_posix_id_pools_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PosixIdPoolRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/posix_id_pool_request.py)
    2.  **API Source:** [`marketplace_posix_id_pools_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_posix_id_pools/marketplace_posix_id_pools_create.py)

=== "TypeScript"

    ```typescript
    import { marketplacePosixIdPoolsCreate } from 'waldur-js-client';
    
    try {
      const response = await marketplacePosixIdPoolsCreate({
      auth: "Token YOUR_API_TOKEN"
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Request Body"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `description` | string |  |  |
    | `service_provider` | string (uuid) |  |  |
    | `offering` | string (uuid) |  |  |
    | `min_uid` | integer (int64) |  |  |
    | `max_uid` | integer (int64) |  |  |
    | `min_gid` | integer (int64) |  |  |
    | `max_gid` | integer (int64) |  |  |
    | `min_group_gid` | integer (int64) |  | First GID of the range reserved for provider project groups. Without it, project groups draw from the GID range. |
    | `max_group_gid` | integer (int64) |  | Last GID of the range reserved for project groups. |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `description` | string |  |
    | `service_provider` | string (uuid) |  |
    | `offering` | string (uuid) |  |
    | `min_uid` | integer (int64) |  |
    | `max_uid` | integer (int64) |  |
    | `next_uid` | integer |  |
    | `min_gid` | integer (int64) |  |
    | `max_gid` | integer (int64) |  |
    | `next_gid` | integer |  |
    | `min_group_gid` | integer (int64) | First GID of the range reserved for provider project groups. Without it, project groups draw from the GID range. |
    | `max_group_gid` | integer (int64) | Last GID of the range reserved for project groups. |
    | `next_group_gid` | integer |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `scope` | string |  |
    | `uid_used` | integer |  |
    | `gid_used` | integer |  |
    | `group_gid_used` | integer |  |
    | `uid_utilization` | number (double) |  |
    | `gid_utilization` | number (double) |  |
    | `group_gid_utilization` | number (double) |  |

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/marketplace-posix-id-pools/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.posix_id_pool_request import PosixIdPoolRequest # (1)
    from waldur_api_client.api.marketplace_posix_id_pools import marketplace_posix_id_pools_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PosixIdPoolRequest()
    response = marketplace_posix_id_pools_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PosixIdPoolRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/posix_id_pool_request.py)
    2.  **API Source:** [`marketplace_posix_id_pools_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_posix_id_pools/marketplace_posix_id_pools_update.py)

=== "TypeScript"

    ```typescript
    import { marketplacePosixIdPoolsUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplacePosixIdPoolsUpdate({
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
    | `description` | string |  |  |
    | `service_provider` | string (uuid) |  |  |
    | `offering` | string (uuid) |  |  |
    | `min_uid` | integer (int64) |  |  |
    | `max_uid` | integer (int64) |  |  |
    | `min_gid` | integer (int64) |  |  |
    | `max_gid` | integer (int64) |  |  |
    | `min_group_gid` | integer (int64) |  | First GID of the range reserved for provider project groups. Without it, project groups draw from the GID range. |
    | `max_group_gid` | integer (int64) |  | Last GID of the range reserved for project groups. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `description` | string |  |
    | `service_provider` | string (uuid) |  |
    | `offering` | string (uuid) |  |
    | `min_uid` | integer (int64) |  |
    | `max_uid` | integer (int64) |  |
    | `next_uid` | integer |  |
    | `min_gid` | integer (int64) |  |
    | `max_gid` | integer (int64) |  |
    | `next_gid` | integer |  |
    | `min_group_gid` | integer (int64) | First GID of the range reserved for provider project groups. Without it, project groups draw from the GID range. |
    | `max_group_gid` | integer (int64) | Last GID of the range reserved for project groups. |
    | `next_group_gid` | integer |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `scope` | string |  |
    | `uid_used` | integer |  |
    | `gid_used` | integer |  |
    | `group_gid_used` | integer |  |
    | `uid_utilization` | number (double) |  |
    | `gid_utilization` | number (double) |  |
    | `group_gid_utilization` | number (double) |  |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/marketplace-posix-id-pools/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_posix_id_pool_request import PatchedPosixIdPoolRequest # (1)
    from waldur_api_client.api.marketplace_posix_id_pools import marketplace_posix_id_pools_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedPosixIdPoolRequest()
    response = marketplace_posix_id_pools_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedPosixIdPoolRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_posix_id_pool_request.py)
    2.  **API Source:** [`marketplace_posix_id_pools_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_posix_id_pools/marketplace_posix_id_pools_partial_update.py)

=== "TypeScript"

    ```typescript
    import { marketplacePosixIdPoolsPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplacePosixIdPoolsPartialUpdate({
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
    | `description` | string |  |  |
    | `min_uid` | integer (int64) |  |  |
    | `max_uid` | integer (int64) |  |  |
    | `min_gid` | integer (int64) |  |  |
    | `max_gid` | integer (int64) |  |  |
    | `min_group_gid` | integer (int64) |  | First GID of the range reserved for provider project groups. Without it, project groups draw from the GID range. |
    | `max_group_gid` | integer (int64) |  | Last GID of the range reserved for project groups. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `description` | string |  |
    | `service_provider` | string (uuid) |  |
    | `offering` | string (uuid) |  |
    | `min_uid` | integer (int64) |  |
    | `max_uid` | integer (int64) |  |
    | `next_uid` | integer |  |
    | `min_gid` | integer (int64) |  |
    | `max_gid` | integer (int64) |  |
    | `next_gid` | integer |  |
    | `min_group_gid` | integer (int64) | First GID of the range reserved for provider project groups. Without it, project groups draw from the GID range. |
    | `max_group_gid` | integer (int64) | Last GID of the range reserved for project groups. |
    | `next_group_gid` | integer |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `scope` | string |  |
    | `uid_used` | integer |  |
    | `gid_used` | integer |  |
    | `group_gid_used` | integer |  |
    | `uid_utilization` | number (double) |  |
    | `gid_utilization` | number (double) |  |
    | `group_gid_utilization` | number (double) |  |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/marketplace-posix-id-pools/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_posix_id_pools import marketplace_posix_id_pools_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_posix_id_pools_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_posix_id_pools_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_posix_id_pools/marketplace_posix_id_pools_destroy.py)

=== "TypeScript"

    ```typescript
    import { marketplacePosixIdPoolsDestroy } from 'waldur-js-client';
    
    try {
      const response = await marketplacePosixIdPoolsDestroy({
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


### Preview re-pointing existing accounts onto this pool

Adding an override pool to an offering that already has accounts changes nothing by itself: accounts created afterwards draw from the override pool, while existing ones keep the values they were given by the previously resolved pool. This action reports which offering users would change and from which value to which, without writing anything. Offering-level pools only.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-posix-id-pools/a1b2c3d4-e5f6-7890-abcd-ef1234567890/repoint_preview/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_posix_id_pools import marketplace_posix_id_pools_repoint_preview_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_posix_id_pools_repoint_preview_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_posix_id_pools_repoint_preview_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_posix_id_pools/marketplace_posix_id_pools_repoint_preview_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplacePosixIdPoolsRepointPreviewRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplacePosixIdPoolsRepointPreviewRetrieve({
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
    | `changes` | array of objects |  |
    | `changes.offering_user_uuid` | string |  |
    | `changes.offering_uuid` | string |  |
    | `changes.offering_name` | string |  |
    | `changes.user_uuid` | string |  |
    | `changes.username` | string |  |
    | `changes.namespace` | string |  |
    | `changes.old_value` | integer |  |
    | `changes.new_value` | integer |  |
    | `released` | integer | Identities freed in the previously resolved pool. Their values are withheld from recycling until an operator returns them. |
    | `retained` | integer | Users whose previous identity stays active because this pool does not manage every namespace they hold a value in. |
    | `other_consumers` | array of objects | Robot accounts and groups of the offering that keep their values from the previously resolved pool; re-pointing moves offering accounts only. |
    | `other_consumers.kind` | string |  |
    | `other_consumers.uid` | integer |  |
    | `other_consumers.gid` | integer |  |
    | `other_consumers.identity_uuid` | string |  |

---

### Pool utilization statistics


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-posix-id-pools/a1b2c3d4-e5f6-7890-abcd-ef1234567890/stats/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_posix_id_pools import marketplace_posix_id_pools_stats_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_posix_id_pools_stats_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_posix_id_pools_stats_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_posix_id_pools/marketplace_posix_id_pools_stats_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplacePosixIdPoolsStatsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplacePosixIdPoolsStatsRetrieve({
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
    | `uid` | any |  |
    | `gid` | any |  |
    | `group_gid` | any | The range reserved for provider project groups, if any. |
    | `utilization_threshold` | integer |  |

---

### Re-point existing accounts onto this pool

Moves the offering's existing accounts onto this override pool and returns the identifiers that changed. Requires 'confirm': true - preview the impact with repoint_preview first, and reconcile the provider's filesystem afterwards, since the accounts' files still carry the old numbers. Values freed in the previously resolved pool are withheld from recycling until an operator returns them. Offering-level pools only.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-posix-id-pools/a1b2c3d4-e5f6-7890-abcd-ef1234567890/repoint/ \
      Authorization:"Token YOUR_API_TOKEN" \
      confirm=true
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.posix_id_pool_repoint_request_request import PosixIdPoolRepointRequestRequest # (1)
    from waldur_api_client.api.marketplace_posix_id_pools import marketplace_posix_id_pools_repoint # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PosixIdPoolRepointRequestRequest(
        confirm=true
    )
    response = marketplace_posix_id_pools_repoint.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PosixIdPoolRepointRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/posix_id_pool_repoint_request_request.py)
    2.  **API Source:** [`marketplace_posix_id_pools_repoint`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_posix_id_pools/marketplace_posix_id_pools_repoint.py)

=== "TypeScript"

    ```typescript
    import { marketplacePosixIdPoolsRepoint } from 'waldur-js-client';
    
    try {
      const response = await marketplacePosixIdPoolsRepoint({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "confirm": true
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
    | `confirm` | boolean | ✓ | Must be true. Re-pointing rewrites identifiers that the provider's directory and filesystem already carry, so it is never applied implicitly - preview it first with repoint_preview. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `changes` | array of objects |  |
    | `changes.offering_user_uuid` | string |  |
    | `changes.offering_uuid` | string |  |
    | `changes.offering_name` | string |  |
    | `changes.user_uuid` | string |  |
    | `changes.username` | string |  |
    | `changes.namespace` | string |  |
    | `changes.old_value` | integer |  |
    | `changes.new_value` | integer |  |
    | `released` | integer | Identities freed in the previously resolved pool. Their values are withheld from recycling until an operator returns them. |
    | `retained` | integer | Users whose previous identity stays active because this pool does not manage every namespace they hold a value in. |
    | `other_consumers` | array of objects | Robot accounts and groups of the offering that keep their values from the previously resolved pool; re-pointing moves offering accounts only. |
    | `other_consumers.kind` | string |  |
    | `other_consumers.uid` | integer |  |
    | `other_consumers.gid` | integer |  |
    | `other_consumers.identity_uuid` | string |  |

---
