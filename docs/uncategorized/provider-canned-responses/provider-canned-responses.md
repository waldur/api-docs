# Provider Canned Responses

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/provider-canned-responses/` | [List Provider Canned Responses](#list-provider-canned-responses) |
| <span class="http-badge http-get">GET</span> | `/api/provider-canned-responses/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/provider-canned-responses/` | [Create](#create) |
| <span class="http-badge http-put">PUT</span> | `/api/provider-canned-responses/{uuid}/` | [Update](#update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/provider-canned-responses/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-delete">DELETE</span> | `/api/provider-canned-responses/{uuid}/` | [Delete](#delete) |
| **Other Actions** | | |
| <span class="http-badge http-post">POST</span> | `/api/provider-canned-responses/{uuid}/render/` | [Render a canned response with context variables](#render-a-canned-response-with-context-variables) |

---
## Core CRUD


### List Provider Canned Responses


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/provider-canned-responses/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.provider_canned_responses import provider_canned_responses_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = provider_canned_responses_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`provider_canned_responses_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/provider_canned_responses/provider_canned_responses_list.py)

=== "TypeScript"

    ```typescript
    import { providerCannedResponsesList } from 'waldur-js-client';
    
    try {
      const response = await providerCannedResponsesList({
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
    | `category` | string |  |
    | `name` | string |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `provider_helpdesk_uuid` | string (uuid) |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `provider_helpdesk` | string (uuid) |  |
    | `text` | string | Template text. Supports Django template syntax. |
    | `category` | string |  |
    | `usage_count` | integer |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/provider-canned-responses/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.provider_canned_responses import provider_canned_responses_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = provider_canned_responses_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`provider_canned_responses_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/provider_canned_responses/provider_canned_responses_retrieve.py)

=== "TypeScript"

    ```typescript
    import { providerCannedResponsesRetrieve } from 'waldur-js-client';
    
    try {
      const response = await providerCannedResponsesRetrieve({
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
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `provider_helpdesk` | string (uuid) |  |
    | `text` | string | Template text. Supports Django template syntax. |
    | `category` | string |  |
    | `usage_count` | integer |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/provider-canned-responses/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-provider-canned-response" \
      provider_helpdesk="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      text="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.provider_canned_response_request import ProviderCannedResponseRequest # (1)
    from waldur_api_client.api.provider_canned_responses import provider_canned_responses_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ProviderCannedResponseRequest(
        name="my-awesome-provider-canned-response",
        provider_helpdesk="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        text="string-value"
    )
    response = provider_canned_responses_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ProviderCannedResponseRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/provider_canned_response_request.py)
    2.  **API Source:** [`provider_canned_responses_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/provider_canned_responses/provider_canned_responses_create.py)

=== "TypeScript"

    ```typescript
    import { providerCannedResponsesCreate } from 'waldur-js-client';
    
    try {
      const response = await providerCannedResponsesCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "name": "my-awesome-provider-canned-response",
        "provider_helpdesk": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "text": "string-value"
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
    | `provider_helpdesk` | string (uuid) | ✓ |  |
    | `text` | string | ✓ | Template text. Supports Django template syntax. |
    | `category` | string |  |  |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `provider_helpdesk` | string (uuid) |  |
    | `text` | string | Template text. Supports Django template syntax. |
    | `category` | string |  |
    | `usage_count` | integer |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/provider-canned-responses/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-provider-canned-response" \
      provider_helpdesk="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      text="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.provider_canned_response_request import ProviderCannedResponseRequest # (1)
    from waldur_api_client.api.provider_canned_responses import provider_canned_responses_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ProviderCannedResponseRequest(
        name="my-awesome-provider-canned-response",
        provider_helpdesk="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        text="string-value"
    )
    response = provider_canned_responses_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ProviderCannedResponseRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/provider_canned_response_request.py)
    2.  **API Source:** [`provider_canned_responses_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/provider_canned_responses/provider_canned_responses_update.py)

=== "TypeScript"

    ```typescript
    import { providerCannedResponsesUpdate } from 'waldur-js-client';
    
    try {
      const response = await providerCannedResponsesUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "name": "my-awesome-provider-canned-response",
        "provider_helpdesk": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "text": "string-value"
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
    | `provider_helpdesk` | string (uuid) | ✓ |  |
    | `text` | string | ✓ | Template text. Supports Django template syntax. |
    | `category` | string |  |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `provider_helpdesk` | string (uuid) |  |
    | `text` | string | Template text. Supports Django template syntax. |
    | `category` | string |  |
    | `usage_count` | integer |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/provider-canned-responses/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_provider_canned_response_request import PatchedProviderCannedResponseRequest # (1)
    from waldur_api_client.api.provider_canned_responses import provider_canned_responses_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedProviderCannedResponseRequest()
    response = provider_canned_responses_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedProviderCannedResponseRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_provider_canned_response_request.py)
    2.  **API Source:** [`provider_canned_responses_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/provider_canned_responses/provider_canned_responses_partial_update.py)

=== "TypeScript"

    ```typescript
    import { providerCannedResponsesPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await providerCannedResponsesPartialUpdate({
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
    | `provider_helpdesk` | string (uuid) |  |  |
    | `text` | string |  | Template text. Supports Django template syntax. |
    | `category` | string |  |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `provider_helpdesk` | string (uuid) |  |
    | `text` | string | Template text. Supports Django template syntax. |
    | `category` | string |  |
    | `usage_count` | integer |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/provider-canned-responses/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.provider_canned_responses import provider_canned_responses_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = provider_canned_responses_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`provider_canned_responses_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/provider_canned_responses/provider_canned_responses_destroy.py)

=== "TypeScript"

    ```typescript
    import { providerCannedResponsesDestroy } from 'waldur-js-client';
    
    try {
      const response = await providerCannedResponsesDestroy({
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


### Render a canned response with context variables


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/provider-canned-responses/a1b2c3d4-e5f6-7890-abcd-ef1234567890/render/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.canned_response_render_request import CannedResponseRenderRequest # (1)
    from waldur_api_client.api.provider_canned_responses import provider_canned_responses_render # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = CannedResponseRenderRequest()
    response = provider_canned_responses_render.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`CannedResponseRenderRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/canned_response_render_request.py)
    2.  **API Source:** [`provider_canned_responses_render`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/provider_canned_responses/provider_canned_responses_render.py)

=== "TypeScript"

    ```typescript
    import { providerCannedResponsesRender } from 'waldur-js-client';
    
    try {
      const response = await providerCannedResponsesRender({
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
    | `context` | object (free-form) |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `rendered_text` | string |

---
