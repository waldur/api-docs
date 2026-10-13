# Marketplace Metric Series

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-metric-series/` | [Get metric series](#get-metric-series) |

---

### Get metric series


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-metric-series/ \
      Authorization:"Token YOUR_API_TOKEN" \
      offering_metric_uuid=="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      start=="2023-10-01T12:00:00Z"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.metric_series_response_aggregate_enum import MetricSeriesResponseAggregateEnum # (1)
    from waldur_api_client.models.metric_series_response_granularity_enum import MetricSeriesResponseGranularityEnum # (2)
    from waldur_api_client.api.marketplace_metric_series import marketplace_metric_series_retrieve # (3)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_metric_series_retrieve.sync(
        client=client,
        offering_metric_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        start="2023-10-01T12:00:00Z"
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`MetricSeriesResponseAggregateEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/metric_series_response_aggregate_enum.py)
    2.  **Model Source:** [`MetricSeriesResponseGranularityEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/metric_series_response_granularity_enum.py)
    3.  **API Source:** [`marketplace_metric_series_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_metric_series/marketplace_metric_series_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceMetricSeriesRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceMetricSeriesRetrieve({
      auth: "Token YOUR_API_TOKEN",
      query: {
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
    | `aggregate` | string |  | How a gauge's points in a bucket combine; counters sum.<br>_Enum: `last`, `max`, `mean`, `min`_ |
    | `end` | string (date-time) |  |  |
    | `granularity` | string |  | _Enum: `auto`, `day`, `hour`, `raw`_ |
    | `group_by` | string |  | Attribute key to break the figure down by |
    | `offering_metric_uuid` | string (uuid) | ✓ |  |
    | `project_uuid` | string (uuid) |  |  |
    | `resource_uuid` | string (uuid) |  |  |
    | `start` | string (date-time) | ✓ |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `granularity` | string |
    | `series` | array of objects |
    | `series.attributes` | object (free-form) |
    | `series.points` | array of objects |
    | `series.points.timestamp` | string (date-time) |
    | `series.points.value` | number (double) |

---
