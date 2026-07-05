# Customer Affiliates

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/customer-affiliates/` | [List Customer Affiliates](#list-customer-affiliates) |
| <span class="http-badge http-get">GET</span> | `/api/customer-affiliates/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/customer-affiliates/` | [Create](#create) |
| <span class="http-badge http-put">PUT</span> | `/api/customer-affiliates/{uuid}/` | [Update](#update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/customer-affiliates/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-delete">DELETE</span> | `/api/customer-affiliates/{uuid}/` | [Delete](#delete) |
| **Other Actions** | | |
| <span class="http-badge http-get">GET</span> | `/api/customer-affiliates/{uuid}/accruals/` | [Accruals](#accruals) |
| <span class="http-badge http-get">GET</span> | `/api/customer-affiliates/{uuid}/earnings/` | [Earnings](#earnings) |

---
## Core CRUD


### List Customer Affiliates


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/customer-affiliates/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.customer_affiliate_o_enum import CustomerAffiliateOEnum # (1)
    from waldur_api_client.api.customer_affiliates import customer_affiliates_list # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = customer_affiliates_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`CustomerAffiliateOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/customer_affiliate_o_enum.py)
    2.  **API Source:** [`customer_affiliates_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/customer_affiliates/customer_affiliates_list.py)

=== "TypeScript"

    ```typescript
    import { customerAffiliatesList } from 'waldur-js-client';
    
    try {
      const response = await customerAffiliatesList({
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
    | `affiliate_name` | string |  |
    | `affiliate_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `is_active` | boolean |  |
    | `o` | array | Ordering<br><br> |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `url` | string (uri) |
    | `customer` | string (uri) |
    | `customer_name` | string |
    | `customer_uuid` | string (uuid) |
    | `affiliate` | string (uri) |
    | `affiliate_name` | string |
    | `affiliate_uuid` | string (uuid) |
    | `fee_percent` | string (decimal) |
    | `is_active` | boolean |
    | `start_date` | string (date) |
    | `end_date` | string (date) |
    | `total_earned` | number (double) |
    | `created` | string (date-time) |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/customer-affiliates/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.customer_affiliates import customer_affiliates_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = customer_affiliates_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`customer_affiliates_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/customer_affiliates/customer_affiliates_retrieve.py)

=== "TypeScript"

    ```typescript
    import { customerAffiliatesRetrieve } from 'waldur-js-client';
    
    try {
      const response = await customerAffiliatesRetrieve({
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
    | `url` | string (uri) |
    | `customer` | string (uri) |
    | `customer_name` | string |
    | `customer_uuid` | string (uuid) |
    | `affiliate` | string (uri) |
    | `affiliate_name` | string |
    | `affiliate_uuid` | string (uuid) |
    | `fee_percent` | string (decimal) |
    | `is_active` | boolean |
    | `start_date` | string (date) |
    | `end_date` | string (date) |
    | `total_earned` | number (double) |
    | `created` | string (date-time) |

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/customer-affiliates/ \
      Authorization:"Token YOUR_API_TOKEN" \
      customer="https://api.example.com/api/customer/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      affiliate="https://api.example.com/api/affiliate/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.create_customer_affiliate_request import CreateCustomerAffiliateRequest # (1)
    from waldur_api_client.api.customer_affiliates import customer_affiliates_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = CreateCustomerAffiliateRequest(
        customer="https://api.example.com/api/customer/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        affiliate="https://api.example.com/api/affiliate/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    )
    response = customer_affiliates_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`CreateCustomerAffiliateRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/create_customer_affiliate_request.py)
    2.  **API Source:** [`customer_affiliates_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/customer_affiliates/customer_affiliates_create.py)

=== "TypeScript"

    ```typescript
    import { customerAffiliatesCreate } from 'waldur-js-client';
    
    try {
      const response = await customerAffiliatesCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "customer": "https://api.example.com/api/customer/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "affiliate": "https://api.example.com/api/affiliate/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
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
    | `customer` | string (uri) | ✓ |
    | `affiliate` | string (uri) | ✓ |
    | `fee_percent` | string (decimal) |  |
    | `is_active` | boolean |  |
    | `start_date` | string (date) |  |
    | `end_date` | string (date) |  |


=== "Responses"

    **`201`** - 
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `url` | string (uri) |
    | `customer` | string (uri) |
    | `customer_name` | string |
    | `customer_uuid` | string (uuid) |
    | `affiliate` | string (uri) |
    | `affiliate_name` | string |
    | `affiliate_uuid` | string (uuid) |
    | `fee_percent` | string (decimal) |
    | `is_active` | boolean |
    | `start_date` | string (date) |
    | `end_date` | string (date) |
    | `total_earned` | number (double) |
    | `created` | string (date-time) |

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/customer-affiliates/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      customer="https://api.example.com/api/customer/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      affiliate="https://api.example.com/api/affiliate/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.create_customer_affiliate_request import CreateCustomerAffiliateRequest # (1)
    from waldur_api_client.api.customer_affiliates import customer_affiliates_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = CreateCustomerAffiliateRequest(
        customer="https://api.example.com/api/customer/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        affiliate="https://api.example.com/api/affiliate/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    )
    response = customer_affiliates_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`CreateCustomerAffiliateRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/create_customer_affiliate_request.py)
    2.  **API Source:** [`customer_affiliates_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/customer_affiliates/customer_affiliates_update.py)

=== "TypeScript"

    ```typescript
    import { customerAffiliatesUpdate } from 'waldur-js-client';
    
    try {
      const response = await customerAffiliatesUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "customer": "https://api.example.com/api/customer/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "affiliate": "https://api.example.com/api/affiliate/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
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


=== "Request Body (required)"

    | Field | Type | Required |
    |---|---|---|
    | `customer` | string (uri) | ✓ |
    | `affiliate` | string (uri) | ✓ |
    | `fee_percent` | string (decimal) |  |
    | `is_active` | boolean |  |
    | `start_date` | string (date) |  |
    | `end_date` | string (date) |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `url` | string (uri) |
    | `customer` | string (uri) |
    | `customer_name` | string |
    | `customer_uuid` | string (uuid) |
    | `affiliate` | string (uri) |
    | `affiliate_name` | string |
    | `affiliate_uuid` | string (uuid) |
    | `fee_percent` | string (decimal) |
    | `is_active` | boolean |
    | `start_date` | string (date) |
    | `end_date` | string (date) |
    | `total_earned` | number (double) |
    | `created` | string (date-time) |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/customer-affiliates/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_create_customer_affiliate_request import PatchedCreateCustomerAffiliateRequest # (1)
    from waldur_api_client.api.customer_affiliates import customer_affiliates_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedCreateCustomerAffiliateRequest()
    response = customer_affiliates_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedCreateCustomerAffiliateRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_create_customer_affiliate_request.py)
    2.  **API Source:** [`customer_affiliates_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/customer_affiliates/customer_affiliates_partial_update.py)

=== "TypeScript"

    ```typescript
    import { customerAffiliatesPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await customerAffiliatesPartialUpdate({
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


=== "Request Body"

    | Field | Type | Required |
    |---|---|---|
    | `customer` | string (uri) |  |
    | `affiliate` | string (uri) |  |
    | `fee_percent` | string (decimal) |  |
    | `is_active` | boolean |  |
    | `start_date` | string (date) |  |
    | `end_date` | string (date) |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `url` | string (uri) |
    | `customer` | string (uri) |
    | `customer_name` | string |
    | `customer_uuid` | string (uuid) |
    | `affiliate` | string (uri) |
    | `affiliate_name` | string |
    | `affiliate_uuid` | string (uuid) |
    | `fee_percent` | string (decimal) |
    | `is_active` | boolean |
    | `start_date` | string (date) |
    | `end_date` | string (date) |
    | `total_earned` | number (double) |
    | `created` | string (date-time) |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/customer-affiliates/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.customer_affiliates import customer_affiliates_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = customer_affiliates_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`customer_affiliates_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/customer_affiliates/customer_affiliates_destroy.py)

=== "TypeScript"

    ```typescript
    import { customerAffiliatesDestroy } from 'waldur-js-client';
    
    try {
      const response = await customerAffiliatesDestroy({
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

## Other Actions


### Accruals

List fees accrued from this affiliate link. Exposes the fee amount and invoice period only — never the referred customer's invoice contents.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/customer-affiliates/a1b2c3d4-e5f6-7890-abcd-ef1234567890/accruals/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.customer_affiliate_o_enum import CustomerAffiliateOEnum # (1)
    from waldur_api_client.api.customer_affiliates import customer_affiliates_accruals_list # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = customer_affiliates_accruals_list.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`CustomerAffiliateOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/customer_affiliate_o_enum.py)
    2.  **API Source:** [`customer_affiliates_accruals_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/customer_affiliates/customer_affiliates_accruals_list.py)

=== "TypeScript"

    ```typescript
    import { customerAffiliatesAccrualsList } from 'waldur-js-client';
    
    try {
      const response = await customerAffiliatesAccrualsList({
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


=== "Query Parameters"

    | Name | Type | Description |
    |---|---|---|
    | `affiliate_name` | string |  |
    | `affiliate_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `is_active` | boolean |  |
    | `o` | array | Ordering<br><br> |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `amount` | string (decimal) |
    | `customer_name` | string |
    | `affiliate_uuid` | string (uuid) |
    | `invoice_year` | integer |
    | `invoice_month` | integer |
    | `created` | string (date-time) |

---

### Earnings

Earnings summary of this affiliate link: lifetime total, per-month series and the affiliate organization's withdrawable credit balance.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/customer-affiliates/a1b2c3d4-e5f6-7890-abcd-ef1234567890/earnings/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.customer_affiliates import customer_affiliates_earnings_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = customer_affiliates_earnings_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`customer_affiliates_earnings_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/customer_affiliates/customer_affiliates_earnings_retrieve.py)

=== "TypeScript"

    ```typescript
    import { customerAffiliatesEarningsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await customerAffiliatesEarningsRetrieve({
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
    | `total_earned` | string (decimal) |
    | `withdrawable_balance` | string (decimal) |
    | `per_month` | array of objects |
    | `per_month.year` | integer |
    | `per_month.month` | integer |
    | `per_month.amount` | string (decimal) |

---
