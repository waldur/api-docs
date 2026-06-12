# Autoprovisioning Rules

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/autoprovisioning-rules/` | [Manage autoprovisioning rules](#manage-autoprovisioning-rules) |
| <span class="http-badge http-get">GET</span> | `/api/autoprovisioning-rules/{uuid}/` | [Manage autoprovisioning rules](#manage-autoprovisioning-rules) |
| <span class="http-badge http-post">POST</span> | `/api/autoprovisioning-rules/` | [Manage autoprovisioning rules](#manage-autoprovisioning-rules) |
| <span class="http-badge http-put">PUT</span> | `/api/autoprovisioning-rules/{uuid}/` | [Manage autoprovisioning rules](#manage-autoprovisioning-rules) |
| <span class="http-badge http-patch">PATCH</span> | `/api/autoprovisioning-rules/{uuid}/` | [Manage autoprovisioning rules](#manage-autoprovisioning-rules) |
| <span class="http-badge http-delete">DELETE</span> | `/api/autoprovisioning-rules/{uuid}/` | [Manage autoprovisioning rules](#manage-autoprovisioning-rules) |
| **Other Actions** | | |
| <span class="http-badge http-post">POST</span> | `/api/autoprovisioning-rules/{uuid}/test-match/` | [Dry-run rule evaluation against a target user.](#dry-run-rule-evaluation-against-a-target-user) |

---
## Core CRUD


### Manage autoprovisioning rules

Manage autoprovisioning rules.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/autoprovisioning-rules/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.autoprovisioning_rules import autoprovisioning_rules_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = autoprovisioning_rules_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`autoprovisioning_rules_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/autoprovisioning_rules/autoprovisioning_rules_list.py)

=== "TypeScript"

    ```typescript
    import { autoprovisioningRulesList } from 'waldur-js-client';
    
    try {
      const response = await autoprovisioningRulesList({
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
    | `name` | string |
    | `uuid` | string (uuid) |
    | `url` | string (uri) |
    | `user_affiliations` | array of strings |
    | `user_email_patterns` | array of strings |
    | `customer` | string (uri) |
    | `customer_name` | string |
    | `customer_uuid` | string |
    | `use_user_organization_as_customer_name` | boolean |
    | `project_role` | string (uri) |
    | `project_role_display_name` | string |
    | `project_role_description` | string |
    | `plan` | string (uri) |
    | `plan_attributes` | object (free-form) |
    | `plan_limits` | object (free-form) |
    | `plan_name` | string |
    | `offering_name` | string |
    | `offering_uuid` | string (uuid) |
    | `category_title` | string |
    | `category_url` | string (uri) |

---

### Manage autoprovisioning rules

Manage autoprovisioning rules.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/autoprovisioning-rules/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.autoprovisioning_rules import autoprovisioning_rules_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = autoprovisioning_rules_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`autoprovisioning_rules_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/autoprovisioning_rules/autoprovisioning_rules_retrieve.py)

