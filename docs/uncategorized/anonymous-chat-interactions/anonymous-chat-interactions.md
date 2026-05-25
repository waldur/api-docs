# Anonymous Chat Interactions

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/anonymous-chat-interactions/` | [List Anonymous Chat Interactions](#list-anonymous-chat-interactions) |
| <span class="http-badge http-get">GET</span> | `/api/anonymous-chat-interactions/{uuid}/` | [Retrieve](#retrieve) |
| **Other Actions** | | |
| <span class="http-badge http-get">GET</span> | `/api/anonymous-chat-interactions/budget/` | [Today's global tenant budget snapshot](#todays-global-tenant-budget-snapshot) |
| <span class="http-badge http-get">GET</span> | `/api/anonymous-chat-interactions/by-session/{session_id}/` | [Full transcript for one anonymous session](#full-transcript-for-one-anonymous-session) |
| <span class="http-badge http-get">GET</span> | `/api/anonymous-chat-interactions/by-user/` | [Aggregate user list (no slug)](#aggregate-user-list-no-slug) |
| <span class="http-badge http-get">GET</span> | `/api/anonymous-chat-interactions/by-user/{user_slug}/` | [All sessions for one pseudonymous user](#all-sessions-for-one-pseudonymous-user) |
| <span class="http-badge http-get">GET</span> | `/api/anonymous-chat-interactions/kpi/` | [Aggregate KPI roll-up](#aggregate-kpi-roll-up) |

---
## Core CRUD


### List Anonymous Chat Interactions


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/anonymous-chat-interactions/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.anonymous_chat_interaction_o_enum import AnonymousChatInteractionOEnum # (1)
    from waldur_api_client.models.injection_severity_enum import InjectionSeverityEnum # (2)
    from waldur_api_client.api.anonymous_chat_interactions import anonymous_chat_interactions_list # (3)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = anonymous_chat_interactions_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`AnonymousChatInteractionOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/anonymous_chat_interaction_o_enum.py)
    2.  **Model Source:** [`InjectionSeverityEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/injection_severity_enum.py)
    3.  **API Source:** [`anonymous_chat_interactions_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/anonymous_chat_interactions/anonymous_chat_interactions_list.py)

=== "TypeScript"

    ```typescript
    import { anonymousChatInteractionsList } from 'waldur-js-client';
    
    try {
      const response = await anonymousChatInteractionsList({
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
    | `created_from` | string (date) |  |
    | `created_to` | string (date) |  |
    | `has_negative_feedback` | boolean |  |
    | `is_flagged` | boolean |  |
    | `o` | array | Ordering<br><br> |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `session_id` | string |  |
    | `severity` | string | _Enum: `none`, `low`, `medium`, `high`, `critical`_ |
    | `user_slug` | string |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `user_slug` | string |  |
    | `user_input` | string |  |
    | `assistant_blocks` | any |  |
    | `offering_uuids` | any |  |
    | `result_count` | integer |  |
    | `is_flagged` | boolean |  |
    | `severity` | string |  |
    | `injection_categories` | any |  |
    | `pii_categories` | any |  |
    | `action_taken` | string |  |
    | `warning` | string |  |
    | `ip_address` | any | An IPv4 or IPv6 address. |
    | `session_id` | string |  |
    | `last_active_at` | string (date-time) |  |
    | `created` | string (date-time) |  |
    | `feedback` | any |  |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/anonymous-chat-interactions/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.anonymous_chat_interactions import anonymous_chat_interactions_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = anonymous_chat_interactions_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`anonymous_chat_interactions_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/anonymous_chat_interactions/anonymous_chat_interactions_retrieve.py)

=== "TypeScript"

    ```typescript
    import { anonymousChatInteractionsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await anonymousChatInteractionsRetrieve({
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
    | `user_slug` | string |  |
    | `user_input` | string |  |
    | `assistant_blocks` | any |  |
    | `offering_uuids` | any |  |
    | `result_count` | integer |  |
    | `is_flagged` | boolean |  |
    | `severity` | string |  |
    | `injection_categories` | any |  |
    | `pii_categories` | any |  |
    | `action_taken` | string |  |
    | `warning` | string |  |
    | `ip_address` | any | An IPv4 or IPv6 address. |
    | `session_id` | string |  |
    | `last_active_at` | string (date-time) |  |
    | `created` | string (date-time) |  |
    | `feedback` | any |  |

---

## Other Actions


### Today's global tenant budget snapshot

Returns the site-wide token + request usage accumulated since 00:00 UTC today and the configured daily caps. Powers the budget gauges card on the staff analytics dashboard.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/anonymous-chat-interactions/budget/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.anonymous_chat_interactions import anonymous_chat_interactions_budget_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = anonymous_chat_interactions_budget_retrieve.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`anonymous_chat_interactions_budget_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/anonymous_chat_interactions/anonymous_chat_interactions_budget_retrieve.py)

