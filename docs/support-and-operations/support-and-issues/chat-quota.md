# Chat Quota

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/chat-quota/usage/` | [List Chat Quota Usage](#list-chat-quota-usage) |
| <span class="http-badge http-post">POST</span> | `/api/chat-quota/set_quota/` | [Set token quota for user](#set-token-quota-for-user) |

---

### List Chat Quota Usage


        Get current token quota and usage for the requesting user.

        Returns token quota for all periods (daily, weekly, monthly):
        - limit: User's custom limit (null = use system default, -1 = unlimited, or positive integer)
        - usage: Tokens used in current period
        - remaining: Tokens remaining (null if unlimited)
        - reset_at: When the period resets
        - system_default: System-wide default limit from configuration (for transparency when limit is null)
        


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/chat-quota/usage/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.chat_quota import chat_quota_usage_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = chat_quota_usage_retrieve.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`chat_quota_usage_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/chat_quota/chat_quota_usage_retrieve.py)

=== "TypeScript"

    ```typescript
    import { chatQuotaUsageRetrieve } from 'waldur-js-client';
    
    try {
      const response = await chatQuotaUsageRetrieve({
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
    | `user_uuid` | string (uuid) | UUID of user to view quota for (staff/support only). Omit to view your own quota. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `daily_limit` | integer | Daily token limit (non-negative integer). Null uses system default. -1 means unlimited. |
    | `daily_usage` | integer |  |
    | `daily_remaining` | integer | Get remaining daily tokens. |
    | `daily_reset_at` | string (date-time) | Calculate next midnight (00:00:00). |
    | `daily_system_default` | integer | Get system default daily token limit from constance config. |
    | `weekly_limit` | integer | Weekly token limit (non-negative integer). Null uses system default. -1 means unlimited. |
    | `weekly_usage` | integer |  |
    | `weekly_remaining` | integer | Get remaining weekly tokens. |
    | `weekly_reset_at` | string (date-time) | Calculate next Monday at midnight. |
    | `weekly_system_default` | integer | Get system default weekly token limit from constance config. |
    | `monthly_limit` | integer | Monthly token limit (non-negative integer). Null uses system default. -1 means unlimited. |
    | `monthly_usage` | integer |  |
    | `monthly_remaining` | integer | Get remaining monthly tokens. |
    | `monthly_reset_at` | string (date-time) | Calculate first day of next month at midnight. |
    | `monthly_system_default` | integer | Get system default monthly token limit from constance config. |

---

### Set token quota for user

Allows staff/support to set token quota limits for a specific user. Configure daily, weekly, and monthly limits:
- Omit field or send `null`: Use system default
- `-1`: Unlimited (no quota enforcement)
- `0` or positive integer: Specific token limit


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/chat-quota/set_quota/ \
      Authorization:"Token YOUR_API_TOKEN" \
      user_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.set_token_quota_request import SetTokenQuotaRequest # (1)
    from waldur_api_client.api.chat_quota import chat_quota_set_quota # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = SetTokenQuotaRequest(
        user_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = chat_quota_set_quota.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`SetTokenQuotaRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/set_token_quota_request.py)
    2.  **API Source:** [`chat_quota_set_quota`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/chat_quota/chat_quota_set_quota.py)

=== "TypeScript"

    ```typescript
    import { chatQuotaSetQuota } from 'waldur-js-client';
    
    try {
      const response = await chatQuotaSetQuota({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "user_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `user_uuid` | string (uuid) | ✓ | UUID of the user to set quota for. |
    | `daily_limit` | integer |  | Daily token limit. Omit or null = system default, -1 = unlimited. |
    | `weekly_limit` | integer |  | Weekly token limit. Omit or null = system default, -1 = unlimited. |
    | `monthly_limit` | integer |  | Monthly token limit. Omit or null = system default, -1 = unlimited. |


=== "Responses"

    **`200`** - No response body
    

---
