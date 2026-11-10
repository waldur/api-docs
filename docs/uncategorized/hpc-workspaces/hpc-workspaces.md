# Hpc Workspaces

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/hpc-workspaces/` | [List HPC workspaces](#list-hpc-workspaces) |
| <span class="http-badge http-get">GET</span> | `/api/hpc-workspaces/{uuid}/` | [HPC workspace overview](#hpc-workspace-overview) |
| **Other Actions** | | |
| <span class="http-badge http-get">GET</span> | `/api/hpc-workspaces/{uuid}/cluster_load/` | [Node load and reservations of the cluster](#node-load-and-reservations-of-the-cluster) |
| <span class="http-badge http-get">GET</span> | `/api/hpc-workspaces/{uuid}/file_content/` | [View a file on the cluster](#view-a-file-on-the-cluster) |
| <span class="http-badge http-get">GET</span> | `/api/hpc-workspaces/{uuid}/files/` | [List a directory on the cluster](#list-a-directory-on-the-cluster) |
| <span class="http-badge http-get">GET</span> | `/api/hpc-workspaces/{uuid}/job_stats/` | [Job statistics of the allocation](#job-statistics-of-the-allocation) |
| <span class="http-badge http-get">GET</span> | `/api/hpc-workspaces/{uuid}/jobs/` | [List jobs of the allocation](#list-jobs-of-the-allocation) |
| <span class="http-badge http-get">GET</span> | `/api/hpc-workspaces/{uuid}/jobs/{job_id}/output/` | [Get the script and output of a job](#get-the-script-and-output-of-a-job) |
| <span class="http-badge http-get">GET</span> | `/api/hpc-workspaces/{uuid}/jobs/{job_id}/performance_pdf/` | [Download the performance report of a job as PDF](#download-the-performance-report-of-a-job-as-pdf) |
| <span class="http-badge http-get">GET</span> | `/api/hpc-workspaces/{uuid}/jobs/{job_id}/performance/` | [Get the performance of a job over its run](#get-the-performance-of-a-job-over-its-run) |
| <span class="http-badge http-get">GET</span> | `/api/hpc-workspaces/{uuid}/jobs/{job_id}/` | [Get a job of the allocation](#get-a-job-of-the-allocation) |
| <span class="http-badge http-get">GET</span> | `/api/hpc-workspaces/{uuid}/output_series/` | [Plot a job output file](#plot-a-job-output-file) |
| <span class="http-badge http-get">GET</span> | `/api/hpc-workspaces/{uuid}/partitions/` | [Partitions of the cluster](#partitions-of-the-cluster) |
| <span class="http-badge http-get">GET</span> | `/api/hpc-workspaces/{uuid}/software/` | [Find software available on the cluster](#find-software-available-on-the-cluster) |
| <span class="http-badge http-get">GET</span> | `/api/hpc-workspaces/{uuid}/usage/` | [Usage of the allocation against its limits](#usage-of-the-allocation-against-its-limits) |
| <span class="http-badge http-post">POST</span> | `/api/hpc-workspaces/{uuid}/jobs/` | [Submit a job to the allocation](#submit-a-job-to-the-allocation) |
| <span class="http-badge http-post">POST</span> | `/api/hpc-workspaces/{uuid}/jobs/{job_id}/cancel/` | [Cancel a job of the allocation](#cancel-a-job-of-the-allocation) |
| <span class="http-badge http-post">POST</span> | `/api/hpc-workspaces/{uuid}/preview_script/` | [Preview a batch script](#preview-a-batch-script) |

---
## Core CRUD


### List HPC workspaces

SLURM allocations visible to the user whose offering is connected to FirecREST or a cluster monitor.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/hpc-workspaces/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.hpc_workspaces import hpc_workspaces_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = hpc_workspaces_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`hpc_workspaces_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/hpc_workspaces/hpc_workspaces_list.py)

=== "TypeScript"

    ```typescript
    import { hpcWorkspacesList } from 'waldur-js-client';
    
    try {
      const response = await hpcWorkspacesList({
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
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `resource_uuid` | string (uuid) | Only the workspace of this resource, e.g. to tell whether a resource page has one. |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `resource_uuid` | string (uuid) |  |
    | `resource_name` | string |  |
    | `account` | string |  |
    | `offering_uuid` | string (uuid) |  |
    | `offering_name` | string |  |
    | `project_uuid` | string (uuid) |  |
    | `project_name` | string |  |
    | `customer_name` | string |  |
    | `system_name` | string |  |
    | `state` | string |  |
    | `firecrest_enabled` | boolean | Jobs can be submitted and canceled and files opened through FirecREST. Without it the workspace is read-only, from the cluster monitor. |
    | `monitoring_enabled` | boolean | Jobs have per-run performance samples from the cluster monitor. |


=== "Authorization"

    The workspace acts on the cluster as the user, with their identity provider token, and no permission scopes that down. So only the user's own sign-in may use it, not a personal access token, an identity provider token or impersonation (see ``is_delegated``).

---

### HPC workspace overview

Allocation, the user's cluster identity and FirecREST system health. Problems reaching FirecREST are reported in 'error' rather than failing the request; 'sign_in_provider' names the identity provider to sign in through again when that is the remedy. Without FirecREST ('firecrest_enabled' false) the health is left out.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/hpc-workspaces/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.hpc_workspaces import hpc_workspaces_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = hpc_workspaces_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`hpc_workspaces_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/hpc_workspaces/hpc_workspaces_retrieve.py)