=== "TypeScript"

    ```typescript
    import { autoprovisioningRulesRetrieve } from 'waldur-js-client';
    
    try {
      const response = await autoprovisioningRulesRetrieve({
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
    | `name` | string |
    | `uuid` | string (uuid) |
    | `url` | string (uri) |
    | `user_affiliations` | array of strings |
    | `user_email_patterns` | array of strings |
    | `customer` | string (uri) |
    | `customer_name` | string |
    | `customer_uuid` | string |
    | `use_user_organization_as_customer_name` | boolean |
    | `project_role` | string (uri) |
    | `project_role_display_name` | string |
    | `project_role_description` | string |
    | `plan` | string (uri) |
    | `plan_attributes` | object (free-form) |
    | `plan_limits` | object (free-form) |
    | `plan_name` | string |
    | `offering_name` | string |
    | `offering_uuid` | string (uuid) |
    | `category_title` | string |
    | `category_url` | string (uri) |

---

### Manage autoprovisioning rules

Manage autoprovisioning rules.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/autoprovisioning-rules/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-autoprovisioning-rule"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.rule_request import RuleRequest # (1)
    from waldur_api_client.api.autoprovisioning_rules import autoprovisioning_rules_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = RuleRequest(
        name="my-awesome-autoprovisioning-rule"
    )
    response = autoprovisioning_rules_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`RuleRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/rule_request.py)
    2.  **API Source:** [`autoprovisioning_rules_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/autoprovisioning_rules/autoprovisioning_rules_create.py)

=== "TypeScript"

    ```typescript
    import { autoprovisioningRulesCreate } from 'waldur-js-client';
    
    try {
      const response = await autoprovisioningRulesCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "name": "my-awesome-autoprovisioning-rule"
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
    | `user_affiliations` | array of strings |  |
    | `user_email_patterns` | array of strings |  |
    | `customer` | string (uri) |  |
    | `use_user_organization_as_customer_name` | boolean |  |
    | `project_role` | string (uri) |  |
    | `project_role_name` | string |  |
    | `plan` | string (uri) |  |
    | `plan_attributes` | object (free-form) |  |
    | `plan_limits` | object (free-form) |  |


=== "Responses"

    **`201`** - 
    
    | Field | Type |
    |---|---|
    | `name` | string |
    | `uuid` | string (uuid) |
    | `url` | string (uri) |
    | `user_affiliations` | array of strings |
    | `user_email_patterns` | array of strings |
    | `customer` | string (uri) |
    | `customer_name` | string |
    | `customer_uuid` | string |
    | `use_user_organization_as_customer_name` | boolean |
    | `project_role` | string (uri) |
    | `project_role_display_name` | string |
    | `project_role_description` | string |
    | `plan` | string (uri) |
    | `plan_attributes` | object (free-form) |
    | `plan_limits` | object (free-form) |
    | `plan_name` | string |
    | `offering_name` | string |
    | `offering_uuid` | string (uuid) |
    | `category_title` | string |
    | `category_url` | string (uri) |

---

### Manage autoprovisioning rules

Manage autoprovisioning rules.


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/autoprovisioning-rules/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-autoprovisioning-rule"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.rule_request import RuleRequest # (1)
    from waldur_api_client.api.autoprovisioning_rules import autoprovisioning_rules_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = RuleRequest(
        name="my-awesome-autoprovisioning-rule"
    )
    response = autoprovisioning_rules_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`RuleRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/rule_request.py)
    2.  **API Source:** [`autoprovisioning_rules_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/autoprovisioning_rules/autoprovisioning_rules_update.py)

=== "TypeScript"

    ```typescript
    import { autoprovisioningRulesUpdate } from 'waldur-js-client';
    
    try {
      const response = await autoprovisioningRulesUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "name": "my-awesome-autoprovisioning-rule"
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
    | `user_affiliations` | array of strings |  |
    | `user_email_patterns` | array of strings |  |
    | `customer` | string (uri) |  |
    | `use_user_organization_as_customer_name` | boolean |  |
    | `project_role` | string (uri) |  |
    | `project_role_name` | string |  |
    | `plan` | string (uri) |  |
    | `plan_attributes` | object (free-form) |  |
    | `plan_limits` | object (free-form) |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `name` | string |
    | `uuid` | string (uuid) |
    | `url` | string (uri) |
    | `user_affiliations` | array of strings |
    | `user_email_patterns` | array of strings |
    | `customer` | string (uri) |
    | `customer_name` | string |
    | `customer_uuid` | string |
    | `use_user_organization_as_customer_name` | boolean |
    | `project_role` | string (uri) |
    | `project_role_display_name` | string |
    | `project_role_description` | string |
    | `plan` | string (uri) |
    | `plan_attributes` | object (free-form) |
    | `plan_limits` | object (free-form) |
    | `plan_name` | string |
    | `offering_name` | string |
    | `offering_uuid` | string (uuid) |
    | `category_title` | string |
    | `category_url` | string (uri) |

---

### Manage autoprovisioning rules

Manage autoprovisioning rules.


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/autoprovisioning-rules/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_rule_request import PatchedRuleRequest # (1)
    from waldur_api_client.api.autoprovisioning_rules import autoprovisioning_rules_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedRuleRequest()
    response = autoprovisioning_rules_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedRuleRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_rule_request.py)
    2.  **API Source:** [`autoprovisioning_rules_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/autoprovisioning_rules/autoprovisioning_rules_partial_update.py)

