# Admin Arrow Billing Sync Items

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/billing-sync-items/` | [Billing sync items](#billing-sync-items) |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/billing-sync-items/{uuid}/` | [Retrieve](#retrieve) |

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
    | `billing_sync` | string (uri) |  |
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
