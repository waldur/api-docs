# Chat

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/chat-messages/` | [List Chat Messages](#list-chat-messages) |
| <span class="http-badge http-get">GET</span> | `/api/chat-sessions/current/` | [Get or create current user's chat session](#get-or-create-current-users-chat-session) |
| <span class="http-badge http-get">GET</span> | `/api/chat-sessions/` | [List Chat Sessions](#list-chat-sessions) |
| <span class="http-badge http-get">GET</span> | `/api/chat-sessions/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-get">GET</span> | `/api/chat-threads/` | [List Chat Threads](#list-chat-threads) |
| <span class="http-badge http-get">GET</span> | `/api/chat-threads/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/chat/stream/` | [Stream](#stream) |
| <span class="http-badge http-post">POST</span> | `/api/chat-threads/{uuid}/archive/` | [Archive thread](#archive-thread) |
| <span class="http-badge http-post">POST</span> | `/api/chat-threads/{uuid}/unarchive/` | [Unarchive thread](#unarchive-thread) |

---

### List Chat Messages


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/chat-messages/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.chat_messages import chat_messages_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = chat_messages_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`chat_messages_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/chat_messages/chat_messages_list.py)

=== "TypeScript"

    ```typescript
    import { chatMessagesList } from 'waldur-js-client';
    
    try {
      const response = await chatMessagesList({
      auth: "Token YOUR_API_TOKEN"
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Query Parameters"

    | Name | Type |
    |---|---|
    | `include_history` | boolean |
    | `is_flagged` | boolean |
    | `thread` | string (uuid) |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `thread` | string (uuid) |
    | `role` | any |
    | `content` | string |
    | `sequence_index` | integer |
    | `replaces` | string (uuid) |
    | `created` | string (date-time) |
    | `is_flagged` | boolean |
    | `injection_score` | number (double) |
    | `injection_severity` | any |
    | `injection_categories` | any |

---

### Get or create current user's chat session

Returns the current user's chat session, creating it if it doesn't exist.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/chat-sessions/current/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.chat_sessions import chat_sessions_current_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = chat_sessions_current_retrieve.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`chat_sessions_current_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/chat_sessions/chat_sessions_current_retrieve.py)

=== "TypeScript"

    ```typescript
    import { chatSessionsCurrentRetrieve } from 'waldur-js-client';
    
    try {
      const response = await chatSessionsCurrentRetrieve({
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
    | `uuid` | string (uuid) |
    | `user` | string (uuid) |
    | `user_username` | string |
    | `user_full_name` | string |
    | `created` | string (date-time) |
    | `modified` | string (date-time) |

---

### List Chat Sessions


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/chat-sessions/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.chat_session_field_enum import ChatSessionFieldEnum # (1)
    from waldur_api_client.api.chat_sessions import chat_sessions_list # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = chat_sessions_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`ChatSessionFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/chat_session_field_enum.py)
    2.  **API Source:** [`chat_sessions_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/chat_sessions/chat_sessions_list.py)

=== "TypeScript"

    ```typescript
    import { chatSessionsList } from 'waldur-js-client';
    
    try {
      const response = await chatSessionsList({
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
    | `field` | array |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `user` | string (uuid) |
    | `user_username` | string |
    | `user_full_name` | string |
    | `created` | string (date-time) |
    | `modified` | string (date-time) |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/chat-sessions/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.chat_session_field_enum import ChatSessionFieldEnum # (1)
    from waldur_api_client.api.chat_sessions import chat_sessions_retrieve # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = chat_sessions_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ChatSessionFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/chat_session_field_enum.py)
    2.  **API Source:** [`chat_sessions_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/chat_sessions/chat_sessions_retrieve.py)

=== "TypeScript"

    ```typescript
    import { chatSessionsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await chatSessionsRetrieve({
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
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `user` | string (uuid) |
    | `user_username` | string |
    | `user_full_name` | string |
    | `created` | string (date-time) |
    | `modified` | string (date-time) |

---

### List Chat Threads


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/chat-threads/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.injection_severity_enum import InjectionSeverityEnum # (1)
    from waldur_api_client.models.thread_session_field_enum import ThreadSessionFieldEnum # (2)
    from waldur_api_client.models.thread_session_o_enum import ThreadSessionOEnum # (3)
    from waldur_api_client.api.chat_threads import chat_threads_list # (4)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = chat_threads_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`InjectionSeverityEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/injection_severity_enum.py)
    2.  **Model Source:** [`ThreadSessionFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/thread_session_field_enum.py)
    3.  **Model Source:** [`ThreadSessionOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/thread_session_o_enum.py)
    4.  **API Source:** [`chat_threads_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/chat_threads/chat_threads_list.py)

=== "TypeScript"

    ```typescript
    import { chatThreadsList } from 'waldur-js-client';
    
    try {
      const response = await chatThreadsList({
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
    | `created` | string (date) |  |
    | `field` | array |  |
    | `is_archived` | boolean |  |
    | `is_flagged` | boolean |  |
    | `max_severity` | string | _Enum: `none`, `low`, `medium`, `high`, `critical`_ |
    | `modified` | string (date) |  |
    | `o` | array | Ordering<br><br> |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `query` | string |  |
    | `user` | string (uuid) |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `name` | string |
    | `chat_session` | string (uuid) |
    | `flags` | any |
    | `is_archived` | boolean |
    | `message_count` | integer |
    | `is_flagged` | boolean |
    | `max_severity` | any |
    | `user_username` | string |
    | `user_full_name` | string |
    | `created` | string (date-time) |
    | `modified` | string (date-time) |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/chat-threads/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.thread_session_field_enum import ThreadSessionFieldEnum # (1)
    from waldur_api_client.api.chat_threads import chat_threads_retrieve # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = chat_threads_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ThreadSessionFieldEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/thread_session_field_enum.py)
    2.  **API Source:** [`chat_threads_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/chat_threads/chat_threads_retrieve.py)

=== "TypeScript"

    ```typescript
    import { chatThreadsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await chatThreadsRetrieve({
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
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |
    | `name` | string |
    | `chat_session` | string (uuid) |
    | `flags` | any |
    | `is_archived` | boolean |
    | `message_count` | integer |
    | `is_flagged` | boolean |
    | `max_severity` | any |
    | `user_username` | string |
    | `user_full_name` | string |
    | `created` | string (date-time) |
    | `modified` | string (date-time) |

---

### Stream


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/chat/stream/ \
      Authorization:"Token YOUR_API_TOKEN" \
      input="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.chat_request_request import ChatRequestRequest # (1)
    from waldur_api_client.api.chat import chat_stream # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ChatRequestRequest(
        input="string-value"
    )
    response = chat_stream.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ChatRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/chat_request_request.py)
    2.  **API Source:** [`chat_stream`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/chat/chat_stream.py)

=== "TypeScript"

    ```typescript
    import { chatStream } from 'waldur-js-client';
    
    try {
      const response = await chatStream({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "input": "string-value"
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
    | `input` | string | ✓ | User input text for the chat model. |
    | `thread_uuid` | string (uuid) |  | Existing thread UUID. If omitted, a new thread is created. |
    | `update_thread_name` | string (uuid) |  | Thread UUID whose name should be set to the assistant's response. Skips message persistence for this call. |
    | `mode` | any |  | 'reload': replace the last assistant response. 'edit': edit a user message and re-stream. Omit for normal new-message behavior. |
    | `edit_message_uuid` | string (uuid) |  | UUID of the user message to edit. Required when mode='edit'. |


=== "Responses"

    **`200`** - 
    

---

### Archive thread

Archive a thread (soft delete).


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/chat-threads/a1b2c3d4-e5f6-7890-abcd-ef1234567890/archive/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.thread_session_request import ThreadSessionRequest # (1)
    from waldur_api_client.api.chat_threads import chat_threads_archive # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ThreadSessionRequest()
    response = chat_threads_archive.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ThreadSessionRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/thread_session_request.py)
    2.  **API Source:** [`chat_threads_archive`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/chat_threads/chat_threads_archive.py)

=== "TypeScript"

    ```typescript
    import { chatThreadsArchive } from 'waldur-js-client';
    
    try {
      const response = await chatThreadsArchive({
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
    | `name` | string |  |
    | `is_archived` | boolean |  |


=== "Responses"

    **`204`** - No response body
    

---

### Unarchive thread

Restore an archived thread.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/chat-threads/a1b2c3d4-e5f6-7890-abcd-ef1234567890/unarchive/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.thread_session_request import ThreadSessionRequest # (1)
    from waldur_api_client.api.chat_threads import chat_threads_unarchive # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ThreadSessionRequest()
    response = chat_threads_unarchive.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ThreadSessionRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/thread_session_request.py)
    2.  **API Source:** [`chat_threads_unarchive`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/chat_threads/chat_threads_unarchive.py)

=== "TypeScript"

    ```typescript
    import { chatThreadsUnarchive } from 'waldur-js-client';
    
    try {
      const response = await chatThreadsUnarchive({
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
    | `name` | string |  |
    | `is_archived` | boolean |  |


=== "Responses"

    **`204`** - No response body
    

---