=== "TypeScript"

    ```typescript
    import { autoprovisioningRulesPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await autoprovisioningRulesPartialUpdate({
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
    | `user_affiliations` | array of strings |  |
    | `user_email_patterns` | array of strings |  |
    | `customer` | string (uri) |  |
    | `use_user_organization_as_customer_name` | boolean |  |
    | `project_role` | string (uri) |  |
    | `project_role_name` | string |  |
    | `plan` | string (uri) |  |
    | `plan_attributes` | object (free-form) |  |
    | `plan_limits` | object (free-form) |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `name` | string |
    | `uuid` | string (uuid) |
    | `url` | string (uri) |
    | `user_affiliations` | array of strings |
    | `user_email_patterns` | array of strings |
    | `customer` | string (uri) |
    | `customer_name` | string |
    | `customer_uuid` | string |
    | `use_user_organization_as_customer_name` | boolean |
    | `project_role` | string (uri) |
    | `project_role_display_name` | string |
    | `project_role_description` | string |
    | `plan` | string (uri) |
    | `plan_attributes` | object (free-form) |
    | `plan_limits` | object (free-form) |
    | `plan_name` | string |
    | `offering_name` | string |
    | `offering_uuid` | string (uuid) |
    | `category_title` | string |
    | `category_url` | string (uri) |

---

### Manage autoprovisioning rules

Manage autoprovisioning rules.


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/autoprovisioning-rules/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.autoprovisioning_rules import autoprovisioning_rules_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = autoprovisioning_rules_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`autoprovisioning_rules_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/autoprovisioning_rules/autoprovisioning_rules_destroy.py)

=== "TypeScript"

    ```typescript
    import { autoprovisioningRulesDestroy } from 'waldur-js-client';
    
    try {
      const response = await autoprovisioningRulesDestroy({
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


### Dry-run rule evaluation against a target user.

Evaluate this rule against the given user without provisioning. Returns per-filter outcomes, the customer-lookup verdict (when the rule uses use_user_organization_as_customer_name) and a top-line would_provision flag together with a human-readable block_reason.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/autoprovisioning-rules/a1b2c3d4-e5f6-7890-abcd-ef1234567890/test-match/ \
      Authorization:"Token YOUR_API_TOKEN" \
      user_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.rule_test_match_request_request import RuleTestMatchRequestRequest # (1)
    from waldur_api_client.api.autoprovisioning_rules import autoprovisioning_rules_test_match # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = RuleTestMatchRequestRequest(
        user_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = autoprovisioning_rules_test_match.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`RuleTestMatchRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/rule_test_match_request_request.py)
    2.  **API Source:** [`autoprovisioning_rules_test_match`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/autoprovisioning_rules/autoprovisioning_rules_test_match.py)

=== "TypeScript"

    ```typescript
    import { autoprovisioningRulesTestMatch } from 'waldur-js-client';
    
    try {
      const response = await autoprovisioningRulesTestMatch({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "user_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `user_uuid` | string (uuid) | ✓ | UUID of the user to evaluate this rule against. |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `would_provision` | boolean |
    | `block_reason` | string |
    | `user_username` | string |
    | `user_email` | string |
    | `user_organization` | string |
    | `user_registration_method` | string |
    | `user_identity_source` | string |
    | `user_affiliations` | array of strings |
    | `user_is_protected` | boolean |
    | `filter_results` | array of objects |
    | `filter_results.name` | string |
    | `filter_results.configured` | boolean |
    | `filter_results.matched` | boolean |
    | `filter_results.user_value` | object (free-form) |
    | `filter_results.rule_value` | object (free-form) |
    | `filter_results.reason` | string |
    | `customer_lookup_performed` | boolean |
    | `customer_candidates` | array of objects |
    | `customer_candidates.uuid` | string (uuid) |
    | `customer_candidates.name` | string |
    | `customer_candidates.abbreviation` | string |
    | `customer_candidates.url` | string |
    | `customer_lookup_ambiguous` | boolean |
    | `resolved_project_name` | string |

---
