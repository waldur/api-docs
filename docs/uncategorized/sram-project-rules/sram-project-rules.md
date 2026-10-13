# Sram Project Rules

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/sram-project-rules/` | [Rules granting project roles to holders of SRAM placeholder roles](#rules-granting-project-roles-to-holders-of-sram-placeholder-roles) |
| <span class="http-badge http-get">GET</span> | `/api/sram-project-rules/{uuid}/` | [Rules granting project roles to holders of SRAM placeholder roles](#rules-granting-project-roles-to-holders-of-sram-placeholder-roles) |
| <span class="http-badge http-post">POST</span> | `/api/sram-project-rules/` | [Rules granting project roles to holders of SRAM placeholder roles](#rules-granting-project-roles-to-holders-of-sram-placeholder-roles) |
| <span class="http-badge http-put">PUT</span> | `/api/sram-project-rules/{uuid}/` | [Rules granting project roles to holders of SRAM placeholder roles](#rules-granting-project-roles-to-holders-of-sram-placeholder-roles) |
| <span class="http-badge http-patch">PATCH</span> | `/api/sram-project-rules/{uuid}/` | [Rules granting project roles to holders of SRAM placeholder roles](#rules-granting-project-roles-to-holders-of-sram-placeholder-roles) |
| <span class="http-badge http-delete">DELETE</span> | `/api/sram-project-rules/{uuid}/` | [Rules granting project roles to holders of SRAM placeholder roles](#rules-granting-project-roles-to-holders-of-sram-placeholder-roles) |
| **Other Actions** | | |
| <span class="http-badge http-get">GET</span> | `/api/sram-project-rules/{uuid}/preview/` | [Preview a rule](#preview-a-rule) |

---
## Core CRUD


### Rules granting project roles to holders of SRAM placeholder roles

Rules granting project roles to holders of SRAM placeholder roles.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/sram-project-rules/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.sram_project_rules import sram_project_rules_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = sram_project_rules_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`sram_project_rules_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/sram_project_rules/sram_project_rules_list.py)

=== "TypeScript"

    ```typescript
    import { sramProjectRulesList } from 'waldur-js-client';
    
    try {
      const response = await sramProjectRulesList({
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
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `is_active` | boolean |  |
    | `source_kind` | string | <br>_Enum: `co`, `group`, `any`_ |
    | `labels` | array of strings |  |
    | `group_short_name_patterns` | array of strings |  |
    | `project_field` | string | <br>_Enum: `backend_id`, `slug`_ |
    | `project_match` | string | <br>_Enum: `exact`, `prefix`, `regex`_ |
    | `project_pattern` | string | Placeholders: {co_external_id}, {co_identifier}, {co_short_name}, {org_short_name}, {group_short_name}. |
    | `project_role` | string (uuid) |  |
    | `project_role_name` | string |  |
    | `project_role_description` | string |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Rules granting project roles to holders of SRAM placeholder roles

Rules granting project roles to holders of SRAM placeholder roles.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/sram-project-rules/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.sram_project_rules import sram_project_rules_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = sram_project_rules_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`sram_project_rules_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/sram_project_rules/sram_project_rules_retrieve.py)

