# Support

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/support-canned-responses/` | [List Support Canned Responses](#list-support-canned-responses) |
| <span class="http-badge http-get">GET</span> | `/api/support-canned-responses/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-get">GET</span> | `/api/support-issue-links/` | [List Support Issue Links](#list-support-issue-links) |
| <span class="http-badge http-get">GET</span> | `/api/support-issue-links/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-get">GET</span> | `/api/support-issue-tags/` | [List Support Issue Tags](#list-support-issue-tags) |
| <span class="http-badge http-get">GET</span> | `/api/support-issue-tags/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-get">GET</span> | `/api/support-saved-filters/` | [List Support Saved Filters](#list-support-saved-filters) |
| <span class="http-badge http-get">GET</span> | `/api/support-saved-filters/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-get">GET</span> | `/api/support/settings/atlassian/current_settings/` | [Get current Atlassian settings (masked secrets)](#get-current-atlassian-settings-masked-secrets) |
| <span class="http-badge http-get">GET</span> | `/api/support/settings/atlassian/` | [List Support Settings Atlassian](#list-support-settings-atlassian) |
| <span class="http-badge http-get">GET</span> | `/api/support/settings/atlassian/{id}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/support-canned-responses/` | [Create](#create) |
| <span class="http-badge http-post">POST</span> | `/api/support-canned-responses/{uuid}/render/` | [Render a canned response with context variables](#render-a-canned-response-with-context-variables) |
| <span class="http-badge http-post">POST</span> | `/api/support-issue-links/` | [Create](#create) |
| <span class="http-badge http-post">POST</span> | `/api/support-issue-tags/` | [Create](#create) |
| <span class="http-badge http-post">POST</span> | `/api/support-provider-webhook/{provider_uuid}/{backend_type}/` | [Webhook](#webhook) |
| <span class="http-badge http-post">POST</span> | `/api/support-saved-filters/` | [Create](#create) |
| <span class="http-badge http-post">POST</span> | `/api/support/settings/atlassian/` | [Create](#create) |
| <span class="http-badge http-post">POST</span> | `/api/support/settings/atlassian/discover_custom_fields/` | [Discover available custom fields](#discover-available-custom-fields) |
| <span class="http-badge http-post">POST</span> | `/api/support/settings/atlassian/discover_priorities/` | [Discover available priorities](#discover-available-priorities) |
| <span class="http-badge http-post">POST</span> | `/api/support/settings/atlassian/discover_projects/` | [Discover available Service Desk projects](#discover-available-service-desk-projects) |
| <span class="http-badge http-post">POST</span> | `/api/support/settings/atlassian/discover_request_types/` | [Discover request types for a selected project](#discover-request-types-for-a-selected-project) |
| <span class="http-badge http-post">POST</span> | `/api/support/settings/atlassian/preview_settings/` | [Generate preview of settings to be saved](#generate-preview-of-settings-to-be-saved) |
| <span class="http-badge http-post">POST</span> | `/api/support/settings/atlassian/save_settings/` | [Save selected settings to constance](#save-selected-settings-to-constance) |
| <span class="http-badge http-post">POST</span> | `/api/support/settings/atlassian/validate_credentials/` | [Validate Atlassian credentials without saving them](#validate-atlassian-credentials-without-saving-them) |
| <span class="http-badge http-put">PUT</span> | `/api/support-canned-responses/{uuid}/` | [Update](#update) |
| <span class="http-badge http-put">PUT</span> | `/api/support-issue-links/{uuid}/` | [Update](#update) |
| <span class="http-badge http-put">PUT</span> | `/api/support-issue-tags/{uuid}/` | [Update](#update) |
| <span class="http-badge http-put">PUT</span> | `/api/support-saved-filters/{uuid}/` | [Update](#update) |
| <span class="http-badge http-put">PUT</span> | `/api/support/settings/atlassian/{id}/` | [Update](#update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/support-canned-responses/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/support-issue-links/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/support-issue-tags/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/support-saved-filters/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/support/settings/atlassian/{id}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-delete">DELETE</span> | `/api/support-canned-responses/{uuid}/` | [Delete](#delete) |
| <span class="http-badge http-delete">DELETE</span> | `/api/support-issue-links/{uuid}/` | [Delete](#delete) |
| <span class="http-badge http-delete">DELETE</span> | `/api/support-issue-tags/{uuid}/` | [Delete](#delete) |
| <span class="http-badge http-delete">DELETE</span> | `/api/support-saved-filters/{uuid}/` | [Delete](#delete) |
| <span class="http-badge http-delete">DELETE</span> | `/api/support/settings/atlassian/{id}/` | [Delete](#delete) |

---

### List Support Canned Responses


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/support-canned-responses/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.support_canned_responses import support_canned_responses_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = support_canned_responses_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`support_canned_responses_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_canned_responses/support_canned_responses_list.py)

=== "TypeScript"

    ```typescript
    import { supportCannedResponsesList } from 'waldur-js-client';
    
    try {
      const response = await supportCannedResponsesList({
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
    | `category` | string |  |
    | `is_active` | boolean |  |
    | `name` | string |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `text` | string | Template text. Supports Django template syntax. |
    | `category` | string |  |
    | `is_active` | boolean |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/support-canned-responses/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.support_canned_responses import support_canned_responses_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = support_canned_responses_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`support_canned_responses_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_canned_responses/support_canned_responses_retrieve.py)

