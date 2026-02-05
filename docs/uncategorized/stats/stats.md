# Stats

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/stats/celery/` | [Get Celery worker statistics](#get-celery-worker-statistics) |
| <span class="http-badge http-get">GET</span> | `/api/stats/database/` | [Get comprehensive database statistics](#get-comprehensive-database-statistics) |
| <span class="http-badge http-get">GET</span> | `/api/stats/table-growth/` | [Get table growth statistics](#get-table-growth-statistics) |
| <span class="http-badge http-post">POST</span> | `/api/stats/query/` | [Execute read-only SQL query](#execute-read-only-sql-query) |

---

### Get Celery worker statistics

Provides a comprehensive snapshot of all Celery workers' status.

This endpoint returns detailed information about:
- **active**: Tasks currently being executed by workers
- **scheduled**: Tasks scheduled for future execution (with ETA)
- **reserved**: Tasks received by workers but not yet started
- **revoked**: Task IDs that have been cancelled/revoked
- **query_task**: Results of task queries (if any)
- **stats**: Detailed worker statistics including uptime, pool info, and broker connection

Each field is a dictionary where keys are worker names (e.g., 'celery@hostname').
If no workers are available, fields will be `null`.

Requires support user permissions.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/stats/celery/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.stats import stats_celery_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = stats_celery_retrieve.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`stats_celery_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/stats/stats_celery_retrieve.py)

=== "TypeScript"

    ```typescript
    import { statsCeleryRetrieve } from 'waldur-js-client';
    
    try {
      const response = await statsCeleryRetrieve({
      auth: "Token YOUR_API_TOKEN"
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `active` | object (free-form) | Currently executing tasks per worker. Keys are worker names, values are lists of active tasks. |
    | `scheduled` | object (free-form) | Tasks scheduled for future execution per worker. Keys are worker names, values are lists of scheduled tasks with ETA. |
    | `reserved` | object (free-form) | Tasks that have been received but not yet started per worker. Keys are worker names, values are lists of reserved tasks. |
    | `revoked` | object (free-form) | IDs of revoked (cancelled) tasks per worker. Keys are worker names, values are lists of task IDs. |
    | `query_task` | object (free-form) | Query results for specific tasks. May be null if no query was performed. |
    | `stats` | object (free-form) | Detailed statistics per worker including uptime, pool info, and resource usage. Keys are worker names. |

---

### Get comprehensive database statistics

Retrieves comprehensive statistics about the PostgreSQL database including:
- **Table statistics**: Top 10 largest tables by size
- **Connection statistics**: Active, idle, and waiting connections with utilization
- **Database size**: Total size, data size, and index size
- **Cache performance**: Buffer cache and index hit ratios (should be >99%)
- **Transaction statistics**: Commits, rollbacks, deadlocks
- **Lock statistics**: Current locks and waiting queries
- **Maintenance statistics**: Dead tuples, vacuum needs, oldest transaction age
- **Active queries**: Currently running queries with duration
- **Query performance**: Sequential vs index scan ratios
- **Replication status**: WAL size and replication lag (if applicable)

This information is useful for monitoring, debugging, and performance tuning.
Requires support user permissions.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/stats/database/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.stats import stats_database_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = stats_database_retrieve.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`stats_database_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/stats/stats_database_retrieve.py)

