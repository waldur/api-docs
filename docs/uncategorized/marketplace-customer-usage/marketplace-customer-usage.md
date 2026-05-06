# Marketplace Customer Usage

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-customer-usage/{uuid}/components-usage/` | [Get resource usage statistics broken down per offering](#get-resource-usage-statistics-broken-down-per-offering) |
| **Other Actions** | | |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-customer-usage/{uuid}/components-usage-by-project/` | [Get per-project usage breakdown for a single offering](#get-per-project-usage-breakdown-for-a-single-offering) |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-customer-usage/{uuid}/components-usage-timeseries/` | [Get monthly usage buckets for a single offering](#get-monthly-usage-buckets-for-a-single-offering) |

---
## Core CRUD


### Get resource usage statistics broken down per offering

Returns one row per (offering, component type, billing type) for all non-terminated resources within the scope. Each row's `usage` and `limit_usage` are aggregated using the offering's own `limit_period`.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-customer-usage/a1b2c3d4-e5f6-7890-abcd-ef1234567890/components-usage/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_customer_usage import marketplace_customer_usage_components_usage_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_customer_usage_components_usage_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_customer_usage_components_usage_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_customer_usage/marketplace_customer_usage_components_usage_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceCustomerUsageComponentsUsageRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceCustomerUsageComponentsUsageRetrieve({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `components` | array of objects |
    | `components.type` | string |
    | `components.name` | string |
    | `components.description` | string |
    | `components.measured_unit` | string |
    | `components.billing_type` | string |
    | `components.usage` | number (double) |
    | `components.limit_usage` | number (double) |
    | `components.limit` | number (double) |
    | `components.offering_name` | string |
    | `components.offering_uuid` | string (uuid) |
    | `components.limit_period` | string |
    | `components.current_period_label` | string |
    | `components.current_period_start` | string (date) |
    | `components.current_period_end` | string (date) |

---

## Other Actions


### Get per-project usage breakdown for a single offering

Returns the customer's usage of one offering broken down by project. Each project entry includes an in-period total `usage` and a monthly `buckets` array. Projects are sorted by usage descending.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-customer-usage/a1b2c3d4-e5f6-7890-abcd-ef1234567890/components-usage-by-project/ \
      Authorization:"Token YOUR_API_TOKEN" \
      offering_uuid=="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_customer_usage import marketplace_customer_usage_components_usage_by_project_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_customer_usage_components_usage_by_project_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        offering_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_customer_usage_components_usage_by_project_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_customer_usage/marketplace_customer_usage_components_usage_by_project_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceCustomerUsageComponentsUsageByProjectRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceCustomerUsageComponentsUsageByProjectRetrieve({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      query: {
        "offering_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Query Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `component_type` | string |  |
    | `offering_uuid` | string (uuid) | ✓ |
    | `period_offset` | integer |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `offering_uuid` | string (uuid) |
    | `offering_name` | string |
    | `type` | string |
    | `name` | string |
    | `measured_unit` | string |
    | `billing_type` | string |
    | `limit_period` | string |
    | `limit` | number (double) |
    | `current_period_label` | string |
    | `current_period_start` | string (date) |
    | `current_period_end` | string (date) |
    | `today` | string (date) |
    | `total_usage` | number (double) |
    | `projects` | array of objects |
    | `projects.project_uuid` | string (uuid) |
    | `projects.project_name` | string |
    | `projects.usage` | number (double) |
    | `projects.buckets` | array of objects |
    | `projects.buckets.billing_period` | string (date) |
    | `projects.buckets.usage` | number (double) |

---

### Get monthly usage buckets for a single offering

Returns a per-month timeseries of `ComponentUsage` for one offering, restricted to that offering's current `limit_period`. Buckets are keyed by `billing_period` (always month-start). `period_offset` shifts the window backward by N periods.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-customer-usage/a1b2c3d4-e5f6-7890-abcd-ef1234567890/components-usage-timeseries/ \
      Authorization:"Token YOUR_API_TOKEN" \
      offering_uuid=="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_customer_usage import marketplace_customer_usage_components_usage_timeseries_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_customer_usage_components_usage_timeseries_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        offering_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_customer_usage_components_usage_timeseries_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_customer_usage/marketplace_customer_usage_components_usage_timeseries_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceCustomerUsageComponentsUsageTimeseriesRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceCustomerUsageComponentsUsageTimeseriesRetrieve({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      query: {
        "offering_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `uuid` | string (uuid) | ✓ |


=== "Query Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `component_type` | string |  |
    | `offering_uuid` | string (uuid) | ✓ |
    | `period_offset` | integer |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `offering_uuid` | string (uuid) |
    | `offering_name` | string |
    | `type` | string |
    | `name` | string |
    | `measured_unit` | string |
    | `billing_type` | string |
    | `limit_period` | string |
    | `limit` | number (double) |
    | `current_period_label` | string |
    | `current_period_start` | string (date) |
    | `current_period_end` | string (date) |
    | `today` | string (date) |
    | `buckets` | array of objects |
    | `buckets.billing_period` | string (date) |
    | `buckets.usage` | number (double) |

---
