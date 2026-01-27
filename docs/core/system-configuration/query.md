# Query

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-post">POST</span> | `/api/query/` | [Execute read-only SQL query](#execute-read-only-sql-query) |

---

### Execute read-only SQL query

Execute a given SQL query against a read-only database replica. This is a powerful tool for diagnostics and reporting, but should be used with caution. Requires support user permissions.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/query/ \
      Authorization:"Token YOUR_API_TOKEN" \
      query="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.query_request import QueryRequest # (1)
    from waldur_api_client.api.query import query # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = QueryRequest(
        query="string-value"
    )
    response = query.sync(
        client=client,
        body=body_data
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`QueryRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/query_request.py)
    2.  **API Source:** [`query`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/query/query.py)

=== "TypeScript"

    ```typescript
    import { query } from 'waldur-js-client';
    
    try {
      const response = await query({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "query": "string-value"
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
    | `query` | string | ✓ |


=== "Responses"

    **`200`** - 
    
    
    ---
    
    **`400`** - No response body
    

---
