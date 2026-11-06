# Event Consumers

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/event-consumers/` | [List Event Consumers](#list-event-consumers) |
| <span class="http-badge http-post">POST</span> | `/api/event-consumers/{uuid}/update_webhook/` | [Update webhook](#update-webhook) |
| <span class="http-badge http-delete">DELETE</span> | `/api/event-consumers/{uuid}/` | [Delete](#delete) |
| **Other Actions** | | |
| <span class="http-badge http-post">POST</span> | `/api/event-consumers/register/` | [Register](#register) |
| <span class="http-badge http-post">POST</span> | `/api/event-consumers/register_webhook/` | [Register webhook](#register-webhook) |
| <span class="http-badge http-post">POST</span> | `/api/event-consumers/{uuid}/resync/` | [Resync](#resync) |

---
## Core CRUD


### List Event Consumers


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/event-consumers/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.backend_resource_req_o_enum import BackendResourceReqOEnum # (1)
    from waldur_api_client.models.delivery_enum import DeliveryEnum # (2)
    from waldur_api_client.api.event_consumers import event_consumers_list # (3)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = event_consumers_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`BackendResourceReqOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/backend_resource_req_o_enum.py)
    2.  **Model Source:** [`DeliveryEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/delivery_enum.py)
    3.  **API Source:** [`event_consumers_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/event_consumers/event_consumers_list.py)

=== "TypeScript"

    ```typescript
    import { eventConsumersList } from 'waldur-js-client';
    
    try {
      const response = await eventConsumersList({
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
    | `delivery` | string | _Enum: `rmq`, `webhook`_ |
    | `is_global` | boolean | Consumer is bound to no scope and therefore receives every event |
    | `o` | array | Ordering<br><br> |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `user_username` | string |  |
    | `user_uuid` | string (uuid) | Owner UUID |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `object_types` | array of strings |  |
    | `scopes` | array of objects |  |
    | `scopes.type` | string |  |
    | `scopes.uuid` | string |  |
    | `is_global` | boolean |  |
    | `rmq_username` | string | RabbitMQ username (UUID hex) for the consumer queue. |
    | `queue_created` | boolean |  |
    | `user_uuid` | string (uuid) |  |
    | `user_username` | string | Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters |
    | `user_full_name` | string |  |
    | `user_is_staff` | boolean | Designates whether the user can log into this admin site. |
    | `auth_kind` | any |  |
    | `auth_token_prefix` | string | Prefix of the Personal Access Token used, when auth_kind is pat. |
    | `auth_token_name` | string | Name of the Personal Access Token used, when auth_kind is pat. |
    | `authorized_via` | any |  |
    | `delivery_blocked_reason` | string |  |
    | `delivery` | any |  |
    | `webhook_destination` | string | Scheme and host of the webhook URL. The full URL is a credential and is never returned. |
    | `payload_filters` | object (free-form) |  |
    | `last_delivered_at` | string (date-time) |  |
    | `last_error` | string |  |
    | `last_error_at` | string (date-time) |  |
    | `ephemeral` | boolean | Registered by a short-lived client (a browser tab). Deleted automatically once its queue has had no reader for EVENT_CONSUMER_EPHEMERAL_IDLE_HOURS. |
    | `unread_since` | string (date-time) | When the sweep first saw this ephemeral consumer's queue without a reader. Cleared when a reader returns or the client re-registers. |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |


=== "Authorization"

    Any signed-in user.
    
    The caller's own event consumers; staff and global support see every consumer. Consumers owned by a site agent are left out.

---

### Update webhook

Change a webhook consumer's destination URL, object types or payload filters. Staff only. Omitted fields are left unchanged.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/event-consumers/a1b2c3d4-e5f6-7890-abcd-ef1234567890/update_webhook/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.event_consumer_webhook_update_request import EventConsumerWebhookUpdateRequest # (1)
    from waldur_api_client.api.event_consumers import event_consumers_update_webhook # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = EventConsumerWebhookUpdateRequest()
    response = event_consumers_update_webhook.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`EventConsumerWebhookUpdateRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/event_consumer_webhook_update_request.py)
    2.  **API Source:** [`event_consumers_update_webhook`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/event_consumers/event_consumers_update_webhook.py)

