# Support Issues

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/support-issues/` | [List Support Issues](#list-support-issues) |
| <span class="http-badge http-get">GET</span> | `/api/support-issues/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/support-issues/` | [Create](#create) |
| <span class="http-badge http-put">PUT</span> | `/api/support-issues/{uuid}/` | [Update](#update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/support-issues/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-delete">DELETE</span> | `/api/support-issues/{uuid}/` | [Delete](#delete) |
| **Other Actions** | | |
| <span class="http-badge http-post">POST</span> | `/api/support-issues/{uuid}/attach_resource/` | [Attach a marketplace resource to an issue](#attach-a-marketplace-resource-to-an-issue) |
| <span class="http-badge http-post">POST</span> | `/api/support-issues/bulk_update/` | [Bulk update multiple issues](#bulk-update-multiple-issues) |
| <span class="http-badge http-post">POST</span> | `/api/support-issues/{uuid}/comment/` | [Comment](#comment) |
| <span class="http-badge http-post">POST</span> | `/api/support-issues/{uuid}/escalate/` | [Escalate an issue](#escalate-an-issue) |
| <span class="http-badge http-post">POST</span> | `/api/support-issues/{uuid}/reroute/` | [Re-route an already-routed issue to a different provider helpdesk](#re-route-an-already-routed-issue-to-a-different-provider-helpdesk) |
| <span class="http-badge http-post">POST</span> | `/api/support-issues/{uuid}/route_to_provider/` | [Manually route an issue to a provider helpdesk](#manually-route-an-issue-to-a-provider-helpdesk) |
| <span class="http-badge http-post">POST</span> | `/api/support-issues/{uuid}/sync/` | [Sync](#sync) |

---
## Core CRUD


### List Support Issues


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/support-issues/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.issue_o_enum import IssueOEnum # (1)
    from waldur_api_client.api.support_issues import support_issues_list # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = support_issues_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`IssueOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/issue_o_enum.py)
    2.  **API Source:** [`support_issues_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_issues/support_issues_list.py)

=== "TypeScript"

    ```typescript
    import { supportIssuesList } from 'waldur-js-client';
    
    try {
      const response = await supportIssuesList({
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
    | `assignee` | string (uri) |  |
    | `assignee_name` | string |  |
    | `caller` | string (uri) |  |
    | `caller_full_name` | string | Caller full name contains |
    | `customer` | string (uri) |  |
    | `customer_uuid` | string (uuid) |  |
    | `is_escalated` | boolean |  |
    | `is_parent` | boolean | Is a parent issue |
    | `is_routed` | boolean | Has been routed to provider |
    | `key` | string |  |
    | `o` | array | Ordering<br><br> |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `project` | string (uri) |  |
    | `project_uuid` | string (uuid) |  |
    | `provider_uuid` | string (uuid) |  |
    | `query` | string | Summary or key contains |
    | `remote_id` | string |  |
    | `reporter` | string (uri) |  |
    | `reporter_name` | string |  |
    | `resolution_year_month` | string |  |
    | `resource` | string (uri) | Filter by resource URL. |
    | `resource_external_ip` | string | Resource external IP |
    | `resource_internal_ip` | string | Resource internal IP |
    | `resource_uuid` | string (uuid) | Resource UUID |
    | `sla_breached` | boolean |  |
    | `status` | string |  |
    | `summary` | string |  |
    | `type` | string |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `type` | string |  |
    | `key` | string |  |
    | `backend_id` | string |  |
    | `backend_name` | string |  |
    | `remote_id` | string |  |
    | `link` | string (uri) | Link to issue in support system. |
    | `summary` | string |  |
    | `description` | string |  |
    | `status` | string |  |
    | `resolution` | string |  |
    | `priority` | string |  |
    | `caller` | string (uri) |  |
    | `caller_uuid` | string (uuid) |  |
    | `caller_full_name` | string |  |
    | `reporter` | string (uri) |  |
    | `reporter_uuid` | string (uuid) |  |
    | `reporter_name` | string |  |
    | `assignee` | string (uri) |  |
    | `assignee_uuid` | string (uuid) |  |
    | `assignee_name` | string |  |
    | `customer` | string (uri) |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `project` | string (uri) |  |
    | `project_uuid` | string (uuid) |  |
    | `project_name` | string |  |
    | `resource` | string |  |
    | `resource_type` | string |  |
    | `resource_name` | string |  |
    | `offering` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `template` | string (uri) |  |
    | `feedback` | any |  |
    | `resolved` | boolean |  |
    | `update_is_available` | boolean |  |
    | `destroy_is_available` | boolean |  |
    | `add_comment_is_available` | boolean |  |
    | `add_attachment_is_available` | boolean |  |
    | `processing_log` | object (free-form) | Internal processing log for debugging order lifecycle events. Visible only to staff. |
    | `order_uuid` | string | Return order UUID if the issue's resource is an Order. |
    | `order_project_uuid` | string | Return order's project UUID if the issue's resource is an Order. |
    | `order_customer_uuid` | string | Return order's customer UUID if the issue's resource is an Order. |
    | `order_resource_name` | string | Return order's resource name if the issue's resource is an Order. |
    | `first_response_deadline` | string (date-time) | Deadline for first response from support staff. |
    | `resolution_deadline` | string (date-time) | Deadline for issue resolution. |
    | `first_response_at` | string (date-time) | Timestamp of first response from support staff. |
    | `sla_breached` | boolean | Whether SLA has been breached for this issue. |
    | `sla_status` | string |  |
    | `parent_issue` | string (uri) |  |
    | `provider_helpdesk` | string (uri) |  |
    | `is_escalated` | boolean | Whether this issue has been escalated. |
    | `escalated_at` | string (date-time) | When the issue was escalated. |
    | `escalation_reason` | string | Reason for escalation. |
    | `is_routed` | boolean |  |
    | `provider_ticket_info` | object (free-form) |  |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/support-issues/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.support_issues import support_issues_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = support_issues_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`support_issues_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_issues/support_issues_retrieve.py)

=== "TypeScript"

    ```typescript
    import { supportIssuesRetrieve } from 'waldur-js-client';
    
    try {
      const response = await supportIssuesRetrieve({
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
    | `type` | string |  |
    | `key` | string |  |
    | `backend_id` | string |  |
    | `backend_name` | string |  |
    | `remote_id` | string |  |
    | `link` | string (uri) | Link to issue in support system. |
    | `summary` | string |  |
    | `description` | string |  |
    | `status` | string |  |
    | `resolution` | string |  |
    | `priority` | string |  |
    | `caller` | string (uri) |  |
    | `caller_uuid` | string (uuid) |  |
    | `caller_full_name` | string |  |
    | `reporter` | string (uri) |  |
    | `reporter_uuid` | string (uuid) |  |
    | `reporter_name` | string |  |
    | `assignee` | string (uri) |  |
    | `assignee_uuid` | string (uuid) |  |
    | `assignee_name` | string |  |
    | `customer` | string (uri) |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `project` | string (uri) |  |
    | `project_uuid` | string (uuid) |  |
    | `project_name` | string |  |
    | `resource` | string |  |
    | `resource_type` | string |  |
    | `resource_name` | string |  |
    | `offering` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `template` | string (uri) |  |
    | `feedback` | any |  |
    | `resolved` | boolean |  |
    | `update_is_available` | boolean |  |
    | `destroy_is_available` | boolean |  |
    | `add_comment_is_available` | boolean |  |
    | `add_attachment_is_available` | boolean |  |
    | `processing_log` | object (free-form) | Internal processing log for debugging order lifecycle events. Visible only to staff. |
    | `order_uuid` | string | Return order UUID if the issue's resource is an Order. |
    | `order_project_uuid` | string | Return order's project UUID if the issue's resource is an Order. |
    | `order_customer_uuid` | string | Return order's customer UUID if the issue's resource is an Order. |
    | `order_resource_name` | string | Return order's resource name if the issue's resource is an Order. |
    | `first_response_deadline` | string (date-time) | Deadline for first response from support staff. |
    | `resolution_deadline` | string (date-time) | Deadline for issue resolution. |
    | `first_response_at` | string (date-time) | Timestamp of first response from support staff. |
    | `sla_breached` | boolean | Whether SLA has been breached for this issue. |
    | `sla_status` | string |  |
    | `parent_issue` | string (uri) |  |
    | `provider_helpdesk` | string (uri) |  |
    | `is_escalated` | boolean | Whether this issue has been escalated. |
    | `escalated_at` | string (date-time) | When the issue was escalated. |
    | `escalation_reason` | string | Reason for escalation. |
    | `is_routed` | boolean |  |
    | `provider_ticket_info` | object (free-form) |  |

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/support-issues/ \
      Authorization:"Token YOUR_API_TOKEN" \
      type="string-value" \
      summary="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.issue_request import IssueRequest # (1)
    from waldur_api_client.api.support_issues import support_issues_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = IssueRequest(
        type="string-value",
        summary="string-value"
    )
    response = support_issues_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`IssueRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/issue_request.py)
    2.  **API Source:** [`support_issues_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_issues/support_issues_create.py)

=== "TypeScript"

    ```typescript
    import { supportIssuesCreate } from 'waldur-js-client';
    
    try {
      const response = await supportIssuesCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "type": "string-value",
        "summary": "string-value"
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
    | `type` | string | ✓ |  |
    | `remote_id` | string |  |  |
    | `summary` | string | ✓ |  |
    | `description` | string |  |  |
    | `priority` | string |  |  |
    | `caller` | string (uri) |  |  |
    | `assignee` | string (uri) |  |  |
    | `customer` | string (uri) |  |  |
    | `project` | string (uri) |  |  |
    | `resource` | string |  |  |
    | `offering` | string (uuid) |  |  |
    | `is_reported_manually` | boolean |  | Set true if issue is created by regular user via portal.<br>_Constraints: write-only, default: `False`_ |
    | `template` | string (uri) |  |  |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `type` | string |  |
    | `key` | string |  |
    | `backend_id` | string |  |
    | `backend_name` | string |  |
    | `remote_id` | string |  |
    | `link` | string (uri) | Link to issue in support system. |
    | `summary` | string |  |
    | `description` | string |  |
    | `status` | string |  |
    | `resolution` | string |  |
    | `priority` | string |  |
    | `caller` | string (uri) |  |
    | `caller_uuid` | string (uuid) |  |
    | `caller_full_name` | string |  |
    | `reporter` | string (uri) |  |
    | `reporter_uuid` | string (uuid) |  |
    | `reporter_name` | string |  |
    | `assignee` | string (uri) |  |
    | `assignee_uuid` | string (uuid) |  |
    | `assignee_name` | string |  |
    | `customer` | string (uri) |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `project` | string (uri) |  |
    | `project_uuid` | string (uuid) |  |
    | `project_name` | string |  |
    | `resource` | string |  |
    | `resource_type` | string |  |
    | `resource_name` | string |  |
    | `offering` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `template` | string (uri) |  |
    | `feedback` | any |  |
    | `resolved` | boolean |  |
    | `update_is_available` | boolean |  |
    | `destroy_is_available` | boolean |  |
    | `add_comment_is_available` | boolean |  |
    | `add_attachment_is_available` | boolean |  |
    | `processing_log` | object (free-form) | Internal processing log for debugging order lifecycle events. Visible only to staff. |
    | `order_uuid` | string | Return order UUID if the issue's resource is an Order. |
    | `order_project_uuid` | string | Return order's project UUID if the issue's resource is an Order. |
    | `order_customer_uuid` | string | Return order's customer UUID if the issue's resource is an Order. |
    | `order_resource_name` | string | Return order's resource name if the issue's resource is an Order. |
    | `first_response_deadline` | string (date-time) | Deadline for first response from support staff. |
    | `resolution_deadline` | string (date-time) | Deadline for issue resolution. |
    | `first_response_at` | string (date-time) | Timestamp of first response from support staff. |
    | `sla_breached` | boolean | Whether SLA has been breached for this issue. |
    | `sla_status` | string |  |
    | `parent_issue` | string (uri) |  |
    | `provider_helpdesk` | string (uri) |  |
    | `is_escalated` | boolean | Whether this issue has been escalated. |
    | `escalated_at` | string (date-time) | When the issue was escalated. |
    | `escalation_reason` | string | Reason for escalation. |
    | `is_routed` | boolean |  |
    | `provider_ticket_info` | object (free-form) |  |

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/support-issues/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      type="string-value" \
      summary="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.issue_request import IssueRequest # (1)
    from waldur_api_client.api.support_issues import support_issues_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = IssueRequest(
        type="string-value",
        summary="string-value"
    )
    response = support_issues_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`IssueRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/issue_request.py)
    2.  **API Source:** [`support_issues_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_issues/support_issues_update.py)

=== "TypeScript"

    ```typescript
    import { supportIssuesUpdate } from 'waldur-js-client';
    
    try {
      const response = await supportIssuesUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "type": "string-value",
        "summary": "string-value"
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
    | `type` | string | ✓ |  |
    | `remote_id` | string |  |  |
    | `summary` | string | ✓ |  |
    | `description` | string |  |  |
    | `priority` | string |  |  |
    | `caller` | string (uri) |  |  |
    | `assignee` | string (uri) |  |  |
    | `customer` | string (uri) |  |  |
    | `project` | string (uri) |  |  |
    | `resource` | string |  |  |
    | `offering` | string (uuid) |  |  |
    | `is_reported_manually` | boolean |  | Set true if issue is created by regular user via portal.<br>_Constraints: write-only, default: `False`_ |
    | `template` | string (uri) |  |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `type` | string |  |
    | `key` | string |  |
    | `backend_id` | string |  |
    | `backend_name` | string |  |
    | `remote_id` | string |  |
    | `link` | string (uri) | Link to issue in support system. |
    | `summary` | string |  |
    | `description` | string |  |
    | `status` | string |  |
    | `resolution` | string |  |
    | `priority` | string |  |
    | `caller` | string (uri) |  |
    | `caller_uuid` | string (uuid) |  |
    | `caller_full_name` | string |  |
    | `reporter` | string (uri) |  |
    | `reporter_uuid` | string (uuid) |  |
    | `reporter_name` | string |  |
    | `assignee` | string (uri) |  |
    | `assignee_uuid` | string (uuid) |  |
    | `assignee_name` | string |  |
    | `customer` | string (uri) |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `project` | string (uri) |  |
    | `project_uuid` | string (uuid) |  |
    | `project_name` | string |  |
    | `resource` | string |  |
    | `resource_type` | string |  |
    | `resource_name` | string |  |
    | `offering` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `template` | string (uri) |  |
    | `feedback` | any |  |
    | `resolved` | boolean |  |
    | `update_is_available` | boolean |  |
    | `destroy_is_available` | boolean |  |
    | `add_comment_is_available` | boolean |  |
    | `add_attachment_is_available` | boolean |  |
    | `processing_log` | object (free-form) | Internal processing log for debugging order lifecycle events. Visible only to staff. |
    | `order_uuid` | string | Return order UUID if the issue's resource is an Order. |
    | `order_project_uuid` | string | Return order's project UUID if the issue's resource is an Order. |
    | `order_customer_uuid` | string | Return order's customer UUID if the issue's resource is an Order. |
    | `order_resource_name` | string | Return order's resource name if the issue's resource is an Order. |
    | `first_response_deadline` | string (date-time) | Deadline for first response from support staff. |
    | `resolution_deadline` | string (date-time) | Deadline for issue resolution. |
    | `first_response_at` | string (date-time) | Timestamp of first response from support staff. |
    | `sla_breached` | boolean | Whether SLA has been breached for this issue. |
    | `sla_status` | string |  |
    | `parent_issue` | string (uri) |  |
    | `provider_helpdesk` | string (uri) |  |
    | `is_escalated` | boolean | Whether this issue has been escalated. |
    | `escalated_at` | string (date-time) | When the issue was escalated. |
    | `escalation_reason` | string | Reason for escalation. |
    | `is_routed` | boolean |  |
    | `provider_ticket_info` | object (free-form) |  |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/support-issues/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_issue_request import PatchedIssueRequest # (1)
    from waldur_api_client.api.support_issues import support_issues_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedIssueRequest()
    response = support_issues_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedIssueRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_issue_request.py)
    2.  **API Source:** [`support_issues_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_issues/support_issues_partial_update.py)

=== "TypeScript"

    ```typescript
    import { supportIssuesPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await supportIssuesPartialUpdate({
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
    | `summary` | string |  |  |
    | `description` | string |  |  |
    | `assignee` | string (uri) |  |  |
    | `offering` | string (uuid) |  |  |
    | `is_reported_manually` | boolean |  | Set true if issue is created by regular user via portal.<br>_Constraints: write-only, default: `False`_ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `type` | string |  |
    | `key` | string |  |
    | `backend_id` | string |  |
    | `backend_name` | string |  |
    | `remote_id` | string |  |
    | `link` | string (uri) | Link to issue in support system. |
    | `summary` | string |  |
    | `description` | string |  |
    | `status` | string |  |
    | `resolution` | string |  |
    | `priority` | string |  |
    | `caller` | string (uri) |  |
    | `caller_uuid` | string (uuid) |  |
    | `caller_full_name` | string |  |
    | `reporter` | string (uri) |  |
    | `reporter_uuid` | string (uuid) |  |
    | `reporter_name` | string |  |
    | `assignee` | string (uri) |  |
    | `assignee_uuid` | string (uuid) |  |
    | `assignee_name` | string |  |
    | `customer` | string (uri) |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `project` | string (uri) |  |
    | `project_uuid` | string (uuid) |  |
    | `project_name` | string |  |
    | `resource` | string |  |
    | `resource_type` | string |  |
    | `resource_name` | string |  |
    | `offering` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `template` | string (uri) |  |
    | `feedback` | any |  |
    | `resolved` | boolean |  |
    | `update_is_available` | boolean |  |
    | `destroy_is_available` | boolean |  |
    | `add_comment_is_available` | boolean |  |
    | `add_attachment_is_available` | boolean |  |
    | `processing_log` | object (free-form) | Internal processing log for debugging order lifecycle events. Visible only to staff. |
    | `order_uuid` | string | Return order UUID if the issue's resource is an Order. |
    | `order_project_uuid` | string | Return order's project UUID if the issue's resource is an Order. |
    | `order_customer_uuid` | string | Return order's customer UUID if the issue's resource is an Order. |
    | `order_resource_name` | string | Return order's resource name if the issue's resource is an Order. |
    | `first_response_deadline` | string (date-time) | Deadline for first response from support staff. |
    | `resolution_deadline` | string (date-time) | Deadline for issue resolution. |
    | `first_response_at` | string (date-time) | Timestamp of first response from support staff. |
    | `sla_breached` | boolean | Whether SLA has been breached for this issue. |
    | `sla_status` | string |  |
    | `parent_issue` | string (uri) |  |
    | `provider_helpdesk` | string (uri) |  |
    | `is_escalated` | boolean | Whether this issue has been escalated. |
    | `escalated_at` | string (date-time) | When the issue was escalated. |
    | `escalation_reason` | string | Reason for escalation. |
    | `is_routed` | boolean |  |
    | `provider_ticket_info` | object (free-form) |  |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/support-issues/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.support_issues import support_issues_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = support_issues_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`support_issues_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_issues/support_issues_destroy.py)

=== "TypeScript"

    ```typescript
    import { supportIssuesDestroy } from 'waldur-js-client';
    
    try {
      const response = await supportIssuesDestroy({
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


### Attach a marketplace resource to an issue


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/support-issues/a1b2c3d4-e5f6-7890-abcd-ef1234567890/attach_resource/ \
      Authorization:"Token YOUR_API_TOKEN" \
      resource="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.attach_resource_request import AttachResourceRequest # (1)
    from waldur_api_client.api.support_issues import support_issues_attach_resource # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = AttachResourceRequest(
        resource="string-value"
    )
    response = support_issues_attach_resource.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`AttachResourceRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/attach_resource_request.py)
    2.  **API Source:** [`support_issues_attach_resource`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_issues/support_issues_attach_resource.py)

=== "TypeScript"

    ```typescript
    import { supportIssuesAttachResource } from 'waldur-js-client';
    
    try {
      const response = await supportIssuesAttachResource({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "resource": "string-value"
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
    | `resource` | string | ✓ | URL of the marketplace resource to attach to this issue. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `type` | string |  |
    | `key` | string |  |
    | `backend_id` | string |  |
    | `backend_name` | string |  |
    | `remote_id` | string |  |
    | `link` | string (uri) | Link to issue in support system. |
    | `summary` | string |  |
    | `description` | string |  |
    | `status` | string |  |
    | `resolution` | string |  |
    | `priority` | string |  |
    | `caller` | string (uri) |  |
    | `caller_uuid` | string (uuid) |  |
    | `caller_full_name` | string |  |
    | `reporter` | string (uri) |  |
    | `reporter_uuid` | string (uuid) |  |
    | `reporter_name` | string |  |
    | `assignee` | string (uri) |  |
    | `assignee_uuid` | string (uuid) |  |
    | `assignee_name` | string |  |
    | `customer` | string (uri) |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `project` | string (uri) |  |
    | `project_uuid` | string (uuid) |  |
    | `project_name` | string |  |
    | `resource` | string |  |
    | `resource_type` | string |  |
    | `resource_name` | string |  |
    | `offering` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `template` | string (uri) |  |
    | `feedback` | any |  |
    | `resolved` | boolean |  |
    | `update_is_available` | boolean |  |
    | `destroy_is_available` | boolean |  |
    | `add_comment_is_available` | boolean |  |
    | `add_attachment_is_available` | boolean |  |
    | `processing_log` | object (free-form) | Internal processing log for debugging order lifecycle events. Visible only to staff. |
    | `order_uuid` | string | Return order UUID if the issue's resource is an Order. |
    | `order_project_uuid` | string | Return order's project UUID if the issue's resource is an Order. |
    | `order_customer_uuid` | string | Return order's customer UUID if the issue's resource is an Order. |
    | `order_resource_name` | string | Return order's resource name if the issue's resource is an Order. |
    | `first_response_deadline` | string (date-time) | Deadline for first response from support staff. |
    | `resolution_deadline` | string (date-time) | Deadline for issue resolution. |
    | `first_response_at` | string (date-time) | Timestamp of first response from support staff. |
    | `sla_breached` | boolean | Whether SLA has been breached for this issue. |
    | `sla_status` | string |  |
    | `parent_issue` | string (uri) |  |
    | `provider_helpdesk` | string (uri) |  |
    | `is_escalated` | boolean | Whether this issue has been escalated. |
    | `escalated_at` | string (date-time) | When the issue was escalated. |
    | `escalation_reason` | string | Reason for escalation. |
    | `is_routed` | boolean |  |
    | `provider_ticket_info` | object (free-form) |  |

---

### Bulk update multiple issues


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/support-issues/bulk_update/ \
      Authorization:"Token YOUR_API_TOKEN" \
      issue_uuids:='[]'
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.bulk_update_issue_request import BulkUpdateIssueRequest # (1)
    from waldur_api_client.api.support_issues import support_issues_bulk_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = BulkUpdateIssueRequest(
        issue_uuids=[]
    )
    response = support_issues_bulk_update.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`BulkUpdateIssueRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/bulk_update_issue_request.py)
    2.  **API Source:** [`support_issues_bulk_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_issues/support_issues_bulk_update.py)

=== "TypeScript"

    ```typescript
    import { supportIssuesBulkUpdate } from 'waldur-js-client';
    
    try {
      const response = await supportIssuesBulkUpdate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "issue_uuids": []
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
    | `issue_uuids` | array of string (uuid)s | ✓ | List of issue UUIDs to update. |
    | `status` | string |  |  |
    | `priority` | string |  |  |
    | `assignee` | string (uuid) |  |  |


=== "Responses"

    **`200`** - No response body
    

---

### Comment


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/support-issues/a1b2c3d4-e5f6-7890-abcd-ef1234567890/comment/ \
      Authorization:"Token YOUR_API_TOKEN" \
      description="A sample description."
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.comment_request import CommentRequest # (1)
    from waldur_api_client.api.support_issues import support_issues_comment # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = CommentRequest(
        description="A sample description."
    )
    response = support_issues_comment.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`CommentRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/comment_request.py)
    2.  **API Source:** [`support_issues_comment`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_issues/support_issues_comment.py)

=== "TypeScript"

    ```typescript
    import { supportIssuesComment } from 'waldur-js-client';
    
    try {
      const response = await supportIssuesComment({
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

    **`201`** - 
    
    | Field | Type |
    |---|---|
    | `url` | string (uri) |
    | `uuid` | string (uuid) |
    | `issue` | string (uri) |
    | `issue_key` | string |
    | `description` | string |
    | `is_public` | boolean |
    | `author_name` | string |
    | `author_uuid` | string (uuid) |
    | `author_user` | string (uri) |
    | `author_email` | string (email) |
    | `author_image` | string (uri) |
    | `backend_id` | string |
    | `remote_id` | string |
    | `created` | string (date-time) |
    | `update_is_available` | boolean |
    | `destroy_is_available` | boolean |

---

### Escalate an issue


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/support-issues/a1b2c3d4-e5f6-7890-abcd-ef1234567890/escalate/ \
      Authorization:"Token YOUR_API_TOKEN" \
      reason="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.escalate_issue_request import EscalateIssueRequest # (1)
    from waldur_api_client.api.support_issues import support_issues_escalate # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = EscalateIssueRequest(
        reason="string-value"
    )
    response = support_issues_escalate.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`EscalateIssueRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/escalate_issue_request.py)
    2.  **API Source:** [`support_issues_escalate`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_issues/support_issues_escalate.py)

=== "TypeScript"

    ```typescript
    import { supportIssuesEscalate } from 'waldur-js-client';
    
    try {
      const response = await supportIssuesEscalate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "reason": "string-value"
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
    | `reason` | string | ✓ | Reason for escalation. |


=== "Responses"

    **`200`** - No response body
    

---

### Re-route an already-routed issue to a different provider helpdesk


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/support-issues/a1b2c3d4-e5f6-7890-abcd-ef1234567890/reroute/ \
      Authorization:"Token YOUR_API_TOKEN" \
      provider_helpdesk="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.route_to_provider_request import RouteToProviderRequest # (1)
    from waldur_api_client.api.support_issues import support_issues_reroute # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = RouteToProviderRequest(
        provider_helpdesk="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = support_issues_reroute.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`RouteToProviderRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/route_to_provider_request.py)
    2.  **API Source:** [`support_issues_reroute`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_issues/support_issues_reroute.py)

=== "TypeScript"

    ```typescript
    import { supportIssuesReroute } from 'waldur-js-client';
    
    try {
      const response = await supportIssuesReroute({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "provider_helpdesk": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `provider_helpdesk` | string (uuid) | ✓ | UUID of the provider helpdesk to route this issue to. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `type` | string |  |
    | `key` | string |  |
    | `backend_id` | string |  |
    | `backend_name` | string |  |
    | `remote_id` | string |  |
    | `link` | string (uri) | Link to issue in support system. |
    | `summary` | string |  |
    | `description` | string |  |
    | `status` | string |  |
    | `resolution` | string |  |
    | `priority` | string |  |
    | `caller` | string (uri) |  |
    | `caller_uuid` | string (uuid) |  |
    | `caller_full_name` | string |  |
    | `reporter` | string (uri) |  |
    | `reporter_uuid` | string (uuid) |  |
    | `reporter_name` | string |  |
    | `assignee` | string (uri) |  |
    | `assignee_uuid` | string (uuid) |  |
    | `assignee_name` | string |  |
    | `customer` | string (uri) |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `project` | string (uri) |  |
    | `project_uuid` | string (uuid) |  |
    | `project_name` | string |  |
    | `resource` | string |  |
    | `resource_type` | string |  |
    | `resource_name` | string |  |
    | `offering` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `template` | string (uri) |  |
    | `feedback` | any |  |
    | `resolved` | boolean |  |
    | `update_is_available` | boolean |  |
    | `destroy_is_available` | boolean |  |
    | `add_comment_is_available` | boolean |  |
    | `add_attachment_is_available` | boolean |  |
    | `processing_log` | object (free-form) | Internal processing log for debugging order lifecycle events. Visible only to staff. |
    | `order_uuid` | string | Return order UUID if the issue's resource is an Order. |
    | `order_project_uuid` | string | Return order's project UUID if the issue's resource is an Order. |
    | `order_customer_uuid` | string | Return order's customer UUID if the issue's resource is an Order. |
    | `order_resource_name` | string | Return order's resource name if the issue's resource is an Order. |
    | `first_response_deadline` | string (date-time) | Deadline for first response from support staff. |
    | `resolution_deadline` | string (date-time) | Deadline for issue resolution. |
    | `first_response_at` | string (date-time) | Timestamp of first response from support staff. |
    | `sla_breached` | boolean | Whether SLA has been breached for this issue. |
    | `sla_status` | string |  |
    | `parent_issue` | string (uri) |  |
    | `provider_helpdesk` | string (uri) |  |
    | `is_escalated` | boolean | Whether this issue has been escalated. |
    | `escalated_at` | string (date-time) | When the issue was escalated. |
    | `escalation_reason` | string | Reason for escalation. |
    | `is_routed` | boolean |  |
    | `provider_ticket_info` | object (free-form) |  |

---

### Manually route an issue to a provider helpdesk


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/support-issues/a1b2c3d4-e5f6-7890-abcd-ef1234567890/route_to_provider/ \
      Authorization:"Token YOUR_API_TOKEN" \
      provider_helpdesk="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.route_to_provider_request import RouteToProviderRequest # (1)
    from waldur_api_client.api.support_issues import support_issues_route_to_provider # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = RouteToProviderRequest(
        provider_helpdesk="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = support_issues_route_to_provider.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`RouteToProviderRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/route_to_provider_request.py)
    2.  **API Source:** [`support_issues_route_to_provider`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_issues/support_issues_route_to_provider.py)

=== "TypeScript"

    ```typescript
    import { supportIssuesRouteToProvider } from 'waldur-js-client';
    
    try {
      const response = await supportIssuesRouteToProvider({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "provider_helpdesk": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `provider_helpdesk` | string (uuid) | ✓ | UUID of the provider helpdesk to route this issue to. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `type` | string |  |
    | `key` | string |  |
    | `backend_id` | string |  |
    | `backend_name` | string |  |
    | `remote_id` | string |  |
    | `link` | string (uri) | Link to issue in support system. |
    | `summary` | string |  |
    | `description` | string |  |
    | `status` | string |  |
    | `resolution` | string |  |
    | `priority` | string |  |
    | `caller` | string (uri) |  |
    | `caller_uuid` | string (uuid) |  |
    | `caller_full_name` | string |  |
    | `reporter` | string (uri) |  |
    | `reporter_uuid` | string (uuid) |  |
    | `reporter_name` | string |  |
    | `assignee` | string (uri) |  |
    | `assignee_uuid` | string (uuid) |  |
    | `assignee_name` | string |  |
    | `customer` | string (uri) |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `project` | string (uri) |  |
    | `project_uuid` | string (uuid) |  |
    | `project_name` | string |  |
    | `resource` | string |  |
    | `resource_type` | string |  |
    | `resource_name` | string |  |
    | `offering` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `template` | string (uri) |  |
    | `feedback` | any |  |
    | `resolved` | boolean |  |
    | `update_is_available` | boolean |  |
    | `destroy_is_available` | boolean |  |
    | `add_comment_is_available` | boolean |  |
    | `add_attachment_is_available` | boolean |  |
    | `processing_log` | object (free-form) | Internal processing log for debugging order lifecycle events. Visible only to staff. |
    | `order_uuid` | string | Return order UUID if the issue's resource is an Order. |
    | `order_project_uuid` | string | Return order's project UUID if the issue's resource is an Order. |
    | `order_customer_uuid` | string | Return order's customer UUID if the issue's resource is an Order. |
    | `order_resource_name` | string | Return order's resource name if the issue's resource is an Order. |
    | `first_response_deadline` | string (date-time) | Deadline for first response from support staff. |
    | `resolution_deadline` | string (date-time) | Deadline for issue resolution. |
    | `first_response_at` | string (date-time) | Timestamp of first response from support staff. |
    | `sla_breached` | boolean | Whether SLA has been breached for this issue. |
    | `sla_status` | string |  |
    | `parent_issue` | string (uri) |  |
    | `provider_helpdesk` | string (uri) |  |
    | `is_escalated` | boolean | Whether this issue has been escalated. |
    | `escalated_at` | string (date-time) | When the issue was escalated. |
    | `escalation_reason` | string | Reason for escalation. |
    | `is_routed` | boolean |  |
    | `provider_ticket_info` | object (free-form) |  |

---

### Sync


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/support-issues/a1b2c3d4-e5f6-7890-abcd-ef1234567890/sync/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.support_issues import support_issues_sync # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = support_issues_sync.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`support_issues_sync`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/support_issues/support_issues_sync.py)

=== "TypeScript"

    ```typescript
    import { supportIssuesSync } from 'waldur-js-client';
    
    try {
      const response = await supportIssuesSync({
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

    **`200`** - No response body
    

---
