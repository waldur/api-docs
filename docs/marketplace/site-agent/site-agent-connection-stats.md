# Marketplace Site Agent Connection Stats

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-site-agent-connection-stats/` | [Get agent connection statistics](#get-agent-connection-statistics) |

---

### Get agent connection statistics

Returns connection status for all registered agents.

For each agent identity, provides:
- Agent metadata (name, version, offering)
- Services and their states
- Event subscriptions with RabbitMQ connection status
- RabbitMQ queues associated with the agent's offering

The RMQ connection data includes:
- Whether the agent is currently connected
- Connection source IP, timestamp, and state
- Traffic statistics (bytes sent/received)

Requires support user permissions.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-site-agent-connection-stats/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_site_agent_connection_stats import marketplace_site_agent_connection_stats_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_site_agent_connection_stats_retrieve.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_site_agent_connection_stats_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_site_agent_connection_stats/marketplace_site_agent_connection_stats_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceSiteAgentConnectionStatsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceSiteAgentConnectionStatsRetrieve({
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
    | `agents` | array of objects | List of agents with connection status |
    | `agents.uuid` | string (uuid) | Agent identity UUID |
    | `agents.name` | string | Agent name |
    | `agents.offering_uuid` | string (uuid) | Associated offering UUID |
    | `agents.offering_name` | string | Associated offering name |
    | `agents.version` | string | Agent version |
    | `agents.last_restarted` | string (date-time) | When the agent was last restarted |
    | `agents.event_consumer_uuid` | string (uuid) | UUID of the unified event consumer the agent drains, null while it still runs on legacy subscriptions |
    | `agents.user_uuid` | string (uuid) | Consumer owner UUID |
    | `agents.user_username` | string | Consumer owner username |
    | `agents.user_full_name` | string | Consumer owner full name |
    | `agents.user_is_staff` | boolean | Whether the consumer owner is a staff user, whose delivery scope is platform-wide |
    | `agents.auth_kind` | any | How the agent authenticated when it registered the queue |
    | `agents.auth_token_prefix` | string | Prefix of the Personal Access Token backing the queue |
    | `agents.auth_token_name` | string | Name of the Personal Access Token backing the queue |
    | `agents.authorized_via` | any | Permission branch that authorised the registration |
    | `agents.delivery_blocked_reason` | string | Why no event can reach this consumer, null when delivery works |
    | `agents.services` | array of objects | Services running within this agent |
    | `agents.services.uuid` | string (uuid) | Service UUID |
    | `agents.services.name` | string | Service name |
    | `agents.services.state` | string | Service state: ACTIVE, IDLE, or ERROR |
    | `agents.services.modified` | string (date-time) | Last modification timestamp |
    | `agents.event_subscriptions` | array of objects | Event subscriptions with connection status |
    | `agents.event_subscriptions.uuid` | string (uuid) | Event subscription UUID |
    | `agents.event_subscriptions.created` | string (date-time) | When the subscription was created |
    | `agents.event_subscriptions.observable_objects` | object (free-form) | List of observable object configurations |
    | `agents.event_subscriptions.rmq_connection` | any | RabbitMQ connection status for this subscription |
    | `agents.queues` | array of objects | RabbitMQ queues for this agent's offering |
    | `agents.queues.name` | string | Queue name |
    | `agents.queues.messages` | integer | Number of messages in queue |
    | `agents.queues.consumers` | integer | Number of active consumers |
    | `agents.queues.object_type` | string | Parsed object type from queue name |
    | `agents.queues.kind` | any | Whether this is the agent's unified consumer queue or a legacy subscription queue |
    | `summary` | any | Summary statistics |
    
    ---
    
    **`503`** - 
    

---
