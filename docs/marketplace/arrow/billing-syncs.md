# Admin Arrow Billing Syncs

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/billing-syncs/` | [Billing syncs](#billing-syncs) |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/billing-syncs/{uuid}/` | [Retrieve](#retrieve) |
| **Sync Control** | | |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/billing-syncs/pause_sync/` | [Pause consumption sync operations](#pause-consumption-sync-operations) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/billing-syncs/reconcile/` | [Trigger reconciliation for a specific period](#trigger-reconciliation-for-a-specific-period) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/billing-syncs/resume_sync/` | [Resume consumption sync operations](#resume-consumption-sync-operations) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/billing-syncs/trigger_consumption_sync/` | [Trigger consumption sync for a specific period](#trigger-consumption-sync-for-a-specific-period) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/billing-syncs/trigger_reconciliation/` | [Trigger reconciliation (check billing export and apply adjustments)](#trigger-reconciliation-check-billing-export-and-apply-adjustments) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/billing-syncs/trigger_sync/` | [Trigger billing sync for a specific period](#trigger-billing-sync-for-a-specific-period) |
| **Data Retrieval** | | |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/billing-syncs/consumption_statistics/` | [Get consumption statistics](#get-consumption-statistics) |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/billing-syncs/consumption_status/` | [Get current consumption sync status](#get-current-consumption-sync-status) |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/billing-syncs/pending_records/` | [List pending consumption records (not yet finalized)](#list-pending-consumption-records-not-yet-finalized) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/billing-syncs/fetch_billing_export/` | [Fetch raw billing export from Arrow API](#fetch-raw-billing-export-from-arrow-api) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/billing-syncs/fetch_consumption/` | [Fetch raw consumption data from Arrow API](#fetch-raw-consumption-data-from-arrow-api) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/billing-syncs/fetch_license_info/` | [Fetch license details from Arrow API](#fetch-license-details-from-arrow-api) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/billing-syncs/sync_resource_historical_consumption/` | [Sync historical consumption for a specific resource from Arrow](#sync-historical-consumption-for-a-specific-resource-from-arrow) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/billing-syncs/sync_resources/` | [Sync resources](#sync-resources) |
| **Cleanup** | | |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/billing-syncs/cleanup_consumption/` | [Delete consumption records with optional dry-run preview](#delete-consumption-records-with-optional-dry-run-preview) |

---
## Core CRUD


### Billing syncs


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/admin/arrow/billing-syncs/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.admin import admin_arrow_billing_syncs_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = admin_arrow_billing_syncs_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`admin_arrow_billing_syncs_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_billing_syncs_list.py)

=== "TypeScript"

    ```typescript
    import { adminArrowBillingSyncsList } from 'waldur-js-client';
    
    try {
      const response = await adminArrowBillingSyncsList({
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
    | `arrow_state` | string |  |
    | `customer_mapping` | string |  |
    | `customer_mapping_uuid` | string (uuid) |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `report_period` | string |  |
    | `report_period_from` | string |  |
    | `report_period_to` | string |  |
    | `settings_uuid` | string (uuid) |  |
    | `state` | integer |  |
    | `statement_reference` | string |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `customer_mapping` | string (uri) |  |
    | `customer_mapping_uuid` | string (uuid) |  |
    | `arrow_reference` | string | Arrow customer ID (e.g., 'XSP661245') |
    | `waldur_customer_name` | string |  |
    | `statement_reference` | string | Arrow statement ID |
    | `report_period` | string | Report period in YYYY-MM format |
    | `arrow_state` | string | Arrow billing state (pending/validated) |
    | `state` | any | Waldur sync state |
    | `state_display` | string |  |
    | `buy_total` | string (decimal) | Total buy amount |
    | `sell_total` | string (decimal) | Total sell amount |
    | `currency` | string | Currency code |
    | `invoice_uuid` | string (uuid) |  |
    | `error_message` | string | Error message if sync failed |
    | `synced_at` | string (date-time) | When billing was last synced |
    | `validated_at` | string (date-time) | When Arrow validated the billing |
    | `reconciled_at` | string (date-time) | When reconciliation was applied |
    | `items` | array of objects |  |
    | `items.uuid` | string (uuid) |  |
    | `items.arrow_line_reference` | string | Arrow line ID |
    | `items.invoice_item_uuid` | string (uuid) |  |
    | `items.original_price` | string (decimal) | Original price for reconciliation tracking |
    | `items.compensation_item_uuid` | string (uuid) |  |
    | `items.vendor_name` | string | Vendor name (e.g., Microsoft) |
    | `items.subscription_reference` | string | Arrow subscription reference |
    | `items.classification` | string | Classification (IAAS/SAAS) |
    | `items.description` | string | Line item description |
    | `items.quantity` | string (decimal) | Quantity |
    | `items.created` | string (date-time) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/admin/arrow/billing-syncs/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.admin import admin_arrow_billing_syncs_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = admin_arrow_billing_syncs_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`admin_arrow_billing_syncs_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_billing_syncs_retrieve.py)

=== "TypeScript"

    ```typescript
    import { adminArrowBillingSyncsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await adminArrowBillingSyncsRetrieve({
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
    | `url` | string (uri) |  |
    | `customer_mapping` | string (uri) |  |
    | `customer_mapping_uuid` | string (uuid) |  |
    | `arrow_reference` | string | Arrow customer ID (e.g., 'XSP661245') |
    | `waldur_customer_name` | string |  |
    | `statement_reference` | string | Arrow statement ID |
    | `report_period` | string | Report period in YYYY-MM format |
    | `arrow_state` | string | Arrow billing state (pending/validated) |
    | `state` | any | Waldur sync state |
    | `state_display` | string |  |
    | `buy_total` | string (decimal) | Total buy amount |
    | `sell_total` | string (decimal) | Total sell amount |
    | `currency` | string | Currency code |
    | `invoice_uuid` | string (uuid) |  |
    | `error_message` | string | Error message if sync failed |
    | `synced_at` | string (date-time) | When billing was last synced |
    | `validated_at` | string (date-time) | When Arrow validated the billing |
    | `reconciled_at` | string (date-time) | When reconciliation was applied |
    | `items` | array of objects |  |
    | `items.uuid` | string (uuid) |  |
    | `items.arrow_line_reference` | string | Arrow line ID |
    | `items.invoice_item_uuid` | string (uuid) |  |
    | `items.original_price` | string (decimal) | Original price for reconciliation tracking |
    | `items.compensation_item_uuid` | string (uuid) |  |
    | `items.vendor_name` | string | Vendor name (e.g., Microsoft) |
    | `items.subscription_reference` | string | Arrow subscription reference |
    | `items.classification` | string | Classification (IAAS/SAAS) |
    | `items.description` | string | Line item description |
    | `items.quantity` | string (decimal) | Quantity |
    | `items.created` | string (date-time) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

## Sync Control


### Pause consumption sync operations

Pause consumption sync operations.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/admin/arrow/billing-syncs/pause_sync/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.sync_pause_request_request import SyncPauseRequestRequest # (1)
    from waldur_api_client.api.admin import admin_arrow_billing_syncs_pause_sync # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = SyncPauseRequestRequest()
    response = admin_arrow_billing_syncs_pause_sync.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`SyncPauseRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/sync_pause_request_request.py)
    2.  **API Source:** [`admin_arrow_billing_syncs_pause_sync`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_billing_syncs_pause_sync.py)

