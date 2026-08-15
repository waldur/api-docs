# Provider Helpdesks

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/provider-helpdesks/` | [List Provider Helpdesks](#list-provider-helpdesks) |
| <span class="http-badge http-get">GET</span> | `/api/provider-helpdesks/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/provider-helpdesks/` | [Create](#create) |
| <span class="http-badge http-put">PUT</span> | `/api/provider-helpdesks/{uuid}/` | [Update](#update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/provider-helpdesks/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-delete">DELETE</span> | `/api/provider-helpdesks/{uuid}/` | [Delete](#delete) |
| **Other Actions** | | |
| <span class="http-badge http-post">POST</span> | `/api/provider-helpdesks/{uuid}/validate/` | [Validate provider helpdesk backend connectivity](#validate-provider-helpdesk-backend-connectivity) |

---
## Core CRUD


### List Provider Helpdesks


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/provider-helpdesks/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.provider_helpdesks import provider_helpdesks_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = provider_helpdesks_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`provider_helpdesks_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/provider_helpdesks/provider_helpdesks_list.py)

=== "TypeScript"

    ```typescript
    import { providerHelpdesksList } from 'waldur-js-client';
    
    try {
      const response = await providerHelpdesksList({
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
    | `backend_type` | string |  |
    | `is_active` | boolean |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `service_provider_uuid` | string (uuid) |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `service_provider` | string (uuid) |  |
    | `service_provider_name` | string |  |
    | `backend_type` | string | <br>_Enum: `basic`, `email`, `atlassian`, `zammad`, `smax`_ |
    | `settings` | object (free-form) | Backend-specific configuration. |
    | `is_active` | boolean |  |
    | `webhook_secret` | string |  |
    | `notification_email` | string (email) | Primary email for notifications. |
    | `notify_on_new_ticket` | boolean |  |
    | `notify_on_comment` | boolean |  |
    | `notify_on_escalation` | boolean |  |
    | `notify_on_sla_warning` | boolean |  |
    | `health_status` | string |  |
    | `last_health_check` | string (date-time) |  |
    | `failed_routing_count` | integer |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/provider-helpdesks/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.provider_helpdesks import provider_helpdesks_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = provider_helpdesks_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`provider_helpdesks_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/provider_helpdesks/provider_helpdesks_retrieve.py)

=== "TypeScript"

    ```typescript
    import { providerHelpdesksRetrieve } from 'waldur-js-client';
    
    try {
      const response = await providerHelpdesksRetrieve({
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
    | `service_provider` | string (uuid) |  |
    | `service_provider_name` | string |  |
    | `backend_type` | string | <br>_Enum: `basic`, `email`, `atlassian`, `zammad`, `smax`_ |
    | `settings` | object (free-form) | Backend-specific configuration. |
    | `is_active` | boolean |  |
    | `webhook_secret` | string |  |
    | `notification_email` | string (email) | Primary email for notifications. |
    | `notify_on_new_ticket` | boolean |  |
    | `notify_on_comment` | boolean |  |
    | `notify_on_escalation` | boolean |  |
    | `notify_on_sla_warning` | boolean |  |
    | `health_status` | string |  |
    | `last_health_check` | string (date-time) |  |
    | `failed_routing_count` | integer |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/provider-helpdesks/ \
      Authorization:"Token YOUR_API_TOKEN" \
      service_provider="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.provider_helpdesk_request import ProviderHelpdeskRequest # (1)
    from waldur_api_client.api.provider_helpdesks import provider_helpdesks_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ProviderHelpdeskRequest(
        service_provider="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = provider_helpdesks_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ProviderHelpdeskRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/provider_helpdesk_request.py)
    2.  **API Source:** [`provider_helpdesks_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/provider_helpdesks/provider_helpdesks_create.py)

=== "TypeScript"

    ```typescript
    import { providerHelpdesksCreate } from 'waldur-js-client';
    
    try {
      const response = await providerHelpdesksCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "service_provider": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `service_provider` | string (uuid) | ✓ |  |
    | `backend_type` | string |  | <br>_Enum: `basic`, `email`, `atlassian`, `zammad`, `smax`_ |
    | `settings` | object (free-form) |  | Backend-specific configuration. |
    | `is_active` | boolean |  |  |
    | `webhook_secret` | string |  |  |
    | `notification_email` | string (email) |  | Primary email for notifications. |
    | `notify_on_new_ticket` | boolean |  |  |
    | `notify_on_comment` | boolean |  |  |
    | `notify_on_escalation` | boolean |  |  |
    | `notify_on_sla_warning` | boolean |  |  |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `service_provider` | string (uuid) |  |
    | `service_provider_name` | string |  |
    | `backend_type` | string | <br>_Enum: `basic`, `email`, `atlassian`, `zammad`, `smax`_ |
    | `settings` | object (free-form) | Backend-specific configuration. |
    | `is_active` | boolean |  |
    | `webhook_secret` | string |  |
    | `notification_email` | string (email) | Primary email for notifications. |
    | `notify_on_new_ticket` | boolean |  |
    | `notify_on_comment` | boolean |  |
    | `notify_on_escalation` | boolean |  |
    | `notify_on_sla_warning` | boolean |  |
    | `health_status` | string |  |
    | `last_health_check` | string (date-time) |  |
    | `failed_routing_count` | integer |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/provider-helpdesks/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      service_provider="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.provider_helpdesk_request import ProviderHelpdeskRequest # (1)
    from waldur_api_client.api.provider_helpdesks import provider_helpdesks_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ProviderHelpdeskRequest(
        service_provider="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = provider_helpdesks_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ProviderHelpdeskRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/provider_helpdesk_request.py)
    2.  **API Source:** [`provider_helpdesks_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/provider_helpdesks/provider_helpdesks_update.py)