=== "TypeScript"

    ```typescript
    import { eventConsumersUpdateWebhook } from 'waldur-js-client';
    
    try {
      const response = await eventConsumersUpdateWebhook({
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
    | `webhook_url` | string |  | HTTP(S) URL the messages are POSTed to as JSON. May carry its credential in the query string; it is stored as a secret and never returned.<br>_Constraints: write-only_ |
    | `payload_filters` | object (free-form) |  | Allow-list over message fields, e.g. {"role_name": ["CUSTOMER.OWNER"], "scope_type": ["customer"]}. A message is delivered only if every listed field holds one of its values. |
    | `object_types` | array of strings |  | Observable object types to receive; an empty list means all. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `object_types` | array of strings |  |
    | `scopes` | array of objects |  |
    | `scopes.type` | string |  |
    | `scopes.uuid` | string |  |
    | `is_global` | boolean |  |
    | `rmq_username` | string | RabbitMQ username (UUID hex) for the consumer queue. |
    | `queue_created` | boolean |  |
    | `user_uuid` | string (uuid) |  |
    | `user_username` | string | Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters |
    | `user_full_name` | string |  |
    | `user_is_staff` | boolean | Designates whether the user can log into this admin site. |
    | `auth_kind` | any |  |
    | `auth_token_prefix` | string | Prefix of the Personal Access Token used, when auth_kind is pat. |
    | `auth_token_name` | string | Name of the Personal Access Token used, when auth_kind is pat. |
    | `authorized_via` | any |  |
    | `delivery_blocked_reason` | string |  |
    | `delivery` | any |  |
    | `webhook_destination` | string | Scheme and host of the webhook URL. The full URL is a credential and is never returned. |
    | `payload_filters` | object (free-form) |  |
    | `last_delivered_at` | string (date-time) |  |
    | `last_error` | string |  |
    | `last_error_at` | string (date-time) |  |
    | `ephemeral` | boolean | Registered by a short-lived client (a browser tab). Deleted automatically once its queue has had no reader for EVENT_CONSUMER_EPHEMERAL_IDLE_HOURS. |
    | `unread_since` | string (date-time) | When the sweep first saw this ephemeral consumer's queue without a reader. Cleared when a reader returns or the client re-registers. |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |


=== "Authorization"

    Staff only.

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/event-consumers/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.event_consumers import event_consumers_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = event_consumers_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`event_consumers_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/event_consumers/event_consumers_destroy.py)

=== "TypeScript"

    ```typescript
    import { eventConsumersDestroy } from 'waldur-js-client';
    
    try {
      const response = await eventConsumersDestroy({
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
    


=== "Authorization"

    All of:
    
    - Any of:
        - Staff.
        - A consumer that does not deliver to a webhook.
    - Any of:
        - The caller's own consumer.
        - Staff.

---

## Other Actions


### Register

Register (or refresh) an event-consumer queue for the calling user. Pass `scopes` to bind the queue to entities you hold a role on; an EMPTY `scopes` list requests a GLOBAL queue (all events, including all-user PII) and requires staff/support. Idempotent per binding set.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/event-consumers/register/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.event_consumer_registration_request import EventConsumerRegistrationRequest # (1)
    from waldur_api_client.api.event_consumers import event_consumers_register # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = EventConsumerRegistrationRequest()
    response = event_consumers_register.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`EventConsumerRegistrationRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/event_consumer_registration_request.py)
    2.  **API Source:** [`event_consumers_register`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/event_consumers/event_consumers_register.py)

=== "TypeScript"

    ```typescript
    import { eventConsumersRegister } from 'waldur-js-client';
    
    try {
      const response = await eventConsumersRegister({
      auth: "Token YOUR_API_TOKEN"
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Request Body"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `object_types` | array of strings |  | Observable object types to receive. An explicit empty list means all types; omitting the field leaves an existing consumer's filter unchanged. |
    | `scopes` | array of objects |  | Entity bindings this consumer receives events for — e.g. several projects, a customer, an offering, or your own user (type 'user', your own UUID) for identity events. You may only bind to an entity you hold a role on, or to yourself. AN EMPTY LIST MEANS GLOBAL (every event, including all-user PII) and is staff/support only. |
    | `scopes.type` | string | ✓ |  |
    | `scopes.uuid` | string (uuid) | ✓ |  |
    | `ephemeral` | boolean |  | Set by short-lived clients such as a browser tab. An ephemeral consumer and its queue are deleted once the queue has had no reader for EVENT_CONSUMER_EPHEMERAL_IDLE_HOURS, or once its owner has no active token. Re-registering an existing consumer without the flag makes it permanent. Re-registering a permanent consumer with it makes it ephemeral only for a browser-style registration (DRF token or session, previously too, bound to your own user); otherwise it stays permanent. Integrations should leave it unset.<br>_Constraints: default: `False`_ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `rmq_username` | string | RabbitMQ username (UUID hex) for STOMP authentication |
    | `queue_name` | string | RabbitMQ queue name (consumer_{consumer_uuid}) |
    | `vhost` | string | RabbitMQ virtual host (user UUID) |
    | `observable_object_types` | array of strings | Object types routed to this queue |
    
    ---
    
    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `rmq_username` | string | RabbitMQ username (UUID hex) for STOMP authentication |
    | `queue_name` | string | RabbitMQ queue name (consumer_{consumer_uuid}) |
    | `vhost` | string | RabbitMQ virtual host (user UUID) |
    | `observable_object_types` | array of strings | Object types routed to this queue |


=== "Authorization"

    Any signed-in user, for a consumer of their own. Each binding names an entity the caller holds a role on, or one below an entity they hold a role on, or the caller themselves; staff and global support bind to anything. A consumer with no bindings receives every event and requires staff or global support.

---

### Register webhook

Create a webhook event consumer: the same messages a queue consumer receives are POSTed as JSON to `webhook_url` instead. Staff only. An EMPTY `scopes` list makes it global (all events, including all-user PII). Use `payload_filters` to narrow delivery, e.g. to one role, and `resync` to send the current state once.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/event-consumers/register_webhook/ \
      Authorization:"Token YOUR_API_TOKEN" \
      webhook_url="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.event_consumer_webhook_request import EventConsumerWebhookRequest # (1)
    from waldur_api_client.api.event_consumers import event_consumers_register_webhook # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = EventConsumerWebhookRequest(
        webhook_url="string-value"
    )
    response = event_consumers_register_webhook.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`EventConsumerWebhookRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/event_consumer_webhook_request.py)
    2.  **API Source:** [`event_consumers_register_webhook`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/event_consumers/event_consumers_register_webhook.py)