=== "TypeScript"

    ```typescript
    import { adminArrowBillingSyncsPauseSync } from 'waldur-js-client';
    
    try {
      const response = await adminArrowBillingSyncsPauseSync({
      auth: "Token YOUR_API_TOKEN"
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Request Body"

    | Field | Type | Required |
    |---|---|---|
    | `settings_uuid` | string (uuid) |  |
    | `pause_global` | boolean |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `paused` | array of strings | List of paused items |
    | `resumed` | array of strings | List of resumed items |

---

### Trigger reconciliation for a specific period

Trigger reconciliation for a specific period.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/admin/arrow/billing-syncs/reconcile/ \
      Authorization:"Token YOUR_API_TOKEN" \
      year=123 \
      month=123
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.reconcile_request_request import ReconcileRequestRequest # (1)
    from waldur_api_client.api.admin import admin_arrow_billing_syncs_reconcile # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ReconcileRequestRequest(
        year=123,
        month=123
    )
    response = admin_arrow_billing_syncs_reconcile.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ReconcileRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/reconcile_request_request.py)
    2.  **API Source:** [`admin_arrow_billing_syncs_reconcile`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_billing_syncs_reconcile.py)

=== "TypeScript"

    ```typescript
    import { adminArrowBillingSyncsReconcile } from 'waldur-js-client';
    
    try {
      const response = await adminArrowBillingSyncsReconcile({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "year": 123,
        "month": 123
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
    | `year` | integer | ✓ |  |
    | `month` | integer | ✓ |  |
    | `settings_uuid` | string (uuid) |  |  |
    | `force` | boolean |  | Force reconciliation even if not validated<br>_Constraints: default: `False`_ |


=== "Responses"

    **`202`** - No response body
    

---

### Resume consumption sync operations

Resume consumption sync operations.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/admin/arrow/billing-syncs/resume_sync/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.sync_pause_request_request import SyncPauseRequestRequest # (1)
    from waldur_api_client.api.admin import admin_arrow_billing_syncs_resume_sync # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = SyncPauseRequestRequest()
    response = admin_arrow_billing_syncs_resume_sync.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`SyncPauseRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/sync_pause_request_request.py)
    2.  **API Source:** [`admin_arrow_billing_syncs_resume_sync`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_billing_syncs_resume_sync.py)

=== "TypeScript"

    ```typescript
    import { adminArrowBillingSyncsResumeSync } from 'waldur-js-client';
    
    try {
      const response = await adminArrowBillingSyncsResumeSync({
      auth: "Token YOUR_API_TOKEN"
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Request Body"

    | Field | Type | Required |
    |---|---|---|
    | `settings_uuid` | string (uuid) |  |
    | `pause_global` | boolean |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `paused` | array of strings | List of paused items |
    | `resumed` | array of strings | List of resumed items |

---

### Trigger consumption sync for a specific period

Trigger consumption sync for a specific period.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/admin/arrow/billing-syncs/trigger_consumption_sync/ \
      Authorization:"Token YOUR_API_TOKEN" \
      year=123 \
      month=123
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.trigger_consumption_sync_request_request import TriggerConsumptionSyncRequestRequest # (1)
    from waldur_api_client.api.admin import admin_arrow_billing_syncs_trigger_consumption_sync # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = TriggerConsumptionSyncRequestRequest(
        year=123,
        month=123
    )
    response = admin_arrow_billing_syncs_trigger_consumption_sync.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`TriggerConsumptionSyncRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/trigger_consumption_sync_request_request.py)
    2.  **API Source:** [`admin_arrow_billing_syncs_trigger_consumption_sync`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_billing_syncs_trigger_consumption_sync.py)

=== "TypeScript"

    ```typescript
    import { adminArrowBillingSyncsTriggerConsumptionSync } from 'waldur-js-client';
    
    try {
      const response = await adminArrowBillingSyncsTriggerConsumptionSync({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "year": 123,
        "month": 123
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
    | `year` | integer | ✓ |  |
    | `month` | integer | ✓ |  |
    | `settings_uuid` | string (uuid) |  |  |
    | `resource_uuid` | string (uuid) |  | Sync specific resource only |


=== "Responses"

    **`202`** - No response body
    

---

### Trigger reconciliation (check billing export and apply adjustments)

Trigger reconciliation (check billing export and apply adjustments).


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/admin/arrow/billing-syncs/trigger_reconciliation/ \
      Authorization:"Token YOUR_API_TOKEN" \
      year=123 \
      month=123
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.reconcile_request_request import ReconcileRequestRequest # (1)
    from waldur_api_client.api.admin import admin_arrow_billing_syncs_trigger_reconciliation # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ReconcileRequestRequest(
        year=123,
        month=123
    )
    response = admin_arrow_billing_syncs_trigger_reconciliation.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ReconcileRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/reconcile_request_request.py)
    2.  **API Source:** [`admin_arrow_billing_syncs_trigger_reconciliation`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_billing_syncs_trigger_reconciliation.py)

=== "TypeScript"

    ```typescript
    import { adminArrowBillingSyncsTriggerReconciliation } from 'waldur-js-client';
    
    try {
      const response = await adminArrowBillingSyncsTriggerReconciliation({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "year": 123,
        "month": 123
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
    | `year` | integer | ✓ |  |
    | `month` | integer | ✓ |  |
    | `settings_uuid` | string (uuid) |  |  |
    | `force` | boolean |  | Force reconciliation even if not validated<br>_Constraints: default: `False`_ |


=== "Responses"

    **`202`** - No response body
    

---

### Trigger billing sync for a specific period

Trigger billing sync for a specific period.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/admin/arrow/billing-syncs/trigger_sync/ \
      Authorization:"Token YOUR_API_TOKEN" \
      year=123 \
      month=123
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.trigger_sync_request_request import TriggerSyncRequestRequest # (1)
    from waldur_api_client.api.admin import admin_arrow_billing_syncs_trigger_sync # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = TriggerSyncRequestRequest(
        year=123,
        month=123
    )
    response = admin_arrow_billing_syncs_trigger_sync.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`TriggerSyncRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/trigger_sync_request_request.py)
    2.  **API Source:** [`admin_arrow_billing_syncs_trigger_sync`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_billing_syncs_trigger_sync.py)

=== "TypeScript"

    ```typescript
    import { adminArrowBillingSyncsTriggerSync } from 'waldur-js-client';
    
    try {
      const response = await adminArrowBillingSyncsTriggerSync({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "year": 123,
        "month": 123
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Request Body (required)"

    | Field | Type | Required |
    |---|---|---|
    | `year` | integer | ✓ |
    | `month` | integer | ✓ |
    | `settings_uuid` | string (uuid) |  |


=== "Responses"

    **`202`** - No response body
    

---

## Data Retrieval


### Get consumption statistics

Get consumption statistics.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/admin/arrow/billing-syncs/consumption_statistics/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.admin import admin_arrow_billing_syncs_consumption_statistics_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = admin_arrow_billing_syncs_consumption_statistics_retrieve.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`admin_arrow_billing_syncs_consumption_statistics_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_billing_syncs_consumption_statistics_retrieve.py)

=== "TypeScript"

    ```typescript
    import { adminArrowBillingSyncsConsumptionStatisticsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await adminArrowBillingSyncsConsumptionStatisticsRetrieve({
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
    | `total_records` | integer |
    | `pending_records` | integer |
    | `finalized_records` | integer |
    | `reconciled_records` | integer |
    | `total_consumed_sell` | string (decimal) |
    | `total_adjustments` | string (decimal) |
    | `period_breakdown` | array of objects |
    | `period_breakdown.period` | string |
    | `period_breakdown.count` | integer |
    | `period_breakdown.consumed_sell` | string (decimal) |
    | `period_breakdown.finalized_count` | integer |
    | `period_breakdown.reconciled_count` | integer |

---

### Get current consumption sync status

Get current consumption sync status.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/admin/arrow/billing-syncs/consumption_status/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.admin import admin_arrow_billing_syncs_consumption_status_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = admin_arrow_billing_syncs_consumption_status_retrieve.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`admin_arrow_billing_syncs_consumption_status_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_billing_syncs_consumption_status_retrieve.py)

=== "TypeScript"

    ```typescript
    import { adminArrowBillingSyncsConsumptionStatusRetrieve } from 'waldur-js-client';
    
    try {
      const response = await adminArrowBillingSyncsConsumptionStatusRetrieve({
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
    | `global_sync_enabled` | boolean |
    | `settings_sync_enabled` | boolean |
    | `settings_uuid` | string (uuid) |
    | `last_sync_run` | string (date-time) |

---

### List pending consumption records (not yet finalized)

List pending consumption records (not yet finalized).


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/admin/arrow/billing-syncs/pending_records/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.admin import admin_arrow_billing_syncs_pending_records_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = admin_arrow_billing_syncs_pending_records_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`admin_arrow_billing_syncs_pending_records_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_billing_syncs_pending_records_list.py)

=== "TypeScript"

    ```typescript
    import { adminArrowBillingSyncsPendingRecordsList } from 'waldur-js-client';
    
    try {
      const response = await adminArrowBillingSyncsPendingRecordsList({
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
    | `arrow_state` | string |  |
    | `customer_mapping` | string |  |
    | `customer_mapping_uuid` | string (uuid) |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `report_period` | string |  |
    | `report_period_from` | string |  |
    | `report_period_to` | string |  |
    | `settings_uuid` | string (uuid) |  |
    | `state` | integer |  |
    | `statement_reference` | string |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `resource_uuid` | string (uuid) |
    | `resource_name` | string |
    | `license_reference` | string |
    | `billing_period` | string (date) |
    | `consumed_sell` | string (decimal) |
    | `last_sync_at` | string (date-time) |

---

### Fetch raw billing export from Arrow API

Fetch raw billing export from Arrow API.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/admin/arrow/billing-syncs/fetch_billing_export/ \
      Authorization:"Token YOUR_API_TOKEN" \
      period_from="string-value" \
      period_to="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.fetch_billing_export_request_request import FetchBillingExportRequestRequest # (1)
    from waldur_api_client.api.admin import admin_arrow_billing_syncs_fetch_billing_export # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = FetchBillingExportRequestRequest(
        period_from="string-value",
        period_to="string-value"
    )
    response = admin_arrow_billing_syncs_fetch_billing_export.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`FetchBillingExportRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/fetch_billing_export_request_request.py)
    2.  **API Source:** [`admin_arrow_billing_syncs_fetch_billing_export`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_billing_syncs_fetch_billing_export.py)

=== "TypeScript"

    ```typescript
    import { adminArrowBillingSyncsFetchBillingExport } from 'waldur-js-client';
    
    try {
      const response = await adminArrowBillingSyncsFetchBillingExport({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "period_from": "string-value",
        "period_to": "string-value"
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
    | `period_from` | string | ✓ | YYYY-MM format |
    | `period_to` | string | ✓ | YYYY-MM format |
    | `classification` | string |  |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `period_from` | string |
    | `period_to` | string |
    | `classification` | string |
    | `row_count` | integer |
    | `data` | array of objects |

---

### Fetch raw consumption data from Arrow API

Fetch raw consumption data from Arrow API.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/admin/arrow/billing-syncs/fetch_consumption/ \
      Authorization:"Token YOUR_API_TOKEN" \
      license_reference="string-value" \
      period="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.fetch_consumption_request_request import FetchConsumptionRequestRequest # (1)
    from waldur_api_client.api.admin import admin_arrow_billing_syncs_fetch_consumption # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = FetchConsumptionRequestRequest(
        license_reference="string-value",
        period="string-value"
    )
    response = admin_arrow_billing_syncs_fetch_consumption.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`FetchConsumptionRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/fetch_consumption_request_request.py)
    2.  **API Source:** [`admin_arrow_billing_syncs_fetch_consumption`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_billing_syncs_fetch_consumption.py)

