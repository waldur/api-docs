# Vmware Ports

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/vmware-ports/` | [List Vmware Ports](#list-vmware-ports) |
| <span class="http-badge http-get">GET</span> | `/api/vmware-ports/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/vmware-ports/{uuid}/pull/` | [Synchronize resource state](#synchronize-resource-state) |
| <span class="http-badge http-post">POST</span> | `/api/vmware-ports/{uuid}/unlink/` | [Unlink resource](#unlink-resource) |
| <span class="http-badge http-delete">DELETE</span> | `/api/vmware-ports/{uuid}/` | [Delete](#delete) |
| **Other Actions** | | |
| <span class="http-badge http-post">POST</span> | `/api/vmware-ports/{uuid}/set_erred/` | [Mark resource as ERRED](#mark-resource-as-erred) |
| <span class="http-badge http-post">POST</span> | `/api/vmware-ports/{uuid}/set_ok/` | [Mark resource as OK](#mark-resource-as-ok) |

---
## Core CRUD


### List Vmware Ports


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/vmware-ports/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.core_states import CoreStates # (1)
    from waldur_api_client.models.vmware_port_field_enum import VmwarePortFieldEnum # (2)
    from waldur_api_client.api.vmware_ports import vmware_ports_list # (3)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = vmware_ports_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`CoreStates`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/core_states.py)
    2.  **Model Source:** [`VmwarePortFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/vmware_port_field_enum.py)
    3.  **API Source:** [`vmware_ports_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/vmware_ports/vmware_ports_list.py)

=== "TypeScript"

    ```typescript
    import { vmwarePortsList } from 'waldur-js-client';
    
    try {
      const response = await vmwarePortsList({
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
    | `network` | string (uri) |  |
    | `network_uuid` | string (uuid) |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `project` | string (uuid) | Project UUID |
    | `project_name` | string | Project name |
    | `project_uuid` | string (uuid) | Project UUID |
    | `service_settings_name` | string | Service settings name |
    | `service_settings_uuid` | string (uuid) | Service settings UUID |
    | `state` | array | State<br><br> |
    | `uuid` | string (uuid) | UUID |
    | `vm` | string (uri) |  |
    | `vm_uuid` | string (uuid) |  |


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
    | `mac_address` | string |
    | `vm` | string (uri) |
    | `vm_uuid` | string (uuid) |
    | `vm_name` | string |
    | `network` | string (uri) |
    | `network_name` | string |
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
      https://api.example.com/api/vmware-ports/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.vmware_port_field_enum import VmwarePortFieldEnum # (1)
    from waldur_api_client.api.vmware_ports import vmware_ports_retrieve # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = vmware_ports_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`VmwarePortFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/vmware_port_field_enum.py)
    2.  **API Source:** [`vmware_ports_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/vmware_ports/vmware_ports_retrieve.py)

=== "TypeScript"

    ```typescript
    import { vmwarePortsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await vmwarePortsRetrieve({
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
    | `mac_address` | string |
    | `vm` | string (uri) |
    | `vm_uuid` | string (uuid) |
    | `vm_name` | string |
    | `network` | string (uri) |
    | `network_name` | string |
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
      https://api.example.com/api/vmware-ports/a1b2c3d4-e5f6-7890-abcd-ef1234567890/pull/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.vmware_ports import vmware_ports_pull # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = vmware_ports_pull.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`vmware_ports_pull`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/vmware_ports/vmware_ports_pull.py)

=== "TypeScript"

    ```typescript
    import { vmwarePortsPull } from 'waldur-js-client';
    
    try {
      const response = await vmwarePortsPull({
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
      https://api.example.com/api/vmware-ports/a1b2c3d4-e5f6-7890-abcd-ef1234567890/unlink/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.vmware_ports import vmware_ports_unlink # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = vmware_ports_unlink.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`vmware_ports_unlink`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/vmware_ports/vmware_ports_unlink.py)

=== "TypeScript"

    ```typescript
    import { vmwarePortsUnlink } from 'waldur-js-client';
    
    try {
      const response = await vmwarePortsUnlink({
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
      https://api.example.com/api/vmware-ports/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.vmware_ports import vmware_ports_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = vmware_ports_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`vmware_ports_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/vmware_ports/vmware_ports_destroy.py)

=== "TypeScript"

    ```typescript
    import { vmwarePortsDestroy } from 'waldur-js-client';
    
    try {
      const response = await vmwarePortsDestroy({
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


### Mark resource as ERRED

Manually transition the resource to ERRED state. This is useful for resources stuck in transitional states (CREATING, UPDATING, DELETING) that cannot be synced via pull. Staff-only operation.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/vmware-ports/a1b2c3d4-e5f6-7890-abcd-ef1234567890/set_erred/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.set_erred_request import SetErredRequest # (1)
    from waldur_api_client.api.vmware_ports import vmware_ports_set_erred # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = SetErredRequest()
    response = vmware_ports_set_erred.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`SetErredRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/set_erred_request.py)
    2.  **API Source:** [`vmware_ports_set_erred`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/vmware_ports/vmware_ports_set_erred.py)

=== "TypeScript"

    ```typescript
    import { vmwarePortsSetErred } from 'waldur-js-client';
    
    try {
      const response = await vmwarePortsSetErred({
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
      https://api.example.com/api/vmware-ports/a1b2c3d4-e5f6-7890-abcd-ef1234567890/set_ok/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.vmware_ports import vmware_ports_set_ok # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = vmware_ports_set_ok.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`vmware_ports_set_ok`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/vmware_ports/vmware_ports_set_ok.py)

=== "TypeScript"

    ```typescript
    import { vmwarePortsSetOk } from 'waldur-js-client';
    
    try {
      const response = await vmwarePortsSetOk({
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
