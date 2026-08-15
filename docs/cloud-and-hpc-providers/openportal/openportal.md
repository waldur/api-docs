# Openportal

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/openportal/access_for_email/` | [Access for email](#access-for-email) |
| <span class="http-badge http-get">GET</span> | `/api/openportal-accounting-summary/` | [List Openportal Accounting Summary](#list-openportal-accounting-summary) |
| <span class="http-badge http-get">GET</span> | `/api/openportal-accounting-summary/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-get">GET</span> | `/api/openportal-managed-project-audit/` | [List Openportal Managed Project Audit](#list-openportal-managed-project-audit) |
| <span class="http-badge http-get">GET</span> | `/api/openportal-managed-project-audit/{id}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-get">GET</span> | `/api/openportal/offering_mapping/` | [Offering mapping](#offering-mapping) |
| <span class="http-badge http-get">GET</span> | `/api/openportal/project_email_policy/{project_uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-get">GET</span> | `/api/openportal/project_mapping/` | [Project mapping](#project-mapping) |
| <span class="http-badge http-get">GET</span> | `/api/openportal-project-storage-reports/` | [List Openportal Project Storage Reports](#list-openportal-project-storage-reports) |
| <span class="http-badge http-get">GET</span> | `/api/openportal-project-storage-reports/{id}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-get">GET</span> | `/api/openportal-project-usage-reports/` | [List Openportal Project Usage Reports](#list-openportal-project-usage-reports) |
| <span class="http-badge http-get">GET</span> | `/api/openportal-project-usage-reports/{id}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-get">GET</span> | `/api/openportal-remote-project-allocations/` | [List Openportal Remote Project Allocations](#list-openportal-remote-project-allocations) |
| <span class="http-badge http-get">GET</span> | `/api/openportal-remote-project-allocations/{id}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-get">GET</span> | `/api/openportal-remote-project-audit/` | [List Openportal Remote Project Audit](#list-openportal-remote-project-audit) |
| <span class="http-badge http-get">GET</span> | `/api/openportal-remote-project-audit/{id}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-get">GET</span> | `/api/openportal-remote-projects/` | [List Openportal Remote Projects](#list-openportal-remote-projects) |
| <span class="http-badge http-get">GET</span> | `/api/openportal-remote-projects/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-get">GET</span> | `/api/openportal-remote-projects/{uuid}/total-usage/` | [Get total usage for remote project](#get-total-usage-for-remote-project) |
| <span class="http-badge http-get">GET</span> | `/api/openportal/user_mapping/` | [User mapping](#user-mapping) |
| <span class="http-badge http-post">POST</span> | `/api/openportal-remote-projects/{uuid}/add-note/` | [Add note to remote project](#add-note-to-remote-project) |
| <span class="http-badge http-post">POST</span> | `/api/openportal-remote-projects/{uuid}/approve-now/` | [Approve remote project now](#approve-remote-project-now) |
| <span class="http-badge http-post">POST</span> | `/api/openportal-remote-projects/{uuid}/hold-indefinitely/` | [Hold remote project indefinitely](#hold-remote-project-indefinitely) |
| <span class="http-badge http-post">POST</span> | `/api/openportal-remote-projects/{uuid}/resend-request/` | [Resend remote project request](#resend-remote-project-request) |
| <span class="http-badge http-post">POST</span> | `/api/openportal-remote-projects/{uuid}/reset-to-pending/` | [Reset remote project to pending](#reset-remote-project-to-pending) |
| <span class="http-badge http-post">POST</span> | `/api/openportal-remote-projects/{uuid}/set-allowed-domains/` | [Set allowed domains for remote project](#set-allowed-domains-for-remote-project) |
| <span class="http-badge http-post">POST</span> | `/api/openportal-remote-projects/{uuid}/set-earliest-approve/` | [Set earliest approve date for remote project](#set-earliest-approve-date-for-remote-project) |
| <span class="http-badge http-post">POST</span> | `/api/openportal-remote-projects/{uuid}/set-links/` | [Set links for remote project](#set-links-for-remote-project) |
| <span class="http-badge http-post">POST</span> | `/api/openportal-remote-projects/{uuid}/set-membership-control/` | [Set membership control for remote project](#set-membership-control-for-remote-project) |

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

### List Openportal Managed Project Audit


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openportal-managed-project-audit/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openportal_managed_project_audit import openportal_managed_project_audit_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openportal_managed_project_audit_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`openportal_managed_project_audit_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal_managed_project_audit/openportal_managed_project_audit_list.py)

=== "TypeScript"

    ```typescript
    import { openportalManagedProjectAuditList } from 'waldur-js-client';
    
    try {
      const response = await openportalManagedProjectAuditList({
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
    | `event_type` | string |  |
    | `managed_project_destination` | string |  |
    | `managed_project_identifier` | string |  |
    | `o` | string | Which field to use when ordering the results. |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `q` | string | Search |
    | `timestamp_after` | string (date-time) |  |
    | `timestamp_before` | string (date-time) |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `id` | integer |  |
    | `identifier` | string | Project identifier copied from ManagedProject at record time. |
    | `destination` | string | Destination copied from ManagedProject at record time. |
    | `timestamp` | string (date-time) |  |
    | `event_type` | string | <br>_Enum: `created`, `approved`, `rejected`, `deleted`, `note_added`, `details_updated`, `project_attached`, `project_detached`_ |
    | `previous_details` | any |  |
    | `new_details` | any |  |
    | `performed_by_full_name` | string |  |
    | `performed_by_uuid` | string (uuid) |  |
    | `note` | string | Optional free-text comment about this event. |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openportal-managed-project-audit/123/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openportal_managed_project_audit import openportal_managed_project_audit_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openportal_managed_project_audit_retrieve.sync(
        id=123,
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openportal_managed_project_audit_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal_managed_project_audit/openportal_managed_project_audit_retrieve.py)

=== "TypeScript"

    ```typescript
    import { openportalManagedProjectAuditRetrieve } from 'waldur-js-client';
    
    try {
      const response = await openportalManagedProjectAuditRetrieve({
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
    | `id` | integer | ✓ | A unique integer value identifying this Managed Project Audit Entry. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `id` | integer |  |
    | `identifier` | string | Project identifier copied from ManagedProject at record time. |
    | `destination` | string | Destination copied from ManagedProject at record time. |
    | `timestamp` | string (date-time) |  |
    | `event_type` | string | <br>_Enum: `created`, `approved`, `rejected`, `deleted`, `note_added`, `details_updated`, `project_attached`, `project_detached`_ |
    | `previous_details` | any |  |
    | `new_details` | any |  |
    | `performed_by_full_name` | string |  |
    | `performed_by_uuid` | string (uuid) |  |
    | `note` | string | Optional free-text comment about this event. |

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
    | `*` | any |

---

### Retrieve

Return the allowed_domains list for a project derived from its AwardDetails. null means no restriction; [] means nothing allowed; a list contains permitted domain globs and/or specific email addresses.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openportal/project_email_policy/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openportal import openportal_project_email_policy_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openportal_project_email_policy_retrieve.sync(
        project_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openportal_project_email_policy_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal/openportal_project_email_policy_retrieve.py)

=== "TypeScript"

    ```typescript
    import { openportalProjectEmailPolicyRetrieve } from 'waldur-js-client';
    
    try {
      const response = await openportalProjectEmailPolicyRetrieve({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "project_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `project_uuid` | string | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `allowed_domains` | array of strings |

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
    | `*` | any |

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

### List Openportal Remote Project Allocations


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openportal-remote-project-allocations/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openportal_remote_project_allocations import openportal_remote_project_allocations_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openportal_remote_project_allocations_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`openportal_remote_project_allocations_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal_remote_project_allocations/openportal_remote_project_allocations_list.py)

=== "TypeScript"

    ```typescript
    import { openportalRemoteProjectAllocationsList } from 'waldur-js-client';
    
    try {
      const response = await openportalRemoteProjectAllocationsList({
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
    | `o` | string | Which field to use when ordering the results. |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `project_uuid` | string (uuid) |  |
    | `remote_project_uuid` | string (uuid) |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `id` | integer |  |
    | `allocation` | string (decimal) | New total allocation (credits) after this change. |
    | `previous_allocation` | string (decimal) | Total allocation before this change.  Null for the first entry. |
    | `delta` | string (decimal) |  |
    | `source_project_name` | string |  |
    | `source_project_uuid` | string (uuid) |  |
    | `submitted_at` | string (date-time) |  |
    | `confirmed_at` | string (date-time) | When the remote portal confirmed this allocation.  Null if pending. |
    | `is_confirmed` | boolean |  |
    | `note` | string | Optional comment, e.g. 'carrying over 20 unused credits from previous award'. |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openportal-remote-project-allocations/123/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openportal_remote_project_allocations import openportal_remote_project_allocations_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openportal_remote_project_allocations_retrieve.sync(
        id=123,
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openportal_remote_project_allocations_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal_remote_project_allocations/openportal_remote_project_allocations_retrieve.py)

=== "TypeScript"

    ```typescript
    import { openportalRemoteProjectAllocationsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await openportalRemoteProjectAllocationsRetrieve({
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
    | `id` | integer | ✓ | A unique integer value identifying this Remote Project Allocation Entry. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `id` | integer |  |
    | `allocation` | string (decimal) | New total allocation (credits) after this change. |
    | `previous_allocation` | string (decimal) | Total allocation before this change.  Null for the first entry. |
    | `delta` | string (decimal) |  |
    | `source_project_name` | string |  |
    | `source_project_uuid` | string (uuid) |  |
    | `submitted_at` | string (date-time) |  |
    | `confirmed_at` | string (date-time) | When the remote portal confirmed this allocation.  Null if pending. |
    | `is_confirmed` | boolean |  |
    | `note` | string | Optional comment, e.g. 'carrying over 20 unused credits from previous award'. |

---

### List Openportal Remote Project Audit


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openportal-remote-project-audit/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openportal_remote_project_audit import openportal_remote_project_audit_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openportal_remote_project_audit_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`openportal_remote_project_audit_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal_remote_project_audit/openportal_remote_project_audit_list.py)

=== "TypeScript"

    ```typescript
    import { openportalRemoteProjectAuditList } from 'waldur-js-client';
    
    try {
      const response = await openportalRemoteProjectAuditList({
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
    | `event_type` | string |  |
    | `o` | string | Which field to use when ordering the results. |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `project_uuid` | string (uuid) |  |
    | `q` | string | Search |
    | `remote_project_uuid` | string (uuid) |  |
    | `timestamp_after` | string (date-time) |  |
    | `timestamp_before` | string (date-time) |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `id` | integer |  |
    | `timestamp` | string (date-time) |  |
    | `event_type` | string | <br>_Enum: `award_attempted`, `award_rejected`, `award_created`, `award_updated`, `award_update_confirmed`, `award_update_rejected`, `state_changed`, `resource_deleted`_ |
    | `previous_details` | any |  |
    | `new_details` | any |  |
    | `performed_by_full_name` | string |  |
    | `performed_by_uuid` | string (uuid) |  |
    | `remote_project_uuid` | string (uuid) |  |
    | `remote_project_url` | string (uri) |  |
    | `remote_response` | object (free-form) | Raw response received from the remote portal, if applicable. |
    | `note` | string | Optional free-text comment about this event. |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openportal-remote-project-audit/123/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openportal_remote_project_audit import openportal_remote_project_audit_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openportal_remote_project_audit_retrieve.sync(
        id=123,
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openportal_remote_project_audit_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal_remote_project_audit/openportal_remote_project_audit_retrieve.py)

=== "TypeScript"

    ```typescript
    import { openportalRemoteProjectAuditRetrieve } from 'waldur-js-client';
    
    try {
      const response = await openportalRemoteProjectAuditRetrieve({
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
    | `id` | integer | ✓ | A unique integer value identifying this Remote Project Audit Entry. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `id` | integer |  |
    | `timestamp` | string (date-time) |  |
    | `event_type` | string | <br>_Enum: `award_attempted`, `award_rejected`, `award_created`, `award_updated`, `award_update_confirmed`, `award_update_rejected`, `state_changed`, `resource_deleted`_ |
    | `previous_details` | any |  |
    | `new_details` | any |  |
    | `performed_by_full_name` | string |  |
    | `performed_by_uuid` | string (uuid) |  |
    | `remote_project_uuid` | string (uuid) |  |
    | `remote_project_url` | string (uri) |  |
    | `remote_response` | object (free-form) | Raw response received from the remote portal, if applicable. |
    | `note` | string | Optional free-text comment about this event. |

---

### List Openportal Remote Projects


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openportal-remote-projects/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.remote_project_state_enum import RemoteProjectStateEnum # (1)
    from waldur_api_client.api.openportal_remote_projects import openportal_remote_projects_list # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openportal_remote_projects_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`RemoteProjectStateEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/remote_project_state_enum.py)
    2.  **API Source:** [`openportal_remote_projects_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal_remote_projects/openportal_remote_projects_list.py)

=== "TypeScript"

    ```typescript
    import { openportalRemoteProjectsList } from 'waldur-js-client';
    
    try {
      const response = await openportalRemoteProjectsList({
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
    | `customer` | string (uri) |  |
    | `customer_uuid` | string (uuid) |  |
    | `destination` | string |  |
    | `identifier` | string |  |
    | `o` | string | Which field to use when ordering the results. |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `project` | string (uri) |  |
    | `project_uuid` | string (uuid) |  |
    | `query` | string |  |
    | `state` | array |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `destination` | string | Routing path from the local portal to the remote resource, e.g. 'airr.brics.isambard-ai'.  Never changes after creation. |
    | `identifier` | string | Stable remote project identifier, e.g. 'u6ac.brics'.  Uniquely identifies the project on the remote portal and never changes.  Null while the project is pending first approval. |
    | `resource_uuid` | string (uuid) |  |
    | `resource_name` | string |  |
    | `state` | string | <br>_Enum: `pending`, `active`, `stale`, `error`, `deleted`_ |
    | `state_display` | string |  |
    | `current_allocation` | string (decimal) | Latest confirmed allocation (credits) for this project.  Updated whenever a RemoteProjectAllocationEntry is confirmed. |
    | `pending_allocation` | string (decimal) | Allocation value currently under review on the remote portal.  Null when no allocation change is pending. |
    | `allocation_string` | string |  |
    | `link_award` | any |  |
    | `link_call` | any |  |
    | `link_project` | any |  |
    | `link_renewal` | any |  |
    | `membership_control` | any | Policy controlling whether the remote portal may independently modify project membership or roles. |
    | `allowed_domains` | array of strings |  |
    | `breakdown` | object (free-form) |  |
    | `last_sent_details` | any |  |
    | `last_confirmed_details` | any |  |
    | `pending_details` | any |  |
    | `award_details` | any |  |
    | `pending_since` | string (date-time) | When the currently pending change was submitted. |
    | `notes` | array of objects |  |
    | `notes.timestamp` | string (date-time) | When the note was created (UTC) |
    | `notes.author` | string | Name of the person who created the note |
    | `notes.text` | string | Free-text content of the note |
    | `earliest_approve` | string (date-time) |  |
    | `error_message` | string | The most recent rejection or error message received from the remote portal.  Cleared when the state transitions to ACTIVE. |
    | `has_pending_change` | boolean |  |
    | `current_project_name` | string |  |
    | `current_project_uuid` | string (uuid) |  |
    | `last_contact_time` | string (date-time) | The most recent time the remote portal acknowledged anything about this project (confirmation, usage report, get_award response, etc.).  Used to detect connectivity issues and to trigger a transition to the STALE state. |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openportal-remote-projects/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openportal_remote_projects import openportal_remote_projects_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openportal_remote_projects_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openportal_remote_projects_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal_remote_projects/openportal_remote_projects_retrieve.py)

=== "TypeScript"

    ```typescript
    import { openportalRemoteProjectsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await openportalRemoteProjectsRetrieve({
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
    | `destination` | string | Routing path from the local portal to the remote resource, e.g. 'airr.brics.isambard-ai'.  Never changes after creation. |
    | `identifier` | string | Stable remote project identifier, e.g. 'u6ac.brics'.  Uniquely identifies the project on the remote portal and never changes.  Null while the project is pending first approval. |
    | `resource_uuid` | string (uuid) |  |
    | `resource_name` | string |  |
    | `state` | string | <br>_Enum: `pending`, `active`, `stale`, `error`, `deleted`_ |
    | `state_display` | string |  |
    | `current_allocation` | string (decimal) | Latest confirmed allocation (credits) for this project.  Updated whenever a RemoteProjectAllocationEntry is confirmed. |
    | `pending_allocation` | string (decimal) | Allocation value currently under review on the remote portal.  Null when no allocation change is pending. |
    | `allocation_string` | string |  |
    | `link_award` | any |  |
    | `link_call` | any |  |
    | `link_project` | any |  |
    | `link_renewal` | any |  |
    | `membership_control` | any | Policy controlling whether the remote portal may independently modify project membership or roles. |
    | `allowed_domains` | array of strings |  |
    | `breakdown` | object (free-form) |  |
    | `last_sent_details` | any |  |
    | `last_confirmed_details` | any |  |
    | `pending_details` | any |  |
    | `award_details` | any |  |
    | `pending_since` | string (date-time) | When the currently pending change was submitted. |
    | `notes` | array of objects |  |
    | `notes.timestamp` | string (date-time) | When the note was created (UTC) |
    | `notes.author` | string | Name of the person who created the note |
    | `notes.text` | string | Free-text content of the note |
    | `earliest_approve` | string (date-time) |  |
    | `error_message` | string | The most recent rejection or error message received from the remote portal.  Cleared when the state transitions to ACTIVE. |
    | `has_pending_change` | boolean |  |
    | `current_project_name` | string |  |
    | `current_project_uuid` | string (uuid) |  |
    | `last_contact_time` | string (date-time) | The most recent time the remote portal acknowledged anything about this project (confirmation, usage report, get_award response, etc.).  Used to detect connectivity issues and to trigger a transition to the STALE state. |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Get total usage for remote project

Get total usage for remote project


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openportal-remote-projects/a1b2c3d4-e5f6-7890-abcd-ef1234567890/total-usage/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openportal_remote_projects import openportal_remote_projects_total_usage_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openportal_remote_projects_total_usage_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openportal_remote_projects_total_usage_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal_remote_projects/openportal_remote_projects_total_usage_retrieve.py)

=== "TypeScript"

    ```typescript
    import { openportalRemoteProjectsTotalUsageRetrieve } from 'waldur-js-client';
    
    try {
      const response = await openportalRemoteProjectsTotalUsageRetrieve({
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
    | `*` | any |

---

### Add note to remote project

Add note to remote project


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/openportal-remote-projects/a1b2c3d4-e5f6-7890-abcd-ef1234567890/add-note/ \
      Authorization:"Token YOUR_API_TOKEN" \
      text="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.add_note_request import AddNoteRequest # (1)
    from waldur_api_client.api.openportal_remote_projects import openportal_remote_projects_add_note # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = AddNoteRequest(
        text="string-value"
    )
    response = openportal_remote_projects_add_note.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`AddNoteRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/add_note_request.py)
    2.  **API Source:** [`openportal_remote_projects_add_note`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal_remote_projects/openportal_remote_projects_add_note.py)

=== "TypeScript"

    ```typescript
    import { openportalRemoteProjectsAddNote } from 'waldur-js-client';
    
    try {
      const response = await openportalRemoteProjectsAddNote({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "text": "string-value"
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

    | Field | Type | Required |
    |---|---|---|
    | `text` | string | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `destination` | string | Routing path from the local portal to the remote resource, e.g. 'airr.brics.isambard-ai'.  Never changes after creation. |
    | `identifier` | string | Stable remote project identifier, e.g. 'u6ac.brics'.  Uniquely identifies the project on the remote portal and never changes.  Null while the project is pending first approval. |
    | `resource_uuid` | string (uuid) |  |
    | `resource_name` | string |  |
    | `state` | string | <br>_Enum: `pending`, `active`, `stale`, `error`, `deleted`_ |
    | `state_display` | string |  |
    | `current_allocation` | string (decimal) | Latest confirmed allocation (credits) for this project.  Updated whenever a RemoteProjectAllocationEntry is confirmed. |
    | `pending_allocation` | string (decimal) | Allocation value currently under review on the remote portal.  Null when no allocation change is pending. |
    | `allocation_string` | string |  |
    | `link_award` | any |  |
    | `link_call` | any |  |
    | `link_project` | any |  |
    | `link_renewal` | any |  |
    | `membership_control` | any | Policy controlling whether the remote portal may independently modify project membership or roles. |
    | `allowed_domains` | array of strings |  |
    | `breakdown` | object (free-form) |  |
    | `last_sent_details` | any |  |
    | `last_confirmed_details` | any |  |
    | `pending_details` | any |  |
    | `award_details` | any |  |
    | `pending_since` | string (date-time) | When the currently pending change was submitted. |
    | `notes` | array of objects |  |
    | `notes.timestamp` | string (date-time) | When the note was created (UTC) |
    | `notes.author` | string | Name of the person who created the note |
    | `notes.text` | string | Free-text content of the note |
    | `earliest_approve` | string (date-time) |  |
    | `error_message` | string | The most recent rejection or error message received from the remote portal.  Cleared when the state transitions to ACTIVE. |
    | `has_pending_change` | boolean |  |
    | `current_project_name` | string |  |
    | `current_project_uuid` | string (uuid) |  |
    | `last_contact_time` | string (date-time) | The most recent time the remote portal acknowledged anything about this project (confirmation, usage report, get_award response, etc.).  Used to detect connectivity issues and to trigger a transition to the STALE state. |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Approve remote project now

Approve remote project now


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/openportal-remote-projects/a1b2c3d4-e5f6-7890-abcd-ef1234567890/approve-now/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openportal_remote_projects import openportal_remote_projects_approve_now # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openportal_remote_projects_approve_now.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openportal_remote_projects_approve_now`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal_remote_projects/openportal_remote_projects_approve_now.py)

=== "TypeScript"

    ```typescript
    import { openportalRemoteProjectsApproveNow } from 'waldur-js-client';
    
    try {
      const response = await openportalRemoteProjectsApproveNow({
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
    | `destination` | string | Routing path from the local portal to the remote resource, e.g. 'airr.brics.isambard-ai'.  Never changes after creation. |
    | `identifier` | string | Stable remote project identifier, e.g. 'u6ac.brics'.  Uniquely identifies the project on the remote portal and never changes.  Null while the project is pending first approval. |
    | `resource_uuid` | string (uuid) |  |
    | `resource_name` | string |  |
    | `state` | string | <br>_Enum: `pending`, `active`, `stale`, `error`, `deleted`_ |
    | `state_display` | string |  |
    | `current_allocation` | string (decimal) | Latest confirmed allocation (credits) for this project.  Updated whenever a RemoteProjectAllocationEntry is confirmed. |
    | `pending_allocation` | string (decimal) | Allocation value currently under review on the remote portal.  Null when no allocation change is pending. |
    | `allocation_string` | string |  |
    | `link_award` | any |  |
    | `link_call` | any |  |
    | `link_project` | any |  |
    | `link_renewal` | any |  |
    | `membership_control` | any | Policy controlling whether the remote portal may independently modify project membership or roles. |
    | `allowed_domains` | array of strings |  |
    | `breakdown` | object (free-form) |  |
    | `last_sent_details` | any |  |
    | `last_confirmed_details` | any |  |
    | `pending_details` | any |  |
    | `award_details` | any |  |
    | `pending_since` | string (date-time) | When the currently pending change was submitted. |
    | `notes` | array of objects |  |
    | `notes.timestamp` | string (date-time) | When the note was created (UTC) |
    | `notes.author` | string | Name of the person who created the note |
    | `notes.text` | string | Free-text content of the note |
    | `earliest_approve` | string (date-time) |  |
    | `error_message` | string | The most recent rejection or error message received from the remote portal.  Cleared when the state transitions to ACTIVE. |
    | `has_pending_change` | boolean |  |
    | `current_project_name` | string |  |
    | `current_project_uuid` | string (uuid) |  |
    | `last_contact_time` | string (date-time) | The most recent time the remote portal acknowledged anything about this project (confirmation, usage report, get_award response, etc.).  Used to detect connectivity issues and to trigger a transition to the STALE state. |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Hold remote project indefinitely

Hold remote project indefinitely


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/openportal-remote-projects/a1b2c3d4-e5f6-7890-abcd-ef1234567890/hold-indefinitely/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openportal_remote_projects import openportal_remote_projects_hold_indefinitely # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openportal_remote_projects_hold_indefinitely.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openportal_remote_projects_hold_indefinitely`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal_remote_projects/openportal_remote_projects_hold_indefinitely.py)

=== "TypeScript"

    ```typescript
    import { openportalRemoteProjectsHoldIndefinitely } from 'waldur-js-client';
    
    try {
      const response = await openportalRemoteProjectsHoldIndefinitely({
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
    | `destination` | string | Routing path from the local portal to the remote resource, e.g. 'airr.brics.isambard-ai'.  Never changes after creation. |
    | `identifier` | string | Stable remote project identifier, e.g. 'u6ac.brics'.  Uniquely identifies the project on the remote portal and never changes.  Null while the project is pending first approval. |
    | `resource_uuid` | string (uuid) |  |
    | `resource_name` | string |  |
    | `state` | string | <br>_Enum: `pending`, `active`, `stale`, `error`, `deleted`_ |
    | `state_display` | string |  |
    | `current_allocation` | string (decimal) | Latest confirmed allocation (credits) for this project.  Updated whenever a RemoteProjectAllocationEntry is confirmed. |
    | `pending_allocation` | string (decimal) | Allocation value currently under review on the remote portal.  Null when no allocation change is pending. |
    | `allocation_string` | string |  |
    | `link_award` | any |  |
    | `link_call` | any |  |
    | `link_project` | any |  |
    | `link_renewal` | any |  |
    | `membership_control` | any | Policy controlling whether the remote portal may independently modify project membership or roles. |
    | `allowed_domains` | array of strings |  |
    | `breakdown` | object (free-form) |  |
    | `last_sent_details` | any |  |
    | `last_confirmed_details` | any |  |
    | `pending_details` | any |  |
    | `award_details` | any |  |
    | `pending_since` | string (date-time) | When the currently pending change was submitted. |
    | `notes` | array of objects |  |
    | `notes.timestamp` | string (date-time) | When the note was created (UTC) |
    | `notes.author` | string | Name of the person who created the note |
    | `notes.text` | string | Free-text content of the note |
    | `earliest_approve` | string (date-time) |  |
    | `error_message` | string | The most recent rejection or error message received from the remote portal.  Cleared when the state transitions to ACTIVE. |
    | `has_pending_change` | boolean |  |
    | `current_project_name` | string |  |
    | `current_project_uuid` | string (uuid) |  |
    | `last_contact_time` | string (date-time) | The most recent time the remote portal acknowledged anything about this project (confirmation, usage report, get_award response, etc.).  Used to detect connectivity issues and to trigger a transition to the STALE state. |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Resend remote project request

Resend remote project request


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/openportal-remote-projects/a1b2c3d4-e5f6-7890-abcd-ef1234567890/resend-request/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openportal_remote_projects import openportal_remote_projects_resend_request # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openportal_remote_projects_resend_request.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openportal_remote_projects_resend_request`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal_remote_projects/openportal_remote_projects_resend_request.py)

=== "TypeScript"

    ```typescript
    import { openportalRemoteProjectsResendRequest } from 'waldur-js-client';
    
    try {
      const response = await openportalRemoteProjectsResendRequest({
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
    | `destination` | string | Routing path from the local portal to the remote resource, e.g. 'airr.brics.isambard-ai'.  Never changes after creation. |
    | `identifier` | string | Stable remote project identifier, e.g. 'u6ac.brics'.  Uniquely identifies the project on the remote portal and never changes.  Null while the project is pending first approval. |
    | `resource_uuid` | string (uuid) |  |
    | `resource_name` | string |  |
    | `state` | string | <br>_Enum: `pending`, `active`, `stale`, `error`, `deleted`_ |
    | `state_display` | string |  |
    | `current_allocation` | string (decimal) | Latest confirmed allocation (credits) for this project.  Updated whenever a RemoteProjectAllocationEntry is confirmed. |
    | `pending_allocation` | string (decimal) | Allocation value currently under review on the remote portal.  Null when no allocation change is pending. |
    | `allocation_string` | string |  |
    | `link_award` | any |  |
    | `link_call` | any |  |
    | `link_project` | any |  |
    | `link_renewal` | any |  |
    | `membership_control` | any | Policy controlling whether the remote portal may independently modify project membership or roles. |
    | `allowed_domains` | array of strings |  |
    | `breakdown` | object (free-form) |  |
    | `last_sent_details` | any |  |
    | `last_confirmed_details` | any |  |
    | `pending_details` | any |  |
    | `award_details` | any |  |
    | `pending_since` | string (date-time) | When the currently pending change was submitted. |
    | `notes` | array of objects |  |
    | `notes.timestamp` | string (date-time) | When the note was created (UTC) |
    | `notes.author` | string | Name of the person who created the note |
    | `notes.text` | string | Free-text content of the note |
    | `earliest_approve` | string (date-time) |  |
    | `error_message` | string | The most recent rejection or error message received from the remote portal.  Cleared when the state transitions to ACTIVE. |
    | `has_pending_change` | boolean |  |
    | `current_project_name` | string |  |
    | `current_project_uuid` | string (uuid) |  |
    | `last_contact_time` | string (date-time) | The most recent time the remote portal acknowledged anything about this project (confirmation, usage report, get_award response, etc.).  Used to detect connectivity issues and to trigger a transition to the STALE state. |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Reset remote project to pending

Reset remote project to pending


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/openportal-remote-projects/a1b2c3d4-e5f6-7890-abcd-ef1234567890/reset-to-pending/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openportal_remote_projects import openportal_remote_projects_reset_to_pending # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openportal_remote_projects_reset_to_pending.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openportal_remote_projects_reset_to_pending`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal_remote_projects/openportal_remote_projects_reset_to_pending.py)

=== "TypeScript"

    ```typescript
    import { openportalRemoteProjectsResetToPending } from 'waldur-js-client';
    
    try {
      const response = await openportalRemoteProjectsResetToPending({
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
    | `destination` | string | Routing path from the local portal to the remote resource, e.g. 'airr.brics.isambard-ai'.  Never changes after creation. |
    | `identifier` | string | Stable remote project identifier, e.g. 'u6ac.brics'.  Uniquely identifies the project on the remote portal and never changes.  Null while the project is pending first approval. |
    | `resource_uuid` | string (uuid) |  |
    | `resource_name` | string |  |
    | `state` | string | <br>_Enum: `pending`, `active`, `stale`, `error`, `deleted`_ |
    | `state_display` | string |  |
    | `current_allocation` | string (decimal) | Latest confirmed allocation (credits) for this project.  Updated whenever a RemoteProjectAllocationEntry is confirmed. |
    | `pending_allocation` | string (decimal) | Allocation value currently under review on the remote portal.  Null when no allocation change is pending. |
    | `allocation_string` | string |  |
    | `link_award` | any |  |
    | `link_call` | any |  |
    | `link_project` | any |  |
    | `link_renewal` | any |  |
    | `membership_control` | any | Policy controlling whether the remote portal may independently modify project membership or roles. |
    | `allowed_domains` | array of strings |  |
    | `breakdown` | object (free-form) |  |
    | `last_sent_details` | any |  |
    | `last_confirmed_details` | any |  |
    | `pending_details` | any |  |
    | `award_details` | any |  |
    | `pending_since` | string (date-time) | When the currently pending change was submitted. |
    | `notes` | array of objects |  |
    | `notes.timestamp` | string (date-time) | When the note was created (UTC) |
    | `notes.author` | string | Name of the person who created the note |
    | `notes.text` | string | Free-text content of the note |
    | `earliest_approve` | string (date-time) |  |
    | `error_message` | string | The most recent rejection or error message received from the remote portal.  Cleared when the state transitions to ACTIVE. |
    | `has_pending_change` | boolean |  |
    | `current_project_name` | string |  |
    | `current_project_uuid` | string (uuid) |  |
    | `last_contact_time` | string (date-time) | The most recent time the remote portal acknowledged anything about this project (confirmation, usage report, get_award response, etc.).  Used to detect connectivity issues and to trigger a transition to the STALE state. |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Set allowed domains for remote project

Set allowed domains for remote project


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/openportal-remote-projects/a1b2c3d4-e5f6-7890-abcd-ef1234567890/set-allowed-domains/ \
      Authorization:"Token YOUR_API_TOKEN" \
      allowed_domains:='[]'
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.set_allowed_domains_request import SetAllowedDomainsRequest # (1)
    from waldur_api_client.api.openportal_remote_projects import openportal_remote_projects_set_allowed_domains # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = SetAllowedDomainsRequest(
        allowed_domains=[]
    )
    response = openportal_remote_projects_set_allowed_domains.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`SetAllowedDomainsRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/set_allowed_domains_request.py)
    2.  **API Source:** [`openportal_remote_projects_set_allowed_domains`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal_remote_projects/openportal_remote_projects_set_allowed_domains.py)

=== "TypeScript"

    ```typescript
    import { openportalRemoteProjectsSetAllowedDomains } from 'waldur-js-client';
    
    try {
      const response = await openportalRemoteProjectsSetAllowedDomains({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "allowed_domains": []
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

    | Field | Type | Required |
    |---|---|---|
    | `allowed_domains` | array of strings | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `destination` | string | Routing path from the local portal to the remote resource, e.g. 'airr.brics.isambard-ai'.  Never changes after creation. |
    | `identifier` | string | Stable remote project identifier, e.g. 'u6ac.brics'.  Uniquely identifies the project on the remote portal and never changes.  Null while the project is pending first approval. |
    | `resource_uuid` | string (uuid) |  |
    | `resource_name` | string |  |
    | `state` | string | <br>_Enum: `pending`, `active`, `stale`, `error`, `deleted`_ |
    | `state_display` | string |  |
    | `current_allocation` | string (decimal) | Latest confirmed allocation (credits) for this project.  Updated whenever a RemoteProjectAllocationEntry is confirmed. |
    | `pending_allocation` | string (decimal) | Allocation value currently under review on the remote portal.  Null when no allocation change is pending. |
    | `allocation_string` | string |  |
    | `link_award` | any |  |
    | `link_call` | any |  |
    | `link_project` | any |  |
    | `link_renewal` | any |  |
    | `membership_control` | any | Policy controlling whether the remote portal may independently modify project membership or roles. |
    | `allowed_domains` | array of strings |  |
    | `breakdown` | object (free-form) |  |
    | `last_sent_details` | any |  |
    | `last_confirmed_details` | any |  |
    | `pending_details` | any |  |
    | `award_details` | any |  |
    | `pending_since` | string (date-time) | When the currently pending change was submitted. |
    | `notes` | array of objects |  |
    | `notes.timestamp` | string (date-time) | When the note was created (UTC) |
    | `notes.author` | string | Name of the person who created the note |
    | `notes.text` | string | Free-text content of the note |
    | `earliest_approve` | string (date-time) |  |
    | `error_message` | string | The most recent rejection or error message received from the remote portal.  Cleared when the state transitions to ACTIVE. |
    | `has_pending_change` | boolean |  |
    | `current_project_name` | string |  |
    | `current_project_uuid` | string (uuid) |  |
    | `last_contact_time` | string (date-time) | The most recent time the remote portal acknowledged anything about this project (confirmation, usage report, get_award response, etc.).  Used to detect connectivity issues and to trigger a transition to the STALE state. |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Set earliest approve date for remote project

Set earliest approve date for remote project


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/openportal-remote-projects/a1b2c3d4-e5f6-7890-abcd-ef1234567890/set-earliest-approve/ \
      Authorization:"Token YOUR_API_TOKEN" \
      earliest_approve="2023-10-01T12:00:00Z"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.set_earliest_approve_request import SetEarliestApproveRequest # (1)
    from waldur_api_client.api.openportal_remote_projects import openportal_remote_projects_set_earliest_approve # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = SetEarliestApproveRequest(
        earliest_approve="2023-10-01T12:00:00Z"
    )
    response = openportal_remote_projects_set_earliest_approve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`SetEarliestApproveRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/set_earliest_approve_request.py)
    2.  **API Source:** [`openportal_remote_projects_set_earliest_approve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal_remote_projects/openportal_remote_projects_set_earliest_approve.py)

=== "TypeScript"

    ```typescript
    import { openportalRemoteProjectsSetEarliestApprove } from 'waldur-js-client';
    
    try {
      const response = await openportalRemoteProjectsSetEarliestApprove({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "earliest_approve": "2023-10-01T12:00:00Z"
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

    | Field | Type | Required |
    |---|---|---|
    | `earliest_approve` | string (date-time) | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `destination` | string | Routing path from the local portal to the remote resource, e.g. 'airr.brics.isambard-ai'.  Never changes after creation. |
    | `identifier` | string | Stable remote project identifier, e.g. 'u6ac.brics'.  Uniquely identifies the project on the remote portal and never changes.  Null while the project is pending first approval. |
    | `resource_uuid` | string (uuid) |  |
    | `resource_name` | string |  |
    | `state` | string | <br>_Enum: `pending`, `active`, `stale`, `error`, `deleted`_ |
    | `state_display` | string |  |
    | `current_allocation` | string (decimal) | Latest confirmed allocation (credits) for this project.  Updated whenever a RemoteProjectAllocationEntry is confirmed. |
    | `pending_allocation` | string (decimal) | Allocation value currently under review on the remote portal.  Null when no allocation change is pending. |
    | `allocation_string` | string |  |
    | `link_award` | any |  |
    | `link_call` | any |  |
    | `link_project` | any |  |
    | `link_renewal` | any |  |
    | `membership_control` | any | Policy controlling whether the remote portal may independently modify project membership or roles. |
    | `allowed_domains` | array of strings |  |
    | `breakdown` | object (free-form) |  |
    | `last_sent_details` | any |  |
    | `last_confirmed_details` | any |  |
    | `pending_details` | any |  |
    | `award_details` | any |  |
    | `pending_since` | string (date-time) | When the currently pending change was submitted. |
    | `notes` | array of objects |  |
    | `notes.timestamp` | string (date-time) | When the note was created (UTC) |
    | `notes.author` | string | Name of the person who created the note |
    | `notes.text` | string | Free-text content of the note |
    | `earliest_approve` | string (date-time) |  |
    | `error_message` | string | The most recent rejection or error message received from the remote portal.  Cleared when the state transitions to ACTIVE. |
    | `has_pending_change` | boolean |  |
    | `current_project_name` | string |  |
    | `current_project_uuid` | string (uuid) |  |
    | `last_contact_time` | string (date-time) | The most recent time the remote portal acknowledged anything about this project (confirmation, usage report, get_award response, etc.).  Used to detect connectivity issues and to trigger a transition to the STALE state. |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Set links for remote project

Set links for remote project


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/openportal-remote-projects/a1b2c3d4-e5f6-7890-abcd-ef1234567890/set-links/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.set_links_request import SetLinksRequest # (1)
    from waldur_api_client.api.openportal_remote_projects import openportal_remote_projects_set_links # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = SetLinksRequest()
    response = openportal_remote_projects_set_links.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`SetLinksRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/set_links_request.py)
    2.  **API Source:** [`openportal_remote_projects_set_links`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal_remote_projects/openportal_remote_projects_set_links.py)

=== "TypeScript"

    ```typescript
    import { openportalRemoteProjectsSetLinks } from 'waldur-js-client';
    
    try {
      const response = await openportalRemoteProjectsSetLinks({
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

    | Field | Type | Required |
    |---|---|---|
    | `award` | any |  |
    | `call` | any |  |
    | `project_link` | any |  |
    | `renewal` | any |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `destination` | string | Routing path from the local portal to the remote resource, e.g. 'airr.brics.isambard-ai'.  Never changes after creation. |
    | `identifier` | string | Stable remote project identifier, e.g. 'u6ac.brics'.  Uniquely identifies the project on the remote portal and never changes.  Null while the project is pending first approval. |
    | `resource_uuid` | string (uuid) |  |
    | `resource_name` | string |  |
    | `state` | string | <br>_Enum: `pending`, `active`, `stale`, `error`, `deleted`_ |
    | `state_display` | string |  |
    | `current_allocation` | string (decimal) | Latest confirmed allocation (credits) for this project.  Updated whenever a RemoteProjectAllocationEntry is confirmed. |
    | `pending_allocation` | string (decimal) | Allocation value currently under review on the remote portal.  Null when no allocation change is pending. |
    | `allocation_string` | string |  |
    | `link_award` | any |  |
    | `link_call` | any |  |
    | `link_project` | any |  |
    | `link_renewal` | any |  |
    | `membership_control` | any | Policy controlling whether the remote portal may independently modify project membership or roles. |
    | `allowed_domains` | array of strings |  |
    | `breakdown` | object (free-form) |  |
    | `last_sent_details` | any |  |
    | `last_confirmed_details` | any |  |
    | `pending_details` | any |  |
    | `award_details` | any |  |
    | `pending_since` | string (date-time) | When the currently pending change was submitted. |
    | `notes` | array of objects |  |
    | `notes.timestamp` | string (date-time) | When the note was created (UTC) |
    | `notes.author` | string | Name of the person who created the note |
    | `notes.text` | string | Free-text content of the note |
    | `earliest_approve` | string (date-time) |  |
    | `error_message` | string | The most recent rejection or error message received from the remote portal.  Cleared when the state transitions to ACTIVE. |
    | `has_pending_change` | boolean |  |
    | `current_project_name` | string |  |
    | `current_project_uuid` | string (uuid) |  |
    | `last_contact_time` | string (date-time) | The most recent time the remote portal acknowledged anything about this project (confirmation, usage report, get_award response, etc.).  Used to detect connectivity issues and to trigger a transition to the STALE state. |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Set membership control for remote project

Set membership control for remote project


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/openportal-remote-projects/a1b2c3d4-e5f6-7890-abcd-ef1234567890/set-membership-control/ \
      Authorization:"Token YOUR_API_TOKEN" \
      membership_control=null
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.set_membership_control_request import SetMembershipControlRequest # (1)
    from waldur_api_client.api.openportal_remote_projects import openportal_remote_projects_set_membership_control # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = SetMembershipControlRequest(
        membership_control=null
    )
    response = openportal_remote_projects_set_membership_control.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`SetMembershipControlRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/set_membership_control_request.py)
    2.  **API Source:** [`openportal_remote_projects_set_membership_control`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal_remote_projects/openportal_remote_projects_set_membership_control.py)

=== "TypeScript"

    ```typescript
    import { openportalRemoteProjectsSetMembershipControl } from 'waldur-js-client';
    
    try {
      const response = await openportalRemoteProjectsSetMembershipControl({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "membership_control": null
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

    | Field | Type | Required |
    |---|---|---|
    | `membership_control` | any | ✓ |


=== "Responses"

    **`202`** - No response body
    

---