=== "TypeScript"

    ```typescript
    import { adminArrowBillingSyncsFetchConsumption } from 'waldur-js-client';
    
    try {
      const response = await adminArrowBillingSyncsFetchConsumption({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "license_reference": "string-value",
        "period": "string-value"
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
    | `license_reference` | string | ✓ |  |
    | `period` | string | ✓ | YYYY-MM format |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `license_reference` | string |
    | `period` | string |
    | `row_count` | integer |
    | `data` | array of objects |

---

### Fetch license details from Arrow API

Fetch license details from Arrow API.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/admin/arrow/billing-syncs/fetch_license_info/ \
      Authorization:"Token YOUR_API_TOKEN" \
      license_reference="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.fetch_license_info_request_request import FetchLicenseInfoRequestRequest # (1)
    from waldur_api_client.api.admin import admin_arrow_billing_syncs_fetch_license_info # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = FetchLicenseInfoRequestRequest(
        license_reference="string-value"
    )
    response = admin_arrow_billing_syncs_fetch_license_info.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`FetchLicenseInfoRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/fetch_license_info_request_request.py)
    2.  **API Source:** [`admin_arrow_billing_syncs_fetch_license_info`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_billing_syncs_fetch_license_info.py)

=== "TypeScript"

    ```typescript
    import { adminArrowBillingSyncsFetchLicenseInfo } from 'waldur-js-client';
    
    try {
      const response = await adminArrowBillingSyncsFetchLicenseInfo({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "license_reference": "string-value"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Request Body (required)"

    | Field | Type | Required |
    |---|---|---|
    | `license_reference` | string | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `data` | object (free-form) | Raw license data from Arrow API |

---

### Sync historical consumption for a specific resource from Arrow

Sync historical consumption for a specific resource from Arrow.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/admin/arrow/billing-syncs/sync_resource_historical_consumption/ \
      Authorization:"Token YOUR_API_TOKEN" \
      resource_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.sync_resource_historical_consumption_request_request import SyncResourceHistoricalConsumptionRequestRequest # (1)
    from waldur_api_client.api.admin import admin_arrow_billing_syncs_sync_resource_historical_consumption # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = SyncResourceHistoricalConsumptionRequestRequest(
        resource_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = admin_arrow_billing_syncs_sync_resource_historical_consumption.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`SyncResourceHistoricalConsumptionRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/sync_resource_historical_consumption_request_request.py)
    2.  **API Source:** [`admin_arrow_billing_syncs_sync_resource_historical_consumption`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_billing_syncs_sync_resource_historical_consumption.py)

