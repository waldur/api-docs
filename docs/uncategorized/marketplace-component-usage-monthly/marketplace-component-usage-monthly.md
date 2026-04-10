# Marketplace Component Usage Monthly

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-component-usage-monthly/` | [List monthly component usage summaries globally](#list-monthly-component-usage-summaries-globally) |

---

### List monthly component usage summaries globally

Returns paginated monthly component usage across all offerings and service providers. Results are automatically filtered by the user's permissions. Defaults to the current month if no time filters ('billing_period', 'start', 'end') are provided.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-component-usage-monthly/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.component_usage_monthly_field_enum import ComponentUsageMonthlyFieldEnum # (1)
    from waldur_api_client.api.marketplace_component_usage_monthly import marketplace_component_usage_monthly_list # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_component_usage_monthly_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`ComponentUsageMonthlyFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/component_usage_monthly_field_enum.py)
    2.  **API Source:** [`marketplace_component_usage_monthly_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_component_usage_monthly/marketplace_component_usage_monthly_list.py)

=== "TypeScript"

    ```typescript
    import { marketplaceComponentUsageMonthlyList } from 'waldur-js-client';
    
    try {
      const response = await marketplaceComponentUsageMonthlyList({
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
    | `billing_period` | string (date) |  |
    | `billing_type` | string |  |
    | `component_type` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `end` | string (date) |  |
    | `field` | array |  |
    | `o` | string | Which field to use when ordering the results. |
    | `offering_type` | string |  |
    | `offering_uuid` | string (uuid) |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `project_uuid` | string (uuid) |  |
    | `start` | string (date) |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `offering_uuid` | string (uuid) |
    | `offering_name` | string |
    | `offering_type` | string |
    | `service_provider_uuid` | string (uuid) |
    | `service_provider_name` | string |
    | `category_uuid` | string (uuid) |
    | `category_title` | string |
    | `component_type` | string |
    | `component_name` | string |
    | `measured_unit` | string |
    | `billing_type` | string |
    | `limit_amount` | integer |
    | `limit_period` | string |
    | `billing_period` | string (date) |
    | `total_consumed` | string (decimal) |
    | `total_allocated` | string (decimal) |
    | `usage_percent` | string (decimal) |

---
