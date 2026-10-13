# Marketplace Offering Metrics

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-offering-metrics/` | [List Marketplace Offering Metrics](#list-marketplace-offering-metrics) |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-offering-metrics/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-offering-metrics/` | [Create](#create) |
| <span class="http-badge http-put">PUT</span> | `/api/marketplace-offering-metrics/{uuid}/` | [Update](#update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/marketplace-offering-metrics/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-delete">DELETE</span> | `/api/marketplace-offering-metrics/{uuid}/` | [Delete](#delete) |
| **Other Actions** | | |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-offering-metrics/{uuid}/archive/` | [Stop collecting and hide the metric from consuming projects](#stop-collecting-and-hide-the-metric-from-consuming-projects) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-offering-metrics/{uuid}/pause/` | [Refuse new points; what was reported stays visible](#refuse-new-points-what-was-reported-stays-visible) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-offering-metrics/{uuid}/purge/` | [Delete everything an archived metric collected, then the metric](#delete-everything-an-archived-metric-collected-then-the-metric) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-offering-metrics/{uuid}/resume/` | [Resume](#resume) |

---
## Core CRUD


### List Marketplace Offering Metrics


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-offering-metrics/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.offering_metric_state_enum import OfferingMetricStateEnum # (1)
    from waldur_api_client.api.marketplace_offering_metrics import marketplace_offering_metrics_list # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_offering_metrics_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`OfferingMetricStateEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/offering_metric_state_enum.py)
    2.  **API Source:** [`marketplace_offering_metrics_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_metrics/marketplace_offering_metrics_list.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingMetricsList } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingMetricsList({
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
    | `definition_uuid` | string (uuid) |  |
    | `key` | string |  |
    | `offering_uuid` | string (uuid) |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `state` | string | _Enum: `active`, `paused`, `archived`_ |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `offering` | string (uuid) |  |
    | `offering_name` | string |  |
    | `definition` | string (uuid) |  |
    | `key` | string | Name services report against. Cannot be changed. |
    | `name` | string |  |
    | `display_name` | string | Empty shows the definition's name. |
    | `unit` | string | UCUM unit, for example h, % or {learners}. |
    | `kind` | any |  |
    | `good_direction` | any |  |
    | `attribute_keys` | array of strings |  |
    | `project_aggregation` | any | How the figures of a project's resources combine. An average is unweighted: every resource counts once. |
    | `state` | any |  |
    | `created` | string (date-time) |  |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-offering-metrics/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_offering_metrics import marketplace_offering_metrics_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_offering_metrics_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_offering_metrics_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_metrics/marketplace_offering_metrics_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingMetricsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingMetricsRetrieve({
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
    | `offering` | string (uuid) |  |
    | `offering_name` | string |  |
    | `definition` | string (uuid) |  |
    | `key` | string | Name services report against. Cannot be changed. |
    | `name` | string |  |
    | `display_name` | string | Empty shows the definition's name. |
    | `unit` | string | UCUM unit, for example h, % or {learners}. |
    | `kind` | any |  |
    | `good_direction` | any |  |
    | `attribute_keys` | array of strings |  |
    | `project_aggregation` | any | How the figures of a project's resources combine. An average is unweighted: every resource counts once. |
    | `state` | any |  |
    | `created` | string (date-time) |  |

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-offering-metrics/ \
      Authorization:"Token YOUR_API_TOKEN" \
      offering="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      definition="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.offering_metric_request import OfferingMetricRequest # (1)
    from waldur_api_client.api.marketplace_offering_metrics import marketplace_offering_metrics_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = OfferingMetricRequest(
        offering="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        definition="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = marketplace_offering_metrics_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`OfferingMetricRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/offering_metric_request.py)
    2.  **API Source:** [`marketplace_offering_metrics_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_metrics/marketplace_offering_metrics_create.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingMetricsCreate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingMetricsCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "offering": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "definition": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `offering` | string (uuid) | ✓ |  |
    | `definition` | string (uuid) | ✓ |  |
    | `display_name` | string |  | Empty shows the definition's name. |
    | `project_aggregation` | any |  | How the figures of a project's resources combine. An average is unweighted: every resource counts once. |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `offering` | string (uuid) |  |
    | `offering_name` | string |  |
    | `definition` | string (uuid) |  |
    | `key` | string | Name services report against. Cannot be changed. |
    | `name` | string |  |
    | `display_name` | string | Empty shows the definition's name. |
    | `unit` | string | UCUM unit, for example h, % or {learners}. |
    | `kind` | any |  |
    | `good_direction` | any |  |
    | `attribute_keys` | array of strings |  |
    | `project_aggregation` | any | How the figures of a project's resources combine. An average is unweighted: every resource counts once. |
    | `state` | any |  |
    | `created` | string (date-time) |  |

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/marketplace-offering-metrics/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      offering="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      definition="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.offering_metric_request import OfferingMetricRequest # (1)
    from waldur_api_client.api.marketplace_offering_metrics import marketplace_offering_metrics_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = OfferingMetricRequest(
        offering="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        definition="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = marketplace_offering_metrics_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`OfferingMetricRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/offering_metric_request.py)
    2.  **API Source:** [`marketplace_offering_metrics_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_metrics/marketplace_offering_metrics_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingMetricsUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingMetricsUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "offering": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "definition": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `offering` | string (uuid) | ✓ |  |
    | `definition` | string (uuid) | ✓ |  |
    | `display_name` | string |  | Empty shows the definition's name. |
    | `project_aggregation` | any |  | How the figures of a project's resources combine. An average is unweighted: every resource counts once. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `offering` | string (uuid) |  |
    | `offering_name` | string |  |
    | `definition` | string (uuid) |  |
    | `key` | string | Name services report against. Cannot be changed. |
    | `name` | string |  |
    | `display_name` | string | Empty shows the definition's name. |
    | `unit` | string | UCUM unit, for example h, % or {learners}. |
    | `kind` | any |  |
    | `good_direction` | any |  |
    | `attribute_keys` | array of strings |  |
    | `project_aggregation` | any | How the figures of a project's resources combine. An average is unweighted: every resource counts once. |
    | `state` | any |  |
    | `created` | string (date-time) |  |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/marketplace-offering-metrics/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_offering_metric_request import PatchedOfferingMetricRequest # (1)
    from waldur_api_client.api.marketplace_offering_metrics import marketplace_offering_metrics_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedOfferingMetricRequest()
    response = marketplace_offering_metrics_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedOfferingMetricRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_offering_metric_request.py)
    2.  **API Source:** [`marketplace_offering_metrics_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_metrics/marketplace_offering_metrics_partial_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingMetricsPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingMetricsPartialUpdate({
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
    | `offering` | string (uuid) |  |  |
    | `definition` | string (uuid) |  |  |
    | `display_name` | string |  | Empty shows the definition's name. |
    | `project_aggregation` | any |  | How the figures of a project's resources combine. An average is unweighted: every resource counts once. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `offering` | string (uuid) |  |
    | `offering_name` | string |  |
    | `definition` | string (uuid) |  |
    | `key` | string | Name services report against. Cannot be changed. |
    | `name` | string |  |
    | `display_name` | string | Empty shows the definition's name. |
    | `unit` | string | UCUM unit, for example h, % or {learners}. |
    | `kind` | any |  |
    | `good_direction` | any |  |
    | `attribute_keys` | array of strings |  |
    | `project_aggregation` | any | How the figures of a project's resources combine. An average is unweighted: every resource counts once. |
    | `state` | any |  |
    | `created` | string (date-time) |  |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/marketplace-offering-metrics/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_offering_metrics import marketplace_offering_metrics_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_offering_metrics_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_offering_metrics_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_metrics/marketplace_offering_metrics_destroy.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingMetricsDestroy } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingMetricsDestroy({
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

## Other Actions


### Stop collecting and hide the metric from consuming projects

Stop collecting and hide the metric from consuming projects.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-offering-metrics/a1b2c3d4-e5f6-7890-abcd-ef1234567890/archive/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_offering_metrics import marketplace_offering_metrics_archive # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_offering_metrics_archive.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_offering_metrics_archive`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_metrics/marketplace_offering_metrics_archive.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingMetricsArchive } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingMetricsArchive({
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
    | `offering` | string (uuid) |  |
    | `offering_name` | string |  |
    | `definition` | string (uuid) |  |
    | `key` | string | Name services report against. Cannot be changed. |
    | `name` | string |  |
    | `display_name` | string | Empty shows the definition's name. |
    | `unit` | string | UCUM unit, for example h, % or {learners}. |
    | `kind` | any |  |
    | `good_direction` | any |  |
    | `attribute_keys` | array of strings |  |
    | `project_aggregation` | any | How the figures of a project's resources combine. An average is unweighted: every resource counts once. |
    | `state` | any |  |
    | `created` | string (date-time) |  |

---

### Refuse new points; what was reported stays visible

Refuse new points; what was reported stays visible.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-offering-metrics/a1b2c3d4-e5f6-7890-abcd-ef1234567890/pause/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_offering_metrics import marketplace_offering_metrics_pause # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_offering_metrics_pause.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_offering_metrics_pause`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_metrics/marketplace_offering_metrics_pause.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingMetricsPause } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingMetricsPause({
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
    | `offering` | string (uuid) |  |
    | `offering_name` | string |  |
    | `definition` | string (uuid) |  |
    | `key` | string | Name services report against. Cannot be changed. |
    | `name` | string |  |
    | `display_name` | string | Empty shows the definition's name. |
    | `unit` | string | UCUM unit, for example h, % or {learners}. |
    | `kind` | any |  |
    | `good_direction` | any |  |
    | `attribute_keys` | array of strings |  |
    | `project_aggregation` | any | How the figures of a project's resources combine. An average is unweighted: every resource counts once. |
    | `state` | any |  |
    | `created` | string (date-time) |  |

---

### Delete everything an archived metric collected, then the metric

Delete everything an archived metric collected, then the metric.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-offering-metrics/a1b2c3d4-e5f6-7890-abcd-ef1234567890/purge/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_offering_metrics import marketplace_offering_metrics_purge # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_offering_metrics_purge.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_offering_metrics_purge`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_metrics/marketplace_offering_metrics_purge.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingMetricsPurge } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingMetricsPurge({
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

    **`202`** - No response body
    

---

### Resume


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-offering-metrics/a1b2c3d4-e5f6-7890-abcd-ef1234567890/resume/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_offering_metrics import marketplace_offering_metrics_resume # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_offering_metrics_resume.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_offering_metrics_resume`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_metrics/marketplace_offering_metrics_resume.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingMetricsResume } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingMetricsResume({
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
    | `offering` | string (uuid) |  |
    | `offering_name` | string |  |
    | `definition` | string (uuid) |  |
    | `key` | string | Name services report against. Cannot be changed. |
    | `name` | string |  |
    | `display_name` | string | Empty shows the definition's name. |
    | `unit` | string | UCUM unit, for example h, % or {learners}. |
    | `kind` | any |  |
    | `good_direction` | any |  |
    | `attribute_keys` | array of strings |  |
    | `project_aggregation` | any | How the figures of a project's resources combine. An average is unweighted: every resource counts once. |
    | `state` | any |  |
    | `created` | string (date-time) |  |

---
