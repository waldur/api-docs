# Admin

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/admin/matrix-appservice/status/` | [Get Matrix appservice status](#get-matrix-appservice-status) |
| <span class="http-badge http-get">GET</span> | `/api/admin/matrix/diagnostics/` | [Run Matrix connectivity diagnostics](#run-matrix-connectivity-diagnostics) |
| <span class="http-badge http-get">GET</span> | `/api/admin/matrix/livekit/overview/` | [Get LiveKit calls overview](#get-livekit-calls-overview) |
| <span class="http-badge http-get">GET</span> | `/api/admin/matrix/livekit/participants/` | [List participants in a LiveKit room](#list-participants-in-a-livekit-room) |
| <span class="http-badge http-post">POST</span> | `/api/admin/matrix-appservice/setup/` | [Setup Matrix appservice registration](#setup-matrix-appservice-registration) |
| <span class="http-badge http-post">POST</span> | `/api/admin/matrix/reprovision/` | [Reprovision all active Matrix rooms on a new homeserver](#reprovision-all-active-matrix-rooms-on-a-new-homeserver) |

---

### Get Matrix appservice status

Returns the current appservice configuration state.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/admin/matrix-appservice/status/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.admin import admin_matrix_appservice_status_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = admin_matrix_appservice_status_retrieve.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`admin_matrix_appservice_status_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_matrix_appservice_status_retrieve.py)

=== "TypeScript"

    ```typescript
    import { adminMatrixAppserviceStatusRetrieve } from 'waldur-js-client';
    
    try {
      const response = await adminMatrixAppserviceStatusRetrieve({
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
    | `enabled` | boolean |
    | `as_token_configured` | boolean |
    | `hs_token_configured` | boolean |
    | `sender_localpart` | string |
    | `tokens_managed_by` | string |
    | `bot_user_id` | string |
    | `webhook_path` | string |
    | `homeserver_url` | string |
    | `homeserver_domain` | string |
    | `transaction_count` | integer |

---

### Run Matrix connectivity diagnostics

Performs live connectivity checks against the configured Matrix homeserver and returns results for each check.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/admin/matrix/diagnostics/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.admin import admin_matrix_diagnostics_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = admin_matrix_diagnostics_retrieve.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`admin_matrix_diagnostics_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_matrix_diagnostics_retrieve.py)

=== "TypeScript"

    ```typescript
    import { adminMatrixDiagnosticsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await adminMatrixDiagnosticsRetrieve({
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
    | `ok` | boolean |  |
    | `checks` | array of objects |  |
    | `checks.name` | string |  |
    | `checks.label` | string |  |
    | `checks.ok` | boolean |  |
    | `checks.detail` | string |  |
    | `checks.metrics` | object (free-form) | The check's numbers, for monitoring: {"round_trip_ms": 12} for appservice_ping, {"failed": 2} for history_exports and {"4xx": 3, "5xx": 0} for webhook_errors. Absent on other checks, and on appservice_ping when the ping failed. |

---

### Get LiveKit calls overview

Point-in-time snapshot of active LiveKit rooms with participant/publisher totals. Staff only. Returns 503 when LiveKit credentials are not configured and 502 when LiveKit is unreachable or rejects the configured credentials.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/admin/matrix/livekit/overview/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.admin import admin_matrix_livekit_overview_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = admin_matrix_livekit_overview_retrieve.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`admin_matrix_livekit_overview_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_matrix_livekit_overview_retrieve.py)

=== "TypeScript"

    ```typescript
    import { adminMatrixLivekitOverviewRetrieve } from 'waldur-js-client';
    
    try {
      const response = await adminMatrixLivekitOverviewRetrieve({
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
    | `rooms` | array of objects |
    | `rooms.sid` | string |
    | `rooms.name` | string |
    | `rooms.num_participants` | integer |
    | `rooms.num_publishers` | integer |
    | `rooms.creation_time` | integer |
    | `rooms.max_participants` | integer |
    | `rooms.metadata` | string |
    | `totals` | object |
    | `totals.room_count` | integer |
    | `totals.participant_count` | integer |
    | `totals.publisher_count` | integer |
    | `livekit_url` | string |

---

### List participants in a LiveKit room

Participants and their tracks for a single LiveKit room. Staff only. An unknown or empty room returns 200 with an empty list. Returns 503 when LiveKit credentials are not configured and 502 when LiveKit is unreachable or rejects the configured credentials.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/admin/matrix/livekit/participants/ \
      Authorization:"Token YOUR_API_TOKEN" \
      room=="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.admin import admin_matrix_livekit_participants_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = admin_matrix_livekit_participants_list.sync(
        client=client,
        room="string-value"
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`admin_matrix_livekit_participants_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_matrix_livekit_participants_list.py)

