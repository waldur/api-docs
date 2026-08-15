# Credit Transactions

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/credit-transactions/` | [List Credit Transactions](#list-credit-transactions) |
| <span class="http-badge http-get">GET</span> | `/api/credit-transactions/{uuid}/` | [Retrieve](#retrieve) |

---

### List Credit Transactions


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/credit-transactions/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.backend_resource_req_o_enum import BackendResourceReqOEnum # (1)
    from waldur_api_client.api.credit_transactions import credit_transactions_list # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = credit_transactions_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`BackendResourceReqOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/backend_resource_req_o_enum.py)
    2.  **API Source:** [`credit_transactions_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/credit_transactions/credit_transactions_list.py)

=== "TypeScript"

    ```typescript
    import { creditTransactionsList } from 'waldur-js-client';
    
    try {
      const response = await creditTransactionsList({
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
    | `credit_uuid` | string (uuid) |  |
    | `customer_uuid` | string (uuid) |  |
    | `o` | array | Ordering<br><br> |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `transaction_type` | string |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `created` | string (date-time) |
    | `amount` | string (decimal) |
    | `transaction_type` | string |
    | `transaction_type_display` | string |
    | `comment` | string |
    | `customer_uuid` | string (uuid) |
    | `customer_name` | string |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/credit-transactions/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.credit_transactions import credit_transactions_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = credit_transactions_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`credit_transactions_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/credit_transactions/credit_transactions_retrieve.py)

=== "TypeScript"

    ```typescript
    import { creditTransactionsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await creditTransactionsRetrieve({
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
    | `amount` | string (decimal) |
    | `transaction_type` | string |
    | `transaction_type_display` | string |
    | `comment` | string |
    | `customer_uuid` | string (uuid) |
    | `customer_name` | string |

---
