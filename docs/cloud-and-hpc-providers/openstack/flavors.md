# Openstack Flavors

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/openstack-flavors/` | [List flavors](#list-flavors) |
| <span class="http-badge http-get">GET</span> | `/api/openstack-flavors/{uuid}/` | [Get flavor details](#get-flavor-details) |
| **Other Actions** | | |
| <span class="http-badge http-get">GET</span> | `/api/openstack-flavors/usage_stats/` | [Get flavor usage statistics](#get-flavor-usage-statistics) |

---
## Core CRUD


### List flavors

Get a list of available VM instance flavors.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openstack-flavors/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.open_stack_flavor_field_enum import OpenStackFlavorFieldEnum # (1)
    from waldur_api_client.models.open_stack_flavor_o_enum import OpenStackFlavorOEnum # (2)
    from waldur_api_client.api.openstack_flavors import openstack_flavors_list # (3)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openstack_flavors_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`OpenStackFlavorFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/open_stack_flavor_field_enum.py)
    2.  **Model Source:** [`OpenStackFlavorOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/open_stack_flavor_o_enum.py)
    3.  **API Source:** [`openstack_flavors_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_flavors/openstack_flavors_list.py)

=== "TypeScript"

    ```typescript
    import { openstackFlavorsList } from 'waldur-js-client';
    
    try {
      const response = await openstackFlavorsList({
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
    | `cores` | integer |  |
    | `cores__gte` | integer |  |
    | `cores__lte` | integer |  |
    | `disk` | integer |  |
    | `disk__gte` | integer |  |
    | `disk__lte` | integer |  |
    | `field` | array |  |
    | `name` | string | Name |
    | `name_exact` | string | Name (exact) |
    | `name_iregex` | string | Name (regex) |
    | `o` | array | Ordering<br><br> |
    | `offering_uuid` | string (uuid) | Offering UUID |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `ram` | integer |  |
    | `ram__gte` | integer |  |
    | `ram__lte` | integer |  |
    | `settings` | string (uri) | Settings URL |
    | `settings_uuid` | string (uuid) | Settings UUID |
    | `tenant` | string (uri) | Tenant URL |
    | `tenant_uuid` | string (uuid) | Tenant UUID |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `settings` | string (uri) |  |
    | `cores` | integer | Number of cores in a VM |
    | `ram` | integer | Memory size in MiB |
    | `disk` | integer | Root disk size in MiB |
    | `backend_id` | string |  |
    | `display_name` | string |  |

---

### Get flavor details

Retrieve details of a specific VM instance flavor.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openstack-flavors/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.open_stack_flavor_field_enum import OpenStackFlavorFieldEnum # (1)
    from waldur_api_client.api.openstack_flavors import openstack_flavors_retrieve # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openstack_flavors_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`OpenStackFlavorFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/open_stack_flavor_field_enum.py)
    2.  **API Source:** [`openstack_flavors_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_flavors/openstack_flavors_retrieve.py)

=== "TypeScript"

    ```typescript
    import { openstackFlavorsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await openstackFlavorsRetrieve({
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


=== "Query Parameters"

    | Name | Type |
    |---|---|
    | `field` | array |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `settings` | string (uri) |  |
    | `cores` | integer | Number of cores in a VM |
    | `ram` | integer | Memory size in MiB |
    | `disk` | integer | Root disk size in MiB |
    | `backend_id` | string |  |
    | `display_name` | string |  |

---

## Other Actions


### Get flavor usage statistics

Retrieve usage statistics for VM instance flavors, showing running and created instance counts for each flavor.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openstack-flavors/usage_stats/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.open_stack_flavor_field_enum import OpenStackFlavorFieldEnum # (1)
    from waldur_api_client.api.openstack_flavors import openstack_flavors_usage_stats_retrieve # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openstack_flavors_usage_stats_retrieve.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`OpenStackFlavorFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/open_stack_flavor_field_enum.py)
    2.  **API Source:** [`openstack_flavors_usage_stats_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_flavors/openstack_flavors_usage_stats_retrieve.py)

=== "TypeScript"

    ```typescript
    import { openstackFlavorsUsageStatsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await openstackFlavorsUsageStatsRetrieve({
      auth: "Token YOUR_API_TOKEN"
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Query Parameters"

    | Name | Type |
    |---|---|
    | `field` | array |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `settings` | string (uri) |  |
    | `cores` | integer | Number of cores in a VM |
    | `ram` | integer | Memory size in MiB |
    | `disk` | integer | Root disk size in MiB |
    | `backend_id` | string |  |
    | `display_name` | string |  |

---
