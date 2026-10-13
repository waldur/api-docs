# Marketplace Metric Points

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-metric-points/` | [Report metric points](#report-metric-points) |

---

### Report metric points

Records points for resources against metrics their offerings adopt. Send one point or a list. A point is identified by resource, metric, attributes and timestamp: sending it again replaces the value. The caller must be allowed to report usage for every resource in the request, or nothing is recorded (403). Other problems refuse only the affected points, listed by index.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-metric-points/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.metric_point_report_request import MetricPointReportRequest # (1)
    from waldur_api_client.api.marketplace_metric_points import marketplace_metric_points_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_metric_points_create.sync(
        client=client,
        body=null
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`MetricPointReportRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/metric_point_report_request.py)
    2.  **API Source:** [`marketplace_metric_points_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_metric_points/marketplace_metric_points_create.py)

=== "TypeScript"

    ```typescript
    import { marketplaceMetricPointsCreate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceMetricPointsCreate({
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
    | `accepted` | integer |
    | `rejected` | array of objects |
    | `rejected.index` | integer |
    | `rejected.reason` | string |

---
