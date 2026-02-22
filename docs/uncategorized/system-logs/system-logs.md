# System Logs

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/system-logs/` | [List System Logs](#list-system-logs) |
| <span class="http-badge http-get">GET</span> | `/api/system-logs/{id}/` | [Retrieve](#retrieve) |
| **Other Actions** | | |
| <span class="http-badge http-get">GET</span> | `/api/system-logs/instances/` | [List system log instances](#list-system-log-instances) |
| <span class="http-badge http-get">GET</span> | `/api/system-logs/stats/` | [Get system log statistics](#get-system-log-statistics) |

---
## Core CRUD


### List System Logs


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/system-logs/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.system_log_level_enum import SystemLogLevelEnum # (1)
    from waldur_api_client.models.system_log_o_enum import SystemLogOEnum # (2)
    from waldur_api_client.models.system_log_source_enum import SystemLogSourceEnum # (3)
    from waldur_api_client.api.system_logs import system_logs_list # (4)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = system_logs_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`SystemLogLevelEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/system_log_level_enum.py)
    2.  **Model Source:** [`SystemLogOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/system_log_o_enum.py)
    3.  **Model Source:** [`SystemLogSourceEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/system_log_source_enum.py)
    4.  **API Source:** [`system_logs_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/system_logs/system_logs_list.py)

=== "TypeScript"

    ```typescript
    import { systemLogsList } from 'waldur-js-client';
    
    try {
      const response = await systemLogsList({
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
    | `created_from` | number |  |
    | `created_to` | number |  |
    | `instance` | string |  |
    | `level` | string | _Enum: `CRITICAL`, `ERROR`, `INFO`, `WARNING`_ |
    | `level_gte` | integer | Min level: 20=INFO, 30=WARNING, 40=ERROR, 50=CRITICAL |
    | `logger_name` | string |  |
    | `message` | string |  |
    | `o` | array | Ordering<br><br> |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `source` | string | _Enum: `api`, `worker`, `beat`_ |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `id` | integer |  |
    | `created` | string (date-time) |  |
    | `source` | any |  |
    | `instance` | string | Pod name (K8s) or container name (Docker) |
    | `level` | string |  |
    | `level_number` | integer |  |
    | `logger_name` | string |  |
    | `message` | string |  |
    | `context` | any |  |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/system-logs/123/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.system_logs import system_logs_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = system_logs_retrieve.sync(
        id=123,
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`system_logs_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/system_logs/system_logs_retrieve.py)

=== "TypeScript"

    ```typescript
    import { systemLogsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await systemLogsRetrieve({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "id": 123
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required | Description |
    |---|---|---|---|
    | `id` | integer | ✓ | A unique integer value identifying this system log. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `id` | integer |  |
    | `created` | string (date-time) |  |
    | `source` | any |  |
    | `instance` | string | Pod name (K8s) or container name (Docker) |
    | `level` | string |  |
    | `level_number` | integer |  |
    | `logger_name` | string |  |
    | `message` | string |  |
    | `context` | any |  |

---

## Other Actions


### List system log instances

List all known instances (pods/containers) with their last activity.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/system-logs/instances/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.system_log_level_enum import SystemLogLevelEnum # (1)
    from waldur_api_client.models.system_log_o_enum import SystemLogOEnum # (2)
    from waldur_api_client.models.system_log_source_enum import SystemLogSourceEnum # (3)
    from waldur_api_client.api.system_logs import system_logs_instances_list # (4)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = system_logs_instances_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`SystemLogLevelEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/system_log_level_enum.py)
    2.  **Model Source:** [`SystemLogOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/system_log_o_enum.py)
    3.  **Model Source:** [`SystemLogSourceEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/system_log_source_enum.py)
    4.  **API Source:** [`system_logs_instances_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/system_logs/system_logs_instances_list.py)

=== "TypeScript"

    ```typescript
    import { systemLogsInstancesList } from 'waldur-js-client';
    
    try {
      const response = await systemLogsInstancesList({
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
    | `created_from` | number |  |
    | `created_to` | number |  |
    | `instance` | string |  |
    | `level` | string | _Enum: `CRITICAL`, `ERROR`, `INFO`, `WARNING`_ |
    | `level_gte` | integer | Min level: 20=INFO, 30=WARNING, 40=ERROR, 50=CRITICAL |
    | `logger_name` | string |  |
    | `message` | string |  |
    | `o` | array | Ordering<br><br> |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `source` | string | _Enum: `api`, `worker`, `beat`_ |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `source` | string |
    | `instance` | string |
    | `last_seen` | string (date-time) |
    | `count` | integer |

---

### Get system log statistics

Return log count statistics per source and instance, plus total table size.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/system-logs/stats/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.system_logs import system_logs_stats_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = system_logs_stats_retrieve.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`system_logs_stats_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/system_logs/system_logs_stats_retrieve.py)

=== "TypeScript"

    ```typescript
    import { systemLogsStatsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await systemLogsStatsRetrieve({
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
    | `instances` | array of objects |
    | `instances.source` | string |
    | `instances.instance` | string |
    | `instances.count` | integer |
    | `total_size_bytes` | integer |
    | `total_size_mb` | number (double) |

---
