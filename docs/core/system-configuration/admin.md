# Admin

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/admin/matrix-appservice/status/` | [Get Matrix appservice status](#get-matrix-appservice-status) |
| <span class="http-badge http-get">GET</span> | `/api/admin/matrix/diagnostics/` | [Run Matrix connectivity diagnostics](#run-matrix-connectivity-diagnostics) |
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
    
    | Field | Type |
    |---|---|
    | `ok` | boolean |
    | `checks` | array of objects |
    | `checks.name` | string |
    | `checks.label` | string |
    | `checks.ok` | boolean |
    | `checks.detail` | string |

---

### Setup Matrix appservice registration

Generates fresh appservice tokens (rotating any existing ones), enables the appservice, and returns registration YAML.


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
    | `homeserver_url` | string (uri) |  | Matrix homeserver base URL. Only persisted if MATRIX_HOMESERVER_URL is not already configured. |
    | `homeserver_domain` | string |  | Matrix homeserver server_name domain. Only persisted if MATRIX_HOMESERVER_DOMAIN is not already configured. |
    | `user_registration_secret` | string |  | Shared secret configured in the homeserver for user registration. Only persisted if MATRIX_USER_REGISTRATION_SECRET is not already configured.<br>_Constraints: write-only_ |


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

### Reprovision all active Matrix rooms on a new homeserver

Resets all active rooms to 'creating' state and re-queues them for provisioning. Also resets all user profiles. Staff only.


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
