# Openstack

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/openstack/discovery/` | [Discovery](#discovery) |
| <span class="http-badge http-get">GET</span> | `/api/openstack/discovery/{id}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/openstack/discovery/` | [Discovery](#discovery) |
| <span class="http-badge http-put">PUT</span> | `/api/openstack/discovery/{id}/` | [Update](#update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/openstack/discovery/{id}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-delete">DELETE</span> | `/api/openstack/discovery/{id}/` | [Delete](#delete) |
| **Other Actions** | | |
| <span class="http-badge http-post">POST</span> | `/api/openstack/discovery/discover_external_networks/` | [Discover available external networks](#discover-available-external-networks) |
| <span class="http-badge http-post">POST</span> | `/api/openstack/discovery/discover_flavors/` | [Discover available flavors](#discover-available-flavors) |
| <span class="http-badge http-post">POST</span> | `/api/openstack/discovery/discover_instance_availability_zones/` | [Discover available Nova instance availability zones](#discover-available-nova-instance-availability-zones) |
| <span class="http-badge http-post">POST</span> | `/api/openstack/discovery/discover_volume_availability_zones/` | [Discover available Cinder volume availability zones](#discover-available-cinder-volume-availability-zones) |
| <span class="http-badge http-post">POST</span> | `/api/openstack/discovery/discover_volume_types/` | [Discover available volume types](#discover-available-volume-types) |
| <span class="http-badge http-post">POST</span> | `/api/openstack/discovery/preview_service_attributes/` | [Build service_attributes and plugin_options from selected values](#build-service_attributes-and-plugin_options-from-selected-values) |
| <span class="http-badge http-post">POST</span> | `/api/openstack/discovery/validate_credentials/` | [Validate OpenStack credentials without saving them](#validate-openstack-credentials-without-saving-them) |

---
## Core CRUD


### Discovery


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

### Discovery


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

## Other Actions


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