=== "TypeScript"

    ```typescript
    import { supportCannedResponsesRetrieve } from 'waldur-js-client';
    
    try {
      const response = await supportCannedResponsesRetrieve({
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
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `text` | string | Template text. Supports Django template syntax. |
    | `category` | string |  |
    | `is_active` | boolean |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### List Support Issue Links


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/support-issue-links/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.support_issue_links import support_issue_links_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = support_issue_links_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`support_issue_links_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_issue_links/support_issue_links_list.py)

=== "TypeScript"

    ```typescript
    import { supportIssueLinksList } from 'waldur-js-client';
    
    try {
      const response = await supportIssueLinksList({
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
    | `link_type` | string |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `source_uuid` | string (uuid) |  |
    | `target_uuid` | string (uuid) |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `url` | string (uri) |
    | `uuid` | string (uuid) |
    | `source` | string (uuid) |
    | `source_key` | string |
    | `target` | string (uuid) |
    | `target_key` | string |
    | `link_type` | string |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/support-issue-links/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.support_issue_links import support_issue_links_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = support_issue_links_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`support_issue_links_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_issue_links/support_issue_links_retrieve.py)

=== "TypeScript"

    ```typescript
    import { supportIssueLinksRetrieve } from 'waldur-js-client';
    
    try {
      const response = await supportIssueLinksRetrieve({
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
    | `url` | string (uri) |
    | `uuid` | string (uuid) |
    | `source` | string (uuid) |
    | `source_key` | string |
    | `target` | string (uuid) |
    | `target_key` | string |
    | `link_type` | string |

---

### List Support Issue Tags


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/support-issue-tags/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.support_issue_tags import support_issue_tags_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = support_issue_tags_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`support_issue_tags_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_issue_tags/support_issue_tags_list.py)

=== "TypeScript"

    ```typescript
    import { supportIssueTagsList } from 'waldur-js-client';
    
    try {
      const response = await supportIssueTagsList({
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
    | `name` | string |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `color` | string | Hex color code, e.g. #FF0000. |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/support-issue-tags/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.support_issue_tags import support_issue_tags_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = support_issue_tags_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`support_issue_tags_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_issue_tags/support_issue_tags_retrieve.py)

=== "TypeScript"

    ```typescript
    import { supportIssueTagsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await supportIssueTagsRetrieve({
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
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `color` | string | Hex color code, e.g. #FF0000. |

---

### List Support Saved Filters


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/support-saved-filters/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.support_saved_filters import support_saved_filters_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = support_saved_filters_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`support_saved_filters_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_saved_filters/support_saved_filters_list.py)

=== "TypeScript"

    ```typescript
    import { supportSavedFiltersList } from 'waldur-js-client';
    
    try {
      const response = await supportSavedFiltersList({
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
    | `is_shared` | boolean |  |
    | `name` | string |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `filter_params` | object (free-form) | Saved filter parameters as JSON. |
    | `is_shared` | boolean | If True, visible to all staff/support users. |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/support-saved-filters/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.support_saved_filters import support_saved_filters_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = support_saved_filters_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`support_saved_filters_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_saved_filters/support_saved_filters_retrieve.py)

=== "TypeScript"

    ```typescript
    import { supportSavedFiltersRetrieve } from 'waldur-js-client';
    
    try {
      const response = await supportSavedFiltersRetrieve({
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
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `filter_params` | object (free-form) | Saved filter parameters as JSON. |
    | `is_shared` | boolean | If True, visible to all staff/support users. |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Get current Atlassian settings (masked secrets)

Get current Atlassian settings (masked secrets).


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/support/settings/atlassian/current_settings/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.support import support_settings_atlassian_current_settings_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = support_settings_atlassian_current_settings_retrieve.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`support_settings_atlassian_current_settings_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support/support_settings_atlassian_current_settings_retrieve.py)

=== "TypeScript"

    ```typescript
    import { supportSettingsAtlassianCurrentSettingsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await supportSettingsAtlassianCurrentSettingsRetrieve({
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

### List Support Settings Atlassian


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/support/settings/atlassian/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.support import support_settings_atlassian_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = support_settings_atlassian_list.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`support_settings_atlassian_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support/support_settings_atlassian_list.py)

=== "TypeScript"

    ```typescript
    import { supportSettingsAtlassianList } from 'waldur-js-client';
    
    try {
      const response = await supportSettingsAtlassianList({
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


=== "Responses"

    **`200`** - No response body
    

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/support/settings/atlassian/123/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.support import support_settings_atlassian_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = support_settings_atlassian_retrieve.sync(
        id=123,
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`support_settings_atlassian_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support/support_settings_atlassian_retrieve.py)

