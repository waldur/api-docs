# Proposal My Requested Resources

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/proposal-my-requested-resources/` | [List Proposal My Requested Resources](#list-proposal-my-requested-resources) |
| <span class="http-badge http-get">GET</span> | `/api/proposal-my-requested-resources/{uuid}/` | [Retrieve](#retrieve) |

---

### List Proposal My Requested Resources


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/proposal-my-requested-resources/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.proposal_states import ProposalStates # (1)
    from waldur_api_client.models.user_requested_resource_o_enum import UserRequestedResourceOEnum # (2)
    from waldur_api_client.api.proposal_my_requested_resources import proposal_my_requested_resources_list # (3)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_my_requested_resources_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`ProposalStates`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/proposal_states.py)
    2.  **Model Source:** [`UserRequestedResourceOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/user_requested_resource_o_enum.py)
    3.  **API Source:** [`proposal_my_requested_resources_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_my_requested_resources/proposal_my_requested_resources_list.py)

=== "TypeScript"

    ```typescript
    import { proposalMyRequestedResourcesList } from 'waldur-js-client';
    
    try {
      const response = await proposalMyRequestedResourcesList({
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
    | `created` | string (date-time) |  |
    | `include_closed` | boolean | Include requests belonging to rejected or canceled proposals. They are omitted by default. |
    | `o` | array | Ordering<br><br> |
    | `offering` | string (uri) | Offering |
    | `offering_uuid` | string (uuid) |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `proposal` | string (uri) | Proposal |
    | `proposal_state` | array | Proposal state<br><br> |
    | `proposal_uuid` | string (uuid) |  |
    | `query` | string | Search by offering, proposal, call or resource name |
    | `resource` | string (uri) | Resource |
    | `resource_uuid` | string (uuid) |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `created` | string (date-time) |
    | `description` | string |
    | `attributes` | object (free-form) |
    | `limits` | object (free-form) |
    | `offering_name` | string |
    | `offering_uuid` | string (uuid) |
    | `call_name` | string |
    | `call_uuid` | string (uuid) |
    | `proposal` | string (uri) |
    | `proposal_name` | string |
    | `proposal_uuid` | string (uuid) |
    | `proposal_state` | string |
    | `resource_name` | string |
    | `resource_uuid` | string (uuid) |
    | `resource_state` | string |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/proposal-my-requested-resources/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.proposal_my_requested_resources import proposal_my_requested_resources_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = proposal_my_requested_resources_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`proposal_my_requested_resources_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/proposal_my_requested_resources/proposal_my_requested_resources_retrieve.py)

=== "TypeScript"

    ```typescript
    import { proposalMyRequestedResourcesRetrieve } from 'waldur-js-client';
    
    try {
      const response = await proposalMyRequestedResourcesRetrieve({
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
    | `uuid` | string (uuid) |
    | `created` | string (date-time) |
    | `description` | string |
    | `attributes` | object (free-form) |
    | `limits` | object (free-form) |
    | `offering_name` | string |
    | `offering_uuid` | string (uuid) |
    | `call_name` | string |
    | `call_uuid` | string (uuid) |
    | `proposal` | string (uri) |
    | `proposal_name` | string |
    | `proposal_uuid` | string (uuid) |
    | `proposal_state` | string |
    | `resource_name` | string |
    | `resource_uuid` | string (uuid) |
    | `resource_state` | string |

---
