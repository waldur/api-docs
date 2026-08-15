# Event Consumers

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/event-consumers/` | [List Event Consumers](#list-event-consumers) |
| <span class="http-badge http-delete">DELETE</span> | `/api/event-consumers/{uuid}/` | [Delete](#delete) |
| **Other Actions** | | |
| <span class="http-badge http-post">POST</span> | `/api/event-consumers/register/` | [Register](#register) |

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
    from waldur_api_client.api.event_consumers import event_consumers_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = event_consumers_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`event_consumers_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/event_consumers/event_consumers_list.py)

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
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `object_types` | object (free-form) | List of observable object types this consumer receives. Empty list means all types. |
    | `scopes` | array of objects |  |
    | `scopes.type` | string |  |
    | `scopes.uuid` | string |  |
    | `is_global` | boolean |  |
    | `rmq_username` | string | RabbitMQ username (UUID hex) for the consumer queue. |
    | `queue_created` | boolean |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

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

---
