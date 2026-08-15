# Marketplace Resource Api Keys

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-resource-api-keys/` | [List Marketplace Resource Api Keys](#list-marketplace-resource-api-keys) |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-resource-api-keys/{uuid}/` | [Retrieve](#retrieve) |
| **Other Actions** | | |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-resource-api-keys/{uuid}/reveal/` | [Reveal an API key](#reveal-an-api-key) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-resource-api-keys/report_created/` | [Report a freshly-applied API key](#report-a-freshly-applied-api-key) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-resource-api-keys/{uuid}/rotate/` | [Rotate an API key](#rotate-an-api-key) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-resource-api-keys/{uuid}/set_erred/` | [Mark an API key as erred](#mark-an-api-key-as-erred) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-resource-api-keys/{uuid}/set_key/` | [Report a rotated API key value](#report-a-rotated-api-key-value) |

---
## Core CRUD


### List Marketplace Resource Api Keys


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-resource-api-keys/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.resource_api_key_state import ResourceApiKeyState # (1)
    from waldur_api_client.api.marketplace_resource_api_keys import marketplace_resource_api_keys_list # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_resource_api_keys_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`ResourceApiKeyState`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/resource_api_key_state.py)
    2.  **API Source:** [`marketplace_resource_api_keys_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_api_keys/marketplace_resource_api_keys_list.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceApiKeysList } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceApiKeysList({
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
    | `modified_before` | string (date-time) | Modified before |
    | `offering_uuid` | string (uuid) | Offering UUID |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `resource_uuid` | string (uuid) | Resource UUID |
    | `state` | array | API key state<br><br> |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `resource_uuid` | string (uuid) |
    | `resource_backend_id` | string |
    | `client_id` | string |
    | `state` | string |
    | `modified` | string (date-time) |
    | `error_message` | string |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-resource-api-keys/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_resource_api_keys import marketplace_resource_api_keys_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_resource_api_keys_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_resource_api_keys_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_api_keys/marketplace_resource_api_keys_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceApiKeysRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceApiKeysRetrieve({
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
    | `resource_uuid` | string (uuid) |
    | `resource_backend_id` | string |
    | `client_id` | string |
    | `state` | string |
    | `modified` | string (date-time) |
    | `error_message` | string |

---

## Other Actions


### Reveal an API key

Returns the decrypted key value. Available to users with resource access (except minimal-visibility viewers). Audit-logged.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-resource-api-keys/a1b2c3d4-e5f6-7890-abcd-ef1234567890/reveal/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_resource_api_keys import marketplace_resource_api_keys_reveal_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_resource_api_keys_reveal_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_resource_api_keys_reveal_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_api_keys/marketplace_resource_api_keys_reveal_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceApiKeysRevealRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceApiKeysRevealRetrieve({
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
    | `resource_uuid` | string (uuid) |
    | `resource_backend_id` | string |
    | `client_id` | string |
    | `state` | string |
    | `modified` | string (date-time) |
    | `error_message` | string |
    | `api_key` | string |

---

### Report a freshly-applied API key

Used by the site agent after it generated and applied a key to the backend. Stores the value encrypted and marks the key OK.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-resource-api-keys/report_created/ \
      Authorization:"Token YOUR_API_TOKEN" \
      resource="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      client_id="string-value" \
      api_key="********"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.resource_api_key_report_created_request import ResourceApiKeyReportCreatedRequest # (1)
    from waldur_api_client.api.marketplace_resource_api_keys import marketplace_resource_api_keys_report_created # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ResourceApiKeyReportCreatedRequest(
        resource="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client_id="string-value",
        api_key="********"
    )
    response = marketplace_resource_api_keys_report_created.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ResourceApiKeyReportCreatedRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/resource_api_key_report_created_request.py)
    2.  **API Source:** [`marketplace_resource_api_keys_report_created`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_api_keys/marketplace_resource_api_keys_report_created.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceApiKeysReportCreated } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceApiKeysReportCreated({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "resource": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "client_id": "string-value",
        "api_key": "********"
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
    | `resource` | string (uuid) | ✓ |
    | `client_id` | string | ✓ |
    | `api_key` | string | ✓ |


=== "Responses"

    **`201`** - 
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `resource_uuid` | string (uuid) |
    | `resource_backend_id` | string |
    | `client_id` | string |
    | `state` | string |
    | `modified` | string (date-time) |
    | `error_message` | string |

---

### Rotate an API key

Asks the site agent to replace this key's value at the backend. The other keys are untouched (zero downtime).


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-resource-api-keys/a1b2c3d4-e5f6-7890-abcd-ef1234567890/rotate/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_resource_api_keys import marketplace_resource_api_keys_rotate # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_resource_api_keys_rotate.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_resource_api_keys_rotate`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_api_keys/marketplace_resource_api_keys_rotate.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceApiKeysRotate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceApiKeysRotate({
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

    **`202`** - 
    
    | Field | Type |
    |---|---|
    | `status` | string |

---

### Mark an API key as erred

Used by the site agent to report that applying the key failed. Stores the error message for the UI.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-resource-api-keys/a1b2c3d4-e5f6-7890-abcd-ef1234567890/set_erred/ \
      Authorization:"Token YOUR_API_TOKEN" \
      error_message="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.resource_api_key_set_erred_request import ResourceApiKeySetErredRequest # (1)
    from waldur_api_client.api.marketplace_resource_api_keys import marketplace_resource_api_keys_set_erred # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ResourceApiKeySetErredRequest(
        error_message="string-value"
    )
    response = marketplace_resource_api_keys_set_erred.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ResourceApiKeySetErredRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/resource_api_key_set_erred_request.py)
    2.  **API Source:** [`marketplace_resource_api_keys_set_erred`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_api_keys/marketplace_resource_api_keys_set_erred.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceApiKeysSetErred } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceApiKeysSetErred({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "error_message": "string-value"
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
    | `error_message` | string | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `resource_uuid` | string (uuid) |
    | `resource_backend_id` | string |
    | `client_id` | string |
    | `state` | string |
    | `modified` | string (date-time) |
    | `error_message` | string |

---

### Report a rotated API key value

Used by the site agent after it applied a rotated key. Replaces the stored value and marks the key OK.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-resource-api-keys/a1b2c3d4-e5f6-7890-abcd-ef1234567890/set_key/ \
      Authorization:"Token YOUR_API_TOKEN" \
      api_key="********"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.resource_api_key_set_key_request import ResourceApiKeySetKeyRequest # (1)
    from waldur_api_client.api.marketplace_resource_api_keys import marketplace_resource_api_keys_set_key # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ResourceApiKeySetKeyRequest(
        api_key="********"
    )
    response = marketplace_resource_api_keys_set_key.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ResourceApiKeySetKeyRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/resource_api_key_set_key_request.py)
    2.  **API Source:** [`marketplace_resource_api_keys_set_key`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_api_keys/marketplace_resource_api_keys_set_key.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceApiKeysSetKey } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceApiKeysSetKey({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "api_key": "********"
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
    | `api_key` | string | ✓ |
    | `client_id` | string |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `resource_uuid` | string (uuid) |
    | `resource_backend_id` | string |
    | `client_id` | string |
    | `state` | string |
    | `modified` | string (date-time) |
    | `error_message` | string |

---