=== "TypeScript"

    ```typescript
    import { sramProjectRulesRetrieve } from 'waldur-js-client';
    
    try {
      const response = await sramProjectRulesRetrieve({
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
    | `name` | string |  |
    | `is_active` | boolean |  |
    | `source_kind` | string | <br>_Enum: `co`, `group`, `any`_ |
    | `labels` | array of strings |  |
    | `group_short_name_patterns` | array of strings |  |
    | `project_field` | string | <br>_Enum: `backend_id`, `slug`_ |
    | `project_match` | string | <br>_Enum: `exact`, `prefix`, `regex`_ |
    | `project_pattern` | string | Placeholders: {co_external_id}, {co_identifier}, {co_short_name}, {org_short_name}, {group_short_name}. |
    | `project_role` | string (uuid) |  |
    | `project_role_name` | string |  |
    | `project_role_description` | string |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Rules granting project roles to holders of SRAM placeholder roles

Rules granting project roles to holders of SRAM placeholder roles.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/sram-project-rules/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-sram-project-rule" \
      project_role="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.sram_project_rule_request import SramProjectRuleRequest # (1)
    from waldur_api_client.api.sram_project_rules import sram_project_rules_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = SramProjectRuleRequest(
        name="my-awesome-sram-project-rule",
        project_role="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = sram_project_rules_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`SramProjectRuleRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/sram_project_rule_request.py)
    2.  **API Source:** [`sram_project_rules_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/sram_project_rules/sram_project_rules_create.py)

=== "TypeScript"

    ```typescript
    import { sramProjectRulesCreate } from 'waldur-js-client';
    
    try {
      const response = await sramProjectRulesCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "name": "my-awesome-sram-project-rule",
        "project_role": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `is_active` | boolean |  |  |
    | `source_kind` | string |  | <br>_Enum: `co`, `group`, `any`_ |
    | `labels` | array of strings |  |  |
    | `group_short_name_patterns` | array of strings |  |  |
    | `project_field` | string |  | <br>_Enum: `backend_id`, `slug`_ |
    | `project_match` | string |  | <br>_Enum: `exact`, `prefix`, `regex`_ |
    | `project_pattern` | string |  | Placeholders: {co_external_id}, {co_identifier}, {co_short_name}, {org_short_name}, {group_short_name}. |
    | `project_role` | string (uuid) | ✓ |  |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `is_active` | boolean |  |
    | `source_kind` | string | <br>_Enum: `co`, `group`, `any`_ |
    | `labels` | array of strings |  |
    | `group_short_name_patterns` | array of strings |  |
    | `project_field` | string | <br>_Enum: `backend_id`, `slug`_ |
    | `project_match` | string | <br>_Enum: `exact`, `prefix`, `regex`_ |
    | `project_pattern` | string | Placeholders: {co_external_id}, {co_identifier}, {co_short_name}, {org_short_name}, {group_short_name}. |
    | `project_role` | string (uuid) |  |
    | `project_role_name` | string |  |
    | `project_role_description` | string |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Rules granting project roles to holders of SRAM placeholder roles

Rules granting project roles to holders of SRAM placeholder roles.


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/sram-project-rules/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-sram-project-rule" \
      project_role="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.sram_project_rule_request import SramProjectRuleRequest # (1)
    from waldur_api_client.api.sram_project_rules import sram_project_rules_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = SramProjectRuleRequest(
        name="my-awesome-sram-project-rule",
        project_role="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = sram_project_rules_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`SramProjectRuleRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/sram_project_rule_request.py)
    2.  **API Source:** [`sram_project_rules_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/sram_project_rules/sram_project_rules_update.py)

=== "TypeScript"

    ```typescript
    import { sramProjectRulesUpdate } from 'waldur-js-client';
    
    try {
      const response = await sramProjectRulesUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "name": "my-awesome-sram-project-rule",
        "project_role": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `is_active` | boolean |  |  |
    | `source_kind` | string |  | <br>_Enum: `co`, `group`, `any`_ |
    | `labels` | array of strings |  |  |
    | `group_short_name_patterns` | array of strings |  |  |
    | `project_field` | string |  | <br>_Enum: `backend_id`, `slug`_ |
    | `project_match` | string |  | <br>_Enum: `exact`, `prefix`, `regex`_ |
    | `project_pattern` | string |  | Placeholders: {co_external_id}, {co_identifier}, {co_short_name}, {org_short_name}, {group_short_name}. |
    | `project_role` | string (uuid) | ✓ |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `is_active` | boolean |  |
    | `source_kind` | string | <br>_Enum: `co`, `group`, `any`_ |
    | `labels` | array of strings |  |
    | `group_short_name_patterns` | array of strings |  |
    | `project_field` | string | <br>_Enum: `backend_id`, `slug`_ |
    | `project_match` | string | <br>_Enum: `exact`, `prefix`, `regex`_ |
    | `project_pattern` | string | Placeholders: {co_external_id}, {co_identifier}, {co_short_name}, {org_short_name}, {group_short_name}. |
    | `project_role` | string (uuid) |  |
    | `project_role_name` | string |  |
    | `project_role_description` | string |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Rules granting project roles to holders of SRAM placeholder roles

Rules granting project roles to holders of SRAM placeholder roles.


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/sram-project-rules/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_sram_project_rule_request import PatchedSramProjectRuleRequest # (1)
    from waldur_api_client.api.sram_project_rules import sram_project_rules_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedSramProjectRuleRequest()
    response = sram_project_rules_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedSramProjectRuleRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_sram_project_rule_request.py)
    2.  **API Source:** [`sram_project_rules_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/sram_project_rules/sram_project_rules_partial_update.py)

=== "TypeScript"

    ```typescript
    import { sramProjectRulesPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await sramProjectRulesPartialUpdate({
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
    | `is_active` | boolean |  |  |
    | `source_kind` | string |  | <br>_Enum: `co`, `group`, `any`_ |
    | `labels` | array of strings |  |  |
    | `group_short_name_patterns` | array of strings |  |  |
    | `project_field` | string |  | <br>_Enum: `backend_id`, `slug`_ |
    | `project_match` | string |  | <br>_Enum: `exact`, `prefix`, `regex`_ |
    | `project_pattern` | string |  | Placeholders: {co_external_id}, {co_identifier}, {co_short_name}, {org_short_name}, {group_short_name}. |
    | `project_role` | string (uuid) |  |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `is_active` | boolean |  |
    | `source_kind` | string | <br>_Enum: `co`, `group`, `any`_ |
    | `labels` | array of strings |  |
    | `group_short_name_patterns` | array of strings |  |
    | `project_field` | string | <br>_Enum: `backend_id`, `slug`_ |
    | `project_match` | string | <br>_Enum: `exact`, `prefix`, `regex`_ |
    | `project_pattern` | string | Placeholders: {co_external_id}, {co_identifier}, {co_short_name}, {org_short_name}, {group_short_name}. |
    | `project_role` | string (uuid) |  |
    | `project_role_name` | string |  |
    | `project_role_description` | string |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Rules granting project roles to holders of SRAM placeholder roles

Rules granting project roles to holders of SRAM placeholder roles.


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/sram-project-rules/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.sram_project_rules import sram_project_rules_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = sram_project_rules_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`sram_project_rules_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/sram_project_rules/sram_project_rules_destroy.py)

=== "TypeScript"

    ```typescript
    import { sramProjectRulesDestroy } from 'waldur-js-client';
    
    try {
      const response = await sramProjectRulesDestroy({
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


### Preview a rule

Groups the rule matches now, with the projects it selects and the placeholder holders who would get the project role.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/sram-project-rules/a1b2c3d4-e5f6-7890-abcd-ef1234567890/preview/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.sram_project_rules import sram_project_rules_preview_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = sram_project_rules_preview_list.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`sram_project_rules_preview_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/sram_project_rules/sram_project_rules_preview_list.py)

=== "TypeScript"

    ```typescript
    import { sramProjectRulesPreviewList } from 'waldur-js-client';
    
    try {
      const response = await sramProjectRulesPreviewList({
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

    | Name | Type | Description |
    |---|---|---|
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `group` | object |  |
    | `group.uuid` | string (uuid) |  |
    | `group.external_id` | string |  |
    | `group.display_name` | string |  |
    | `group.urn` | string | SRAM global URN: '<organisation>:<co>' or '<organisation>:<co>:<group>'. |
    | `group.kind` | any |  |
    | `group.description` | string |  |
    | `group.labels` | array of strings |  |
    | `group.customer_uuid` | string (uuid) |  |
    | `group.customer_name` | string |  |
    | `group.role_uuid` | string (uuid) |  |
    | `group.role_name` | string |  |
    | `group.member_count` | integer |  |
    | `group.created` | string (date-time) |  |
    | `group.modified` | string (date-time) |  |
    | `projects` | array of objects |  |
    | `projects.uuid` | string (uuid) |  |
    | `projects.name` | string |  |
    | `projects.slug` | string |  |
    | `projects.backend_id` | string |  |
    | `users` | array of objects |  |
    | `users.uuid` | string (uuid) |  |
    | `users.username` | string |  |
    | `users.full_name` | string |  |

---