=== "TypeScript"

    ```typescript
    import { statsDatabaseRetrieve } from 'waldur-js-client';
    
    try {
      const response = await statsDatabaseRetrieve({
      auth: "Token YOUR_API_TOKEN"
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `table_stats` | array of objects | Top largest tables by size |
    | `table_stats.table_name` | string | Name of the database table |
    | `table_stats.total_size` | integer | Total size of the table in bytes |
    | `table_stats.data_size` | integer | Size of the actual data in bytes |
    | `table_stats.external_size` | integer | Size of external data (e.g., TOAST) in bytes |
    | `connections` | any | Connection statistics |
    | `database_size` | any | Database size information |
    | `cache_performance` | any | Cache hit ratios and memory settings |
    | `transactions` | any | Transaction commit/rollback statistics |
    | `locks` | any | Current lock statistics |
    | `maintenance` | any | Vacuum and maintenance statistics |
    | `active_queries` | any | Currently running queries |
    | `query_performance` | any | Query performance indicators |
    | `replication` | any | Replication status (if applicable) |

---

### Get table growth statistics

Retrieves historical table growth statistics for detecting abnormal patterns.

This endpoint returns:
- **date**: Current date of the statistics
- **weekly_threshold_percent**: Configured alert threshold for weekly growth
- **monthly_threshold_percent**: Configured alert threshold for monthly growth
- **tables**: List of tables with their growth statistics, sorted by growth rate

Each table entry includes:
- Current size and row estimates
- Size and row estimates from 7 days ago
- Size and row estimates from 30 days ago
- Weekly and monthly growth percentages

Use this data to identify tables that may be experiencing abnormal growth,
which could indicate bugs like the version-based get_or_create issue.

Query parameters:
- **table_name** (optional): Filter to a specific table name
- **days** (optional, default 30): Number of days of history to include

Requires support user permissions.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/stats/table-growth/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.stats import stats_table_growth_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = stats_table_growth_retrieve.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`stats_table_growth_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/stats/stats_table_growth_retrieve.py)

=== "TypeScript"

    ```typescript
    import { statsTableGrowthRetrieve } from 'waldur-js-client';
    
    try {
      const response = await statsTableGrowthRetrieve({
      auth: "Token YOUR_API_TOKEN"
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `date` | string (date) | Current date of the statistics |
    | `weekly_threshold_percent` | integer | Configured weekly growth alert threshold |
    | `monthly_threshold_percent` | integer | Configured monthly growth alert threshold |
    | `tables` | array of objects | Table growth statistics sorted by growth rate |
    | `tables.table_name` | string | Name of the database table |
    | `tables.current_total_size` | integer | Current total size including indexes in bytes |
    | `tables.current_data_size` | integer | Current data-only size in bytes |
    | `tables.current_row_estimate` | integer | Current estimated row count |
    | `tables.week_ago_total_size` | integer | Total size from 7 days ago in bytes |
    | `tables.week_ago_row_estimate` | integer | Row estimate from 7 days ago |
    | `tables.month_ago_total_size` | integer | Total size from 30 days ago in bytes |
    | `tables.month_ago_row_estimate` | integer | Row estimate from 30 days ago |
    | `tables.weekly_growth_percent` | number (double) | Percentage growth over the past week |
    | `tables.monthly_growth_percent` | number (double) | Percentage growth over the past month |
    | `tables.weekly_row_growth_percent` | number (double) | Percentage row count growth over the past week |
    | `tables.monthly_row_growth_percent` | number (double) | Percentage row count growth over the past month |
    | `alerts` | array of objects | List of tables that exceeded configured growth thresholds |
    | `alerts.table_name` | string | Name of the table triggering the alert |
    | `alerts.period` | any | Growth period that exceeded the threshold |
    | `alerts.growth_percent` | number (double) | Actual growth percentage observed |
    | `alerts.threshold` | integer | Configured threshold that was exceeded |

---

### Execute read-only SQL query

Execute a given SQL query against a read-only database replica. This is a powerful tool for diagnostics and reporting, but should be used with caution. Requires support user permissions.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/stats/query/ \
      Authorization:"Token YOUR_API_TOKEN" \
      query="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.query_request import QueryRequest # (1)
    from waldur_api_client.api.stats import stats_query # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = QueryRequest(
        query="string-value"
    )
    response = stats_query.sync(
        client=client,
        body=body_data
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`QueryRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/query_request.py)
    2.  **API Source:** [`stats_query`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/stats/stats_query.py)

=== "TypeScript"

    ```typescript
    import { statsQuery } from 'waldur-js-client';
    
    try {
      const response = await statsQuery({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "query": "string-value"
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
    | `query` | string | ✓ | Search query string |


=== "Responses"

    **`200`** - 
    
    
    ---
    
    **`400`** - No response body
    

---
