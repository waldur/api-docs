# Access Subnets

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/access-subnets/` | [List access subnets](#list-access-subnets) |
| <span class="http-badge http-get">GET</span> | `/api/access-subnets/{uuid}/` | [Retrieve access subnet](#retrieve-access-subnet) |
| <span class="http-badge http-post">POST</span> | `/api/access-subnets/` | [Create an access subnet](#create-an-access-subnet) |
| <span class="http-badge http-put">PUT</span> | `/api/access-subnets/{uuid}/` | [Update an access subnet](#update-an-access-subnet) |
| <span class="http-badge http-patch">PATCH</span> | `/api/access-subnets/{uuid}/` | [Partially update an access subnet](#partially-update-an-access-subnet) |
| <span class="http-badge http-delete">DELETE</span> | `/api/access-subnets/{uuid}/` | [Delete an access subnet](#delete-an-access-subnet) |
| **Other Actions** | | |
| <span class="http-badge http-get">GET</span> | `/api/access-subnets/resource_impact/` | [Show which resources the access subnets reach](#show-which-resources-the-access-subnets-reach) |

---
## Core CRUD


### List access subnets

Retrieve a list of access subnets. Staff and support users can see all subnets, while other users can only see subnets associated with customers they have a role in.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/access-subnets/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.access_subnets import access_subnets_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = access_subnets_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`access_subnets_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/access_subnets/access_subnets_list.py)

=== "TypeScript"

    ```typescript
    import { accessSubnetsList } from 'waldur-js-client';
    
    try {
      const response = await accessSubnetsList({
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
    | `applies_to_portal` | boolean | Applies to portal |
    | `customer` | string (uri) | Customer URL |
    | `customer_uuid` | string (uuid) | Customer UUID |
    | `description` | string | Description |
    | `inet` | string | Inet |
    | `is_staff_managed` | boolean | Is staff managed |
    | `o` | string | Which field to use when ordering the results. |
    | `offering_uuid` | string (uuid) | Offering UUID |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `inet` | string |  |
    | `description` | string |  |
    | `customer` | string (uri) |  |
    | `applies_to_portal` | boolean | Whether this network may sign in to the portal on behalf of the organization. Off by default: any portal-scoped entry restricts sign-in for everyone in the organization. |
    | `offerings` | array of string (uuid)s | UUIDs of offerings this network may reach. Only offerings the organization consumes and that enable access subnets are accepted. |
    | `scoped_offerings` | array of objects |  |
    | `scoped_offerings.uuid` | string |  |
    | `scoped_offerings.name` | string |  |
    | `scoped_offerings.has_live_resources` | boolean |  |
    | `is_staff_managed` | boolean | Set when staff created the entry. Such entries are read-only for everyone else, regardless of mask width. |

---

### Retrieve access subnet

Fetch the details of a specific access subnet by its UUID.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/access-subnets/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.access_subnets import access_subnets_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = access_subnets_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`access_subnets_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/access_subnets/access_subnets_retrieve.py)

