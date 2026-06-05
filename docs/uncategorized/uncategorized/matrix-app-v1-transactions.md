# Matrix App V1 Transactions

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-put">PUT</span> | `/_matrix/app/v1/transactions/{txn_id}` | [Matrix Application Service transaction webhook](#matrix-application-service-transaction-webhook) |

---

### Matrix Application Service transaction webhook

Receives event transactions from the Matrix homeserver. Authenticated via hs_token in the Authorization header.


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/_matrix/app/v1/transactions/string-value \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api._matrix import _matrix_app_v1_transactions_update # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = _matrix_app_v1_transactions_update.sync(
        txn_id="string-value",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`_matrix_app_v1_transactions_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/_matrix/_matrix_app_v1_transactions_update.py)

=== "TypeScript"

    ```typescript
    import { MatrixAppV1TransactionsUpdate } from 'waldur-js-client';
    
    try {
      const response = await MatrixAppV1TransactionsUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "txn_id": "string-value"
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
    | `txn_id` | string | ✓ |


=== "Responses"

    **`200`** - No response body
    

---
