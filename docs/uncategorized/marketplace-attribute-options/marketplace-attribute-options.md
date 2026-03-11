# Marketplace Attribute Options

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-attribute-options/` | [List attribute options](#list-attribute-options) |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-attribute-options/{uuid}/` | [Retrieve an attribute option](#retrieve-an-attribute-option) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-attribute-options/` | [Create an attribute option](#create-an-attribute-option) |
| <span class="http-badge http-put">PUT</span> | `/api/marketplace-attribute-options/{uuid}/` | [Update an attribute option](#update-an-attribute-option) |
| <span class="http-badge http-patch">PATCH</span> | `/api/marketplace-attribute-options/{uuid}/` | [Partially update an attribute option](#partially-update-an-attribute-option) |
| <span class="http-badge http-delete">DELETE</span> | `/api/marketplace-attribute-options/{uuid}/` | [Delete an attribute option](#delete-an-attribute-option) |

---

### List attribute options

Returns a paginated list of options for choice-type attributes. Filter by attribute (URL). Default option is determined by attribute.default.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-attribute-options/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_attribute_options import marketplace_attribute_options_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_attribute_options_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`marketplace_attribute_options_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_attribute_options/marketplace_attribute_options_list.py)

=== "TypeScript"

    ```typescript
    import { marketplaceAttributeOptionsList } from 'waldur-js-client';
    
    try {
      const response = await marketplaceAttributeOptionsList({
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
    | `attribute` | string (uri) | Attribute URL |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `id` | integer |  |
    | `key` | string |  |
    | `title` | string |  |
    | `attribute` | string (uri) |  |
    | `attribute_title` | string |  |
    | `is_default` | boolean | Return True if this option is the default for its attribute. |

---

### Retrieve an attribute option

Returns the details of a specific attribute option.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-attribute-options/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_attribute_options import marketplace_attribute_options_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_attribute_options_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_attribute_options_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_attribute_options/marketplace_attribute_options_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceAttributeOptionsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceAttributeOptionsRetrieve({
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
    | `id` | integer |  |
    | `key` | string |  |
    | `title` | string |  |
    | `attribute` | string (uri) |  |
    | `attribute_title` | string |  |
    | `is_default` | boolean | Return True if this option is the default for its attribute. |

---

### Create an attribute option

Creates a new option for a choice-type attribute. Requires staff permissions.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-attribute-options/ \
      Authorization:"Token YOUR_API_TOKEN" \
      key="ssh-rsa AAAAB3NzaC1yc2EAAA..." \
      title="string-value" \
      attribute="https://api.example.com/api/attribute/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.attribute_option_request import AttributeOptionRequest # (1)
    from waldur_api_client.api.marketplace_attribute_options import marketplace_attribute_options_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = AttributeOptionRequest(
        key="ssh-rsa AAAAB3NzaC1yc2EAAA...",
        title="string-value",
        attribute="https://api.example.com/api/attribute/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    )
    response = marketplace_attribute_options_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`AttributeOptionRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/attribute_option_request.py)
    2.  **API Source:** [`marketplace_attribute_options_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_attribute_options/marketplace_attribute_options_create.py)

=== "TypeScript"

    ```typescript
    import { marketplaceAttributeOptionsCreate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceAttributeOptionsCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "key": "ssh-rsa AAAAB3NzaC1yc2EAAA...",
        "title": "string-value",
        "attribute": "https://api.example.com/api/attribute/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
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
    | `key` | string | ✓ |
    | `title` | string | ✓ |
    | `attribute` | string (uri) | ✓ |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `id` | integer |  |
    | `key` | string |  |
    | `title` | string |  |
    | `attribute` | string (uri) |  |
    | `attribute_title` | string |  |
    | `is_default` | boolean | Return True if this option is the default for its attribute. |

---

### Update an attribute option

Updates an existing attribute option. Requires staff permissions.


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/marketplace-attribute-options/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      key="ssh-rsa AAAAB3NzaC1yc2EAAA..." \
      title="string-value" \
      attribute="https://api.example.com/api/attribute/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.attribute_option_request import AttributeOptionRequest # (1)
    from waldur_api_client.api.marketplace_attribute_options import marketplace_attribute_options_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = AttributeOptionRequest(
        key="ssh-rsa AAAAB3NzaC1yc2EAAA...",
        title="string-value",
        attribute="https://api.example.com/api/attribute/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    )
    response = marketplace_attribute_options_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`AttributeOptionRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/attribute_option_request.py)
    2.  **API Source:** [`marketplace_attribute_options_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_attribute_options/marketplace_attribute_options_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceAttributeOptionsUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceAttributeOptionsUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "key": "ssh-rsa AAAAB3NzaC1yc2EAAA...",
        "title": "string-value",
        "attribute": "https://api.example.com/api/attribute/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
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
    | `key` | string | ✓ |
    | `title` | string | ✓ |
    | `attribute` | string (uri) | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `id` | integer |  |
    | `key` | string |  |
    | `title` | string |  |
    | `attribute` | string (uri) |  |
    | `attribute_title` | string |  |
    | `is_default` | boolean | Return True if this option is the default for its attribute. |

---

### Partially update an attribute option

Partially updates an existing attribute option. To set the default option, PATCH the attribute with default=<option_key>. Requires staff permissions.


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/marketplace-attribute-options/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_attribute_option_request import PatchedAttributeOptionRequest # (1)
    from waldur_api_client.api.marketplace_attribute_options import marketplace_attribute_options_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedAttributeOptionRequest()
    response = marketplace_attribute_options_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedAttributeOptionRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_attribute_option_request.py)
    2.  **API Source:** [`marketplace_attribute_options_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_attribute_options/marketplace_attribute_options_partial_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceAttributeOptionsPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceAttributeOptionsPartialUpdate({
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
    | `key` | string |  |
    | `title` | string |  |
    | `attribute` | string (uri) |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `id` | integer |  |
    | `key` | string |  |
    | `title` | string |  |
    | `attribute` | string (uri) |  |
    | `attribute_title` | string |  |
    | `is_default` | boolean | Return True if this option is the default for its attribute. |

---

### Delete an attribute option

Deletes an attribute option. Requires staff permissions.


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/marketplace-attribute-options/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_attribute_options import marketplace_attribute_options_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_attribute_options_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_attribute_options_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_attribute_options/marketplace_attribute_options_destroy.py)

=== "TypeScript"

    ```typescript
    import { marketplaceAttributeOptionsDestroy } from 'waldur-js-client';
    
    try {
      const response = await marketplaceAttributeOptionsDestroy({
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