=== "TypeScript"

    ```typescript
    import { accessSubnetsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await accessSubnetsRetrieve({
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
    | `inet` | string |  |
    | `description` | string |  |
    | `customer` | string (uri) |  |
    | `applies_to_portal` | boolean | Whether this network may sign in to the portal on behalf of the organization. Off by default: any portal-scoped entry restricts sign-in for everyone in the organization. |
    | `offerings` | array of string (uuid)s | UUIDs of offerings this network may reach. Only offerings the organization consumes and that enable access subnets are accepted. |
    | `scoped_offerings` | array of objects |  |
    | `scoped_offerings.uuid` | string |  |
    | `scoped_offerings.name` | string |  |
    | `scoped_offerings.has_live_resources` | boolean |  |
    | `is_staff_managed` | boolean | Set when staff created the entry. Such entries are read-only for everyone else, regardless of mask width. |

---

### Create an access subnet

Create a new access subnet for a customer.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/access-subnets/ \
      Authorization:"Token YOUR_API_TOKEN" \
      inet="string-value" \
      customer="https://api.example.com/api/customer/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.access_subnet_request import AccessSubnetRequest # (1)
    from waldur_api_client.api.access_subnets import access_subnets_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = AccessSubnetRequest(
        inet="string-value",
        customer="https://api.example.com/api/customer/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    )
    response = access_subnets_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`AccessSubnetRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/access_subnet_request.py)
    2.  **API Source:** [`access_subnets_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/access_subnets/access_subnets_create.py)

=== "TypeScript"

    ```typescript
    import { accessSubnetsCreate } from 'waldur-js-client';
    
    try {
      const response = await accessSubnetsCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "inet": "string-value",
        "customer": "https://api.example.com/api/customer/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
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
    | `inet` | string | ✓ |  |
    | `description` | string |  |  |
    | `customer` | string (uri) | ✓ |  |
    | `applies_to_portal` | boolean |  | Whether this network may sign in to the portal on behalf of the organization. Off by default: any portal-scoped entry restricts sign-in for everyone in the organization. |
    | `offerings` | array of string (uuid)s |  | UUIDs of offerings this network may reach. Only offerings the organization consumes and that enable access subnets are accepted. |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `inet` | string |  |
    | `description` | string |  |
    | `customer` | string (uri) |  |
    | `applies_to_portal` | boolean | Whether this network may sign in to the portal on behalf of the organization. Off by default: any portal-scoped entry restricts sign-in for everyone in the organization. |
    | `offerings` | array of string (uuid)s | UUIDs of offerings this network may reach. Only offerings the organization consumes and that enable access subnets are accepted. |
    | `scoped_offerings` | array of objects |  |
    | `scoped_offerings.uuid` | string |  |
    | `scoped_offerings.name` | string |  |
    | `scoped_offerings.has_live_resources` | boolean |  |
    | `is_staff_managed` | boolean | Set when staff created the entry. Such entries are read-only for everyone else, regardless of mask width. |

---

### Update an access subnet

Update an existing access subnet.


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/access-subnets/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      inet="string-value" \
      customer="https://api.example.com/api/customer/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.access_subnet_request import AccessSubnetRequest # (1)
    from waldur_api_client.api.access_subnets import access_subnets_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = AccessSubnetRequest(
        inet="string-value",
        customer="https://api.example.com/api/customer/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    )
    response = access_subnets_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`AccessSubnetRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/access_subnet_request.py)
    2.  **API Source:** [`access_subnets_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/access_subnets/access_subnets_update.py)

=== "TypeScript"

    ```typescript
    import { accessSubnetsUpdate } from 'waldur-js-client';
    
    try {
      const response = await accessSubnetsUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "inet": "string-value",
        "customer": "https://api.example.com/api/customer/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
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
    | `inet` | string | ✓ |  |
    | `description` | string |  |  |
    | `customer` | string (uri) | ✓ |  |
    | `applies_to_portal` | boolean |  | Whether this network may sign in to the portal on behalf of the organization. Off by default: any portal-scoped entry restricts sign-in for everyone in the organization. |
    | `offerings` | array of string (uuid)s |  | UUIDs of offerings this network may reach. Only offerings the organization consumes and that enable access subnets are accepted. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `inet` | string |  |
    | `description` | string |  |
    | `customer` | string (uri) |  |
    | `applies_to_portal` | boolean | Whether this network may sign in to the portal on behalf of the organization. Off by default: any portal-scoped entry restricts sign-in for everyone in the organization. |
    | `offerings` | array of string (uuid)s | UUIDs of offerings this network may reach. Only offerings the organization consumes and that enable access subnets are accepted. |
    | `scoped_offerings` | array of objects |  |
    | `scoped_offerings.uuid` | string |  |
    | `scoped_offerings.name` | string |  |
    | `scoped_offerings.has_live_resources` | boolean |  |
    | `is_staff_managed` | boolean | Set when staff created the entry. Such entries are read-only for everyone else, regardless of mask width. |

---

### Partially update an access subnet

Partially update an existing access subnet.


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/access-subnets/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_access_subnet_request import PatchedAccessSubnetRequest # (1)
    from waldur_api_client.api.access_subnets import access_subnets_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedAccessSubnetRequest()
    response = access_subnets_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedAccessSubnetRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_access_subnet_request.py)
    2.  **API Source:** [`access_subnets_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/access_subnets/access_subnets_partial_update.py)

=== "TypeScript"

    ```typescript
    import { accessSubnetsPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await accessSubnetsPartialUpdate({
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
    | `inet` | string |  |  |
    | `description` | string |  |  |
    | `applies_to_portal` | boolean |  | Whether this network may sign in to the portal on behalf of the organization. Off by default: any portal-scoped entry restricts sign-in for everyone in the organization. |
    | `offerings` | array of string (uuid)s |  | UUIDs of offerings this network may reach. Only offerings the organization consumes and that enable access subnets are accepted. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `inet` | string |  |
    | `description` | string |  |
    | `customer` | string (uri) |  |
    | `applies_to_portal` | boolean | Whether this network may sign in to the portal on behalf of the organization. Off by default: any portal-scoped entry restricts sign-in for everyone in the organization. |
    | `offerings` | array of string (uuid)s | UUIDs of offerings this network may reach. Only offerings the organization consumes and that enable access subnets are accepted. |
    | `scoped_offerings` | array of objects |  |
    | `scoped_offerings.uuid` | string |  |
    | `scoped_offerings.name` | string |  |
    | `scoped_offerings.has_live_resources` | boolean |  |
    | `is_staff_managed` | boolean | Set when staff created the entry. Such entries are read-only for everyone else, regardless of mask width. |

---

### Delete an access subnet

Delete an existing access subnet.


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/access-subnets/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.access_subnets import access_subnets_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = access_subnets_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`access_subnets_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/access_subnets/access_subnets_destroy.py)

