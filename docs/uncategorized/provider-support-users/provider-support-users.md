# Provider Support Users

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/provider-support-users/` | [List Provider Support Users](#list-provider-support-users) |
| <span class="http-badge http-get">GET</span> | `/api/provider-support-users/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/provider-support-users/` | [Create](#create) |
| <span class="http-badge http-put">PUT</span> | `/api/provider-support-users/{uuid}/` | [Update](#update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/provider-support-users/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-delete">DELETE</span> | `/api/provider-support-users/{uuid}/` | [Delete](#delete) |
| **Other Actions** | | |
| <span class="http-badge http-get">GET</span> | `/api/provider-support-users/team_workload/` | [Get workload for all team members](#get-workload-for-all-team-members) |

---
## Core CRUD


### List Provider Support Users


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/provider-support-users/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.provider_support_users import provider_support_users_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = provider_support_users_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`provider_support_users_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/provider_support_users/provider_support_users_list.py)

=== "TypeScript"

    ```typescript
    import { providerSupportUsersList } from 'waldur-js-client';
    
    try {
      const response = await providerSupportUsersList({
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
    | `is_active` | boolean |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `provider_helpdesk_uuid` | string (uuid) |  |
    | `role` | string |  |
    | `user_full_name` | string | User full name contains |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `user` | string (uri) |  |
    | `user_full_name` | string |  |
    | `user_email` | string (email) |  |
    | `provider_helpdesk` | string (uuid) |  |
    | `role` | string | <br>_Enum: `agent`, `manager`_ |
    | `is_active` | boolean |  |
    | `skills` | array of strings | List of skill tags for routing. |
    | `max_open_tickets` | integer | Maximum number of open tickets this user can handle. |
    | `open_ticket_count` | integer |  |
    | `has_capacity` | boolean |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/provider-support-users/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.provider_support_users import provider_support_users_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = provider_support_users_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`provider_support_users_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/provider_support_users/provider_support_users_retrieve.py)

=== "TypeScript"

    ```typescript
    import { providerSupportUsersRetrieve } from 'waldur-js-client';
    
    try {
      const response = await providerSupportUsersRetrieve({
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
    | `user` | string (uri) |  |
    | `user_full_name` | string |  |
    | `user_email` | string (email) |  |
    | `provider_helpdesk` | string (uuid) |  |
    | `role` | string | <br>_Enum: `agent`, `manager`_ |
    | `is_active` | boolean |  |
    | `skills` | array of strings | List of skill tags for routing. |
    | `max_open_tickets` | integer | Maximum number of open tickets this user can handle. |
    | `open_ticket_count` | integer |  |
    | `has_capacity` | boolean |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/provider-support-users/ \
      Authorization:"Token YOUR_API_TOKEN" \
      user="https://api.example.com/api/user/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      provider_helpdesk="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.provider_support_user_request import ProviderSupportUserRequest # (1)
    from waldur_api_client.api.provider_support_users import provider_support_users_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ProviderSupportUserRequest(
        user="https://api.example.com/api/user/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        provider_helpdesk="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = provider_support_users_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ProviderSupportUserRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/provider_support_user_request.py)
    2.  **API Source:** [`provider_support_users_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/provider_support_users/provider_support_users_create.py)

=== "TypeScript"

    ```typescript
    import { providerSupportUsersCreate } from 'waldur-js-client';
    
    try {
      const response = await providerSupportUsersCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "user": "https://api.example.com/api/user/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "provider_helpdesk": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `user` | string (uri) | ✓ |  |
    | `provider_helpdesk` | string (uuid) | ✓ |  |
    | `role` | string |  | <br>_Enum: `agent`, `manager`_ |
    | `is_active` | boolean |  |  |
    | `skills` | array of strings |  | List of skill tags for routing. |
    | `max_open_tickets` | integer |  | Maximum number of open tickets this user can handle. |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `user` | string (uri) |  |
    | `user_full_name` | string |  |
    | `user_email` | string (email) |  |
    | `provider_helpdesk` | string (uuid) |  |
    | `role` | string | <br>_Enum: `agent`, `manager`_ |
    | `is_active` | boolean |  |
    | `skills` | array of strings | List of skill tags for routing. |
    | `max_open_tickets` | integer | Maximum number of open tickets this user can handle. |
    | `open_ticket_count` | integer |  |
    | `has_capacity` | boolean |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/provider-support-users/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      user="https://api.example.com/api/user/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      provider_helpdesk="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.provider_support_user_request import ProviderSupportUserRequest # (1)
    from waldur_api_client.api.provider_support_users import provider_support_users_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ProviderSupportUserRequest(
        user="https://api.example.com/api/user/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        provider_helpdesk="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = provider_support_users_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ProviderSupportUserRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/provider_support_user_request.py)
    2.  **API Source:** [`provider_support_users_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/provider_support_users/provider_support_users_update.py)