=== "TypeScript"

    ```typescript
    import { supportSettingsAtlassianRetrieve } from 'waldur-js-client';
    
    try {
      const response = await supportSettingsAtlassianRetrieve({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "id": 123
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required | Description |
    |---|---|---|---|
    | `id` | integer | ✓ | A unique integer value identifying this issue. |


=== "Responses"

    **`200`** - No response body
    

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/support-canned-responses/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-support-canned-response" \
      text="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.canned_response_request import CannedResponseRequest # (1)
    from waldur_api_client.api.support_canned_responses import support_canned_responses_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = CannedResponseRequest(
        name="my-awesome-support-canned-response",
        text="string-value"
    )
    response = support_canned_responses_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`CannedResponseRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/canned_response_request.py)
    2.  **API Source:** [`support_canned_responses_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_canned_responses/support_canned_responses_create.py)

=== "TypeScript"

    ```typescript
    import { supportCannedResponsesCreate } from 'waldur-js-client';
    
    try {
      const response = await supportCannedResponsesCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "name": "my-awesome-support-canned-response",
        "text": "string-value"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Request Body (required)"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `name` | string | ✓ |  |
    | `text` | string | ✓ | Template text. Supports Django template syntax. |
    | `category` | string |  |  |
    | `is_active` | boolean |  |  |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `text` | string | Template text. Supports Django template syntax. |
    | `category` | string |  |
    | `is_active` | boolean |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Render a canned response with context variables


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/support-canned-responses/a1b2c3d4-e5f6-7890-abcd-ef1234567890/render/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.canned_response_render_request import CannedResponseRenderRequest # (1)
    from waldur_api_client.api.support_canned_responses import support_canned_responses_render # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = CannedResponseRenderRequest()
    response = support_canned_responses_render.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`CannedResponseRenderRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/canned_response_render_request.py)
    2.  **API Source:** [`support_canned_responses_render`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_canned_responses/support_canned_responses_render.py)

=== "TypeScript"

    ```typescript
    import { supportCannedResponsesRender } from 'waldur-js-client';
    
    try {
      const response = await supportCannedResponsesRender({
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
    | `context` | object (free-form) |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `rendered_text` | string |

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/support-issue-links/ \
      Authorization:"Token YOUR_API_TOKEN" \
      source="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      target="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.issue_link_request import IssueLinkRequest # (1)
    from waldur_api_client.api.support_issue_links import support_issue_links_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = IssueLinkRequest(
        source="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        target="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = support_issue_links_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`IssueLinkRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/issue_link_request.py)
    2.  **API Source:** [`support_issue_links_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_issue_links/support_issue_links_create.py)

=== "TypeScript"

    ```typescript
    import { supportIssueLinksCreate } from 'waldur-js-client';
    
    try {
      const response = await supportIssueLinksCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "source": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "target": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `source` | string (uuid) | ✓ |
    | `target` | string (uuid) | ✓ |
    | `link_type` | string |  |


=== "Responses"

    **`201`** - 
    
    | Field | Type |
    |---|---|
    | `url` | string (uri) |
    | `uuid` | string (uuid) |
    | `source` | string (uuid) |
    | `source_key` | string |
    | `target` | string (uuid) |
    | `target_key` | string |
    | `link_type` | string |

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/support-issue-tags/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-support-issue-tag"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.issue_tag_request import IssueTagRequest # (1)
    from waldur_api_client.api.support_issue_tags import support_issue_tags_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = IssueTagRequest(
        name="my-awesome-support-issue-tag"
    )
    response = support_issue_tags_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`IssueTagRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/issue_tag_request.py)
    2.  **API Source:** [`support_issue_tags_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_issue_tags/support_issue_tags_create.py)

=== "TypeScript"

    ```typescript
    import { supportIssueTagsCreate } from 'waldur-js-client';
    
    try {
      const response = await supportIssueTagsCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "name": "my-awesome-support-issue-tag"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Request Body (required)"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `name` | string | ✓ |  |
    | `color` | string |  | Hex color code, e.g. #FF0000. |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `color` | string | Hex color code, e.g. #FF0000. |

---

### Webhook


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/support-provider-webhook/a1b2c3d4-e5f6-7890-abcd-ef1234567890/string-value/ \
      Authorization:"Token YOUR_API_TOKEN" \
      event_type="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.webhook_payload_request import WebhookPayloadRequest # (1)
    from waldur_api_client.api.support_provider_webhook import support_provider_webhook # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = WebhookPayloadRequest(
        event_type="string-value"
    )
    response = support_provider_webhook.sync(
        backend_type="string-value",
        provider_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`WebhookPayloadRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/webhook_payload_request.py)
    2.  **API Source:** [`support_provider_webhook`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_provider_webhook/support_provider_webhook.py)

=== "TypeScript"

    ```typescript
    import { supportProviderWebhook } from 'waldur-js-client';
    
    try {
      const response = await supportProviderWebhook({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "backend_type": "string-value",
        "provider_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "event_type": "string-value"
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
    | `backend_type` | string | ✓ |
    | `provider_uuid` | string | ✓ |


=== "Request Body (required)"

    | Field | Type | Required |
    |---|---|---|
    | `event_type` | string | ✓ |
    | `issue_backend_id` | string |  |
    | `comment` | string |  |
    | `new_status` | string |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `event_type` | string |
    | `issue_backend_id` | string |
    | `comment` | string |
    | `new_status` | string |

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/support-saved-filters/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-support-saved-filter"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.saved_filter_request import SavedFilterRequest # (1)
    from waldur_api_client.api.support_saved_filters import support_saved_filters_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = SavedFilterRequest(
        name="my-awesome-support-saved-filter"
    )
    response = support_saved_filters_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`SavedFilterRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/saved_filter_request.py)
    2.  **API Source:** [`support_saved_filters_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_saved_filters/support_saved_filters_create.py)

=== "TypeScript"

    ```typescript
    import { supportSavedFiltersCreate } from 'waldur-js-client';
    
    try {
      const response = await supportSavedFiltersCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "name": "my-awesome-support-saved-filter"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Request Body (required)"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `name` | string | ✓ |  |
    | `filter_params` | object (free-form) |  | Saved filter parameters as JSON. |
    | `is_shared` | boolean |  | If True, visible to all staff/support users. |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `filter_params` | object (free-form) | Saved filter parameters as JSON. |
    | `is_shared` | boolean | If True, visible to all staff/support users. |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/support/settings/atlassian/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.support import support_settings_atlassian_create # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = support_settings_atlassian_create.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`support_settings_atlassian_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support/support_settings_atlassian_create.py)

=== "TypeScript"

    ```typescript
    import { supportSettingsAtlassianCreate } from 'waldur-js-client';
    
    try {
      const response = await supportSettingsAtlassianCreate({
      auth: "Token YOUR_API_TOKEN"
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Responses"

    **`201`** - No response body
    

---

### Discover available custom fields

Discover available custom fields.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/support/settings/atlassian/discover_custom_fields/ \
      Authorization:"Token YOUR_API_TOKEN" \
      api_url="https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      auth_method=null
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.discover_custom_fields_request_request import DiscoverCustomFieldsRequestRequest # (1)
    from waldur_api_client.api.support import support_settings_atlassian_discover_custom_fields # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = DiscoverCustomFieldsRequestRequest(
        api_url="https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        auth_method=null
    )
    response = support_settings_atlassian_discover_custom_fields.sync(
        client=client,
        body=body_data
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`DiscoverCustomFieldsRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/discover_custom_fields_request_request.py)
    2.  **API Source:** [`support_settings_atlassian_discover_custom_fields`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support/support_settings_atlassian_discover_custom_fields.py)

=== "TypeScript"

    ```typescript
    import { supportSettingsAtlassianDiscoverCustomFields } from 'waldur-js-client';
    
    try {
      const response = await supportSettingsAtlassianDiscoverCustomFields({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "api_url": "https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "auth_method": null
      }
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


=== "Request Body (required)"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `api_url` | string (uri) | ✓ | Atlassian API URL (e.g., https://your-domain.atlassian.net) |
    | `auth_method` | any | ✓ | Authentication method to use |
    | `email` | string (email) |  |  |
    | `token` | string |  | <br>_Constraints: write-only_ |
    | `personal_access_token` | string |  | <br>_Constraints: write-only_ |
    | `username` | string |  |  |
    | `password` | string |  | <br>_Constraints: write-only_ |
    | `verify_ssl` | boolean |  | <br>_Constraints: default: `True`_ |
    | `project_id` | string |  |  |
    | `request_type_id` | string |  | Optional: Filter fields by request type |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `id` | string |
    | `name` | string |
    | `clause_names` | array of strings |
    | `field_type` | string |
    | `required` | boolean |

---

### Discover available priorities

Discover available priorities.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/support/settings/atlassian/discover_priorities/ \
      Authorization:"Token YOUR_API_TOKEN" \
      api_url="https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      auth_method=null
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.discover_priorities_request_request import DiscoverPrioritiesRequestRequest # (1)
    from waldur_api_client.api.support import support_settings_atlassian_discover_priorities # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = DiscoverPrioritiesRequestRequest(
        api_url="https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        auth_method=null
    )
    response = support_settings_atlassian_discover_priorities.sync(
        client=client,
        body=body_data
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`DiscoverPrioritiesRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/discover_priorities_request_request.py)
    2.  **API Source:** [`support_settings_atlassian_discover_priorities`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support/support_settings_atlassian_discover_priorities.py)

=== "TypeScript"

    ```typescript
    import { supportSettingsAtlassianDiscoverPriorities } from 'waldur-js-client';
    
    try {
      const response = await supportSettingsAtlassianDiscoverPriorities({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "api_url": "https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "auth_method": null
      }
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


=== "Request Body (required)"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `api_url` | string (uri) | ✓ | Atlassian API URL (e.g., https://your-domain.atlassian.net) |
    | `auth_method` | any | ✓ | Authentication method to use |
    | `email` | string (email) |  |  |
    | `token` | string |  | <br>_Constraints: write-only_ |
    | `personal_access_token` | string |  | <br>_Constraints: write-only_ |
    | `username` | string |  |  |
    | `password` | string |  | <br>_Constraints: write-only_ |
    | `verify_ssl` | boolean |  | <br>_Constraints: default: `True`_ |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `id` | string |
    | `name` | string |
    | `description` | string |
    | `icon_url` | string (uri) |

---

### Discover available Service Desk projects

Discover available Service Desk projects.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/support/settings/atlassian/discover_projects/ \
      Authorization:"Token YOUR_API_TOKEN" \
      api_url="https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      auth_method=null
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.discover_projects_request_request import DiscoverProjectsRequestRequest # (1)
    from waldur_api_client.api.support import support_settings_atlassian_discover_projects # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = DiscoverProjectsRequestRequest(
        api_url="https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        auth_method=null
    )
    response = support_settings_atlassian_discover_projects.sync(
        client=client,
        body=body_data
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`DiscoverProjectsRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/discover_projects_request_request.py)
    2.  **API Source:** [`support_settings_atlassian_discover_projects`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support/support_settings_atlassian_discover_projects.py)

=== "TypeScript"

    ```typescript
    import { supportSettingsAtlassianDiscoverProjects } from 'waldur-js-client';
    
    try {
      const response = await supportSettingsAtlassianDiscoverProjects({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "api_url": "https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "auth_method": null
      }
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


=== "Request Body (required)"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `api_url` | string (uri) | ✓ | Atlassian API URL (e.g., https://your-domain.atlassian.net) |
    | `auth_method` | any | ✓ | Authentication method to use |
    | `email` | string (email) |  |  |
    | `token` | string |  | <br>_Constraints: write-only_ |
    | `personal_access_token` | string |  | <br>_Constraints: write-only_ |
    | `username` | string |  |  |
    | `password` | string |  | <br>_Constraints: write-only_ |
    | `verify_ssl` | boolean |  | <br>_Constraints: default: `True`_ |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `id` | string |
    | `key` | string |
    | `name` | string |
    | `description` | string |

---

### Discover request types for a selected project

Discover request types for a selected project.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/support/settings/atlassian/discover_request_types/ \
      Authorization:"Token YOUR_API_TOKEN" \
      api_url="https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      auth_method=null \
      project_id="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.discover_request_types_request_request import DiscoverRequestTypesRequestRequest # (1)
    from waldur_api_client.api.support import support_settings_atlassian_discover_request_types # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = DiscoverRequestTypesRequestRequest(
        api_url="https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        auth_method=null,
        project_id="string-value"
    )
    response = support_settings_atlassian_discover_request_types.sync(
        client=client,
        body=body_data
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`DiscoverRequestTypesRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/discover_request_types_request_request.py)
    2.  **API Source:** [`support_settings_atlassian_discover_request_types`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support/support_settings_atlassian_discover_request_types.py)

=== "TypeScript"

    ```typescript
    import { supportSettingsAtlassianDiscoverRequestTypes } from 'waldur-js-client';
    
    try {
      const response = await supportSettingsAtlassianDiscoverRequestTypes({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "api_url": "https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "auth_method": null,
        "project_id": "string-value"
      }
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


=== "Request Body (required)"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `api_url` | string (uri) | ✓ | Atlassian API URL (e.g., https://your-domain.atlassian.net) |
    | `auth_method` | any | ✓ | Authentication method to use |
    | `email` | string (email) |  |  |
    | `token` | string |  | <br>_Constraints: write-only_ |
    | `personal_access_token` | string |  | <br>_Constraints: write-only_ |
    | `username` | string |  |  |
    | `password` | string |  | <br>_Constraints: write-only_ |
    | `verify_ssl` | boolean |  | <br>_Constraints: default: `True`_ |
    | `project_id` | string | ✓ | Service Desk project ID or key |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `id` | string |
    | `name` | string |
    | `description` | string |
    | `issue_type_id` | string |

---

### Generate preview of settings to be saved

Generate preview of settings to be saved.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/support/settings/atlassian/preview_settings/ \
      Authorization:"Token YOUR_API_TOKEN" \
      api_url="https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      auth_method="api_token" \
      project_id="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.atlassian_settings_preview_request import AtlassianSettingsPreviewRequest # (1)
    from waldur_api_client.api.support import support_settings_atlassian_preview_settings # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = AtlassianSettingsPreviewRequest(
        api_url="https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        auth_method="api_token",
        project_id="string-value"
    )
    response = support_settings_atlassian_preview_settings.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`AtlassianSettingsPreviewRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/atlassian_settings_preview_request.py)
    2.  **API Source:** [`support_settings_atlassian_preview_settings`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support/support_settings_atlassian_preview_settings.py)

=== "TypeScript"

    ```typescript
    import { supportSettingsAtlassianPreviewSettings } from 'waldur-js-client';
    
    try {
      const response = await supportSettingsAtlassianPreviewSettings({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "api_url": "https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "auth_method": "api_token",
        "project_id": "string-value"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Request Body (required)"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `api_url` | string (uri) | ✓ |  |
    | `auth_method` | string | ✓ | <br>_Enum: `api_token`, `personal_access_token`, `basic`_ |
    | `email` | string (email) |  |  |
    | `token` | string |  | <br>_Constraints: write-only_ |
    | `personal_access_token` | string |  | <br>_Constraints: write-only_ |
    | `username` | string |  |  |
    | `password` | string |  | <br>_Constraints: write-only_ |
    | `verify_ssl` | boolean |  | <br>_Constraints: default: `True`_ |
    | `project_id` | string | ✓ |  |
    | `issue_types` | array of strings |  |  |
    | `support_type_mapping` | object (free-form) |  | Mapping from frontend types to backend request types |
    | `reporter_field` | string |  |  |
    | `impact_field` | string |  |  |
    | `organisation_field` | string |  |  |
    | `project_field` | string |  |  |
    | `affected_resource_field` | string |  |  |
    | `caller_field` | string |  |  |
    | `template_field` | string |  |  |
    | `sla_field` | string |  |  |
    | `resolution_sla_field` | string |  |  |
    | `satisfaction_field` | string |  |  |
    | `request_feedback_field` | string |  |  |
    | `waldur_backend_id_field` | string |  |  |
    | `default_offering_issue_type` | string |  | Default issue type for marketplace request-based orders |
    | `use_old_api` | boolean |  | <br>_Constraints: default: `False`_ |
    | `custom_field_mapping_enabled` | boolean |  | <br>_Constraints: default: `True`_ |


=== "Responses"

    **`200`** - No response body
    

---

### Save selected settings to constance

Save selected settings to constance.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/support/settings/atlassian/save_settings/ \
      Authorization:"Token YOUR_API_TOKEN" \
      api_url="https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      auth_method="api_token" \
      project_id="string-value" \
      confirm_save=true
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.atlassian_settings_save_request import AtlassianSettingsSaveRequest # (1)
    from waldur_api_client.api.support import support_settings_atlassian_save_settings # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = AtlassianSettingsSaveRequest(
        api_url="https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        auth_method="api_token",
        project_id="string-value",
        confirm_save=true
    )
    response = support_settings_atlassian_save_settings.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`AtlassianSettingsSaveRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/atlassian_settings_save_request.py)
    2.  **API Source:** [`support_settings_atlassian_save_settings`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support/support_settings_atlassian_save_settings.py)

=== "TypeScript"

    ```typescript
    import { supportSettingsAtlassianSaveSettings } from 'waldur-js-client';
    
    try {
      const response = await supportSettingsAtlassianSaveSettings({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "api_url": "https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "auth_method": "api_token",
        "project_id": "string-value",
        "confirm_save": true
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Request Body (required)"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `api_url` | string (uri) | ✓ |  |
    | `auth_method` | string | ✓ | <br>_Enum: `api_token`, `personal_access_token`, `basic`_ |
    | `email` | string (email) |  |  |
    | `token` | string |  | <br>_Constraints: write-only_ |
    | `personal_access_token` | string |  | <br>_Constraints: write-only_ |
    | `username` | string |  |  |
    | `password` | string |  | <br>_Constraints: write-only_ |
    | `verify_ssl` | boolean |  | <br>_Constraints: default: `True`_ |
    | `project_id` | string | ✓ |  |
    | `issue_types` | array of strings |  |  |
    | `support_type_mapping` | object (free-form) |  | Mapping from frontend types to backend request types |
    | `reporter_field` | string |  |  |
    | `impact_field` | string |  |  |
    | `organisation_field` | string |  |  |
    | `project_field` | string |  |  |
    | `affected_resource_field` | string |  |  |
    | `caller_field` | string |  |  |
    | `template_field` | string |  |  |
    | `sla_field` | string |  |  |
    | `resolution_sla_field` | string |  |  |
    | `satisfaction_field` | string |  |  |
    | `request_feedback_field` | string |  |  |
    | `waldur_backend_id_field` | string |  |  |
    | `default_offering_issue_type` | string |  | Default issue type for marketplace request-based orders |
    | `use_old_api` | boolean |  | <br>_Constraints: default: `False`_ |
    | `custom_field_mapping_enabled` | boolean |  | <br>_Constraints: default: `True`_ |
    | `confirm_save` | boolean | ✓ | Must be True to confirm saving settings |


=== "Responses"

    **`200`** - No response body
    

---

### Validate Atlassian credentials without saving them

Validate Atlassian credentials without saving them.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/support/settings/atlassian/validate_credentials/ \
      Authorization:"Token YOUR_API_TOKEN" \
      api_url="https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/" \
      auth_method=null
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.atlassian_credentials_request import AtlassianCredentialsRequest # (1)
    from waldur_api_client.api.support import support_settings_atlassian_validate_credentials # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = AtlassianCredentialsRequest(
        api_url="https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        auth_method=null
    )
    response = support_settings_atlassian_validate_credentials.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`AtlassianCredentialsRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/atlassian_credentials_request.py)
    2.  **API Source:** [`support_settings_atlassian_validate_credentials`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support/support_settings_atlassian_validate_credentials.py)

