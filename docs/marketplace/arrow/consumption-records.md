# Admin Arrow Consumption Records

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/consumption-records/` | [Consumption records](#consumption-records) |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/consumption-records/{uuid}/` | [Retrieve](#retrieve) |

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
    | `resource` | string (uri) |  |
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