=== "TypeScript"

    ```typescript
    import { adminArrowBillingSyncsSyncResourceHistoricalConsumption } from 'waldur-js-client';
    
    try {
      const response = await adminArrowBillingSyncsSyncResourceHistoricalConsumption({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "resource_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `resource_uuid` | string (uuid) | ✓ | UUID of the resource to sync |
    | `period_from` | string |  | Start period in YYYY-MM format. Defaults to 12 months ago. |
    | `period_to` | string |  | End period in YYYY-MM format. Defaults to current month. |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `resource_uuid` | string (uuid) |
    | `resource_name` | string |
    | `periods_synced` | integer |
    | `periods_skipped` | integer |
    | `errors` | array of objects |

---

### Sync resources

Sync Arrow IAAS subscriptions to Waldur Resources. Matches subscriptions by Vendor Subscription ID to resource backend_id. Updates resource report and current_usages fields. With force_import=True, auto-creates Customers and Projects from Arrow data.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/admin/arrow/billing-syncs/sync_resources/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.sync_resources_request_request import SyncResourcesRequestRequest # (1)
    from waldur_api_client.api.admin import admin_arrow_billing_syncs_sync_resources # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = SyncResourcesRequestRequest()
    response = admin_arrow_billing_syncs_sync_resources.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`SyncResourcesRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/sync_resources_request_request.py)
    2.  **API Source:** [`admin_arrow_billing_syncs_sync_resources`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_billing_syncs_sync_resources.py)