=== "TypeScript"

    ```typescript
    import { supportSettingsAtlassianValidateCredentials } from 'waldur-js-client';
    
    try {
      const response = await supportSettingsAtlassianValidateCredentials({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "api_url": "https://api.example.com/api/api-url/a1b2c3d4-e5f6-7890-abcd-ef1234567890/",
        "auth_method": null
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Request Body (required)"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `api_url` | string (uri) | ✓ | Atlassian API URL (e.g., https://your-domain.atlassian.net) |
    | `auth_method` | any | ✓ | Authentication method to use |
    | `email` | string (email) |  |  |
    | `token` | string |  | <br>_Constraints: write-only_ |
    | `personal_access_token` | string |  | <br>_Constraints: write-only_ |
    | `username` | string |  |  |
    | `password` | string |  | <br>_Constraints: write-only_ |
    | `verify_ssl` | boolean |  | <br>_Constraints: default: `True`_ |


=== "Responses"

    **`200`** - No response body
    

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/support-canned-responses/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-support-canned-response" \
      text="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.canned_response_request import CannedResponseRequest # (1)
    from waldur_api_client.api.support_canned_responses import support_canned_responses_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = CannedResponseRequest(
        name="my-awesome-support-canned-response",
        text="string-value"
    )
    response = support_canned_responses_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`CannedResponseRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/canned_response_request.py)
    2.  **API Source:** [`support_canned_responses_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_canned_responses/support_canned_responses_update.py)

=== "TypeScript"

    ```typescript
    import { supportCannedResponsesUpdate } from 'waldur-js-client';
    
    try {
      const response = await supportCannedResponsesUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "name": "my-awesome-support-canned-response",
        "text": "string-value"
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

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `name` | string | ✓ |  |
    | `text` | string | ✓ | Template text. Supports Django template syntax. |
    | `category` | string |  |  |
    | `is_active` | boolean |  |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `text` | string | Template text. Supports Django template syntax. |
    | `category` | string |  |
    | `is_active` | boolean |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/support-issue-links/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      source="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      target="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.issue_link_request import IssueLinkRequest # (1)
    from waldur_api_client.api.support_issue_links import support_issue_links_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = IssueLinkRequest(
        source="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        target="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = support_issue_links_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`IssueLinkRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/issue_link_request.py)
    2.  **API Source:** [`support_issue_links_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_issue_links/support_issue_links_update.py)

=== "TypeScript"

    ```typescript
    import { supportIssueLinksUpdate } from 'waldur-js-client';
    
    try {
      const response = await supportIssueLinksUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "source": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "target": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `source` | string (uuid) | ✓ |
    | `target` | string (uuid) | ✓ |
    | `link_type` | string |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `url` | string (uri) |
    | `uuid` | string (uuid) |
    | `source` | string (uuid) |
    | `source_key` | string |
    | `target` | string (uuid) |
    | `target_key` | string |
    | `link_type` | string |

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/support-issue-tags/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-support-issue-tag"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.issue_tag_request import IssueTagRequest # (1)
    from waldur_api_client.api.support_issue_tags import support_issue_tags_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = IssueTagRequest(
        name="my-awesome-support-issue-tag"
    )
    response = support_issue_tags_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`IssueTagRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/issue_tag_request.py)
    2.  **API Source:** [`support_issue_tags_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_issue_tags/support_issue_tags_update.py)

=== "TypeScript"

    ```typescript
    import { supportIssueTagsUpdate } from 'waldur-js-client';
    
    try {
      const response = await supportIssueTagsUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "name": "my-awesome-support-issue-tag"
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

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `name` | string | ✓ |  |
    | `color` | string |  | Hex color code, e.g. #FF0000. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `color` | string | Hex color code, e.g. #FF0000. |

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/support-saved-filters/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-support-saved-filter"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.saved_filter_request import SavedFilterRequest # (1)
    from waldur_api_client.api.support_saved_filters import support_saved_filters_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = SavedFilterRequest(
        name="my-awesome-support-saved-filter"
    )
    response = support_saved_filters_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`SavedFilterRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/saved_filter_request.py)
    2.  **API Source:** [`support_saved_filters_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_saved_filters/support_saved_filters_update.py)

=== "TypeScript"

    ```typescript
    import { supportSavedFiltersUpdate } from 'waldur-js-client';
    
    try {
      const response = await supportSavedFiltersUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "name": "my-awesome-support-saved-filter"
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

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `name` | string | ✓ |  |
    | `filter_params` | object (free-form) |  | Saved filter parameters as JSON. |
    | `is_shared` | boolean |  | If True, visible to all staff/support users. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `filter_params` | object (free-form) | Saved filter parameters as JSON. |
    | `is_shared` | boolean | If True, visible to all staff/support users. |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/support/settings/atlassian/123/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.support import support_settings_atlassian_update # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = support_settings_atlassian_update.sync(
        id=123,
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`support_settings_atlassian_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support/support_settings_atlassian_update.py)

=== "TypeScript"

    ```typescript
    import { supportSettingsAtlassianUpdate } from 'waldur-js-client';
    
    try {
      const response = await supportSettingsAtlassianUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "id": 123
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required | Description |
    |---|---|---|---|
    | `id` | integer | ✓ | A unique integer value identifying this issue. |


=== "Responses"

    **`200`** - No response body
    

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/support-canned-responses/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_canned_response_request import PatchedCannedResponseRequest # (1)
    from waldur_api_client.api.support_canned_responses import support_canned_responses_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedCannedResponseRequest()
    response = support_canned_responses_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedCannedResponseRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_canned_response_request.py)
    2.  **API Source:** [`support_canned_responses_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_canned_responses/support_canned_responses_partial_update.py)

