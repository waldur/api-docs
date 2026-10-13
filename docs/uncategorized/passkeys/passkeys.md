# Passkeys

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/passkeys/` | [List Passkeys](#list-passkeys) |
| <span class="http-badge http-get">GET</span> | `/api/passkeys/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-put">PUT</span> | `/api/passkeys/{uuid}/` | [Update](#update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/passkeys/{uuid}/` | [Partial Update](#partial-update) |
| **Other Actions** | | |
| <span class="http-badge http-post">POST</span> | `/api/passkeys/mfa/begin/` | [Begin the passkey second factor](#begin-the-passkey-second-factor) |
| <span class="http-badge http-post">POST</span> | `/api/passkeys/mfa/finish/` | [Finish the passkey second factor](#finish-the-passkey-second-factor) |
| <span class="http-badge http-post">POST</span> | `/api/passkeys/registration/begin/` | [Begin passkey registration](#begin-passkey-registration) |
| <span class="http-badge http-post">POST</span> | `/api/passkeys/registration/finish/` | [Finish passkey registration](#finish-passkey-registration) |
| <span class="http-badge http-post">POST</span> | `/api/passkeys/{uuid}/revoke/` | [Revoke a passkey](#revoke-a-passkey) |
| <span class="http-badge http-post">POST</span> | `/api/passkeys/signin/begin/` | [Begin passwordless passkey sign-in](#begin-passwordless-passkey-sign-in) |
| <span class="http-badge http-post">POST</span> | `/api/passkeys/signin/finish/` | [Finish passwordless passkey sign-in](#finish-passwordless-passkey-sign-in) |

---
## Core CRUD


### List Passkeys


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/passkeys/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.passkeys import passkeys_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = passkeys_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`passkeys_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/passkeys/passkeys_list.py)

=== "TypeScript"

    ```typescript
    import { passkeysList } from 'waldur-js-client';
    
    try {
      const response = await passkeysList({
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

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/passkeys/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.passkeys import passkeys_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = passkeys_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`passkeys_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/passkeys/passkeys_retrieve.py)

=== "TypeScript"

    ```typescript
    import { passkeysRetrieve } from 'waldur-js-client';
    
    try {
      const response = await passkeysRetrieve({
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

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/passkeys/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-passkey"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.passkey_credential_update_request import PasskeyCredentialUpdateRequest # (1)
    from waldur_api_client.api.passkeys import passkeys_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PasskeyCredentialUpdateRequest(
        name="my-awesome-passkey"
    )
    response = passkeys_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PasskeyCredentialUpdateRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/passkey_credential_update_request.py)
    2.  **API Source:** [`passkeys_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/passkeys/passkeys_update.py)

=== "TypeScript"

    ```typescript
    import { passkeysUpdate } from 'waldur-js-client';
    
    try {
      const response = await passkeysUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "name": "my-awesome-passkey"
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
    | `name` | string | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `name` | string |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/passkeys/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_passkey_credential_update_request import PatchedPasskeyCredentialUpdateRequest # (1)
    from waldur_api_client.api.passkeys import passkeys_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedPasskeyCredentialUpdateRequest()
    response = passkeys_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedPasskeyCredentialUpdateRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_passkey_credential_update_request.py)
    2.  **API Source:** [`passkeys_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/passkeys/passkeys_partial_update.py)

=== "TypeScript"

    ```typescript
    import { passkeysPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await passkeysPartialUpdate({
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
    | `name` | string |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `name` | string |

---

## Other Actions


### Begin the passkey second factor


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/passkeys/mfa/begin/ \
      Authorization:"Token YOUR_API_TOKEN" \
      ceremony="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.passkey_mfa_begin_request import PasskeyMfaBeginRequest # (1)
    from waldur_api_client.api.passkeys import passkeys_mfa_begin # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PasskeyMfaBeginRequest(
        ceremony="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = passkeys_mfa_begin.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PasskeyMfaBeginRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/passkey_mfa_begin_request.py)
    2.  **API Source:** [`passkeys_mfa_begin`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/passkeys/passkeys_mfa_begin.py)

=== "TypeScript"

    ```typescript
    import { passkeysMfaBegin } from 'waldur-js-client';
    
    try {
      const response = await passkeysMfaBegin({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "ceremony": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `ceremony` | string (uuid) | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `ceremony` | string (uuid) |
    | `options` | object (free-form) |

---

### Finish the passkey second factor


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/passkeys/mfa/finish/ \
      Authorization:"Token YOUR_API_TOKEN" \
      ceremony="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      credential:='{}'
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.passkey_assertion_finish_request import PasskeyAssertionFinishRequest # (1)
    from waldur_api_client.api.passkeys import passkeys_mfa_finish # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PasskeyAssertionFinishRequest(
        ceremony="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        credential={}
    )
    response = passkeys_mfa_finish.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PasskeyAssertionFinishRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/passkey_assertion_finish_request.py)
    2.  **API Source:** [`passkeys_mfa_finish`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/passkeys/passkeys_mfa_finish.py)

=== "TypeScript"

    ```typescript
    import { passkeysMfaFinish } from 'waldur-js-client';
    
    try {
      const response = await passkeysMfaFinish({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "ceremony": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "credential": {}
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
    | `ceremony` | string (uuid) | ✓ |
    | `credential` | object (free-form) | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `token` | string |

---

### Begin passkey registration


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/passkeys/registration/begin/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.passkeys import passkeys_registration_begin # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = passkeys_registration_begin.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`passkeys_registration_begin`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/passkeys/passkeys_registration_begin.py)

=== "TypeScript"

    ```typescript
    import { passkeysRegistrationBegin } from 'waldur-js-client';
    
    try {
      const response = await passkeysRegistrationBegin({
      auth: "Token YOUR_API_TOKEN"
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `ceremony` | string (uuid) |
    | `options` | object (free-form) |

---

### Finish passkey registration


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/passkeys/registration/finish/ \
      Authorization:"Token YOUR_API_TOKEN" \
      ceremony="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      name="my-awesome-passkeys-registration-finish" \
      credential:='{}'
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.passkey_registration_finish_request import PasskeyRegistrationFinishRequest # (1)
    from waldur_api_client.api.passkeys import passkeys_registration_finish # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PasskeyRegistrationFinishRequest(
        ceremony="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        name="my-awesome-passkeys-registration-finish",
        credential={}
    )
    response = passkeys_registration_finish.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PasskeyRegistrationFinishRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/passkey_registration_finish_request.py)
    2.  **API Source:** [`passkeys_registration_finish`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/passkeys/passkeys_registration_finish.py)

=== "TypeScript"

    ```typescript
    import { passkeysRegistrationFinish } from 'waldur-js-client';
    
    try {
      const response = await passkeysRegistrationFinish({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "ceremony": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "name": "my-awesome-passkeys-registration-finish",
        "credential": {}
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
    | `ceremony` | string (uuid) | ✓ |
    | `name` | string | ✓ |
    | `credential` | object (free-form) | ✓ |


=== "Responses"

    **`201`** - 
    
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

### Revoke a passkey


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/passkeys/a1b2c3d4-e5f6-7890-abcd-ef1234567890/revoke/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.passkey_revoke_request import PasskeyRevokeRequest # (1)
    from waldur_api_client.api.passkeys import passkeys_revoke # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PasskeyRevokeRequest()
    response = passkeys_revoke.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PasskeyRevokeRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/passkey_revoke_request.py)
    2.  **API Source:** [`passkeys_revoke`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/passkeys/passkeys_revoke.py)

=== "TypeScript"

    ```typescript
    import { passkeysRevoke } from 'waldur-js-client';
    
    try {
      const response = await passkeysRevoke({
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
    | `reason` | string |  |


=== "Responses"

    **`204`** - No response body
    

---

### Begin passwordless passkey sign-in


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/passkeys/signin/begin/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.passkeys import passkeys_signin_begin # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = passkeys_signin_begin.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`passkeys_signin_begin`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/passkeys/passkeys_signin_begin.py)

=== "TypeScript"

    ```typescript
    import { passkeysSigninBegin } from 'waldur-js-client';
    
    try {
      const response = await passkeysSigninBegin({
      auth: "Token YOUR_API_TOKEN"
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `ceremony` | string (uuid) |
    | `options` | object (free-form) |

---

### Finish passwordless passkey sign-in


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/passkeys/signin/finish/ \
      Authorization:"Token YOUR_API_TOKEN" \
      ceremony="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      credential:='{}'
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.passkey_assertion_finish_request import PasskeyAssertionFinishRequest # (1)
    from waldur_api_client.api.passkeys import passkeys_signin_finish # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PasskeyAssertionFinishRequest(
        ceremony="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        credential={}
    )
    response = passkeys_signin_finish.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PasskeyAssertionFinishRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/passkey_assertion_finish_request.py)
    2.  **API Source:** [`passkeys_signin_finish`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/passkeys/passkeys_signin_finish.py)

=== "TypeScript"

    ```typescript
    import { passkeysSigninFinish } from 'waldur-js-client';
    
    try {
      const response = await passkeysSigninFinish({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "ceremony": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "credential": {}
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
    | `ceremony` | string (uuid) | ✓ |
    | `credential` | object (free-form) | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `token` | string |

---