=== "TypeScript"

    ```typescript
    import { hpcWorkspacesRetrieve } from 'waldur-js-client';
    
    try {
      const response = await hpcWorkspacesRetrieve({
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
    | `resource_uuid` | string (uuid) |  |
    | `resource_name` | string |  |
    | `account` | string |  |
    | `offering_uuid` | string (uuid) |  |
    | `offering_name` | string |  |
    | `project_uuid` | string (uuid) |  |
    | `project_name` | string |  |
    | `customer_name` | string |  |
    | `system_name` | string |  |
    | `state` | string |  |
    | `firecrest_enabled` | boolean | Jobs can be submitted and canceled and files opened through FirecREST. Without it the workspace is read-only, from the cluster monitor. |
    | `monitoring_enabled` | boolean | Jobs have per-run performance samples from the cluster monitor. |
    | `username` | string |  |
    | `home_directory` | string |  |
    | `healthy` | boolean |  |
    | `services_health` | array of objects |  |
    | `services_health.service_type` | string |  |
    | `services_health.healthy` | boolean |  |
    | `services_health.message` | string |  |
    | `services_health.last_checked` | string |  |
    | `error` | string |  |
    | `sign_in_provider` | string | Identity provider to sign in through again to restore HPC access, when that is what 'error' asks for. |


=== "Authorization"

    The workspace acts on the cluster as the user, with their identity provider token, and no permission scopes that down. So only the user's own sign-in may use it, not a personal access token, an identity provider token or impersonation (see ``is_delegated``).

---

## Other Actions


### Node load and reservations of the cluster

Every node with its state, CPU load and partitions, a summary per partition and the upcoming reservations and maintenance windows.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/hpc-workspaces/a1b2c3d4-e5f6-7890-abcd-ef1234567890/cluster_load/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.hpc_workspaces import hpc_workspaces_cluster_load_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = hpc_workspaces_cluster_load_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`hpc_workspaces_cluster_load_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/hpc_workspaces/hpc_workspaces_cluster_load_retrieve.py)

=== "TypeScript"

    ```typescript
    import { hpcWorkspacesClusterLoadRetrieve } from 'waldur-js-client';
    
    try {
      const response = await hpcWorkspacesClusterLoadRetrieve({
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
    | `announcements` | array of objects |  |
    | `announcements.uuid` | string (uuid) |  |
    | `announcements.name` | string |  |
    | `announcements.message` | string |  |
    | `announcements.state` | string |  |
    | `announcements.impact` | string |  |
    | `announcements.outage` | boolean |  |
    | `announcements.impact_description` | string |  |
    | `announcements.start` | integer |  |
    | `announcements.end` | integer |  |
    | `announcements.partitions` | array of strings |  |
    | `announcements.expected_reservation` | string | Reservation the site agent creates for it, when sync is enabled. |
    | `announcements.reservation_in_place` | boolean | Whether the cluster holds it; null when no reservation is due. |
    | `nodes` | array of objects |  |
    | `nodes.name` | string |  |
    | `nodes.partitions` | array of strings |  |
    | `nodes.state` | string |  |
    | `nodes.cpus` | integer |  |
    | `nodes.alloc_cpus` | integer |  |
    | `nodes.load_percent` | number (double) |  |
    | `nodes.free_memory_mb` | integer |  |
    | `nodes.reason` | string |  |
    | `partitions` | array of objects |  |
    | `partitions.name` | string |  |
    | `partitions.total` | integer |  |
    | `partitions.idle` | integer |  |
    | `partitions.mixed` | integer |  |
    | `partitions.allocated` | integer |  |
    | `partitions.unavailable` | integer |  |
    | `partitions.reserved` | integer |  |
    | `partitions.average_load_percent` | number (double) |  |
    | `reservations` | array of objects |  |
    | `reservations.name` | string |  |
    | `reservations.start` | integer |  |
    | `reservations.end` | integer |  |
    | `reservations.node_list` | string |  |
    | `reservations.node_count` | integer |  |
    | `reservations.maintenance` | boolean |  |
    | `reservations.active` | boolean |  |
    | `reservations.partitions` | array of strings |  |
    | `reservations.announced` | boolean | For maintenance reservations: whether Waldur announces it. |
    | `charts` | array of objects |  |
    | `charts.chart_type` | string | <br>_Enum: `line`, `area`, `bar`, `stacked_bar`, `scatter`, `heatmap`, `timeline`_ |
    | `charts.title` | string |  |
    | `charts.subtitle` | string |  |
    | `charts.x` | object |  |
    | `charts.x.type` | any |  |
    | `charts.x.label` | string |  |
    | `charts.x.unit` | string |  |
    | `charts.x.min` | number (double) |  |
    | `charts.x.max` | number (double) |  |
    | `charts.x.categories` | array of strings | Category labels, in order, for a category axis. |
    | `charts.y` | object |  |
    | `charts.y.type` | any |  |
    | `charts.y.label` | string |  |
    | `charts.y.unit` | string |  |
    | `charts.y.min` | number (double) |  |
    | `charts.y.max` | number (double) |  |
    | `charts.y.categories` | array of strings | Category labels, in order, for a category axis. |
    | `charts.y2` | any | Right-hand value axis. |
    | `charts.series` | array of objects |  |
    | `charts.series.name` | string |  |
    | `charts.series.style` | any |  |
    | `charts.series.tone` | string | <br>_Enum: `neutral`, `info`, `success`, `warning`, `danger`_ |
    | `charts.series.y_axis` | any | Secondary plots against `y2`, for a series in other units. |
    | `charts.series.points` | array of arrays | [x, y] pairs; heatmap [x, y, value]; timeline [row, start, end, limit_end]. |
    | `charts.series.labels` | array of strings | Tooltip text per point. |
    | `charts.series.ids` | array of strings | Identifier per point (e.g. a job ID) the page may link to. |
    | `charts.annotations` | array of objects |  |
    | `charts.annotations.type` | string | <br>_Enum: `line_x`, `line_y`, `area_x`, `area_y`_ |
    | `charts.annotations.value` | number (double) |  |
    | `charts.annotations.value_end` | number (double) |  |
    | `charts.annotations.label` | string |  |
    | `charts.annotations.tone` | any |  |
    | `charts.link` | object |  |
    | `charts.link.label` | string |  |
    | `charts.link.url` | string |  |
    | `charts.empty_message` | string | Shown instead of the chart when no series has points. |


=== "Authorization"

    The workspace acts on the cluster as the user, with their identity provider token, and no permission scopes that down. So only the user's own sign-in may use it, not a personal access token, an identity provider token or impersonation (see ``is_delegated``).

---

### View a file on the cluster

Content of a small text file (bounded by FirecREST's operation size limit).


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/hpc-workspaces/a1b2c3d4-e5f6-7890-abcd-ef1234567890/file_content/ \
      Authorization:"Token YOUR_API_TOKEN" \
      path=="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.hpc_workspaces import hpc_workspaces_file_content_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = hpc_workspaces_file_content_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        path="string-value"
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`hpc_workspaces_file_content_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/hpc_workspaces/hpc_workspaces_file_content_retrieve.py)

