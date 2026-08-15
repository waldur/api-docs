# Provider Tickets

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/provider-tickets/` | [List Provider Tickets](#list-provider-tickets) |
| <span class="http-badge http-get">GET</span> | `/api/provider-tickets/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-put">PUT</span> | `/api/provider-tickets/{uuid}/` | [Update](#update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/provider-tickets/{uuid}/` | [Partial Update](#partial-update) |
| **Other Actions** | | |
| <span class="http-badge http-get">GET</span> | `/api/provider-tickets/{uuid}/customer_context/` | [Get customer context for this ticket](#get-customer-context-for-this-ticket) |
| <span class="http-badge http-get">GET</span> | `/api/provider-tickets/stats/` | [Get statistics for provider tickets](#get-statistics-for-provider-tickets) |
| <span class="http-badge http-post">POST</span> | `/api/provider-tickets/{uuid}/assign/` | [Assign](#assign) |
| <span class="http-badge http-post">POST</span> | `/api/provider-tickets/{uuid}/claim/` | [Claim](#claim) |
| <span class="http-badge http-post">POST</span> | `/api/provider-tickets/{uuid}/comment/` | [Comment](#comment) |
| <span class="http-badge http-post">POST</span> | `/api/provider-tickets/{uuid}/resolve/` | [Resolve](#resolve) |

---
## Core CRUD


### List Provider Tickets


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/provider-tickets/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.provider_ticket_o_enum import ProviderTicketOEnum # (1)
    from waldur_api_client.api.provider_tickets import provider_tickets_list # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = provider_tickets_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`ProviderTicketOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/provider_ticket_o_enum.py)
    2.  **API Source:** [`provider_tickets_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/provider_tickets/provider_tickets_list.py)

=== "TypeScript"

    ```typescript
    import { providerTicketsList } from 'waldur-js-client';
    
    try {
      const response = await providerTicketsList({
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
    | `is_escalated` | boolean |  |
    | `o` | array | Ordering<br><br> |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `priority` | string |  |
    | `provider_assignee` | string (uuid) |  |
    | `sla_breached` | boolean |  |
    | `status` | string |  |
    | `summary` | string |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `key` | string |  |
    | `summary` | string |  |
    | `description` | string |  |
    | `type` | string |  |
    | `status` | string |  |
    | `priority` | string |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `parent_issue_key` | string |  |
    | `parent_issue_uuid` | string (uuid) |  |
    | `is_escalated` | boolean | Whether this issue has been escalated. |
    | `escalated_at` | string (date-time) | When the issue was escalated. |
    | `provider_assignee` | string (uuid) |  |
    | `provider_assignee_name` | string |  |
    | `first_response_deadline` | string (date-time) | Deadline for first response from support staff. |
    | `resolution_deadline` | string (date-time) | Deadline for issue resolution. |
    | `first_response_at` | string (date-time) | Timestamp of first response from support staff. |
    | `sla_breached` | boolean | Whether SLA has been breached for this issue. |
    | `customer` | string (uri) |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `project` | string (uri) |  |
    | `project_uuid` | string (uuid) |  |
    | `project_name` | string |  |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/provider-tickets/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.provider_tickets import provider_tickets_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = provider_tickets_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`provider_tickets_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/provider_tickets/provider_tickets_retrieve.py)

=== "TypeScript"

    ```typescript
    import { providerTicketsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await providerTicketsRetrieve({
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
    | `key` | string |  |
    | `summary` | string |  |
    | `description` | string |  |
    | `type` | string |  |
    | `status` | string |  |
    | `priority` | string |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `parent_issue_key` | string |  |
    | `parent_issue_uuid` | string (uuid) |  |
    | `is_escalated` | boolean | Whether this issue has been escalated. |
    | `escalated_at` | string (date-time) | When the issue was escalated. |
    | `provider_assignee` | string (uuid) |  |
    | `provider_assignee_name` | string |  |
    | `first_response_deadline` | string (date-time) | Deadline for first response from support staff. |
    | `resolution_deadline` | string (date-time) | Deadline for issue resolution. |
    | `first_response_at` | string (date-time) | Timestamp of first response from support staff. |
    | `sla_breached` | boolean | Whether SLA has been breached for this issue. |
    | `customer` | string (uri) |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `project` | string (uri) |  |
    | `project_uuid` | string (uuid) |  |
    | `project_name` | string |  |

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/provider-tickets/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.provider_ticket_request import ProviderTicketRequest # (1)
    from waldur_api_client.api.provider_tickets import provider_tickets_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ProviderTicketRequest()
    response = provider_tickets_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ProviderTicketRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/provider_ticket_request.py)
    2.  **API Source:** [`provider_tickets_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/provider_tickets/provider_tickets_update.py)

=== "TypeScript"

    ```typescript
    import { providerTicketsUpdate } from 'waldur-js-client';
    
    try {
      const response = await providerTicketsUpdate({
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
    | `escalated_at` | string (date-time) |  | When the issue was escalated. |
    | `customer` | string (uri) |  |  |
    | `project` | string (uri) |  |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `key` | string |  |
    | `summary` | string |  |
    | `description` | string |  |
    | `type` | string |  |
    | `status` | string |  |
    | `priority` | string |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `parent_issue_key` | string |  |
    | `parent_issue_uuid` | string (uuid) |  |
    | `is_escalated` | boolean | Whether this issue has been escalated. |
    | `escalated_at` | string (date-time) | When the issue was escalated. |
    | `provider_assignee` | string (uuid) |  |
    | `provider_assignee_name` | string |  |
    | `first_response_deadline` | string (date-time) | Deadline for first response from support staff. |
    | `resolution_deadline` | string (date-time) | Deadline for issue resolution. |
    | `first_response_at` | string (date-time) | Timestamp of first response from support staff. |
    | `sla_breached` | boolean | Whether SLA has been breached for this issue. |
    | `customer` | string (uri) |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `project` | string (uri) |  |
    | `project_uuid` | string (uuid) |  |
    | `project_name` | string |  |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/provider-tickets/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_provider_ticket_request import PatchedProviderTicketRequest # (1)
    from waldur_api_client.api.provider_tickets import provider_tickets_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedProviderTicketRequest()
    response = provider_tickets_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedProviderTicketRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_provider_ticket_request.py)
    2.  **API Source:** [`provider_tickets_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/provider_tickets/provider_tickets_partial_update.py)

=== "TypeScript"

    ```typescript
    import { providerTicketsPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await providerTicketsPartialUpdate({
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
    | `escalated_at` | string (date-time) |  | When the issue was escalated. |
    | `customer` | string (uri) |  |  |
    | `project` | string (uri) |  |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `key` | string |  |
    | `summary` | string |  |
    | `description` | string |  |
    | `type` | string |  |
    | `status` | string |  |
    | `priority` | string |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `parent_issue_key` | string |  |
    | `parent_issue_uuid` | string (uuid) |  |
    | `is_escalated` | boolean | Whether this issue has been escalated. |
    | `escalated_at` | string (date-time) | When the issue was escalated. |
    | `provider_assignee` | string (uuid) |  |
    | `provider_assignee_name` | string |  |
    | `first_response_deadline` | string (date-time) | Deadline for first response from support staff. |
    | `resolution_deadline` | string (date-time) | Deadline for issue resolution. |
    | `first_response_at` | string (date-time) | Timestamp of first response from support staff. |
    | `sla_breached` | boolean | Whether SLA has been breached for this issue. |
    | `customer` | string (uri) |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `project` | string (uri) |  |
    | `project_uuid` | string (uuid) |  |
    | `project_name` | string |  |

---

## Other Actions


### Get customer context for this ticket


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/provider-tickets/a1b2c3d4-e5f6-7890-abcd-ef1234567890/customer_context/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.provider_tickets import provider_tickets_customer_context_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = provider_tickets_customer_context_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`provider_tickets_customer_context_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/provider_tickets/provider_tickets_customer_context_retrieve.py)

=== "TypeScript"

    ```typescript
    import { providerTicketsCustomerContextRetrieve } from 'waldur-js-client';
    
    try {
      const response = await providerTicketsCustomerContextRetrieve({
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
    | `caller` | object |
    | `caller.full_name` | string |
    | `caller.email` | string (email) |
    | `caller.organization` | string |
    | `resource` | any |
    | `recent_tickets` | array of objects |
    | `recent_tickets.uuid` | string (uuid) |
    | `recent_tickets.key` | string |
    | `recent_tickets.summary` | string |
    | `recent_tickets.status` | string |
    | `recent_tickets.created` | string (date-time) |

---

### Get statistics for provider tickets


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/provider-tickets/stats/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.provider_tickets import provider_tickets_stats_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = provider_tickets_stats_retrieve.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`provider_tickets_stats_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/provider_tickets/provider_tickets_stats_retrieve.py)

=== "TypeScript"

    ```typescript
    import { providerTicketsStatsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await providerTicketsStatsRetrieve({
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
    | `total_open` | integer |
    | `total_resolved` | integer |
    | `total_escalated` | integer |
    | `sla_breach_count` | integer |
    | `avg_resolution_hours` | number (double) |
    | `by_status` | object (free-form) |

---

### Assign


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/provider-tickets/a1b2c3d4-e5f6-7890-abcd-ef1234567890/assign/ \
      Authorization:"Token YOUR_API_TOKEN" \
      provider_support_user="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.provider_assign_request import ProviderAssignRequest # (1)
    from waldur_api_client.api.provider_tickets import provider_tickets_assign # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ProviderAssignRequest(
        provider_support_user="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = provider_tickets_assign.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ProviderAssignRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/provider_assign_request.py)
    2.  **API Source:** [`provider_tickets_assign`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/provider_tickets/provider_tickets_assign.py)

=== "TypeScript"

    ```typescript
    import { providerTicketsAssign } from 'waldur-js-client';
    
    try {
      const response = await providerTicketsAssign({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "provider_support_user": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `provider_support_user` | string (uuid) | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `status` | string |

---

### Claim


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/provider-tickets/a1b2c3d4-e5f6-7890-abcd-ef1234567890/claim/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.provider_ticket_request import ProviderTicketRequest # (1)
    from waldur_api_client.api.provider_tickets import provider_tickets_claim # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ProviderTicketRequest()
    response = provider_tickets_claim.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ProviderTicketRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/provider_ticket_request.py)
    2.  **API Source:** [`provider_tickets_claim`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/provider_tickets/provider_tickets_claim.py)

=== "TypeScript"

    ```typescript
    import { providerTicketsClaim } from 'waldur-js-client';
    
    try {
      const response = await providerTicketsClaim({
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
    | `escalated_at` | string (date-time) |  | When the issue was escalated. |
    | `customer` | string (uri) |  |  |
    | `project` | string (uri) |  |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `status` | string |

---

### Comment


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/provider-tickets/a1b2c3d4-e5f6-7890-abcd-ef1234567890/comment/ \
      Authorization:"Token YOUR_API_TOKEN" \
      description="A sample description."
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.provider_comment_request import ProviderCommentRequest # (1)
    from waldur_api_client.api.provider_tickets import provider_tickets_comment # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ProviderCommentRequest(
        description="A sample description."
    )
    response = provider_tickets_comment.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ProviderCommentRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/provider_comment_request.py)
    2.  **API Source:** [`provider_tickets_comment`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/provider_tickets/provider_tickets_comment.py)

=== "TypeScript"

    ```typescript
    import { providerTicketsComment } from 'waldur-js-client';
    
    try {
      const response = await providerTicketsComment({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "description": "A sample description."
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
    | `description` | string | ✓ |
    | `is_public` | boolean |  |


=== "Responses"

    **`201`** - No response body
    

---

### Resolve


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/provider-tickets/a1b2c3d4-e5f6-7890-abcd-ef1234567890/resolve/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.provider_tickets import provider_tickets_resolve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = provider_tickets_resolve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`provider_tickets_resolve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/provider_tickets/provider_tickets_resolve.py)

=== "TypeScript"

    ```typescript
    import { providerTicketsResolve } from 'waldur-js-client';
    
    try {
      const response = await providerTicketsResolve({
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
    | `status` | string |

---