=== "TypeScript"

    ```typescript
    import { adminArrowBillingSyncsSyncResources } from 'waldur-js-client';
    
    try {
      const response = await adminArrowBillingSyncsSyncResources({
      auth: "Token YOUR_API_TOKEN"
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Request Body"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `period_from` | string |  | Start period in YYYY-MM format (default: 6 months ago, Arrow max) |
    | `period_to` | string |  | End period in YYYY-MM format (default: current month) |
    | `settings_uuid` | string (uuid) |  |  |
    | `offering_uuid` | string (uuid) |  | Offering UUID for creating new resources |
    | `project_uuid` | string (uuid) |  | Project UUID for creating new resources (ignored if force_import=True) |
    | `force_import` | boolean |  | If True, auto-create Waldur Customers and Projects from Arrow data. Each Arrow customer gets a Waldur Customer with an 'Arrow Azure Subscriptions' project.<br>_Constraints: default: `False`_ |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `synced` | integer |
    | `created` | integer |
    | `updated` | integer |
    | `orders_created` | integer |
    | `customers_created` | integer |
    | `projects_created` | integer |
    | `mappings_created` | integer |
    | `invoices_created` | integer |
    | `invoice_items_created` | integer |
    | `errors` | array of objects |

---

## Cleanup


### Delete consumption records with optional dry-run preview

Delete consumption records with optional dry-run preview.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/admin/arrow/billing-syncs/cleanup_consumption/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.cleanup_consumption_request_request import CleanupConsumptionRequestRequest # (1)
    from waldur_api_client.api.admin import admin_arrow_billing_syncs_cleanup_consumption # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = CleanupConsumptionRequestRequest()
    response = admin_arrow_billing_syncs_cleanup_consumption.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`CleanupConsumptionRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/cleanup_consumption_request_request.py)
    2.  **API Source:** [`admin_arrow_billing_syncs_cleanup_consumption`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_billing_syncs_cleanup_consumption.py)

=== "TypeScript"

    ```typescript
    import { adminArrowBillingSyncsCleanupConsumption } from 'waldur-js-client';
    
    try {
      const response = await adminArrowBillingSyncsCleanupConsumption({
      auth: "Token YOUR_API_TOKEN"
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Request Body"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `period_from` | string |  | YYYY-MM format |
    | `period_to` | string |  | YYYY-MM format |
    | `resource_uuid` | string (uuid) |  |  |
    | `only_finalized` | boolean |  | <br>_Constraints: default: `False`_ |
    | `only_unfinalized` | boolean |  | <br>_Constraints: default: `False`_ |
    | `dry_run` | boolean |  | <br>_Constraints: default: `True`_ |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `dry_run` | boolean |
    | `records_to_delete` | integer |
    | `records_deleted` | integer |
    | `compensation_items_affected` | integer |
    | `invoice_items_affected` | integer |

---
