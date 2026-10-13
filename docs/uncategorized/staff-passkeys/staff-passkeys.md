# Staff Passkeys

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/staff-passkeys/` | [List Staff Passkeys](#list-staff-passkeys) |
| **Other Actions** | | |
| <span class="http-badge http-post">POST</span> | `/api/staff-passkeys/{uuid}/revoke/` | [Revoke another user's passkey](#revoke-another-users-passkey) |

---
## Core CRUD


### List Staff Passkeys


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/staff-passkeys/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.staff_passkeys import staff_passkeys_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = staff_passkeys_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`staff_passkeys_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/staff_passkeys/staff_passkeys_list.py)

=== "TypeScript"

    ```typescript
    import { staffPasskeysList } from 'waldur-js-client';
    
    try {
      const response = await staffPasskeysList({
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
    | `aaguid` | string |  |
    | `transports` | object (free-form) |  |
    | `attachment` | any |  |
    | `rp_id` | string |  |
    | `is_backup_eligible` | boolean |  |
    | `is_backed_up` | boolean |  |
    | `is_discoverable` | boolean |  |
    | `is_user_verified` | boolean |  |
    | `is_orphaned` | boolean |  |
    | `created` | string (date-time) |  |
    | `last_used_at` | string (date-time) |  |
    | `use_count` | integer |  |
    | `is_active` | boolean |  |
    | `revoked_at` | string (date-time) |  |
    | `revoked_by_username` | string | Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters |
    | `revocation_reason` | string |  |

---

## Other Actions


### Revoke another user's passkey


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/staff-passkeys/a1b2c3d4-e5f6-7890-abcd-ef1234567890/revoke/ \
      Authorization:"Token YOUR_API_TOKEN" \
      reason="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.passkey_staff_revoke_request import PasskeyStaffRevokeRequest # (1)
    from waldur_api_client.api.staff_passkeys import staff_passkeys_revoke # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PasskeyStaffRevokeRequest(
        reason="string-value"
    )
    response = staff_passkeys_revoke.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PasskeyStaffRevokeRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/passkey_staff_revoke_request.py)
    2.  **API Source:** [`staff_passkeys_revoke`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/staff_passkeys/staff_passkeys_revoke.py)

=== "TypeScript"

    ```typescript
    import { staffPasskeysRevoke } from 'waldur-js-client';
    
    try {
      const response = await staffPasskeysRevoke({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "reason": "string-value"
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
    | `reason` | string | ✓ |


=== "Responses"

    **`204`** - No response body
    

---
