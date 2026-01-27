# Support Statistics

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/support-statistics/` | [List Support Statistics](#list-support-statistics) |

---

### List Support Statistics


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/support-statistics/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.support_statistics import support_statistics_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = support_statistics_retrieve.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`support_statistics_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_statistics/support_statistics_retrieve.py)

=== "TypeScript"

    ```typescript
    import { supportStatisticsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await supportStatisticsRetrieve({
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
    | `open_issues_count` | integer |
    | `closed_this_month_count` | integer |
    | `recent_broadcasts_count` | integer |

---
