# Identity Bridge

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/identity-bridge/stats/` | [Get Identity Bridge statistics](#get-identity-bridge-statistics) |
| <span class="http-badge http-post">POST</span> | `/api/identity-bridge/` | [Push user attributes from an ISD](#push-user-attributes-from-an-isd) |
| <span class="http-badge http-post">POST</span> | `/api/identity-bridge/remove/` | [Remove a user from an ISD](#remove-a-user-from-an-isd) |

---

### Get Identity Bridge statistics

Returns system-wide statistics about the Identity Bridge: feature configuration, per-ISD user counts, stale attribute detection, and total federated user counts. Staff only.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/identity-bridge/stats/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.identity_bridge import identity_bridge_stats_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = identity_bridge_stats_retrieve.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`identity_bridge_stats_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/identity_bridge/identity_bridge_stats_retrieve.py)

=== "TypeScript"

    ```typescript
    import { identityBridgeStatsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await identityBridgeStatsRetrieve({
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
    | `deactivation_policy` | string |
    | `allowed_attributes` | array of strings |
    | `total_federated_users` | integer |
    | `total_active_federated_users` | integer |
    | `users_per_isd` | array of objects |
    | `users_per_isd.isd` | string |
    | `users_per_isd.user_count` | integer |
    | `users_per_isd.stale_user_count` | integer |
    | `users_per_isd.oldest_sync` | string |
    | `stale_threshold_days` | integer |
    | `identity_managers` | array of objects |
    | `identity_managers.uuid` | string (uuid) |
    | `identity_managers.full_name` | string |
    | `identity_managers.managed_isds` | array of strings |

---

### Push user attributes from an ISD

Allows Identity Service Domains (ISDs) to push user attributes to Waldur. Creates or updates a user based on username (CUID). Requires FEDERATED_IDENTITY_SYNC_ENABLED to be True. Caller must be staff or an identity manager with the declared source in managed_isds.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/identity-bridge/ \
      Authorization:"Token YOUR_API_TOKEN" \
      username="alice" \
      source="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.identity_bridge_request_request import IdentityBridgeRequestRequest # (1)
    from waldur_api_client.api.identity_bridge import identity_bridge # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = IdentityBridgeRequestRequest(
        username="alice",
        source="string-value"
    )
    response = identity_bridge.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`IdentityBridgeRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/identity_bridge_request_request.py)
    2.  **API Source:** [`identity_bridge`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/identity_bridge/identity_bridge.py)

=== "TypeScript"

    ```typescript
    import { identityBridge } from 'waldur-js-client';
    
    try {
      const response = await identityBridge({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "username": "alice",
        "source": "string-value"
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
    | `username` | string | ✓ | CUID / username of the user to create or update. |
    | `source` | string | ✓ | ISD source identifier, e.g. 'isd:puhuri'. Must match ^[a-z]+:[a-zA-Z0-9._-]+$. |
    | `first_name` | string |  |  |
    | `last_name` | string |  |  |
    | `email` | string (email) |  |  |
    | `organization` | string |  |  |
    | `affiliations` | array of strings |  |  |
    | `civil_number` | string |  |  |
    | `phone_number` | string |  |  |
    | `identity_source` | string |  |  |
    | `gender` | integer |  |  |
    | `personal_title` | string |  |  |
    | `birth_date` | string (date) |  |  |
    | `place_of_birth` | string |  |  |
    | `country_of_residence` | string |  |  |
    | `nationality` | string |  |  |
    | `nationalities` | array of strings |  |  |
    | `organization_country` | string |  |  |
    | `organization_type` | string |  |  |
    | `eduperson_assurance` | array of strings |  |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `created` | boolean |
    | `updated_fields` | array of strings |

---

### Remove a user from an ISD

Signals that a user has been removed from an ISD. Removes the source from active_isds, clears attributes owned by that source, and deactivates the user if no ISDs remain (configurable via FEDERATED_IDENTITY_DEACTIVATION_POLICY). Requires FEDERATED_IDENTITY_SYNC_ENABLED to be True. Caller must be staff or an identity manager with the declared source in managed_isds.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/identity-bridge/remove/ \
      Authorization:"Token YOUR_API_TOKEN" \
      username="alice" \
      source="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.identity_bridge_remove_request import IdentityBridgeRemoveRequest # (1)
    from waldur_api_client.api.identity_bridge import identity_bridge_remove # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = IdentityBridgeRemoveRequest(
        username="alice",
        source="string-value"
    )
    response = identity_bridge_remove.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`IdentityBridgeRemoveRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/identity_bridge_remove_request.py)
    2.  **API Source:** [`identity_bridge_remove`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/identity_bridge/identity_bridge_remove.py)

=== "TypeScript"

    ```typescript
    import { identityBridgeRemove } from 'waldur-js-client';
    
    try {
      const response = await identityBridgeRemove({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "username": "alice",
        "source": "string-value"
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
    | `username` | string | ✓ | CUID / username of the user to remove from the ISD. |
    | `source` | string | ✓ | ISD source identifier, e.g. 'isd:puhuri'. Must match ^[a-z]+:[a-zA-Z0-9._-]+$. |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `deactivated` | boolean |

---