=== "TypeScript"

    ```typescript
    import { providerHelpdesksUpdate } from 'waldur-js-client';
    
    try {
      const response = await providerHelpdesksUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "service_provider": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `service_provider` | string (uuid) | ✓ |  |
    | `backend_type` | string |  | <br>_Enum: `basic`, `email`, `atlassian`, `zammad`, `smax`_ |
    | `settings` | object (free-form) |  | Backend-specific configuration. |
    | `is_active` | boolean |  |  |
    | `webhook_secret` | string |  |  |
    | `notification_email` | string (email) |  | Primary email for notifications. |
    | `notify_on_new_ticket` | boolean |  |  |
    | `notify_on_comment` | boolean |  |  |
    | `notify_on_escalation` | boolean |  |  |
    | `notify_on_sla_warning` | boolean |  |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `service_provider` | string (uuid) |  |
    | `service_provider_name` | string |  |
    | `backend_type` | string | <br>_Enum: `basic`, `email`, `atlassian`, `zammad`, `smax`_ |
    | `settings` | object (free-form) | Backend-specific configuration. |
    | `is_active` | boolean |  |
    | `webhook_secret` | string |  |
    | `notification_email` | string (email) | Primary email for notifications. |
    | `notify_on_new_ticket` | boolean |  |
    | `notify_on_comment` | boolean |  |
    | `notify_on_escalation` | boolean |  |
    | `notify_on_sla_warning` | boolean |  |
    | `health_status` | string |  |
    | `last_health_check` | string (date-time) |  |
    | `failed_routing_count` | integer |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/provider-helpdesks/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_provider_helpdesk_request import PatchedProviderHelpdeskRequest # (1)
    from waldur_api_client.api.provider_helpdesks import provider_helpdesks_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedProviderHelpdeskRequest()
    response = provider_helpdesks_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedProviderHelpdeskRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_provider_helpdesk_request.py)
    2.  **API Source:** [`provider_helpdesks_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/provider_helpdesks/provider_helpdesks_partial_update.py)

=== "TypeScript"

    ```typescript
    import { providerHelpdesksPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await providerHelpdesksPartialUpdate({
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
    | `service_provider` | string (uuid) |  |  |
    | `backend_type` | string |  | <br>_Enum: `basic`, `email`, `atlassian`, `zammad`, `smax`_ |
    | `settings` | object (free-form) |  | Backend-specific configuration. |
    | `is_active` | boolean |  |  |
    | `webhook_secret` | string |  |  |
    | `notification_email` | string (email) |  | Primary email for notifications. |
    | `notify_on_new_ticket` | boolean |  |  |
    | `notify_on_comment` | boolean |  |  |
    | `notify_on_escalation` | boolean |  |  |
    | `notify_on_sla_warning` | boolean |  |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `service_provider` | string (uuid) |  |
    | `service_provider_name` | string |  |
    | `backend_type` | string | <br>_Enum: `basic`, `email`, `atlassian`, `zammad`, `smax`_ |
    | `settings` | object (free-form) | Backend-specific configuration. |
    | `is_active` | boolean |  |
    | `webhook_secret` | string |  |
    | `notification_email` | string (email) | Primary email for notifications. |
    | `notify_on_new_ticket` | boolean |  |
    | `notify_on_comment` | boolean |  |
    | `notify_on_escalation` | boolean |  |
    | `notify_on_sla_warning` | boolean |  |
    | `health_status` | string |  |
    | `last_health_check` | string (date-time) |  |
    | `failed_routing_count` | integer |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/provider-helpdesks/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.provider_helpdesks import provider_helpdesks_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = provider_helpdesks_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`provider_helpdesks_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/provider_helpdesks/provider_helpdesks_destroy.py)

=== "TypeScript"

    ```typescript
    import { providerHelpdesksDestroy } from 'waldur-js-client';
    
    try {
      const response = await providerHelpdesksDestroy({
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


### Validate provider helpdesk backend connectivity


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/provider-helpdesks/a1b2c3d4-e5f6-7890-abcd-ef1234567890/validate/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.provider_helpdesks import provider_helpdesks_validate # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = provider_helpdesks_validate.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`provider_helpdesks_validate`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/provider_helpdesks/provider_helpdesks_validate.py)

=== "TypeScript"

    ```typescript
    import { providerHelpdesksValidate } from 'waldur-js-client';
    
    try {
      const response = await providerHelpdesksValidate({
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

    **`200`** - No response body
    

---