=== "TypeScript"

    ```typescript
    import { supportCannedResponsesPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await supportCannedResponsesPartialUpdate({
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
    | `name` | string |  |  |
    | `text` | string |  | Template text. Supports Django template syntax. |
    | `category` | string |  |  |
    | `is_active` | boolean |  |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `text` | string | Template text. Supports Django template syntax. |
    | `category` | string |  |
    | `is_active` | boolean |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/support-issue-links/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_issue_link_request import PatchedIssueLinkRequest # (1)
    from waldur_api_client.api.support_issue_links import support_issue_links_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedIssueLinkRequest()
    response = support_issue_links_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedIssueLinkRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_issue_link_request.py)
    2.  **API Source:** [`support_issue_links_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_issue_links/support_issue_links_partial_update.py)

=== "TypeScript"

    ```typescript
    import { supportIssueLinksPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await supportIssueLinksPartialUpdate({
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
    | `source` | string (uuid) |  |
    | `target` | string (uuid) |  |
    | `link_type` | string |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `url` | string (uri) |
    | `uuid` | string (uuid) |
    | `source` | string (uuid) |
    | `source_key` | string |
    | `target` | string (uuid) |
    | `target_key` | string |
    | `link_type` | string |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/support-issue-tags/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_issue_tag_request import PatchedIssueTagRequest # (1)
    from waldur_api_client.api.support_issue_tags import support_issue_tags_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedIssueTagRequest()
    response = support_issue_tags_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedIssueTagRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_issue_tag_request.py)
    2.  **API Source:** [`support_issue_tags_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_issue_tags/support_issue_tags_partial_update.py)

