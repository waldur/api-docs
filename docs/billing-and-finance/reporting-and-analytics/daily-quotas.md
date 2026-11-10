# Daily Quotas

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/daily-quotas/` | [List Daily Quotas](#list-daily-quotas) |

---

### List Daily Quotas


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/daily-quotas/ \
      Authorization:"Token YOUR_API_TOKEN" \
      scope=="https://api.example.com/api/scope/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.daily_quotas import daily_quotas_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = daily_quotas_retrieve.sync(
        client=client,
        scope="https://api.example.com/api/scope/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`daily_quotas_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/daily_quotas/daily_quotas_retrieve.py)

=== "TypeScript"

    ```typescript
    import { dailyQuotasRetrieve } from 'waldur-js-client';
    
    try {
      const response = await dailyQuotasRetrieve({
      auth: "Token YOUR_API_TOKEN",
      query: {
        "scope": "https://api.example.com/api/scope/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
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
    | `end` | string (date) |  | End date in format YYYY-MM-DD |
    | `quota_names` | array |  | List of quota names |
    | `scope` | string (uri) | ✓ | URL of the project or organization |
    | `start` | string (date) |  | Start date in format YYYY-MM-DD |


=== "Responses"

    **`200`** - 
    


=== "Authorization"

    The scope must be a project or organization that the caller's roles reach; staff and support may name any.

---
