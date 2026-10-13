# Marketplace Metric Definitions

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-metric-definitions/` | [List Marketplace Metric Definitions](#list-marketplace-metric-definitions) |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-metric-definitions/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-metric-definitions/` | [Create](#create) |
| <span class="http-badge http-put">PUT</span> | `/api/marketplace-metric-definitions/{uuid}/` | [Update](#update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/marketplace-metric-definitions/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-delete">DELETE</span> | `/api/marketplace-metric-definitions/{uuid}/` | [Delete](#delete) |

---

### List Marketplace Metric Definitions


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-metric-definitions/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.metric_definition_state_enum import MetricDefinitionStateEnum # (1)
    from waldur_api_client.models.metric_kind_enum import MetricKindEnum # (2)
    from waldur_api_client.api.marketplace_metric_definitions import marketplace_metric_definitions_list # (3)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_metric_definitions_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`MetricDefinitionStateEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/metric_definition_state_enum.py)
    2.  **Model Source:** [`MetricKindEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/metric_kind_enum.py)
    3.  **API Source:** [`marketplace_metric_definitions_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_metric_definitions/marketplace_metric_definitions_list.py)

=== "TypeScript"

    ```typescript
    import { marketplaceMetricDefinitionsList } from 'waldur-js-client';
    
    try {
      const response = await marketplaceMetricDefinitionsList({
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
    | `is_global` | boolean |  |
    | `key` | string |  |
    | `kind` | string | _Enum: `gauge`, `counter`_ |
    | `name` | string |  |
    | `owner_customer_uuid` | string (uuid) |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `state` | string | _Enum: `active`, `deprecated`_ |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `key` | string | Name services report against. Cannot be changed. |
    | `name` | string |  |
    | `description` | string |  |
    | `unit` | string | UCUM unit, for example h, % or {learners}. |
    | `kind` | string | <br>_Enum: `gauge`, `counter`_ |
    | `good_direction` | string | <br>_Enum: `up`, `down`, `neutral`_ |
    | `attribute_keys` | array of strings |  |
    | `max_attribute_values` | integer | Distinct values one attribute may take per resource. |
    | `retention_policy` | string (uuid) |  |
    | `owner_customer` | string (uuid) | Service provider the definition is private to; empty is global. |
    | `owner_customer_name` | string |  |
    | `state` | string | <br>_Enum: `active`, `deprecated`_ |
    | `created` | string (date-time) |  |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-metric-definitions/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_metric_definitions import marketplace_metric_definitions_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_metric_definitions_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_metric_definitions_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_metric_definitions/marketplace_metric_definitions_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceMetricDefinitionsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceMetricDefinitionsRetrieve({
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
    | `key` | string | Name services report against. Cannot be changed. |
    | `name` | string |  |
    | `description` | string |  |
    | `unit` | string | UCUM unit, for example h, % or {learners}. |
    | `kind` | string | <br>_Enum: `gauge`, `counter`_ |
    | `good_direction` | string | <br>_Enum: `up`, `down`, `neutral`_ |
    | `attribute_keys` | array of strings |  |
    | `max_attribute_values` | integer | Distinct values one attribute may take per resource. |
    | `retention_policy` | string (uuid) |  |
    | `owner_customer` | string (uuid) | Service provider the definition is private to; empty is global. |
    | `owner_customer_name` | string |  |
    | `state` | string | <br>_Enum: `active`, `deprecated`_ |
    | `created` | string (date-time) |  |

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-metric-definitions/ \
      Authorization:"Token YOUR_API_TOKEN" \
      key="ssh-rsa AAAAB3NzaC1yc2EAAA..." \
      name="my-awesome-marketplace-metric-definition"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.metric_definition_request import MetricDefinitionRequest # (1)
    from waldur_api_client.api.marketplace_metric_definitions import marketplace_metric_definitions_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = MetricDefinitionRequest(
        key="ssh-rsa AAAAB3NzaC1yc2EAAA...",
        name="my-awesome-marketplace-metric-definition"
    )
    response = marketplace_metric_definitions_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`MetricDefinitionRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/metric_definition_request.py)
    2.  **API Source:** [`marketplace_metric_definitions_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_metric_definitions/marketplace_metric_definitions_create.py)

=== "TypeScript"

    ```typescript
    import { marketplaceMetricDefinitionsCreate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceMetricDefinitionsCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "key": "ssh-rsa AAAAB3NzaC1yc2EAAA...",
        "name": "my-awesome-marketplace-metric-definition"
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
    | `key` | string | ✓ | Name services report against. Cannot be changed. |
    | `name` | string | ✓ |  |
    | `description` | string |  |  |
    | `unit` | string |  | UCUM unit, for example h, % or {learners}. |
    | `kind` | string |  | <br>_Enum: `gauge`, `counter`_ |
    | `good_direction` | string |  | <br>_Enum: `up`, `down`, `neutral`_ |
    | `attribute_keys` | array of strings |  |  |
    | `max_attribute_values` | integer |  | Distinct values one attribute may take per resource. |
    | `retention_policy` | string (uuid) |  |  |
    | `owner_customer` | string (uuid) |  | Service provider the definition is private to; empty is global. |
    | `state` | string |  | <br>_Enum: `active`, `deprecated`_ |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `key` | string | Name services report against. Cannot be changed. |
    | `name` | string |  |
    | `description` | string |  |
    | `unit` | string | UCUM unit, for example h, % or {learners}. |
    | `kind` | string | <br>_Enum: `gauge`, `counter`_ |
    | `good_direction` | string | <br>_Enum: `up`, `down`, `neutral`_ |
    | `attribute_keys` | array of strings |  |
    | `max_attribute_values` | integer | Distinct values one attribute may take per resource. |
    | `retention_policy` | string (uuid) |  |
    | `owner_customer` | string (uuid) | Service provider the definition is private to; empty is global. |
    | `owner_customer_name` | string |  |
    | `state` | string | <br>_Enum: `active`, `deprecated`_ |
    | `created` | string (date-time) |  |

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/marketplace-metric-definitions/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      key="ssh-rsa AAAAB3NzaC1yc2EAAA..." \
      name="my-awesome-marketplace-metric-definition"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.metric_definition_request import MetricDefinitionRequest # (1)
    from waldur_api_client.api.marketplace_metric_definitions import marketplace_metric_definitions_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = MetricDefinitionRequest(
        key="ssh-rsa AAAAB3NzaC1yc2EAAA...",
        name="my-awesome-marketplace-metric-definition"
    )
    response = marketplace_metric_definitions_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`MetricDefinitionRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/metric_definition_request.py)
    2.  **API Source:** [`marketplace_metric_definitions_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_metric_definitions/marketplace_metric_definitions_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceMetricDefinitionsUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceMetricDefinitionsUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "key": "ssh-rsa AAAAB3NzaC1yc2EAAA...",
        "name": "my-awesome-marketplace-metric-definition"
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
    | `key` | string | ✓ | Name services report against. Cannot be changed. |
    | `name` | string | ✓ |  |
    | `description` | string |  |  |
    | `unit` | string |  | UCUM unit, for example h, % or {learners}. |
    | `kind` | string |  | <br>_Enum: `gauge`, `counter`_ |
    | `good_direction` | string |  | <br>_Enum: `up`, `down`, `neutral`_ |
    | `attribute_keys` | array of strings |  |  |
    | `max_attribute_values` | integer |  | Distinct values one attribute may take per resource. |
    | `retention_policy` | string (uuid) |  |  |
    | `owner_customer` | string (uuid) |  | Service provider the definition is private to; empty is global. |
    | `state` | string |  | <br>_Enum: `active`, `deprecated`_ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `key` | string | Name services report against. Cannot be changed. |
    | `name` | string |  |
    | `description` | string |  |
    | `unit` | string | UCUM unit, for example h, % or {learners}. |
    | `kind` | string | <br>_Enum: `gauge`, `counter`_ |
    | `good_direction` | string | <br>_Enum: `up`, `down`, `neutral`_ |
    | `attribute_keys` | array of strings |  |
    | `max_attribute_values` | integer | Distinct values one attribute may take per resource. |
    | `retention_policy` | string (uuid) |  |
    | `owner_customer` | string (uuid) | Service provider the definition is private to; empty is global. |
    | `owner_customer_name` | string |  |
    | `state` | string | <br>_Enum: `active`, `deprecated`_ |
    | `created` | string (date-time) |  |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/marketplace-metric-definitions/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_metric_definition_request import PatchedMetricDefinitionRequest # (1)
    from waldur_api_client.api.marketplace_metric_definitions import marketplace_metric_definitions_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedMetricDefinitionRequest()
    response = marketplace_metric_definitions_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedMetricDefinitionRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_metric_definition_request.py)
    2.  **API Source:** [`marketplace_metric_definitions_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_metric_definitions/marketplace_metric_definitions_partial_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceMetricDefinitionsPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceMetricDefinitionsPartialUpdate({
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
    | `key` | string |  | Name services report against. Cannot be changed. |
    | `name` | string |  |  |
    | `description` | string |  |  |
    | `unit` | string |  | UCUM unit, for example h, % or {learners}. |
    | `kind` | string |  | <br>_Enum: `gauge`, `counter`_ |
    | `good_direction` | string |  | <br>_Enum: `up`, `down`, `neutral`_ |
    | `attribute_keys` | array of strings |  |  |
    | `max_attribute_values` | integer |  | Distinct values one attribute may take per resource. |
    | `retention_policy` | string (uuid) |  |  |
    | `owner_customer` | string (uuid) |  | Service provider the definition is private to; empty is global. |
    | `state` | string |  | <br>_Enum: `active`, `deprecated`_ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `key` | string | Name services report against. Cannot be changed. |
    | `name` | string |  |
    | `description` | string |  |
    | `unit` | string | UCUM unit, for example h, % or {learners}. |
    | `kind` | string | <br>_Enum: `gauge`, `counter`_ |
    | `good_direction` | string | <br>_Enum: `up`, `down`, `neutral`_ |
    | `attribute_keys` | array of strings |  |
    | `max_attribute_values` | integer | Distinct values one attribute may take per resource. |
    | `retention_policy` | string (uuid) |  |
    | `owner_customer` | string (uuid) | Service provider the definition is private to; empty is global. |
    | `owner_customer_name` | string |  |
    | `state` | string | <br>_Enum: `active`, `deprecated`_ |
    | `created` | string (date-time) |  |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/marketplace-metric-definitions/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_metric_definitions import marketplace_metric_definitions_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_metric_definitions_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_metric_definitions_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_metric_definitions/marketplace_metric_definitions_destroy.py)

=== "TypeScript"

    ```typescript
    import { marketplaceMetricDefinitionsDestroy } from 'waldur-js-client';
    
    try {
      const response = await marketplaceMetricDefinitionsDestroy({
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
