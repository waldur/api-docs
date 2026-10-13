# Matrix

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/matrix/credentials/` | [Get Matrix login credentials](#get-matrix-login-credentials) |
| <span class="http-badge http-get">GET</span> | `/api/matrix/exports/{uuid}/download/{kind}/` | [Download a Matrix history export file](#download-a-matrix-history-export-file) |
| <span class="http-badge http-get">GET</span> | `/api/matrix/exports/` | [List Matrix Exports](#list-matrix-exports) |
| <span class="http-badge http-get">GET</span> | `/api/matrix/exports/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-get">GET</span> | `/api/matrix/rooms/eligible_projects/` | [List projects the caller can create a Matrix room for](#list-projects-the-caller-can-create-a-matrix-room-for) |
| <span class="http-badge http-get">GET</span> | `/api/matrix/rooms/` | [List Matrix Rooms](#list-matrix-rooms) |
| <span class="http-badge http-get">GET</span> | `/api/matrix/rooms/{uuid}/members/` | [List room members](#list-room-members) |
| <span class="http-badge http-get">GET</span> | `/api/matrix/rooms/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/matrix/credentials/password/` | [Generate a Matrix password](#generate-a-matrix-password) |
| <span class="http-badge http-post">POST</span> | `/api/matrix/credentials/recovery-key/` | [Show the recovery key of chat encryption](#show-the-recovery-key-of-chat-encryption) |
| <span class="http-badge http-post">POST</span> | `/api/matrix/crypto/escrow/` | [Escrow the recovery key of chat encryption](#escrow-the-recovery-key-of-chat-encryption) |
| <span class="http-badge http-post">POST</span> | `/api/matrix/crypto/lease/` | [Take the lease to set up or reset chat encryption](#take-the-lease-to-set-up-or-reset-chat-encryption) |
| <span class="http-badge http-post">POST</span> | `/api/matrix/crypto/lease/release/` | [Release the lease to set up or reset chat encryption](#release-the-lease-to-set-up-or-reset-chat-encryption) |
| <span class="http-badge http-post">POST</span> | `/api/matrix/rooms/` | [Create a Matrix room for a project](#create-a-matrix-room-for-a-project) |
| <span class="http-badge http-post">POST</span> | `/api/matrix/rooms/{uuid}/disable/` | [Disable an active chat room](#disable-an-active-chat-room) |
| <span class="http-badge http-post">POST</span> | `/api/matrix/rooms/{uuid}/export_history/` | [Trigger manual history export](#trigger-manual-history-export) |
| <span class="http-badge http-post">POST</span> | `/api/matrix/rooms/{uuid}/join/` | [Join a chat room as staff](#join-a-chat-room-as-staff) |
| <span class="http-badge http-post">POST</span> | `/api/matrix/rooms/{uuid}/leave/` | [Leave a chat room as staff](#leave-a-chat-room-as-staff) |
| <span class="http-badge http-post">POST</span> | `/api/matrix/rooms/{uuid}/open/` | [Open a chat room's conversation](#open-a-chat-rooms-conversation) |
| <span class="http-badge http-post">POST</span> | `/api/matrix/rooms/{uuid}/reactivate/` | [Re-enable an archived chat room](#re-enable-an-archived-chat-room) |
| <span class="http-badge http-post">POST</span> | `/api/matrix/rooms/{uuid}/retry/` | [Retry a stuck or failed room operation](#retry-a-stuck-or-failed-room-operation) |
| <span class="http-badge http-post">POST</span> | `/api/matrix/rooms/{uuid}/sync_members/` | [Force sync room membership with project members](#force-sync-room-membership-with-project-members) |
| <span class="http-badge http-post">POST</span> | `/api/matrix/session/` | [Start a Matrix web chat session](#start-a-matrix-web-chat-session) |
| <span class="http-badge http-delete">DELETE</span> | `/api/matrix/rooms/{uuid}/` | [Delete](#delete) |

---

### Get Matrix login credentials

Returns what an external Matrix client needs to sign the authenticated user in, per MATRIX_EXTERNAL_LOGIN_METHOD. Never a password or an access token: in password mode the user generates a password with POST /api/matrix/credentials/password/.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/matrix/credentials/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.matrix import matrix_credentials_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = matrix_credentials_retrieve.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`matrix_credentials_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/matrix/matrix_credentials_retrieve.py)

=== "TypeScript"

    ```typescript
    import { matrixCredentialsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await matrixCredentialsRetrieve({
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
    | `method` | string |
    | `homeserver_url` | string |
    | `matrix_user_id` | string |

---

### Download a Matrix history export file


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/matrix/exports/string-value/download/export/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.matrix import matrix_exports_download_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = matrix_exports_download_retrieve.sync(
        kind="export",
        uuid="string-value",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`matrix_exports_download_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/matrix/matrix_exports_download_retrieve.py)

=== "TypeScript"

    ```typescript
    import { matrixExportsDownloadRetrieve } from 'waldur-js-client';
    
    try {
      const response = await matrixExportsDownloadRetrieve({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "kind": "export",
        "uuid": "string-value"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required | Description |
    |---|---|---|---|
    | `kind` | string | ✓ | Which artifact to stream.<br>_Enum: `export`, `media`_ |
    | `uuid` | string | ✓ |  |


=== "Responses"

    **`200`** - 
    

---

### List Matrix Exports


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/matrix/exports/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.export_type_enum import ExportTypeEnum # (1)
    from waldur_api_client.models.matrix_history_export_state_enum import MatrixHistoryExportStateEnum # (2)
    from waldur_api_client.api.matrix import matrix_exports_list # (3)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = matrix_exports_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`ExportTypeEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/export_type_enum.py)
    2.  **Model Source:** [`MatrixHistoryExportStateEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/matrix_history_export_state_enum.py)
    3.  **API Source:** [`matrix_exports_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/matrix/matrix_exports_list.py)

=== "TypeScript"

    ```typescript
    import { matrixExportsList } from 'waldur-js-client';
    
    try {
      const response = await matrixExportsList({
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
    | `export_type` | string | _Enum: `periodic`, `on_deletion`, `manual`_ |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `room_uuid` | string (uuid) | Room UUID |
    | `state` | string | _Enum: `pending`, `exporting`, `completed`, `failed`_ |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `url` | string (uri) |
    | `room_uuid` | string (uuid) |
    | `room_name` | string |
    | `export_type` | any |
    | `message_count` | integer |
    | `media_count` | integer |
    | `state` | any |
    | `error_message` | string |
    | `export_file_url` | string |
    | `media_file_url` | string |
    | `started_at` | string (date-time) |
    | `completed_at` | string (date-time) |
    | `created` | string (date-time) |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/matrix/exports/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.matrix import matrix_exports_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = matrix_exports_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`matrix_exports_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/matrix/matrix_exports_retrieve.py)

=== "TypeScript"

    ```typescript
    import { matrixExportsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await matrixExportsRetrieve({
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
    | `url` | string (uri) |
    | `room_uuid` | string (uuid) |
    | `room_name` | string |
    | `export_type` | any |
    | `message_count` | integer |
    | `media_count` | integer |
    | `state` | any |
    | `error_message` | string |
    | `export_file_url` | string |
    | `media_file_url` | string |
    | `started_at` | string (date-time) |
    | `completed_at` | string (date-time) |
    | `created` | string (date-time) |

---

### List projects the caller can create a Matrix room for

Returns projects where the caller holds MATRIX_ROOM.CREATE on the project or its organization (staff and support see all) and no MatrixRoom row exists yet. Existing archived rooms still block creation, so projects with any room are excluded.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/matrix/rooms/eligible_projects/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.matrix_room_state_enum import MatrixRoomStateEnum # (1)
    from waldur_api_client.api.matrix import matrix_rooms_eligible_projects_list # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = matrix_rooms_eligible_projects_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`MatrixRoomStateEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/matrix_room_state_enum.py)
    2.  **API Source:** [`matrix_rooms_eligible_projects_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/matrix/matrix_rooms_eligible_projects_list.py)

=== "TypeScript"

    ```typescript
    import { matrixRoomsEligibleProjectsList } from 'waldur-js-client';
    
    try {
      const response = await matrixRoomsEligibleProjectsList({
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
    | `customer_uuid` | string | Limit results to projects under this customer. |
    | `member` | boolean | Only rooms the current user is a member of |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `project_uuid` | string (uuid) | Project UUID |
    | `state` | string | _Enum: `creating`, `active`, `disabling`, `archived`, `error`_ |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `uuid` | string |
    | `name` | string |
    | `customer_uuid` | string |
    | `customer_name` | string |

---

### List Matrix Rooms


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/matrix/rooms/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.matrix_room_state_enum import MatrixRoomStateEnum # (1)
    from waldur_api_client.api.matrix import matrix_rooms_list # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = matrix_rooms_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`MatrixRoomStateEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/matrix_room_state_enum.py)
    2.  **API Source:** [`matrix_rooms_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/matrix/matrix_rooms_list.py)

=== "TypeScript"

    ```typescript
    import { matrixRoomsList } from 'waldur-js-client';
    
    try {
      const response = await matrixRoomsList({
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
    | `member` | boolean | Only rooms the current user is a member of |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `project_uuid` | string (uuid) | Project UUID |
    | `state` | string | _Enum: `creating`, `active`, `disabling`, `archived`, `error`_ |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `room_id` | string | Matrix room ID, e.g. !abc:domain |
    | `room_name` | string |  |
    | `room_alias` | string | Matrix room alias, e.g. #project-name:domain |
    | `state` | any |  |
    | `error_message` | string |  |
    | `scope` | string |  |
    | `scope_uuid` | string |  |
    | `scope_name` | string |  |
    | `customer_uuid` | string |  |
    | `customer_name` | string |  |
    | `members_count` | integer |  |
    | `members` | array of objects |  |
    | `members.user_full_name` | string |  |
    | `members.matrix_user_id` | string |  |
    | `members.membership_state` | string |  |
    | `current_user_membership_state` | string |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### List room members


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/matrix/rooms/a1b2c3d4-e5f6-7890-abcd-ef1234567890/members/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.matrix_room_state_enum import MatrixRoomStateEnum # (1)
    from waldur_api_client.api.matrix import matrix_rooms_members_list # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = matrix_rooms_members_list.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`MatrixRoomStateEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/matrix_room_state_enum.py)
    2.  **API Source:** [`matrix_rooms_members_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/matrix/matrix_rooms_members_list.py)

=== "TypeScript"

    ```typescript
    import { matrixRoomsMembersList } from 'waldur-js-client';
    
    try {
      const response = await matrixRoomsMembersList({
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
    | `member` | boolean | Only rooms the current user is a member of |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `project_uuid` | string (uuid) | Project UUID |
    | `state` | string | _Enum: `creating`, `active`, `disabling`, `archived`, `error`_ |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `user_uuid` | string (uuid) |
    | `user_full_name` | string |
    | `user_image` | string (uri) |
    | `matrix_user_id` | string |
    | `power_level` | integer |
    | `membership_state` | any |
    | `created` | string (date-time) |
    | `modified` | string (date-time) |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/matrix/rooms/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.matrix import matrix_rooms_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = matrix_rooms_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`matrix_rooms_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/matrix/matrix_rooms_retrieve.py)

=== "TypeScript"

    ```typescript
    import { matrixRoomsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await matrixRoomsRetrieve({
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
    | `url` | string (uri) |  |
    | `room_id` | string | Matrix room ID, e.g. !abc:domain |
    | `room_name` | string |  |
    | `room_alias` | string | Matrix room alias, e.g. #project-name:domain |
    | `state` | any |  |
    | `error_message` | string |  |
    | `scope` | string |  |
    | `scope_uuid` | string |  |
    | `scope_name` | string |  |
    | `customer_uuid` | string |  |
    | `customer_name` | string |  |
    | `members_count` | integer |  |
    | `members` | array of objects |  |
    | `members.user_full_name` | string |  |
    | `members.matrix_user_id` | string |  |
    | `members.membership_state` | string |  |
    | `current_user_membership_state` | string |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Generate a Matrix password

Sets a new random password on the authenticated user's Matrix account and returns it. It is not stored, so it is shown only in this response; generating again replaces it. Only in password mode.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/matrix/credentials/password/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.matrix import matrix_credentials_password # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = matrix_credentials_password.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`matrix_credentials_password`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/matrix/matrix_credentials_password.py)

=== "TypeScript"

    ```typescript
    import { matrixCredentialsPassword } from 'waldur-js-client';
    
    try {
      const response = await matrixCredentialsPassword({
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
    | `homeserver_url` | string |
    | `matrix_user_id` | string |
    | `password` | string |
    
    ---
    
    **`403`** - The user was deactivated while the request ran.
    
    
    ---
    
    **`404`** - Matrix chat is not enabled.
    
    
    ---
    
    **`409`** - Matrix passwords are not in use.
    
    
    ---
    
    **`503`** - The homeserver did not set it: either the Waldur bot is not a homeserver admin yet, the homeserver's admin API is not reachable or the account is a homeserver admin's, which needs an operator, or the homeserver failed and a later try may succeed. The detail says which.
    

---

### Show the recovery key of chat encryption

Returns the caller's escrowed recovery key, so that another Matrix client, such as Element, can unlock their encrypted history. Only a key that opens the user's secret storage on the homeserver is returned; null otherwise. A POST, as each reveal is recorded in the user's event log.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/matrix/credentials/recovery-key/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.matrix import matrix_credentials_recovery_key # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = matrix_credentials_recovery_key.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`matrix_credentials_recovery_key`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/matrix/matrix_credentials_recovery_key.py)

=== "TypeScript"

    ```typescript
    import { matrixCredentialsRecoveryKey } from 'waldur-js-client';
    
    try {
      const response = await matrixCredentialsRecoveryKey({
      auth: "Token YOUR_API_TOKEN"
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `recovery_key` | string | The user's secret-storage recovery key, for unlocking chat history in another Matrix client. Null while Waldur holds no key that opens the user's secret storage. |
    
    ---
    
    **`403`** - Not the user's own sign-in: a personal or OIDC access token, or staff impersonating the user.
    
    
    ---
    
    **`404`** - Matrix chat is not enabled.
    
    
    ---
    
    **`503`** - The homeserver could not be asked.
    

---

### Escrow the recovery key of chat encryption

Stores the caller's new secret-storage recovery key. Only the holder of a current lease may; the drawer calls this before it uploads any key, so Waldur never loses a key the homeserver depends on.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/matrix/crypto/escrow/ \
      Authorization:"Token YOUR_API_TOKEN" \
      lease="string-value" \
      recovery_key="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.matrix_crypto_escrow_request import MatrixCryptoEscrowRequest # (1)
    from waldur_api_client.api.matrix import matrix_crypto_escrow # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = MatrixCryptoEscrowRequest(
        lease="string-value",
        recovery_key="string-value"
    )
    response = matrix_crypto_escrow.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`MatrixCryptoEscrowRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/matrix_crypto_escrow_request.py)
    2.  **API Source:** [`matrix_crypto_escrow`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/matrix/matrix_crypto_escrow.py)

=== "TypeScript"

    ```typescript
    import { matrixCryptoEscrow } from 'waldur-js-client';
    
    try {
      const response = await matrixCryptoEscrow({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "lease": "string-value",
        "recovery_key": "string-value"
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
    | `lease` | string | ✓ |
    | `recovery_key` | string | ✓ |


=== "Responses"

    **`204`** - No response body
    
    
    ---
    
    **`404`** - Matrix chat is not enabled.
    
    
    ---
    
    **`409`** - 
    
    | Field | Type |
    |---|---|
    | `state` | string |
    | `detail` | string |

---

### Take the lease to set up or reset chat encryption

Admits one browser at a time to setting up the caller's end-to-end encryption (`bootstrap`), or to replacing an identity Waldur can't unlock (`reset`). A reset also returns a temporary password for the homeserver's interactive auth; it is replaced once the new recovery key is escrowed, or when the lease runs out. 409 says why the request can't proceed: `set_up`, `locked` (set up without a key Waldur holds), `not_locked`, or `in_progress` (with Retry-After).


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/matrix/crypto/lease/ \
      Authorization:"Token YOUR_API_TOKEN" \
      kind="bootstrap"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.matrix_crypto_lease_request_request import MatrixCryptoLeaseRequestRequest # (1)
    from waldur_api_client.api.matrix import matrix_crypto_lease # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = MatrixCryptoLeaseRequestRequest(
        kind="bootstrap"
    )
    response = matrix_crypto_lease.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`MatrixCryptoLeaseRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/matrix_crypto_lease_request_request.py)
    2.  **API Source:** [`matrix_crypto_lease`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/matrix/matrix_crypto_lease.py)

=== "TypeScript"

    ```typescript
    import { matrixCryptoLease } from 'waldur-js-client';
    
    try {
      const response = await matrixCryptoLease({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "kind": "bootstrap"
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
    | `kind` | string | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `lease` | string |  |
    | `expires_at` | string (date-time) |  |
    | `temporary_password` | string | For a reset only: the password to answer the homeserver's interactive auth with. Replaced once the new key is escrowed. |
    
    ---
    
    **`404`** - Matrix chat is not enabled.
    
    
    ---
    
    **`409`** - 
    
    | Field | Type |
    |---|---|
    | `state` | string |
    | `detail` | string |
    
    ---
    
    **`503`** - The homeserver could not be asked, or the bot is not a homeserver admin (needed for a reset).
    

---

### Release the lease to set up or reset chat encryption

Ends the caller's lease once its setup or reset is done, or has failed, so another window need not wait for it to run out. A lease that is no longer held is ignored.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/matrix/crypto/lease/release/ \
      Authorization:"Token YOUR_API_TOKEN" \
      lease="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.matrix_crypto_lease_release_request import MatrixCryptoLeaseReleaseRequest # (1)
    from waldur_api_client.api.matrix import matrix_crypto_lease_release # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = MatrixCryptoLeaseReleaseRequest(
        lease="string-value"
    )
    response = matrix_crypto_lease_release.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`MatrixCryptoLeaseReleaseRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/matrix_crypto_lease_release_request.py)
    2.  **API Source:** [`matrix_crypto_lease_release`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/matrix/matrix_crypto_lease_release.py)

=== "TypeScript"

    ```typescript
    import { matrixCryptoLeaseRelease } from 'waldur-js-client';
    
    try {
      const response = await matrixCryptoLeaseRelease({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "lease": "string-value"
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
    | `lease` | string | ✓ |


=== "Responses"

    **`204`** - No response body
    
    
    ---
    
    **`404`** - Chat disabled.
    

---

### Create a Matrix room for a project


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/matrix/rooms/ \
      Authorization:"Token YOUR_API_TOKEN" \
      project="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.matrix_room_create_request import MatrixRoomCreateRequest # (1)
    from waldur_api_client.api.matrix import matrix_rooms_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = MatrixRoomCreateRequest(
        project="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = matrix_rooms_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`MatrixRoomCreateRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/matrix_room_create_request.py)
    2.  **API Source:** [`matrix_rooms_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/matrix/matrix_rooms_create.py)

=== "TypeScript"

    ```typescript
    import { matrixRoomsCreate } from 'waldur-js-client';
    
    try {
      const response = await matrixRoomsCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "project": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `project` | string (uuid) | ✓ |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `room_id` | string | Matrix room ID, e.g. !abc:domain |
    | `room_name` | string |  |
    | `room_alias` | string | Matrix room alias, e.g. #project-name:domain |
    | `state` | any |  |
    | `error_message` | string |  |
    | `scope` | string |  |
    | `scope_uuid` | string |  |
    | `scope_name` | string |  |
    | `customer_uuid` | string |  |
    | `customer_name` | string |  |
    | `members_count` | integer |  |
    | `members` | array of objects |  |
    | `members.user_full_name` | string |  |
    | `members.matrix_user_id` | string |  |
    | `members.membership_state` | string |  |
    | `current_user_membership_state` | string |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Disable an active chat room


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/matrix/rooms/a1b2c3d4-e5f6-7890-abcd-ef1234567890/disable/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.matrix_room_disable_request import MatrixRoomDisableRequest # (1)
    from waldur_api_client.api.matrix import matrix_rooms_disable # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = MatrixRoomDisableRequest()
    response = matrix_rooms_disable.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`MatrixRoomDisableRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/matrix_room_disable_request.py)
    2.  **API Source:** [`matrix_rooms_disable`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/matrix/matrix_rooms_disable.py)

=== "TypeScript"

    ```typescript
    import { matrixRoomsDisable } from 'waldur-js-client';
    
    try {
      const response = await matrixRoomsDisable({
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
    | `delete_history` | boolean |  |


=== "Responses"

    **`202`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `room_id` | string | Matrix room ID, e.g. !abc:domain |
    | `room_name` | string |  |
    | `room_alias` | string | Matrix room alias, e.g. #project-name:domain |
    | `state` | any |  |
    | `error_message` | string |  |
    | `scope` | string |  |
    | `scope_uuid` | string |  |
    | `scope_name` | string |  |
    | `customer_uuid` | string |  |
    | `customer_name` | string |  |
    | `members_count` | integer |  |
    | `members` | array of objects |  |
    | `members.user_full_name` | string |  |
    | `members.matrix_user_id` | string |  |
    | `members.membership_state` | string |  |
    | `current_user_membership_state` | string |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Trigger manual history export


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/matrix/rooms/a1b2c3d4-e5f6-7890-abcd-ef1234567890/export_history/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.matrix import matrix_rooms_export_history # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = matrix_rooms_export_history.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`matrix_rooms_export_history`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/matrix/matrix_rooms_export_history.py)

=== "TypeScript"

    ```typescript
    import { matrixRoomsExportHistory } from 'waldur-js-client';
    
    try {
      const response = await matrixRoomsExportHistory({
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
    | `url` | string (uri) |
    | `room_uuid` | string (uuid) |
    | `room_name` | string |
    | `export_type` | any |
    | `message_count` | integer |
    | `media_count` | integer |
    | `state` | any |
    | `error_message` | string |
    | `export_file_url` | string |
    | `media_file_url` | string |
    | `started_at` | string (date-time) |
    | `completed_at` | string (date-time) |
    | `created` | string (date-time) |
    
    ---
    
    **`202`** - 
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `url` | string (uri) |
    | `room_uuid` | string (uuid) |
    | `room_name` | string |
    | `export_type` | any |
    | `message_count` | integer |
    | `media_count` | integer |
    | `state` | any |
    | `error_message` | string |
    | `export_file_url` | string |
    | `media_file_url` | string |
    | `started_at` | string (date-time) |
    | `completed_at` | string (date-time) |
    | `created` | string (date-time) |

---

### Join a chat room as staff

Staff self-join: provisions the caller, adds them with a Moderator badge (power level 50), and posts a bot announcement.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/matrix/rooms/a1b2c3d4-e5f6-7890-abcd-ef1234567890/join/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.matrix import matrix_rooms_join # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = matrix_rooms_join.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`matrix_rooms_join`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/matrix/matrix_rooms_join.py)

=== "TypeScript"

    ```typescript
    import { matrixRoomsJoin } from 'waldur-js-client';
    
    try {
      const response = await matrixRoomsJoin({
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
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `room_id` | string | Matrix room ID, e.g. !abc:domain |
    | `room_name` | string |  |
    | `room_alias` | string | Matrix room alias, e.g. #project-name:domain |
    | `state` | any |  |
    | `error_message` | string |  |
    | `scope` | string |  |
    | `scope_uuid` | string |  |
    | `scope_name` | string |  |
    | `customer_uuid` | string |  |
    | `customer_name` | string |  |
    | `members_count` | integer |  |
    | `members` | array of objects |  |
    | `members.user_full_name` | string |  |
    | `members.matrix_user_id` | string |  |
    | `members.membership_state` | string |  |
    | `current_user_membership_state` | string |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Leave a chat room as staff

Staff self-leave: posts a bot announcement and removes the caller from the room.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/matrix/rooms/a1b2c3d4-e5f6-7890-abcd-ef1234567890/leave/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.matrix import matrix_rooms_leave # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = matrix_rooms_leave.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`matrix_rooms_leave`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/matrix/matrix_rooms_leave.py)

=== "TypeScript"

    ```typescript
    import { matrixRoomsLeave } from 'waldur-js-client';
    
    try {
      const response = await matrixRoomsLeave({
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
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `room_id` | string | Matrix room ID, e.g. !abc:domain |
    | `room_name` | string |  |
    | `room_alias` | string | Matrix room alias, e.g. #project-name:domain |
    | `state` | any |  |
    | `error_message` | string |  |
    | `scope` | string |  |
    | `scope_uuid` | string |  |
    | `scope_name` | string |  |
    | `customer_uuid` | string |  |
    | `customer_name` | string |  |
    | `members_count` | integer |  |
    | `members` | array of objects |  |
    | `members.user_full_name` | string |  |
    | `members.matrix_user_id` | string |  |
    | `members.membership_state` | string |  |
    | `current_user_membership_state` | string |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Open a chat room's conversation

Returns the Matrix room ID to a current member of the room, accepting their pending invite. Other callers get 403; a room that is not active gets 409.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/matrix/rooms/a1b2c3d4-e5f6-7890-abcd-ef1234567890/open/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.matrix import matrix_rooms_open # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = matrix_rooms_open.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`matrix_rooms_open`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/matrix/matrix_rooms_open.py)

=== "TypeScript"

    ```typescript
    import { matrixRoomsOpen } from 'waldur-js-client';
    
    try {
      const response = await matrixRoomsOpen({
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
    | `room_id` | string |
    
    ---
    
    **`403`** - The caller is not a member of the room.
    
    
    ---
    
    **`409`** - The room is not active.
    

---

### Re-enable an archived chat room


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/matrix/rooms/a1b2c3d4-e5f6-7890-abcd-ef1234567890/reactivate/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.matrix import matrix_rooms_reactivate # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = matrix_rooms_reactivate.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`matrix_rooms_reactivate`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/matrix/matrix_rooms_reactivate.py)

=== "TypeScript"

    ```typescript
    import { matrixRoomsReactivate } from 'waldur-js-client';
    
    try {
      const response = await matrixRoomsReactivate({
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
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `room_id` | string | Matrix room ID, e.g. !abc:domain |
    | `room_name` | string |  |
    | `room_alias` | string | Matrix room alias, e.g. #project-name:domain |
    | `state` | any |  |
    | `error_message` | string |  |
    | `scope` | string |  |
    | `scope_uuid` | string |  |
    | `scope_name` | string |  |
    | `customer_uuid` | string |  |
    | `customer_name` | string |  |
    | `members_count` | integer |  |
    | `members` | array of objects |  |
    | `members.user_full_name` | string |  |
    | `members.matrix_user_id` | string |  |
    | `members.membership_state` | string |  |
    | `current_user_membership_state` | string |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Retry a stuck or failed room operation


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/matrix/rooms/a1b2c3d4-e5f6-7890-abcd-ef1234567890/retry/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.matrix import matrix_rooms_retry # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = matrix_rooms_retry.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`matrix_rooms_retry`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/matrix/matrix_rooms_retry.py)

=== "TypeScript"

    ```typescript
    import { matrixRoomsRetry } from 'waldur-js-client';
    
    try {
      const response = await matrixRoomsRetry({
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
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `room_id` | string | Matrix room ID, e.g. !abc:domain |
    | `room_name` | string |  |
    | `room_alias` | string | Matrix room alias, e.g. #project-name:domain |
    | `state` | any |  |
    | `error_message` | string |  |
    | `scope` | string |  |
    | `scope_uuid` | string |  |
    | `scope_name` | string |  |
    | `customer_uuid` | string |  |
    | `customer_name` | string |  |
    | `members_count` | integer |  |
    | `members` | array of objects |  |
    | `members.user_full_name` | string |  |
    | `members.matrix_user_id` | string |  |
    | `members.membership_state` | string |  |
    | `current_user_membership_state` | string |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Force sync room membership with project members


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/matrix/rooms/a1b2c3d4-e5f6-7890-abcd-ef1234567890/sync_members/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.matrix import matrix_rooms_sync_members # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = matrix_rooms_sync_members.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`matrix_rooms_sync_members`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/matrix/matrix_rooms_sync_members.py)

=== "TypeScript"

    ```typescript
    import { matrixRoomsSyncMembers } from 'waldur-js-client';
    
    try {
      const response = await matrixRoomsSyncMembers({
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

    **`202`** - No response body
    

---

### Start a Matrix web chat session

Signs the caller in to Matrix on a new web device and returns short-lived tokens for the chat drawer. The tokens are not stored.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/matrix/session/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.matrix import matrix_session # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = matrix_session.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`matrix_session`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/matrix/matrix_session.py)

=== "TypeScript"

    ```typescript
    import { matrixSession } from 'waldur-js-client';
    
    try {
      const response = await matrixSession({
      auth: "Token YOUR_API_TOKEN"
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `homeserver_url` | string |  |
    | `matrix_user_id` | string |  |
    | `device_id` | string |  |
    | `access_token` | string |  |
    | `refresh_token` | string |  |
    | `expires_in_ms` | integer |  |
    | `recovery_key` | string | The user's secret-storage recovery key, or null before encryption is set up. Only ever returned to its owner. |
    
    ---
    
    **`404`** - Matrix chat is not enabled.
    
    
    ---
    
    **`503`** - The homeserver could not start a session: either it failed and a later try may succeed, or the user's Matrix account is locked, which needs an operator. The detail says which.
    

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/matrix/rooms/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.matrix import matrix_rooms_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = matrix_rooms_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`matrix_rooms_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/matrix/matrix_rooms_destroy.py)

=== "TypeScript"

    ```typescript
    import { matrixRoomsDestroy } from 'waldur-js-client';
    
    try {
      const response = await matrixRoomsDestroy({
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
