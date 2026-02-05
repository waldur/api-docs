# Openstack External Networks

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/openstack-external-networks/` | [List external networks](#list-external-networks) |
| <span class="http-badge http-get">GET</span> | `/api/openstack-external-networks/{uuid}/` | [Get external network details](#get-external-network-details) |

---

### List external networks

Get a list of provider-level external networks discovered from OpenStack.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openstack-external-networks/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openstack_external_networks import openstack_external_networks_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openstack_external_networks_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`openstack_external_networks_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_external_networks/openstack_external_networks_list.py)

=== "TypeScript"

    ```typescript
    import { openstackExternalNetworksList } from 'waldur-js-client';
    
    try {
      const response = await openstackExternalNetworksList({
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
    | `settings` | string | Settings URL |
    | `settings_uuid` | string (uuid) | Settings UUID |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `settings` | string (uri) |  |
    | `backend_id` | string |  |
    | `is_shared` | boolean |  |
    | `is_default` | boolean |  |
    | `status` | string |  |
    | `description` | string |  |
    | `subnets` | array of objects |  |
    | `subnets.uuid` | string (uuid) |  |
    | `subnets.name` | string |  |
    | `subnets.backend_id` | string |  |
    | `subnets.cidr` | string |  |
    | `subnets.gateway_ip` | any | An IPv4 or IPv6 address. |
    | `subnets.ip_version` | integer |  |
    | `subnets.enable_dhcp` | boolean |  |
    | `subnets.allocation_pools` | any |  |
    | `subnets.dns_nameservers` | any |  |
    | `subnets.public_ip_range` | string | Public CIDR mapped to this subnet (for carrier-grade NAT overlay) |
    | `subnets.description` | string |  |

---

### Get external network details

Retrieve details of a specific external network, including its subnets.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openstack-external-networks/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openstack_external_networks import openstack_external_networks_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openstack_external_networks_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openstack_external_networks_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openstack_external_networks/openstack_external_networks_retrieve.py)

=== "TypeScript"

    ```typescript
    import { openstackExternalNetworksRetrieve } from 'waldur-js-client';
    
    try {
      const response = await openstackExternalNetworksRetrieve({
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
    | `backend_id` | string |  |
    | `is_shared` | boolean |  |
    | `is_default` | boolean |  |
    | `status` | string |  |
    | `description` | string |  |
    | `subnets` | array of objects |  |
    | `subnets.uuid` | string (uuid) |  |
    | `subnets.name` | string |  |
    | `subnets.backend_id` | string |  |
    | `subnets.cidr` | string |  |
    | `subnets.gateway_ip` | any | An IPv4 or IPv6 address. |
    | `subnets.ip_version` | integer |  |
    | `subnets.enable_dhcp` | boolean |  |
    | `subnets.allocation_pools` | any |  |
    | `subnets.dns_nameservers` | any |  |
    | `subnets.public_ip_range` | string | Public CIDR mapped to this subnet (for carrier-grade NAT overlay) |
    | `subnets.description` | string |  |

---