=== "TypeScript"

    ```typescript
    import { hpcWorkspacesFileContentRetrieve } from 'waldur-js-client';
    
    try {
      const response = await hpcWorkspacesFileContentRetrieve({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      query: {
        "path": "string-value"
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
    | `path` | string | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `path` | string |
    | `content` | string |


=== "Authorization"

    The workspace acts on the cluster as the user, with their identity provider token, and no permission scopes that down. So only the user's own sign-in may use it, not a personal access token, an identity provider token or impersonation (see ``is_delegated``).

---

### List a directory on the cluster


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/hpc-workspaces/a1b2c3d4-e5f6-7890-abcd-ef1234567890/files/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.hpc_workspaces import hpc_workspaces_files_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = hpc_workspaces_files_list.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`hpc_workspaces_files_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/hpc_workspaces/hpc_workspaces_files_list.py)

=== "TypeScript"

    ```typescript
    import { hpcWorkspacesFilesList } from 'waldur-js-client';
    
    try {
      const response = await hpcWorkspacesFilesList({
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


=== "Query Parameters"

    | Name | Type | Description |
    |---|---|---|
    | `path` | string | Directory to list; defaults to home. |
    | `show_hidden` | boolean | _Default: `False`_ |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `name` | string |  |
    | `type` | string | 'd' directory, '-' file, 'l' link |
    | `link_target` | string |  |
    | `user` | string |  |
    | `group` | string |  |
    | `permissions` | string |  |
    | `last_modified` | string |  |
    | `size` | string |  |


=== "Authorization"

    The workspace acts on the cluster as the user, with their identity provider token, and no permission scopes that down. So only the user's own sign-in may use it, not a personal access token, an identity provider token or impersonation (see ``is_delegated``).

---

### Job statistics of the allocation

Outcomes per day, failures by exit code, time limit fit, CPU and memory efficiency, queue waits by partition and right-sizing suggestions over the last days, with chart specs for each figure.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/hpc-workspaces/a1b2c3d4-e5f6-7890-abcd-ef1234567890/job_stats/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.hpc_workspaces import hpc_workspaces_job_stats_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = hpc_workspaces_job_stats_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`hpc_workspaces_job_stats_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/hpc_workspaces/hpc_workspaces_job_stats_retrieve.py)

