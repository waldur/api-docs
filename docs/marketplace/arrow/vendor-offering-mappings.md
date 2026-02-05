# Admin Arrow Vendor Offering Mappings

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/vendor-offering-mappings/` | [Vendor offering mappings](#vendor-offering-mappings) |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/vendor-offering-mappings/{uuid}/` | [Retrieve](#retrieve) |
| **Data** | | |
| <span class="http-badge http-get">GET</span> | `/api/admin/arrow/vendor-offering-mappings/vendor_choices/` | [Get vendor names from Arrow catalog API (IAAS category)](#get-vendor-names-from-arrow-catalog-api-iaas-category) |
| **Other Actions** | | |
| <span class="http-badge http-post">POST</span> | `/api/admin/arrow/vendor-offering-mappings/` | [Vendor offering mappings](#vendor-offering-mappings) |
| <span class="http-badge http-put">PUT</span> | `/api/admin/arrow/vendor-offering-mappings/{uuid}/` | [Update](#update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/admin/arrow/vendor-offering-mappings/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-delete">DELETE</span> | `/api/admin/arrow/vendor-offering-mappings/{uuid}/` | [Delete](#delete) |

---
## Core CRUD


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

## Data


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

## Other Actions


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
