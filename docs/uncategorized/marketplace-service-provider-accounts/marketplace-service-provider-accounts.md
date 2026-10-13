# Marketplace Service Provider Accounts

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-service-provider-accounts/` | [List service provider accounts](#list-service-provider-accounts) |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-service-provider-accounts/{uuid}/` | [Retrieve a service provider account](#retrieve-a-service-provider-account) |
| <span class="http-badge http-put">PUT</span> | `/api/marketplace-service-provider-accounts/{uuid}/` | [Update a service provider account](#update-a-service-provider-account) |
| <span class="http-badge http-patch">PATCH</span> | `/api/marketplace-service-provider-accounts/{uuid}/` | [Update a service provider account](#update-a-service-provider-account) |
| <span class="http-badge http-delete">DELETE</span> | `/api/marketplace-service-provider-accounts/{uuid}/` | [Delete a service provider account](#delete-a-service-provider-account) |

---

### List service provider accounts


        Returns a paginated list of the accounts a service provider holds for its users --
        one per user per provider, shared by every offering of that provider.
        Scoped to providers whose organization the caller can see.
        


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-service-provider-accounts/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.offering_user_o_enum import OfferingUserOEnum # (1)
    from waldur_api_client.models.offering_user_state import OfferingUserState # (2)
    from waldur_api_client.models.runtime_state_enum import RuntimeStateEnum # (3)
    from waldur_api_client.models.service_provider_account_field_enum import ServiceProviderAccountFieldEnum # (4)
    from waldur_api_client.api.marketplace_service_provider_accounts import marketplace_service_provider_accounts_list # (5)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_service_provider_accounts_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`OfferingUserOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/offering_user_o_enum.py)
    2.  **Model Source:** [`OfferingUserState`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/offering_user_state.py)
    3.  **Model Source:** [`RuntimeStateEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/runtime_state_enum.py)
    4.  **Model Source:** [`ServiceProviderAccountFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/service_provider_account_field_enum.py)
    5.  **API Source:** [`marketplace_service_provider_accounts_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_service_provider_accounts/marketplace_service_provider_accounts_list.py)

=== "TypeScript"

    ```typescript
    import { marketplaceServiceProviderAccountsList } from 'waldur-js-client';
    
    try {
      const response = await marketplaceServiceProviderAccountsList({
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
    | `created` | string (date-time) | Created after |
    | `created_before` | string (date-time) | Created before |
    | `customer_uuid` | string (uuid) | Provider organization UUID |
    | `field` | array |  |
    | `is_restricted` | boolean | Is restricted |
    | `modified` | string (date-time) | Modified after |
    | `modified_before` | string (date-time) | Modified before |
    | `o` | array | Ordering<br><br> |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `provider_uuid` | string (uuid) | Service provider UUID |
    | `query` | string | Search by username, user name, UID or primary GID |
    | `runtime_state` | array | Account runtime state<br><br> |
    | `state` | array | Account state<br><br> |
    | `user_username` | string | User username |
    | `user_uuid` | string (uuid) | User UUID |
    | `username` | string | Username |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `service_provider` | string (uri) |  |
    | `service_provider_uuid` | string (uuid) |  |
    | `service_provider_name` | string |  |
    | `user` | string (uri) |  |
    | `user_uuid` | string (uuid) |  |
    | `user_username` | string |  |
    | `user_full_name` | string |  |
    | `user_email` | string |  |
    | `username` | string |  |
    | `state` | any |  |
    | `runtime_state` | any | Operational/access state of the user account. Separate from lifecycle state; can be set by the service provider at any time. |
    | `is_restricted` | boolean |  |
    | `service_provider_comment` | string | Additional comment for pending states like validation or account linking |
    | `service_provider_comment_url` | string (uri) | URL link for additional information or actions related to service provider comment |
    | `uidnumber` | integer |  |
    | `primarygroup` | integer |  |
    | `login_shell` | string |  |
    | `home_directory` | string |  |
    | `offering_count` | integer |  |

---

### Retrieve a service provider account

Returns one provider account, including its POSIX identity and the number of offering accounts reading through it.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-service-provider-accounts/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.service_provider_account_field_enum import ServiceProviderAccountFieldEnum # (1)
    from waldur_api_client.api.marketplace_service_provider_accounts import marketplace_service_provider_accounts_retrieve # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_service_provider_accounts_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ServiceProviderAccountFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/service_provider_account_field_enum.py)
    2.  **API Source:** [`marketplace_service_provider_accounts_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_service_provider_accounts/marketplace_service_provider_accounts_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceServiceProviderAccountsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceServiceProviderAccountsRetrieve({
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

    | Name | Type |
    |---|---|
    | `field` | array |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `service_provider` | string (uri) |  |
    | `service_provider_uuid` | string (uuid) |  |
    | `service_provider_name` | string |  |
    | `user` | string (uri) |  |
    | `user_uuid` | string (uuid) |  |
    | `user_username` | string |  |
    | `user_full_name` | string |  |
    | `user_email` | string |  |
    | `username` | string |  |
    | `state` | any |  |
    | `runtime_state` | any | Operational/access state of the user account. Separate from lifecycle state; can be set by the service provider at any time. |
    | `is_restricted` | boolean |  |
    | `service_provider_comment` | string | Additional comment for pending states like validation or account linking |
    | `service_provider_comment_url` | string (uri) | URL link for additional information or actions related to service provider comment |
    | `uidnumber` | integer |  |
    | `primarygroup` | integer |  |
    | `login_shell` | string |  |
    | `home_directory` | string |  |
    | `offering_count` | integer |  |

---

### Update a service provider account


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/marketplace-service-provider-accounts/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.service_provider_account_request import ServiceProviderAccountRequest # (1)
    from waldur_api_client.api.marketplace_service_provider_accounts import marketplace_service_provider_accounts_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ServiceProviderAccountRequest()
    response = marketplace_service_provider_accounts_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ServiceProviderAccountRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/service_provider_account_request.py)
    2.  **API Source:** [`marketplace_service_provider_accounts_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_service_provider_accounts/marketplace_service_provider_accounts_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceServiceProviderAccountsUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceServiceProviderAccountsUpdate({
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

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `username` | string |  |  |
    | `runtime_state` | any |  | Operational/access state of the user account. Separate from lifecycle state; can be set by the service provider at any time. |
    | `service_provider_comment` | string |  | Additional comment for pending states like validation or account linking |
    | `service_provider_comment_url` | string (uri) |  | URL link for additional information or actions related to service provider comment |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `service_provider` | string (uri) |  |
    | `service_provider_uuid` | string (uuid) |  |
    | `service_provider_name` | string |  |
    | `user` | string (uri) |  |
    | `user_uuid` | string (uuid) |  |
    | `user_username` | string |  |
    | `user_full_name` | string |  |
    | `user_email` | string |  |
    | `username` | string |  |
    | `state` | any |  |
    | `runtime_state` | any | Operational/access state of the user account. Separate from lifecycle state; can be set by the service provider at any time. |
    | `is_restricted` | boolean |  |
    | `service_provider_comment` | string | Additional comment for pending states like validation or account linking |
    | `service_provider_comment_url` | string (uri) | URL link for additional information or actions related to service provider comment |
    | `uidnumber` | integer |  |
    | `primarygroup` | integer |  |
    | `login_shell` | string |  |
    | `home_directory` | string |  |
    | `offering_count` | integer |  |

---

### Update a service provider account


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/marketplace-service-provider-accounts/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_service_provider_account_request import PatchedServiceProviderAccountRequest # (1)
    from waldur_api_client.api.marketplace_service_provider_accounts import marketplace_service_provider_accounts_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedServiceProviderAccountRequest()
    response = marketplace_service_provider_accounts_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedServiceProviderAccountRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_service_provider_account_request.py)
    2.  **API Source:** [`marketplace_service_provider_accounts_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_service_provider_accounts/marketplace_service_provider_accounts_partial_update.py)

=== "TypeScript"

    ```typescript
    import { marketplaceServiceProviderAccountsPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceServiceProviderAccountsPartialUpdate({
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

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `username` | string |  |  |
    | `runtime_state` | any |  | Operational/access state of the user account. Separate from lifecycle state; can be set by the service provider at any time. |
    | `service_provider_comment` | string |  | Additional comment for pending states like validation or account linking |
    | `service_provider_comment_url` | string (uri) |  | URL link for additional information or actions related to service provider comment |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `service_provider` | string (uri) |  |
    | `service_provider_uuid` | string (uuid) |  |
    | `service_provider_name` | string |  |
    | `user` | string (uri) |  |
    | `user_uuid` | string (uuid) |  |
    | `user_username` | string |  |
    | `user_full_name` | string |  |
    | `user_email` | string |  |
    | `username` | string |  |
    | `state` | any |  |
    | `runtime_state` | any | Operational/access state of the user account. Separate from lifecycle state; can be set by the service provider at any time. |
    | `is_restricted` | boolean |  |
    | `service_provider_comment` | string | Additional comment for pending states like validation or account linking |
    | `service_provider_comment_url` | string (uri) | URL link for additional information or actions related to service provider comment |
    | `uidnumber` | integer |  |
    | `primarygroup` | integer |  |
    | `login_shell` | string |  |
    | `home_directory` | string |  |
    | `offering_count` | integer |  |

---

### Delete a service provider account

Refused while offering accounts still read through this record.


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/marketplace-service-provider-accounts/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_service_provider_accounts import marketplace_service_provider_accounts_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_service_provider_accounts_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_service_provider_accounts_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_service_provider_accounts/marketplace_service_provider_accounts_destroy.py)

=== "TypeScript"

    ```typescript
    import { marketplaceServiceProviderAccountsDestroy } from 'waldur-js-client';
    
    try {
      const response = await marketplaceServiceProviderAccountsDestroy({
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
