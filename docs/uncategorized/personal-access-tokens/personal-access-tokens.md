# Personal Access Tokens

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/personal-access-tokens/` | [List Personal Access Tokens](#list-personal-access-tokens) |
| <span class="http-badge http-get">GET</span> | `/api/personal-access-tokens/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/personal-access-tokens/` | [Create a personal access token](#create-a-personal-access-token) |
| <span class="http-badge http-delete">DELETE</span> | `/api/personal-access-tokens/{uuid}/` | [Revoke a personal access token](#revoke-a-personal-access-token) |
| **Other Actions** | | |
| <span class="http-badge http-get">GET</span> | `/api/personal-access-tokens/available_scopes/` | [List available scopes for PAT creation](#list-available-scopes-for-pat-creation) |
| <span class="http-badge http-post">POST</span> | `/api/personal-access-tokens/{uuid}/rotate/` | [Rotate a personal access token](#rotate-a-personal-access-token) |

---
## Core CRUD


### List Personal Access Tokens


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/personal-access-tokens/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.personal_access_tokens import personal_access_tokens_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = personal_access_tokens_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`personal_access_tokens_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/personal_access_tokens/personal_access_tokens_list.py)

=== "TypeScript"

    ```typescript
    import { personalAccessTokensList } from 'waldur-js-client';
    
    try {
      const response = await personalAccessTokensList({
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
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `token_prefix` | string |  |
    | `scopes` | array of strings |  |
    | `expires_at` | string (date-time) |  |
    | `is_active` | boolean |  |
    | `last_used_at` | string (date-time) |  |
    | `last_used_ip` | any | An IPv4 or IPv6 address. |
    | `use_count` | integer |  |
    | `created` | string (date-time) |  |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/personal-access-tokens/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.personal_access_tokens import personal_access_tokens_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = personal_access_tokens_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`personal_access_tokens_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/personal_access_tokens/personal_access_tokens_retrieve.py)

=== "TypeScript"

    ```typescript
    import { personalAccessTokensRetrieve } from 'waldur-js-client';
    
    try {
      const response = await personalAccessTokensRetrieve({
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
    | `name` | string |  |
    | `token_prefix` | string |  |
    | `scopes` | array of strings |  |
    | `expires_at` | string (date-time) |  |
    | `is_active` | boolean |  |
    | `last_used_at` | string (date-time) |  |
    | `last_used_ip` | any | An IPv4 or IPv6 address. |
    | `use_count` | integer |  |
    | `created` | string (date-time) |  |

---

### Create a personal access token


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/personal-access-tokens/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-personal-access-token" \
      scopes:='[]' \
      expires_at="2023-10-01T12:00:00Z"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.personal_access_token_create_request import PersonalAccessTokenCreateRequest # (1)
    from waldur_api_client.api.personal_access_tokens import personal_access_tokens_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PersonalAccessTokenCreateRequest(
        name="my-awesome-personal-access-token",
        scopes=[],
        expires_at="2023-10-01T12:00:00Z"
    )
    response = personal_access_tokens_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PersonalAccessTokenCreateRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/personal_access_token_create_request.py)
    2.  **API Source:** [`personal_access_tokens_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/personal_access_tokens/personal_access_tokens_create.py)

=== "TypeScript"

    ```typescript
    import { personalAccessTokensCreate } from 'waldur-js-client';
    
    try {
      const response = await personalAccessTokensCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "name": "my-awesome-personal-access-token",
        "scopes": [],
        "expires_at": "2023-10-01T12:00:00Z"
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
    | `scopes` | array of strings | ✓ |
    | `expires_at` | string (date-time) | ✓ |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `token` | string | Plaintext token — shown only once. |
    | `scopes` | array of strings |  |
    | `expires_at` | string (date-time) |  |
    | `created` | string (date-time) |  |

---

### Revoke a personal access token


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/personal-access-tokens/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.personal_access_tokens import personal_access_tokens_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = personal_access_tokens_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`personal_access_tokens_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/personal_access_tokens/personal_access_tokens_destroy.py)

=== "TypeScript"

    ```typescript
    import { personalAccessTokensDestroy } from 'waldur-js-client';
    
    try {
      const response = await personalAccessTokensDestroy({
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


### List available scopes for PAT creation

Return permissions the current user can delegate to a PAT.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/personal-access-tokens/available_scopes/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.personal_access_tokens import personal_access_tokens_available_scopes_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = personal_access_tokens_available_scopes_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`personal_access_tokens_available_scopes_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/personal_access_tokens/personal_access_tokens_available_scopes_list.py)

=== "TypeScript"

    ```typescript
    import { personalAccessTokensAvailableScopesList } from 'waldur-js-client';
    
    try {
      const response = await personalAccessTokensAvailableScopesList({
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
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `permission` | string |
    | `description` | string |

---

### Rotate a personal access token

Atomically revoke the old token and create a new one with the same scopes.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/personal-access-tokens/a1b2c3d4-e5f6-7890-abcd-ef1234567890/rotate/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.personal_access_tokens import personal_access_tokens_rotate # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = personal_access_tokens_rotate.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`personal_access_tokens_rotate`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/personal_access_tokens/personal_access_tokens_rotate.py)

=== "TypeScript"

    ```typescript
    import { personalAccessTokensRotate } from 'waldur-js-client';
    
    try {
      const response = await personalAccessTokensRotate({
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

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `token` | string | Plaintext token — shown only once. |
    | `scopes` | array of strings |  |
    | `expires_at` | string (date-time) |  |
    | `created` | string (date-time) |  |

---
