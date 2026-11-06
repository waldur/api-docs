# Marketplace User Offering Consents

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-user-offering-consents/` | [List user offering consents](#list-user-offering-consents) |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-user-offering-consents/{uuid}/` | [Retrieve a user offering consent](#retrieve-a-user-offering-consent) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-user-offering-consents/` | [Grant consent to an offering's Terms of Service](#grant-consent-to-an-offerings-terms-of-service) |
| **Other Actions** | | |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-user-offering-consents/{uuid}/revoke/` | [Revoke consent to Terms of Service](#revoke-consent-to-terms-of-service) |

---
## Core CRUD


### List user offering consents

Returns a paginated list of Terms of Service consents for the current user. Staff and support users can see all consents.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-user-offering-consents/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.user_offering_consent_o_enum import UserOfferingConsentOEnum # (1)
    from waldur_api_client.api.marketplace_user_offering_consents import marketplace_user_offering_consents_list # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_user_offering_consents_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`UserOfferingConsentOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/user_offering_consent_o_enum.py)
    2.  **API Source:** [`marketplace_user_offering_consents_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_user_offering_consents/marketplace_user_offering_consents_list.py)

=== "TypeScript"

    ```typescript
    import { marketplaceUserOfferingConsentsList } from 'waldur-js-client';
    
    try {
      const response = await marketplaceUserOfferingConsentsList({
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
    | `has_consent` | boolean | Has consent |
    | `o` | array | Ordering<br><br> |
    | `offering` | string (uri) | Offering URL |
    | `offering_uuid` | string (uuid) | Offering UUID |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `requires_reconsent` | boolean | Requires reconsent |
    | `user` | string (uri) | User URL |
    | `user_uuid` | string (uuid) | User UUID |
    | `version` | string | Version |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `user_uuid` | string (uuid) |  |
    | `offering_uuid` | string (uuid) |  |
    | `agreement_date` | string (date-time) |  |
    | `version` | string |  |
    | `revocation_date` | string (date-time) |  |
    | `created` | string (date-time) |  |
    | `user_username` | string | Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters |
    | `user_full_name` | string |  |
    | `user_email` | string (email) |  |
    | `offering_name` | string |  |
    | `offering_slug` | string |  |
    | `offering_url` | string (uri) |  |
    | `modified` | string (date-time) |  |
    | `has_consent` | boolean |  |
    | `requires_reconsent` | boolean |  |
    | `collected_attributes` | array of strings | List of user attributes that will be shared with service provider |


=== "Authorization"

    Any signed-in user.
    
    The caller's own consents. Staff and support see all.

---

### Retrieve a user offering consent

Returns the details of a specific consent record.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-user-offering-consents/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_user_offering_consents import marketplace_user_offering_consents_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_user_offering_consents_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_user_offering_consents_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_user_offering_consents/marketplace_user_offering_consents_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceUserOfferingConsentsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceUserOfferingConsentsRetrieve({
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
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `user_uuid` | string (uuid) |  |
    | `offering_uuid` | string (uuid) |  |
    | `agreement_date` | string (date-time) |  |
    | `version` | string |  |
    | `revocation_date` | string (date-time) |  |
    | `created` | string (date-time) |  |
    | `user_username` | string | Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters |
    | `user_full_name` | string |  |
    | `user_email` | string (email) |  |
    | `offering_name` | string |  |
    | `offering_slug` | string |  |
    | `offering_url` | string (uri) |  |
    | `modified` | string (date-time) |  |
    | `has_consent` | boolean |  |
    | `requires_reconsent` | boolean |  |
    | `collected_attributes` | array of strings | List of user attributes that will be shared with service provider |


=== "Authorization"

    Any signed-in user.
    
    The caller's own consents. Staff and support see all.

---

### Grant consent to an offering's Terms of Service

Creates a consent record for the current user and a specific offering. This indicates that the user has accepted the active Terms of Service for that offering. If a consent already exists (even if revoked), it will be reactivated and updated with the current ToS version.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-user-offering-consents/ \
      Authorization:"Token YOUR_API_TOKEN" \
      offering="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.user_offering_consent_create_request import UserOfferingConsentCreateRequest # (1)
    from waldur_api_client.api.marketplace_user_offering_consents import marketplace_user_offering_consents_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = UserOfferingConsentCreateRequest(
        offering="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = marketplace_user_offering_consents_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`UserOfferingConsentCreateRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/user_offering_consent_create_request.py)
    2.  **API Source:** [`marketplace_user_offering_consents_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_user_offering_consents/marketplace_user_offering_consents_create.py)

=== "TypeScript"

    ```typescript
    import { marketplaceUserOfferingConsentsCreate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceUserOfferingConsentsCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "offering": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `offering` | string (uuid) | ✓ |


=== "Responses"

    **`201`** - 
    
    | Field | Type |
    |---|---|
    | `offering` | string (uuid) |


=== "Authorization"

    A consent of the caller's own, to the offering named in the request.

---

## Other Actions


### Revoke consent to Terms of Service

Revokes a user's consent to the Terms of Service for an offering. The consent record is marked with a revocation date, and the user may lose access to related resources if consent is required.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-user-offering-consents/a1b2c3d4-e5f6-7890-abcd-ef1234567890/revoke/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_user_offering_consents import marketplace_user_offering_consents_revoke # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_user_offering_consents_revoke.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_user_offering_consents_revoke`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_user_offering_consents/marketplace_user_offering_consents_revoke.py)

=== "TypeScript"

    ```typescript
    import { marketplaceUserOfferingConsentsRevoke } from 'waldur-js-client';
    
    try {
      const response = await marketplaceUserOfferingConsentsRevoke({
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
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `user_uuid` | string (uuid) |  |
    | `offering_uuid` | string (uuid) |  |
    | `agreement_date` | string (date-time) |  |
    | `version` | string |  |
    | `revocation_date` | string (date-time) |  |
    | `created` | string (date-time) |  |
    | `user_username` | string | Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters |
    | `user_full_name` | string |  |
    | `user_email` | string (email) |  |
    | `offering_name` | string |  |
    | `offering_slug` | string |  |
    | `offering_url` | string (uri) |  |
    | `modified` | string (date-time) |  |
    | `has_consent` | boolean |  |
    | `requires_reconsent` | boolean |  |
    | `collected_attributes` | array of strings | List of user attributes that will be shared with service provider |


=== "Authorization"

    Any of:
    
    - Staff.
    - The consent's user.

---
