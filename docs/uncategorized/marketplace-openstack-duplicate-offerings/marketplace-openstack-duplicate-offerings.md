# Marketplace Openstack Duplicate Offerings

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-openstack-duplicate-offerings/` | [List Marketplace Openstack Duplicate Offerings](#list-marketplace-openstack-duplicate-offerings) |
| **Other Actions** | | |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-openstack-duplicate-offerings/remediate/` | [Remediate](#remediate) |

---
## Core CRUD


### List Marketplace Openstack Duplicate Offerings


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-openstack-duplicate-offerings/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_openstack_duplicate_offerings import marketplace_openstack_duplicate_offerings_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_openstack_duplicate_offerings_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`marketplace_openstack_duplicate_offerings_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_openstack_duplicate_offerings/marketplace_openstack_duplicate_offerings_list.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOpenstackDuplicateOfferingsList } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOpenstackDuplicateOfferingsList({
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
    | `tenant_id` | integer |
    | `tenant_uuid` | string (uuid) |
    | `tenant_name` | string |
    | `customer_name` | string |
    | `customer_uuid` | string (uuid) |
    | `offering_type` | string |
    | `recommended_keeper_id` | integer |
    | `orphan_count` | integer |
    | `candidates` | array of objects |
    | `candidates.id` | integer |
    | `candidates.uuid` | string (uuid) |
    | `candidates.name` | string |
    | `candidates.state` | string |
    | `candidates.active_resources` | integer |
    | `candidates.total_resources` | integer |
    | `candidates.is_recommended_keeper` | boolean |

---

## Other Actions


### Remediate

Collapse one duplicate per-tenant offering group onto its keeper. Previews by default; pass dry_run=false to apply. Refuses to run when history (billing periods, usage records) cannot be re-pointed.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-openstack-duplicate-offerings/remediate/ \
      Authorization:"Token YOUR_API_TOKEN" \
      tenant_id=123 \
      offering_type="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.duplicate_offering_remediate_request import DuplicateOfferingRemediateRequest # (1)
    from waldur_api_client.api.marketplace_openstack_duplicate_offerings import marketplace_openstack_duplicate_offerings_remediate # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = DuplicateOfferingRemediateRequest(
        tenant_id=123,
        offering_type="string-value"
    )
    response = marketplace_openstack_duplicate_offerings_remediate.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`DuplicateOfferingRemediateRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/duplicate_offering_remediate_request.py)
    2.  **API Source:** [`marketplace_openstack_duplicate_offerings_remediate`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_openstack_duplicate_offerings/marketplace_openstack_duplicate_offerings_remediate.py)

=== "TypeScript"

    ```typescript
    import { marketplaceOpenstackDuplicateOfferingsRemediate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceOpenstackDuplicateOfferingsRemediate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "tenant_id": 123,
        "offering_type": "string-value"
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
    | `tenant_id` | integer | ✓ |  |
    | `offering_type` | string | ✓ |  |
    | `dry_run` | boolean |  | Preview the changes without applying them. Mirrors the dry-run-by-default behaviour of the dedupe_tenant_offerings command.<br>_Constraints: default: `True`_ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `tenant_id` | integer |  |
    | `offering_type` | string |  |
    | `keeper_id` | integer |  |
    | `keeper_name` | string |  |
    | `dry_run` | boolean |  |
    | `duplicates` | array of objects |  |
    | `duplicates.duplicate_id` | integer |  |
    | `duplicates.duplicate_name` | string |  |
    | `duplicates.keeper_id` | integer |  |
    | `duplicates.keeper_name` | string |  |
    | `duplicates.action` | string | delete (nothing attached), merge, or skip. |
    | `duplicates.is_empty` | boolean |  |
    | `duplicates.resource_count` | integer |  |
    | `duplicates.order_count` | integer |  |
    | `duplicates.plan_period_count` | integer |  |
    | `duplicates.component_usage_count` | integer |  |
    | `duplicates.component_quota_count` | integer |  |
    | `duplicates.blockers` | array of strings |  |
    | `blockers` | array of strings |  |

---
