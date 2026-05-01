# Role Availabilities

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/role-availabilities/` | [List Role Availabilities](#list-role-availabilities) |
| <span class="http-badge http-get">GET</span> | `/api/role-availabilities/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-delete">DELETE</span> | `/api/role-availabilities/{uuid}/` | [Delete](#delete) |

---

### List Role Availabilities


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/role-availabilities/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.role_availabilities import role_availabilities_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = role_availabilities_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`role_availabilities_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/role_availabilities/role_availabilities_list.py)

=== "TypeScript"

    ```typescript
    import { roleAvailabilitiesList } from 'waldur-js-client';
    
    try {
      const response = await roleAvailabilitiesList({
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
    | `object_id` | integer | Scope object id |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `role_name` | string | Role name contains |
    | `role_uuid` | string (uuid) | Role UUID |
    | `scope_type` | string | Scope content type (e.g. 'offering', 'customer') |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `role_uuid` | string (uuid) |
    | `role_name` | string |
    | `role_content_type` | string |
    | `scope_type` | string |
    | `scope_uuid` | string |
    | `scope_name` | string |
    | `is_profile_managed` | boolean |
    | `profile_uuid` | string |
    | `profile_name` | string |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/role-availabilities/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.role_availabilities import role_availabilities_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = role_availabilities_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`role_availabilities_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/role_availabilities/role_availabilities_retrieve.py)

=== "TypeScript"

    ```typescript
    import { roleAvailabilitiesRetrieve } from 'waldur-js-client';
    
    try {
      const response = await roleAvailabilitiesRetrieve({
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
    | `role_uuid` | string (uuid) |
    | `role_name` | string |
    | `role_content_type` | string |
    | `scope_type` | string |
    | `scope_uuid` | string |
    | `scope_name` | string |
    | `is_profile_managed` | boolean |
    | `profile_uuid` | string |
    | `profile_name` | string |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/role-availabilities/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.role_availabilities import role_availabilities_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = role_availabilities_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`role_availabilities_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/role_availabilities/role_availabilities_destroy.py)

=== "TypeScript"

    ```typescript
    import { roleAvailabilitiesDestroy } from 'waldur-js-client';
    
    try {
      const response = await roleAvailabilitiesDestroy({
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
