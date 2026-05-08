# Marketplace Site Agent Logs

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-site-agent-logs/` | [List Marketplace Site Agent Logs](#list-marketplace-site-agent-logs) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-site-agent-logs/` | [Push site agent logs](#push-site-agent-logs) |

---

### List Marketplace Site Agent Logs


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-site-agent-logs/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_site_agent_logs import marketplace_site_agent_logs_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_site_agent_logs_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`marketplace_site_agent_logs_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_site_agent_logs/marketplace_site_agent_logs_list.py)

=== "TypeScript"

    ```typescript
    import { marketplaceSiteAgentLogsList } from 'waldur-js-client';
    
    try {
      const response = await marketplaceSiteAgentLogsList({
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
    | `agent_identity_uuid` | string (uuid) |  |
    | `level` | string |  |
    | `offering_uuid` | string (uuid) |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `timestamp_from` | number (float) |  |
    | `timestamp_to` | number (float) |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `offering` | string (uri) |  |
    | `offering_uuid` | string (uuid) |  |
    | `agent_identity_uuid` | string (uuid) |  |
    | `timestamp` | number (double) | Unix timestamp of the log entry |
    | `level` | string | <br>_Enum: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`_ |
    | `message` | string |  |
    | `module` | string |  |
    | `created` | string (date-time) |  |

---

### Push site agent logs

Receive a batch of log entries from a site agent. Send a list where each entry includes agent_identity_uuid.


=== "HTTPie"

    ```bash
    echo '[{"agent_identity_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "timestamp": 123.45, "level": "DEBUG", "message": "string-value", "module": "string-value"}]' | http \
      POST \
      https://api.example.com/api/marketplace-site-agent-logs/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_site_agent_logs import marketplace_site_agent_logs_create # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_site_agent_logs_create.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`marketplace_site_agent_logs_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_site_agent_logs/marketplace_site_agent_logs_create.py)

=== "TypeScript"

    ```typescript
    import { marketplaceSiteAgentLogsCreate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceSiteAgentLogsCreate({
      auth: "Token YOUR_API_TOKEN",
      body: [{"agent_identity_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "timestamp": 123.45, "level": "DEBUG", "message": "string-value", "module": "string-value"}]
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Query Parameters"

    | Name | Type | Description |
    |---|---|---|
    | `agent_identity_uuid` | string (uuid) |  |
    | `level` | string |  |
    | `offering_uuid` | string (uuid) |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `timestamp_from` | number (float) |  |
    | `timestamp_to` | number (float) |  |


=== "Request Body (required)"

    The request body is an array of objects, where each object has the following structure:
    
    | Field | Type | Required |
    |---|---|---|
    | `agent_identity_uuid` | string (uuid) | ✓ |
    | `timestamp` | number (double) | ✓ |
    | `level` | string | ✓ |
    | `message` | string | ✓ |
    | `module` | string | ✓ |


=== "Responses"

    **`201`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `offering` | string (uri) |  |
    | `offering_uuid` | string (uuid) |  |
    | `agent_identity_uuid` | string (uuid) |  |
    | `timestamp` | number (double) | Unix timestamp of the log entry |
    | `level` | string | <br>_Enum: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`_ |
    | `message` | string |  |
    | `module` | string |  |
    | `created` | string (date-time) |  |

---
