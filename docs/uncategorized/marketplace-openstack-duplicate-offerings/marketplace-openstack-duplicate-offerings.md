# Marketplace Openstack Duplicate Offerings

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-openstack-duplicate-offerings/` | [List Marketplace Openstack Duplicate Offerings](#list-marketplace-openstack-duplicate-offerings) |

---

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