=== "TypeScript"

    ```typescript
    import { anonymousChatInteractionsBudgetRetrieve } from 'waldur-js-client';
    
    try {
      const response = await anonymousChatInteractionsBudgetRetrieve({
      auth: "Token YOUR_API_TOKEN"
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `tokens_today` | integer |
    | `tokens_limit` | integer |
    | `resets_at` | string (date-time) |

---

### Full transcript for one anonymous session

Returns the ordered list of interactions belonging to the given ``session_id``. Use this to read a conversation as a transcript.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/anonymous-chat-interactions/by-session/string-value/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.anonymous_chat_interaction_o_enum import AnonymousChatInteractionOEnum # (1)
    from waldur_api_client.models.injection_severity_enum import InjectionSeverityEnum # (2)
    from waldur_api_client.api.anonymous_chat_interactions import anonymous_chat_interactions_by_session_list # (3)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = anonymous_chat_interactions_by_session_list.sync(
        session_id="string-value",
        client=client
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`AnonymousChatInteractionOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/anonymous_chat_interaction_o_enum.py)
    2.  **Model Source:** [`InjectionSeverityEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/injection_severity_enum.py)
    3.  **API Source:** [`anonymous_chat_interactions_by_session_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/anonymous_chat_interactions/anonymous_chat_interactions_by_session_list.py)