=== "TypeScript"

    ```typescript
    import { hpcWorkspacesJobStatsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await hpcWorkspacesJobStatsRetrieve({
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


=== "Query Parameters"

    | Name | Type | Description |
    |---|---|---|
    | `days` | integer | Days of job history, up to FirecREST's longest window (7 days).<br>_Default: `7`_ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `days` | integer |  |
    | `since` | integer |  |
    | `until` | integer |  |
    | `totals` | object |  |
    | `totals.completed` | integer |  |
    | `totals.failed` | integer |  |
    | `totals.timeout` | integer |  |
    | `totals.cancelled` | integer |  |
    | `totals.running` | integer |  |
    | `totals.pending` | integer |  |
    | `cpu_hours` | number (double) |  |
    | `failures` | array of objects |  |
    | `failures.exit_code` | integer |  |
    | `failures.count` | integer |  |
    | `failures.names` | array of strings |  |
    | `failures.latest_job_id` | string |  |
    | `wait_by_partition` | array of objects |  |
    | `wait_by_partition.partition` | string |  |
    | `wait_by_partition.jobs` | integer |  |
    | `wait_by_partition.median_wait_seconds` | integer |  |
    | `wait_by_partition.p90_wait_seconds` | integer |  |
    | `suggestions` | array of objects |  |
    | `suggestions.kind` | string | <br>_Enum: `time_limit`, `cpu_efficiency`_ |
    | `suggestions.name` | string |  |
    | `suggestions.jobs` | integer |  |
    | `suggestions.message` | string |  |
    | `suggestions.current_limit_minutes` | integer |  |
    | `suggestions.suggested_limit_minutes` | integer |  |
    | `charts` | array of objects |  |
    | `charts.chart_type` | string | <br>_Enum: `line`, `area`, `bar`, `stacked_bar`, `scatter`, `heatmap`, `timeline`_ |
    | `charts.title` | string |  |
    | `charts.subtitle` | string |  |
    | `charts.x` | object |  |
    | `charts.x.type` | any |  |
    | `charts.x.label` | string |  |
    | `charts.x.unit` | string |  |
    | `charts.x.min` | number (double) |  |
    | `charts.x.max` | number (double) |  |
    | `charts.x.categories` | array of strings | Category labels, in order, for a category axis. |
    | `charts.y` | object |  |
    | `charts.y.type` | any |  |
    | `charts.y.label` | string |  |
    | `charts.y.unit` | string |  |
    | `charts.y.min` | number (double) |  |
    | `charts.y.max` | number (double) |  |
    | `charts.y.categories` | array of strings | Category labels, in order, for a category axis. |
    | `charts.y2` | any | Right-hand value axis. |
    | `charts.series` | array of objects |  |
    | `charts.series.name` | string |  |
    | `charts.series.style` | any |  |
    | `charts.series.tone` | string | <br>_Enum: `neutral`, `info`, `success`, `warning`, `danger`_ |
    | `charts.series.y_axis` | any | Secondary plots against `y2`, for a series in other units. |
    | `charts.series.points` | array of arrays | [x, y] pairs; heatmap [x, y, value]; timeline [row, start, end, limit_end]. |
    | `charts.series.labels` | array of strings | Tooltip text per point. |
    | `charts.series.ids` | array of strings | Identifier per point (e.g. a job ID) the page may link to. |
    | `charts.annotations` | array of objects |  |
    | `charts.annotations.type` | string | <br>_Enum: `line_x`, `line_y`, `area_x`, `area_y`_ |
    | `charts.annotations.value` | number (double) |  |
    | `charts.annotations.value_end` | number (double) |  |
    | `charts.annotations.label` | string |  |
    | `charts.annotations.tone` | any |  |
    | `charts.link` | object |  |
    | `charts.link.label` | string |  |
    | `charts.link.url` | string |  |
    | `charts.empty_message` | string | Shown instead of the chart when no series has points. |


=== "Authorization"

    The workspace acts on the cluster as the user, with their identity provider token, and no permission scopes that down. So only the user's own sign-in may use it, not a personal access token, an identity provider token or impersonation (see ``is_delegated``).

---

### List jobs of the allocation


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/hpc-workspaces/a1b2c3d4-e5f6-7890-abcd-ef1234567890/jobs/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.hpc_job_time_window_enum import HpcJobTimeWindowEnum # (1)
    from waldur_api_client.api.hpc_workspaces import hpc_workspaces_jobs_list # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = hpc_workspaces_jobs_list.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`HpcJobTimeWindowEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/hpc_job_time_window_enum.py)
    2.  **API Source:** [`hpc_workspaces_jobs_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/hpc_workspaces/hpc_workspaces_jobs_list.py)

=== "TypeScript"

    ```typescript
    import { hpcWorkspacesJobsList } from 'waldur-js-client';
    
    try {
      const response = await hpcWorkspacesJobsList({
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


=== "Query Parameters"

    | Name | Type | Description |
    |---|---|---|
    | `time_window` | string | How far back to look for finished jobs (default 24h).<br>_Enum: `1h`, `8h`, `24h`, `3d`, `7d`_ |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `job_id` | string |  |
    | `name` | string |  |
    | `state` | string |  |
    | `state_reason` | string |  |
    | `exit_code` | integer |  |
    | `account` | string |  |
    | `partition` | string |  |
    | `user` | string |  |
    | `nodes` | string |  |
    | `allocation_nodes` | integer |  |
    | `working_directory` | string |  |
    | `start_time` | integer |  |
    | `end_time` | integer |  |
    | `elapsed` | integer | Seconds |
    | `time_limit` | integer | Seconds (FirecREST converts Slurm's minutes) |
    | `submit_time` | integer |  |
    | `wait_seconds` | integer | From submission to start |
    | `allocation_cpus` | integer |  |
    | `requested_memory_mb` | integer |  |
    | `cpu_time_seconds` | integer |  |
    | `cpu_hours` | number (double) | Allocated CPUs x elapsed time |
    | `cpu_efficiency` | number (double) | CPU time / (CPUs x elapsed), 0..1; finished jobs only |
    | `max_rss_mb` | integer |  |
    | `memory_efficiency` | number (double) | Peak RSS / requested memory, 0..1; finished jobs only |
    | `allocation_gpus` | integer |  |
    | `gpu_hours` | number (double) | Allocated GPUs x elapsed time |
    | `energy_kwh` | number (double) | Energy consumed; where accounting records the energy TRES |
    | `mean_power_w` | integer | Energy / elapsed time, all of the job's nodes |


=== "Authorization"

    The workspace acts on the cluster as the user, with their identity provider token, and no permission scopes that down. So only the user's own sign-in may use it, not a personal access token, an identity provider token or impersonation (see ``is_delegated``).

---

### Get the script and output of a job

The batch script and the last lines of standard output and error.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/hpc-workspaces/a1b2c3d4-e5f6-7890-abcd-ef1234567890/jobs/string-value/output/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.hpc_workspaces import hpc_workspaces_jobs_output_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = hpc_workspaces_jobs_output_retrieve.sync(
        job_id="string-value",
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`hpc_workspaces_jobs_output_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/hpc_workspaces/hpc_workspaces_jobs_output_retrieve.py)

=== "TypeScript"

    ```typescript
    import { hpcWorkspacesJobsOutputRetrieve } from 'waldur-js-client';
    
    try {
      const response = await hpcWorkspacesJobsOutputRetrieve({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "job_id": "string-value",
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `job_id` | string | ✓ | Slurm job ID |
    | `uuid` | string (uuid) | ✓ |  |


=== "Query Parameters"

    | Name | Type | Description |
    |---|---|---|
    | `lines` | integer | _Default: `100`_ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `job` | object |  |
    | `job.job_id` | string |  |
    | `job.name` | string |  |
    | `job.state` | string |  |
    | `job.state_reason` | string |  |
    | `job.exit_code` | integer |  |
    | `job.account` | string |  |
    | `job.partition` | string |  |
    | `job.user` | string |  |
    | `job.nodes` | string |  |
    | `job.allocation_nodes` | integer |  |
    | `job.working_directory` | string |  |
    | `job.start_time` | integer |  |
    | `job.end_time` | integer |  |
    | `job.elapsed` | integer | Seconds |
    | `job.time_limit` | integer | Seconds (FirecREST converts Slurm's minutes) |
    | `job.submit_time` | integer |  |
    | `job.wait_seconds` | integer | From submission to start |
    | `job.allocation_cpus` | integer |  |
    | `job.requested_memory_mb` | integer |  |
    | `job.cpu_time_seconds` | integer |  |
    | `job.cpu_hours` | number (double) | Allocated CPUs x elapsed time |
    | `job.cpu_efficiency` | number (double) | CPU time / (CPUs x elapsed), 0..1; finished jobs only |
    | `job.max_rss_mb` | integer |  |
    | `job.memory_efficiency` | number (double) | Peak RSS / requested memory, 0..1; finished jobs only |
    | `job.allocation_gpus` | integer |  |
    | `job.gpu_hours` | number (double) | Allocated GPUs x elapsed time |
    | `job.energy_kwh` | number (double) | Energy consumed; where accounting records the energy TRES |
    | `job.mean_power_w` | integer | Energy / elapsed time, all of the job's nodes |
    | `script` | string |  |
    | `standard_output` | object |  |
    | `standard_output.path` | string |  |
    | `standard_output.content` | string |  |
    | `standard_error` | object |  |
    | `standard_error.path` | string |  |
    | `standard_error.content` | string |  |


=== "Authorization"

    The workspace acts on the cluster as the user, with their identity provider token, and no permission scopes that down. So only the user's own sign-in may use it, not a personal access token, an identity provider token or impersonation (see ``is_delegated``).

---

### Download the performance report of a job as PDF

The job's accounting, summary figures, charts and processes from the cluster monitor, as one PDF. Without monitor samples the report keeps the accounting and says why.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/hpc-workspaces/a1b2c3d4-e5f6-7890-abcd-ef1234567890/jobs/string-value/performance_pdf/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.hpc_workspaces import hpc_workspaces_jobs_performance_pdf_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = hpc_workspaces_jobs_performance_pdf_retrieve.sync(
        job_id="string-value",
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`hpc_workspaces_jobs_performance_pdf_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/hpc_workspaces/hpc_workspaces_jobs_performance_pdf_retrieve.py)

=== "TypeScript"

    ```typescript
    import { hpcWorkspacesJobsPerformancePdfRetrieve } from 'waldur-js-client';
    
    try {
      const response = await hpcWorkspacesJobsPerformancePdfRetrieve({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "job_id": "string-value",
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `job_id` | string | ✓ | Slurm job ID |
    | `uuid` | string (uuid) | ✓ |  |


=== "Responses"

    **`200`** - 
    


=== "Authorization"

    The workspace acts on the cluster as the user, with their identity provider token, and no permission scopes that down. So only the user's own sign-in may use it, not a personal access token, an identity provider token or impersonation (see ``is_delegated``).

---

### Get the performance of a job over its run

Per-GPU use, GPU memory and power, CPU cores and host memory over the job's run, and its busiest processes, from the cluster monitor (slurm-monitor with Sonar probes) as the signed-in user.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/hpc-workspaces/a1b2c3d4-e5f6-7890-abcd-ef1234567890/jobs/string-value/performance/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.hpc_workspaces import hpc_workspaces_jobs_performance_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = hpc_workspaces_jobs_performance_retrieve.sync(
        job_id="string-value",
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`hpc_workspaces_jobs_performance_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/hpc_workspaces/hpc_workspaces_jobs_performance_retrieve.py)

=== "TypeScript"

    ```typescript
    import { hpcWorkspacesJobsPerformanceRetrieve } from 'waldur-js-client';
    
    try {
      const response = await hpcWorkspacesJobsPerformanceRetrieve({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "job_id": "string-value",
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `job_id` | string | ✓ | Slurm job ID |
    | `uuid` | string (uuid) | ✓ |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `available` | boolean |  |
    | `message` | string | Why there is nothing to show, when not available |
    | `start_time` | integer | Epoch seconds |
    | `end_time` | integer | Epoch seconds |
    | `resolution` | integer | Seconds between points |
    | `summary` | object |  |
    | `summary.nodes` | integer |  |
    | `summary.gpus` | integer |  |
    | `summary.gpu_hours_observed` | number (double) | GPU samples x sample interval |
    | `summary.gpu_use_percent` | number (double) | Mean over the job's GPUs and samples |
    | `summary.idle_share_percent` | number (double) | Samples where every GPU of the job is under 5% |
    | `summary.gpu_memory_percent` | number (double) |  |
    | `summary.gpu_memory_peak_gib` | number (double) | Highest reading of one GPU |
    | `summary.gpu_memory_total_gib` | number (double) | Memory of one GPU |
    | `summary.gpu_power_watts` | number (double) | Mean per GPU |
    | `summary.cpu_cores_mean` | number (double) | Summed over the job's nodes |
    | `summary.host_memory_peak_gib` | number (double) |  |
    | `summary.host_memory_mean_gib` | number (double) |  |
    | `summary.samples` | integer |  |
    | `summary.coverage_percent` | number (double) | Sample times seen out of those expected |
    | `summary.first_sample` | integer | Epoch seconds |
    | `summary.last_sample` | integer | Epoch seconds |
    | `charts` | array of objects |  |
    | `charts.chart_type` | string | <br>_Enum: `line`, `area`, `bar`, `stacked_bar`, `scatter`, `heatmap`, `timeline`_ |
    | `charts.title` | string |  |
    | `charts.subtitle` | string |  |
    | `charts.x` | object |  |
    | `charts.x.type` | any |  |
    | `charts.x.label` | string |  |
    | `charts.x.unit` | string |  |
    | `charts.x.min` | number (double) |  |
    | `charts.x.max` | number (double) |  |
    | `charts.x.categories` | array of strings | Category labels, in order, for a category axis. |
    | `charts.y` | object |  |
    | `charts.y.type` | any |  |
    | `charts.y.label` | string |  |
    | `charts.y.unit` | string |  |
    | `charts.y.min` | number (double) |  |
    | `charts.y.max` | number (double) |  |
    | `charts.y.categories` | array of strings | Category labels, in order, for a category axis. |
    | `charts.y2` | any | Right-hand value axis. |
    | `charts.series` | array of objects |  |
    | `charts.series.name` | string |  |
    | `charts.series.style` | any |  |
    | `charts.series.tone` | string | <br>_Enum: `neutral`, `info`, `success`, `warning`, `danger`_ |
    | `charts.series.y_axis` | any | Secondary plots against `y2`, for a series in other units. |
    | `charts.series.points` | array of arrays | [x, y] pairs; heatmap [x, y, value]; timeline [row, start, end, limit_end]. |
    | `charts.series.labels` | array of strings | Tooltip text per point. |
    | `charts.series.ids` | array of strings | Identifier per point (e.g. a job ID) the page may link to. |
    | `charts.annotations` | array of objects |  |
    | `charts.annotations.type` | string | <br>_Enum: `line_x`, `line_y`, `area_x`, `area_y`_ |
    | `charts.annotations.value` | number (double) |  |
    | `charts.annotations.value_end` | number (double) |  |
    | `charts.annotations.label` | string |  |
    | `charts.annotations.tone` | any |  |
    | `charts.link` | object |  |
    | `charts.link.label` | string |  |
    | `charts.link.url` | string |  |
    | `charts.empty_message` | string | Shown instead of the chart when no series has points. |
    | `processes` | array of objects |  |
    | `processes.command` | string |  |
    | `processes.nodes` | integer |  |
    | `processes.samples` | integer |  |
    | `processes.mean_cpu_percent` | number (double) |  |
    | `processes.max_cpu_percent` | number (double) |  |
    | `processes.peak_rss_gib` | number (double) |  |
    | `warnings` | array of strings |  |


=== "Authorization"

    The workspace acts on the cluster as the user, with their identity provider token, and no permission scopes that down. So only the user's own sign-in may use it, not a personal access token, an identity provider token or impersonation (see ``is_delegated``).

---

### Get a job of the allocation


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/hpc-workspaces/a1b2c3d4-e5f6-7890-abcd-ef1234567890/jobs/string-value/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.hpc_workspaces import hpc_workspaces_jobs_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = hpc_workspaces_jobs_retrieve.sync(
        job_id="string-value",
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`hpc_workspaces_jobs_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/hpc_workspaces/hpc_workspaces_jobs_retrieve.py)

=== "TypeScript"

    ```typescript
    import { hpcWorkspacesJobsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await hpcWorkspacesJobsRetrieve({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "job_id": "string-value",
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `job_id` | string | ✓ | Slurm job ID |
    | `uuid` | string (uuid) | ✓ |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `job_id` | string |  |
    | `name` | string |  |
    | `state` | string |  |
    | `state_reason` | string |  |
    | `exit_code` | integer |  |
    | `account` | string |  |
    | `partition` | string |  |
    | `user` | string |  |
    | `nodes` | string |  |
    | `allocation_nodes` | integer |  |
    | `working_directory` | string |  |
    | `start_time` | integer |  |
    | `end_time` | integer |  |
    | `elapsed` | integer | Seconds |
    | `time_limit` | integer | Seconds (FirecREST converts Slurm's minutes) |
    | `submit_time` | integer |  |
    | `wait_seconds` | integer | From submission to start |
    | `allocation_cpus` | integer |  |
    | `requested_memory_mb` | integer |  |
    | `cpu_time_seconds` | integer |  |
    | `cpu_hours` | number (double) | Allocated CPUs x elapsed time |
    | `cpu_efficiency` | number (double) | CPU time / (CPUs x elapsed), 0..1; finished jobs only |
    | `max_rss_mb` | integer |  |
    | `memory_efficiency` | number (double) | Peak RSS / requested memory, 0..1; finished jobs only |
    | `allocation_gpus` | integer |  |
    | `gpu_hours` | number (double) | Allocated GPUs x elapsed time |
    | `energy_kwh` | number (double) | Energy consumed; where accounting records the energy TRES |
    | `mean_power_w` | integer | Energy / elapsed time, all of the job's nodes |


=== "Authorization"

    The workspace acts on the cluster as the user, with their identity provider token, and no permission scopes that down. So only the user's own sign-in may use it, not a personal access token, an identity provider token or impersonation (see ``is_delegated``).

---

### Plot a job output file

Reads a GROMACS .xvg, a CSV/TSV table or a WRF rsl log from the cluster and returns its series as a chart spec, with a short summary.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/hpc-workspaces/a1b2c3d4-e5f6-7890-abcd-ef1234567890/output_series/ \
      Authorization:"Token YOUR_API_TOKEN" \
      path=="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.hpc_workspaces import hpc_workspaces_output_series_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = hpc_workspaces_output_series_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        path="string-value"
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`hpc_workspaces_output_series_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/hpc_workspaces/hpc_workspaces_output_series_retrieve.py)

=== "TypeScript"

    ```typescript
    import { hpcWorkspacesOutputSeriesRetrieve } from 'waldur-js-client';
    
    try {
      const response = await hpcWorkspacesOutputSeriesRetrieve({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      query: {
        "path": "string-value"
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

    | Name | Type | Required | Description |
    |---|---|---|---|
    | `forecast_hours` | number (double) |  | WRF only: forecast length, if namelist.input next to the log does not say. |
    | `path` | string | ✓ |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `path` | string |  |
    | `kind` | string | <br>_Enum: `xvg`, `csv`, `wrf_rsl`_ |
    | `title` | string |  |
    | `summary` | object (free-form) |  |
    | `chart` | object |  |
    | `chart.chart_type` | string | <br>_Enum: `line`, `area`, `bar`, `stacked_bar`, `scatter`, `heatmap`, `timeline`_ |
    | `chart.title` | string |  |
    | `chart.subtitle` | string |  |
    | `chart.x` | object |  |
    | `chart.x.type` | any |  |
    | `chart.x.label` | string |  |
    | `chart.x.unit` | string |  |
    | `chart.x.min` | number (double) |  |
    | `chart.x.max` | number (double) |  |
    | `chart.x.categories` | array of strings | Category labels, in order, for a category axis. |
    | `chart.y` | object |  |
    | `chart.y.type` | any |  |
    | `chart.y.label` | string |  |
    | `chart.y.unit` | string |  |
    | `chart.y.min` | number (double) |  |
    | `chart.y.max` | number (double) |  |
    | `chart.y.categories` | array of strings | Category labels, in order, for a category axis. |
    | `chart.y2` | any | Right-hand value axis. |
    | `chart.series` | array of objects |  |
    | `chart.series.name` | string |  |
    | `chart.series.style` | any |  |
    | `chart.series.tone` | string | <br>_Enum: `neutral`, `info`, `success`, `warning`, `danger`_ |
    | `chart.series.y_axis` | any | Secondary plots against `y2`, for a series in other units. |
    | `chart.series.points` | array of arrays | [x, y] pairs; heatmap [x, y, value]; timeline [row, start, end, limit_end]. |
    | `chart.series.labels` | array of strings | Tooltip text per point. |
    | `chart.series.ids` | array of strings | Identifier per point (e.g. a job ID) the page may link to. |
    | `chart.annotations` | array of objects |  |
    | `chart.annotations.type` | string | <br>_Enum: `line_x`, `line_y`, `area_x`, `area_y`_ |
    | `chart.annotations.value` | number (double) |  |
    | `chart.annotations.value_end` | number (double) |  |
    | `chart.annotations.label` | string |  |
    | `chart.annotations.tone` | any |  |
    | `chart.link` | object |  |
    | `chart.link.label` | string |  |
    | `chart.link.url` | string |  |
    | `chart.empty_message` | string | Shown instead of the chart when no series has points. |


=== "Authorization"

    The workspace acts on the cluster as the user, with their identity provider token, and no permission scopes that down. So only the user's own sign-in may use it, not a personal access token, an identity provider token or impersonation (see ``is_delegated``).

---

### Partitions of the cluster

Partitions the provider publishes in Waldur (limits, QoS, architecture) merged with what the cluster reports live through FirecREST (node counts).


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/hpc-workspaces/a1b2c3d4-e5f6-7890-abcd-ef1234567890/partitions/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.hpc_workspaces import hpc_workspaces_partitions_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = hpc_workspaces_partitions_list.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`hpc_workspaces_partitions_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/hpc_workspaces/hpc_workspaces_partitions_list.py)

=== "TypeScript"

    ```typescript
    import { hpcWorkspacesPartitionsList } from 'waldur-js-client';
    
    try {
      const response = await hpcWorkspacesPartitionsList({
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
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `name` | string |  |
    | `published` | boolean | The provider publishes this partition in Waldur. |
    | `live` | boolean | The cluster reports this partition. |
    | `total_nodes` | integer |  |
    | `idle_nodes` | integer |  |
    | `cpus` | integer |  |
    | `max_time` | integer | Minutes |
    | `default_time` | integer | Minutes |
    | `max_nodes` | integer |  |
    | `max_cpus_per_node` | integer |  |
    | `max_mem_per_node` | integer | MB |
    | `cpu_arch` | string |  |
    | `gpu_arch` | string |  |
    | `qos` | array of strings |  |
    | `default_qos` | string |  |


=== "Authorization"

    The workspace acts on the cluster as the user, with their identity provider token, and no permission scopes that down. So only the user's own sign-in may use it, not a personal access token, an identity provider token or impersonation (see ``is_delegated``).

---

### Find software available on the cluster

Searches the offering's software catalogs (EESSI, Spack, ...); with a partition, only builds for its CPU architecture. Returns the lines a batch script needs.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/hpc-workspaces/a1b2c3d4-e5f6-7890-abcd-ef1234567890/software/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.hpc_workspaces import hpc_workspaces_software_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = hpc_workspaces_software_list.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`hpc_workspaces_software_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/hpc_workspaces/hpc_workspaces_software_list.py)

=== "TypeScript"

    ```typescript
    import { hpcWorkspacesSoftwareList } from 'waldur-js-client';
    
    try {
      const response = await hpcWorkspacesSoftwareList({
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


=== "Query Parameters"

    | Name | Type | Description |
    |---|---|---|
    | `partition` | string | _Default: ``_ |
    | `query` | string | _Default: ``_ |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `name` | string |  |
    | `version` | string |  |
    | `catalog` | string |  |
    | `catalog_type` | string |  |
    | `description` | string |  |
    | `setup` | array of strings | Lines making the catalog available, placed before 'load'. |
    | `load` | string | Line loading this version in a job. |
    | `cpu_families` | array of strings |  |
    | `gpu_architectures` | array of strings |  |


=== "Authorization"

    The workspace acts on the cluster as the user, with their identity provider token, and no permission scopes that down. So only the user's own sign-in may use it, not a personal access token, an identity provider token or impersonation (see ``is_delegated``).

---

### Usage of the allocation against its limits

Consumption of each limited component in the current limit period from Waldur's usage records, per user, with a run-out forecast at the recent pace.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/hpc-workspaces/a1b2c3d4-e5f6-7890-abcd-ef1234567890/usage/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.hpc_workspaces import hpc_workspaces_usage_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = hpc_workspaces_usage_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`hpc_workspaces_usage_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/hpc_workspaces/hpc_workspaces_usage_retrieve.py)

=== "TypeScript"

    ```typescript
    import { hpcWorkspacesUsageRetrieve } from 'waldur-js-client';
    
    try {
      const response = await hpcWorkspacesUsageRetrieve({
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
    | `as_of` | string (date) |  |
    | `components` | array of objects |  |
    | `components.type` | string |  |
    | `components.name` | string |  |
    | `components.unit` | string |  |
    | `components.limit` | number (double) |  |
    | `components.limit_period` | string |  |
    | `components.period_start` | string (date) |  |
    | `components.period_end` | string (date) |  |
    | `components.consumed` | number (double) |  |
    | `components.percent` | number (double) |  |
    | `components.daily_rate` | number (double) |  |
    | `components.runs_out` | string (date) |  |
    | `components.runs_out_before_period_end` | boolean |  |
    | `components.cumulative` | array of objects |  |
    | `components.cumulative.date` | string (date) |  |
    | `components.cumulative.value` | number (double) |  |
    | `components.monthly` | array of objects |  |
    | `components.monthly.month` | string (date) |  |
    | `components.monthly.value` | number (double) |  |
    | `components.users` | array of objects |  |
    | `components.users.username` | string |  |
    | `components.users.total` | number (double) |  |
    | `components.users.monthly` | array of objects |  |
    | `components.users.monthly.month` | string (date) |  |
    | `components.users.monthly.value` | number (double) |  |
    | `charts` | array of objects |  |
    | `charts.chart_type` | string | <br>_Enum: `line`, `area`, `bar`, `stacked_bar`, `scatter`, `heatmap`, `timeline`_ |
    | `charts.title` | string |  |
    | `charts.subtitle` | string |  |
    | `charts.x` | object |  |
    | `charts.x.type` | any |  |
    | `charts.x.label` | string |  |
    | `charts.x.unit` | string |  |
    | `charts.x.min` | number (double) |  |
    | `charts.x.max` | number (double) |  |
    | `charts.x.categories` | array of strings | Category labels, in order, for a category axis. |
    | `charts.y` | object |  |
    | `charts.y.type` | any |  |
    | `charts.y.label` | string |  |
    | `charts.y.unit` | string |  |
    | `charts.y.min` | number (double) |  |
    | `charts.y.max` | number (double) |  |
    | `charts.y.categories` | array of strings | Category labels, in order, for a category axis. |
    | `charts.y2` | any | Right-hand value axis. |
    | `charts.series` | array of objects |  |
    | `charts.series.name` | string |  |
    | `charts.series.style` | any |  |
    | `charts.series.tone` | string | <br>_Enum: `neutral`, `info`, `success`, `warning`, `danger`_ |
    | `charts.series.y_axis` | any | Secondary plots against `y2`, for a series in other units. |
    | `charts.series.points` | array of arrays | [x, y] pairs; heatmap [x, y, value]; timeline [row, start, end, limit_end]. |
    | `charts.series.labels` | array of strings | Tooltip text per point. |
    | `charts.series.ids` | array of strings | Identifier per point (e.g. a job ID) the page may link to. |
    | `charts.annotations` | array of objects |  |
    | `charts.annotations.type` | string | <br>_Enum: `line_x`, `line_y`, `area_x`, `area_y`_ |
    | `charts.annotations.value` | number (double) |  |
    | `charts.annotations.value_end` | number (double) |  |
    | `charts.annotations.label` | string |  |
    | `charts.annotations.tone` | any |  |
    | `charts.link` | object |  |
    | `charts.link.label` | string |  |
    | `charts.link.url` | string |  |
    | `charts.empty_message` | string | Shown instead of the chart when no series has points. |


=== "Authorization"

    The workspace acts on the cluster as the user, with their identity provider token, and no permission scopes that down. So only the user's own sign-in may use it, not a personal access token, an identity provider token or impersonation (see ``is_delegated``).

---

### Submit a job to the allocation

Renders the batch script from the parameters, checks them against the published partition and QoS limits and submits it under the allocation's account.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/hpc-workspaces/a1b2c3d4-e5f6-7890-abcd-ef1234567890/jobs/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-hpc-workspace" \
      commands="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.hpc_job_spec_request import HpcJobSpecRequest # (1)
    from waldur_api_client.api.hpc_workspaces import hpc_workspaces_jobs # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = HpcJobSpecRequest(
        name="my-awesome-hpc-workspace",
        commands="string-value"
    )
    response = hpc_workspaces_jobs.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`HpcJobSpecRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/hpc_job_spec_request.py)
    2.  **API Source:** [`hpc_workspaces_jobs`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/hpc_workspaces/hpc_workspaces_jobs.py)

=== "TypeScript"

    ```typescript
    import { hpcWorkspacesJobs } from 'waldur-js-client';
    
    try {
      const response = await hpcWorkspacesJobs({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "name": "my-awesome-hpc-workspace",
        "commands": "string-value"
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
    | `name` | string | ✓ |  |
    | `commands` | string | ✓ | Shell commands the job runs. |
    | `partition` | string |  | <br>_Constraints: default: ``_ |
    | `qos` | string |  | <br>_Constraints: default: ``_ |
    | `nodes` | integer |  | <br>_Constraints: default: `1`_ |
    | `ntasks_per_node` | integer |  | <br>_Constraints: default: `1`_ |
    | `cpus_per_task` | integer |  | <br>_Constraints: default: `1`_ |
    | `memory_mb` | integer |  |  |
    | `time_limit_minutes` | integer |  | <br>_Constraints: default: `60`_ |
    | `gpus_per_node` | integer |  | <br>_Constraints: default: `0`_ |
    | `modules` | array of strings |  | Setup lines, e.g. 'module load GROMACS/2024.1-foss-2023b'. |
    | `working_directory` | string |  | <br>_Constraints: default: ``_ |
    | `environment` | object (free-form) |  |  |
    | `files` | array of objects |  | Files written into the working directory before the commands run, such as the program the job runs. |
    | `files.name` | string | ✓ | File name in the job's working directory, e.g. 'matmul.py'. |
    | `files.content` | string | ✓ | File content. |


=== "Responses"

    **`201`** - 
    
    | Field | Type |
    |---|---|
    | `job_id` | string |
    | `script` | string |
    | `warnings` | array of strings |


=== "Authorization"

    The workspace acts on the cluster as the user, with their identity provider token, and no permission scopes that down. So only the user's own sign-in may use it, not a personal access token, an identity provider token or impersonation (see ``is_delegated``).

---

### Cancel a job of the allocation


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/hpc-workspaces/a1b2c3d4-e5f6-7890-abcd-ef1234567890/jobs/string-value/cancel/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.hpc_workspaces import hpc_workspaces_jobs_cancel # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = hpc_workspaces_jobs_cancel.sync(
        job_id="string-value",
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`hpc_workspaces_jobs_cancel`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/hpc_workspaces/hpc_workspaces_jobs_cancel.py)

=== "TypeScript"

    ```typescript
    import { hpcWorkspacesJobsCancel } from 'waldur-js-client';
    
    try {
      const response = await hpcWorkspacesJobsCancel({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "job_id": "string-value",
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `job_id` | string | ✓ | Slurm job ID |
    | `uuid` | string (uuid) | ✓ |  |


=== "Responses"

    **`204`** - No response body
    


=== "Authorization"

    The workspace acts on the cluster as the user, with their identity provider token, and no permission scopes that down. So only the user's own sign-in may use it, not a personal access token, an identity provider token or impersonation (see ``is_delegated``).

---

### Preview a batch script

Renders the batch script for the parameters and validates them, without submitting.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/hpc-workspaces/a1b2c3d4-e5f6-7890-abcd-ef1234567890/preview_script/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-hpc-workspace" \
      commands="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.hpc_job_spec_request import HpcJobSpecRequest # (1)
    from waldur_api_client.api.hpc_workspaces import hpc_workspaces_preview_script # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = HpcJobSpecRequest(
        name="my-awesome-hpc-workspace",
        commands="string-value"
    )
    response = hpc_workspaces_preview_script.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`HpcJobSpecRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/hpc_job_spec_request.py)
    2.  **API Source:** [`hpc_workspaces_preview_script`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/hpc_workspaces/hpc_workspaces_preview_script.py)

=== "TypeScript"

    ```typescript
    import { hpcWorkspacesPreviewScript } from 'waldur-js-client';
    
    try {
      const response = await hpcWorkspacesPreviewScript({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "name": "my-awesome-hpc-workspace",
        "commands": "string-value"
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
    | `name` | string | ✓ |  |
    | `commands` | string | ✓ | Shell commands the job runs. |
    | `partition` | string |  | <br>_Constraints: default: ``_ |
    | `qos` | string |  | <br>_Constraints: default: ``_ |
    | `nodes` | integer |  | <br>_Constraints: default: `1`_ |
    | `ntasks_per_node` | integer |  | <br>_Constraints: default: `1`_ |
    | `cpus_per_task` | integer |  | <br>_Constraints: default: `1`_ |
    | `memory_mb` | integer |  |  |
    | `time_limit_minutes` | integer |  | <br>_Constraints: default: `60`_ |
    | `gpus_per_node` | integer |  | <br>_Constraints: default: `0`_ |
    | `modules` | array of strings |  | Setup lines, e.g. 'module load GROMACS/2024.1-foss-2023b'. |
    | `working_directory` | string |  | <br>_Constraints: default: ``_ |
    | `environment` | object (free-form) |  |  |
    | `files` | array of objects |  | Files written into the working directory before the commands run, such as the program the job runs. |
    | `files.name` | string | ✓ | File name in the job's working directory, e.g. 'matmul.py'. |
    | `files.content` | string | ✓ | File content. |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `script` | string |
    | `errors` | array of strings |
    | `warnings` | array of strings |


=== "Authorization"

    The workspace acts on the cluster as the user, with their identity provider token, and no permission scopes that down. So only the user's own sign-in may use it, not a personal access token, an identity provider token or impersonation (see ``is_delegated``).

---
