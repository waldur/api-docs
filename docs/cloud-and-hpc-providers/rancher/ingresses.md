# Rancher Ingresses

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/rancher-ingresses/` | [List Rancher Ingresses](#list-rancher-ingresses) |
| <span class="http-badge http-get">GET</span> | `/api/rancher-ingresses/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/rancher-ingresses/` | [Create](#create) |
| <span class="http-badge http-post">POST</span> | `/api/rancher-ingresses/{uuid}/pull/` | [Synchronize resource state](#synchronize-resource-state) |
| <span class="http-badge http-post">POST</span> | `/api/rancher-ingresses/{uuid}/unlink/` | [Unlink resource](#unlink-resource) |
| <span class="http-badge http-put">PUT</span> | `/api/rancher-ingresses/{uuid}/` | [Update](#update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/rancher-ingresses/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-delete">DELETE</span> | `/api/rancher-ingresses/{uuid}/` | [Delete](#delete) |
| **Other Actions** | | |
| <span class="http-badge http-get">GET</span> | `/api/rancher-ingresses/{uuid}/yaml/` | [Yaml](#yaml) |
| <span class="http-badge http-post">POST</span> | `/api/rancher-ingresses/{uuid}/set_erred/` | [Mark resource as ERRED](#mark-resource-as-erred) |
| <span class="http-badge http-post">POST</span> | `/api/rancher-ingresses/{uuid}/set_ok/` | [Mark resource as OK](#mark-resource-as-ok) |
| <span class="http-badge http-put">PUT</span> | `/api/rancher-ingresses/{uuid}/yaml/` | [Yaml](#yaml) |

---
## Core CRUD


### List Rancher Ingresses


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/rancher-ingresses/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.core_states import CoreStates # (1)
    from waldur_api_client.models.rancher_ingress_field_enum import RancherIngressFieldEnum # (2)
    from waldur_api_client.api.rancher_ingresses import rancher_ingresses_list # (3)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = rancher_ingresses_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`CoreStates`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/core_states.py)
    2.  **Model Source:** [`RancherIngressFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/rancher_ingress_field_enum.py)
    3.  **API Source:** [`rancher_ingresses_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/rancher_ingresses/rancher_ingresses_list.py)

=== "TypeScript"

    ```typescript
    import { rancherIngressesList } from 'waldur-js-client';
    
    try {
      const response = await rancherIngressesList({
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
    | `backend_id` | string | Backend ID |
    | `can_manage` | boolean | Can manage |
    | `cluster_uuid` | string (uuid) |  |
    | `customer` | string (uuid) | Customer UUID |
    | `customer_abbreviation` | string | Customer abbreviation |
    | `customer_name` | string | Customer name |
    | `customer_native_name` | string | Customer native name |
    | `customer_uuid` | string (uuid) | Customer UUID |
    | `description` | string | Description |
    | `external_ip` | string | External IP |
    | `field` | array |  |
    | `name` | string | Name |
    | `name_exact` | string | Name (exact) |
    | `namespace_uuid` | string (uuid) |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `project` | string (uuid) | Project UUID |
    | `project_name` | string | Project name |
    | `project_uuid` | string (uuid) | Project UUID |
    | `rancher_project_uuid` | string (uuid) |  |
    | `service_settings_name` | string | Service settings name |
    | `service_settings_uuid` | string (uuid) | Service settings UUID |
    | `state` | array | State<br><br> |
    | `uuid` | string (uuid) | UUID |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `url` | string (uri) |
    | `uuid` | string (uuid) |
    | `name` | string |
    | `description` | string |
    | `service_name` | string |
    | `service_settings` | string (uri) |
    | `service_settings_uuid` | string (uuid) |
    | `service_settings_state` | string |
    | `service_settings_error_message` | string |
    | `project` | string (uri) |
    | `project_name` | string |
    | `project_uuid` | string (uuid) |
    | `customer` | string (uri) |
    | `customer_uuid` | string (uuid) |
    | `customer_name` | string |
    | `customer_native_name` | string |
    | `customer_abbreviation` | string |
    | `error_message` | string |
    | `error_traceback` | string |
    | `resource_type` | string |
    | `state` | any |
    | `created` | string (date-time) |
    | `modified` | string (date-time) |
    | `backend_id` | string |
    | `access_url` | string |
    | `runtime_state` | string |
    | `rancher_project` | string (uri) |
    | `rancher_project_name` | string |
    | `namespace` | string (uri) |
    | `namespace_name` | string |
    | `rules` | any |
    | `marketplace_offering_uuid` | string |
    | `marketplace_offering_name` | string |
    | `marketplace_offering_plugin_options` | object (free-form) |
    | `marketplace_category_uuid` | string |
    | `marketplace_category_name` | string |
    | `marketplace_resource_uuid` | string |
    | `marketplace_plan_uuid` | string |
    | `marketplace_resource_state` | string |
    | `is_usage_based` | boolean |
    | `is_limit_based` | boolean |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/rancher-ingresses/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.rancher_ingress_field_enum import RancherIngressFieldEnum # (1)
    from waldur_api_client.api.rancher_ingresses import rancher_ingresses_retrieve # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = rancher_ingresses_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`RancherIngressFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/rancher_ingress_field_enum.py)
    2.  **API Source:** [`rancher_ingresses_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/rancher_ingresses/rancher_ingresses_retrieve.py)

=== "TypeScript"

    ```typescript
    import { rancherIngressesRetrieve } from 'waldur-js-client';
    
    try {
      const response = await rancherIngressesRetrieve({
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
    
    | Field | Type |
    |---|---|
    | `url` | string (uri) |
    | `uuid` | string (uuid) |
    | `name` | string |
    | `description` | string |
    | `service_name` | string |
    | `service_settings` | string (uri) |
    | `service_settings_uuid` | string (uuid) |
    | `service_settings_state` | string |
    | `service_settings_error_message` | string |
    | `project` | string (uri) |
    | `project_name` | string |
    | `project_uuid` | string (uuid) |
    | `customer` | string (uri) |
    | `customer_uuid` | string (uuid) |
    | `customer_name` | string |
    | `customer_native_name` | string |
    | `customer_abbreviation` | string |
    | `error_message` | string |
    | `error_traceback` | string |
    | `resource_type` | string |
    | `state` | any |
    | `created` | string (date-time) |
    | `modified` | string (date-time) |
    | `backend_id` | string |
    | `access_url` | string |
    | `runtime_state` | string |
    | `rancher_project` | string (uri) |
    | `rancher_project_name` | string |
    | `namespace` | string (uri) |
    | `namespace_name` | string |
    | `rules` | any |
    | `marketplace_offering_uuid` | string |
    | `marketplace_offering_name` | string |
    | `marketplace_offering_plugin_options` | object (free-form) |
    | `marketplace_category_uuid` | string |
    | `marketplace_category_name` | string |
    | `marketplace_resource_uuid` | string |
    | `marketplace_plan_uuid` | string |
    | `marketplace_resource_state` | string |
    | `is_usage_based` | boolean |
    | `is_limit_based` | boolean |

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/rancher-ingresses/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-rancher-ingress" \
      service_settings="https://api.example.com/api/service-settings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      project="https://api.example.com/api/project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      rancher_project="https://api.example.com/api/rancher-project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.rancher_ingress_request import RancherIngressRequest # (1)
    from waldur_api_client.api.rancher_ingresses import rancher_ingresses_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = RancherIngressRequest(
        name="my-awesome-rancher-ingress",
        service_settings="https://api.example.com/api/service-settings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        project="https://api.example.com/api/project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        rancher_project="https://api.example.com/api/rancher-project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    )
    response = rancher_ingresses_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`RancherIngressRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/rancher_ingress_request.py)
    2.  **API Source:** [`rancher_ingresses_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/rancher_ingresses/rancher_ingresses_create.py)

=== "TypeScript"

    ```typescript
    import { rancherIngressesCreate } from 'waldur-js-client';
    
    try {
      const response = await rancherIngressesCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "name": "my-awesome-rancher-ingress",
        "service_settings": "https://api.example.com/api/service-settings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "project": "https://api.example.com/api/project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "rancher_project": "https://api.example.com/api/rancher-project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
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
    | `description` | string |  |
    | `service_settings` | string (uri) | ✓ |
    | `project` | string (uri) | ✓ |
    | `error_message` | string |  |
    | `error_traceback` | string |  |
    | `backend_id` | string |  |
    | `runtime_state` | string |  |
    | `rancher_project` | string (uri) | ✓ |
    | `namespace` | string (uri) |  |
    | `rules` | any |  |


=== "Responses"

    **`201`** - 
    
    | Field | Type |
    |---|---|
    | `url` | string (uri) |
    | `uuid` | string (uuid) |
    | `name` | string |
    | `description` | string |
    | `service_name` | string |
    | `service_settings` | string (uri) |
    | `service_settings_uuid` | string (uuid) |
    | `service_settings_state` | string |
    | `service_settings_error_message` | string |
    | `project` | string (uri) |
    | `project_name` | string |
    | `project_uuid` | string (uuid) |
    | `customer` | string (uri) |
    | `customer_uuid` | string (uuid) |
    | `customer_name` | string |
    | `customer_native_name` | string |
    | `customer_abbreviation` | string |
    | `error_message` | string |
    | `error_traceback` | string |
    | `resource_type` | string |
    | `state` | any |
    | `created` | string (date-time) |
    | `modified` | string (date-time) |
    | `backend_id` | string |
    | `access_url` | string |
    | `runtime_state` | string |
    | `rancher_project` | string (uri) |
    | `rancher_project_name` | string |
    | `namespace` | string (uri) |
    | `namespace_name` | string |
    | `rules` | any |
    | `marketplace_offering_uuid` | string |
    | `marketplace_offering_name` | string |
    | `marketplace_offering_plugin_options` | object (free-form) |
    | `marketplace_category_uuid` | string |
    | `marketplace_category_name` | string |
    | `marketplace_resource_uuid` | string |
    | `marketplace_plan_uuid` | string |
    | `marketplace_resource_state` | string |
    | `is_usage_based` | boolean |
    | `is_limit_based` | boolean |

---

### Synchronize resource state

Schedule an asynchronous pull operation to synchronize resource state from the backend. Returns 202 if the pull was scheduled successfully, or 409 if the pull operation is not implemented for this resource type.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/rancher-ingresses/a1b2c3d4-e5f6-7890-abcd-ef1234567890/pull/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.rancher_ingresses import rancher_ingresses_pull # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = rancher_ingresses_pull.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`rancher_ingresses_pull`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/rancher_ingresses/rancher_ingresses_pull.py)

=== "TypeScript"

    ```typescript
    import { rancherIngressesPull } from 'waldur-js-client';
    
    try {
      const response = await rancherIngressesPull({
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

    **`202`** - 
    
    | Field | Type |
    |---|---|
    | `detail` | string |
    
    ---
    
    **`409`** - 
    
    | Field | Type |
    |---|---|
    | `detail` | string |

---

### Unlink resource

Delete resource from the database without scheduling operations on backend
        and without checking current state of the resource. It is intended to be used
        for removing resource stuck in transitioning state.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/rancher-ingresses/a1b2c3d4-e5f6-7890-abcd-ef1234567890/unlink/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.rancher_ingresses import rancher_ingresses_unlink # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = rancher_ingresses_unlink.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`rancher_ingresses_unlink`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/rancher_ingresses/rancher_ingresses_unlink.py)

=== "TypeScript"

    ```typescript
    import { rancherIngressesUnlink } from 'waldur-js-client';
    
    try {
      const response = await rancherIngressesUnlink({
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

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/rancher-ingresses/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-rancher-ingress" \
      service_settings="https://api.example.com/api/service-settings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      project="https://api.example.com/api/project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      rancher_project="https://api.example.com/api/rancher-project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.rancher_ingress_request import RancherIngressRequest # (1)
    from waldur_api_client.api.rancher_ingresses import rancher_ingresses_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = RancherIngressRequest(
        name="my-awesome-rancher-ingress",
        service_settings="https://api.example.com/api/service-settings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        project="https://api.example.com/api/project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        rancher_project="https://api.example.com/api/rancher-project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    )
    response = rancher_ingresses_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`RancherIngressRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/rancher_ingress_request.py)
    2.  **API Source:** [`rancher_ingresses_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/rancher_ingresses/rancher_ingresses_update.py)

=== "TypeScript"

    ```typescript
    import { rancherIngressesUpdate } from 'waldur-js-client';
    
    try {
      const response = await rancherIngressesUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "name": "my-awesome-rancher-ingress",
        "service_settings": "https://api.example.com/api/service-settings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "project": "https://api.example.com/api/project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "rancher_project": "https://api.example.com/api/rancher-project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
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

    | Field | Type | Required |
    |---|---|---|
    | `name` | string | ✓ |
    | `description` | string |  |
    | `service_settings` | string (uri) | ✓ |
    | `project` | string (uri) | ✓ |
    | `error_message` | string |  |
    | `error_traceback` | string |  |
    | `backend_id` | string |  |
    | `runtime_state` | string |  |
    | `rancher_project` | string (uri) | ✓ |
    | `namespace` | string (uri) |  |
    | `rules` | any |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `url` | string (uri) |
    | `uuid` | string (uuid) |
    | `name` | string |
    | `description` | string |
    | `service_name` | string |
    | `service_settings` | string (uri) |
    | `service_settings_uuid` | string (uuid) |
    | `service_settings_state` | string |
    | `service_settings_error_message` | string |
    | `project` | string (uri) |
    | `project_name` | string |
    | `project_uuid` | string (uuid) |
    | `customer` | string (uri) |
    | `customer_uuid` | string (uuid) |
    | `customer_name` | string |
    | `customer_native_name` | string |
    | `customer_abbreviation` | string |
    | `error_message` | string |
    | `error_traceback` | string |
    | `resource_type` | string |
    | `state` | any |
    | `created` | string (date-time) |
    | `modified` | string (date-time) |
    | `backend_id` | string |
    | `access_url` | string |
    | `runtime_state` | string |
    | `rancher_project` | string (uri) |
    | `rancher_project_name` | string |
    | `namespace` | string (uri) |
    | `namespace_name` | string |
    | `rules` | any |
    | `marketplace_offering_uuid` | string |
    | `marketplace_offering_name` | string |
    | `marketplace_offering_plugin_options` | object (free-form) |
    | `marketplace_category_uuid` | string |
    | `marketplace_category_name` | string |
    | `marketplace_resource_uuid` | string |
    | `marketplace_plan_uuid` | string |
    | `marketplace_resource_state` | string |
    | `is_usage_based` | boolean |
    | `is_limit_based` | boolean |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/rancher-ingresses/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_rancher_ingress_request import PatchedRancherIngressRequest # (1)
    from waldur_api_client.api.rancher_ingresses import rancher_ingresses_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedRancherIngressRequest()
    response = rancher_ingresses_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedRancherIngressRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_rancher_ingress_request.py)
    2.  **API Source:** [`rancher_ingresses_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/rancher_ingresses/rancher_ingresses_partial_update.py)

=== "TypeScript"

    ```typescript
    import { rancherIngressesPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await rancherIngressesPartialUpdate({
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

    | Field | Type | Required |
    |---|---|---|
    | `name` | string |  |
    | `description` | string |  |
    | `service_settings` | string (uri) |  |
    | `project` | string (uri) |  |
    | `error_message` | string |  |
    | `error_traceback` | string |  |
    | `backend_id` | string |  |
    | `runtime_state` | string |  |
    | `rancher_project` | string (uri) |  |
    | `namespace` | string (uri) |  |
    | `rules` | any |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `url` | string (uri) |
    | `uuid` | string (uuid) |
    | `name` | string |
    | `description` | string |
    | `service_name` | string |
    | `service_settings` | string (uri) |
    | `service_settings_uuid` | string (uuid) |
    | `service_settings_state` | string |
    | `service_settings_error_message` | string |
    | `project` | string (uri) |
    | `project_name` | string |
    | `project_uuid` | string (uuid) |
    | `customer` | string (uri) |
    | `customer_uuid` | string (uuid) |
    | `customer_name` | string |
    | `customer_native_name` | string |
    | `customer_abbreviation` | string |
    | `error_message` | string |
    | `error_traceback` | string |
    | `resource_type` | string |
    | `state` | any |
    | `created` | string (date-time) |
    | `modified` | string (date-time) |
    | `backend_id` | string |
    | `access_url` | string |
    | `runtime_state` | string |
    | `rancher_project` | string (uri) |
    | `rancher_project_name` | string |
    | `namespace` | string (uri) |
    | `namespace_name` | string |
    | `rules` | any |
    | `marketplace_offering_uuid` | string |
    | `marketplace_offering_name` | string |
    | `marketplace_offering_plugin_options` | object (free-form) |
    | `marketplace_category_uuid` | string |
    | `marketplace_category_name` | string |
    | `marketplace_resource_uuid` | string |
    | `marketplace_plan_uuid` | string |
    | `marketplace_resource_state` | string |
    | `is_usage_based` | boolean |
    | `is_limit_based` | boolean |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/rancher-ingresses/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.rancher_ingresses import rancher_ingresses_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = rancher_ingresses_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`rancher_ingresses_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/rancher_ingresses/rancher_ingresses_destroy.py)

=== "TypeScript"

    ```typescript
    import { rancherIngressesDestroy } from 'waldur-js-client';
    
    try {
      const response = await rancherIngressesDestroy({
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


### Yaml


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/rancher-ingresses/a1b2c3d4-e5f6-7890-abcd-ef1234567890/yaml/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.rancher_ingress_field_enum import RancherIngressFieldEnum # (1)
    from waldur_api_client.api.rancher_ingresses import rancher_ingresses_yaml_retrieve # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = rancher_ingresses_yaml_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`RancherIngressFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/rancher_ingress_field_enum.py)
    2.  **API Source:** [`rancher_ingresses_yaml_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/rancher_ingresses/rancher_ingresses_yaml_retrieve.py)

=== "TypeScript"

    ```typescript
    import { rancherIngressesYamlRetrieve } from 'waldur-js-client';
    
    try {
      const response = await rancherIngressesYamlRetrieve({
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
    
    | Field | Type |
    |---|---|
    | `url` | string (uri) |
    | `uuid` | string (uuid) |
    | `name` | string |
    | `description` | string |
    | `service_name` | string |
    | `service_settings` | string (uri) |
    | `service_settings_uuid` | string (uuid) |
    | `service_settings_state` | string |
    | `service_settings_error_message` | string |
    | `project` | string (uri) |
    | `project_name` | string |
    | `project_uuid` | string (uuid) |
    | `customer` | string (uri) |
    | `customer_uuid` | string (uuid) |
    | `customer_name` | string |
    | `customer_native_name` | string |
    | `customer_abbreviation` | string |
    | `error_message` | string |
    | `error_traceback` | string |
    | `resource_type` | string |
    | `state` | any |
    | `created` | string (date-time) |
    | `modified` | string (date-time) |
    | `backend_id` | string |
    | `access_url` | string |
    | `runtime_state` | string |
    | `rancher_project` | string (uri) |
    | `rancher_project_name` | string |
    | `namespace` | string (uri) |
    | `namespace_name` | string |
    | `rules` | any |
    | `marketplace_offering_uuid` | string |
    | `marketplace_offering_name` | string |
    | `marketplace_offering_plugin_options` | object (free-form) |
    | `marketplace_category_uuid` | string |
    | `marketplace_category_name` | string |
    | `marketplace_resource_uuid` | string |
    | `marketplace_plan_uuid` | string |
    | `marketplace_resource_state` | string |
    | `is_usage_based` | boolean |
    | `is_limit_based` | boolean |

---

### Mark resource as ERRED

Manually transition the resource to ERRED state. This is useful for resources stuck in transitional states (CREATING, UPDATING, DELETING) that cannot be synced via pull. Staff-only operation.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/rancher-ingresses/a1b2c3d4-e5f6-7890-abcd-ef1234567890/set_erred/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.set_erred_request import SetErredRequest # (1)
    from waldur_api_client.api.rancher_ingresses import rancher_ingresses_set_erred # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = SetErredRequest()
    response = rancher_ingresses_set_erred.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`SetErredRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/set_erred_request.py)
    2.  **API Source:** [`rancher_ingresses_set_erred`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/rancher_ingresses/rancher_ingresses_set_erred.py)

=== "TypeScript"

    ```typescript
    import { rancherIngressesSetErred } from 'waldur-js-client';
    
    try {
      const response = await rancherIngressesSetErred({
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

    | Field | Type | Required |
    |---|---|---|
    | `error_message` | string |  |
    | `error_traceback` | string |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `detail` | string |

---

### Mark resource as OK

Manually transition the resource to OK state and clear error fields. Staff-only operation.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/rancher-ingresses/a1b2c3d4-e5f6-7890-abcd-ef1234567890/set_ok/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.rancher_ingresses import rancher_ingresses_set_ok # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = rancher_ingresses_set_ok.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`rancher_ingresses_set_ok`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/rancher_ingresses/rancher_ingresses_set_ok.py)

=== "TypeScript"

    ```typescript
    import { rancherIngressesSetOk } from 'waldur-js-client';
    
    try {
      const response = await rancherIngressesSetOk({
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
    | `detail` | string |

---

### Yaml


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/rancher-ingresses/a1b2c3d4-e5f6-7890-abcd-ef1234567890/yaml/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-rancher-ingress" \
      service_settings="https://api.example.com/api/service-settings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      project="https://api.example.com/api/project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      rancher_project="https://api.example.com/api/rancher-project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.rancher_ingress_request import RancherIngressRequest # (1)
    from waldur_api_client.api.rancher_ingresses import rancher_ingresses_yaml_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = RancherIngressRequest(
        name="my-awesome-rancher-ingress",
        service_settings="https://api.example.com/api/service-settings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        project="https://api.example.com/api/project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        rancher_project="https://api.example.com/api/rancher-project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    )
    response = rancher_ingresses_yaml_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`RancherIngressRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/rancher_ingress_request.py)
    2.  **API Source:** [`rancher_ingresses_yaml_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/rancher_ingresses/rancher_ingresses_yaml_update.py)

=== "TypeScript"

    ```typescript
    import { rancherIngressesYamlUpdate } from 'waldur-js-client';
    
    try {
      const response = await rancherIngressesYamlUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "name": "my-awesome-rancher-ingress",
        "service_settings": "https://api.example.com/api/service-settings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "project": "https://api.example.com/api/project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "rancher_project": "https://api.example.com/api/rancher-project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
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

    | Field | Type | Required |
    |---|---|---|
    | `name` | string | ✓ |
    | `description` | string |  |
    | `service_settings` | string (uri) | ✓ |
    | `project` | string (uri) | ✓ |
    | `error_message` | string |  |
    | `error_traceback` | string |  |
    | `backend_id` | string |  |
    | `runtime_state` | string |  |
    | `rancher_project` | string (uri) | ✓ |
    | `namespace` | string (uri) |  |
    | `rules` | any |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `url` | string (uri) |
    | `uuid` | string (uuid) |
    | `name` | string |
    | `description` | string |
    | `service_name` | string |
    | `service_settings` | string (uri) |
    | `service_settings_uuid` | string (uuid) |
    | `service_settings_state` | string |
    | `service_settings_error_message` | string |
    | `project` | string (uri) |
    | `project_name` | string |
    | `project_uuid` | string (uuid) |
    | `customer` | string (uri) |
    | `customer_uuid` | string (uuid) |
    | `customer_name` | string |
    | `customer_native_name` | string |
    | `customer_abbreviation` | string |
    | `error_message` | string |
    | `error_traceback` | string |
    | `resource_type` | string |
    | `state` | any |
    | `created` | string (date-time) |
    | `modified` | string (date-time) |
    | `backend_id` | string |
    | `access_url` | string |
    | `runtime_state` | string |
    | `rancher_project` | string (uri) |
    | `rancher_project_name` | string |
    | `namespace` | string (uri) |
    | `namespace_name` | string |
    | `rules` | any |
    | `marketplace_offering_uuid` | string |
    | `marketplace_offering_name` | string |
    | `marketplace_offering_plugin_options` | object (free-form) |
    | `marketplace_category_uuid` | string |
    | `marketplace_category_name` | string |
    | `marketplace_resource_uuid` | string |
    | `marketplace_plan_uuid` | string |
    | `marketplace_resource_state` | string |
    | `is_usage_based` | boolean |
    | `is_limit_based` | boolean |

---
