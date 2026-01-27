# Customer Quotas

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/customer-quotas/` | [List customer quotas](#list-customer-quotas) |

---

### List customer quotas

List customer quotas.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/customer-quotas/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.customer_quotas import customer_quotas_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = customer_quotas_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`customer_quotas_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/customer_quotas/customer_quotas_list.py)

=== "TypeScript"

    ```typescript
    import { customerQuotasList } from 'waldur-js-client';
    
    try {
      const response = await customerQuotasList({
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
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `customer_name` | string |
    | `customer_abbreviation` | string |
    | `value` | integer |

---
