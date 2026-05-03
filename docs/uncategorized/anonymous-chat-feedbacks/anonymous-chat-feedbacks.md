# Anonymous Chat Feedbacks

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/anonymous-chat-feedbacks/` | [List Anonymous Chat Feedbacks](#list-anonymous-chat-feedbacks) |
| <span class="http-badge http-get">GET</span> | `/api/anonymous-chat-feedbacks/{interaction_uuid}/` | [Retrieve](#retrieve) |

---

### List Anonymous Chat Feedbacks


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/anonymous-chat-feedbacks/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.anonymous_chat_feedback_o_enum import AnonymousChatFeedbackOEnum # (1)
    from waldur_api_client.api.anonymous_chat_feedbacks import anonymous_chat_feedbacks_list # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = anonymous_chat_feedbacks_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`AnonymousChatFeedbackOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/anonymous_chat_feedback_o_enum.py)
    2.  **API Source:** [`anonymous_chat_feedbacks_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/anonymous_chat_feedbacks/anonymous_chat_feedbacks_list.py)

=== "TypeScript"

    ```typescript
    import { anonymousChatFeedbacksList } from 'waldur-js-client';
    
    try {
      const response = await anonymousChatFeedbacksList({
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
    | `has_comment` | boolean |  |
    | `o` | array | Ordering<br><br> |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `score` | integer |  |
    | `submitted_from` | string (date) |  |
    | `submitted_to` | string (date) |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `interaction_uuid` | string (uuid) |  |
    | `score` | integer |  |
    | `comment` | string |  |
    | `category` | any |  |
    | `submitted_from_ip` | any | An IPv4 or IPv6 address. |
    | `submitted_at` | string (date-time) |  |
    | `llm_resolution_score` | integer |  |
    | `llm_intent_category` | string |  |
    | `llm_hallucination_detected` | boolean |  |
    | `llm_hallucination_details` | string |  |
    | `llm_summary` | string |  |
    | `llm_reviewed_at` | string (date-time) |  |
    | `llm_judge_input_tokens` | integer |  |
    | `llm_judge_output_tokens` | integer |  |
    | `llm_judge_model` | string |  |
    | `modified_at` | string (date-time) |  |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/anonymous-chat-feedbacks/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.anonymous_chat_feedbacks import anonymous_chat_feedbacks_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = anonymous_chat_feedbacks_retrieve.sync(
        interaction_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`anonymous_chat_feedbacks_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/anonymous_chat_feedbacks/anonymous_chat_feedbacks_retrieve.py)

=== "TypeScript"

    ```typescript
    import { anonymousChatFeedbacksRetrieve } from 'waldur-js-client';
    
    try {
      const response = await anonymousChatFeedbacksRetrieve({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "interaction_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `interaction_uuid` | string (uuid) | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `interaction_uuid` | string (uuid) |  |
    | `score` | integer |  |
    | `comment` | string |  |
    | `category` | any |  |
    | `submitted_from_ip` | any | An IPv4 or IPv6 address. |
    | `submitted_at` | string (date-time) |  |
    | `llm_resolution_score` | integer |  |
    | `llm_intent_category` | string |  |
    | `llm_hallucination_detected` | boolean |  |
    | `llm_hallucination_details` | string |  |
    | `llm_summary` | string |  |
    | `llm_reviewed_at` | string (date-time) |  |
    | `llm_judge_input_tokens` | integer |  |
    | `llm_judge_output_tokens` | integer |  |
    | `llm_judge_model` | string |  |
    | `modified_at` | string (date-time) |  |

---
