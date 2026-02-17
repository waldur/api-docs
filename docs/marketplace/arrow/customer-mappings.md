# Admin Arrow Customer Mappings

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/customer-mappings/` | [Customer mappings](#customer-mappings) |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/customer-mappings/{uuid}/` | [Retrieve](#retrieve) |
| **Data Retrieval** | | |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/customer-mappings/available_customers/` | [Available customers](#available-customers) |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/customer-mappings/{uuid}/billing_summary/` | [Get billing and consumption summary for this customer mapping](#get-billing-and-consumption-summary-for-this-customer-mapping) |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/customer-mappings/{uuid}/discover_licenses/` | [Discover Arrow licenses for this customer and show linkable Waldur resources](#discover-arrow-licenses-for-this-customer-and-show-linkable-waldur-resources) |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/customer-mappings/{uuid}/fetch_arrow_data/` | [Fetch fresh consumption and billing data from Arrow API for this customer](#fetch-fresh-consumption-and-billing-data-from-arrow-api-for-this-customer) |
| **Sync & Management** | | |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/customer-mappings/{uuid}/import_license/` | [Import an Arrow license as a new Waldur resource](#import-an-arrow-license-as-a-new-waldur-resource) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/customer-mappings/{uuid}/link_resource/` | [Link a Waldur resource to an Arrow license by setting its backend_id](#link-a-waldur-resource-to-an-arrow-license-by-setting-its-backend_id) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/customer-mappings/sync_from_arrow/` | [Sync customer list from Arrow and update arrow_company_name](#sync-customer-list-from-arrow-and-update-arrow_company_name) |
| **Other Actions** | | |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/customer-mappings/` | [Customer mappings](#customer-mappings) |
| <span class="http-badge http-put">PUT</span> | `/api/admin/arrow/customer-mappings/{uuid}/` | [Update](#update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/admin/arrow/customer-mappings/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-delete">DELETE</span> | `/api/admin/arrow/customer-mappings/{uuid}/` | [Delete](#delete) |

---
## Core CRUD


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
    | `settings` | string (uri) |  |
    | `settings_uuid` | string (uuid) |  |
    | `waldur_customer` | string (uri) |  |
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

## Data Retrieval


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

## Sync & Management


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

## Other Actions


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
