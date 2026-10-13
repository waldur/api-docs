# Marketplace Resource Api Keys

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-resource-api-keys/` | [List Marketplace Resource Api Keys](#list-marketplace-resource-api-keys) |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-resource-api-keys/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-resource-api-keys/` | [Request an API key](#request-an-api-key) |
| <span class="http-badge http-patch">PATCH</span> | `/api/marketplace-resource-api-keys/{uuid}/` | [Edit an API key](#edit-an-api-key) |
| <span class="http-badge http-delete">DELETE</span> | `/api/marketplace-resource-api-keys/{uuid}/` | [Delete an API key](#delete-an-api-key) |
| **Other Actions** | | |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-resource-api-keys/{uuid}/reveal/` | [Reveal an API key](#reveal-an-api-key) |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-resource-api-keys/usage_totals/` | [Total API key usage of a resource](#total-api-key-usage-of-a-resource) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-resource-api-keys/{uuid}/pause/` | [Pause an API key](#pause-an-api-key) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-resource-api-keys/report_created/` | [Report a freshly-applied API key](#report-a-freshly-applied-api-key) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-resource-api-keys/{uuid}/report_usage/` | [Report API key usage](#report-api-key-usage) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-resource-api-keys/{uuid}/resume/` | [Resume an API key](#resume-an-api-key) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-resource-api-keys/{uuid}/retry/` | [Retry a failed API key command](#retry-a-failed-api-key-command) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-resource-api-keys/{uuid}/rotate/` | [Rotate an API key](#rotate-an-api-key) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-resource-api-keys/{uuid}/set_deleted/` | [Report an API key deleted](#report-an-api-key-deleted) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-resource-api-keys/{uuid}/set_erred/` | [Mark an API key as erred](#mark-an-api-key-as-erred) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-resource-api-keys/{uuid}/set_key/` | [Report a created or rotated API key value](#report-a-created-or-rotated-api-key-value) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-resource-api-keys/{uuid}/set_ok/` | [Report an API key resumed or updated](#report-an-api-key-resumed-or-updated) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-resource-api-keys/{uuid}/set_paused/` | [Report an API key paused](#report-an-api-key-paused) |

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
    from waldur_api_client.models.resource_api_key_action import ResourceApiKeyAction # (1)
    from waldur_api_client.models.resource_api_key_state import ResourceApiKeyState # (2)
    from waldur_api_client.api.marketplace_resource_api_keys import marketplace_resource_api_keys_list # (3)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_resource_api_keys_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`ResourceApiKeyAction`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/resource_api_key_action.py)
    2.  **Model Source:** [`ResourceApiKeyState`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/resource_api_key_state.py)
    3.  **API Source:** [`marketplace_resource_api_keys_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_api_keys/marketplace_resource_api_keys_list.py)

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
    | `has_pending_action` | boolean | Has a pending command |
    | `modified_before` | string (date-time) | Modified before |
    | `offering_uuid` | string (uuid) | Offering UUID |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `pending_action` | array | Pending command<br><br> |
    | `resource_uuid` | string (uuid) | Resource UUID |
    | `state` | array | API key state<br><br> |
    | `user_uuid` | string (uuid) | Assignee UUID |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `resource_uuid` | string (uuid) |  |
    | `resource_backend_id` | string |  |
    | `client_id` | string |  |
    | `state` | string | <br>_Enum: `Creating`, `OK`, `Updating`, `Paused`, `Deleting`, `Deleted`, `Erred`_ |
    | `pending_action` | any |  |
    | `modified` | string (date-time) |  |
    | `issued_at` | string (date-time) | When the agent last stored a value for this key: its creation or its latest rotation. Unlike modified, a pause or an edit leaves it alone. |
    | `error_message` | string |  |
    | `user_uuid` | string (uuid) |  |
    | `user_full_name` | string |  |
    | `limits` | object (free-form) |  |
    | `allowed_models` | array of strings |  |
    | `current_usages` | object (free-form) |  |
    | `usage_period` | string (date) |  |
    | `paused_by_limit` | boolean |  |

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
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `resource_uuid` | string (uuid) |  |
    | `resource_backend_id` | string |  |
    | `client_id` | string |  |
    | `state` | string | <br>_Enum: `Creating`, `OK`, `Updating`, `Paused`, `Deleting`, `Deleted`, `Erred`_ |
    | `pending_action` | any |  |
    | `modified` | string (date-time) |  |
    | `issued_at` | string (date-time) | When the agent last stored a value for this key: its creation or its latest rotation. Unlike modified, a pause or an edit leaves it alone. |
    | `error_message` | string |  |
    | `user_uuid` | string (uuid) |  |
    | `user_full_name` | string |  |
    | `limits` | object (free-form) |  |
    | `allowed_models` | array of strings |  |
    | `current_usages` | object (free-form) |  |
    | `usage_period` | string (date) |  |
    | `paused_by_limit` | boolean |  |

---

### Request an API key

Asks the site agent to create a key for the resource. Waldur generates nothing: the key appears as Creating and turns OK once the agent reports it. Only on offerings with enable_api_key_provisioning.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-resource-api-keys/ \
      Authorization:"Token YOUR_API_TOKEN" \
      resource="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.resource_api_key_create_request import ResourceApiKeyCreateRequest # (1)
    from waldur_api_client.api.marketplace_resource_api_keys import marketplace_resource_api_keys_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ResourceApiKeyCreateRequest(
        resource="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = marketplace_resource_api_keys_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ResourceApiKeyCreateRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/resource_api_key_create_request.py)
    2.  **API Source:** [`marketplace_resource_api_keys_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_api_keys/marketplace_resource_api_keys_create.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceApiKeysCreate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceApiKeysCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "resource": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `user` | string (uuid) |  | Assignee. When set, only this user can reveal the key. |
    | `limits` | object (free-form) |  | Limits per component type; zero or absent means no limit. |
    | `allowed_models` | array of strings |  | Models the key may call; empty or absent allows every model. |
    | `resource` | string (uuid) | ✓ |  |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `resource_uuid` | string (uuid) |  |
    | `resource_backend_id` | string |  |
    | `client_id` | string |  |
    | `state` | string | <br>_Enum: `Creating`, `OK`, `Updating`, `Paused`, `Deleting`, `Deleted`, `Erred`_ |
    | `pending_action` | any |  |
    | `modified` | string (date-time) |  |
    | `issued_at` | string (date-time) | When the agent last stored a value for this key: its creation or its latest rotation. Unlike modified, a pause or an edit leaves it alone. |
    | `error_message` | string |  |
    | `user_uuid` | string (uuid) |  |
    | `user_full_name` | string |  |
    | `limits` | object (free-form) |  |
    | `allowed_models` | array of strings |  |
    | `current_usages` | object (free-form) |  |
    | `usage_period` | string (date) |  |
    | `paused_by_limit` | boolean |  |

---

### Edit an API key

Changes the key's assignee, limits or model allowlist. A change to limits or models is sent to the site agent as an update command, unless the key is paused: resuming it applies them. Only on offerings with enable_api_key_provisioning, except for unassigning the key ({"user": null}).


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/marketplace-resource-api-keys/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_resource_api_key_update_request import PatchedResourceApiKeyUpdateRequest # (1)
    from waldur_api_client.api.marketplace_resource_api_keys import marketplace_resource_api_keys_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedResourceApiKeyUpdateRequest()
    response = marketplace_resource_api_keys_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedResourceApiKeyUpdateRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_resource_api_key_update_request.py)
    2.  **API Source:** [`marketplace_resource_api_keys_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_api_keys/marketplace_resource_api_keys_partial_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceApiKeysPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceApiKeysPartialUpdate({
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
    | `user` | string (uuid) |  | Assignee. When set, only this user can reveal the key. |
    | `limits` | object (free-form) |  | Limits per component type; zero or absent means no limit. |
    | `allowed_models` | array of strings |  | Models the key may call; empty or absent allows every model. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `resource_uuid` | string (uuid) |  |
    | `resource_backend_id` | string |  |
    | `client_id` | string |  |
    | `state` | string | <br>_Enum: `Creating`, `OK`, `Updating`, `Paused`, `Deleting`, `Deleted`, `Erred`_ |
    | `pending_action` | any |  |
    | `modified` | string (date-time) |  |
    | `issued_at` | string (date-time) | When the agent last stored a value for this key: its creation or its latest rotation. Unlike modified, a pause or an edit leaves it alone. |
    | `error_message` | string |  |
    | `user_uuid` | string (uuid) |  |
    | `user_full_name` | string |  |
    | `limits` | object (free-form) |  |
    | `allowed_models` | array of strings |  |
    | `current_usages` | object (free-form) |  |
    | `usage_period` | string (date) |  |
    | `paused_by_limit` | boolean |  |

---

### Delete an API key

Asks the site agent to revoke the key at the backend. Once it has, the key is Deleted: it no longer lists by default, but its row and reported usage are kept. A requested key the agent has not created yet, or failed to create, is Deleted at once.


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/marketplace-resource-api-keys/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_resource_api_keys import marketplace_resource_api_keys_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_resource_api_keys_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_resource_api_keys_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_api_keys/marketplace_resource_api_keys_destroy.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceApiKeysDestroy } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceApiKeysDestroy({
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

## Other Actions


### Reveal an API key

Returns the decrypted key value. Available to users with resource access (except minimal-visibility viewers); a key with an assignee only to the assignee. Staff and support always. Audit-logged.


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
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `resource_uuid` | string (uuid) |  |
    | `resource_backend_id` | string |  |
    | `client_id` | string |  |
    | `state` | string | <br>_Enum: `Creating`, `OK`, `Updating`, `Paused`, `Deleting`, `Deleted`, `Erred`_ |
    | `pending_action` | any |  |
    | `modified` | string (date-time) |  |
    | `issued_at` | string (date-time) | When the agent last stored a value for this key: its creation or its latest rotation. Unlike modified, a pause or an edit leaves it alone. |
    | `error_message` | string |  |
    | `user_uuid` | string (uuid) |  |
    | `user_full_name` | string |  |
    | `limits` | object (free-form) |  |
    | `allowed_models` | array of strings |  |
    | `current_usages` | object (free-form) |  |
    | `usage_period` | string (date) |  |
    | `paused_by_limit` | boolean |  |
    | `api_key` | string |  |

---

### Total API key usage of a resource

Sums the usage the site agent reported for the resource's keys in the current month, per component type. Deleted keys are included, so deleting a key leaves the total unchanged.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-resource-api-keys/usage_totals/ \
      Authorization:"Token YOUR_API_TOKEN" \
      resource_uuid=="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_resource_api_keys import marketplace_resource_api_keys_usage_totals_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_resource_api_keys_usage_totals_retrieve.sync(
        client=client,
        resource_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_resource_api_keys_usage_totals_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_api_keys/marketplace_resource_api_keys_usage_totals_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceApiKeysUsageTotalsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceApiKeysUsageTotalsRetrieve({
      auth: "Token YOUR_API_TOKEN",
      query: {
        "resource_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Query Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `resource_uuid` | string (uuid) | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `usages` | object (free-form) | Usage per component type in the current month, summed over the resource's keys, deleted ones included. |

---

### Pause an API key

Asks the site agent to stop the backend accepting this key. The key keeps its value; the resource and its other keys keep serving.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-resource-api-keys/a1b2c3d4-e5f6-7890-abcd-ef1234567890/pause/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_resource_api_keys import marketplace_resource_api_keys_pause # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_resource_api_keys_pause.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_resource_api_keys_pause`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_api_keys/marketplace_resource_api_keys_pause.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceApiKeysPause } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceApiKeysPause({
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

### Report a freshly-applied API key

Used by the site agent after it generated and applied a key to the backend at provisioning. Stores the value encrypted and marks the key OK. A requested key is reported through set_key instead.


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
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `resource_uuid` | string (uuid) |  |
    | `resource_backend_id` | string |  |
    | `client_id` | string |  |
    | `state` | string | <br>_Enum: `Creating`, `OK`, `Updating`, `Paused`, `Deleting`, `Deleted`, `Erred`_ |
    | `pending_action` | any |  |
    | `modified` | string (date-time) |  |
    | `issued_at` | string (date-time) | When the agent last stored a value for this key: its creation or its latest rotation. Unlike modified, a pause or an edit leaves it alone. |
    | `error_message` | string |  |
    | `user_uuid` | string (uuid) |  |
    | `user_full_name` | string |  |
    | `limits` | object (free-form) |  |
    | `allowed_models` | array of strings |  |
    | `current_usages` | object (free-form) |  |
    | `usage_period` | string (date) |  |
    | `paused_by_limit` | boolean |  |

---

### Report API key usage

Used by the site agent to report a key's usage so far in a month, per component type. Merged into the key's usage for that month; a later month replaces it, and an earlier one is refused. A key whose usage reaches its limit is paused, and a key paused for its limit is resumed once under it again. Accepted for a deleted key too.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-resource-api-keys/a1b2c3d4-e5f6-7890-abcd-ef1234567890/report_usage/ \
      Authorization:"Token YOUR_API_TOKEN" \
      usages:='{}'
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.resource_api_key_usage_request import ResourceApiKeyUsageRequest # (1)
    from waldur_api_client.api.marketplace_resource_api_keys import marketplace_resource_api_keys_report_usage # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ResourceApiKeyUsageRequest(
        usages={}
    )
    response = marketplace_resource_api_keys_report_usage.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ResourceApiKeyUsageRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/resource_api_key_usage_request.py)
    2.  **API Source:** [`marketplace_resource_api_keys_report_usage`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_api_keys/marketplace_resource_api_keys_report_usage.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceApiKeysReportUsage } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceApiKeysReportUsage({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "usages": {}
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
    | `usages` | object (free-form) | ✓ | The key's usage so far in billing_period, per component type. |
    | `billing_period` | string (date) |  | Any day of the month the usage belongs to; the current month when omitted. Limits are monthly, so a later month starts them afresh. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `resource_uuid` | string (uuid) |  |
    | `resource_backend_id` | string |  |
    | `client_id` | string |  |
    | `state` | string | <br>_Enum: `Creating`, `OK`, `Updating`, `Paused`, `Deleting`, `Deleted`, `Erred`_ |
    | `pending_action` | any |  |
    | `modified` | string (date-time) |  |
    | `issued_at` | string (date-time) | When the agent last stored a value for this key: its creation or its latest rotation. Unlike modified, a pause or an edit leaves it alone. |
    | `error_message` | string |  |
    | `user_uuid` | string (uuid) |  |
    | `user_full_name` | string |  |
    | `limits` | object (free-form) |  |
    | `allowed_models` | array of strings |  |
    | `current_usages` | object (free-form) |  |
    | `usage_period` | string (date) |  |
    | `paused_by_limit` | boolean |  |

---

### Resume an API key

Asks the site agent to accept a paused key again, with the limits and models it has now. Available without governance too, so a key paused before the provider switched it off can come back.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-resource-api-keys/a1b2c3d4-e5f6-7890-abcd-ef1234567890/resume/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_resource_api_keys import marketplace_resource_api_keys_resume # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_resource_api_keys_resume.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_resource_api_keys_resume`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_api_keys/marketplace_resource_api_keys_resume.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceApiKeysResume } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceApiKeysResume({
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

### Retry a failed API key command

Sends the command that left the key Erred to the site agent again, with the key's current limits and models. An Erred key accepts only this, the same command, or a delete.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-resource-api-keys/a1b2c3d4-e5f6-7890-abcd-ef1234567890/retry/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_resource_api_keys import marketplace_resource_api_keys_retry # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_resource_api_keys_retry.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_resource_api_keys_retry`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_api_keys/marketplace_resource_api_keys_retry.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceApiKeysRetry } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceApiKeysRetry({
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

### Report an API key deleted

Used by the site agent once the backend has revoked the key. The stored value is dropped; the row and its usage are kept.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-resource-api-keys/a1b2c3d4-e5f6-7890-abcd-ef1234567890/set_deleted/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_resource_api_keys import marketplace_resource_api_keys_set_deleted # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_resource_api_keys_set_deleted.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_resource_api_keys_set_deleted`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_api_keys/marketplace_resource_api_keys_set_deleted.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceApiKeysSetDeleted } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceApiKeysSetDeleted({
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
    | `resource_uuid` | string (uuid) |  |
    | `resource_backend_id` | string |  |
    | `client_id` | string |  |
    | `state` | string | <br>_Enum: `Creating`, `OK`, `Updating`, `Paused`, `Deleting`, `Deleted`, `Erred`_ |
    | `pending_action` | any |  |
    | `modified` | string (date-time) |  |
    | `issued_at` | string (date-time) | When the agent last stored a value for this key: its creation or its latest rotation. Unlike modified, a pause or an edit leaves it alone. |
    | `error_message` | string |  |
    | `user_uuid` | string (uuid) |  |
    | `user_full_name` | string |  |
    | `limits` | object (free-form) |  |
    | `allowed_models` | array of strings |  |
    | `current_usages` | object (free-form) |  |
    | `usage_period` | string (date) |  |
    | `paused_by_limit` | boolean |  |

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
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `resource_uuid` | string (uuid) |  |
    | `resource_backend_id` | string |  |
    | `client_id` | string |  |
    | `state` | string | <br>_Enum: `Creating`, `OK`, `Updating`, `Paused`, `Deleting`, `Deleted`, `Erred`_ |
    | `pending_action` | any |  |
    | `modified` | string (date-time) |  |
    | `issued_at` | string (date-time) | When the agent last stored a value for this key: its creation or its latest rotation. Unlike modified, a pause or an edit leaves it alone. |
    | `error_message` | string |  |
    | `user_uuid` | string (uuid) |  |
    | `user_full_name` | string |  |
    | `limits` | object (free-form) |  |
    | `allowed_models` | array of strings |  |
    | `current_usages` | object (free-form) |  |
    | `usage_period` | string (date) |  |
    | `paused_by_limit` | boolean |  |

---

### Report a created or rotated API key value

Used by the site agent after it applied a requested or rotated key. Replaces the stored value and marks the key OK. A requested key carries the client_id the agent gave it.


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
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `resource_uuid` | string (uuid) |  |
    | `resource_backend_id` | string |  |
    | `client_id` | string |  |
    | `state` | string | <br>_Enum: `Creating`, `OK`, `Updating`, `Paused`, `Deleting`, `Deleted`, `Erred`_ |
    | `pending_action` | any |  |
    | `modified` | string (date-time) |  |
    | `issued_at` | string (date-time) | When the agent last stored a value for this key: its creation or its latest rotation. Unlike modified, a pause or an edit leaves it alone. |
    | `error_message` | string |  |
    | `user_uuid` | string (uuid) |  |
    | `user_full_name` | string |  |
    | `limits` | object (free-form) |  |
    | `allowed_models` | array of strings |  |
    | `current_usages` | object (free-form) |  |
    | `usage_period` | string (date) |  |
    | `paused_by_limit` | boolean |  |

---

### Report an API key resumed or updated

Used by the site agent once the backend accepts a resumed key again, or has applied a key's new limits and models.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-resource-api-keys/a1b2c3d4-e5f6-7890-abcd-ef1234567890/set_ok/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_resource_api_keys import marketplace_resource_api_keys_set_ok # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_resource_api_keys_set_ok.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_resource_api_keys_set_ok`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_api_keys/marketplace_resource_api_keys_set_ok.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceApiKeysSetOk } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceApiKeysSetOk({
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
    | `resource_uuid` | string (uuid) |  |
    | `resource_backend_id` | string |  |
    | `client_id` | string |  |
    | `state` | string | <br>_Enum: `Creating`, `OK`, `Updating`, `Paused`, `Deleting`, `Deleted`, `Erred`_ |
    | `pending_action` | any |  |
    | `modified` | string (date-time) |  |
    | `issued_at` | string (date-time) | When the agent last stored a value for this key: its creation or its latest rotation. Unlike modified, a pause or an edit leaves it alone. |
    | `error_message` | string |  |
    | `user_uuid` | string (uuid) |  |
    | `user_full_name` | string |  |
    | `limits` | object (free-form) |  |
    | `allowed_models` | array of strings |  |
    | `current_usages` | object (free-form) |  |
    | `usage_period` | string (date) |  |
    | `paused_by_limit` | boolean |  |

---

### Report an API key paused

Used by the site agent once the backend refuses the key.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-resource-api-keys/a1b2c3d4-e5f6-7890-abcd-ef1234567890/set_paused/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_resource_api_keys import marketplace_resource_api_keys_set_paused # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_resource_api_keys_set_paused.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_resource_api_keys_set_paused`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_api_keys/marketplace_resource_api_keys_set_paused.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceApiKeysSetPaused } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceApiKeysSetPaused({
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
    | `resource_uuid` | string (uuid) |  |
    | `resource_backend_id` | string |  |
    | `client_id` | string |  |
    | `state` | string | <br>_Enum: `Creating`, `OK`, `Updating`, `Paused`, `Deleting`, `Deleted`, `Erred`_ |
    | `pending_action` | any |  |
    | `modified` | string (date-time) |  |
    | `issued_at` | string (date-time) | When the agent last stored a value for this key: its creation or its latest rotation. Unlike modified, a pause or an edit leaves it alone. |
    | `error_message` | string |  |
    | `user_uuid` | string (uuid) |  |
    | `user_full_name` | string |  |
    | `limits` | object (free-form) |  |
    | `allowed_models` | array of strings |  |
    | `current_usages` | object (free-form) |  |
    | `usage_period` | string (date) |  |
    | `paused_by_limit` | boolean |  |

---
