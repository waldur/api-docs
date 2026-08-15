# Helpdesk Stats

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/helpdesk-stats/` | [List Helpdesk Stats](#list-helpdesk-stats) |

---

### List Helpdesk Stats


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/helpdesk-stats/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.helpdesk_stats import helpdesk_stats_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = helpdesk_stats_retrieve.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`helpdesk_stats_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/helpdesk_stats/helpdesk_stats_retrieve.py)

=== "TypeScript"

    ```typescript
    import { helpdeskStatsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await helpdeskStatsRetrieve({
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
    | `total_open` | integer |
    | `total_closed_this_month` | integer |
    | `total_routed` | integer |
    | `total_escalated` | integer |
    | `sla_breach_count` | integer |
    | `avg_first_response_hours` | number (double) |
    | `avg_resolution_hours` | number (double) |
    | `by_status` | object (free-form) |
    | `by_priority` | object (free-form) |

---
