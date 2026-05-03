# Marketplace Chat

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-chat/click/` | [Click](#click) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-chat/feedback/` | [Feedback](#feedback) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-chat/stream/` | [Stream](#stream) |

---

### Click


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-chat/click/ \
      Authorization:"Token YOUR_API_TOKEN" \
      interaction_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      feedback_token="********" \
      offering_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.anonymous_chat_click_request_request import AnonymousChatClickRequestRequest # (1)
    from waldur_api_client.api.marketplace_chat import marketplace_chat_click # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = AnonymousChatClickRequestRequest(
        interaction_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        feedback_token="********",
        offering_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = marketplace_chat_click.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`AnonymousChatClickRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/anonymous_chat_click_request_request.py)
    2.  **API Source:** [`marketplace_chat_click`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_chat/marketplace_chat_click.py)

=== "TypeScript"

    ```typescript
    import { marketplaceChatClick } from 'waldur-js-client';
    
    try {
      const response = await marketplaceChatClick({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "interaction_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "feedback_token": "********",
        "offering_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `interaction_uuid` | string (uuid) | ✓ | UUID of the interaction this click belongs to. |
    | `feedback_token` | string | ✓ | HMAC-bound bearer issued in the streaming `m` frame (same as /feedback/). |
    | `offering_uuid` | string (uuid) | ✓ | UUID of the clicked offering. Must appear in the parent interaction's recommended set, else 400. |


=== "Responses"

    **`200`** - Click recorded.
    
    
    ---
    
    **`400`** - offering_uuid not in interaction's recommended set.
    
    
    ---
    
    **`403`** - Missing or forged feedback_token.
    
    
    ---
    
    **`404`** - Unknown interaction_uuid.
    

---

### Feedback


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-chat/feedback/ \
      Authorization:"Token YOUR_API_TOKEN" \
      interaction_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      feedback_token="********" \
      score=123
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.anonymous_chat_feedback_request_request import AnonymousChatFeedbackRequestRequest # (1)
    from waldur_api_client.api.marketplace_chat import marketplace_chat_feedback # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = AnonymousChatFeedbackRequestRequest(
        interaction_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        feedback_token="********",
        score=123
    )
    response = marketplace_chat_feedback.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`AnonymousChatFeedbackRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/anonymous_chat_feedback_request_request.py)
    2.  **API Source:** [`marketplace_chat_feedback`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_chat/marketplace_chat_feedback.py)

=== "TypeScript"

    ```typescript
    import { marketplaceChatFeedback } from 'waldur-js-client';
    
    try {
      const response = await marketplaceChatFeedback({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "interaction_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "feedback_token": "********",
        "score": 123
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
    | `interaction_uuid` | string (uuid) | ✓ | UUID of the interaction the feedback is about (from the streaming `m` frame). |
    | `feedback_token` | string | ✓ | HMAC-bound bearer issued in the streaming `m` frame. |
    | `score` | integer | ✓ | +1 thumbs-up or -1 thumbs-down (0 not accepted). |
    | `comment` | string |  | Optional free-text comment.<br>_Constraints: default: ``_ |
    | `category` | any |  | Required when score == -1; rejected when score == 1.<br>_Constraints: default: ``_ |


=== "Responses"

    **`200`** - Feedback recorded.
    
    
    ---
    
    **`400`** - Invalid body shape, or comment was rejected by injection guard.
    
    
    ---
    
    **`403`** - Missing or forged feedback_token.
    
    
    ---
    
    **`404`** - Unknown interaction_uuid.
    

---

### Stream

Anonymous chat streaming endpoint. Returns NDJSON with one assistant content block per line. Final `m` frame carries input/output token counts.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-chat/stream/ \
      Authorization:"Token YOUR_API_TOKEN" \
      input="string-value" \
      session_id="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.anonymous_chat_stream_request_request import AnonymousChatStreamRequestRequest # (1)
    from waldur_api_client.api.marketplace_chat import marketplace_chat_stream # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = AnonymousChatStreamRequestRequest(
        input="string-value",
        session_id="string-value"
    )
    response = marketplace_chat_stream.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`AnonymousChatStreamRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/anonymous_chat_stream_request_request.py)
    2.  **API Source:** [`marketplace_chat_stream`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_chat/marketplace_chat_stream.py)

=== "TypeScript"

    ```typescript
    import { marketplaceChatStream } from 'waldur-js-client';
    
    try {
      const response = await marketplaceChatStream({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "input": "string-value",
        "session_id": "string-value"
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
    | `input` | string | ✓ | User input text for the anonymous marketplace assistant. |
    | `session_id` | string | ✓ | Client-generated session identifier. Bound to the originating IP on first use; subsequent requests from a different IP get 403. |


=== "Responses"

    **`200`** - NDJSON stream of assistant content blocks.
    
    
    ---
    
    **`400`** - Input rejected by injection/PII guard.
    
    
    ---
    
    **`403`** - Session bound to different IP, or IP blocked.
    
    
    ---
    
    **`409`** - Per-IP daily request or token cap exhausted, or the anonymous chat API URL/token is not configured. Carries Retry-After header + structured rate-limit body for the per-IP variants.
    
    
    ---
    
    **`424`** - Anonymous chat is disabled (master switch off or public marketplace browsing disabled).
    
    
    ---
    
    **`429`** - Site-wide per-minute burst cap exhausted. Retry-After header + structured rate-limit body.
    
    
    ---
    
    **`503`** - Site-wide daily token or request budget exhausted. Retry-After header + structured rate-limit body.
    

---