=== "TypeScript"

    ```typescript
    import { anonymousChatInteractionsBySessionList } from 'waldur-js-client';
    
    try {
      const response = await anonymousChatInteractionsBySessionList({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "session_id": "string-value"
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
    | `session_id` | string | ✓ |


=== "Query Parameters"

    | Name | Type | Description |
    |---|---|---|
    | `created_from` | string (date) |  |
    | `created_to` | string (date) |  |
    | `has_negative_feedback` | boolean |  |
    | `is_flagged` | boolean |  |
    | `o` | array | Ordering<br><br> |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `session_id` | string |  |
    | `severity` | string | _Enum: `none`, `low`, `medium`, `high`, `critical`_ |
    | `user_slug` | string |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `user_slug` | string |  |
    | `user_input` | string |  |
    | `assistant_blocks` | any |  |
    | `offering_uuids` | any |  |
    | `result_count` | integer |  |
    | `is_flagged` | boolean |  |
    | `severity` | string |  |
    | `injection_categories` | any |  |
    | `pii_categories` | any |  |
    | `action_taken` | string |  |
    | `warning` | string |  |
    | `ip_address` | any | An IPv4 or IPv6 address. |
    | `session_id` | string |  |
    | `last_active_at` | string (date-time) |  |
    | `created` | string (date-time) |  |
    | `feedback` | any |  |

---

### Aggregate user list (no slug)

Returns one row per user_slug with aggregate counters. Powers the staff Users page in the admin analytics.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/anonymous-chat-interactions/by-user/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.anonymous_chat_interaction_o_enum import AnonymousChatInteractionOEnum # (1)
    from waldur_api_client.models.injection_severity_enum import InjectionSeverityEnum # (2)
    from waldur_api_client.api.anonymous_chat_interactions import anonymous_chat_interactions_by_user_aggregate # (3)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = anonymous_chat_interactions_by_user_aggregate.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`AnonymousChatInteractionOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/anonymous_chat_interaction_o_enum.py)
    2.  **Model Source:** [`InjectionSeverityEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/injection_severity_enum.py)
    3.  **API Source:** [`anonymous_chat_interactions_by_user_aggregate`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/anonymous_chat_interactions/anonymous_chat_interactions_by_user_aggregate.py)

=== "TypeScript"

    ```typescript
    import { anonymousChatInteractionsByUserAggregate } from 'waldur-js-client';
    
    try {
      const response = await anonymousChatInteractionsByUserAggregate({
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
    | `created_from` | string (date) |  |
    | `created_to` | string (date) |  |
    | `has_negative_feedback` | boolean |  |
    | `is_flagged` | boolean |  |
    | `o` | array | Ordering<br><br> |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `session_id` | string |  |
    | `severity` | string | _Enum: `none`, `low`, `medium`, `high`, `critical`_ |
    | `user_slug` | string |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `user_slug` | string |
    | `last_seen` | string (date-time) |
    | `total_interactions` | integer |
    | `session_count` | integer |
    | `positive_feedback` | integer |
    | `negative_feedback` | integer |
    | `no_feedback` | integer |
    | `injection_strikes` | integer |

---

### All sessions for one pseudonymous user

Returns interactions sharing a ``user_slug`` (Scrypt of originating IP) — across however many sessions that anon user opened, ordered chronologically.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/anonymous-chat-interactions/by-user/string-value/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.anonymous_chat_interaction_o_enum import AnonymousChatInteractionOEnum # (1)
    from waldur_api_client.models.injection_severity_enum import InjectionSeverityEnum # (2)
    from waldur_api_client.api.anonymous_chat_interactions import anonymous_chat_interactions_by_user_list # (3)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = anonymous_chat_interactions_by_user_list.sync(
        user_slug="string-value",
        client=client
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`AnonymousChatInteractionOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/anonymous_chat_interaction_o_enum.py)
    2.  **Model Source:** [`InjectionSeverityEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/injection_severity_enum.py)
    3.  **API Source:** [`anonymous_chat_interactions_by_user_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/anonymous_chat_interactions/anonymous_chat_interactions_by_user_list.py)

=== "TypeScript"

    ```typescript
    import { anonymousChatInteractionsByUserList } from 'waldur-js-client';
    
    try {
      const response = await anonymousChatInteractionsByUserList({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "user_slug": "string-value"
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
    | `user_slug` | string | ✓ |


=== "Query Parameters"

    | Name | Type | Description |
    |---|---|---|
    | `created_from` | string (date) |  |
    | `created_to` | string (date) |  |
    | `has_negative_feedback` | boolean |  |
    | `is_flagged` | boolean |  |
    | `o` | array | Ordering<br><br> |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `session_id` | string |  |
    | `severity` | string | _Enum: `none`, `low`, `medium`, `high`, `critical`_ |
    | `user_slug` | string |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `user_slug` | string |  |
    | `user_input` | string |  |
    | `assistant_blocks` | any |  |
    | `offering_uuids` | any |  |
    | `result_count` | integer |  |
    | `is_flagged` | boolean |  |
    | `severity` | string |  |
    | `injection_categories` | any |  |
    | `pii_categories` | any |  |
    | `action_taken` | string |  |
    | `warning` | string |  |
    | `ip_address` | any | An IPv4 or IPv6 address. |
    | `session_id` | string |  |
    | `last_active_at` | string (date-time) |  |
    | `created` | string (date-time) |  |
    | `feedback` | any |  |

---

### Aggregate KPI roll-up

Returns aggregate counters and rates for the anonymous chat flow. Filters are honoured (date range etc.) so the same parameters work as on the list endpoint.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/anonymous-chat-interactions/kpi/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.anonymous_chat_interactions import anonymous_chat_interactions_kpi_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = anonymous_chat_interactions_kpi_retrieve.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`anonymous_chat_interactions_kpi_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/anonymous_chat_interactions/anonymous_chat_interactions_kpi_retrieve.py)

=== "TypeScript"

    ```typescript
    import { anonymousChatInteractionsKpiRetrieve } from 'waldur-js-client';
    
    try {
      const response = await anonymousChatInteractionsKpiRetrieve({
      auth: "Token YOUR_API_TOKEN"
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `interactions_total` | integer |  |
    | `sessions_total` | integer |  |
    | `unique_users` | integer | Distinct user_slug values in the window — proxy for active anonymous users. |
    | `flagged_total` | integer |  |
    | `feedback_positive` | integer |  |
    | `feedback_negative` | integer |  |
    | `satisfaction_rate` | number (double) | positive / (positive + negative); null when no human feedback. |
    | `clicks_total` | integer |  |
    | `click_through_rate` | number (double) | clicks / interactions; null when no interactions. |
    | `avg_llm_resolution_score` | number (double) | Mean of llm_resolution_score across reviewed sessions (1-5). |
    | `llm_intent_distribution` | object (free-form) | Counts keyed by llm_intent_category. |
    | `hallucination_rate` | number (double) | Share of reviewed sessions flagged as hallucinating. |
    | `review_coverage` | number (double) | Reviewed sessions / total reviewable sessions. Operations health signal — drops below ~90% if the review budget is too tight or the task is failing. |
    | `daily_volume` | array of objects | Per-day query counts across the filter window. |
    | `daily_volume.date` | string (date) |  |
    | `daily_volume.count` | integer |  |
    | `severity_by_day` | any | Stacked-bar input. Shape: {labels: [iso-date], series: {NONE: [...], LOW: [...], MEDIUM: [...], HIGH: [...], CRITICAL: [...]}} |

---
