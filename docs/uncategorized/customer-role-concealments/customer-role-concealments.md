# Customer Role Concealments

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/customer-role-concealments/` | [List Customer Role Concealments](#list-customer-role-concealments) |
| <span class="http-badge http-get">GET</span> | `/api/customer-role-concealments/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/customer-role-concealments/` | [Create](#create) |
| <span class="http-badge http-delete">DELETE</span> | `/api/customer-role-concealments/{uuid}/` | [Delete](#delete) |

---

### List Customer Role Concealments


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/customer-role-concealments/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.customer_role_concealments import customer_role_concealments_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = customer_role_concealments_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`customer_role_concealments_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/customer_role_concealments/customer_role_concealments_list.py)

=== "TypeScript"

    ```typescript
    import { customerRoleConcealmentsList } from 'waldur-js-client';
    
    try {
      const response = await customerRoleConcealmentsList({
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
    | `role_uuid` | string (uuid) | Role UUID |
    | `scope_uuid` | string (uuid) | Customer (scope) UUID |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `role` | string (uuid) |
    | `role_name` | string |
    | `customer_uuid` | string |
    | `customer_name` | string |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/customer-role-concealments/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.customer_role_concealments import customer_role_concealments_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = customer_role_concealments_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`customer_role_concealments_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/customer_role_concealments/customer_role_concealments_retrieve.py)

=== "TypeScript"

    ```typescript
    import { customerRoleConcealmentsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await customerRoleConcealmentsRetrieve({
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
    | `role` | string (uuid) |
    | `role_name` | string |
    | `customer_uuid` | string |
    | `customer_name` | string |

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/customer-role-concealments/ \
      Authorization:"Token YOUR_API_TOKEN" \
      role="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      customer="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.customer_role_concealment_request import CustomerRoleConcealmentRequest # (1)
    from waldur_api_client.api.customer_role_concealments import customer_role_concealments_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = CustomerRoleConcealmentRequest(
        role="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        customer="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = customer_role_concealments_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`CustomerRoleConcealmentRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/customer_role_concealment_request.py)
    2.  **API Source:** [`customer_role_concealments_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/customer_role_concealments/customer_role_concealments_create.py)

=== "TypeScript"

    ```typescript
    import { customerRoleConcealmentsCreate } from 'waldur-js-client';
    
    try {
      const response = await customerRoleConcealmentsCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "role": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "customer": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `role` | string (uuid) | ✓ |
    | `customer` | string (uuid) | ✓ |


=== "Responses"

    **`201`** - 
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `role` | string (uuid) |
    | `role_name` | string |
    | `customer_uuid` | string |
    | `customer_name` | string |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/customer-role-concealments/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.customer_role_concealments import customer_role_concealments_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = customer_role_concealments_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`customer_role_concealments_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/customer_role_concealments/customer_role_concealments_destroy.py)

=== "TypeScript"

    ```typescript
    import { customerRoleConcealmentsDestroy } from 'waldur-js-client';
    
    try {
      const response = await customerRoleConcealmentsDestroy({
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

    **`204`** - No response body
    

---
