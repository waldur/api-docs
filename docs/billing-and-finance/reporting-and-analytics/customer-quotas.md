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
    from waldur_api_client.models.customer_quotas_quota_name_enum import CustomerQuotasQuotaNameEnum # (1)
    from waldur_api_client.api.customer_quotas import customer_quotas_list # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = customer_quotas_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`CustomerQuotasQuotaNameEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/customer_quotas_quota_name_enum.py)
    2.  **API Source:** [`customer_quotas_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/customer_quotas/customer_quotas_list.py)

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
    | `quota_name` | string | Name of the quota<br>_Enum: `estimated_price`, `nc_resource_count`, `os_cpu_count`, `os_ram_size`, `os_storage_size`, `vpc_cpu_count`, `vpc_floating_ip_count`, `vpc_instance_count`, `vpc_ram_size`, `vpc_storage_size`_ |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `customer_name` | string |
    | `customer_abbreviation` | string |
    | `value` | integer |

---
