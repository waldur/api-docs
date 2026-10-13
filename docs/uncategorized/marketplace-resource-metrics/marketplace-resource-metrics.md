# Marketplace Resource Metrics

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-resource-metrics/` | [Get a resource's metric figures](#get-a-resources-metric-figures) |

---

### Get a resource's metric figures

Figures for the current and the previous calendar month. A resource has no goals: they apply to a project's combined figure.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-resource-metrics/ \
      Authorization:"Token YOUR_API_TOKEN" \
      resource_uuid=="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_resource_metrics import marketplace_resource_metrics_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_resource_metrics_list.sync(
        client=client,
        resource_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`marketplace_resource_metrics_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_resource_metrics/marketplace_resource_metrics_list.py)

=== "TypeScript"

    ```typescript
    import { marketplaceResourceMetricsList } from 'waldur-js-client';
    
    try {
      const response = await marketplaceResourceMetricsList({
      auth: "Token YOUR_API_TOKEN",
      query: {
        "resource_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Query Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `resource_uuid` | string (uuid) | ✓ |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `offering_metric` | object |  |
    | `offering_metric.uuid` | string (uuid) |  |
    | `offering_metric.offering` | string (uuid) |  |
    | `offering_metric.offering_name` | string |  |
    | `offering_metric.definition` | string (uuid) |  |
    | `offering_metric.key` | string | Name services report against. Cannot be changed. |
    | `offering_metric.name` | string |  |
    | `offering_metric.display_name` | string | Empty shows the definition's name. |
    | `offering_metric.unit` | string | UCUM unit, for example h, % or {learners}. |
    | `offering_metric.kind` | any |  |
    | `offering_metric.good_direction` | any |  |
    | `offering_metric.attribute_keys` | array of strings |  |
    | `offering_metric.project_aggregation` | any | How the figures of a project's resources combine. An average is unweighted: every resource counts once. |
    | `offering_metric.state` | any |  |
    | `offering_metric.created` | string (date-time) |  |
    | `period` | string |  |
    | `period_start` | string (date-time) |  |
    | `current` | number (double) |  |
    | `previous` | number (double) |  |

---
