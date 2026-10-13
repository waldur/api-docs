# Otlp

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-post">POST</span> | `/api/otlp/v1/metrics/` | [Receive OTLP/HTTP metrics](#receive-otlphttp-metrics) |

---

### Receive OTLP/HTTP metrics

Accepts an OpenTelemetry ExportMetricsServiceRequest as JSON or protobuf, optionally gzip-encoded. Each resource must carry the waldur.resource.uuid attribute; a metric's name is the key of a metric the resource's offering adopts. Gauge and Sum (delta or cumulative) are accepted; other types and refused points are counted in partial_success.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/otlp/v1/metrics/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.otlp import otlp_v1_metrics # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = otlp_v1_metrics.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`otlp_v1_metrics`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/otlp/otlp_v1_metrics.py)

=== "TypeScript"

    ```typescript
    import { otlpV1Metrics } from 'waldur-js-client';
    
    try {
      const response = await otlpV1Metrics({
      auth: "Token YOUR_API_TOKEN"
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Responses"

    **`200`** - 
    

---