=== "TypeScript"

    ```typescript
    import { accessSubnetsDestroy } from 'waldur-js-client';
    
    try {
      const response = await accessSubnetsDestroy({
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


### Show which resources the access subnets reach

For each of the organization's live resources of an offering that supports access subnets, the addresses that may reach it, where each came from, and whether the list is enforced or merely advisory. Resources of offerings without access subnet support are omitted: no allow-list can apply to them. Pass access_subnet_uuid to narrow it to the resources one address reaches.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/access-subnets/resource_impact/ \
      Authorization:"Token YOUR_API_TOKEN" \
      customer_uuid=="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.access_subnets import access_subnets_resource_impact_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = access_subnets_resource_impact_retrieve.sync(
        client=client,
        customer_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`access_subnets_resource_impact_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/access_subnets/access_subnets_resource_impact_retrieve.py)

=== "TypeScript"

    ```typescript
    import { accessSubnetsResourceImpactRetrieve } from 'waldur-js-client';
    
    try {
      const response = await accessSubnetsResourceImpactRetrieve({
      auth: "Token YOUR_API_TOKEN",
      query: {
        "customer_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Query Parameters"

    | Name | Type | Required | Description |
    |---|---|---|---|
    | `access_subnet_uuid` | string (uuid) |  | Limit to the resources this one address reaches. |
    | `customer_uuid` | string (uuid) | ✓ | Organization whose resources to report on. |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `resources` | array of objects |
    | `resources.resource_uuid` | string |
    | `resources.resource_name` | string |
    | `resources.project_name` | string |
    | `resources.offering_uuid` | string |
    | `resources.offering_name` | string |
    | `resources.concealment_enabled` | boolean |
    | `resources.unrestricted` | boolean |
    | `resources.addresses` | array of objects |
    | `resources.addresses.inet` | string |
    | `resources.addresses.description` | string |
    | `resources.addresses.source` | string |
    | `resources.addresses.is_staff_managed` | boolean |
    | `resources.packed` | array of strings |

---
