# Openportal

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/openportal/access_for_email/` | [Access for email](#access-for-email) |
| <span class="http-badge http-get">GET</span> | `/api/openportal-accounting-summary/` | [List Openportal Accounting Summary](#list-openportal-accounting-summary) |
| <span class="http-badge http-get">GET</span> | `/api/openportal-accounting-summary/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-get">GET</span> | `/api/openportal/offering_mapping/` | [Offering mapping](#offering-mapping) |
| <span class="http-badge http-get">GET</span> | `/api/openportal/project_mapping/` | [Project mapping](#project-mapping) |
| <span class="http-badge http-get">GET</span> | `/api/openportal-project-storage-reports/` | [List Openportal Project Storage Reports](#list-openportal-project-storage-reports) |
| <span class="http-badge http-get">GET</span> | `/api/openportal-project-storage-reports/{id}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-get">GET</span> | `/api/openportal-project-usage-reports/` | [List Openportal Project Usage Reports](#list-openportal-project-usage-reports) |
| <span class="http-badge http-get">GET</span> | `/api/openportal-project-usage-reports/{id}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-get">GET</span> | `/api/openportal/user_mapping/` | [User mapping](#user-mapping) |

---

### Access for email


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openportal/access_for_email/ \
      Authorization:"Token YOUR_API_TOKEN" \
      q=="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openportal import openportal_access_for_email_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openportal_access_for_email_list.sync(
        client=client,
        q="string-value"
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`openportal_access_for_email_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal/openportal_access_for_email_list.py)

=== "TypeScript"

    ```typescript
    import { openportalAccessForEmailList } from 'waldur-js-client';
    
    try {
      const response = await openportalAccessForEmailList({
      auth: "Token YOUR_API_TOKEN",
      query: {
        "q": "string-value"
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
    | `q` | string | ✓ | Free text search query (email, short_name, project_name, or project_id) |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `email` | string (email) |
    | `status` | string |
    | `short_name` | string |
    | `projects` | object (free-form) |
    | `invited_by` | string |
    | `reason` | string |

---

### List Openportal Accounting Summary


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openportal-accounting-summary/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openportal_accounting_summary import openportal_accounting_summary_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openportal_accounting_summary_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`openportal_accounting_summary_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal_accounting_summary/openportal_accounting_summary_list.py)

=== "TypeScript"

    ```typescript
    import { openportalAccountingSummaryList } from 'waldur-js-client';
    
    try {
      const response = await openportalAccountingSummaryList({
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
    | `customer_uuid` | string (uuid) |  |
    | `is_active` | boolean |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `project_uuid` | string (uuid) |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `project_uuid` | string (uuid) |
    | `project_name` | string |
    | `customer_uuid` | string (uuid) |
    | `customer_name` | string |
    | `start_date` | string (date) |
    | `end_date` | string (date) |
    | `total_credits` | string (decimal) |
    | `total_spend` | string (decimal) |
    | `current_month_spend` | string (decimal) |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openportal-accounting-summary/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openportal_accounting_summary import openportal_accounting_summary_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openportal_accounting_summary_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openportal_accounting_summary_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal_accounting_summary/openportal_accounting_summary_retrieve.py)

=== "TypeScript"

    ```typescript
    import { openportalAccountingSummaryRetrieve } from 'waldur-js-client';
    
    try {
      const response = await openportalAccountingSummaryRetrieve({
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
    
    | Field | Type |
    |---|---|
    | `project_uuid` | string (uuid) |
    | `project_name` | string |
    | `customer_uuid` | string (uuid) |
    | `customer_name` | string |
    | `start_date` | string (date) |
    | `end_date` | string (date) |
    | `total_credits` | string (decimal) |
    | `total_spend` | string (decimal) |
    | `current_month_spend` | string (decimal) |

---

### Offering mapping

Map OpenPortal destination strings to Waldur Offering objects. Pass each destination as a repeated 'identifier' query parameter. Returns a dict keyed by identifier; unknown destinations map to null. Accessible to all authenticated users.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openportal/offering_mapping/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openportal import openportal_offering_mapping_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openportal_offering_mapping_retrieve.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openportal_offering_mapping_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal/openportal_offering_mapping_retrieve.py)

=== "TypeScript"

    ```typescript
    import { openportalOfferingMappingRetrieve } from 'waldur-js-client';
    
    try {
      const response = await openportalOfferingMappingRetrieve({
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
    | `identifier` | array | OpenPortal destination string (repeatable). |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `uuid` | string |
    | `name` | string |
    | `description` | string |
    | `slug` | string |

---

### Project mapping

Map OpenPortal ProjectIdentifier strings to Waldur Project objects. Pass each identifier as a repeated 'identifier' query parameter. Returns a dict keyed by identifier; unknown identifiers map to null. Staff and support see all projects; regular users see only projects they are a member of.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openportal/project_mapping/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openportal import openportal_project_mapping_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openportal_project_mapping_retrieve.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openportal_project_mapping_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal/openportal_project_mapping_retrieve.py)

=== "TypeScript"

    ```typescript
    import { openportalProjectMappingRetrieve } from 'waldur-js-client';
    
    try {
      const response = await openportalProjectMappingRetrieve({
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
    | `identifier` | array | OpenPortal ProjectIdentifier string (repeatable). |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `uuid` | string |
    | `name` | string |
    | `customer_uuid` | string |
    | `customer_name` | string |

---

### List Openportal Project Storage Reports


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openportal-project-storage-reports/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openportal_project_storage_reports import openportal_project_storage_reports_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openportal_project_storage_reports_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`openportal_project_storage_reports_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal_project_storage_reports/openportal_project_storage_reports_list.py)

=== "TypeScript"

    ```typescript
    import { openportalProjectStorageReportsList } from 'waldur-js-client';
    
    try {
      const response = await openportalProjectStorageReportsList({
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
    | `month` | integer |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `project_identifier` | string |  |
    | `project_uuid` | string (uuid) |  |
    | `resource` | string |  |
    | `year` | integer |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `id` | integer |  |
    | `year` | integer |  |
    | `month` | integer |  |
    | `project_identifier` | string |  |
    | `resource` | string |  |
    | `report` | object |  |
    | `report.project` | string |  |
    | `report.generated_at` | string | RFC3339 timestamp |
    | `report.project_quotas` | object (free-form) | Volume → Quota |
    | `report.user_quotas` | object (free-form) | UserIdentifier → (Volume → Quota) |
    | `report.users` | object (free-form) | UserIdentifier → local_username |
    | `report.daily_reports` | object (free-form) | "YYYY-MM-DD" → DailyStorageReportJson. Absent from JSON when there are no daily snapshots. |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openportal-project-storage-reports/123/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openportal_project_storage_reports import openportal_project_storage_reports_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openportal_project_storage_reports_retrieve.sync(
        id=123,
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openportal_project_storage_reports_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal_project_storage_reports/openportal_project_storage_reports_retrieve.py)

=== "TypeScript"

    ```typescript
    import { openportalProjectStorageReportsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await openportalProjectStorageReportsRetrieve({
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
    | `id` | integer | ✓ | A unique integer value identifying this cached project storage report. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `id` | integer |  |
    | `year` | integer |  |
    | `month` | integer |  |
    | `project_identifier` | string |  |
    | `resource` | string |  |
    | `report` | object |  |
    | `report.project` | string |  |
    | `report.generated_at` | string | RFC3339 timestamp |
    | `report.project_quotas` | object (free-form) | Volume → Quota |
    | `report.user_quotas` | object (free-form) | UserIdentifier → (Volume → Quota) |
    | `report.users` | object (free-form) | UserIdentifier → local_username |
    | `report.daily_reports` | object (free-form) | "YYYY-MM-DD" → DailyStorageReportJson. Absent from JSON when there are no daily snapshots. |

---

### List Openportal Project Usage Reports


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openportal-project-usage-reports/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openportal_project_usage_reports import openportal_project_usage_reports_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openportal_project_usage_reports_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`openportal_project_usage_reports_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal_project_usage_reports/openportal_project_usage_reports_list.py)

=== "TypeScript"

    ```typescript
    import { openportalProjectUsageReportsList } from 'waldur-js-client';
    
    try {
      const response = await openportalProjectUsageReportsList({
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
    | `is_complete` | boolean |  |
    | `month` | integer |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `project_identifier` | string |  |
    | `project_uuid` | string (uuid) |  |
    | `resource` | string |  |
    | `year` | integer |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `id` | integer |  |
    | `year` | integer |  |
    | `month` | integer |  |
    | `project_identifier` | string |  |
    | `resource` | string |  |
    | `is_complete` | boolean |  |
    | `report` | object |  |
    | `report.project` | string | ProjectIdentifier string e.g. "aiproject.brics" |
    | `report.reports` | object (free-form) | "YYYY-MM-DD" → DailyProjectUsageReportJson |
    | `report.users` | object (free-form) | UserIdentifier → local_username. e.g. { "chris.aiproject.brics": "chris.aiproject" } |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openportal-project-usage-reports/123/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openportal_project_usage_reports import openportal_project_usage_reports_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openportal_project_usage_reports_retrieve.sync(
        id=123,
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openportal_project_usage_reports_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal_project_usage_reports/openportal_project_usage_reports_retrieve.py)

=== "TypeScript"

    ```typescript
    import { openportalProjectUsageReportsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await openportalProjectUsageReportsRetrieve({
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
    | `id` | integer | ✓ | A unique integer value identifying this cached project usage report. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `id` | integer |  |
    | `year` | integer |  |
    | `month` | integer |  |
    | `project_identifier` | string |  |
    | `resource` | string |  |
    | `is_complete` | boolean |  |
    | `report` | object |  |
    | `report.project` | string | ProjectIdentifier string e.g. "aiproject.brics" |
    | `report.reports` | object (free-form) | "YYYY-MM-DD" → DailyProjectUsageReportJson |
    | `report.users` | object (free-form) | UserIdentifier → local_username. e.g. { "chris.aiproject.brics": "chris.aiproject" } |

---

### User mapping

Map OpenPortal UserIdentifier strings (or email addresses) to Waldur User objects. Pass each value as a repeated 'identifier' query parameter. If the values contain '@' they are treated as email addresses (used for cached reports from remote portals); otherwise they are treated as UserIdentifier strings (used for local OpenPortal resources). Returns a dict keyed by the supplied string; unknown values map to null. Staff and support see all users; regular users may only look up users who share a project with them.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openportal/user_mapping/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openportal import openportal_user_mapping_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openportal_user_mapping_retrieve.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openportal_user_mapping_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal/openportal_user_mapping_retrieve.py)

=== "TypeScript"

    ```typescript
    import { openportalUserMappingRetrieve } from 'waldur-js-client';
    
    try {
      const response = await openportalUserMappingRetrieve({
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
    | `identifier` | array | OpenPortal UserIdentifier string or email address (repeatable). All values in a single request must be the same type. |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `uuid` | string |
    | `full_name` | string |
    | `email` | string (email) |
    | `username` | string |

---