=== "TypeScript"

    ```typescript
    import { providerSupportUsersUpdate } from 'waldur-js-client';
    
    try {
      const response = await providerSupportUsersUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "user": "https://api.example.com/api/user/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "provider_helpdesk": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `user` | string (uri) | ✓ |  |
    | `provider_helpdesk` | string (uuid) | ✓ |  |
    | `role` | string |  | <br>_Enum: `agent`, `manager`_ |
    | `is_active` | boolean |  |  |
    | `skills` | array of strings |  | List of skill tags for routing. |
    | `max_open_tickets` | integer |  | Maximum number of open tickets this user can handle. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `user` | string (uri) |  |
    | `user_full_name` | string |  |
    | `user_email` | string (email) |  |
    | `provider_helpdesk` | string (uuid) |  |
    | `role` | string | <br>_Enum: `agent`, `manager`_ |
    | `is_active` | boolean |  |
    | `skills` | array of strings | List of skill tags for routing. |
    | `max_open_tickets` | integer | Maximum number of open tickets this user can handle. |
    | `open_ticket_count` | integer |  |
    | `has_capacity` | boolean |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/provider-support-users/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_provider_support_user_request import PatchedProviderSupportUserRequest # (1)
    from waldur_api_client.api.provider_support_users import provider_support_users_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedProviderSupportUserRequest()
    response = provider_support_users_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedProviderSupportUserRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_provider_support_user_request.py)
    2.  **API Source:** [`provider_support_users_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/provider_support_users/provider_support_users_partial_update.py)

=== "TypeScript"

    ```typescript
    import { providerSupportUsersPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await providerSupportUsersPartialUpdate({
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
    | `user` | string (uri) |  |  |
    | `provider_helpdesk` | string (uuid) |  |  |
    | `role` | string |  | <br>_Enum: `agent`, `manager`_ |
    | `is_active` | boolean |  |  |
    | `skills` | array of strings |  | List of skill tags for routing. |
    | `max_open_tickets` | integer |  | Maximum number of open tickets this user can handle. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `user` | string (uri) |  |
    | `user_full_name` | string |  |
    | `user_email` | string (email) |  |
    | `provider_helpdesk` | string (uuid) |  |
    | `role` | string | <br>_Enum: `agent`, `manager`_ |
    | `is_active` | boolean |  |
    | `skills` | array of strings | List of skill tags for routing. |
    | `max_open_tickets` | integer | Maximum number of open tickets this user can handle. |
    | `open_ticket_count` | integer |  |
    | `has_capacity` | boolean |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/provider-support-users/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.provider_support_users import provider_support_users_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = provider_support_users_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`provider_support_users_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/provider_support_users/provider_support_users_destroy.py)

=== "TypeScript"

    ```typescript
    import { providerSupportUsersDestroy } from 'waldur-js-client';
    
    try {
      const response = await providerSupportUsersDestroy({
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


### Get workload for all team members


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/provider-support-users/team_workload/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.provider_support_users import provider_support_users_team_workload_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = provider_support_users_team_workload_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`provider_support_users_team_workload_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/provider_support_users/provider_support_users_team_workload_list.py)

=== "TypeScript"

    ```typescript
    import { providerSupportUsersTeamWorkloadList } from 'waldur-js-client';
    
    try {
      const response = await providerSupportUsersTeamWorkloadList({
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
    | `is_active` | boolean |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `provider_helpdesk_uuid` | string (uuid) |  |
    | `role` | string |  |
    | `user_full_name` | string | User full name contains |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `user_full_name` | string |
    | `open_ticket_count` | integer |
    | `max_open_tickets` | integer |
    | `has_capacity` | boolean |

---
