# Marketplace Project Posix Groups

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-project-posix-groups/` | [List POSIX group GIDs assigned to a project](#list-posix-group-gids-assigned-to-a-project) |

---

### List POSIX group GIDs assigned to a project

Returns every POSIX group GID a project has been assigned, across all offerings: project-mapped groups (project_group_gid) and resource / resource-project role groups (role_group_gid). The project_uuid query parameter is required.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-project-posix-groups/ \
      Authorization:"Token YOUR_API_TOKEN" \
      project_uuid=="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_project_posix_groups import marketplace_project_posix_groups_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_project_posix_groups_list.sync(
        client=client,
        project_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`marketplace_project_posix_groups_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_project_posix_groups/marketplace_project_posix_groups_list.py)

=== "TypeScript"

    ```typescript
    import { marketplaceProjectPosixGroupsList } from 'waldur-js-client';
    
    try {
      const response = await marketplaceProjectPosixGroupsList({
      auth: "Token YOUR_API_TOKEN",
      query: {
        "project_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Query Parameters"

    | Name | Type | Required |
    |---|---|---|
    | `project_uuid` | string | ✓ |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `kind` | string |
    | `gid` | integer |
    | `offering_uuid` | string |
    | `offering_name` | string |
    | `provider_name` | string |
    | `role` | string |
    | `scope_type` | string |
    | `scope_name` | string |
    | `scope_uuid` | string |

---