=== "TypeScript"

    ```typescript
    import { adminMatrixLivekitParticipantsList } from 'waldur-js-client';
    
    try {
      const response = await adminMatrixLivekitParticipantsList({
      auth: "Token YOUR_API_TOKEN",
      query: {
        "room": "string-value"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Query Parameters"

    | Name | Type | Required | Description |
    |---|---|---|---|
    | `room` | string | ✓ | LiveKit room name. A query parameter rather than a path segment because Element Call room names are base64 and routinely contain '/'. |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `sid` | string |  |
    | `identity` | string |  |
    | `state` | string |  |
    | `is_publisher` | boolean |  |
    | `joined_at` | integer |  |
    | `tracks` | array of objects |  |
    | `tracks.sid` | string |  |
    | `tracks.name` | string |  |
    | `tracks.type` | string |  |
    | `tracks.muted` | boolean |  |
    | `tracks.width` | integer |  |
    | `tracks.height` | integer |  |
    | `tracks.source` | string | What the track carries, as LiveKit names it: CAMERA, MICROPHONE, SCREEN_SHARE, SCREEN_SHARE_AUDIO or UNKNOWN. |
    | `tracks.encryption` | string | How the publisher encrypts the track's media end to end, as LiveKit names it: GCM (LiveKit's end-to-end encryption, which Matrix calls in encrypted rooms use), CUSTOM (another scheme) or NONE (only encrypted between the browser and LiveKit). |

---

### Setup Matrix appservice registration

Generates fresh appservice tokens (rotating any existing ones), enables the appservice, and returns registration YAML. Returns 409 when the deployment owns the tokens; see MATRIX_TOKENS_MANAGED_BY.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/admin/matrix-appservice/setup/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.matrix_appservice_setup_request import MatrixAppserviceSetupRequest # (1)
    from waldur_api_client.api.admin import admin_matrix_appservice_setup # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = MatrixAppserviceSetupRequest()
    response = admin_matrix_appservice_setup.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`MatrixAppserviceSetupRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/matrix_appservice_setup_request.py)
    2.  **API Source:** [`admin_matrix_appservice_setup`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_matrix_appservice_setup.py)

=== "TypeScript"

    ```typescript
    import { adminMatrixAppserviceSetup } from 'waldur-js-client';
    
    try {
      const response = await adminMatrixAppserviceSetup({
      auth: "Token YOUR_API_TOKEN"
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Request Body"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `url` | string |  | Waldur URL reachable by the Matrix homeserver (for webhook callbacks) |
    | `sender_localpart` | string |  | Localpart for the appservice bot user, e.g. 'waldur-bot' |
    | `homeserver_url` | string (uri) |  | Matrix homeserver base URL. Only persisted if MATRIX_HOMESERVER_URL is not already configured; a different value is refused. |
    | `homeserver_public_url` | string (uri) |  | Optional. Matrix homeserver URL used by browser clients. Leave blank when the homeserver URL above is reachable from both servers and browsers. Set this for deployments where the two differ (e.g. Docker-internal vs. Caddy-proxied). Only persisted if MATRIX_HOMESERVER_PUBLIC_URL is not already configured; a different value is refused. |
    | `homeserver_domain` | string |  | Matrix homeserver server_name domain. Only persisted if MATRIX_HOMESERVER_DOMAIN is not already configured; a different value is refused. |
    | `user_registration_secret` | string |  | Registration token the homeserver requires for sign-up (its registration_token). Only persisted if MATRIX_USER_REGISTRATION_SECRET is not already configured; a different value is refused.<br>_Constraints: write-only_ |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `registration_yaml` | string |
    | `as_token` | string |
    | `hs_token` | string |
    | `sender_localpart` | string |
    | `webhook_url` | string |
    | `bot_provision_status` | string |
    
    ---
    
    **`409`** - The deployment owns the appservice tokens and re-seeds them on every sync. Rotate its Matrix secret and redeploy instead, or clear MATRIX_TOKENS_MANAGED_BY if the deployment no longer manages Matrix.
    

---

### Reprovision all active Matrix rooms on a new homeserver

Resets all active rooms to 'creating' state and re-queues them for provisioning. Also resets all user profiles. Only for moving to a new homeserver: on the same homeserver, every old room stays behind with its history next to a new, empty one. Staff only.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/admin/matrix/reprovision/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.admin import admin_matrix_reprovision # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = admin_matrix_reprovision.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`admin_matrix_reprovision`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_matrix_reprovision.py)

=== "TypeScript"

    ```typescript
    import { adminMatrixReprovision } from 'waldur-js-client';
    
    try {
      const response = await adminMatrixReprovision({
      auth: "Token YOUR_API_TOKEN"
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Responses"

    **`202`** - 
    
    | Field | Type |
    |---|---|
    | `rooms_reprovisioned` | integer |
    | `users_reset` | integer |

---
