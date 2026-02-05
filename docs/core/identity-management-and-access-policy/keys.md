# Keys

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/keys/` | [List Keys](#list-keys) |
| <span class="http-badge http-get">GET</span> | `/api/keys/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/keys/` | [Create](#create) |
| <span class="http-badge http-delete">DELETE</span> | `/api/keys/{uuid}/` | [Delete](#delete) |
| **Other Actions** | | |
| <span class="http-badge http-get">GET</span> | `/api/keys/{uuid}/history/at/` | [Get object state at a specific timestamp](#get-object-state-at-a-specific-timestamp) |
| <span class="http-badge http-get">GET</span> | `/api/keys/{uuid}/history/` | [Get version history](#get-version-history) |

---
## Core CRUD


### List Keys


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/keys/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.keys import keys_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = keys_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`keys_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/keys/keys_list.py)

=== "TypeScript"

    ```typescript
    import { keysList } from 'waldur-js-client';
    
    try {
      const response = await keysList({
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
    | `created` | string (date-time) | Created after |
    | `field` | array |  |
    | `fingerprint_md5` | string |  |
    | `fingerprint_sha256` | string |  |
    | `fingerprint_sha512` | string |  |
    | `is_shared` | boolean |  |
    | `modified` | string (date-time) | Modified after |
    | `name` | string | Name |
    | `name_exact` | string | Name (exact) |
    | `o` | array | Ordering<br><br> |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `user_uuid` | string (uuid) | User UUID |
    | `uuid` | string (uuid) | UUID |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `url` | string (uri) |
    | `uuid` | string (uuid) |
    | `name` | string |
    | `public_key` | string |
    | `fingerprint_md5` | string |
    | `fingerprint_sha256` | string |
    | `fingerprint_sha512` | string |
    | `user_uuid` | string (uuid) |
    | `is_shared` | boolean |
    | `type` | string |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/keys/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.keys import keys_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = keys_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`keys_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/keys/keys_retrieve.py)

=== "TypeScript"

    ```typescript
    import { keysRetrieve } from 'waldur-js-client';
    
    try {
      const response = await keysRetrieve({
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
    | `name` | string |
    | `public_key` | string |
    | `fingerprint_md5` | string |
    | `fingerprint_sha256` | string |
    | `fingerprint_sha512` | string |
    | `user_uuid` | string (uuid) |
    | `is_shared` | boolean |
    | `type` | string |

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/keys/ \
      Authorization:"Token YOUR_API_TOKEN" \
      public_key="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.ssh_key_request import SshKeyRequest # (1)
    from waldur_api_client.api.keys import keys_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = SshKeyRequest(
        public_key="string-value"
    )
    response = keys_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`SshKeyRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/ssh_key_request.py)
    2.  **API Source:** [`keys_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/keys/keys_create.py)

=== "TypeScript"

    ```typescript
    import { keysCreate } from 'waldur-js-client';
    
    try {
      const response = await keysCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "public_key": "string-value"
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
    | `name` | string |  |
    | `public_key` | string | ✓ |


=== "Responses"

    **`201`** - 
    
    | Field | Type |
    |---|---|
    | `url` | string (uri) |
    | `uuid` | string (uuid) |
    | `name` | string |
    | `public_key` | string |
    | `fingerprint_md5` | string |
    | `fingerprint_sha256` | string |
    | `fingerprint_sha512` | string |
    | `user_uuid` | string (uuid) |
    | `is_shared` | boolean |
    | `type` | string |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/keys/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.keys import keys_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = keys_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`keys_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/keys/keys_destroy.py)

=== "TypeScript"

    ```typescript
    import { keysDestroy } from 'waldur-js-client';
    
    try {
      const response = await keysDestroy({
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


### Get object state at a specific timestamp

Returns the state of the object as it was at the specified timestamp. Only accessible by staff and support users.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/keys/a1b2c3d4-e5f6-7890-abcd-ef1234567890/history/at/ \
      Authorization:"Token YOUR_API_TOKEN" \
      timestamp=="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.keys import keys_history_at_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = keys_history_at_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        timestamp="string-value"
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`keys_history_at_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/keys/keys_history_at_retrieve.py)

=== "TypeScript"

    ```typescript
    import { keysHistoryAtRetrieve } from 'waldur-js-client';
    
    try {
      const response = await keysHistoryAtRetrieve({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      query: {
        "timestamp": "string-value"
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

    | Name | Type | Required | Description |
    |---|---|---|---|
    | `timestamp` | string | ✓ | ISO 8601 timestamp to query the object state at |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `id` | integer | Version ID |
    | `revision_date` | string (date-time) | When this revision was created |
    | `revision_user` | object (free-form) | User who created this revision |
    | `revision_comment` | string | Comment describing the revision |
    | `serialized_data` | object (free-form) | Serialized model fields at this revision |
    
    ---
    
    **`400`** - 
    
    
    ---
    
    **`404`** - 
    

---

### Get version history

Returns the version history for this object. Only accessible by staff and support users.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/keys/a1b2c3d4-e5f6-7890-abcd-ef1234567890/history/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.keys import keys_history_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = keys_history_list.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`keys_history_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/keys/keys_history_list.py)

=== "TypeScript"

    ```typescript
    import { keysHistoryList } from 'waldur-js-client';
    
    try {
      const response = await keysHistoryList({
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
    | `created` | string (date-time) | Created after |
    | `created_after` | string | Filter versions created after this timestamp (ISO 8601) |
    | `created_before` | string | Filter versions created before this timestamp (ISO 8601) |
    | `fingerprint_md5` | string |  |
    | `fingerprint_sha256` | string |  |
    | `fingerprint_sha512` | string |  |
    | `is_shared` | boolean |  |
    | `modified` | string (date-time) | Modified after |
    | `name` | string | Name |
    | `name_exact` | string | Name (exact) |
    | `o` | array | Ordering<br><br> |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `user_uuid` | string (uuid) | User UUID |
    | `uuid` | string (uuid) | UUID |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `id` | integer | Version ID |
    | `revision_date` | string (date-time) | When this revision was created |
    | `revision_user` | object (free-form) | User who created this revision |
    | `revision_comment` | string | Comment describing the revision |
    | `serialized_data` | object (free-form) | Serialized model fields at this revision |

---
