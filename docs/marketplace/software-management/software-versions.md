# Marketplace Software Versions

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-software-versions/` | [List software versions](#list-software-versions) |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-software-versions/{uuid}/` | [Retrieve a software version](#retrieve-a-software-version) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-software-versions/` | [Create a software version](#create-a-software-version) |
| <span class="http-badge http-put">PUT</span> | `/api/marketplace-software-versions/{uuid}/` | [Update a software version](#update-a-software-version) |
| <span class="http-badge http-patch">PATCH</span> | `/api/marketplace-software-versions/{uuid}/` | [Partially update a software version](#partially-update-a-software-version) |
| <span class="http-badge http-delete">DELETE</span> | `/api/marketplace-software-versions/{uuid}/` | [Delete a software version](#delete-a-software-version) |

---

### List software versions

Returns a paginated list of software versions. Can be filtered by package, catalog, offering, or CPU architecture.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-software-versions/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.catalog_type_enum import CatalogTypeEnum # (1)
    from waldur_api_client.models.software_version_o_enum import SoftwareVersionOEnum # (2)
    from waldur_api_client.api.marketplace_software_versions import marketplace_software_versions_list # (3)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_software_versions_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`CatalogTypeEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/catalog_type_enum.py)
    2.  **Model Source:** [`SoftwareVersionOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/software_version_o_enum.py)
    3.  **API Source:** [`marketplace_software_versions_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_software_versions/marketplace_software_versions_list.py)

=== "TypeScript"

    ```typescript
    import { marketplaceSoftwareVersionsList } from 'waldur-js-client';
    
    try {
      const response = await marketplaceSoftwareVersionsList({
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
    | `catalog_type` | string | Filter versions by catalog type (binary_runtime, source_package, package_manager)<br><br><br>_Enum: `binary_runtime`, `source_package`, `package_manager`_ |
    | `catalog_uuid` | string (uuid) |  |
    | `cpu_family` | string |  |
    | `cpu_microarchitecture` | string |  |
    | `o` | array | Ordering<br><br> |
    | `offering_uuid` | string (uuid) |  |
    | `package_name` | string |  |
    | `package_uuid` | string (uuid) |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `release_date_after` | string (date) | Filter versions by release date range (release_date_after, release_date_before) |
    | `release_date_before` | string (date) | Filter versions by release date range (release_date_after, release_date_before) |
    | `toolchain_families_compatibility` | string | Filter versions compatible with a specific toolchain family (e.g., foss_2022b) |
    | `toolchain_name` | string | Filter versions by toolchain name (e.g., foss, gfbf) |
    | `toolchain_version` | string | Filter versions by toolchain version (e.g., 2023b) |
    | `version` | string |  |
    | `version_exact` | string | Filter versions by exact version string |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `version` | string |  |
    | `release_date` | string (date) |  |
    | `dependencies` | any | Package dependencies (format varies by catalog type) |
    | `metadata` | any | Version-specific metadata (toolchains, build info, modules, etc.) |
    | `package_name` | string |  |
    | `catalog_type` | string |  |
    | `target_count` | integer |  |
    | `module` | object (free-form) |  |
    | `required_modules` | array of anys |  |
    | `extensions` | array of anys |  |
    | `toolchain` | object (free-form) |  |
    | `toolchain_families_compatibility` | array of anys |  |

---

### Retrieve a software version

Returns the details of a specific software version, including its release date and target count.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-software-versions/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_software_versions import marketplace_software_versions_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_software_versions_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_software_versions_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_software_versions/marketplace_software_versions_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceSoftwareVersionsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceSoftwareVersionsRetrieve({
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
    | `version` | string |  |
    | `release_date` | string (date) |  |
    | `dependencies` | any | Package dependencies (format varies by catalog type) |
    | `metadata` | any | Version-specific metadata (toolchains, build info, modules, etc.) |
    | `package_name` | string |  |
    | `catalog_type` | string |  |
    | `target_count` | integer |  |
    | `module` | object (free-form) |  |
    | `required_modules` | array of anys |  |
    | `extensions` | array of anys |  |
    | `toolchain` | object (free-form) |  |
    | `toolchain_families_compatibility` | array of anys |  |

---

### Create a software version

Creates a new version for a software package. Requires staff permissions.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-software-versions/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_software_versions import marketplace_software_versions_create # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_software_versions_create.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_software_versions_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_software_versions/marketplace_software_versions_create.py)

=== "TypeScript"

    ```typescript
    import { marketplaceSoftwareVersionsCreate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceSoftwareVersionsCreate({
      auth: "Token YOUR_API_TOKEN"
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `version` | string |  |
    | `release_date` | string (date) |  |
    | `dependencies` | any | Package dependencies (format varies by catalog type) |
    | `metadata` | any | Version-specific metadata (toolchains, build info, modules, etc.) |
    | `package_name` | string |  |
    | `catalog_type` | string |  |
    | `target_count` | integer |  |
    | `module` | object (free-form) |  |
    | `required_modules` | array of anys |  |
    | `extensions` | array of anys |  |
    | `toolchain` | object (free-form) |  |
    | `toolchain_families_compatibility` | array of anys |  |

---

### Update a software version

Updates an existing software version. Requires staff permissions.


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/marketplace-software-versions/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_software_versions import marketplace_software_versions_update # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_software_versions_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_software_versions_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_software_versions/marketplace_software_versions_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceSoftwareVersionsUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceSoftwareVersionsUpdate({
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
    | `version` | string |  |
    | `release_date` | string (date) |  |
    | `dependencies` | any | Package dependencies (format varies by catalog type) |
    | `metadata` | any | Version-specific metadata (toolchains, build info, modules, etc.) |
    | `package_name` | string |  |
    | `catalog_type` | string |  |
    | `target_count` | integer |  |
    | `module` | object (free-form) |  |
    | `required_modules` | array of anys |  |
    | `extensions` | array of anys |  |
    | `toolchain` | object (free-form) |  |
    | `toolchain_families_compatibility` | array of anys |  |

---

### Partially update a software version

Partially updates an existing software version. Requires staff permissions.


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/marketplace-software-versions/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_software_versions import marketplace_software_versions_partial_update # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_software_versions_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_software_versions_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_software_versions/marketplace_software_versions_partial_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceSoftwareVersionsPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceSoftwareVersionsPartialUpdate({
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
    | `version` | string |  |
    | `release_date` | string (date) |  |
    | `dependencies` | any | Package dependencies (format varies by catalog type) |
    | `metadata` | any | Version-specific metadata (toolchains, build info, modules, etc.) |
    | `package_name` | string |  |
    | `catalog_type` | string |  |
    | `target_count` | integer |  |
    | `module` | object (free-form) |  |
    | `required_modules` | array of anys |  |
    | `extensions` | array of anys |  |
    | `toolchain` | object (free-form) |  |
    | `toolchain_families_compatibility` | array of anys |  |

---

### Delete a software version

Deletes a software version. Requires staff permissions.


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/marketplace-software-versions/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_software_versions import marketplace_software_versions_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_software_versions_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_software_versions_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_software_versions/marketplace_software_versions_destroy.py)

=== "TypeScript"

    ```typescript
    import { marketplaceSoftwareVersionsDestroy } from 'waldur-js-client';
    
    try {
      const response = await marketplaceSoftwareVersionsDestroy({
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
