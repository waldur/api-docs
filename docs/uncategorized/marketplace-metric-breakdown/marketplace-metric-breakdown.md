# Marketplace Metric Breakdown

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-metric-breakdown/` | [Break a metric figure down by an attribute or by resource](#break-a-metric-figure-down-by-an-attribute-or-by-resource) |

---

### Break a metric figure down by an attribute or by resource


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-metric-breakdown/ \
      Authorization:"Token YOUR_API_TOKEN" \
      group_by=="https://api.example.com/api/users/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      offering_metric_uuid=="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      start=="2023-10-01T12:00:00Z"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_metric_breakdown import marketplace_metric_breakdown_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_metric_breakdown_list.sync(
        client=client,
        group_by="https://api.example.com/api/users/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        offering_metric_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        start="2023-10-01T12:00:00Z"
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`marketplace_metric_breakdown_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_metric_breakdown/marketplace_metric_breakdown_list.py)

=== "TypeScript"

    ```typescript
    import { marketplaceMetricBreakdownList } from 'waldur-js-client';
    
    try {
      const response = await marketplaceMetricBreakdownList({
      auth: "Token YOUR_API_TOKEN",
      query: {
        "group_by": "https://api.example.com/api/users/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "offering_metric_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "start": "2023-10-01T12:00:00Z"
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
    | `end` | string (date-time) |  |  |
    | `group_by` | string | ✓ | An attribute the metric declares, or 'resource' to break a project's figure down by its resources. |
    | `offering_metric_uuid` | string (uuid) | ✓ |  |
    | `project_uuid` | string (uuid) |  | The project whose figure to break down. Either this or resource_uuid. |
    | `resource_uuid` | string (uuid) |  | The resource whose figure to break down. Either this or project_uuid. |
    | `start` | string (date-time) | ✓ |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `value` | object (free-form) | The attribute's value, or the resource's name when broken down by resource. |
    | `figure` | number (double) |  |
    | `resource_uuid` | string (uuid) |  |
    | `resource_name` | string |  |

---
