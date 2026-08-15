# Helpdesk Health

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/helpdesk-health/` | [List Helpdesk Health](#list-helpdesk-health) |

---

### List Helpdesk Health


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/helpdesk-health/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.helpdesk_health import helpdesk_health_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = helpdesk_health_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`helpdesk_health_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/helpdesk_health/helpdesk_health_list.py)

=== "TypeScript"

    ```typescript
    import { helpdeskHealthList } from 'waldur-js-client';
    
    try {
      const response = await helpdeskHealthList({
      auth: "Token YOUR_API_TOKEN"
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `provider_name` | string |
    | `backend_type` | string |
    | `is_active` | boolean |
    | `health_status` | string |
    | `last_health_check` | string (date-time) |
    | `failed_routing_count` | integer |

---