=== "TypeScript"

    ```typescript
    import { supportIssueTagsPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await supportIssueTagsPartialUpdate({
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
    | `name` | string |  |  |
    | `color` | string |  | Hex color code, e.g. #FF0000. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `color` | string | Hex color code, e.g. #FF0000. |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/support-saved-filters/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_saved_filter_request import PatchedSavedFilterRequest # (1)
    from waldur_api_client.api.support_saved_filters import support_saved_filters_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedSavedFilterRequest()
    response = support_saved_filters_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedSavedFilterRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_saved_filter_request.py)
    2.  **API Source:** [`support_saved_filters_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_saved_filters/support_saved_filters_partial_update.py)

=== "TypeScript"

    ```typescript
    import { supportSavedFiltersPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await supportSavedFiltersPartialUpdate({
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
    | `name` | string |  |  |
    | `filter_params` | object (free-form) |  | Saved filter parameters as JSON. |
    | `is_shared` | boolean |  | If True, visible to all staff/support users. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `filter_params` | object (free-form) | Saved filter parameters as JSON. |
    | `is_shared` | boolean | If True, visible to all staff/support users. |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/support/settings/atlassian/123/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.support import support_settings_atlassian_partial_update # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = support_settings_atlassian_partial_update.sync(
        id=123,
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`support_settings_atlassian_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support/support_settings_atlassian_partial_update.py)

