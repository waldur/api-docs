# Admin Arrow Settings

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/settings/` | [List Admin Arrow Settings](#list-admin-arrow-settings) |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/settings/{uuid}/` | [Retrieve](#retrieve) |
| **Management** | | |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/settings/discover_customers/` | [Discover Arrow customers and suggest mappings to Waldur customers](#discover-arrow-customers-and-suggest-mappings-to-waldur-customers) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/settings/preview_settings/` | [Preview settings configuration before saving](#preview-settings-configuration-before-saving) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/settings/save_settings/` | [Save Arrow settings and customer mappings](#save-arrow-settings-and-customer-mappings) |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/settings/validate_credentials/` | [Validate Arrow API credentials without saving them](#validate-arrow-api-credentials-without-saving-them) |
| **Other Actions** | | |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/settings/` | [Create](#create) |
| <span class="http-badge http-put">PUT</span> | `/api/admin/arrow/settings/{uuid}/` | [Update](#update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/admin/arrow/settings/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-delete">DELETE</span> | `/api/admin/arrow/settings/{uuid}/` | [Delete](#delete) |

---
## Core CRUD


### List Admin Arrow Settings


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
    | `invoice_item_prefix` | string | Prefix for invoice item names (e.g. 'Arrow consumption') |
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
    | `invoice_item_prefix` | string | Prefix for invoice item names (e.g. 'Arrow consumption') |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

## Management


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
    | `export_types` | array of objects |
    | `export_types.reference` | string |
    | `export_types.name` | string |
    | `export_types.required_fields_total` | integer |
    | `export_types.required_fields_found` | integer |
    | `export_types.important_fields_total` | integer |
    | `export_types.important_fields_found` | integer |
    | `export_types.missing_required_fields` | array of strings |
    | `export_types.missing_important_fields` | array of strings |
    | `export_types.compatible` | boolean |
    | `export_types.recommended` | boolean |

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

## Other Actions


### Create


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
    | `invoice_item_prefix` | string |  | Prefix for invoice item names (e.g. 'Arrow consumption') |


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
    | `invoice_item_prefix` | string | Prefix for invoice item names (e.g. 'Arrow consumption') |
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
    | `invoice_item_prefix` | string |  | Prefix for invoice item names (e.g. 'Arrow consumption') |


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
    | `invoice_item_prefix` | string | Prefix for invoice item names (e.g. 'Arrow consumption') |
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
    | `invoice_item_prefix` | string |  | Prefix for invoice item names (e.g. 'Arrow consumption') |


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
    | `invoice_item_prefix` | string | Prefix for invoice item names (e.g. 'Arrow consumption') |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

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
