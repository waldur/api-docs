# Admin

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/billing-sync-items/` | [Billing sync items](#billing-sync-items) |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/billing-sync-items/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/billing-syncs/consumption_statistics/` | [Get consumption statistics](#get-consumption-statistics) |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/billing-syncs/consumption_status/` | [Get current consumption sync status](#get-current-consumption-sync-status) |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/billing-syncs/` | [Billing syncs](#billing-syncs) |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/billing-syncs/pending_records/` | [List pending consumption records (not yet finalized)](#list-pending-consumption-records-not-yet-finalized) |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/billing-syncs/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/consumption-records/` | [Consumption records](#consumption-records) |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/consumption-records/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/customer-mappings/available_customers/` | [Available customers](#available-customers) |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/customer-mappings/{uuid}/billing_summary/` | [Get billing and consumption summary for this customer mapping](#get-billing-and-consumption-summary-for-this-customer-mapping) |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/customer-mappings/{uuid}/discover_licenses/` | [Discover Arrow licenses for this customer and show linkable Waldur resources](#discover-arrow-licenses-for-this-customer-and-show-linkable-waldur-resources) |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/customer-mappings/{uuid}/fetch_arrow_data/` | [Fetch fresh consumption and billing data from Arrow API for this customer](#fetch-fresh-consumption-and-billing-data-from-arrow-api-for-this-customer) |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/customer-mappings/` | [Customer mappings](#customer-mappings) |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/customer-mappings/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/settings/` | [Settings](#settings) |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/settings/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/vendor-offering-mappings/` | [Vendor offering mappings](#vendor-offering-mappings) |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/vendor-offering-mappings/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/vendor-offering-mappings/vendor_choices/` | [Get vendor names from Arrow catalog API (IAAS category)](#get-vendor-names-from-arrow-catalog-api-iaas-category) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/billing-syncs/cleanup_consumption/` | [Delete consumption records with optional dry-run preview](#delete-consumption-records-with-optional-dry-run-preview) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/billing-syncs/fetch_billing_export/` | [Fetch raw billing export from Arrow API](#fetch-raw-billing-export-from-arrow-api) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/billing-syncs/fetch_consumption/` | [Fetch raw consumption data from Arrow API](#fetch-raw-consumption-data-from-arrow-api) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/billing-syncs/fetch_license_info/` | [Fetch license details from Arrow API](#fetch-license-details-from-arrow-api) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/billing-syncs/pause_sync/` | [Pause consumption sync operations](#pause-consumption-sync-operations) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/billing-syncs/reconcile/` | [Trigger reconciliation for a specific period](#trigger-reconciliation-for-a-specific-period) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/billing-syncs/resume_sync/` | [Resume consumption sync operations](#resume-consumption-sync-operations) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/billing-syncs/sync_resource_historical_consumption/` | [Sync historical consumption for a specific resource from Arrow](#sync-historical-consumption-for-a-specific-resource-from-arrow) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/billing-syncs/sync_resources/` | [Sync resources](#sync-resources) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/billing-syncs/trigger_consumption_sync/` | [Trigger consumption sync for a specific period](#trigger-consumption-sync-for-a-specific-period) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/billing-syncs/trigger_reconciliation/` | [Trigger reconciliation (check billing export and apply adjustments)](#trigger-reconciliation-check-billing-export-and-apply-adjustments) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/billing-syncs/trigger_sync/` | [Trigger billing sync for a specific period](#trigger-billing-sync-for-a-specific-period) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/customer-mappings/` | [Customer mappings](#customer-mappings) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/customer-mappings/{uuid}/import_license/` | [Import an Arrow license as a new Waldur resource](#import-an-arrow-license-as-a-new-waldur-resource) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/customer-mappings/{uuid}/link_resource/` | [Link a Waldur resource to an Arrow license by setting its backend_id](#link-a-waldur-resource-to-an-arrow-license-by-setting-its-backend_id) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/customer-mappings/sync_from_arrow/` | [Sync customer list from Arrow and update arrow_company_name](#sync-customer-list-from-arrow-and-update-arrow_company_name) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/settings/` | [Settings](#settings) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/settings/discover_customers/` | [Discover Arrow customers and suggest mappings to Waldur customers](#discover-arrow-customers-and-suggest-mappings-to-waldur-customers) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/settings/preview_settings/` | [Preview settings configuration before saving](#preview-settings-configuration-before-saving) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/settings/save_settings/` | [Save Arrow settings and customer mappings](#save-arrow-settings-and-customer-mappings) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/settings/validate_credentials/` | [Validate Arrow API credentials without saving them](#validate-arrow-api-credentials-without-saving-them) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/vendor-offering-mappings/` | [Vendor offering mappings](#vendor-offering-mappings) |
| <span class="http-badge http-put">PUT</span> | `/api/admin/arrow/customer-mappings/{uuid}/` | [Update](#update) |
| <span class="http-badge http-put">PUT</span> | `/api/admin/arrow/settings/{uuid}/` | [Update](#update) |
| <span class="http-badge http-put">PUT</span> | `/api/admin/arrow/vendor-offering-mappings/{uuid}/` | [Update](#update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/admin/arrow/customer-mappings/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/admin/arrow/settings/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/admin/arrow/vendor-offering-mappings/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-delete">DELETE</span> | `/api/admin/arrow/customer-mappings/{uuid}/` | [Delete](#delete) |
| <span class="http-badge http-delete">DELETE</span> | `/api/admin/arrow/settings/{uuid}/` | [Delete](#delete) |
| <span class="http-badge http-delete">DELETE</span> | `/api/admin/arrow/vendor-offering-mappings/{uuid}/` | [Delete](#delete) |

---

### Billing sync items


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/admin/arrow/billing-sync-items/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.admin import admin_arrow_billing_sync_items_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = admin_arrow_billing_sync_items_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`admin_arrow_billing_sync_items_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_billing_sync_items_list.py)

=== "TypeScript"

    ```typescript
    import { adminArrowBillingSyncItemsList } from 'waldur-js-client';
    
    try {
      const response = await adminArrowBillingSyncItemsList({
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
    | `arrow_line_reference` | string |  |
    | `billing_sync` | string |  |
    | `billing_sync_uuid` | string (uuid) |  |
    | `classification` | string |  |
    | `has_compensation` | boolean |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `report_period` | string |  |
    | `subscription_reference` | string |  |
    | `vendor_name` | string |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `billing_sync` | string (uri) |  |
    | `billing_sync_uuid` | string (uuid) |  |
    | `report_period` | string | Report period in YYYY-MM format |
    | `arrow_line_reference` | string | Arrow line ID |
    | `invoice_item_uuid` | string (uuid) |  |
    | `original_price` | string (decimal) | Original price for reconciliation tracking |
    | `compensation_item_uuid` | string (uuid) |  |
    | `has_compensation` | boolean |  |
    | `vendor_name` | string | Vendor name (e.g., Microsoft) |
    | `subscription_reference` | string | Arrow subscription reference |
    | `classification` | string | Classification (IAAS/SAAS) |
    | `description` | string | Line item description |
    | `quantity` | string (decimal) | Quantity |
    | `created` | string (date-time) |  |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/admin/arrow/billing-sync-items/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.admin import admin_arrow_billing_sync_items_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = admin_arrow_billing_sync_items_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`admin_arrow_billing_sync_items_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_billing_sync_items_retrieve.py)

=== "TypeScript"

    ```typescript
    import { adminArrowBillingSyncItemsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await adminArrowBillingSyncItemsRetrieve({
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
    | `billing_sync` | string (uri) |  |
    | `billing_sync_uuid` | string (uuid) |  |
    | `report_period` | string | Report period in YYYY-MM format |
    | `arrow_line_reference` | string | Arrow line ID |
    | `invoice_item_uuid` | string (uuid) |  |
    | `original_price` | string (decimal) | Original price for reconciliation tracking |
    | `compensation_item_uuid` | string (uuid) |  |
    | `has_compensation` | boolean |  |
    | `vendor_name` | string | Vendor name (e.g., Microsoft) |
    | `subscription_reference` | string | Arrow subscription reference |
    | `classification` | string | Classification (IAAS/SAAS) |
    | `description` | string | Line item description |
    | `quantity` | string (decimal) | Quantity |
    | `created` | string (date-time) |  |

---

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

### Consumption records


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/admin/arrow/consumption-records/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.admin import admin_arrow_consumption_records_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = admin_arrow_consumption_records_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`admin_arrow_consumption_records_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_consumption_records_list.py)

=== "TypeScript"

    ```typescript
    import { adminArrowConsumptionRecordsList } from 'waldur-js-client';
    
    try {
      const response = await adminArrowConsumptionRecordsList({
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
    | `billing_period` | string (date) |  |
    | `billing_period_from` | string (date) |  |
    | `billing_period_to` | string (date) |  |
    | `customer_uuid` | string (uuid) |  |
    | `is_finalized` | boolean |  |
    | `is_reconciled` | boolean |  |
    | `license_reference` | string |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `project_uuid` | string (uuid) |  |
    | `resource` | string |  |
    | `resource_uuid` | string (uuid) |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `resource` | string (uri) |  |
    | `resource_uuid` | string (uuid) |  |
    | `resource_name` | string |  |
    | `project_uuid` | string (uuid) |  |
    | `project_name` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `license_reference` | string | Arrow license reference (e.g., 'XSP12345') |
    | `billing_period` | string (date) | First day of the billing month |
    | `consumed_sell` | string (decimal) | Consumed sell amount from Consumption API |
    | `consumed_buy` | string (decimal) | Consumed buy amount from Consumption API |
    | `final_sell` | string (decimal) | Final sell amount from billing export |
    | `final_buy` | string (decimal) | Final buy amount from billing export |
    | `invoice_item_uuid` | string (uuid) |  |
    | `compensation_item_uuid` | string (uuid) |  |
    | `last_sync_at` | string (date-time) | When consumption was last synced from API |
    | `finalized_at` | string (date-time) | When billing export data arrived |
    | `reconciled_at` | string (date-time) | When reconciliation was applied |
    | `is_finalized` | boolean |  |
    | `is_reconciled` | boolean |  |
    | `adjustment_amount` | string (decimal) |  |
    | `raw_data` | any | Raw consumption data for debugging |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/admin/arrow/consumption-records/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.admin import admin_arrow_consumption_records_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = admin_arrow_consumption_records_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`admin_arrow_consumption_records_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_consumption_records_retrieve.py)

=== "TypeScript"

    ```typescript
    import { adminArrowConsumptionRecordsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await adminArrowConsumptionRecordsRetrieve({
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
    | `resource` | string (uri) |  |
    | `resource_uuid` | string (uuid) |  |
    | `resource_name` | string |  |
    | `project_uuid` | string (uuid) |  |
    | `project_name` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `license_reference` | string | Arrow license reference (e.g., 'XSP12345') |
    | `billing_period` | string (date) | First day of the billing month |
    | `consumed_sell` | string (decimal) | Consumed sell amount from Consumption API |
    | `consumed_buy` | string (decimal) | Consumed buy amount from Consumption API |
    | `final_sell` | string (decimal) | Final sell amount from billing export |
    | `final_buy` | string (decimal) | Final buy amount from billing export |
    | `invoice_item_uuid` | string (uuid) |  |
    | `compensation_item_uuid` | string (uuid) |  |
    | `last_sync_at` | string (date-time) | When consumption was last synced from API |
    | `finalized_at` | string (date-time) | When billing export data arrived |
    | `reconciled_at` | string (date-time) | When reconciliation was applied |
    | `is_finalized` | boolean |  |
    | `is_reconciled` | boolean |  |
    | `adjustment_amount` | string (decimal) |  |
    | `raw_data` | any | Raw consumption data for debugging |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Available customers

Get available Arrow customers that are not yet mapped, with suggestions for Waldur organization matches.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/admin/arrow/customer-mappings/available_customers/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.admin import admin_arrow_customer_mappings_available_customers_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = admin_arrow_customer_mappings_available_customers_retrieve.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`admin_arrow_customer_mappings_available_customers_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_customer_mappings_available_customers_retrieve.py)

=== "TypeScript"

    ```typescript
    import { adminArrowCustomerMappingsAvailableCustomersRetrieve } from 'waldur-js-client';
    
    try {
      const response = await adminArrowCustomerMappingsAvailableCustomersRetrieve({
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
    | `settings_uuid` | string (uuid) |
    | `arrow_customers` | array of objects |
    | `arrow_customers.reference` | string |
    | `arrow_customers.companyName` | string |
    | `arrow_customers.email` | string |
    | `arrow_customers.city` | string |
    | `arrow_customers.countryCode` | string |
    | `waldur_customers` | array of objects |
    | `waldur_customers.uuid` | string (uuid) |
    | `waldur_customers.name` | string |
    | `waldur_customers.abbreviation` | string |
    | `suggestions` | array of objects |
    | `suggestions.arrow_customer` | object |
    | `suggestions.arrow_customer.reference` | string |
    | `suggestions.arrow_customer.companyName` | string |
    | `suggestions.arrow_customer.email` | string |
    | `suggestions.arrow_customer.city` | string |
    | `suggestions.arrow_customer.countryCode` | string |
    | `suggestions.suggested_waldur_customer` | object |
    | `suggestions.suggested_waldur_customer.uuid` | string (uuid) |
    | `suggestions.suggested_waldur_customer.name` | string |
    | `suggestions.suggested_waldur_customer.abbreviation` | string |
    | `suggestions.confidence` | number (double) |
    | `suggestions.existing_mapping` | boolean |

---

### Get billing and consumption summary for this customer mapping

Get billing and consumption summary for this customer mapping.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/admin/arrow/customer-mappings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/billing_summary/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.admin import admin_arrow_customer_mappings_billing_summary_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = admin_arrow_customer_mappings_billing_summary_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`admin_arrow_customer_mappings_billing_summary_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_customer_mappings_billing_summary_retrieve.py)

=== "TypeScript"

    ```typescript
    import { adminArrowCustomerMappingsBillingSummaryRetrieve } from 'waldur-js-client';
    
    try {
      const response = await adminArrowCustomerMappingsBillingSummaryRetrieve({
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
    | `customer_mapping_uuid` | string (uuid) |
    | `arrow_reference` | string |
    | `arrow_company_name` | string |
    | `waldur_customer_uuid` | string (uuid) |
    | `waldur_customer_name` | string |
    | `total_consumption_records` | integer |
    | `total_consumed_sell` | string (decimal) |
    | `total_final_sell` | string (decimal) |
    | `pending_records` | integer |
    | `finalized_records` | integer |
    | `reconciled_records` | integer |
    | `total_billing_syncs` | integer |
    | `total_billing_sell` | string (decimal) |
    | `recent_consumption_records` | array of objects |
    | `recent_consumption_records.uuid` | string (uuid) |
    | `recent_consumption_records.license_reference` | string |
    | `recent_consumption_records.resource_name` | string |
    | `recent_consumption_records.billing_period` | string (date) |
    | `recent_consumption_records.consumed_sell` | string (decimal) |
    | `recent_consumption_records.final_sell` | string (decimal) |
    | `recent_consumption_records.is_finalized` | boolean |
    | `recent_consumption_records.is_reconciled` | boolean |
    | `recent_billing_syncs` | array of objects |
    | `recent_billing_syncs.uuid` | string (uuid) |
    | `recent_billing_syncs.report_period` | string |
    | `recent_billing_syncs.state` | string |
    | `recent_billing_syncs.sell_total` | string (decimal) |
    | `recent_billing_syncs.items_count` | integer |
    | `recent_billing_syncs.created` | string (date-time) |

---

### Discover Arrow licenses for this customer and show linkable Waldur resources

Discover Arrow licenses for this customer and show linkable Waldur resources.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/admin/arrow/customer-mappings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/discover_licenses/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.admin import admin_arrow_customer_mappings_discover_licenses_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = admin_arrow_customer_mappings_discover_licenses_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`admin_arrow_customer_mappings_discover_licenses_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_customer_mappings_discover_licenses_retrieve.py)

=== "TypeScript"

    ```typescript
    import { adminArrowCustomerMappingsDiscoverLicensesRetrieve } from 'waldur-js-client';
    
    try {
      const response = await adminArrowCustomerMappingsDiscoverLicensesRetrieve({
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
    | `customer_mapping_uuid` | string (uuid) |  |
    | `arrow_reference` | string |  |
    | `waldur_customer_name` | string |  |
    | `arrow_licenses` | array of objects | Arrow licenses from billing export for this customer. |
    | `arrow_licenses.license_reference` | string | Arrow license reference (e.g., XSP12345). Use this as resource backend_id. |
    | `arrow_licenses.vendor_name` | string |  |
    | `arrow_licenses.offer_name` | string |  |
    | `arrow_licenses.offer_sku` | string |  |
    | `arrow_licenses.friendly_name` | string |  |
    | `waldur_resources` | array of objects | Waldur resources for this customer. |
    | `waldur_resources.uuid` | string (uuid) |  |
    | `waldur_resources.name` | string |  |
    | `waldur_resources.backend_id` | string | Current backend_id (Arrow license reference if linked). |
    | `waldur_resources.project_name` | string |  |
    | `waldur_resources.offering_name` | string |  |
    | `waldur_resources.state` | string |  |
    | `suggestions` | array of objects | Suggested matches based on name similarity. |
    | `suggestions.resource_uuid` | string (uuid) |  |
    | `suggestions.resource_name` | string |  |
    | `suggestions.license_reference` | string |  |
    | `suggestions.license_name` | string |  |
    | `suggestions.confidence` | number (double) | Confidence score (0-1) based on name similarity. |
    | `error` | string |  |

---

### Fetch fresh consumption and billing data from Arrow API for this customer

Fetch fresh consumption and billing data from Arrow API for this customer.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/admin/arrow/customer-mappings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/fetch_arrow_data/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.admin import admin_arrow_customer_mappings_fetch_arrow_data_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = admin_arrow_customer_mappings_fetch_arrow_data_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`admin_arrow_customer_mappings_fetch_arrow_data_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_customer_mappings_fetch_arrow_data_retrieve.py)

=== "TypeScript"

    ```typescript
    import { adminArrowCustomerMappingsFetchArrowDataRetrieve } from 'waldur-js-client';
    
    try {
      const response = await adminArrowCustomerMappingsFetchArrowDataRetrieve({
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
    | `customer_mapping_uuid` | string (uuid) |  |
    | `arrow_reference` | string |  |
    | `arrow_company_name` | string |  |
    | `waldur_customer_name` | string |  |
    | `period` | string |  |
    | `billing_available` | boolean |  |
    | `billing_lines` | array of objects |  |
    | `billing_lines.vendor_name` | string |  |
    | `billing_lines.subscription_reference` | string |  |
    | `billing_lines.license_reference` | string | Arrow license reference. Used to fetch consumption data. |
    | `billing_lines.offer_sku` | string |  |
    | `billing_lines.classification` | string |  |
    | `billing_lines.quantity` | string (decimal) |  |
    | `billing_lines.sell_price` | string (decimal) |  |
    | `billing_lines.buy_price` | string (decimal) |  |
    | `billing_total_sell` | string (decimal) |  |
    | `billing_total_buy` | string (decimal) |  |
    | `consumption_lines` | array of objects |  |
    | `consumption_lines.license_reference` | string | Arrow license reference (same as resource backend_id). |
    | `consumption_lines.resource_name` | string |  |
    | `consumption_lines.resource_uuid` | string | UUID of the Waldur resource. |
    | `consumption_lines.period` | string |  |
    | `consumption_lines.sell_price` | string (decimal) |  |
    | `consumption_lines.buy_price` | string (decimal) |  |
    | `consumption_lines.error` | string | Error message if fetch failed. |
    | `consumption_total_sell` | string (decimal) |  |
    | `consumption_total_buy` | string (decimal) |  |
    | `total_customer_resources` | integer | Total number of resources for this customer in Waldur. |
    | `resources_with_backend_id` | integer | Number of resources with backend_id set (Arrow license reference). |
    | `matched_resources` | integer | Number of resources for which consumption was successfully fetched. |
    | `error` | string |  |

---

### Customer mappings


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/admin/arrow/customer-mappings/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.admin import admin_arrow_customer_mappings_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = admin_arrow_customer_mappings_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`admin_arrow_customer_mappings_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_customer_mappings_list.py)

=== "TypeScript"

    ```typescript
    import { adminArrowCustomerMappingsList } from 'waldur-js-client';
    
    try {
      const response = await adminArrowCustomerMappingsList({
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
    | `arrow_company_name` | string |  |
    | `arrow_reference` | string |  |
    | `is_active` | boolean |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `settings` | string |  |
    | `settings_uuid` | string (uuid) |  |
    | `waldur_customer` | string |  |
    | `waldur_customer_uuid` | string (uuid) |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `settings` | string (uri) |  |
    | `settings_uuid` | string (uuid) |  |
    | `arrow_reference` | string | Arrow customer ID (e.g., 'XSP661245') |
    | `arrow_company_name` | string | Arrow company name |
    | `waldur_customer` | string (uri) |  |
    | `waldur_customer_uuid` | string (uuid) |  |
    | `waldur_customer_name` | string |  |
    | `is_active` | boolean | Whether this mapping is active |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/admin/arrow/customer-mappings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.admin import admin_arrow_customer_mappings_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = admin_arrow_customer_mappings_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`admin_arrow_customer_mappings_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_customer_mappings_retrieve.py)

=== "TypeScript"

    ```typescript
    import { adminArrowCustomerMappingsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await adminArrowCustomerMappingsRetrieve({
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
    | `settings` | string (uri) |  |
    | `settings_uuid` | string (uuid) |  |
    | `arrow_reference` | string | Arrow customer ID (e.g., 'XSP661245') |
    | `arrow_company_name` | string | Arrow company name |
    | `waldur_customer` | string (uri) |  |
    | `waldur_customer_uuid` | string (uuid) |  |
    | `waldur_customer_name` | string |  |
    | `is_active` | boolean | Whether this mapping is active |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Settings


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/admin/arrow/settings/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.admin import admin_arrow_settings_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = admin_arrow_settings_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`admin_arrow_settings_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_settings_list.py)

=== "TypeScript"

    ```typescript
    import { adminArrowSettingsList } from 'waldur-js-client';
    
    try {
      const response = await adminArrowSettingsList({
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
    | `is_active` | boolean |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `sync_enabled` | boolean |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `api_url` | string (uri) | Arrow API base URL |
    | `api_key` | string | Arrow API Key (leave empty on update to keep current) |
    | `export_type_reference` | string | Billing export template reference |
    | `classification_filter` | string | Filter for IaaS/SaaS classification |
    | `is_active` | boolean | Whether this settings record is active |
    | `sync_enabled` | boolean | Whether automatic billing sync is enabled |
    | `partner_reference` | string | Arrow partner reference (discovered from API) |
    | `partner_name` | string | Arrow partner name (discovered from API) |
    | `invoice_price_source` | any | Which price to use for invoice items: sell or buy |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/admin/arrow/settings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.admin import admin_arrow_settings_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = admin_arrow_settings_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`admin_arrow_settings_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_settings_retrieve.py)

=== "TypeScript"

    ```typescript
    import { adminArrowSettingsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await adminArrowSettingsRetrieve({
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
    | `api_url` | string (uri) | Arrow API base URL |
    | `api_key` | string | Arrow API Key (leave empty on update to keep current) |
    | `export_type_reference` | string | Billing export template reference |
    | `classification_filter` | string | Filter for IaaS/SaaS classification |
    | `is_active` | boolean | Whether this settings record is active |
    | `sync_enabled` | boolean | Whether automatic billing sync is enabled |
    | `partner_reference` | string | Arrow partner reference (discovered from API) |
    | `partner_name` | string | Arrow partner name (discovered from API) |
    | `invoice_price_source` | any | Which price to use for invoice items: sell or buy |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Vendor offering mappings


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/admin/arrow/vendor-offering-mappings/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.admin import admin_arrow_vendor_offering_mappings_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = admin_arrow_vendor_offering_mappings_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`admin_arrow_vendor_offering_mappings_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_vendor_offering_mappings_list.py)

=== "TypeScript"

    ```typescript
    import { adminArrowVendorOfferingMappingsList } from 'waldur-js-client';
    
    try {
      const response = await adminArrowVendorOfferingMappingsList({
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
    | `arrow_vendor_name` | string |  |
    | `is_active` | boolean |  |
    | `offering` | string |  |
    | `offering_uuid` | string (uuid) |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `settings` | string |  |
    | `settings_uuid` | string (uuid) |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `settings` | string (uri) |  |
    | `settings_uuid` | string (uuid) |  |
    | `arrow_vendor_name` | string | Arrow vendor name (e.g., 'Microsoft', 'Amazon Web Services') |
    | `offering` | string (uri) | Waldur marketplace offering for this vendor |
    | `offering_uuid` | string (uuid) |  |
    | `offering_name` | string |  |
    | `offering_type` | string |  |
    | `is_active` | boolean | Whether this mapping is active |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/admin/arrow/vendor-offering-mappings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.admin import admin_arrow_vendor_offering_mappings_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = admin_arrow_vendor_offering_mappings_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`admin_arrow_vendor_offering_mappings_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_vendor_offering_mappings_retrieve.py)

=== "TypeScript"

    ```typescript
    import { adminArrowVendorOfferingMappingsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await adminArrowVendorOfferingMappingsRetrieve({
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
    | `settings` | string (uri) |  |
    | `settings_uuid` | string (uuid) |  |
    | `arrow_vendor_name` | string | Arrow vendor name (e.g., 'Microsoft', 'Amazon Web Services') |
    | `offering` | string (uri) | Waldur marketplace offering for this vendor |
    | `offering_uuid` | string (uuid) |  |
    | `offering_name` | string |  |
    | `offering_type` | string |  |
    | `is_active` | boolean | Whether this mapping is active |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Get vendor names from Arrow catalog API (IAAS category)

Get vendor names from Arrow catalog API (IAAS category).


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/admin/arrow/vendor-offering-mappings/vendor_choices/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.admin import admin_arrow_vendor_offering_mappings_vendor_choices_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = admin_arrow_vendor_offering_mappings_vendor_choices_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`admin_arrow_vendor_offering_mappings_vendor_choices_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_vendor_offering_mappings_vendor_choices_list.py)

=== "TypeScript"

    ```typescript
    import { adminArrowVendorOfferingMappingsVendorChoicesList } from 'waldur-js-client';
    
    try {
      const response = await adminArrowVendorOfferingMappingsVendorChoicesList({
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
    | `arrow_vendor_name` | string |  |
    | `is_active` | boolean |  |
    | `offering` | string |  |
    | `offering_uuid` | string (uuid) |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `settings` | string |  |
    | `settings_uuid` | string (uuid) |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `value` | string |
    | `label` | string |

---

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

### Customer mappings


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/admin/arrow/customer-mappings/ \
      Authorization:"Token YOUR_API_TOKEN" \
      settings="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      arrow_reference="string-value" \
      waldur_customer="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.arrow_customer_mapping_create_request import ArrowCustomerMappingCreateRequest # (1)
    from waldur_api_client.api.admin import admin_arrow_customer_mappings_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ArrowCustomerMappingCreateRequest(
        settings="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        arrow_reference="string-value",
        waldur_customer="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = admin_arrow_customer_mappings_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ArrowCustomerMappingCreateRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/arrow_customer_mapping_create_request.py)
    2.  **API Source:** [`admin_arrow_customer_mappings_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_customer_mappings_create.py)

=== "TypeScript"

    ```typescript
    import { adminArrowCustomerMappingsCreate } from 'waldur-js-client';
    
    try {
      const response = await adminArrowCustomerMappingsCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "settings": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "arrow_reference": "string-value",
        "waldur_customer": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `settings` | string (uuid) | ✓ |  |
    | `arrow_reference` | string | ✓ | Arrow customer ID (e.g., 'XSP661245') |
    | `arrow_company_name` | string |  | Arrow company name |
    | `waldur_customer` | string (uuid) | ✓ |  |
    | `is_active` | boolean |  | Whether this mapping is active |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `settings` | string (uuid) |  |
    | `settings_uuid` | string (uuid) |  |
    | `arrow_reference` | string | Arrow customer ID (e.g., 'XSP661245') |
    | `arrow_company_name` | string | Arrow company name |
    | `waldur_customer` | string (uuid) |  |
    | `waldur_customer_uuid` | string (uuid) |  |
    | `waldur_customer_name` | string |  |
    | `is_active` | boolean | Whether this mapping is active |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Import an Arrow license as a new Waldur resource

Import an Arrow license as a new Waldur resource.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/admin/arrow/customer-mappings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/import_license/ \
      Authorization:"Token YOUR_API_TOKEN" \
      license_reference="string-value" \
      offering_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      project_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.import_license_request_request import ImportLicenseRequestRequest # (1)
    from waldur_api_client.api.admin import admin_arrow_customer_mappings_import_license # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ImportLicenseRequestRequest(
        license_reference="string-value",
        offering_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        project_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = admin_arrow_customer_mappings_import_license.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ImportLicenseRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/import_license_request_request.py)
    2.  **API Source:** [`admin_arrow_customer_mappings_import_license`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_customer_mappings_import_license.py)

=== "TypeScript"

    ```typescript
    import { adminArrowCustomerMappingsImportLicense } from 'waldur-js-client';
    
    try {
      const response = await adminArrowCustomerMappingsImportLicense({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "license_reference": "string-value",
        "offering_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
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
    | `uuid` | string (uuid) | ✓ |


=== "Request Body (required)"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `license_reference` | string | ✓ | Arrow license reference (e.g., XSP12345). Will be set as backend_id. |
    | `license_name` | string |  | Name for the new resource. Defaults to license_reference if not provided. |
    | `offering_uuid` | string (uuid) | ✓ | UUID of the Waldur offering to create the resource under. |
    | `project_uuid` | string (uuid) | ✓ | UUID of the project to create the resource in. |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `resource_uuid` | string (uuid) |
    | `resource_name` | string |
    | `license_reference` | string |
    | `offering_name` | string |
    | `project_name` | string |
    | `success` | boolean |

---

### Link a Waldur resource to an Arrow license by setting its backend_id

Link a Waldur resource to an Arrow license by setting its backend_id.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/admin/arrow/customer-mappings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/link_resource/ \
      Authorization:"Token YOUR_API_TOKEN" \
      resource_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      license_reference="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.link_resource_request_request import LinkResourceRequestRequest # (1)
    from waldur_api_client.api.admin import admin_arrow_customer_mappings_link_resource # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = LinkResourceRequestRequest(
        resource_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        license_reference="string-value"
    )
    response = admin_arrow_customer_mappings_link_resource.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`LinkResourceRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/link_resource_request_request.py)
    2.  **API Source:** [`admin_arrow_customer_mappings_link_resource`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_customer_mappings_link_resource.py)

=== "TypeScript"

    ```typescript
    import { adminArrowCustomerMappingsLinkResource } from 'waldur-js-client';
    
    try {
      const response = await adminArrowCustomerMappingsLinkResource({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "resource_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "license_reference": "string-value"
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
    | `resource_uuid` | string (uuid) | ✓ | UUID of the Waldur resource to link. |
    | `license_reference` | string | ✓ | Arrow license reference to set as backend_id (e.g., XSP12345). |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `resource_uuid` | string (uuid) |
    | `resource_name` | string |
    | `license_reference` | string |
    | `previous_backend_id` | string |
    | `success` | boolean |

---

### Sync customer list from Arrow and update arrow_company_name

Sync customer list from Arrow and update arrow_company_name.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/admin/arrow/customer-mappings/sync_from_arrow/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.sync_from_arrow_request_request import SyncFromArrowRequestRequest # (1)
    from waldur_api_client.api.admin import admin_arrow_customer_mappings_sync_from_arrow # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = SyncFromArrowRequestRequest()
    response = admin_arrow_customer_mappings_sync_from_arrow.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`SyncFromArrowRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/sync_from_arrow_request_request.py)
    2.  **API Source:** [`admin_arrow_customer_mappings_sync_from_arrow`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_customer_mappings_sync_from_arrow.py)

=== "TypeScript"

    ```typescript
    import { adminArrowCustomerMappingsSyncFromArrow } from 'waldur-js-client';
    
    try {
      const response = await adminArrowCustomerMappingsSyncFromArrow({
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


=== "Responses"

    **`200`** - No response body
    

---

### Settings


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/admin/arrow/settings/ \
      Authorization:"Token YOUR_API_TOKEN" \
      api_url="https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      api_key="********"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.arrow_settings_create_request import ArrowSettingsCreateRequest # (1)
    from waldur_api_client.api.admin import admin_arrow_settings_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ArrowSettingsCreateRequest(
        api_url="https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        api_key="********"
    )
    response = admin_arrow_settings_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ArrowSettingsCreateRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/arrow_settings_create_request.py)
    2.  **API Source:** [`admin_arrow_settings_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_settings_create.py)

=== "TypeScript"

    ```typescript
    import { adminArrowSettingsCreate } from 'waldur-js-client';
    
    try {
      const response = await adminArrowSettingsCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "api_url": "https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "api_key": "********"
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
    | `api_url` | string (uri) | ✓ | Arrow API base URL |
    | `api_key` | string | ✓ | Arrow API Key (required for creation)<br>_Constraints: write-only_ |
    | `export_type_reference` | string |  | Billing export template reference |
    | `classification_filter` | string |  | Filter for IaaS/SaaS classification |
    | `is_active` | boolean |  | Whether this settings record is active |
    | `sync_enabled` | boolean |  | Whether automatic billing sync is enabled |
    | `invoice_price_source` | any |  | Which price to use for invoice items: sell or buy |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `api_url` | string (uri) | Arrow API base URL |
    | `export_type_reference` | string | Billing export template reference |
    | `classification_filter` | string | Filter for IaaS/SaaS classification |
    | `is_active` | boolean | Whether this settings record is active |
    | `sync_enabled` | boolean | Whether automatic billing sync is enabled |
    | `partner_reference` | string | Arrow partner reference (discovered from API) |
    | `partner_name` | string | Arrow partner name (discovered from API) |
    | `invoice_price_source` | any | Which price to use for invoice items: sell or buy |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Discover Arrow customers and suggest mappings to Waldur customers

Discover Arrow customers and suggest mappings to Waldur customers.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/admin/arrow/settings/discover_customers/ \
      Authorization:"Token YOUR_API_TOKEN" \
      api_url="https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      api_key="********"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.discover_customers_request_request import DiscoverCustomersRequestRequest # (1)
    from waldur_api_client.api.admin import admin_arrow_settings_discover_customers # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = DiscoverCustomersRequestRequest(
        api_url="https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        api_key="********"
    )
    response = admin_arrow_settings_discover_customers.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`DiscoverCustomersRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/discover_customers_request_request.py)
    2.  **API Source:** [`admin_arrow_settings_discover_customers`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_settings_discover_customers.py)

=== "TypeScript"

    ```typescript
    import { adminArrowSettingsDiscoverCustomers } from 'waldur-js-client';
    
    try {
      const response = await adminArrowSettingsDiscoverCustomers({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "api_url": "https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "api_key": "********"
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
    | `api_url` | string (uri) | ✓ | Arrow API base URL |
    | `api_key` | string | ✓ | Arrow API Key |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `arrow_customers` | array of objects |
    | `arrow_customers.reference` | string |
    | `arrow_customers.companyName` | string |
    | `arrow_customers.email` | string |
    | `arrow_customers.city` | string |
    | `arrow_customers.countryCode` | string |
    | `waldur_customers` | array of objects |
    | `waldur_customers.uuid` | string (uuid) |
    | `waldur_customers.name` | string |
    | `waldur_customers.abbreviation` | string |
    | `suggestions` | array of objects |
    | `suggestions.arrow_customer` | object |
    | `suggestions.arrow_customer.reference` | string |
    | `suggestions.arrow_customer.companyName` | string |
    | `suggestions.arrow_customer.email` | string |
    | `suggestions.arrow_customer.city` | string |
    | `suggestions.arrow_customer.countryCode` | string |
    | `suggestions.suggested_waldur_customer` | object |
    | `suggestions.suggested_waldur_customer.uuid` | string (uuid) |
    | `suggestions.suggested_waldur_customer.name` | string |
    | `suggestions.suggested_waldur_customer.abbreviation` | string |
    | `suggestions.confidence` | number (double) |
    | `suggestions.existing_mapping` | boolean |

---

### Preview settings configuration before saving

Preview settings configuration before saving.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/admin/arrow/settings/preview_settings/ \
      Authorization:"Token YOUR_API_TOKEN" \
      api_url="https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      api_key="********"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.preview_settings_request_request import PreviewSettingsRequestRequest # (1)
    from waldur_api_client.api.admin import admin_arrow_settings_preview_settings # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PreviewSettingsRequestRequest(
        api_url="https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        api_key="********"
    )
    response = admin_arrow_settings_preview_settings.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PreviewSettingsRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/preview_settings_request_request.py)
    2.  **API Source:** [`admin_arrow_settings_preview_settings`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_settings_preview_settings.py)

=== "TypeScript"

    ```typescript
    import { adminArrowSettingsPreviewSettings } from 'waldur-js-client';
    
    try {
      const response = await adminArrowSettingsPreviewSettings({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "api_url": "https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "api_key": "********"
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
    | `api_url` | string (uri) | ✓ | Arrow API base URL |
    | `api_key` | string | ✓ | Arrow API Key |
    | `export_type_reference` | string |  |  |
    | `classification_filter` | string |  | <br>_Constraints: default: `IAAS`_ |
    | `sync_enabled` | boolean |  | <br>_Constraints: default: `False`_ |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `api_url` | string (uri) |
    | `partner_name` | string |
    | `partner_reference` | string |
    | `export_type_reference` | string |
    | `classification_filter` | string |
    | `sync_enabled` | boolean |

---

### Save Arrow settings and customer mappings

Save Arrow settings and customer mappings.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/admin/arrow/settings/save_settings/ \
      Authorization:"Token YOUR_API_TOKEN" \
      api_url="https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      api_key="********"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.save_settings_request_request import SaveSettingsRequestRequest # (1)
    from waldur_api_client.api.admin import admin_arrow_settings_save_settings # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = SaveSettingsRequestRequest(
        api_url="https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        api_key="********"
    )
    response = admin_arrow_settings_save_settings.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`SaveSettingsRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/save_settings_request_request.py)
    2.  **API Source:** [`admin_arrow_settings_save_settings`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_settings_save_settings.py)

=== "TypeScript"

    ```typescript
    import { adminArrowSettingsSaveSettings } from 'waldur-js-client';
    
    try {
      const response = await adminArrowSettingsSaveSettings({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "api_url": "https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "api_key": "********"
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
    | `api_url` | string (uri) | ✓ | Arrow API base URL |
    | `api_key` | string | ✓ | Arrow API Key |
    | `export_type_reference` | string |  |  |
    | `classification_filter` | string |  | <br>_Constraints: default: `IAAS`_ |
    | `sync_enabled` | boolean |  | <br>_Constraints: default: `False`_ |
    | `customer_mappings` | array of objects |  |  |
    | `customer_mappings.arrow_reference` | string | ✓ |  |
    | `customer_mappings.waldur_customer_uuid` | string (uuid) | ✓ |  |


=== "Responses"

    **`201`** - 
    
    | Field | Type |
    |---|---|
    | `settings_uuid` | string (uuid) |
    | `mappings_created` | integer |
    | `message` | string |

---

### Validate Arrow API credentials without saving them

Validate Arrow API credentials without saving them.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/admin/arrow/settings/validate_credentials/ \
      Authorization:"Token YOUR_API_TOKEN" \
      api_url="https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      api_key="********"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.arrow_credentials_request import ArrowCredentialsRequest # (1)
    from waldur_api_client.api.admin import admin_arrow_settings_validate_credentials # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ArrowCredentialsRequest(
        api_url="https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        api_key="********"
    )
    response = admin_arrow_settings_validate_credentials.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ArrowCredentialsRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/arrow_credentials_request.py)
    2.  **API Source:** [`admin_arrow_settings_validate_credentials`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_settings_validate_credentials.py)

=== "TypeScript"

    ```typescript
    import { adminArrowSettingsValidateCredentials } from 'waldur-js-client';
    
    try {
      const response = await adminArrowSettingsValidateCredentials({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "api_url": "https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "api_key": "********"
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
    | `api_url` | string (uri) | ✓ | Arrow API base URL |
    | `api_key` | string | ✓ | Arrow API Key |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `valid` | boolean |
    | `message` | string |
    | `error` | string |
    | `partner_info` | object (free-form) |

---

### Vendor offering mappings


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/admin/arrow/vendor-offering-mappings/ \
      Authorization:"Token YOUR_API_TOKEN" \
      settings="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      arrow_vendor_name="string-value" \
      offering="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.arrow_vendor_offering_mapping_create_request import ArrowVendorOfferingMappingCreateRequest # (1)
    from waldur_api_client.api.admin import admin_arrow_vendor_offering_mappings_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ArrowVendorOfferingMappingCreateRequest(
        settings="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        arrow_vendor_name="string-value",
        offering="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = admin_arrow_vendor_offering_mappings_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ArrowVendorOfferingMappingCreateRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/arrow_vendor_offering_mapping_create_request.py)
    2.  **API Source:** [`admin_arrow_vendor_offering_mappings_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_vendor_offering_mappings_create.py)

=== "TypeScript"

    ```typescript
    import { adminArrowVendorOfferingMappingsCreate } from 'waldur-js-client';
    
    try {
      const response = await adminArrowVendorOfferingMappingsCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "settings": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "arrow_vendor_name": "string-value",
        "offering": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `settings` | string (uuid) | ✓ |  |
    | `arrow_vendor_name` | string | ✓ | Arrow vendor name (e.g., 'Microsoft', 'Amazon Web Services') |
    | `offering` | string (uuid) | ✓ |  |
    | `is_active` | boolean |  | Whether this mapping is active |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `settings` | string (uuid) |  |
    | `settings_uuid` | string (uuid) |  |
    | `arrow_vendor_name` | string | Arrow vendor name (e.g., 'Microsoft', 'Amazon Web Services') |
    | `offering` | string (uuid) |  |
    | `offering_uuid` | string (uuid) |  |
    | `offering_name` | string |  |
    | `offering_type` | string |  |
    | `is_active` | boolean | Whether this mapping is active |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/admin/arrow/customer-mappings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      settings="https://api.example.com/api/settings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      arrow_reference="string-value" \
      waldur_customer="https://api.example.com/api/waldur-customer/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.arrow_customer_mapping_request import ArrowCustomerMappingRequest # (1)
    from waldur_api_client.api.admin import admin_arrow_customer_mappings_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ArrowCustomerMappingRequest(
        settings="https://api.example.com/api/settings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        arrow_reference="string-value",
        waldur_customer="https://api.example.com/api/waldur-customer/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    )
    response = admin_arrow_customer_mappings_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ArrowCustomerMappingRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/arrow_customer_mapping_request.py)
    2.  **API Source:** [`admin_arrow_customer_mappings_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_customer_mappings_update.py)

=== "TypeScript"

    ```typescript
    import { adminArrowCustomerMappingsUpdate } from 'waldur-js-client';
    
    try {
      const response = await adminArrowCustomerMappingsUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "settings": "https://api.example.com/api/settings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "arrow_reference": "string-value",
        "waldur_customer": "https://api.example.com/api/waldur-customer/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
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
    | `settings` | string (uri) | ✓ |  |
    | `arrow_reference` | string | ✓ | Arrow customer ID (e.g., 'XSP661245') |
    | `arrow_company_name` | string |  | Arrow company name |
    | `waldur_customer` | string (uri) | ✓ |  |
    | `is_active` | boolean |  | Whether this mapping is active |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `settings` | string (uri) |  |
    | `settings_uuid` | string (uuid) |  |
    | `arrow_reference` | string | Arrow customer ID (e.g., 'XSP661245') |
    | `arrow_company_name` | string | Arrow company name |
    | `waldur_customer` | string (uri) |  |
    | `waldur_customer_uuid` | string (uuid) |  |
    | `waldur_customer_name` | string |  |
    | `is_active` | boolean | Whether this mapping is active |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/admin/arrow/settings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      api_url="https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.arrow_settings_request import ArrowSettingsRequest # (1)
    from waldur_api_client.api.admin import admin_arrow_settings_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ArrowSettingsRequest(
        api_url="https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    )
    response = admin_arrow_settings_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ArrowSettingsRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/arrow_settings_request.py)
    2.  **API Source:** [`admin_arrow_settings_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_settings_update.py)

=== "TypeScript"

    ```typescript
    import { adminArrowSettingsUpdate } from 'waldur-js-client';
    
    try {
      const response = await adminArrowSettingsUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "api_url": "https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
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
    | `api_url` | string (uri) | ✓ | Arrow API base URL |
    | `api_key` | string |  | Arrow API Key (leave empty on update to keep current) |
    | `export_type_reference` | string |  | Billing export template reference |
    | `classification_filter` | string |  | Filter for IaaS/SaaS classification |
    | `is_active` | boolean |  | Whether this settings record is active |
    | `sync_enabled` | boolean |  | Whether automatic billing sync is enabled |
    | `invoice_price_source` | any |  | Which price to use for invoice items: sell or buy |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `api_url` | string (uri) | Arrow API base URL |
    | `api_key` | string | Arrow API Key (leave empty on update to keep current) |
    | `export_type_reference` | string | Billing export template reference |
    | `classification_filter` | string | Filter for IaaS/SaaS classification |
    | `is_active` | boolean | Whether this settings record is active |
    | `sync_enabled` | boolean | Whether automatic billing sync is enabled |
    | `partner_reference` | string | Arrow partner reference (discovered from API) |
    | `partner_name` | string | Arrow partner name (discovered from API) |
    | `invoice_price_source` | any | Which price to use for invoice items: sell or buy |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/admin/arrow/vendor-offering-mappings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      settings="https://api.example.com/api/settings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      arrow_vendor_name="string-value" \
      offering="https://api.example.com/api/offering/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.arrow_vendor_offering_mapping_request import ArrowVendorOfferingMappingRequest # (1)
    from waldur_api_client.api.admin import admin_arrow_vendor_offering_mappings_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ArrowVendorOfferingMappingRequest(
        settings="https://api.example.com/api/settings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        arrow_vendor_name="string-value",
        offering="https://api.example.com/api/offering/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    )
    response = admin_arrow_vendor_offering_mappings_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ArrowVendorOfferingMappingRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/arrow_vendor_offering_mapping_request.py)
    2.  **API Source:** [`admin_arrow_vendor_offering_mappings_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_vendor_offering_mappings_update.py)

=== "TypeScript"

    ```typescript
    import { adminArrowVendorOfferingMappingsUpdate } from 'waldur-js-client';
    
    try {
      const response = await adminArrowVendorOfferingMappingsUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "settings": "https://api.example.com/api/settings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "arrow_vendor_name": "string-value",
        "offering": "https://api.example.com/api/offering/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
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
    | `settings` | string (uri) | ✓ |  |
    | `arrow_vendor_name` | string | ✓ | Arrow vendor name (e.g., 'Microsoft', 'Amazon Web Services') |
    | `offering` | string (uri) | ✓ | Waldur marketplace offering for this vendor |
    | `is_active` | boolean |  | Whether this mapping is active |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `settings` | string (uri) |  |
    | `settings_uuid` | string (uuid) |  |
    | `arrow_vendor_name` | string | Arrow vendor name (e.g., 'Microsoft', 'Amazon Web Services') |
    | `offering` | string (uri) | Waldur marketplace offering for this vendor |
    | `offering_uuid` | string (uuid) |  |
    | `offering_name` | string |  |
    | `offering_type` | string |  |
    | `is_active` | boolean | Whether this mapping is active |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/admin/arrow/customer-mappings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_arrow_customer_mapping_request import PatchedArrowCustomerMappingRequest # (1)
    from waldur_api_client.api.admin import admin_arrow_customer_mappings_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedArrowCustomerMappingRequest()
    response = admin_arrow_customer_mappings_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedArrowCustomerMappingRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_arrow_customer_mapping_request.py)
    2.  **API Source:** [`admin_arrow_customer_mappings_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_customer_mappings_partial_update.py)

=== "TypeScript"

    ```typescript
    import { adminArrowCustomerMappingsPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await adminArrowCustomerMappingsPartialUpdate({
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
    | `settings` | string (uri) |  |  |
    | `arrow_reference` | string |  | Arrow customer ID (e.g., 'XSP661245') |
    | `arrow_company_name` | string |  | Arrow company name |
    | `waldur_customer` | string (uri) |  |  |
    | `is_active` | boolean |  | Whether this mapping is active |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `settings` | string (uri) |  |
    | `settings_uuid` | string (uuid) |  |
    | `arrow_reference` | string | Arrow customer ID (e.g., 'XSP661245') |
    | `arrow_company_name` | string | Arrow company name |
    | `waldur_customer` | string (uri) |  |
    | `waldur_customer_uuid` | string (uuid) |  |
    | `waldur_customer_name` | string |  |
    | `is_active` | boolean | Whether this mapping is active |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/admin/arrow/settings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_arrow_settings_request import PatchedArrowSettingsRequest # (1)
    from waldur_api_client.api.admin import admin_arrow_settings_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedArrowSettingsRequest()
    response = admin_arrow_settings_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedArrowSettingsRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_arrow_settings_request.py)
    2.  **API Source:** [`admin_arrow_settings_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_settings_partial_update.py)

=== "TypeScript"

    ```typescript
    import { adminArrowSettingsPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await adminArrowSettingsPartialUpdate({
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
    | `api_url` | string (uri) |  | Arrow API base URL |
    | `api_key` | string |  | Arrow API Key (leave empty on update to keep current) |
    | `export_type_reference` | string |  | Billing export template reference |
    | `classification_filter` | string |  | Filter for IaaS/SaaS classification |
    | `is_active` | boolean |  | Whether this settings record is active |
    | `sync_enabled` | boolean |  | Whether automatic billing sync is enabled |
    | `invoice_price_source` | any |  | Which price to use for invoice items: sell or buy |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `api_url` | string (uri) | Arrow API base URL |
    | `api_key` | string | Arrow API Key (leave empty on update to keep current) |
    | `export_type_reference` | string | Billing export template reference |
    | `classification_filter` | string | Filter for IaaS/SaaS classification |
    | `is_active` | boolean | Whether this settings record is active |
    | `sync_enabled` | boolean | Whether automatic billing sync is enabled |
    | `partner_reference` | string | Arrow partner reference (discovered from API) |
    | `partner_name` | string | Arrow partner name (discovered from API) |
    | `invoice_price_source` | any | Which price to use for invoice items: sell or buy |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/admin/arrow/vendor-offering-mappings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_arrow_vendor_offering_mapping_request import PatchedArrowVendorOfferingMappingRequest # (1)
    from waldur_api_client.api.admin import admin_arrow_vendor_offering_mappings_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedArrowVendorOfferingMappingRequest()
    response = admin_arrow_vendor_offering_mappings_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedArrowVendorOfferingMappingRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_arrow_vendor_offering_mapping_request.py)
    2.  **API Source:** [`admin_arrow_vendor_offering_mappings_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_vendor_offering_mappings_partial_update.py)

=== "TypeScript"

    ```typescript
    import { adminArrowVendorOfferingMappingsPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await adminArrowVendorOfferingMappingsPartialUpdate({
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
    | `settings` | string (uri) |  |  |
    | `arrow_vendor_name` | string |  | Arrow vendor name (e.g., 'Microsoft', 'Amazon Web Services') |
    | `offering` | string (uri) |  | Waldur marketplace offering for this vendor |
    | `is_active` | boolean |  | Whether this mapping is active |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `settings` | string (uri) |  |
    | `settings_uuid` | string (uuid) |  |
    | `arrow_vendor_name` | string | Arrow vendor name (e.g., 'Microsoft', 'Amazon Web Services') |
    | `offering` | string (uri) | Waldur marketplace offering for this vendor |
    | `offering_uuid` | string (uuid) |  |
    | `offering_name` | string |  |
    | `offering_type` | string |  |
    | `is_active` | boolean | Whether this mapping is active |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/admin/arrow/customer-mappings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.admin import admin_arrow_customer_mappings_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = admin_arrow_customer_mappings_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`admin_arrow_customer_mappings_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_customer_mappings_destroy.py)

=== "TypeScript"

    ```typescript
    import { adminArrowCustomerMappingsDestroy } from 'waldur-js-client';
    
    try {
      const response = await adminArrowCustomerMappingsDestroy({
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

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/admin/arrow/settings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.admin import admin_arrow_settings_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = admin_arrow_settings_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`admin_arrow_settings_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_settings_destroy.py)

=== "TypeScript"

    ```typescript
    import { adminArrowSettingsDestroy } from 'waldur-js-client';
    
    try {
      const response = await adminArrowSettingsDestroy({
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

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/admin/arrow/vendor-offering-mappings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.admin import admin_arrow_vendor_offering_mappings_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = admin_arrow_vendor_offering_mappings_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`admin_arrow_vendor_offering_mappings_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/admin/admin_arrow_vendor_offering_mappings_destroy.py)

=== "TypeScript"

    ```typescript
    import { adminArrowVendorOfferingMappingsDestroy } from 'waldur-js-client';
    
    try {
      const response = await adminArrowVendorOfferingMappingsDestroy({
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
