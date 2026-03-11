# Marketplace Attributes

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-attributes/` | [List attributes](#list-attributes) |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-attributes/{uuid}/` | [Retrieve an attribute](#retrieve-an-attribute) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-attributes/` | [Create an attribute](#create-an-attribute) |
| <span class="http-badge http-put">PUT</span> | `/api/marketplace-attributes/{uuid}/` | [Update an attribute](#update-an-attribute) |
| <span class="http-badge http-patch">PATCH</span> | `/api/marketplace-attributes/{uuid}/` | [Partially update an attribute](#partially-update-an-attribute) |
| <span class="http-badge http-delete">DELETE</span> | `/api/marketplace-attributes/{uuid}/` | [Delete an attribute](#delete-an-attribute) |

---

### List attributes

Returns a paginated list of all attributes. Attributes define form fields within section. Filter by section (URL).


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-attributes/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_attributes import marketplace_attributes_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_attributes_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`marketplace_attributes_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_attributes/marketplace_attributes_list.py)

=== "TypeScript"

    ```typescript
    import { marketplaceAttributesList } from 'waldur-js-client';
    
    try {
      const response = await marketplaceAttributesList({
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
    | `section` | string (uri) | Section URL |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `key` | string |  |
    | `created` | string (date-time) |  |
    | `title` | string |  |
    | `section` | string (uri) |  |
    | `section_title` | string |  |
    | `type` | string | <br>_Enum: `boolean`, `string`, `text`, `integer`, `choice`, `list`_ |
    | `required` | boolean | A value must be provided for the attribute. |
    | `default` | any |  |

---

### Retrieve an attribute

Returns the details of a specific attribute, identified by its UUID.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-attributes/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_attributes import marketplace_attributes_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_attributes_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_attributes_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_attributes/marketplace_attributes_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceAttributesRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceAttributesRetrieve({
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
    | `key` | string |  |
    | `created` | string (date-time) |  |
    | `title` | string |  |
    | `section` | string (uri) |  |
    | `section_title` | string |  |
    | `type` | string | <br>_Enum: `boolean`, `string`, `text`, `integer`, `choice`, `list`_ |
    | `required` | boolean | A value must be provided for the attribute. |
    | `default` | any |  |

---

### Create an attribute

Creates a new attribute within a section. Requires staff permissions.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-attributes/ \
      Authorization:"Token YOUR_API_TOKEN" \
      key="ssh-rsa AAAAB3NzaC1yc2EAAA..." \
      title="string-value" \
      section="https://api.example.com/api/section/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      type="boolean"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.attribute_request import AttributeRequest # (1)
    from waldur_api_client.api.marketplace_attributes import marketplace_attributes_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = AttributeRequest(
        key="ssh-rsa AAAAB3NzaC1yc2EAAA...",
        title="string-value",
        section="https://api.example.com/api/section/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        type="boolean"
    )
    response = marketplace_attributes_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`AttributeRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/attribute_request.py)
    2.  **API Source:** [`marketplace_attributes_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_attributes/marketplace_attributes_create.py)

=== "TypeScript"

    ```typescript
    import { marketplaceAttributesCreate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceAttributesCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "key": "ssh-rsa AAAAB3NzaC1yc2EAAA...",
        "title": "string-value",
        "section": "https://api.example.com/api/section/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "type": "boolean"
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
    | `key` | string | ✓ |  |
    | `title` | string | ✓ |  |
    | `section` | string (uri) | ✓ |  |
    | `type` | string | ✓ | <br>_Enum: `boolean`, `string`, `text`, `integer`, `choice`, `list`_ |
    | `required` | boolean |  | A value must be provided for the attribute. |
    | `default` | any |  |  |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `key` | string |  |
    | `created` | string (date-time) |  |
    | `title` | string |  |
    | `section` | string (uri) |  |
    | `section_title` | string |  |
    | `type` | string | <br>_Enum: `boolean`, `string`, `text`, `integer`, `choice`, `list`_ |
    | `required` | boolean | A value must be provided for the attribute. |
    | `default` | any |  |

---

### Update an attribute

Updates an existing attribute. Requires staff permissions.


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/marketplace-attributes/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      key="ssh-rsa AAAAB3NzaC1yc2EAAA..." \
      title="string-value" \
      section="https://api.example.com/api/section/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      type="boolean"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.attribute_request import AttributeRequest # (1)
    from waldur_api_client.api.marketplace_attributes import marketplace_attributes_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = AttributeRequest(
        key="ssh-rsa AAAAB3NzaC1yc2EAAA...",
        title="string-value",
        section="https://api.example.com/api/section/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        type="boolean"
    )
    response = marketplace_attributes_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`AttributeRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/attribute_request.py)
    2.  **API Source:** [`marketplace_attributes_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_attributes/marketplace_attributes_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceAttributesUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceAttributesUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "key": "ssh-rsa AAAAB3NzaC1yc2EAAA...",
        "title": "string-value",
        "section": "https://api.example.com/api/section/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "type": "boolean"
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
    | `key` | string | ✓ |  |
    | `title` | string | ✓ |  |
    | `section` | string (uri) | ✓ |  |
    | `type` | string | ✓ | <br>_Enum: `boolean`, `string`, `text`, `integer`, `choice`, `list`_ |
    | `required` | boolean |  | A value must be provided for the attribute. |
    | `default` | any |  |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `key` | string |  |
    | `created` | string (date-time) |  |
    | `title` | string |  |
    | `section` | string (uri) |  |
    | `section_title` | string |  |
    | `type` | string | <br>_Enum: `boolean`, `string`, `text`, `integer`, `choice`, `list`_ |
    | `required` | boolean | A value must be provided for the attribute. |
    | `default` | any |  |

---

### Partially update an attribute

Partially updates an existing attribute. Requires staff permissions.


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/marketplace-attributes/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_attribute_request import PatchedAttributeRequest # (1)
    from waldur_api_client.api.marketplace_attributes import marketplace_attributes_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedAttributeRequest()
    response = marketplace_attributes_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedAttributeRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_attribute_request.py)
    2.  **API Source:** [`marketplace_attributes_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_attributes/marketplace_attributes_partial_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceAttributesPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceAttributesPartialUpdate({
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
    | `key` | string |  |  |
    | `title` | string |  |  |
    | `section` | string (uri) |  |  |
    | `type` | string |  | <br>_Enum: `boolean`, `string`, `text`, `integer`, `choice`, `list`_ |
    | `required` | boolean |  | A value must be provided for the attribute. |
    | `default` | any |  |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `key` | string |  |
    | `created` | string (date-time) |  |
    | `title` | string |  |
    | `section` | string (uri) |  |
    | `section_title` | string |  |
    | `type` | string | <br>_Enum: `boolean`, `string`, `text`, `integer`, `choice`, `list`_ |
    | `required` | boolean | A value must be provided for the attribute. |
    | `default` | any |  |

---

### Delete an attribute

Deletes an attribute. Requires staff permissions.


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/marketplace-attributes/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_attributes import marketplace_attributes_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_attributes_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_attributes_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_attributes/marketplace_attributes_destroy.py)

=== "TypeScript"

    ```typescript
    import { marketplaceAttributesDestroy } from 'waldur-js-client';
    
    try {
      const response = await marketplaceAttributesDestroy({
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
