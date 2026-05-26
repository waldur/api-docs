# Marketplace Offering Profiles

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-offering-profiles/` | [List Marketplace Offering Profiles](#list-marketplace-offering-profiles) |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-offering-profiles/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-offering-profiles/` | [Create](#create) |
| <span class="http-badge http-put">PUT</span> | `/api/marketplace-offering-profiles/{uuid}/` | [Update](#update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/marketplace-offering-profiles/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-delete">DELETE</span> | `/api/marketplace-offering-profiles/{uuid}/` | [Delete](#delete) |
| **Other Actions** | | |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-offering-profiles/{uuid}/add_role/` | [Add role](#add-role) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-offering-profiles/{uuid}/remove_role/` | [Remove role](#remove-role) |

---
## Core CRUD


### List Marketplace Offering Profiles


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-offering-profiles/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_offering_profiles import marketplace_offering_profiles_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_offering_profiles_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`marketplace_offering_profiles_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_profiles/marketplace_offering_profiles_list.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingProfilesList } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingProfilesList({
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

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `name` | string |
    | `description` | string |
    | `roles` | array of objects |
    | `roles.uuid` | string |
    | `roles.name` | string |
    | `roles.content_type` | string |
    | `roles.description` | string |
    | `offerings_count` | integer |
    | `created` | string (date-time) |
    | `modified` | string (date-time) |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-offering-profiles/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_offering_profiles import marketplace_offering_profiles_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_offering_profiles_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_offering_profiles_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_profiles/marketplace_offering_profiles_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingProfilesRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingProfilesRetrieve({
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
    | `uuid` | string (uuid) |
    | `name` | string |
    | `description` | string |
    | `roles` | array of objects |
    | `roles.uuid` | string |
    | `roles.name` | string |
    | `roles.content_type` | string |
    | `roles.description` | string |
    | `offerings_count` | integer |
    | `created` | string (date-time) |
    | `modified` | string (date-time) |

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-offering-profiles/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-marketplace-offering-profile"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.offering_profile_request import OfferingProfileRequest # (1)
    from waldur_api_client.api.marketplace_offering_profiles import marketplace_offering_profiles_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = OfferingProfileRequest(
        name="my-awesome-marketplace-offering-profile"
    )
    response = marketplace_offering_profiles_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`OfferingProfileRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/offering_profile_request.py)
    2.  **API Source:** [`marketplace_offering_profiles_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_profiles/marketplace_offering_profiles_create.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingProfilesCreate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingProfilesCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "name": "my-awesome-marketplace-offering-profile"
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


=== "Responses"

    **`201`** - 
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `name` | string |
    | `description` | string |
    | `roles` | array of objects |
    | `roles.uuid` | string |
    | `roles.name` | string |
    | `roles.content_type` | string |
    | `roles.description` | string |
    | `offerings_count` | integer |
    | `created` | string (date-time) |
    | `modified` | string (date-time) |

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/marketplace-offering-profiles/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-marketplace-offering-profile"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.offering_profile_request import OfferingProfileRequest # (1)
    from waldur_api_client.api.marketplace_offering_profiles import marketplace_offering_profiles_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = OfferingProfileRequest(
        name="my-awesome-marketplace-offering-profile"
    )
    response = marketplace_offering_profiles_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`OfferingProfileRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/offering_profile_request.py)
    2.  **API Source:** [`marketplace_offering_profiles_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_profiles/marketplace_offering_profiles_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingProfilesUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingProfilesUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "name": "my-awesome-marketplace-offering-profile"
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


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `name` | string |
    | `description` | string |
    | `roles` | array of objects |
    | `roles.uuid` | string |
    | `roles.name` | string |
    | `roles.content_type` | string |
    | `roles.description` | string |
    | `offerings_count` | integer |
    | `created` | string (date-time) |
    | `modified` | string (date-time) |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/marketplace-offering-profiles/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_offering_profile_request import PatchedOfferingProfileRequest # (1)
    from waldur_api_client.api.marketplace_offering_profiles import marketplace_offering_profiles_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedOfferingProfileRequest()
    response = marketplace_offering_profiles_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedOfferingProfileRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_offering_profile_request.py)
    2.  **API Source:** [`marketplace_offering_profiles_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_profiles/marketplace_offering_profiles_partial_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingProfilesPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingProfilesPartialUpdate({
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


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `name` | string |
    | `description` | string |
    | `roles` | array of objects |
    | `roles.uuid` | string |
    | `roles.name` | string |
    | `roles.content_type` | string |
    | `roles.description` | string |
    | `offerings_count` | integer |
    | `created` | string (date-time) |
    | `modified` | string (date-time) |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/marketplace-offering-profiles/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_offering_profiles import marketplace_offering_profiles_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_offering_profiles_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_offering_profiles_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_profiles/marketplace_offering_profiles_destroy.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingProfilesDestroy } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingProfilesDestroy({
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


### Add role


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-offering-profiles/a1b2c3d4-e5f6-7890-abcd-ef1234567890/add_role/ \
      Authorization:"Token YOUR_API_TOKEN" \
      role="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.offering_profile_role_assign_request import OfferingProfileRoleAssignRequest # (1)
    from waldur_api_client.api.marketplace_offering_profiles import marketplace_offering_profiles_add_role # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = OfferingProfileRoleAssignRequest(
        role="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = marketplace_offering_profiles_add_role.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`OfferingProfileRoleAssignRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/offering_profile_role_assign_request.py)
    2.  **API Source:** [`marketplace_offering_profiles_add_role`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_profiles/marketplace_offering_profiles_add_role.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingProfilesAddRole } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingProfilesAddRole({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "role": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `role` | string (uuid) | ✓ | Role UUID to add or remove. |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `name` | string |
    | `description` | string |
    | `roles` | array of objects |
    | `roles.uuid` | string |
    | `roles.name` | string |
    | `roles.content_type` | string |
    | `roles.description` | string |
    | `offerings_count` | integer |
    | `created` | string (date-time) |
    | `modified` | string (date-time) |

---

### Remove role


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-offering-profiles/a1b2c3d4-e5f6-7890-abcd-ef1234567890/remove_role/ \
      Authorization:"Token YOUR_API_TOKEN" \
      role="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.offering_profile_role_assign_request import OfferingProfileRoleAssignRequest # (1)
    from waldur_api_client.api.marketplace_offering_profiles import marketplace_offering_profiles_remove_role # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = OfferingProfileRoleAssignRequest(
        role="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = marketplace_offering_profiles_remove_role.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`OfferingProfileRoleAssignRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/offering_profile_role_assign_request.py)
    2.  **API Source:** [`marketplace_offering_profiles_remove_role`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_profiles/marketplace_offering_profiles_remove_role.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingProfilesRemoveRole } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingProfilesRemoveRole({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "role": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `role` | string (uuid) | ✓ | Role UUID to add or remove. |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `name` | string |
    | `description` | string |
    | `roles` | array of objects |
    | `roles.uuid` | string |
    | `roles.name` | string |
    | `roles.content_type` | string |
    | `roles.description` | string |
    | `offerings_count` | integer |
    | `created` | string (date-time) |
    | `modified` | string (date-time) |

---
