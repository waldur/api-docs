# Openportal Project Template

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/openportal-project-template/` | [List Openportal Project Template](#list-openportal-project-template) |
| <span class="http-badge http-get">GET</span> | `/api/openportal-project-template/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/openportal-project-template/` | [Create ProjectTemplate object](#create-projecttemplate-object) |
| <span class="http-badge http-put">PUT</span> | `/api/openportal-project-template/{uuid}/` | [Update ProjectTemplate object (full update)](#update-projecttemplate-object-full-update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/openportal-project-template/{uuid}/` | [Partially update ProjectTemplate object](#partially-update-projecttemplate-object) |
| <span class="http-badge http-delete">DELETE</span> | `/api/openportal-project-template/{uuid}/` | [Delete](#delete) |
| **Other Actions** | | |
| <span class="http-badge http-delete">DELETE</span> | `/api/openportal-project-template/{uuid}/delete/` | [Delete ProjectTemplate object](#delete-projecttemplate-object) |

---
## Core CRUD


### List Openportal Project Template


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openportal-project-template/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openportal_project_template import openportal_project_template_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openportal_project_template_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`openportal_project_template_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal_project_template/openportal_project_template_list.py)

=== "TypeScript"

    ```typescript
    import { openportalProjectTemplateList } from 'waldur-js-client';
    
    try {
      const response = await openportalProjectTemplateList({
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
    | `name` | string |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `portal` | string |  |
    | `uuid` | string (uuid) |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `offering` | string | The offering for which this template applies. |
    | `provider` | string (uri) |  |
    | `provider_data` | any |  |
    | `portal` | string |  |
    | `key` | string | The key that is used to authenticate requests for this class. |
    | `customer` | string (uri) |  |
    | `customer_data` | any |  |
    | `shortname` | string |  |
    | `offerings` | array of string (uri)s |  |
    | `offerings_data` | array of objects |  |
    | `offerings_data.name` | string |  |
    | `offerings_data.uuid` | string (uuid) |  |
    | `approval_limit` | string (decimal) | The credit limit beyond which requests need to be approved by a local admin. If this is None, then no local approval is required. If this is set to 0, then all requests (including creating the project) need to be approved. |
    | `max_credit_limit` | string (decimal) | The maximum credit limit for any projects created in this class. Any requests beyond this limit are automatically rejected. If this is None, then no maximum limit is set. If this is set to 0, then no projects can be created in this class. |
    | `allocation_units_mapping` | any | The mapping of credits to allocation units, i.e. how many allocation units to award per credit allocated. |
    | `role_mapping` | any | The mapping of role names from the remote portal to role information in this portal for users in projects created in this class. |
    | `role_mapping_data` | object (free-form) | Serialize the role mapping dictionary returned by get_role_mapping() |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/openportal-project-template/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openportal_project_template import openportal_project_template_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openportal_project_template_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openportal_project_template_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal_project_template/openportal_project_template_retrieve.py)

=== "TypeScript"

    ```typescript
    import { openportalProjectTemplateRetrieve } from 'waldur-js-client';
    
    try {
      const response = await openportalProjectTemplateRetrieve({
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
    | `name` | string |  |
    | `offering` | string | The offering for which this template applies. |
    | `provider` | string (uri) |  |
    | `provider_data` | any |  |
    | `portal` | string |  |
    | `key` | string | The key that is used to authenticate requests for this class. |
    | `customer` | string (uri) |  |
    | `customer_data` | any |  |
    | `shortname` | string |  |
    | `offerings` | array of string (uri)s |  |
    | `offerings_data` | array of objects |  |
    | `offerings_data.name` | string |  |
    | `offerings_data.uuid` | string (uuid) |  |
    | `approval_limit` | string (decimal) | The credit limit beyond which requests need to be approved by a local admin. If this is None, then no local approval is required. If this is set to 0, then all requests (including creating the project) need to be approved. |
    | `max_credit_limit` | string (decimal) | The maximum credit limit for any projects created in this class. Any requests beyond this limit are automatically rejected. If this is None, then no maximum limit is set. If this is set to 0, then no projects can be created in this class. |
    | `allocation_units_mapping` | any | The mapping of credits to allocation units, i.e. how many allocation units to award per credit allocated. |
    | `role_mapping` | any | The mapping of role names from the remote portal to role information in this portal for users in projects created in this class. |
    | `role_mapping_data` | object (free-form) | Serialize the role mapping dictionary returned by get_role_mapping() |

---

### Create ProjectTemplate object

Create ProjectTemplate object


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/openportal-project-template/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-openportal-project-template" \
      provider="https://api.example.com/api/provider/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      portal="string-value" \
      customer="https://api.example.com/api/customer/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      offerings:='[]'
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.project_template_request import ProjectTemplateRequest # (1)
    from waldur_api_client.api.openportal_project_template import openportal_project_template_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ProjectTemplateRequest(
        name="my-awesome-openportal-project-template",
        provider="https://api.example.com/api/provider/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        portal="string-value",
        customer="https://api.example.com/api/customer/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        offerings=[]
    )
    response = openportal_project_template_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ProjectTemplateRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/project_template_request.py)
    2.  **API Source:** [`openportal_project_template_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal_project_template/openportal_project_template_create.py)

=== "TypeScript"

    ```typescript
    import { openportalProjectTemplateCreate } from 'waldur-js-client';
    
    try {
      const response = await openportalProjectTemplateCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "name": "my-awesome-openportal-project-template",
        "provider": "https://api.example.com/api/provider/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "portal": "string-value",
        "customer": "https://api.example.com/api/customer/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "offerings": []
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
    | `offering` | string |  | The offering for which this template applies. |
    | `provider` | string (uri) | ✓ |  |
    | `portal` | string | ✓ |  |
    | `key` | string |  | The key that is used to authenticate requests for this class. |
    | `customer` | string (uri) | ✓ |  |
    | `shortname` | string |  |  |
    | `offerings` | array of string (uri)s | ✓ |  |
    | `approval_limit` | string (decimal) |  | The credit limit beyond which requests need to be approved by a local admin. If this is None, then no local approval is required. If this is set to 0, then all requests (including creating the project) need to be approved. |
    | `max_credit_limit` | string (decimal) |  | The maximum credit limit for any projects created in this class. Any requests beyond this limit are automatically rejected. If this is None, then no maximum limit is set. If this is set to 0, then no projects can be created in this class. |
    | `allocation_units_mapping` | any |  | The mapping of credits to allocation units, i.e. how many allocation units to award per credit allocated. |
    | `role_mapping` | any |  | The mapping of role names from the remote portal to role information in this portal for users in projects created in this class. |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `offering` | string | The offering for which this template applies. |
    | `provider` | string (uri) |  |
    | `provider_data` | any |  |
    | `portal` | string |  |
    | `key` | string | The key that is used to authenticate requests for this class. |
    | `customer` | string (uri) |  |
    | `customer_data` | any |  |
    | `shortname` | string |  |
    | `offerings` | array of string (uri)s |  |
    | `offerings_data` | array of objects |  |
    | `offerings_data.name` | string |  |
    | `offerings_data.uuid` | string (uuid) |  |
    | `approval_limit` | string (decimal) | The credit limit beyond which requests need to be approved by a local admin. If this is None, then no local approval is required. If this is set to 0, then all requests (including creating the project) need to be approved. |
    | `max_credit_limit` | string (decimal) | The maximum credit limit for any projects created in this class. Any requests beyond this limit are automatically rejected. If this is None, then no maximum limit is set. If this is set to 0, then no projects can be created in this class. |
    | `allocation_units_mapping` | any | The mapping of credits to allocation units, i.e. how many allocation units to award per credit allocated. |
    | `role_mapping` | any | The mapping of role names from the remote portal to role information in this portal for users in projects created in this class. |
    | `role_mapping_data` | object (free-form) | Serialize the role mapping dictionary returned by get_role_mapping() |

---

### Update ProjectTemplate object (full update)

Update ProjectTemplate object (full update)


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/openportal-project-template/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-openportal-project-template" \
      provider="https://api.example.com/api/provider/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      portal="string-value" \
      customer="https://api.example.com/api/customer/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      offerings:='[]'
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.project_template_request import ProjectTemplateRequest # (1)
    from waldur_api_client.api.openportal_project_template import openportal_project_template_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ProjectTemplateRequest(
        name="my-awesome-openportal-project-template",
        provider="https://api.example.com/api/provider/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        portal="string-value",
        customer="https://api.example.com/api/customer/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        offerings=[]
    )
    response = openportal_project_template_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ProjectTemplateRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/project_template_request.py)
    2.  **API Source:** [`openportal_project_template_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal_project_template/openportal_project_template_update.py)

=== "TypeScript"

    ```typescript
    import { openportalProjectTemplateUpdate } from 'waldur-js-client';
    
    try {
      const response = await openportalProjectTemplateUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "name": "my-awesome-openportal-project-template",
        "provider": "https://api.example.com/api/provider/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "portal": "string-value",
        "customer": "https://api.example.com/api/customer/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "offerings": []
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
    | `name` | string | ✓ |  |
    | `offering` | string |  | The offering for which this template applies. |
    | `provider` | string (uri) | ✓ |  |
    | `portal` | string | ✓ |  |
    | `key` | string |  | The key that is used to authenticate requests for this class. |
    | `customer` | string (uri) | ✓ |  |
    | `shortname` | string |  |  |
    | `offerings` | array of string (uri)s | ✓ |  |
    | `approval_limit` | string (decimal) |  | The credit limit beyond which requests need to be approved by a local admin. If this is None, then no local approval is required. If this is set to 0, then all requests (including creating the project) need to be approved. |
    | `max_credit_limit` | string (decimal) |  | The maximum credit limit for any projects created in this class. Any requests beyond this limit are automatically rejected. If this is None, then no maximum limit is set. If this is set to 0, then no projects can be created in this class. |
    | `allocation_units_mapping` | any |  | The mapping of credits to allocation units, i.e. how many allocation units to award per credit allocated. |
    | `role_mapping` | any |  | The mapping of role names from the remote portal to role information in this portal for users in projects created in this class. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `offering` | string | The offering for which this template applies. |
    | `provider` | string (uri) |  |
    | `provider_data` | any |  |
    | `portal` | string |  |
    | `key` | string | The key that is used to authenticate requests for this class. |
    | `customer` | string (uri) |  |
    | `customer_data` | any |  |
    | `shortname` | string |  |
    | `offerings` | array of string (uri)s |  |
    | `offerings_data` | array of objects |  |
    | `offerings_data.name` | string |  |
    | `offerings_data.uuid` | string (uuid) |  |
    | `approval_limit` | string (decimal) | The credit limit beyond which requests need to be approved by a local admin. If this is None, then no local approval is required. If this is set to 0, then all requests (including creating the project) need to be approved. |
    | `max_credit_limit` | string (decimal) | The maximum credit limit for any projects created in this class. Any requests beyond this limit are automatically rejected. If this is None, then no maximum limit is set. If this is set to 0, then no projects can be created in this class. |
    | `allocation_units_mapping` | any | The mapping of credits to allocation units, i.e. how many allocation units to award per credit allocated. |
    | `role_mapping` | any | The mapping of role names from the remote portal to role information in this portal for users in projects created in this class. |
    | `role_mapping_data` | object (free-form) | Serialize the role mapping dictionary returned by get_role_mapping() |

---

### Partially update ProjectTemplate object

Partially update ProjectTemplate object


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/openportal-project-template/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_project_template_request import PatchedProjectTemplateRequest # (1)
    from waldur_api_client.api.openportal_project_template import openportal_project_template_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedProjectTemplateRequest()
    response = openportal_project_template_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedProjectTemplateRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_project_template_request.py)
    2.  **API Source:** [`openportal_project_template_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal_project_template/openportal_project_template_partial_update.py)

=== "TypeScript"

    ```typescript
    import { openportalProjectTemplatePartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await openportalProjectTemplatePartialUpdate({
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
    | `offering` | string |  | The offering for which this template applies. |
    | `provider` | string (uri) |  |  |
    | `portal` | string |  |  |
    | `key` | string |  | The key that is used to authenticate requests for this class. |
    | `customer` | string (uri) |  |  |
    | `shortname` | string |  |  |
    | `offerings` | array of string (uri)s |  |  |
    | `approval_limit` | string (decimal) |  | The credit limit beyond which requests need to be approved by a local admin. If this is None, then no local approval is required. If this is set to 0, then all requests (including creating the project) need to be approved. |
    | `max_credit_limit` | string (decimal) |  | The maximum credit limit for any projects created in this class. Any requests beyond this limit are automatically rejected. If this is None, then no maximum limit is set. If this is set to 0, then no projects can be created in this class. |
    | `allocation_units_mapping` | any |  | The mapping of credits to allocation units, i.e. how many allocation units to award per credit allocated. |
    | `role_mapping` | any |  | The mapping of role names from the remote portal to role information in this portal for users in projects created in this class. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `offering` | string | The offering for which this template applies. |
    | `provider` | string (uri) |  |
    | `provider_data` | any |  |
    | `portal` | string |  |
    | `key` | string | The key that is used to authenticate requests for this class. |
    | `customer` | string (uri) |  |
    | `customer_data` | any |  |
    | `shortname` | string |  |
    | `offerings` | array of string (uri)s |  |
    | `offerings_data` | array of objects |  |
    | `offerings_data.name` | string |  |
    | `offerings_data.uuid` | string (uuid) |  |
    | `approval_limit` | string (decimal) | The credit limit beyond which requests need to be approved by a local admin. If this is None, then no local approval is required. If this is set to 0, then all requests (including creating the project) need to be approved. |
    | `max_credit_limit` | string (decimal) | The maximum credit limit for any projects created in this class. Any requests beyond this limit are automatically rejected. If this is None, then no maximum limit is set. If this is set to 0, then no projects can be created in this class. |
    | `allocation_units_mapping` | any | The mapping of credits to allocation units, i.e. how many allocation units to award per credit allocated. |
    | `role_mapping` | any | The mapping of role names from the remote portal to role information in this portal for users in projects created in this class. |
    | `role_mapping_data` | object (free-form) | Serialize the role mapping dictionary returned by get_role_mapping() |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/openportal-project-template/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openportal_project_template import openportal_project_template_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openportal_project_template_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openportal_project_template_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal_project_template/openportal_project_template_destroy.py)

=== "TypeScript"

    ```typescript
    import { openportalProjectTemplateDestroy } from 'waldur-js-client';
    
    try {
      const response = await openportalProjectTemplateDestroy({
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


### Delete ProjectTemplate object

Delete ProjectTemplate object


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/openportal-project-template/a1b2c3d4-e5f6-7890-abcd-ef1234567890/delete/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.openportal_project_template import openportal_project_template_delete_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = openportal_project_template_delete_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`openportal_project_template_delete_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/openportal_project_template/openportal_project_template_delete_destroy.py)

=== "TypeScript"

    ```typescript
    import { openportalProjectTemplateDeleteDestroy } from 'waldur-js-client';
    
    try {
      const response = await openportalProjectTemplateDeleteDestroy({
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
