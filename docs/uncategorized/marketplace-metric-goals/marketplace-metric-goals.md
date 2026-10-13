# Marketplace Metric Goals

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-metric-goals/` | [List Marketplace Metric Goals](#list-marketplace-metric-goals) |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-metric-goals/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-metric-goals/` | [Create](#create) |
| <span class="http-badge http-put">PUT</span> | `/api/marketplace-metric-goals/{uuid}/` | [Update](#update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/marketplace-metric-goals/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-delete">DELETE</span> | `/api/marketplace-metric-goals/{uuid}/` | [Delete](#delete) |

---

### List Marketplace Metric Goals


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-metric-goals/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.metric_goal_period_enum import MetricGoalPeriodEnum # (1)
    from waldur_api_client.api.marketplace_metric_goals import marketplace_metric_goals_list # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_metric_goals_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`MetricGoalPeriodEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/metric_goal_period_enum.py)
    2.  **API Source:** [`marketplace_metric_goals_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_metric_goals/marketplace_metric_goals_list.py)

=== "TypeScript"

    ```typescript
    import { marketplaceMetricGoalsList } from 'waldur-js-client';
    
    try {
      const response = await marketplaceMetricGoalsList({
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
    | `is_default` | boolean |  |
    | `offering_metric_uuid` | string (uuid) |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `period` | string | _Enum: `month`, `quarter`, `rolling_30d`_ |
    | `project_uuid` | string (uuid) |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `offering_metric` | string (uuid) |  |
    | `metric_name` | string |  |
    | `project` | string (uuid) | Empty sets the offering's default goal. |
    | `project_name` | string |  |
    | `comparator` | string | <br>_Enum: `ge`, `le`_ |
    | `value` | string (decimal) |  |
    | `period` | string | <br>_Enum: `month`, `quarter`, `rolling_30d`_ |
    | `created` | string (date-time) |  |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-metric-goals/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_metric_goals import marketplace_metric_goals_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_metric_goals_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_metric_goals_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_metric_goals/marketplace_metric_goals_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceMetricGoalsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceMetricGoalsRetrieve({
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
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `offering_metric` | string (uuid) |  |
    | `metric_name` | string |  |
    | `project` | string (uuid) | Empty sets the offering's default goal. |
    | `project_name` | string |  |
    | `comparator` | string | <br>_Enum: `ge`, `le`_ |
    | `value` | string (decimal) |  |
    | `period` | string | <br>_Enum: `month`, `quarter`, `rolling_30d`_ |
    | `created` | string (date-time) |  |

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-metric-goals/ \
      Authorization:"Token YOUR_API_TOKEN" \
      offering_metric="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      value="12.34"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.metric_goal_request import MetricGoalRequest # (1)
    from waldur_api_client.api.marketplace_metric_goals import marketplace_metric_goals_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = MetricGoalRequest(
        offering_metric="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        value="12.34"
    )
    response = marketplace_metric_goals_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`MetricGoalRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/metric_goal_request.py)
    2.  **API Source:** [`marketplace_metric_goals_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_metric_goals/marketplace_metric_goals_create.py)

=== "TypeScript"

    ```typescript
    import { marketplaceMetricGoalsCreate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceMetricGoalsCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "offering_metric": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "value": "12.34"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Request Body (required)"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `offering_metric` | string (uuid) | ✓ |  |
    | `project` | string (uuid) |  | Empty sets the offering's default goal. |
    | `comparator` | string |  | <br>_Enum: `ge`, `le`_ |
    | `value` | string (decimal) | ✓ |  |
    | `period` | string |  | <br>_Enum: `month`, `quarter`, `rolling_30d`_ |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `offering_metric` | string (uuid) |  |
    | `metric_name` | string |  |
    | `project` | string (uuid) | Empty sets the offering's default goal. |
    | `project_name` | string |  |
    | `comparator` | string | <br>_Enum: `ge`, `le`_ |
    | `value` | string (decimal) |  |
    | `period` | string | <br>_Enum: `month`, `quarter`, `rolling_30d`_ |
    | `created` | string (date-time) |  |

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/marketplace-metric-goals/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      offering_metric="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      value="12.34"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.metric_goal_request import MetricGoalRequest # (1)
    from waldur_api_client.api.marketplace_metric_goals import marketplace_metric_goals_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = MetricGoalRequest(
        offering_metric="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        value="12.34"
    )
    response = marketplace_metric_goals_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`MetricGoalRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/metric_goal_request.py)
    2.  **API Source:** [`marketplace_metric_goals_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_metric_goals/marketplace_metric_goals_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceMetricGoalsUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceMetricGoalsUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "offering_metric": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "value": "12.34"
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


=== "Request Body (required)"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `offering_metric` | string (uuid) | ✓ |  |
    | `project` | string (uuid) |  | Empty sets the offering's default goal. |
    | `comparator` | string |  | <br>_Enum: `ge`, `le`_ |
    | `value` | string (decimal) | ✓ |  |
    | `period` | string |  | <br>_Enum: `month`, `quarter`, `rolling_30d`_ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `offering_metric` | string (uuid) |  |
    | `metric_name` | string |  |
    | `project` | string (uuid) | Empty sets the offering's default goal. |
    | `project_name` | string |  |
    | `comparator` | string | <br>_Enum: `ge`, `le`_ |
    | `value` | string (decimal) |  |
    | `period` | string | <br>_Enum: `month`, `quarter`, `rolling_30d`_ |
    | `created` | string (date-time) |  |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/marketplace-metric-goals/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_metric_goal_request import PatchedMetricGoalRequest # (1)
    from waldur_api_client.api.marketplace_metric_goals import marketplace_metric_goals_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedMetricGoalRequest()
    response = marketplace_metric_goals_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedMetricGoalRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_metric_goal_request.py)
    2.  **API Source:** [`marketplace_metric_goals_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_metric_goals/marketplace_metric_goals_partial_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceMetricGoalsPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceMetricGoalsPartialUpdate({
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


=== "Request Body"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `offering_metric` | string (uuid) |  |  |
    | `project` | string (uuid) |  | Empty sets the offering's default goal. |
    | `comparator` | string |  | <br>_Enum: `ge`, `le`_ |
    | `value` | string (decimal) |  |  |
    | `period` | string |  | <br>_Enum: `month`, `quarter`, `rolling_30d`_ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `offering_metric` | string (uuid) |  |
    | `metric_name` | string |  |
    | `project` | string (uuid) | Empty sets the offering's default goal. |
    | `project_name` | string |  |
    | `comparator` | string | <br>_Enum: `ge`, `le`_ |
    | `value` | string (decimal) |  |
    | `period` | string | <br>_Enum: `month`, `quarter`, `rolling_30d`_ |
    | `created` | string (date-time) |  |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/marketplace-metric-goals/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_metric_goals import marketplace_metric_goals_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_metric_goals_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_metric_goals_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_metric_goals/marketplace_metric_goals_destroy.py)

=== "TypeScript"

    ```typescript
    import { marketplaceMetricGoalsDestroy } from 'waldur-js-client';
    
    try {
      const response = await marketplaceMetricGoalsDestroy({
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

    **`204`** - No response body
    

---
