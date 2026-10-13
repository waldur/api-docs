# Sram Groups

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/sram-groups/` | [SRAM collaborations and groups provisioned into Waldur](#sram-collaborations-and-groups-provisioned-into-waldur) |
| <span class="http-badge http-get">GET</span> | `/api/sram-groups/{uuid}/` | [SRAM collaborations and groups provisioned into Waldur](#sram-collaborations-and-groups-provisioned-into-waldur) |

---

### SRAM collaborations and groups provisioned into Waldur

SRAM collaborations and groups provisioned into Waldur.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/sram-groups/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.sram_group_kind_enum import SramGroupKindEnum # (1)
    from waldur_api_client.api.sram_groups import sram_groups_list # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = sram_groups_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`SramGroupKindEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/sram_group_kind_enum.py)
    2.  **API Source:** [`sram_groups_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/sram_groups/sram_groups_list.py)

=== "TypeScript"

    ```typescript
    import { sramGroupsList } from 'waldur-js-client';
    
    try {
      const response = await sramGroupsList({
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
    | `customer_uuid` | string (uuid) |  |
    | `display_name` | string |  |
    | `kind` | string | _Enum: `co`, `group`_ |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `external_id` | string |  |
    | `display_name` | string |  |
    | `urn` | string | SRAM global URN: '<organisation>:<co>' or '<organisation>:<co>:<group>'. |
    | `kind` | any |  |
    | `description` | string |  |
    | `labels` | array of strings |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `role_uuid` | string (uuid) |  |
    | `role_name` | string |  |
    | `member_count` | integer |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### SRAM collaborations and groups provisioned into Waldur

SRAM collaborations and groups provisioned into Waldur.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/sram-groups/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.sram_groups import sram_groups_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = sram_groups_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`sram_groups_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/sram_groups/sram_groups_retrieve.py)

=== "TypeScript"

    ```typescript
    import { sramGroupsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await sramGroupsRetrieve({
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
    | `external_id` | string |  |
    | `display_name` | string |  |
    | `urn` | string | SRAM global URN: '<organisation>:<co>' or '<organisation>:<co>:<group>'. |
    | `kind` | any |  |
    | `description` | string |  |
    | `labels` | array of strings |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `role_uuid` | string (uuid) |  |
    | `role_name` | string |  |
    | `member_count` | integer |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---
