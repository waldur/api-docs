# Marketplace Offering Merges

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-offering-merges/` | [List Marketplace Offering Merges](#list-marketplace-offering-merges) |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-offering-merges/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-offering-merges/` | [Create](#create) |
| <span class="http-badge http-patch">PATCH</span> | `/api/marketplace-offering-merges/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-delete">DELETE</span> | `/api/marketplace-offering-merges/{uuid}/` | [Delete](#delete) |
| **Other Actions** | | |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-offering-merges/{uuid}/affected/` | [List the rows one preview entry changes, newest first](#list-the-rows-one-preview-entry-changes-newest-first) |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-offering-merges/suggest_mapping/` | [Suggest plan mappings by name and component mappings by type](#suggest-plan-mappings-by-name-and-component-mappings-by-type) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-offering-merges/{uuid}/execute/` | [Queue a previewed merge for execution](#queue-a-previewed-merge-for-execution) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-offering-merges/{uuid}/preview/` | [Compute the merge preview: counts, blockers and warnings](#compute-the-merge-preview-counts-blockers-and-warnings) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-offering-merges/{uuid}/undo/` | [Queue the undo of a completed merge](#queue-the-undo-of-a-completed-merge) |

---
## Core CRUD


### List Marketplace Offering Merges


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-offering-merges/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.offering_merge_state_enum import OfferingMergeStateEnum # (1)
    from waldur_api_client.api.marketplace_offering_merges import marketplace_offering_merges_list # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_offering_merges_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`OfferingMergeStateEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/offering_merge_state_enum.py)
    2.  **API Source:** [`marketplace_offering_merges_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_merges/marketplace_offering_merges_list.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingMergesList } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingMergesList({
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
    | `created` | string (date-time) | Created after |
    | `created_before` | string (date-time) | Created before |
    | `created_by_uuid` | string (uuid) | Created by UUID |
    | `modified` | string (date-time) | Modified after |
    | `modified_before` | string (date-time) | Modified before |
    | `offering_uuid` | string (uuid) | Source or target offering UUID |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `source_offering_uuid` | string (uuid) | Source offering UUID |
    | `state` | array |  |
    | `target_offering_uuid` | string (uuid) | Target offering UUID |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `state` | any |  |
    | `sources` | array of string (uuid)s | Offerings whose resources and history move to the target. |
    | `target` | string (uuid) |  |
    | `source_offerings` | array of objects |  |
    | `source_offerings.uuid` | string (uuid) |  |
    | `source_offerings.name` | string |  |
    | `source_offerings.state` | string |  |
    | `target_offering` | any |  |
    | `created_by` | string (uuid) |  |
    | `created_by_full_name` | string |  |
    | `plan_mapping` | object (free-form) | Source plan UUID to target plan UUID. |
    | `component_mapping` | object (free-form) | Per source offering UUID: source component type to target component type. |
    | `attribute_key_mapping` | object (free-form) | Order and resource answer key renames: old key to new key. |
    | `invoice_policy` | string | <br>_Enum: `open_month`, `all_months`_ |
    | `preview` | any |  |
    | `verification` | any |  |
    | `progress` | any |  |
    | `error_message` | string |  |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-offering-merges/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_offering_merges import marketplace_offering_merges_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_offering_merges_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_offering_merges_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_merges/marketplace_offering_merges_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingMergesRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingMergesRetrieve({
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
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `state` | any |  |
    | `sources` | array of string (uuid)s | Offerings whose resources and history move to the target. |
    | `target` | string (uuid) |  |
    | `source_offerings` | array of objects |  |
    | `source_offerings.uuid` | string (uuid) |  |
    | `source_offerings.name` | string |  |
    | `source_offerings.state` | string |  |
    | `target_offering` | any |  |
    | `created_by` | string (uuid) |  |
    | `created_by_full_name` | string |  |
    | `plan_mapping` | object (free-form) | Source plan UUID to target plan UUID. |
    | `component_mapping` | object (free-form) | Per source offering UUID: source component type to target component type. |
    | `attribute_key_mapping` | object (free-form) | Order and resource answer key renames: old key to new key. |
    | `invoice_policy` | string | <br>_Enum: `open_month`, `all_months`_ |
    | `preview` | any |  |
    | `verification` | any |  |
    | `progress` | any |  |
    | `error_message` | string |  |

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-offering-merges/ \
      Authorization:"Token YOUR_API_TOKEN" \
      sources:='[]' \
      target="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.offering_merge_request import OfferingMergeRequest # (1)
    from waldur_api_client.api.marketplace_offering_merges import marketplace_offering_merges_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = OfferingMergeRequest(
        sources=[],
        target="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = marketplace_offering_merges_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`OfferingMergeRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/offering_merge_request.py)
    2.  **API Source:** [`marketplace_offering_merges_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_merges/marketplace_offering_merges_create.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingMergesCreate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingMergesCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "sources": [],
        "target": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `sources` | array of string (uuid)s | ✓ | Offerings whose resources and history move to the target. |
    | `target` | string (uuid) | ✓ |  |
    | `plan_mapping` | object (free-form) |  | Source plan UUID to target plan UUID. |
    | `component_mapping` | object (free-form) |  | Per source offering UUID: source component type to target component type. |
    | `attribute_key_mapping` | object (free-form) |  | Order and resource answer key renames: old key to new key. |
    | `invoice_policy` | string |  | <br>_Enum: `open_month`, `all_months`_ |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `state` | any |  |
    | `sources` | array of string (uuid)s | Offerings whose resources and history move to the target. |
    | `target` | string (uuid) |  |
    | `source_offerings` | array of objects |  |
    | `source_offerings.uuid` | string (uuid) |  |
    | `source_offerings.name` | string |  |
    | `source_offerings.state` | string |  |
    | `target_offering` | any |  |
    | `created_by` | string (uuid) |  |
    | `created_by_full_name` | string |  |
    | `plan_mapping` | object (free-form) | Source plan UUID to target plan UUID. |
    | `component_mapping` | object (free-form) | Per source offering UUID: source component type to target component type. |
    | `attribute_key_mapping` | object (free-form) | Order and resource answer key renames: old key to new key. |
    | `invoice_policy` | string | <br>_Enum: `open_month`, `all_months`_ |
    | `preview` | any |  |
    | `verification` | any |  |
    | `progress` | any |  |
    | `error_message` | string |  |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/marketplace-offering-merges/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_offering_merge_request import PatchedOfferingMergeRequest # (1)
    from waldur_api_client.api.marketplace_offering_merges import marketplace_offering_merges_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedOfferingMergeRequest()
    response = marketplace_offering_merges_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedOfferingMergeRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_offering_merge_request.py)
    2.  **API Source:** [`marketplace_offering_merges_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_merges/marketplace_offering_merges_partial_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingMergesPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingMergesPartialUpdate({
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
    | `sources` | array of string (uuid)s |  | Offerings whose resources and history move to the target. |
    | `target` | string (uuid) |  |  |
    | `plan_mapping` | object (free-form) |  | Source plan UUID to target plan UUID. |
    | `component_mapping` | object (free-form) |  | Per source offering UUID: source component type to target component type. |
    | `attribute_key_mapping` | object (free-form) |  | Order and resource answer key renames: old key to new key. |
    | `invoice_policy` | string |  | <br>_Enum: `open_month`, `all_months`_ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `state` | any |  |
    | `sources` | array of string (uuid)s | Offerings whose resources and history move to the target. |
    | `target` | string (uuid) |  |
    | `source_offerings` | array of objects |  |
    | `source_offerings.uuid` | string (uuid) |  |
    | `source_offerings.name` | string |  |
    | `source_offerings.state` | string |  |
    | `target_offering` | any |  |
    | `created_by` | string (uuid) |  |
    | `created_by_full_name` | string |  |
    | `plan_mapping` | object (free-form) | Source plan UUID to target plan UUID. |
    | `component_mapping` | object (free-form) | Per source offering UUID: source component type to target component type. |
    | `attribute_key_mapping` | object (free-form) | Order and resource answer key renames: old key to new key. |
    | `invoice_policy` | string | <br>_Enum: `open_month`, `all_months`_ |
    | `preview` | any |  |
    | `verification` | any |  |
    | `progress` | any |  |
    | `error_message` | string |  |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/marketplace-offering-merges/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_offering_merges import marketplace_offering_merges_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_offering_merges_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_offering_merges_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_merges/marketplace_offering_merges_destroy.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingMergesDestroy } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingMergesDestroy({
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


### List the rows one preview entry changes, newest first

List the rows one preview entry changes, newest first.

Staff and support; nothing is written. A merge that has not run yet
recomputes its plan, so the listing is what the executor would do
rather than a stored copy of it. A merge that has run, or has been
undone, is described from its journal: what was actually written.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-offering-merges/a1b2c3d4-e5f6-7890-abcd-ef1234567890/affected/ \
      Authorization:"Token YOUR_API_TOKEN" \
      entry=="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_offering_merges import marketplace_offering_merges_affected_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_offering_merges_affected_list.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        entry="string-value"
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`marketplace_offering_merges_affected_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_merges/marketplace_offering_merges_affected_list.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingMergesAffectedList } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingMergesAffectedList({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      query: {
        "entry": "string-value"
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

    | Name | Type | Required | Description |
    |---|---|---|---|
    | `entry` | string | ✓ | Coverage registry entry, as reported by the preview: marketplace.Resource.offering, invoices.InvoiceItem.details, and so on. |
    | `page` | integer |  | A page number within the paginated result set. |
    | `page_size` | integer |  | Number of results to return per page. |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `id` | integer | Primary key of the row. |
    | `uuid` | string | The object's UUID, when it has one. |
    | `model` | string | Model label of the row. |
    | `field` | string | Column the merge writes. |
    | `description` | string | The object described in names rather than primary keys. |
    | `old_value` | string | The current value, resolved to a name. |
    | `new_value` | string | The value after the merge; null when the row does not change. |
    | `kept_on_source` | boolean | Whether the row stays with the archived source instead of moving. |

---

### Suggest plan mappings by name and component mappings by type

Suggest plan mappings by name and component mappings by type.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-offering-merges/suggest_mapping/ \
      Authorization:"Token YOUR_API_TOKEN" \
      sources=="string-value" \
      target=="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_offering_merges import marketplace_offering_merges_suggest_mapping_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_offering_merges_suggest_mapping_retrieve.sync(
        client=client,
        sources="string-value",
        target="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_offering_merges_suggest_mapping_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_merges/marketplace_offering_merges_suggest_mapping_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingMergesSuggestMappingRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingMergesSuggestMappingRetrieve({
      auth: "Token YOUR_API_TOKEN",
      query: {
        "sources": "string-value",
        "target": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `sources` | string | ✓ | Source offering UUIDs, comma-separated or repeated. |
    | `target` | string (uuid) | ✓ | Target offering UUID. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `plan_mapping` | object (free-form) | Source plan UUID to the target plan with the same name. |
    | `component_mapping` | object (free-form) | Per source offering UUID: source component type to the target component of the same type, else the same name. |
    | `unmatched_plans` | array of objects |  |
    | `unmatched_plans.offering_uuid` | string |  |
    | `unmatched_plans.plan_uuid` | string |  |
    | `unmatched_plans.name` | string |  |
    | `unmatched_components` | array of objects |  |
    | `unmatched_components.offering_uuid` | string |  |
    | `unmatched_components.type` | string |  |
    | `unmatched_components.name` | string |  |

---

### Queue a previewed merge for execution

Queue a previewed merge for execution.

Refused with 400 if the stored preview has blockers or a warning code
is missing from ``acknowledged_warnings``, and with 409 unless the
merge is ``previewed``, which also refuses a second request.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-offering-merges/a1b2c3d4-e5f6-7890-abcd-ef1234567890/execute/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.offering_merge_execute_request import OfferingMergeExecuteRequest # (1)
    from waldur_api_client.api.marketplace_offering_merges import marketplace_offering_merges_execute # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = OfferingMergeExecuteRequest()
    response = marketplace_offering_merges_execute.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`OfferingMergeExecuteRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/offering_merge_execute_request.py)
    2.  **API Source:** [`marketplace_offering_merges_execute`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_merges/marketplace_offering_merges_execute.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingMergesExecute } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingMergesExecute({
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
    | `acknowledged_warnings` | array of strings |  | Codes of every warning in the stored preview. |


=== "Responses"

    **`202`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `state` | any |  |
    | `sources` | array of string (uuid)s | Offerings whose resources and history move to the target. |
    | `target` | string (uuid) |  |
    | `source_offerings` | array of objects |  |
    | `source_offerings.uuid` | string (uuid) |  |
    | `source_offerings.name` | string |  |
    | `source_offerings.state` | string |  |
    | `target_offering` | any |  |
    | `created_by` | string (uuid) |  |
    | `created_by_full_name` | string |  |
    | `plan_mapping` | object (free-form) | Source plan UUID to target plan UUID. |
    | `component_mapping` | object (free-form) | Per source offering UUID: source component type to target component type. |
    | `attribute_key_mapping` | object (free-form) | Order and resource answer key renames: old key to new key. |
    | `invoice_policy` | string | <br>_Enum: `open_month`, `all_months`_ |
    | `preview` | any |  |
    | `verification` | any |  |
    | `progress` | any |  |
    | `error_message` | string |  |
    
    ---
    
    **`400`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `detail` | string |  |
    | `missing_acknowledgements` | array of strings |  |
    | `blockers` | array of objects |  |
    | `blockers.code` | string | Machine-readable reason. |
    | `blockers.message` | string |  |
    | `blockers.details` | object (free-form) | Issue-specific details: offerings, plans, keys or counts. |
    
    ---
    
    **`409`** - The merge is not previewed.
    

---

### Compute the merge preview: counts, blockers and warnings

Compute the merge preview: counts, blockers and warnings.

Staff store it on the record, which moves to ``previewed``. Support
receive the same preview without it being stored.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-offering-merges/a1b2c3d4-e5f6-7890-abcd-ef1234567890/preview/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_offering_merges import marketplace_offering_merges_preview # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_offering_merges_preview.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_offering_merges_preview`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_merges/marketplace_offering_merges_preview.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingMergesPreview } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingMergesPreview({
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
    | `target` | string | Target offering UUID. |
    | `sources` | array of strings | Source offering UUIDs. |
    | `counts` | object (free-form) | Rows per coverage registry entry (model.Field label). |
    | `entries` | array of objects | The same counts, grouped by area and classified by effect. |
    | `entries.label` | string | Coverage registry entry, as model.Field label. |
    | `entries.area` | any | Part of the service the rows belong to. |
    | `entries.area_title` | string | The area, for a human reader. |
    | `entries.effect` | any | What the merge does to the rows. |
    | `entries.effect_title` | string | The effect, for a human reader. |
    | `entries.count` | integer | Rows the entry covers. |
    | `entries.left_on_source` | integer | Of those, rows that stay on a source because the target has them already. |
    | `entries.can_list_rows` | boolean | Whether the affected endpoint can list the rows one by one. |
    | `left_on_source` | object (free-form) | Rows that stay on a source because the target has them already. |
    | `summaries_to_recompute` | object |  |
    | `summaries_to_recompute.components` | integer | Components whose monthly usage summaries are recomputed. |
    | `summaries_to_recompute.periods` | array of strings | Months recomputed, as YYYY-MM. |
    | `invoice_items` | object |  |
    | `invoice_items.policy` | string | The merge's invoice_policy. |
    | `invoice_items.to_rewrite` | integer | Invoice items whose snapshot the chosen policy rewrites. |
    | `invoice_items.to_rewrite_by_policy` | object (free-form) | Invoice items each policy would rewrite. |
    | `invoice_items.on_closed_invoices` | integer |  |
    | `invoice_items.kept_on_closed_invoices` | integer |  |
    | `blockers` | array of objects |  |
    | `blockers.code` | string | Machine-readable reason. |
    | `blockers.message` | string |  |
    | `blockers.details` | object (free-form) | Issue-specific details: offerings, plans, keys or counts. |
    | `warnings` | array of objects |  |
    | `warnings.code` | string | Machine-readable reason. |
    | `warnings.message` | string |  |
    | `warnings.details` | object (free-form) | Issue-specific details: offerings, plans, keys or counts. |
    
    ---
    
    **`409`** - The merge is not in a previewable state.
    

---

### Queue the undo of a completed merge

Queue the undo of a completed merge.

The engine's preconditions are checked first: if the undo would be
refused, the answer is 400 with the blockers and nothing is queued.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-offering-merges/a1b2c3d4-e5f6-7890-abcd-ef1234567890/undo/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_offering_merges import marketplace_offering_merges_undo # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_offering_merges_undo.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_offering_merges_undo`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_offering_merges/marketplace_offering_merges_undo.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOfferingMergesUndo } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOfferingMergesUndo({
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

    **`202`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `state` | any |  |
    | `sources` | array of string (uuid)s | Offerings whose resources and history move to the target. |
    | `target` | string (uuid) |  |
    | `source_offerings` | array of objects |  |
    | `source_offerings.uuid` | string (uuid) |  |
    | `source_offerings.name` | string |  |
    | `source_offerings.state` | string |  |
    | `target_offering` | any |  |
    | `created_by` | string (uuid) |  |
    | `created_by_full_name` | string |  |
    | `plan_mapping` | object (free-form) | Source plan UUID to target plan UUID. |
    | `component_mapping` | object (free-form) | Per source offering UUID: source component type to target component type. |
    | `attribute_key_mapping` | object (free-form) | Order and resource answer key renames: old key to new key. |
    | `invoice_policy` | string | <br>_Enum: `open_month`, `all_months`_ |
    | `preview` | any |  |
    | `verification` | any |  |
    | `progress` | any |  |
    | `error_message` | string |  |
    
    ---
    
    **`400`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `detail` | string |  |
    | `missing_acknowledgements` | array of strings |  |
    | `blockers` | array of objects |  |
    | `blockers.code` | string | Machine-readable reason. |
    | `blockers.message` | string |  |
    | `blockers.details` | object (free-form) | Issue-specific details: offerings, plans, keys or counts. |
    
    ---
    
    **`409`** - The merge is not done.
    

---
