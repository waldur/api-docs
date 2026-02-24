# Marketplace Software Catalogs

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-software-catalogs/` | [List software catalogs](#list-software-catalogs) |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-software-catalogs/{uuid}/` | [Retrieve a software catalog](#retrieve-a-software-catalog) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-software-catalogs/` | [Create a software catalog](#create-a-software-catalog) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-software-catalogs/{uuid}/update_catalog/` | [Trigger async update for an existing catalog](#trigger-async-update-for-an-existing-catalog) |
| <span class="http-badge http-put">PUT</span> | `/api/marketplace-software-catalogs/{uuid}/` | [Update a software catalog](#update-a-software-catalog) |
| <span class="http-badge http-patch">PATCH</span> | `/api/marketplace-software-catalogs/{uuid}/` | [Partially update a software catalog](#partially-update-a-software-catalog) |
| <span class="http-badge http-delete">DELETE</span> | `/api/marketplace-software-catalogs/{uuid}/` | [Delete a software catalog](#delete-a-software-catalog) |
| **Other Actions** | | |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-software-catalogs/discover/` | [Discover available software catalog versions](#discover-available-software-catalog-versions) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-software-catalogs/import_catalog/` | [Import a new software catalog](#import-a-new-software-catalog) |

---
## Core CRUD


### List software catalogs

Returns a paginated list of available software catalogs, such as EESSI or Spack.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-software-catalogs/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.catalog_type_enum import CatalogTypeEnum # (1)
    from waldur_api_client.models.software_catalog_o_enum import SoftwareCatalogOEnum # (2)
    from waldur_api_client.api.marketplace_software_catalogs import marketplace_software_catalogs_list # (3)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_software_catalogs_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`CatalogTypeEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/catalog_type_enum.py)
    2.  **Model Source:** [`SoftwareCatalogOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/software_catalog_o_enum.py)
    3.  **API Source:** [`marketplace_software_catalogs_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_software_catalogs/marketplace_software_catalogs_list.py)

=== "TypeScript"

    ```typescript
    import { marketplaceSoftwareCatalogsList } from 'waldur-js-client';
    
    try {
      const response = await marketplaceSoftwareCatalogsList({
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
    | `auto_update_enabled` | boolean | Filter catalogs by auto-update status |
    | `catalog_type` | string | Filter by catalog type (binary_runtime, source_package, package_manager)<br><br><br>_Enum: `binary_runtime`, `source_package`, `package_manager`_ |
    | `description` | string | Filter catalogs by description (case-insensitive partial match) |
    | `name` | string |  |
    | `o` | array | Ordering<br><br> |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `version` | string |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `name` | string | Catalog name (e.g., EESSI, Spack) |
    | `version` | string | Catalog version (e.g., 2023.06, 0.21.0) |
    | `catalog_type` | any | Type of software catalog |
    | `catalog_type_display` | string |  |
    | `source_url` | string (uri) | Catalog source URL |
    | `description` | string |  |
    | `metadata` | any | Catalog-specific metadata (architecture maps, API endpoints, etc.) |
    | `auto_update_enabled` | boolean | Whether to automatically update this catalog via scheduled tasks |
    | `last_update_attempt` | string (date-time) |  |
    | `last_successful_update` | string (date-time) |  |
    | `update_errors` | string |  |
    | `package_count` | integer |  |
    | `version_count` | integer |  |
    | `target_count` | integer |  |

---

### Retrieve a software catalog

Returns the details of a specific software catalog, including its name, version, and the number of packages it contains.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-software-catalogs/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_software_catalogs import marketplace_software_catalogs_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_software_catalogs_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_software_catalogs_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_software_catalogs/marketplace_software_catalogs_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceSoftwareCatalogsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceSoftwareCatalogsRetrieve({
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
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `name` | string | Catalog name (e.g., EESSI, Spack) |
    | `version` | string | Catalog version (e.g., 2023.06, 0.21.0) |
    | `catalog_type` | any | Type of software catalog |
    | `catalog_type_display` | string |  |
    | `source_url` | string (uri) | Catalog source URL |
    | `description` | string |  |
    | `metadata` | any | Catalog-specific metadata (architecture maps, API endpoints, etc.) |
    | `auto_update_enabled` | boolean | Whether to automatically update this catalog via scheduled tasks |
    | `last_update_attempt` | string (date-time) |  |
    | `last_successful_update` | string (date-time) |  |
    | `update_errors` | string |  |
    | `package_count` | integer |  |
    | `version_count` | integer |  |
    | `target_count` | integer |  |

---

### Create a software catalog

Creates a new software catalog. Requires staff permissions.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-software-catalogs/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-marketplace-software-catalog" \
      version="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.software_catalog_request import SoftwareCatalogRequest # (1)
    from waldur_api_client.api.marketplace_software_catalogs import marketplace_software_catalogs_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = SoftwareCatalogRequest(
        name="my-awesome-marketplace-software-catalog",
        version="string-value"
    )
    response = marketplace_software_catalogs_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`SoftwareCatalogRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/software_catalog_request.py)
    2.  **API Source:** [`marketplace_software_catalogs_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_software_catalogs/marketplace_software_catalogs_create.py)

=== "TypeScript"

    ```typescript
    import { marketplaceSoftwareCatalogsCreate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceSoftwareCatalogsCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "name": "my-awesome-marketplace-software-catalog",
        "version": "string-value"
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
    | `name` | string | ✓ | Catalog name (e.g., EESSI, Spack) |
    | `version` | string | ✓ | Catalog version (e.g., 2023.06, 0.21.0) |
    | `catalog_type` | any |  | Type of software catalog<br>_Constraints: default: `binary_runtime`_ |
    | `source_url` | string (uri) |  | Catalog source URL |
    | `description` | string |  |  |
    | `metadata` | any |  | Catalog-specific metadata (architecture maps, API endpoints, etc.) |
    | `auto_update_enabled` | boolean |  | Whether to automatically update this catalog via scheduled tasks |
    | `update_errors` | string |  |  |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `name` | string | Catalog name (e.g., EESSI, Spack) |
    | `version` | string | Catalog version (e.g., 2023.06, 0.21.0) |
    | `catalog_type` | any | Type of software catalog |
    | `catalog_type_display` | string |  |
    | `source_url` | string (uri) | Catalog source URL |
    | `description` | string |  |
    | `metadata` | any | Catalog-specific metadata (architecture maps, API endpoints, etc.) |
    | `auto_update_enabled` | boolean | Whether to automatically update this catalog via scheduled tasks |
    | `last_update_attempt` | string (date-time) |  |
    | `last_successful_update` | string (date-time) |  |
    | `update_errors` | string |  |
    | `package_count` | integer |  |
    | `version_count` | integer |  |
    | `target_count` | integer |  |

---

### Trigger async update for an existing catalog

Triggers a Celery task to update the given catalog from its upstream source. Returns 202 Accepted immediately. Staff only.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-software-catalogs/a1b2c3d4-e5f6-7890-abcd-ef1234567890/update_catalog/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-marketplace-software-catalog" \
      version="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.software_catalog_request import SoftwareCatalogRequest # (1)
    from waldur_api_client.api.marketplace_software_catalogs import marketplace_software_catalogs_update_catalog # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = SoftwareCatalogRequest(
        name="my-awesome-marketplace-software-catalog",
        version="string-value"
    )
    response = marketplace_software_catalogs_update_catalog.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`SoftwareCatalogRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/software_catalog_request.py)
    2.  **API Source:** [`marketplace_software_catalogs_update_catalog`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_software_catalogs/marketplace_software_catalogs_update_catalog.py)

=== "TypeScript"

    ```typescript
    import { marketplaceSoftwareCatalogsUpdateCatalog } from 'waldur-js-client';
    
    try {
      const response = await marketplaceSoftwareCatalogsUpdateCatalog({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "name": "my-awesome-marketplace-software-catalog",
        "version": "string-value"
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
    | `name` | string | ✓ | Catalog name (e.g., EESSI, Spack) |
    | `version` | string | ✓ | Catalog version (e.g., 2023.06, 0.21.0) |
    | `catalog_type` | any |  | Type of software catalog<br>_Constraints: default: `binary_runtime`_ |
    | `source_url` | string (uri) |  | Catalog source URL |
    | `description` | string |  |  |
    | `metadata` | any |  | Catalog-specific metadata (architecture maps, API endpoints, etc.) |
    | `auto_update_enabled` | boolean |  | Whether to automatically update this catalog via scheduled tasks |
    | `update_errors` | string |  |  |


=== "Responses"

    **`202`** - No response body
    

---

### Update a software catalog

Updates an existing software catalog. Requires staff permissions.


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/marketplace-software-catalogs/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-marketplace-software-catalog" \
      version="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.software_catalog_request import SoftwareCatalogRequest # (1)
    from waldur_api_client.api.marketplace_software_catalogs import marketplace_software_catalogs_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = SoftwareCatalogRequest(
        name="my-awesome-marketplace-software-catalog",
        version="string-value"
    )
    response = marketplace_software_catalogs_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`SoftwareCatalogRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/software_catalog_request.py)
    2.  **API Source:** [`marketplace_software_catalogs_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_software_catalogs/marketplace_software_catalogs_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceSoftwareCatalogsUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceSoftwareCatalogsUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "name": "my-awesome-marketplace-software-catalog",
        "version": "string-value"
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
    | `name` | string | ✓ | Catalog name (e.g., EESSI, Spack) |
    | `version` | string | ✓ | Catalog version (e.g., 2023.06, 0.21.0) |
    | `catalog_type` | any |  | Type of software catalog<br>_Constraints: default: `binary_runtime`_ |
    | `source_url` | string (uri) |  | Catalog source URL |
    | `description` | string |  |  |
    | `metadata` | any |  | Catalog-specific metadata (architecture maps, API endpoints, etc.) |
    | `auto_update_enabled` | boolean |  | Whether to automatically update this catalog via scheduled tasks |
    | `update_errors` | string |  |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `name` | string | Catalog name (e.g., EESSI, Spack) |
    | `version` | string | Catalog version (e.g., 2023.06, 0.21.0) |
    | `catalog_type` | any | Type of software catalog |
    | `catalog_type_display` | string |  |
    | `source_url` | string (uri) | Catalog source URL |
    | `description` | string |  |
    | `metadata` | any | Catalog-specific metadata (architecture maps, API endpoints, etc.) |
    | `auto_update_enabled` | boolean | Whether to automatically update this catalog via scheduled tasks |
    | `last_update_attempt` | string (date-time) |  |
    | `last_successful_update` | string (date-time) |  |
    | `update_errors` | string |  |
    | `package_count` | integer |  |
    | `version_count` | integer |  |
    | `target_count` | integer |  |

---

### Partially update a software catalog

Partially updates an existing software catalog. Requires staff permissions.


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/marketplace-software-catalogs/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_software_catalog_request import PatchedSoftwareCatalogRequest # (1)
    from waldur_api_client.api.marketplace_software_catalogs import marketplace_software_catalogs_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedSoftwareCatalogRequest()
    response = marketplace_software_catalogs_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedSoftwareCatalogRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_software_catalog_request.py)
    2.  **API Source:** [`marketplace_software_catalogs_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_software_catalogs/marketplace_software_catalogs_partial_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceSoftwareCatalogsPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceSoftwareCatalogsPartialUpdate({
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
    | `name` | string |  | Catalog name (e.g., EESSI, Spack) |
    | `version` | string |  | Catalog version (e.g., 2023.06, 0.21.0) |
    | `catalog_type` | any |  | Type of software catalog<br>_Constraints: default: `binary_runtime`_ |
    | `source_url` | string (uri) |  | Catalog source URL |
    | `description` | string |  |  |
    | `metadata` | any |  | Catalog-specific metadata (architecture maps, API endpoints, etc.) |
    | `auto_update_enabled` | boolean |  | Whether to automatically update this catalog via scheduled tasks |
    | `update_errors` | string |  |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `name` | string | Catalog name (e.g., EESSI, Spack) |
    | `version` | string | Catalog version (e.g., 2023.06, 0.21.0) |
    | `catalog_type` | any | Type of software catalog |
    | `catalog_type_display` | string |  |
    | `source_url` | string (uri) | Catalog source URL |
    | `description` | string |  |
    | `metadata` | any | Catalog-specific metadata (architecture maps, API endpoints, etc.) |
    | `auto_update_enabled` | boolean | Whether to automatically update this catalog via scheduled tasks |
    | `last_update_attempt` | string (date-time) |  |
    | `last_successful_update` | string (date-time) |  |
    | `update_errors` | string |  |
    | `package_count` | integer |  |
    | `version_count` | integer |  |
    | `target_count` | integer |  |

---

### Delete a software catalog

Deletes a software catalog. Requires staff permissions.


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/marketplace-software-catalogs/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_software_catalogs import marketplace_software_catalogs_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_software_catalogs_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_software_catalogs_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_software_catalogs/marketplace_software_catalogs_destroy.py)

=== "TypeScript"

    ```typescript
    import { marketplaceSoftwareCatalogsDestroy } from 'waldur-js-client';
    
    try {
      const response = await marketplaceSoftwareCatalogsDestroy({
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

## Other Actions


### Discover available software catalog versions

Queries upstream sources (EESSI, Spack) for available catalog versions without creating anything. Returns detected versions and whether an update is available compared to existing database records.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-software-catalogs/discover/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.catalog_type_enum import CatalogTypeEnum # (1)
    from waldur_api_client.models.software_catalog_o_enum import SoftwareCatalogOEnum # (2)
    from waldur_api_client.api.marketplace_software_catalogs import marketplace_software_catalogs_discover_list # (3)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_software_catalogs_discover_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`CatalogTypeEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/catalog_type_enum.py)
    2.  **Model Source:** [`SoftwareCatalogOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/software_catalog_o_enum.py)
    3.  **API Source:** [`marketplace_software_catalogs_discover_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_software_catalogs/marketplace_software_catalogs_discover_list.py)

=== "TypeScript"

    ```typescript
    import { marketplaceSoftwareCatalogsDiscoverList } from 'waldur-js-client';
    
    try {
      const response = await marketplaceSoftwareCatalogsDiscoverList({
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
    | `auto_update_enabled` | boolean | Filter catalogs by auto-update status |
    | `catalog_type` | string | Filter by catalog type (binary_runtime, source_package, package_manager)<br><br><br>_Enum: `binary_runtime`, `source_package`, `package_manager`_ |
    | `description` | string | Filter catalogs by description (case-insensitive partial match) |
    | `name` | string |  |
    | `o` | array | Ordering<br><br> |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `version` | string |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `name` | string |
    | `catalog_type` | string |
    | `latest_version` | string |
    | `existing` | boolean |
    | `existing_version` | string |
    | `update_available` | boolean |

---

### Import a new software catalog

Creates a new catalog record and triggers async data loading via Celery. Returns 202 Accepted immediately. Staff only.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-software-catalogs/import_catalog/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="EESSI"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.software_catalog_import_request import SoftwareCatalogImportRequest # (1)
    from waldur_api_client.api.marketplace_software_catalogs import marketplace_software_catalogs_import_catalog # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = SoftwareCatalogImportRequest(
        name="EESSI"
    )
    response = marketplace_software_catalogs_import_catalog.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`SoftwareCatalogImportRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/software_catalog_import_request.py)
    2.  **API Source:** [`marketplace_software_catalogs_import_catalog`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_software_catalogs/marketplace_software_catalogs_import_catalog.py)

=== "TypeScript"

    ```typescript
    import { marketplaceSoftwareCatalogsImportCatalog } from 'waldur-js-client';
    
    try {
      const response = await marketplaceSoftwareCatalogsImportCatalog({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "name": "EESSI"
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
    | `name` | string | ✓ |


=== "Responses"

    **`202`** - No response body
    

---
