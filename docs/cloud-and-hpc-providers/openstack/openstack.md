# Openstack

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/openstack/discovery/` | [List Openstack Discovery](#list-openstack-discovery) |
| <span class="http-badge http-get">GET</span> | `/api/openstack/discovery/{id}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-get">GET</span> | `/api/openstack-health-monitors/` | [List health monitors](#list-health-monitors) |
| <span class="http-badge http-get">GET</span> | `/api/openstack-health-monitors/{uuid}/` | [Get health monitor details](#get-health-monitor-details) |
| <span class="http-badge http-get">GET</span> | `/api/openstack-listeners/` | [List listeners](#list-listeners) |
| <span class="http-badge http-get">GET</span> | `/api/openstack-listeners/{uuid}/` | [Get listener details](#get-listener-details) |
| <span class="http-badge http-get">GET</span> | `/api/openstack-loadbalancers/` | [List load balancers](#list-load-balancers) |
| <span class="http-badge http-get">GET</span> | `/api/openstack-loadbalancers/{uuid}/` | [Get load balancer details](#get-load-balancer-details) |
| <span class="http-badge http-get">GET</span> | `/api/openstack-pool-members/` | [List pool members](#list-pool-members) |
| <span class="http-badge http-get">GET</span> | `/api/openstack-pool-members/{uuid}/` | [Get pool member details](#get-pool-member-details) |
| <span class="http-badge http-get">GET</span> | `/api/openstack-pools/` | [List pools](#list-pools) |
| <span class="http-badge http-get">GET</span> | `/api/openstack-pools/{uuid}/` | [Get pool details](#get-pool-details) |
| <span class="http-badge http-post">POST</span> | `/api/openstack/discovery/` | [Create](#create) |
| <span class="http-badge http-post">POST</span> | `/api/openstack/discovery/discover_external_networks/` | [Discover available external networks](#discover-available-external-networks) |
| <span class="http-badge http-post">POST</span> | `/api/openstack/discovery/discover_flavors/` | [Discover available flavors](#discover-available-flavors) |
| <span class="http-badge http-post">POST</span> | `/api/openstack/discovery/discover_instance_availability_zones/` | [Discover available Nova instance availability zones](#discover-available-nova-instance-availability-zones) |
| <span class="http-badge http-post">POST</span> | `/api/openstack/discovery/discover_volume_availability_zones/` | [Discover available Cinder volume availability zones](#discover-available-cinder-volume-availability-zones) |
| <span class="http-badge http-post">POST</span> | `/api/openstack/discovery/discover_volume_types/` | [Discover available volume types](#discover-available-volume-types) |
| <span class="http-badge http-post">POST</span> | `/api/openstack/discovery/preview_service_attributes/` | [Build service_attributes and plugin_options from selected values](#build-service_attributes-and-plugin_options-from-selected-values) |
| <span class="http-badge http-post">POST</span> | `/api/openstack/discovery/validate_credentials/` | [Validate OpenStack credentials without saving them](#validate-openstack-credentials-without-saving-them) |
| <span class="http-badge http-post">POST</span> | `/api/openstack-health-monitors/` | [Create health monitor](#create-health-monitor) |
| <span class="http-badge http-post">POST</span> | `/api/openstack-health-monitors/{uuid}/pull/` | [Pull health monitor](#pull-health-monitor) |
| <span class="http-badge http-post">POST</span> | `/api/openstack-listeners/` | [Create listener](#create-listener) |
| <span class="http-badge http-post">POST</span> | `/api/openstack-listeners/{uuid}/pull/` | [Pull listener](#pull-listener) |
| <span class="http-badge http-post">POST</span> | `/api/openstack-loadbalancers/{uuid}/attach_floating_ip/` | [Attach floating IP to VIP](#attach-floating-ip-to-vip) |
| <span class="http-badge http-post">POST</span> | `/api/openstack-loadbalancers/` | [Create load balancer](#create-load-balancer) |
| <span class="http-badge http-post">POST</span> | `/api/openstack-loadbalancers/{uuid}/detach_floating_ip/` | [Detach floating IP from VIP](#detach-floating-ip-from-vip) |
| <span class="http-badge http-post">POST</span> | `/api/openstack-loadbalancers/{uuid}/pull/` | [Pull load balancer](#pull-load-balancer) |
| <span class="http-badge http-post">POST</span> | `/api/openstack-loadbalancers/{uuid}/unlink/` | [Unlink load balancer](#unlink-load-balancer) |
| <span class="http-badge http-post">POST</span> | `/api/openstack-pool-members/` | [Create pool member](#create-pool-member) |
| <span class="http-badge http-post">POST</span> | `/api/openstack-pool-members/{uuid}/pull/` | [Pull pool member](#pull-pool-member) |
| <span class="http-badge http-post">POST</span> | `/api/openstack-pools/` | [Create pool](#create-pool) |
| <span class="http-badge http-post">POST</span> | `/api/openstack-pools/{uuid}/pull/` | [Pull pool](#pull-pool) |
| <span class="http-badge http-put">PUT</span> | `/api/openstack/discovery/{id}/` | [Update](#update) |
| <span class="http-badge http-put">PUT</span> | `/api/openstack-health-monitors/{uuid}/` | [Update health monitor](#update-health-monitor) |
| <span class="http-badge http-put">PUT</span> | `/api/openstack-listeners/{uuid}/` | [Update listener](#update-listener) |
| <span class="http-badge http-put">PUT</span> | `/api/openstack-loadbalancers/{uuid}/` | [Update load balancer](#update-load-balancer) |
| <span class="http-badge http-put">PUT</span> | `/api/openstack-pool-members/{uuid}/` | [Update pool member](#update-pool-member) |
| <span class="http-badge http-put">PUT</span> | `/api/openstack-pools/{uuid}/` | [Update pool](#update-pool) |
| <span class="http-badge http-patch">PATCH</span> | `/api/openstack/discovery/{id}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/openstack-health-monitors/{uuid}/` | [Partially update health monitor](#partially-update-health-monitor) |
| <span class="http-badge http-patch">PATCH</span> | `/api/openstack-listeners/{uuid}/` | [Partially update listener](#partially-update-listener) |
| <span class="http-badge http-patch">PATCH</span> | `/api/openstack-loadbalancers/{uuid}/` | [Partially update load balancer](#partially-update-load-balancer) |
| <span class="http-badge http-patch">PATCH</span> | `/api/openstack-pool-members/{uuid}/` | [Partially update pool member](#partially-update-pool-member) |
| <span class="http-badge http-patch">PATCH</span> | `/api/openstack-pools/{uuid}/` | [Partially update pool](#partially-update-pool) |
| <span class="http-badge http-delete">DELETE</span> | `/api/openstack/discovery/{id}/` | [Delete](#delete) |
| <span class="http-badge http-delete">DELETE</span> | `/api/openstack-health-monitors/{uuid}/` | [Delete health monitor](#delete-health-monitor) |
| <span class="http-badge http-delete">DELETE</span> | `/api/openstack-listeners/{uuid}/` | [Delete listener](#delete-listener) |
| <span class="http-badge http-delete">DELETE</span> | `/api/openstack-loadbalancers/{uuid}/` | [Delete load balancer](#delete-load-balancer) |
| <span class="http-badge http-delete">DELETE</span> | `/api/openstack-pool-members/{uuid}/` | [Delete pool member](#delete-pool-member) |
| <span class="http-badge http-delete">DELETE</span> | `/api/openstack-pools/{uuid}/` | [Delete pool](#delete-pool) |

---

### List Openstack Discovery


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openstack/discovery/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openstack import openstack_discovery_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openstack_discovery_list.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openstack_discovery_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack/openstack_discovery_list.py)

=== "TypeScript"

    ```typescript
    import { openstackDiscoveryList } from 'waldur-js-client';
    
    try {
      const response = await openstackDiscoveryList({
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
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |


=== "Responses"

    **`200`** - No response body
    

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openstack/discovery/123/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openstack import openstack_discovery_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openstack_discovery_retrieve.sync(
        id=123,
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openstack_discovery_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack/openstack_discovery_retrieve.py)

=== "TypeScript"

    ```typescript
    import { openstackDiscoveryRetrieve } from 'waldur-js-client';
    
    try {
      const response = await openstackDiscoveryRetrieve({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "id": 123
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required | Description |
    |---|---|---|---|
    | `id` | integer | ✓ | A unique integer value identifying this Service provider. |


=== "Responses"

    **`200`** - No response body
    

---

### List health monitors

Get a list of pool health monitors.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openstack-health-monitors/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.core_states import CoreStates # (1)
    from waldur_api_client.models.open_stack_health_monitor_field_enum import OpenStackHealthMonitorFieldEnum # (2)
    from waldur_api_client.api.openstack_health_monitors import openstack_health_monitors_list # (3)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openstack_health_monitors_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`CoreStates`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/core_states.py)
    2.  **Model Source:** [`OpenStackHealthMonitorFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/open_stack_health_monitor_field_enum.py)
    3.  **API Source:** [`openstack_health_monitors_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_health_monitors/openstack_health_monitors_list.py)

=== "TypeScript"

    ```typescript
    import { openstackHealthMonitorsList } from 'waldur-js-client';
    
    try {
      const response = await openstackHealthMonitorsList({
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
    | `field` | array |  |
    | `load_balancer_uuid` | string (uuid) | Load balancer UUID |
    | `name` | string | Name |
    | `name_exact` | string | Name (exact) |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `pool` | string (uri) | Pool URL |
    | `pool_uuid` | string (uuid) | Pool UUID |
    | `state` | array | State<br><br> |
    | `tenant_uuid` | string (uuid) | Tenant UUID |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `description` | string |  |
    | `service_name` | string |  |
    | `service_settings` | string (uri) |  |
    | `service_settings_uuid` | string (uuid) |  |
    | `service_settings_state` | string |  |
    | `service_settings_error_message` | string |  |
    | `project` | string (uri) |  |
    | `project_name` | string |  |
    | `project_uuid` | string (uuid) |  |
    | `customer` | string (uri) |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `customer_native_name` | string |  |
    | `customer_abbreviation` | string |  |
    | `error_message` | string |  |
    | `error_traceback` | string |  |
    | `resource_type` | string |  |
    | `state` | any |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `backend_id` | string | Health monitor ID in Octavia |
    | `access_url` | string |  |
    | `pool` | string (uri) | Pool this health monitor belongs to |
    | `pool_name` | string |  |
    | `pool_uuid` | string (uuid) |  |
    | `load_balancer_uuid` | string (uuid) |  |
    | `type` | string |  |
    | `delay` | integer |  |
    | `timeout` | integer |  |
    | `max_retries` | integer |  |
    | `provisioning_status` | string |  |
    | `operating_status` | string |  |
    | `marketplace_offering_uuid` | string |  |
    | `marketplace_offering_name` | string |  |
    | `marketplace_offering_type` | string |  |
    | `marketplace_offering_plugin_options` | object (free-form) |  |
    | `marketplace_category_uuid` | string |  |
    | `marketplace_category_name` | string |  |
    | `marketplace_resource_uuid` | string |  |
    | `marketplace_plan_uuid` | string |  |
    | `marketplace_resource_state` | string |  |
    | `is_usage_based` | boolean |  |
    | `is_limit_based` | boolean |  |

---

### Get health monitor details

Retrieve details of a specific health monitor.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openstack-health-monitors/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.open_stack_health_monitor_field_enum import OpenStackHealthMonitorFieldEnum # (1)
    from waldur_api_client.api.openstack_health_monitors import openstack_health_monitors_retrieve # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openstack_health_monitors_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`OpenStackHealthMonitorFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/open_stack_health_monitor_field_enum.py)
    2.  **API Source:** [`openstack_health_monitors_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_health_monitors/openstack_health_monitors_retrieve.py)

=== "TypeScript"

    ```typescript
    import { openstackHealthMonitorsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await openstackHealthMonitorsRetrieve({
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
    | `description` | string |  |
    | `service_name` | string |  |
    | `service_settings` | string (uri) |  |
    | `service_settings_uuid` | string (uuid) |  |
    | `service_settings_state` | string |  |
    | `service_settings_error_message` | string |  |
    | `project` | string (uri) |  |
    | `project_name` | string |  |
    | `project_uuid` | string (uuid) |  |
    | `customer` | string (uri) |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `customer_native_name` | string |  |
    | `customer_abbreviation` | string |  |
    | `error_message` | string |  |
    | `error_traceback` | string |  |
    | `resource_type` | string |  |
    | `state` | any |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `backend_id` | string | Health monitor ID in Octavia |
    | `access_url` | string |  |
    | `pool` | string (uri) | Pool this health monitor belongs to |
    | `pool_name` | string |  |
    | `pool_uuid` | string (uuid) |  |
    | `load_balancer_uuid` | string (uuid) |  |
    | `type` | string |  |
    | `delay` | integer |  |
    | `timeout` | integer |  |
    | `max_retries` | integer |  |
    | `provisioning_status` | string |  |
    | `operating_status` | string |  |
    | `marketplace_offering_uuid` | string |  |
    | `marketplace_offering_name` | string |  |
    | `marketplace_offering_type` | string |  |
    | `marketplace_offering_plugin_options` | object (free-form) |  |
    | `marketplace_category_uuid` | string |  |
    | `marketplace_category_name` | string |  |
    | `marketplace_resource_uuid` | string |  |
    | `marketplace_plan_uuid` | string |  |
    | `marketplace_resource_state` | string |  |
    | `is_usage_based` | boolean |  |
    | `is_limit_based` | boolean |  |

---

### List listeners

Get a list of load balancer listeners.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openstack-listeners/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.core_states import CoreStates # (1)
    from waldur_api_client.models.open_stack_listener_field_enum import OpenStackListenerFieldEnum # (2)
    from waldur_api_client.api.openstack_listeners import openstack_listeners_list # (3)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openstack_listeners_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`CoreStates`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/core_states.py)
    2.  **Model Source:** [`OpenStackListenerFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/open_stack_listener_field_enum.py)
    3.  **API Source:** [`openstack_listeners_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_listeners/openstack_listeners_list.py)

=== "TypeScript"

    ```typescript
    import { openstackListenersList } from 'waldur-js-client';
    
    try {
      const response = await openstackListenersList({
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
    | `field` | array |  |
    | `load_balancer` | string (uri) | Load balancer URL |
    | `load_balancer_uuid` | string (uuid) | Load balancer UUID |
    | `name` | string | Name |
    | `name_exact` | string | Name (exact) |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `state` | array | State<br><br> |
    | `tenant_uuid` | string (uuid) | Tenant UUID |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `description` | string |  |
    | `service_name` | string |  |
    | `service_settings` | string (uri) |  |
    | `service_settings_uuid` | string (uuid) |  |
    | `service_settings_state` | string |  |
    | `service_settings_error_message` | string |  |
    | `project` | string (uri) |  |
    | `project_name` | string |  |
    | `project_uuid` | string (uuid) |  |
    | `customer` | string (uri) |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `customer_native_name` | string |  |
    | `customer_abbreviation` | string |  |
    | `error_message` | string |  |
    | `error_traceback` | string |  |
    | `resource_type` | string |  |
    | `state` | any |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `backend_id` | string | Listener ID in Octavia |
    | `access_url` | string |  |
    | `load_balancer` | string (uri) | Load balancer this listener belongs to |
    | `load_balancer_name` | string |  |
    | `load_balancer_uuid` | string (uuid) |  |
    | `protocol` | string |  |
    | `protocol_port` | integer |  |
    | `default_pool` | string (uri) | Default pool for this listener |
    | `provisioning_status` | string |  |
    | `operating_status` | string |  |
    | `marketplace_offering_uuid` | string |  |
    | `marketplace_offering_name` | string |  |
    | `marketplace_offering_type` | string |  |
    | `marketplace_offering_plugin_options` | object (free-form) |  |
    | `marketplace_category_uuid` | string |  |
    | `marketplace_category_name` | string |  |
    | `marketplace_resource_uuid` | string |  |
    | `marketplace_plan_uuid` | string |  |
    | `marketplace_resource_state` | string |  |
    | `is_usage_based` | boolean |  |
    | `is_limit_based` | boolean |  |

---

### Get listener details

Retrieve details of a specific listener.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openstack-listeners/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.open_stack_listener_field_enum import OpenStackListenerFieldEnum # (1)
    from waldur_api_client.api.openstack_listeners import openstack_listeners_retrieve # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openstack_listeners_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`OpenStackListenerFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/open_stack_listener_field_enum.py)
    2.  **API Source:** [`openstack_listeners_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_listeners/openstack_listeners_retrieve.py)

=== "TypeScript"

    ```typescript
    import { openstackListenersRetrieve } from 'waldur-js-client';
    
    try {
      const response = await openstackListenersRetrieve({
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
    | `description` | string |  |
    | `service_name` | string |  |
    | `service_settings` | string (uri) |  |
    | `service_settings_uuid` | string (uuid) |  |
    | `service_settings_state` | string |  |
    | `service_settings_error_message` | string |  |
    | `project` | string (uri) |  |
    | `project_name` | string |  |
    | `project_uuid` | string (uuid) |  |
    | `customer` | string (uri) |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `customer_native_name` | string |  |
    | `customer_abbreviation` | string |  |
    | `error_message` | string |  |
    | `error_traceback` | string |  |
    | `resource_type` | string |  |
    | `state` | any |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `backend_id` | string | Listener ID in Octavia |
    | `access_url` | string |  |
    | `load_balancer` | string (uri) | Load balancer this listener belongs to |
    | `load_balancer_name` | string |  |
    | `load_balancer_uuid` | string (uuid) |  |
    | `protocol` | string |  |
    | `protocol_port` | integer |  |
    | `default_pool` | string (uri) | Default pool for this listener |
    | `provisioning_status` | string |  |
    | `operating_status` | string |  |
    | `marketplace_offering_uuid` | string |  |
    | `marketplace_offering_name` | string |  |
    | `marketplace_offering_type` | string |  |
    | `marketplace_offering_plugin_options` | object (free-form) |  |
    | `marketplace_category_uuid` | string |  |
    | `marketplace_category_name` | string |  |
    | `marketplace_resource_uuid` | string |  |
    | `marketplace_plan_uuid` | string |  |
    | `marketplace_resource_state` | string |  |
    | `is_usage_based` | boolean |  |
    | `is_limit_based` | boolean |  |

---

### List load balancers

Get a list of load balancers.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openstack-loadbalancers/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.core_states import CoreStates # (1)
    from waldur_api_client.models.open_stack_load_balancer_field_enum import OpenStackLoadBalancerFieldEnum # (2)
    from waldur_api_client.api.openstack_loadbalancers import openstack_loadbalancers_list # (3)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openstack_loadbalancers_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`CoreStates`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/core_states.py)
    2.  **Model Source:** [`OpenStackLoadBalancerFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/open_stack_load_balancer_field_enum.py)
    3.  **API Source:** [`openstack_loadbalancers_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_loadbalancers/openstack_loadbalancers_list.py)

=== "TypeScript"

    ```typescript
    import { openstackLoadbalancersList } from 'waldur-js-client';
    
    try {
      const response = await openstackLoadbalancersList({
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
    | `field` | array |  |
    | `name` | string | Name |
    | `name_exact` | string | Name (exact) |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `state` | array | State<br><br> |
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
    | `description` | string |  |
    | `service_name` | string |  |
    | `service_settings` | string (uri) |  |
    | `service_settings_uuid` | string (uuid) |  |
    | `service_settings_state` | string |  |
    | `service_settings_error_message` | string |  |
    | `project` | string (uri) |  |
    | `project_name` | string |  |
    | `project_uuid` | string (uuid) |  |
    | `customer` | string (uri) |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `customer_native_name` | string |  |
    | `customer_abbreviation` | string |  |
    | `error_message` | string |  |
    | `error_traceback` | string |  |
    | `resource_type` | string |  |
    | `state` | any |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `backend_id` | string | Load balancer ID in Octavia |
    | `access_url` | string |  |
    | `tenant` | string (uri) | OpenStack tenant this load balancer belongs to |
    | `tenant_name` | string |  |
    | `tenant_uuid` | string (uuid) |  |
    | `vip_address` | any | An IPv4 or IPv6 address. |
    | `vip_subnet` | string (uri) |  |
    | `vip_port` | string (uri) |  |
    | `attached_floating_ip` | string (uri) | Floating IP attached to the VIP port |
    | `provider` | string |  |
    | `provisioning_status` | string |  |
    | `operating_status` | string |  |
    | `marketplace_offering_uuid` | string |  |
    | `marketplace_offering_name` | string |  |
    | `marketplace_offering_type` | string |  |
    | `marketplace_offering_plugin_options` | object (free-form) |  |
    | `marketplace_category_uuid` | string |  |
    | `marketplace_category_name` | string |  |
    | `marketplace_resource_uuid` | string |  |
    | `marketplace_plan_uuid` | string |  |
    | `marketplace_resource_state` | string |  |
    | `is_usage_based` | boolean |  |
    | `is_limit_based` | boolean |  |

---

### Get load balancer details

Retrieve details of a specific load balancer.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openstack-loadbalancers/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.open_stack_load_balancer_field_enum import OpenStackLoadBalancerFieldEnum # (1)
    from waldur_api_client.api.openstack_loadbalancers import openstack_loadbalancers_retrieve # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openstack_loadbalancers_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`OpenStackLoadBalancerFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/open_stack_load_balancer_field_enum.py)
    2.  **API Source:** [`openstack_loadbalancers_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_loadbalancers/openstack_loadbalancers_retrieve.py)

=== "TypeScript"

    ```typescript
    import { openstackLoadbalancersRetrieve } from 'waldur-js-client';
    
    try {
      const response = await openstackLoadbalancersRetrieve({
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
    | `description` | string |  |
    | `service_name` | string |  |
    | `service_settings` | string (uri) |  |
    | `service_settings_uuid` | string (uuid) |  |
    | `service_settings_state` | string |  |
    | `service_settings_error_message` | string |  |
    | `project` | string (uri) |  |
    | `project_name` | string |  |
    | `project_uuid` | string (uuid) |  |
    | `customer` | string (uri) |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `customer_native_name` | string |  |
    | `customer_abbreviation` | string |  |
    | `error_message` | string |  |
    | `error_traceback` | string |  |
    | `resource_type` | string |  |
    | `state` | any |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `backend_id` | string | Load balancer ID in Octavia |
    | `access_url` | string |  |
    | `tenant` | string (uri) | OpenStack tenant this load balancer belongs to |
    | `tenant_name` | string |  |
    | `tenant_uuid` | string (uuid) |  |
    | `vip_address` | any | An IPv4 or IPv6 address. |
    | `vip_subnet` | string (uri) |  |
    | `vip_port` | string (uri) |  |
    | `attached_floating_ip` | string (uri) | Floating IP attached to the VIP port |
    | `provider` | string |  |
    | `provisioning_status` | string |  |
    | `operating_status` | string |  |
    | `marketplace_offering_uuid` | string |  |
    | `marketplace_offering_name` | string |  |
    | `marketplace_offering_type` | string |  |
    | `marketplace_offering_plugin_options` | object (free-form) |  |
    | `marketplace_category_uuid` | string |  |
    | `marketplace_category_name` | string |  |
    | `marketplace_resource_uuid` | string |  |
    | `marketplace_plan_uuid` | string |  |
    | `marketplace_resource_state` | string |  |
    | `is_usage_based` | boolean |  |
    | `is_limit_based` | boolean |  |

---

### List pool members

Get a list of pool members.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openstack-pool-members/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.core_states import CoreStates # (1)
    from waldur_api_client.models.open_stack_pool_member_field_enum import OpenStackPoolMemberFieldEnum # (2)
    from waldur_api_client.api.openstack_pool_members import openstack_pool_members_list # (3)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openstack_pool_members_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`CoreStates`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/core_states.py)
    2.  **Model Source:** [`OpenStackPoolMemberFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/open_stack_pool_member_field_enum.py)
    3.  **API Source:** [`openstack_pool_members_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_pool_members/openstack_pool_members_list.py)

=== "TypeScript"

    ```typescript
    import { openstackPoolMembersList } from 'waldur-js-client';
    
    try {
      const response = await openstackPoolMembersList({
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
    | `field` | array |  |
    | `load_balancer_uuid` | string (uuid) | Load balancer UUID |
    | `name` | string | Name |
    | `name_exact` | string | Name (exact) |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `pool` | string (uri) | Pool URL |
    | `pool_uuid` | string (uuid) | Pool UUID |
    | `state` | array | State<br><br> |
    | `tenant_uuid` | string (uuid) | Tenant UUID |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `description` | string |  |
    | `service_name` | string |  |
    | `service_settings` | string (uri) |  |
    | `service_settings_uuid` | string (uuid) |  |
    | `service_settings_state` | string |  |
    | `service_settings_error_message` | string |  |
    | `project` | string (uri) |  |
    | `project_name` | string |  |
    | `project_uuid` | string (uuid) |  |
    | `customer` | string (uri) |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `customer_native_name` | string |  |
    | `customer_abbreviation` | string |  |
    | `error_message` | string |  |
    | `error_traceback` | string |  |
    | `resource_type` | string |  |
    | `state` | any |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `backend_id` | string | Member ID in Octavia |
    | `access_url` | string |  |
    | `pool` | string (uri) | Pool this member belongs to |
    | `pool_name` | string |  |
    | `pool_uuid` | string (uuid) |  |
    | `load_balancer_uuid` | string (uuid) |  |
    | `address` | any | An IPv4 or IPv6 address. |
    | `protocol_port` | integer |  |
    | `subnet` | string (uri) |  |
    | `weight` | integer |  |
    | `provisioning_status` | string |  |
    | `operating_status` | string |  |
    | `marketplace_offering_uuid` | string |  |
    | `marketplace_offering_name` | string |  |
    | `marketplace_offering_type` | string |  |
    | `marketplace_offering_plugin_options` | object (free-form) |  |
    | `marketplace_category_uuid` | string |  |
    | `marketplace_category_name` | string |  |
    | `marketplace_resource_uuid` | string |  |
    | `marketplace_plan_uuid` | string |  |
    | `marketplace_resource_state` | string |  |
    | `is_usage_based` | boolean |  |
    | `is_limit_based` | boolean |  |

---

### Get pool member details

Retrieve details of a specific pool member.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openstack-pool-members/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.open_stack_pool_member_field_enum import OpenStackPoolMemberFieldEnum # (1)
    from waldur_api_client.api.openstack_pool_members import openstack_pool_members_retrieve # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openstack_pool_members_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`OpenStackPoolMemberFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/open_stack_pool_member_field_enum.py)
    2.  **API Source:** [`openstack_pool_members_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_pool_members/openstack_pool_members_retrieve.py)

=== "TypeScript"

    ```typescript
    import { openstackPoolMembersRetrieve } from 'waldur-js-client';
    
    try {
      const response = await openstackPoolMembersRetrieve({
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
    | `description` | string |  |
    | `service_name` | string |  |
    | `service_settings` | string (uri) |  |
    | `service_settings_uuid` | string (uuid) |  |
    | `service_settings_state` | string |  |
    | `service_settings_error_message` | string |  |
    | `project` | string (uri) |  |
    | `project_name` | string |  |
    | `project_uuid` | string (uuid) |  |
    | `customer` | string (uri) |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `customer_native_name` | string |  |
    | `customer_abbreviation` | string |  |
    | `error_message` | string |  |
    | `error_traceback` | string |  |
    | `resource_type` | string |  |
    | `state` | any |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `backend_id` | string | Member ID in Octavia |
    | `access_url` | string |  |
    | `pool` | string (uri) | Pool this member belongs to |
    | `pool_name` | string |  |
    | `pool_uuid` | string (uuid) |  |
    | `load_balancer_uuid` | string (uuid) |  |
    | `address` | any | An IPv4 or IPv6 address. |
    | `protocol_port` | integer |  |
    | `subnet` | string (uri) |  |
    | `weight` | integer |  |
    | `provisioning_status` | string |  |
    | `operating_status` | string |  |
    | `marketplace_offering_uuid` | string |  |
    | `marketplace_offering_name` | string |  |
    | `marketplace_offering_type` | string |  |
    | `marketplace_offering_plugin_options` | object (free-form) |  |
    | `marketplace_category_uuid` | string |  |
    | `marketplace_category_name` | string |  |
    | `marketplace_resource_uuid` | string |  |
    | `marketplace_plan_uuid` | string |  |
    | `marketplace_resource_state` | string |  |
    | `is_usage_based` | boolean |  |
    | `is_limit_based` | boolean |  |

---

### List pools

Get a list of load balancer pools.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openstack-pools/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.core_states import CoreStates # (1)
    from waldur_api_client.models.open_stack_pool_field_enum import OpenStackPoolFieldEnum # (2)
    from waldur_api_client.api.openstack_pools import openstack_pools_list # (3)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openstack_pools_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`CoreStates`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/core_states.py)
    2.  **Model Source:** [`OpenStackPoolFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/open_stack_pool_field_enum.py)
    3.  **API Source:** [`openstack_pools_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_pools/openstack_pools_list.py)

=== "TypeScript"

    ```typescript
    import { openstackPoolsList } from 'waldur-js-client';
    
    try {
      const response = await openstackPoolsList({
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
    | `field` | array |  |
    | `load_balancer` | string (uri) | Load balancer URL |
    | `load_balancer_uuid` | string (uuid) | Load balancer UUID |
    | `name` | string | Name |
    | `name_exact` | string | Name (exact) |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `state` | array | State<br><br> |
    | `tenant_uuid` | string (uuid) | Tenant UUID |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `description` | string |  |
    | `service_name` | string |  |
    | `service_settings` | string (uri) |  |
    | `service_settings_uuid` | string (uuid) |  |
    | `service_settings_state` | string |  |
    | `service_settings_error_message` | string |  |
    | `project` | string (uri) |  |
    | `project_name` | string |  |
    | `project_uuid` | string (uuid) |  |
    | `customer` | string (uri) |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `customer_native_name` | string |  |
    | `customer_abbreviation` | string |  |
    | `error_message` | string |  |
    | `error_traceback` | string |  |
    | `resource_type` | string |  |
    | `state` | any |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `backend_id` | string | Pool ID in Octavia |
    | `access_url` | string |  |
    | `load_balancer` | string (uri) | Load balancer this pool belongs to |
    | `load_balancer_name` | string |  |
    | `load_balancer_uuid` | string (uuid) |  |
    | `protocol` | string |  |
    | `lb_algorithm` | string |  |
    | `provisioning_status` | string |  |
    | `operating_status` | string |  |
    | `marketplace_offering_uuid` | string |  |
    | `marketplace_offering_name` | string |  |
    | `marketplace_offering_type` | string |  |
    | `marketplace_offering_plugin_options` | object (free-form) |  |
    | `marketplace_category_uuid` | string |  |
    | `marketplace_category_name` | string |  |
    | `marketplace_resource_uuid` | string |  |
    | `marketplace_plan_uuid` | string |  |
    | `marketplace_resource_state` | string |  |
    | `is_usage_based` | boolean |  |
    | `is_limit_based` | boolean |  |

---

### Get pool details

Retrieve details of a specific pool.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openstack-pools/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.open_stack_pool_field_enum import OpenStackPoolFieldEnum # (1)
    from waldur_api_client.api.openstack_pools import openstack_pools_retrieve # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openstack_pools_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`OpenStackPoolFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/open_stack_pool_field_enum.py)
    2.  **API Source:** [`openstack_pools_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_pools/openstack_pools_retrieve.py)

=== "TypeScript"

    ```typescript
    import { openstackPoolsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await openstackPoolsRetrieve({
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
    | `description` | string |  |
    | `service_name` | string |  |
    | `service_settings` | string (uri) |  |
    | `service_settings_uuid` | string (uuid) |  |
    | `service_settings_state` | string |  |
    | `service_settings_error_message` | string |  |
    | `project` | string (uri) |  |
    | `project_name` | string |  |
    | `project_uuid` | string (uuid) |  |
    | `customer` | string (uri) |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `customer_native_name` | string |  |
    | `customer_abbreviation` | string |  |
    | `error_message` | string |  |
    | `error_traceback` | string |  |
    | `resource_type` | string |  |
    | `state` | any |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `backend_id` | string | Pool ID in Octavia |
    | `access_url` | string |  |
    | `load_balancer` | string (uri) | Load balancer this pool belongs to |
    | `load_balancer_name` | string |  |
    | `load_balancer_uuid` | string (uuid) |  |
    | `protocol` | string |  |
    | `lb_algorithm` | string |  |
    | `provisioning_status` | string |  |
    | `operating_status` | string |  |
    | `marketplace_offering_uuid` | string |  |
    | `marketplace_offering_name` | string |  |
    | `marketplace_offering_type` | string |  |
    | `marketplace_offering_plugin_options` | object (free-form) |  |
    | `marketplace_category_uuid` | string |  |
    | `marketplace_category_name` | string |  |
    | `marketplace_resource_uuid` | string |  |
    | `marketplace_plan_uuid` | string |  |
    | `marketplace_resource_state` | string |  |
    | `is_usage_based` | boolean |  |
    | `is_limit_based` | boolean |  |

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/openstack/discovery/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openstack import openstack_discovery_create # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openstack_discovery_create.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openstack_discovery_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack/openstack_discovery_create.py)

=== "TypeScript"

    ```typescript
    import { openstackDiscoveryCreate } from 'waldur-js-client';
    
    try {
      const response = await openstackDiscoveryCreate({
      auth: "Token YOUR_API_TOKEN"
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Responses"

    **`201`** - No response body
    

---

### Discover available external networks

Discover available external networks.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/openstack/discovery/discover_external_networks/ \
      Authorization:"Token YOUR_API_TOKEN" \
      auth_url="https://api.example.com/api/auth-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      username="alice" \
      password="********"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.discover_external_networks_request_request import DiscoverExternalNetworksRequestRequest # (1)
    from waldur_api_client.api.openstack import openstack_discovery_discover_external_networks # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = DiscoverExternalNetworksRequestRequest(
        auth_url="https://api.example.com/api/auth-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        username="alice",
        password="********"
    )
    response = openstack_discovery_discover_external_networks.sync(
        client=client,
        body=body_data
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`DiscoverExternalNetworksRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/discover_external_networks_request_request.py)
    2.  **API Source:** [`openstack_discovery_discover_external_networks`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack/openstack_discovery_discover_external_networks.py)

=== "TypeScript"

    ```typescript
    import { openstackDiscoveryDiscoverExternalNetworks } from 'waldur-js-client';
    
    try {
      const response = await openstackDiscoveryDiscoverExternalNetworks({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "auth_url": "https://api.example.com/api/auth-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "username": "alice",
        "password": "********"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Query Parameters"

    | Name | Type | Description |
    |---|---|---|
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |


=== "Request Body (required)"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `auth_url` | string (uri) | ✓ | Keystone auth URL (e.g., https://cloud.example.com:5000/v3) |
    | `username` | string | ✓ |  |
    | `password` | string | ✓ | <br>_Constraints: write-only_ |
    | `user_domain_name` | string |  | Keystone user domain name<br>_Constraints: default: `Default`_ |
    | `project_domain_name` | string |  | Keystone project domain name<br>_Constraints: default: `Default`_ |
    | `project_name` | string |  | Keystone project (tenant) name<br>_Constraints: default: `admin`_ |
    | `auth_type` | any |  | Authentication method: password or v3applicationcredential<br>_Constraints: default: `password`_ |
    | `verify_ssl` | boolean |  | <br>_Constraints: default: `False`_ |
    | `certificate` | string |  | PEM-encoded CA certificate for SSL verification<br>_Constraints: write-only_ |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `id` | string |
    | `name` | string |
    | `is_shared` | boolean |
    | `subnets` | array of objects |
    | `subnets.id` | string |
    | `subnets.name` | string |
    | `subnets.cidr` | string |
    | `subnets.gateway_ip` | string |
    | `subnets.ip_version` | integer |

---

### Discover available flavors

Discover available flavors.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/openstack/discovery/discover_flavors/ \
      Authorization:"Token YOUR_API_TOKEN" \
      auth_url="https://api.example.com/api/auth-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      username="alice" \
      password="********"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.discover_flavors_request_request import DiscoverFlavorsRequestRequest # (1)
    from waldur_api_client.api.openstack import openstack_discovery_discover_flavors # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = DiscoverFlavorsRequestRequest(
        auth_url="https://api.example.com/api/auth-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        username="alice",
        password="********"
    )
    response = openstack_discovery_discover_flavors.sync(
        client=client,
        body=body_data
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`DiscoverFlavorsRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/discover_flavors_request_request.py)
    2.  **API Source:** [`openstack_discovery_discover_flavors`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack/openstack_discovery_discover_flavors.py)

=== "TypeScript"

    ```typescript
    import { openstackDiscoveryDiscoverFlavors } from 'waldur-js-client';
    
    try {
      const response = await openstackDiscoveryDiscoverFlavors({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "auth_url": "https://api.example.com/api/auth-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "username": "alice",
        "password": "********"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Query Parameters"

    | Name | Type | Description |
    |---|---|---|
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |


=== "Request Body (required)"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `auth_url` | string (uri) | ✓ | Keystone auth URL (e.g., https://cloud.example.com:5000/v3) |
    | `username` | string | ✓ |  |
    | `password` | string | ✓ | <br>_Constraints: write-only_ |
    | `user_domain_name` | string |  | Keystone user domain name<br>_Constraints: default: `Default`_ |
    | `project_domain_name` | string |  | Keystone project domain name<br>_Constraints: default: `Default`_ |
    | `project_name` | string |  | Keystone project (tenant) name<br>_Constraints: default: `admin`_ |
    | `auth_type` | any |  | Authentication method: password or v3applicationcredential<br>_Constraints: default: `password`_ |
    | `verify_ssl` | boolean |  | <br>_Constraints: default: `False`_ |
    | `certificate` | string |  | PEM-encoded CA certificate for SSL verification<br>_Constraints: write-only_ |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `id` | string |  |
    | `name` | string |  |
    | `vcpus` | integer |  |
    | `ram` | integer | RAM in MB |
    | `disk` | integer | Disk in GB |

---

### Discover available Nova instance availability zones

Discover available Nova instance availability zones.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/openstack/discovery/discover_instance_availability_zones/ \
      Authorization:"Token YOUR_API_TOKEN" \
      auth_url="https://api.example.com/api/auth-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      username="alice" \
      password="********"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.discover_instance_availability_zones_request_request import DiscoverInstanceAvailabilityZonesRequestRequest # (1)
    from waldur_api_client.api.openstack import openstack_discovery_discover_instance_availability_zones # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = DiscoverInstanceAvailabilityZonesRequestRequest(
        auth_url="https://api.example.com/api/auth-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        username="alice",
        password="********"
    )
    response = openstack_discovery_discover_instance_availability_zones.sync(
        client=client,
        body=body_data
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`DiscoverInstanceAvailabilityZonesRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/discover_instance_availability_zones_request_request.py)
    2.  **API Source:** [`openstack_discovery_discover_instance_availability_zones`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack/openstack_discovery_discover_instance_availability_zones.py)

=== "TypeScript"

    ```typescript
    import { openstackDiscoveryDiscoverInstanceAvailabilityZones } from 'waldur-js-client';
    
    try {
      const response = await openstackDiscoveryDiscoverInstanceAvailabilityZones({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "auth_url": "https://api.example.com/api/auth-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "username": "alice",
        "password": "********"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Query Parameters"

    | Name | Type | Description |
    |---|---|---|
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |


=== "Request Body (required)"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `auth_url` | string (uri) | ✓ | Keystone auth URL (e.g., https://cloud.example.com:5000/v3) |
    | `username` | string | ✓ |  |
    | `password` | string | ✓ | <br>_Constraints: write-only_ |
    | `user_domain_name` | string |  | Keystone user domain name<br>_Constraints: default: `Default`_ |
    | `project_domain_name` | string |  | Keystone project domain name<br>_Constraints: default: `Default`_ |
    | `project_name` | string |  | Keystone project (tenant) name<br>_Constraints: default: `admin`_ |
    | `auth_type` | any |  | Authentication method: password or v3applicationcredential<br>_Constraints: default: `password`_ |
    | `verify_ssl` | boolean |  | <br>_Constraints: default: `False`_ |
    | `certificate` | string |  | PEM-encoded CA certificate for SSL verification<br>_Constraints: write-only_ |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `name` | string |
    | `state` | string |

---

### Discover available Cinder volume availability zones

Discover available Cinder volume availability zones.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/openstack/discovery/discover_volume_availability_zones/ \
      Authorization:"Token YOUR_API_TOKEN" \
      auth_url="https://api.example.com/api/auth-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      username="alice" \
      password="********"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.discover_volume_availability_zones_request_request import DiscoverVolumeAvailabilityZonesRequestRequest # (1)
    from waldur_api_client.api.openstack import openstack_discovery_discover_volume_availability_zones # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = DiscoverVolumeAvailabilityZonesRequestRequest(
        auth_url="https://api.example.com/api/auth-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        username="alice",
        password="********"
    )
    response = openstack_discovery_discover_volume_availability_zones.sync(
        client=client,
        body=body_data
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`DiscoverVolumeAvailabilityZonesRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/discover_volume_availability_zones_request_request.py)
    2.  **API Source:** [`openstack_discovery_discover_volume_availability_zones`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack/openstack_discovery_discover_volume_availability_zones.py)

=== "TypeScript"

    ```typescript
    import { openstackDiscoveryDiscoverVolumeAvailabilityZones } from 'waldur-js-client';
    
    try {
      const response = await openstackDiscoveryDiscoverVolumeAvailabilityZones({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "auth_url": "https://api.example.com/api/auth-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "username": "alice",
        "password": "********"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Query Parameters"

    | Name | Type | Description |
    |---|---|---|
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |


=== "Request Body (required)"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `auth_url` | string (uri) | ✓ | Keystone auth URL (e.g., https://cloud.example.com:5000/v3) |
    | `username` | string | ✓ |  |
    | `password` | string | ✓ | <br>_Constraints: write-only_ |
    | `user_domain_name` | string |  | Keystone user domain name<br>_Constraints: default: `Default`_ |
    | `project_domain_name` | string |  | Keystone project domain name<br>_Constraints: default: `Default`_ |
    | `project_name` | string |  | Keystone project (tenant) name<br>_Constraints: default: `admin`_ |
    | `auth_type` | any |  | Authentication method: password or v3applicationcredential<br>_Constraints: default: `password`_ |
    | `verify_ssl` | boolean |  | <br>_Constraints: default: `False`_ |
    | `certificate` | string |  | PEM-encoded CA certificate for SSL verification<br>_Constraints: write-only_ |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `name` | string |
    | `state` | string |

---

### Discover available volume types

Discover available volume types.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/openstack/discovery/discover_volume_types/ \
      Authorization:"Token YOUR_API_TOKEN" \
      auth_url="https://api.example.com/api/auth-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      username="alice" \
      password="********"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.discover_volume_types_request_request import DiscoverVolumeTypesRequestRequest # (1)
    from waldur_api_client.api.openstack import openstack_discovery_discover_volume_types # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = DiscoverVolumeTypesRequestRequest(
        auth_url="https://api.example.com/api/auth-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        username="alice",
        password="********"
    )
    response = openstack_discovery_discover_volume_types.sync(
        client=client,
        body=body_data
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`DiscoverVolumeTypesRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/discover_volume_types_request_request.py)
    2.  **API Source:** [`openstack_discovery_discover_volume_types`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack/openstack_discovery_discover_volume_types.py)

=== "TypeScript"

    ```typescript
    import { openstackDiscoveryDiscoverVolumeTypes } from 'waldur-js-client';
    
    try {
      const response = await openstackDiscoveryDiscoverVolumeTypes({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "auth_url": "https://api.example.com/api/auth-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "username": "alice",
        "password": "********"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Query Parameters"

    | Name | Type | Description |
    |---|---|---|
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |


=== "Request Body (required)"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `auth_url` | string (uri) | ✓ | Keystone auth URL (e.g., https://cloud.example.com:5000/v3) |
    | `username` | string | ✓ |  |
    | `password` | string | ✓ | <br>_Constraints: write-only_ |
    | `user_domain_name` | string |  | Keystone user domain name<br>_Constraints: default: `Default`_ |
    | `project_domain_name` | string |  | Keystone project domain name<br>_Constraints: default: `Default`_ |
    | `project_name` | string |  | Keystone project (tenant) name<br>_Constraints: default: `admin`_ |
    | `auth_type` | any |  | Authentication method: password or v3applicationcredential<br>_Constraints: default: `password`_ |
    | `verify_ssl` | boolean |  | <br>_Constraints: default: `False`_ |
    | `certificate` | string |  | PEM-encoded CA certificate for SSL verification<br>_Constraints: write-only_ |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `id` | string |
    | `name` | string |
    | `description` | string |

---

### Build service_attributes and plugin_options from selected values

Build service_attributes and plugin_options from selected values.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/openstack/discovery/preview_service_attributes/ \
      Authorization:"Token YOUR_API_TOKEN" \
      auth_url="https://api.example.com/api/auth-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      username="alice" \
      password="********"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.preview_service_attributes_request_request import PreviewServiceAttributesRequestRequest # (1)
    from waldur_api_client.api.openstack import openstack_discovery_preview_service_attributes # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PreviewServiceAttributesRequestRequest(
        auth_url="https://api.example.com/api/auth-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        username="alice",
        password="********"
    )
    response = openstack_discovery_preview_service_attributes.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PreviewServiceAttributesRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/preview_service_attributes_request_request.py)
    2.  **API Source:** [`openstack_discovery_preview_service_attributes`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack/openstack_discovery_preview_service_attributes.py)

=== "TypeScript"

    ```typescript
    import { openstackDiscoveryPreviewServiceAttributes } from 'waldur-js-client';
    
    try {
      const response = await openstackDiscoveryPreviewServiceAttributes({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "auth_url": "https://api.example.com/api/auth-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "username": "alice",
        "password": "********"
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
    | `auth_url` | string (uri) | ✓ | Keystone auth URL (e.g., https://cloud.example.com:5000/v3) |
    | `username` | string | ✓ |  |
    | `password` | string | ✓ | <br>_Constraints: write-only_ |
    | `user_domain_name` | string |  | Keystone user domain name<br>_Constraints: default: `Default`_ |
    | `project_domain_name` | string |  | Keystone project domain name<br>_Constraints: default: `Default`_ |
    | `project_name` | string |  | Keystone project (tenant) name<br>_Constraints: default: `admin`_ |
    | `auth_type` | any |  | Authentication method: password or v3applicationcredential<br>_Constraints: default: `password`_ |
    | `verify_ssl` | boolean |  | <br>_Constraints: default: `False`_ |
    | `certificate` | string |  | PEM-encoded CA certificate for SSL verification<br>_Constraints: write-only_ |
    | `external_network_id` | string |  | Selected external network ID<br>_Constraints: default: ``_ |
    | `instance_availability_zone` | string |  | Selected instance availability zone name<br>_Constraints: default: ``_ |
    | `volume_availability_zone` | string |  | Selected volume availability zone name<br>_Constraints: default: ``_ |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `service_attributes` | object (free-form) |
    | `plugin_options` | object (free-form) |

---

### Validate OpenStack credentials without saving them

Validate OpenStack credentials without saving them.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/openstack/discovery/validate_credentials/ \
      Authorization:"Token YOUR_API_TOKEN" \
      auth_url="https://api.example.com/api/auth-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      username="alice" \
      password="********"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.open_stack_credentials_request import OpenStackCredentialsRequest # (1)
    from waldur_api_client.api.openstack import openstack_discovery_validate_credentials # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = OpenStackCredentialsRequest(
        auth_url="https://api.example.com/api/auth-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        username="alice",
        password="********"
    )
    response = openstack_discovery_validate_credentials.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`OpenStackCredentialsRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/open_stack_credentials_request.py)
    2.  **API Source:** [`openstack_discovery_validate_credentials`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack/openstack_discovery_validate_credentials.py)

=== "TypeScript"

    ```typescript
    import { openstackDiscoveryValidateCredentials } from 'waldur-js-client';
    
    try {
      const response = await openstackDiscoveryValidateCredentials({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "auth_url": "https://api.example.com/api/auth-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "username": "alice",
        "password": "********"
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
    | `auth_url` | string (uri) | ✓ | Keystone auth URL (e.g., https://cloud.example.com:5000/v3) |
    | `username` | string | ✓ |  |
    | `password` | string | ✓ | <br>_Constraints: write-only_ |
    | `user_domain_name` | string |  | Keystone user domain name<br>_Constraints: default: `Default`_ |
    | `project_domain_name` | string |  | Keystone project domain name<br>_Constraints: default: `Default`_ |
    | `project_name` | string |  | Keystone project (tenant) name<br>_Constraints: default: `admin`_ |
    | `auth_type` | any |  | Authentication method: password or v3applicationcredential<br>_Constraints: default: `password`_ |
    | `verify_ssl` | boolean |  | <br>_Constraints: default: `False`_ |
    | `certificate` | string |  | PEM-encoded CA certificate for SSL verification<br>_Constraints: write-only_ |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `valid` | boolean |
    | `message` | string |
    | `error` | string |
    | `server_info` | any |

---

### Create health monitor

Create a new health monitor for a pool.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/openstack-health-monitors/ \
      Authorization:"Token YOUR_API_TOKEN" \
      pool="https://api.example.com/api/pool/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      type="TCP"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.create_health_monitor_request import CreateHealthMonitorRequest # (1)
    from waldur_api_client.api.openstack_health_monitors import openstack_health_monitors_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = CreateHealthMonitorRequest(
        pool="https://api.example.com/api/pool/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        type="TCP"
    )
    response = openstack_health_monitors_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`CreateHealthMonitorRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/create_health_monitor_request.py)
    2.  **API Source:** [`openstack_health_monitors_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_health_monitors/openstack_health_monitors_create.py)

=== "TypeScript"

    ```typescript
    import { openstackHealthMonitorsCreate } from 'waldur-js-client';
    
    try {
      const response = await openstackHealthMonitorsCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "pool": "https://api.example.com/api/pool/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "type": "TCP"
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
    | `name` | string |  |  |
    | `delay` | integer |  | Interval between health checks in seconds<br>_Constraints: default: `5`_ |
    | `timeout` | integer |  | Time in seconds to timeout a health check<br>_Constraints: default: `5`_ |
    | `max_retries` | integer |  | <br>_Constraints: default: `3`_ |
    | `max_retries_down` | integer |  | <br>_Constraints: default: `3`_ |
    | `pool` | string (uri) | ✓ | Pool this health monitor belongs to |
    | `type` | string | ✓ | <br>_Enum: `TCP`, `UDP`_ |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `delay` | integer | Interval between health checks in seconds |
    | `timeout` | integer | Time in seconds to timeout a health check |
    | `max_retries` | integer |  |
    | `max_retries_down` | integer |  |
    | `pool` | string (uri) | Pool this health monitor belongs to |
    | `type` | string | <br>_Enum: `TCP`, `UDP`_ |

---

### Pull health monitor

Synchronize health monitor state from the OpenStack backend. Also pulls the associated pool and load balancer.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/openstack-health-monitors/a1b2c3d4-e5f6-7890-abcd-ef1234567890/pull/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openstack_health_monitors import openstack_health_monitors_pull # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openstack_health_monitors_pull.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openstack_health_monitors_pull`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_health_monitors/openstack_health_monitors_pull.py)

=== "TypeScript"

    ```typescript
    import { openstackHealthMonitorsPull } from 'waldur-js-client';
    
    try {
      const response = await openstackHealthMonitorsPull({
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

    **`202`** - No response body
    

---

### Create listener

Create a new listener for a load balancer.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/openstack-listeners/ \
      Authorization:"Token YOUR_API_TOKEN" \
      load_balancer="https://api.example.com/api/load-balancer/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      protocol="TCP" \
      protocol_port=8080
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.create_listener_request import CreateListenerRequest # (1)
    from waldur_api_client.api.openstack_listeners import openstack_listeners_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = CreateListenerRequest(
        load_balancer="https://api.example.com/api/load-balancer/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        protocol="TCP",
        protocol_port=8080
    )
    response = openstack_listeners_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`CreateListenerRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/create_listener_request.py)
    2.  **API Source:** [`openstack_listeners_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_listeners/openstack_listeners_create.py)

=== "TypeScript"

    ```typescript
    import { openstackListenersCreate } from 'waldur-js-client';
    
    try {
      const response = await openstackListenersCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "load_balancer": "https://api.example.com/api/load-balancer/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "protocol": "TCP",
        "protocol_port": 8080
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
    | `name` | string |  |  |
    | `default_pool` | string (uri) |  |  |
    | `load_balancer` | string (uri) | ✓ | Load balancer this listener belongs to |
    | `protocol` | string | ✓ | <br>_Enum: `TCP`, `UDP`_ |
    | `protocol_port` | integer | ✓ | Port on which the listener listens |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `name` | string |  |
    | `default_pool` | string (uri) |  |
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `load_balancer` | string (uri) | Load balancer this listener belongs to |
    | `protocol` | string | <br>_Enum: `TCP`, `UDP`_ |
    | `protocol_port` | integer | Port on which the listener listens |

---

### Pull listener

Synchronize listener state from the OpenStack backend. Also pulls pools of the load balancer and the load balancer itself.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/openstack-listeners/a1b2c3d4-e5f6-7890-abcd-ef1234567890/pull/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openstack_listeners import openstack_listeners_pull # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openstack_listeners_pull.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openstack_listeners_pull`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_listeners/openstack_listeners_pull.py)

=== "TypeScript"

    ```typescript
    import { openstackListenersPull } from 'waldur-js-client';
    
    try {
      const response = await openstackListenersPull({
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

    **`202`** - No response body
    

---

### Attach floating IP to VIP

Attach a floating IP to the load balancer VIP port.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/openstack-loadbalancers/a1b2c3d4-e5f6-7890-abcd-ef1234567890/attach_floating_ip/ \
      Authorization:"Token YOUR_API_TOKEN" \
      floating_ip="8.8.8.8"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.load_balancer_attach_floating_ip_request import LoadBalancerAttachFloatingIPRequest # (1)
    from waldur_api_client.api.openstack_loadbalancers import openstack_loadbalancers_attach_floating_ip # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = LoadBalancerAttachFloatingIPRequest(
        floating_ip="8.8.8.8"
    )
    response = openstack_loadbalancers_attach_floating_ip.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`LoadBalancerAttachFloatingIPRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/load_balancer_attach_floating_ip_request.py)
    2.  **API Source:** [`openstack_loadbalancers_attach_floating_ip`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_loadbalancers/openstack_loadbalancers_attach_floating_ip.py)

=== "TypeScript"

    ```typescript
    import { openstackLoadbalancersAttachFloatingIp } from 'waldur-js-client';
    
    try {
      const response = await openstackLoadbalancersAttachFloatingIp({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "floating_ip": "8.8.8.8"
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
    | `floating_ip` | string (uri) | ✓ |


=== "Responses"

    **`202`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `status` | string | Message that execution of the operation was scheduled. |

---

### Create load balancer

Create a new load balancer.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/openstack-loadbalancers/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-openstack-loadbalancer" \
      tenant="https://api.example.com/api/tenant/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      vip_subnet="https://api.example.com/api/vip-subnet/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.create_load_balancer_request import CreateLoadBalancerRequest # (1)
    from waldur_api_client.api.openstack_loadbalancers import openstack_loadbalancers_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = CreateLoadBalancerRequest(
        name="my-awesome-openstack-loadbalancer",
        tenant="https://api.example.com/api/tenant/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        vip_subnet="https://api.example.com/api/vip-subnet/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    )
    response = openstack_loadbalancers_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`CreateLoadBalancerRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/create_load_balancer_request.py)
    2.  **API Source:** [`openstack_loadbalancers_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_loadbalancers/openstack_loadbalancers_create.py)

=== "TypeScript"

    ```typescript
    import { openstackLoadbalancersCreate } from 'waldur-js-client';
    
    try {
      const response = await openstackLoadbalancersCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "name": "my-awesome-openstack-loadbalancer",
        "tenant": "https://api.example.com/api/tenant/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "vip_subnet": "https://api.example.com/api/vip-subnet/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
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
    | `name` | string | ✓ |  |
    | `tenant` | string (uri) | ✓ | OpenStack tenant this load balancer belongs to |
    | `vip_subnet` | string (uri) | ✓ |  |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `tenant` | string (uri) | OpenStack tenant this load balancer belongs to |
    | `vip_subnet` | string (uri) |  |

---

### Detach floating IP from VIP

Detach floating IP from the load balancer VIP port.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/openstack-loadbalancers/a1b2c3d4-e5f6-7890-abcd-ef1234567890/detach_floating_ip/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openstack_loadbalancers import openstack_loadbalancers_detach_floating_ip # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openstack_loadbalancers_detach_floating_ip.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openstack_loadbalancers_detach_floating_ip`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_loadbalancers/openstack_loadbalancers_detach_floating_ip.py)

=== "TypeScript"

    ```typescript
    import { openstackLoadbalancersDetachFloatingIp } from 'waldur-js-client';
    
    try {
      const response = await openstackLoadbalancersDetachFloatingIp({
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
    
    | Field | Type | Description |
    |---|---|---|
    | `status` | string | Message that execution of the operation was scheduled. |

---

### Pull load balancer

Synchronize load balancer state from the OpenStack backend.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/openstack-loadbalancers/a1b2c3d4-e5f6-7890-abcd-ef1234567890/pull/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openstack_loadbalancers import openstack_loadbalancers_pull # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openstack_loadbalancers_pull.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openstack_loadbalancers_pull`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_loadbalancers/openstack_loadbalancers_pull.py)

=== "TypeScript"

    ```typescript
    import { openstackLoadbalancersPull } from 'waldur-js-client';
    
    try {
      const response = await openstackLoadbalancersPull({
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

    **`202`** - No response body
    

---

### Unlink load balancer

Delete the load balancer from the Waldur database without scheduling operations on the OpenStack backend and without checking resource state. Staff-only; intended for cleaning up records stuck in transitional states.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/openstack-loadbalancers/a1b2c3d4-e5f6-7890-abcd-ef1234567890/unlink/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openstack_loadbalancers import openstack_loadbalancers_unlink # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openstack_loadbalancers_unlink.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openstack_loadbalancers_unlink`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_loadbalancers/openstack_loadbalancers_unlink.py)

=== "TypeScript"

    ```typescript
    import { openstackLoadbalancersUnlink } from 'waldur-js-client';
    
    try {
      const response = await openstackLoadbalancersUnlink({
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

### Create pool member

Create a new member for a pool.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/openstack-pool-members/ \
      Authorization:"Token YOUR_API_TOKEN" \
      pool="https://api.example.com/api/pool/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      address=null \
      protocol_port=8080 \
      subnet="https://api.example.com/api/subnet/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.create_pool_member_request import CreatePoolMemberRequest # (1)
    from waldur_api_client.api.openstack_pool_members import openstack_pool_members_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = CreatePoolMemberRequest(
        pool="https://api.example.com/api/pool/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        address=null,
        protocol_port=8080,
        subnet="https://api.example.com/api/subnet/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    )
    response = openstack_pool_members_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`CreatePoolMemberRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/create_pool_member_request.py)
    2.  **API Source:** [`openstack_pool_members_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_pool_members/openstack_pool_members_create.py)

=== "TypeScript"

    ```typescript
    import { openstackPoolMembersCreate } from 'waldur-js-client';
    
    try {
      const response = await openstackPoolMembersCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "pool": "https://api.example.com/api/pool/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "address": null,
        "protocol_port": 8080,
        "subnet": "https://api.example.com/api/subnet/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
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
    | `name` | string |  |  |
    | `weight` | integer |  | <br>_Constraints: default: `1`_ |
    | `pool` | string (uri) | ✓ | Pool this member belongs to |
    | `address` | any | ✓ | An IPv4 or IPv6 address. |
    | `protocol_port` | integer | ✓ | Port on the backend server |
    | `subnet` | string (uri) | ✓ |  |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `weight` | integer |  |
    | `pool` | string (uri) | Pool this member belongs to |
    | `address` | any | An IPv4 or IPv6 address. |
    | `protocol_port` | integer | Port on the backend server |
    | `subnet` | string (uri) |  |

---

### Pull pool member

Synchronize pool member state from the OpenStack backend. Also pulls the associated pool and load balancer.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/openstack-pool-members/a1b2c3d4-e5f6-7890-abcd-ef1234567890/pull/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openstack_pool_members import openstack_pool_members_pull # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openstack_pool_members_pull.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openstack_pool_members_pull`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_pool_members/openstack_pool_members_pull.py)

=== "TypeScript"

    ```typescript
    import { openstackPoolMembersPull } from 'waldur-js-client';
    
    try {
      const response = await openstackPoolMembersPull({
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

    **`202`** - No response body
    

---

### Create pool

Create a new pool for a load balancer.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/openstack-pools/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-openstack-pool" \
      load_balancer="https://api.example.com/api/load-balancer/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      protocol="TCP"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.create_pool_request import CreatePoolRequest # (1)
    from waldur_api_client.api.openstack_pools import openstack_pools_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = CreatePoolRequest(
        name="my-awesome-openstack-pool",
        load_balancer="https://api.example.com/api/load-balancer/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        protocol="TCP"
    )
    response = openstack_pools_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`CreatePoolRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/create_pool_request.py)
    2.  **API Source:** [`openstack_pools_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_pools/openstack_pools_create.py)

=== "TypeScript"

    ```typescript
    import { openstackPoolsCreate } from 'waldur-js-client';
    
    try {
      const response = await openstackPoolsCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "name": "my-awesome-openstack-pool",
        "load_balancer": "https://api.example.com/api/load-balancer/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "protocol": "TCP"
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
    | `name` | string | ✓ |  |
    | `load_balancer` | string (uri) | ✓ | Load balancer this pool belongs to |
    | `protocol` | string | ✓ | <br>_Enum: `TCP`, `UDP`_ |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `load_balancer` | string (uri) | Load balancer this pool belongs to |
    | `protocol` | string | <br>_Enum: `TCP`, `UDP`_ |

---

### Pull pool

Synchronize pool state from the OpenStack backend. Also pulls the associated load balancer.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/openstack-pools/a1b2c3d4-e5f6-7890-abcd-ef1234567890/pull/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openstack_pools import openstack_pools_pull # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openstack_pools_pull.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openstack_pools_pull`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_pools/openstack_pools_pull.py)

=== "TypeScript"

    ```typescript
    import { openstackPoolsPull } from 'waldur-js-client';
    
    try {
      const response = await openstackPoolsPull({
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

    **`202`** - No response body
    

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/openstack/discovery/123/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openstack import openstack_discovery_update # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openstack_discovery_update.sync(
        id=123,
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openstack_discovery_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack/openstack_discovery_update.py)

=== "TypeScript"

    ```typescript
    import { openstackDiscoveryUpdate } from 'waldur-js-client';
    
    try {
      const response = await openstackDiscoveryUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "id": 123
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required | Description |
    |---|---|---|---|
    | `id` | integer | ✓ | A unique integer value identifying this Service provider. |


=== "Responses"

    **`200`** - No response body
    

---

### Update health monitor

Update an existing health monitor.


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/openstack-health-monitors/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.update_health_monitor_request import UpdateHealthMonitorRequest # (1)
    from waldur_api_client.api.openstack_health_monitors import openstack_health_monitors_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = UpdateHealthMonitorRequest()
    response = openstack_health_monitors_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`UpdateHealthMonitorRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/update_health_monitor_request.py)
    2.  **API Source:** [`openstack_health_monitors_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_health_monitors/openstack_health_monitors_update.py)

=== "TypeScript"

    ```typescript
    import { openstackHealthMonitorsUpdate } from 'waldur-js-client';
    
    try {
      const response = await openstackHealthMonitorsUpdate({
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
    | `name` | string |  |  |
    | `delay` | integer |  | Interval between health checks in seconds<br>_Constraints: default: `5`_ |
    | `timeout` | integer |  | Time in seconds to timeout a health check<br>_Constraints: default: `5`_ |
    | `max_retries` | integer |  | <br>_Constraints: default: `3`_ |
    | `max_retries_down` | integer |  | <br>_Constraints: default: `3`_ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `delay` | integer | Interval between health checks in seconds |
    | `timeout` | integer | Time in seconds to timeout a health check |
    | `max_retries` | integer |  |
    | `max_retries_down` | integer |  |

---

### Update listener

Update an existing listener.


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/openstack-listeners/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.update_listener_request import UpdateListenerRequest # (1)
    from waldur_api_client.api.openstack_listeners import openstack_listeners_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = UpdateListenerRequest()
    response = openstack_listeners_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`UpdateListenerRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/update_listener_request.py)
    2.  **API Source:** [`openstack_listeners_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_listeners/openstack_listeners_update.py)

=== "TypeScript"

    ```typescript
    import { openstackListenersUpdate } from 'waldur-js-client';
    
    try {
      const response = await openstackListenersUpdate({
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
    | `default_pool` | string (uri) |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `name` | string |
    | `default_pool` | string (uri) |

---

### Update load balancer

Update an existing load balancer.


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/openstack-loadbalancers/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-openstack-loadbalancer"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.update_load_balancer_request import UpdateLoadBalancerRequest # (1)
    from waldur_api_client.api.openstack_loadbalancers import openstack_loadbalancers_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = UpdateLoadBalancerRequest(
        name="my-awesome-openstack-loadbalancer"
    )
    response = openstack_loadbalancers_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`UpdateLoadBalancerRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/update_load_balancer_request.py)
    2.  **API Source:** [`openstack_loadbalancers_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_loadbalancers/openstack_loadbalancers_update.py)

=== "TypeScript"

    ```typescript
    import { openstackLoadbalancersUpdate } from 'waldur-js-client';
    
    try {
      const response = await openstackLoadbalancersUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "name": "my-awesome-openstack-loadbalancer"
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


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `url` | string (uri) |
    | `uuid` | string (uuid) |
    | `name` | string |

---

### Update pool member

Update an existing pool member.


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/openstack-pool-members/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.update_pool_member_request import UpdatePoolMemberRequest # (1)
    from waldur_api_client.api.openstack_pool_members import openstack_pool_members_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = UpdatePoolMemberRequest()
    response = openstack_pool_members_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`UpdatePoolMemberRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/update_pool_member_request.py)
    2.  **API Source:** [`openstack_pool_members_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_pool_members/openstack_pool_members_update.py)

=== "TypeScript"

    ```typescript
    import { openstackPoolMembersUpdate } from 'waldur-js-client';
    
    try {
      const response = await openstackPoolMembersUpdate({
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
    | `weight` | integer |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `url` | string (uri) |
    | `uuid` | string (uuid) |
    | `name` | string |
    | `weight` | integer |

---

### Update pool

Update an existing pool.


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/openstack-pools/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-openstack-pool"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.update_pool_request import UpdatePoolRequest # (1)
    from waldur_api_client.api.openstack_pools import openstack_pools_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = UpdatePoolRequest(
        name="my-awesome-openstack-pool"
    )
    response = openstack_pools_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`UpdatePoolRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/update_pool_request.py)
    2.  **API Source:** [`openstack_pools_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_pools/openstack_pools_update.py)

=== "TypeScript"

    ```typescript
    import { openstackPoolsUpdate } from 'waldur-js-client';
    
    try {
      const response = await openstackPoolsUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "name": "my-awesome-openstack-pool"
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


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `url` | string (uri) |
    | `uuid` | string (uuid) |
    | `name` | string |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/openstack/discovery/123/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openstack import openstack_discovery_partial_update # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openstack_discovery_partial_update.sync(
        id=123,
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openstack_discovery_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack/openstack_discovery_partial_update.py)

=== "TypeScript"

    ```typescript
    import { openstackDiscoveryPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await openstackDiscoveryPartialUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "id": 123
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required | Description |
    |---|---|---|---|
    | `id` | integer | ✓ | A unique integer value identifying this Service provider. |


=== "Responses"

    **`200`** - No response body
    

---

### Partially update health monitor

Update specific fields of a health monitor.


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/openstack-health-monitors/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_update_health_monitor_request import PatchedUpdateHealthMonitorRequest # (1)
    from waldur_api_client.api.openstack_health_monitors import openstack_health_monitors_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedUpdateHealthMonitorRequest()
    response = openstack_health_monitors_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedUpdateHealthMonitorRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_update_health_monitor_request.py)
    2.  **API Source:** [`openstack_health_monitors_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_health_monitors/openstack_health_monitors_partial_update.py)

=== "TypeScript"

    ```typescript
    import { openstackHealthMonitorsPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await openstackHealthMonitorsPartialUpdate({
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
    | `name` | string |  |  |
    | `delay` | integer |  | Interval between health checks in seconds<br>_Constraints: default: `5`_ |
    | `timeout` | integer |  | Time in seconds to timeout a health check<br>_Constraints: default: `5`_ |
    | `max_retries` | integer |  | <br>_Constraints: default: `3`_ |
    | `max_retries_down` | integer |  | <br>_Constraints: default: `3`_ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `delay` | integer | Interval between health checks in seconds |
    | `timeout` | integer | Time in seconds to timeout a health check |
    | `max_retries` | integer |  |
    | `max_retries_down` | integer |  |

---

### Partially update listener

Update specific fields of a listener.


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/openstack-listeners/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_update_listener_request import PatchedUpdateListenerRequest # (1)
    from waldur_api_client.api.openstack_listeners import openstack_listeners_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedUpdateListenerRequest()
    response = openstack_listeners_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedUpdateListenerRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_update_listener_request.py)
    2.  **API Source:** [`openstack_listeners_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_listeners/openstack_listeners_partial_update.py)

=== "TypeScript"

    ```typescript
    import { openstackListenersPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await openstackListenersPartialUpdate({
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
    | `default_pool` | string (uri) |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `name` | string |
    | `default_pool` | string (uri) |

---

### Partially update load balancer

Update specific fields of a load balancer.


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/openstack-loadbalancers/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_update_load_balancer_request import PatchedUpdateLoadBalancerRequest # (1)
    from waldur_api_client.api.openstack_loadbalancers import openstack_loadbalancers_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedUpdateLoadBalancerRequest()
    response = openstack_loadbalancers_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedUpdateLoadBalancerRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_update_load_balancer_request.py)
    2.  **API Source:** [`openstack_loadbalancers_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_loadbalancers/openstack_loadbalancers_partial_update.py)

=== "TypeScript"

    ```typescript
    import { openstackLoadbalancersPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await openstackLoadbalancersPartialUpdate({
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


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `url` | string (uri) |
    | `uuid` | string (uuid) |
    | `name` | string |

---

### Partially update pool member

Update specific fields of a pool member.


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/openstack-pool-members/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_update_pool_member_request import PatchedUpdatePoolMemberRequest # (1)
    from waldur_api_client.api.openstack_pool_members import openstack_pool_members_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedUpdatePoolMemberRequest()
    response = openstack_pool_members_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedUpdatePoolMemberRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_update_pool_member_request.py)
    2.  **API Source:** [`openstack_pool_members_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_pool_members/openstack_pool_members_partial_update.py)

=== "TypeScript"

    ```typescript
    import { openstackPoolMembersPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await openstackPoolMembersPartialUpdate({
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
    | `weight` | integer |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `url` | string (uri) |
    | `uuid` | string (uuid) |
    | `name` | string |
    | `weight` | integer |

---

### Partially update pool

Update specific fields of a pool.


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/openstack-pools/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_update_pool_request import PatchedUpdatePoolRequest # (1)
    from waldur_api_client.api.openstack_pools import openstack_pools_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedUpdatePoolRequest()
    response = openstack_pools_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedUpdatePoolRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_update_pool_request.py)
    2.  **API Source:** [`openstack_pools_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_pools/openstack_pools_partial_update.py)

=== "TypeScript"

    ```typescript
    import { openstackPoolsPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await openstackPoolsPartialUpdate({
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


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `url` | string (uri) |
    | `uuid` | string (uuid) |
    | `name` | string |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/openstack/discovery/123/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openstack import openstack_discovery_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openstack_discovery_destroy.sync(
        id=123,
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openstack_discovery_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack/openstack_discovery_destroy.py)

=== "TypeScript"

    ```typescript
    import { openstackDiscoveryDestroy } from 'waldur-js-client';
    
    try {
      const response = await openstackDiscoveryDestroy({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "id": 123
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required | Description |
    |---|---|---|---|
    | `id` | integer | ✓ | A unique integer value identifying this Service provider. |


=== "Responses"

    **`204`** - No response body
    

---

### Delete health monitor

Delete a health monitor.


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/openstack-health-monitors/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openstack_health_monitors import openstack_health_monitors_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openstack_health_monitors_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openstack_health_monitors_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_health_monitors/openstack_health_monitors_destroy.py)

=== "TypeScript"

    ```typescript
    import { openstackHealthMonitorsDestroy } from 'waldur-js-client';
    
    try {
      const response = await openstackHealthMonitorsDestroy({
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

### Delete listener

Delete a listener.


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/openstack-listeners/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openstack_listeners import openstack_listeners_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openstack_listeners_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openstack_listeners_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_listeners/openstack_listeners_destroy.py)

=== "TypeScript"

    ```typescript
    import { openstackListenersDestroy } from 'waldur-js-client';
    
    try {
      const response = await openstackListenersDestroy({
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

### Delete load balancer

Delete a load balancer.


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/openstack-loadbalancers/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openstack_loadbalancers import openstack_loadbalancers_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openstack_loadbalancers_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openstack_loadbalancers_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_loadbalancers/openstack_loadbalancers_destroy.py)

=== "TypeScript"

    ```typescript
    import { openstackLoadbalancersDestroy } from 'waldur-js-client';
    
    try {
      const response = await openstackLoadbalancersDestroy({
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

### Delete pool member

Delete a pool member.


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/openstack-pool-members/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openstack_pool_members import openstack_pool_members_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openstack_pool_members_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openstack_pool_members_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_pool_members/openstack_pool_members_destroy.py)

=== "TypeScript"

    ```typescript
    import { openstackPoolMembersDestroy } from 'waldur-js-client';
    
    try {
      const response = await openstackPoolMembersDestroy({
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

### Delete pool

Delete a pool.


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/openstack-pools/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openstack_pools import openstack_pools_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openstack_pools_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openstack_pools_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_pools/openstack_pools_destroy.py)

=== "TypeScript"

    ```typescript
    import { openstackPoolsDestroy } from 'waldur-js-client';
    
    try {
      const response = await openstackPoolsDestroy({
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
