# Openportal

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/openportal-accounting-summary/` | [List Openportal Accounting Summary](#list-openportal-accounting-summary) |
| <span class="http-badge http-get">GET</span> | `/api/openportal-accounting-summary/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-get">GET</span> | `/api/openportal-project-storage-reports/` | [List Openportal Project Storage Reports](#list-openportal-project-storage-reports) |
| <span class="http-badge http-get">GET</span> | `/api/openportal-project-storage-reports/{id}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-get">GET</span> | `/api/openportal-project-usage-reports/` | [List Openportal Project Usage Reports](#list-openportal-project-usage-reports) |
| <span class="http-badge http-get">GET</span> | `/api/openportal-project-usage-reports/{id}/` | [Retrieve](#retrieve) |

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
    
    | Field | Type |
    |---|---|
    | `id` | integer |
    | `year` | integer |
    | `month` | integer |
    | `project_identifier` | string |
    | `resource` | string |
    | `report` | any |

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
    
    | Field | Type |
    |---|---|
    | `id` | integer |
    | `year` | integer |
    | `month` | integer |
    | `project_identifier` | string |
    | `resource` | string |
    | `report` | any |

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
    
    | Field | Type |
    |---|---|
    | `id` | integer |
    | `year` | integer |
    | `month` | integer |
    | `project_identifier` | string |
    | `resource` | string |
    | `is_complete` | boolean |
    | `report` | any |

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
    
    | Field | Type |
    |---|---|
    | `id` | integer |
    | `year` | integer |
    | `month` | integer |
    | `project_identifier` | string |
    | `resource` | string |
    | `is_complete` | boolean |
    | `report` | any |

---