=== "TypeScript"

    ```typescript
    import { supportSettingsAtlassianPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await supportSettingsAtlassianPartialUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "id": 123
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required | Description |
    |---|---|---|---|
    | `id` | integer | ✓ | A unique integer value identifying this issue. |


=== "Responses"

    **`200`** - No response body
    

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/support-canned-responses/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.support_canned_responses import support_canned_responses_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = support_canned_responses_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`support_canned_responses_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_canned_responses/support_canned_responses_destroy.py)

=== "TypeScript"

    ```typescript
    import { supportCannedResponsesDestroy } from 'waldur-js-client';
    
    try {
      const response = await supportCannedResponsesDestroy({
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

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/support-issue-links/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.support_issue_links import support_issue_links_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = support_issue_links_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`support_issue_links_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_issue_links/support_issue_links_destroy.py)

=== "TypeScript"

    ```typescript
    import { supportIssueLinksDestroy } from 'waldur-js-client';
    
    try {
      const response = await supportIssueLinksDestroy({
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

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/support-issue-tags/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.support_issue_tags import support_issue_tags_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = support_issue_tags_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`support_issue_tags_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_issue_tags/support_issue_tags_destroy.py)

=== "TypeScript"

    ```typescript
    import { supportIssueTagsDestroy } from 'waldur-js-client';
    
    try {
      const response = await supportIssueTagsDestroy({
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

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/support-saved-filters/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.support_saved_filters import support_saved_filters_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = support_saved_filters_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`support_saved_filters_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_saved_filters/support_saved_filters_destroy.py)

=== "TypeScript"

    ```typescript
    import { supportSavedFiltersDestroy } from 'waldur-js-client';
    
    try {
      const response = await supportSavedFiltersDestroy({
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

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/support/settings/atlassian/123/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.support import support_settings_atlassian_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = support_settings_atlassian_destroy.sync(
        id=123,
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`support_settings_atlassian_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support/support_settings_atlassian_destroy.py)

=== "TypeScript"

    ```typescript
    import { supportSettingsAtlassianDestroy } from 'waldur-js-client';
    
    try {
      const response = await supportSettingsAtlassianDestroy({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "id": 123
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Path Parameters"

    | Name | Type | Required | Description |
    |---|---|---|---|
    | `id` | integer | ✓ | A unique integer value identifying this issue. |


=== "Responses"

    **`204`** - No response body
    

---
