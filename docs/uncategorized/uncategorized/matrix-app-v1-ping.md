# Matrix App V1 Ping

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-post">POST</span> | `/_matrix/app/v1/ping` | [Matrix Application Service ping](#matrix-application-service-ping) |

---

### Matrix Application Service ping

Called by the homeserver when Waldur asks it to ping the appservice (MSC2659). Authenticated via hs_token in the Authorization header.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/_matrix/app/v1/ping \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api._matrix import _matrix_app_v1_ping # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = _matrix_app_v1_ping.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`_matrix_app_v1_ping`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/_matrix/_matrix_app_v1_ping.py)

=== "TypeScript"

    ```typescript
    import { MatrixAppV1Ping } from 'waldur-js-client';
    
    try {
      const response = await MatrixAppV1Ping({
      auth: "Token YOUR_API_TOKEN"
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Responses"

    **`200`** - No response body
    

---
