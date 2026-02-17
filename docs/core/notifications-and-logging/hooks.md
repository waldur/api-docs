# Hooks

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/hooks/` | [List Hooks](#list-hooks) |

---

### List Hooks


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/hooks/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.hooks import hooks_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = hooks_list.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`hooks_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/hooks/hooks_list.py)

=== "TypeScript"

    ```typescript
    import { hooksList } from 'waldur-js-client';
    
    try {
      const response = await hooksList({
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
    | `author_uuid` | string (uuid) | Filter by author UUID. |
    | `is_active` | boolean | Filter by active status. |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |


=== "Responses"

    **`200`** - No response body
    

---