=== "TypeScript"

    ```typescript
    import { eventConsumersRegisterWebhook } from 'waldur-js-client';
    
    try {
      const response = await eventConsumersRegisterWebhook({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "webhook_url": "string-value"
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
    | `webhook_url` | string | ✓ | HTTP(S) URL the messages are POSTed to as JSON. May carry its credential in the query string; it is stored as a secret and never returned.<br>_Constraints: write-only_ |
    | `payload_filters` | object (free-form) |  | Allow-list over message fields, e.g. {"role_name": ["CUSTOMER.OWNER"], "scope_type": ["customer"]}. A message is delivered only if every listed field holds one of its values. |
    | `object_types` | array of strings |  | Observable object types to receive. An explicit empty list means all types; omitting the field leaves an existing consumer's filter unchanged. |
    | `scopes` | array of objects |  | Entity bindings this consumer receives events for — e.g. several projects, a customer, an offering, or your own user (type 'user', your own UUID) for identity events. You may only bind to an entity you hold a role on, or to yourself. AN EMPTY LIST MEANS GLOBAL (every event, including all-user PII) and is staff/support only. |
    | `scopes.type` | string | ✓ |  |
    | `scopes.uuid` | string (uuid) | ✓ |  |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `object_types` | array of strings |  |
    | `scopes` | array of objects |  |
    | `scopes.type` | string |  |
    | `scopes.uuid` | string |  |
    | `is_global` | boolean |  |
    | `rmq_username` | string | RabbitMQ username (UUID hex) for the consumer queue. |
    | `queue_created` | boolean |  |
    | `user_uuid` | string (uuid) |  |
    | `user_username` | string | Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters |
    | `user_full_name` | string |  |
    | `user_is_staff` | boolean | Designates whether the user can log into this admin site. |
    | `auth_kind` | any |  |
    | `auth_token_prefix` | string | Prefix of the Personal Access Token used, when auth_kind is pat. |
    | `auth_token_name` | string | Name of the Personal Access Token used, when auth_kind is pat. |
    | `authorized_via` | any |  |
    | `delivery_blocked_reason` | string |  |
    | `delivery` | any |  |
    | `webhook_destination` | string | Scheme and host of the webhook URL. The full URL is a credential and is never returned. |
    | `payload_filters` | object (free-form) |  |
    | `last_delivered_at` | string (date-time) |  |
    | `last_error` | string |  |
    | `last_error_at` | string (date-time) |  |
    | `ephemeral` | boolean | Registered by a short-lived client (a browser tab). Deleted automatically once its queue has had no reader for EVENT_CONSUMER_EPHEMERAL_IDLE_HOURS. |
    | `unread_since` | string (date-time) | When the sweep first saw this ephemeral consumer's queue without a reader. Cleared when a reader returns or the client re-registers. |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |


=== "Authorization"

    Staff only.

---

### Resync

Replay the current state to a global consumer, through its own transport and filters, so a receiver that starts late can seed itself. Every active role grant is sent as a `user_role` message with `event_type` `role_snapshot`. Runs asynchronously. Staff, or support for its own consumers: support is read-only, so another user's consumer is not found.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/event-consumers/a1b2c3d4-e5f6-7890-abcd-ef1234567890/resync/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.event_consumers import event_consumers_resync # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = event_consumers_resync.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`event_consumers_resync`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/event_consumers/event_consumers_resync.py)

=== "TypeScript"

    ```typescript
    import { eventConsumersResync } from 'waldur-js-client';
    
    try {
      const response = await eventConsumersResync({
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

    **`202`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `object_types` | array of strings | Object types whose current state is being replayed. |


=== "Authorization"

    Staff or support only.

---
