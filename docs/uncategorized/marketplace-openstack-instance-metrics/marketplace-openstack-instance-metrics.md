# Marketplace Openstack Instance Metrics

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-openstack-instance-metrics/{uuid}/` | [Get how often an instance's or volume's metrics are read](#get-how-often-an-instances-or-volumes-metrics-are-read) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-openstack-instance-metrics/{uuid}/update_now/` | [Read an instance's metrics now](#read-an-instances-metrics-now) |
| **Other Actions** | | |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-openstack-instance-metrics/{uuid}/faster_updates/` | [Read an instance's metrics faster for a while](#read-an-instances-metrics-faster-for-a-while) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-openstack-instance-metrics/{uuid}/normal_updates/` | [Return an instance to the provider's interval](#return-an-instance-to-the-providers-interval) |

---
## Core CRUD


### Get how often an instance's or volume's metrics are read


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-openstack-instance-metrics/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_openstack_instance_metrics import marketplace_openstack_instance_metrics_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_openstack_instance_metrics_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_openstack_instance_metrics_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_openstack_instance_metrics/marketplace_openstack_instance_metrics_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOpenstackInstanceMetricsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOpenstackInstanceMetricsRetrieve({
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

    | Name | Type | Required | Description |
    |---|---|---|---|
    | `uuid` | string (uuid) | ✓ | UUID of the instance or volume resource. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `enabled` | boolean | Whether the instance's provider collects instance metrics. |
    | `interval_minutes` | integer | Minutes between reads now, the faster ones included. |
    | `offering_interval_minutes` | integer | Minutes between reads when nobody asked for faster ones. |
    | `faster_until` | string (date-time) |  |
    | `last_polled_at` | string (date-time) |  |
    | `next_poll_at` | string (date-time) | Empty while the instance is not running. |
    | `can_manage` | boolean | Whether the user may ask for faster reads or a read now. |
    | `instance_name` | string | The instance whose reads cover the resource; for a volume, the one it is attached to. Empty for a detached volume. |
    | `instance_resource_uuid` | string (uuid) |  |


=== "Authorization"

    An instance or volume resource whose metrics the caller sees: staff, support, its consumer (a role in its project or organization) or its provider (a role in the offering's organization or service provider, or on the offering). Others get a 404.

---

### Read an instance's metrics now

Refused while the last read, or the last one asked for, is less than five minutes old.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-openstack-instance-metrics/a1b2c3d4-e5f6-7890-abcd-ef1234567890/update_now/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_openstack_instance_metrics import marketplace_openstack_instance_metrics_update_now # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_openstack_instance_metrics_update_now.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_openstack_instance_metrics_update_now`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_openstack_instance_metrics/marketplace_openstack_instance_metrics_update_now.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOpenstackInstanceMetricsUpdateNow } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOpenstackInstanceMetricsUpdateNow({
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

    | Name | Type | Required | Description |
    |---|---|---|---|
    | `uuid` | string (uuid) | ✓ | UUID of the instance or volume resource. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `enabled` | boolean | Whether the instance's provider collects instance metrics. |
    | `interval_minutes` | integer | Minutes between reads now, the faster ones included. |
    | `offering_interval_minutes` | integer | Minutes between reads when nobody asked for faster ones. |
    | `faster_until` | string (date-time) |  |
    | `last_polled_at` | string (date-time) |  |
    | `next_poll_at` | string (date-time) | Empty while the instance is not running. |
    | `can_manage` | boolean | Whether the user may ask for faster reads or a read now. |
    | `instance_name` | string | The instance whose reads cover the resource; for a volume, the one it is attached to. Empty for a detached volume. |
    | `instance_resource_uuid` | string (uuid) |  |


=== "Authorization"

    All of:
    
    - An instance or volume resource whose metrics the caller sees: staff, support, its consumer (a role in its project or organization) or its provider (a role in the offering's organization or service provider, or on the offering). Others get a 404.
    - OPENSTACK_INSTANCE.MANAGE on the project or organization of the instance whose reads cover the resource (for a volume, the instance it is attached to); staff pass.

---

## Other Actions


### Read an instance's metrics faster for a while

Reads the instance now, then every interval_minutes for the given hours, after which the provider's interval applies again. Asked on a volume, it applies to the instance the volume is attached to.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-openstack-instance-metrics/a1b2c3d4-e5f6-7890-abcd-ef1234567890/faster_updates/ \
      Authorization:"Token YOUR_API_TOKEN" \
      interval_minutes=5 \
      hours=123
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.instance_metrics_faster_updates_request import InstanceMetricsFasterUpdatesRequest # (1)
    from waldur_api_client.api.marketplace_openstack_instance_metrics import marketplace_openstack_instance_metrics_faster_updates # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = InstanceMetricsFasterUpdatesRequest(
        interval_minutes=5,
        hours=123
    )
    response = marketplace_openstack_instance_metrics_faster_updates.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`InstanceMetricsFasterUpdatesRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/instance_metrics_faster_updates_request.py)
    2.  **API Source:** [`marketplace_openstack_instance_metrics_faster_updates`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_openstack_instance_metrics/marketplace_openstack_instance_metrics_faster_updates.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOpenstackInstanceMetricsFasterUpdates } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOpenstackInstanceMetricsFasterUpdates({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "interval_minutes": 5,
        "hours": 123
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
    | `uuid` | string (uuid) | ✓ | UUID of the instance or volume resource. |


=== "Request Body (required)"

    | Field | Type | Required |
    |---|---|---|
    | `interval_minutes` | integer | ✓ |
    | `hours` | integer | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `enabled` | boolean | Whether the instance's provider collects instance metrics. |
    | `interval_minutes` | integer | Minutes between reads now, the faster ones included. |
    | `offering_interval_minutes` | integer | Minutes between reads when nobody asked for faster ones. |
    | `faster_until` | string (date-time) |  |
    | `last_polled_at` | string (date-time) |  |
    | `next_poll_at` | string (date-time) | Empty while the instance is not running. |
    | `can_manage` | boolean | Whether the user may ask for faster reads or a read now. |
    | `instance_name` | string | The instance whose reads cover the resource; for a volume, the one it is attached to. Empty for a detached volume. |
    | `instance_resource_uuid` | string (uuid) |  |


=== "Authorization"

    All of:
    
    - An instance or volume resource whose metrics the caller sees: staff, support, its consumer (a role in its project or organization) or its provider (a role in the offering's organization or service provider, or on the offering). Others get a 404.
    - OPENSTACK_INSTANCE.MANAGE on the project or organization of the instance whose reads cover the resource (for a volume, the instance it is attached to); staff pass.

---

### Return an instance to the provider's interval


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-openstack-instance-metrics/a1b2c3d4-e5f6-7890-abcd-ef1234567890/normal_updates/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_openstack_instance_metrics import marketplace_openstack_instance_metrics_normal_updates # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_openstack_instance_metrics_normal_updates.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_openstack_instance_metrics_normal_updates`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_openstack_instance_metrics/marketplace_openstack_instance_metrics_normal_updates.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOpenstackInstanceMetricsNormalUpdates } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOpenstackInstanceMetricsNormalUpdates({
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

    | Name | Type | Required | Description |
    |---|---|---|---|
    | `uuid` | string (uuid) | ✓ | UUID of the instance or volume resource. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `enabled` | boolean | Whether the instance's provider collects instance metrics. |
    | `interval_minutes` | integer | Minutes between reads now, the faster ones included. |
    | `offering_interval_minutes` | integer | Minutes between reads when nobody asked for faster ones. |
    | `faster_until` | string (date-time) |  |
    | `last_polled_at` | string (date-time) |  |
    | `next_poll_at` | string (date-time) | Empty while the instance is not running. |
    | `can_manage` | boolean | Whether the user may ask for faster reads or a read now. |
    | `instance_name` | string | The instance whose reads cover the resource; for a volume, the one it is attached to. Empty for a detached volume. |
    | `instance_resource_uuid` | string (uuid) |  |


=== "Authorization"

    All of:
    
    - An instance or volume resource whose metrics the caller sees: staff, support, its consumer (a role in its project or organization) or its provider (a role in the offering's organization or service provider, or on the offering). Others get a 404.
    - OPENSTACK_INSTANCE.MANAGE on the project or organization of the instance whose reads cover the resource (for a volume, the instance it is attached to); staff pass.

---
