# Call Workflow Step Notification Rules

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/call-workflow-step-notification-rules/` | [List Call Workflow Step Notification Rules](#list-call-workflow-step-notification-rules) |
| <span class="http-badge http-get">GET</span> | `/api/call-workflow-step-notification-rules/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/call-workflow-step-notification-rules/` | [Create](#create) |
| <span class="http-badge http-put">PUT</span> | `/api/call-workflow-step-notification-rules/{uuid}/` | [Update](#update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/call-workflow-step-notification-rules/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-delete">DELETE</span> | `/api/call-workflow-step-notification-rules/{uuid}/` | [Delete](#delete) |

---

### List Call Workflow Step Notification Rules


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/call-workflow-step-notification-rules/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.call_workflow_step_notification_rules import call_workflow_step_notification_rules_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = call_workflow_step_notification_rules_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`call_workflow_step_notification_rules_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/call_workflow_step_notification_rules/call_workflow_step_notification_rules_list.py)

=== "TypeScript"

    ```typescript
    import { callWorkflowStepNotificationRulesList } from 'waldur-js-client';
    
    try {
      const response = await callWorkflowStepNotificationRulesList({
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
    | `call_uuid` | string (uuid) |  |
    | `is_enabled` | boolean |  |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `step` | string |  |
    | `trigger` | string |  |
    | `workflow_step_uuid` | string (uuid) |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `workflow_step` | string (uuid) |  |
    | `workflow_step_uuid` | string (uuid) |  |
    | `step` | any |  |
    | `call_uuid` | string (uuid) |  |
    | `trigger` | string | <br>_Enum: `step_started`, `step_completed`, `step_rejected`, `step_expired`, `deadline_approaching`_ |
    | `recipient` | string | <br>_Enum: `applicant`, `responsible_role`, `assigned_reviewers`, `call_managers`, `all_pool_reviewers`, `panel_chair`_ |
    | `days_before` | integer | Only for deadline_approaching: how many days before the step's deadline the reminder is sent. |
    | `is_enabled` | boolean |  |
    | `notified_proposal_roles` | array of strings | Only for an applicant audience: names of the proposal roles whose holders are notified. Empty notifies the proposal creator and every member of the proposal team. |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/call-workflow-step-notification-rules/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.call_workflow_step_notification_rules import call_workflow_step_notification_rules_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = call_workflow_step_notification_rules_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`call_workflow_step_notification_rules_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/call_workflow_step_notification_rules/call_workflow_step_notification_rules_retrieve.py)

=== "TypeScript"

    ```typescript
    import { callWorkflowStepNotificationRulesRetrieve } from 'waldur-js-client';
    
    try {
      const response = await callWorkflowStepNotificationRulesRetrieve({
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
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `workflow_step` | string (uuid) |  |
    | `workflow_step_uuid` | string (uuid) |  |
    | `step` | any |  |
    | `call_uuid` | string (uuid) |  |
    | `trigger` | string | <br>_Enum: `step_started`, `step_completed`, `step_rejected`, `step_expired`, `deadline_approaching`_ |
    | `recipient` | string | <br>_Enum: `applicant`, `responsible_role`, `assigned_reviewers`, `call_managers`, `all_pool_reviewers`, `panel_chair`_ |
    | `days_before` | integer | Only for deadline_approaching: how many days before the step's deadline the reminder is sent. |
    | `is_enabled` | boolean |  |
    | `notified_proposal_roles` | array of strings | Only for an applicant audience: names of the proposal roles whose holders are notified. Empty notifies the proposal creator and every member of the proposal team. |

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/call-workflow-step-notification-rules/ \
      Authorization:"Token YOUR_API_TOKEN" \
      workflow_step="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      trigger="step_started" \
      recipient="applicant"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.call_workflow_step_notification_rule_request import CallWorkflowStepNotificationRuleRequest # (1)
    from waldur_api_client.api.call_workflow_step_notification_rules import call_workflow_step_notification_rules_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = CallWorkflowStepNotificationRuleRequest(
        workflow_step="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        trigger="step_started",
        recipient="applicant"
    )
    response = call_workflow_step_notification_rules_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`CallWorkflowStepNotificationRuleRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/call_workflow_step_notification_rule_request.py)
    2.  **API Source:** [`call_workflow_step_notification_rules_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/call_workflow_step_notification_rules/call_workflow_step_notification_rules_create.py)

=== "TypeScript"

    ```typescript
    import { callWorkflowStepNotificationRulesCreate } from 'waldur-js-client';
    
    try {
      const response = await callWorkflowStepNotificationRulesCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "workflow_step": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "trigger": "step_started",
        "recipient": "applicant"
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
    | `workflow_step` | string (uuid) | ✓ |  |
    | `trigger` | string | ✓ | <br>_Enum: `step_started`, `step_completed`, `step_rejected`, `step_expired`, `deadline_approaching`_ |
    | `recipient` | string | ✓ | <br>_Enum: `applicant`, `responsible_role`, `assigned_reviewers`, `call_managers`, `all_pool_reviewers`, `panel_chair`_ |
    | `days_before` | integer |  | Only for deadline_approaching: how many days before the step's deadline the reminder is sent. |
    | `is_enabled` | boolean |  |  |
    | `notified_proposal_roles` | array of strings |  | Only for an applicant audience: names of the proposal roles whose holders are notified. Empty notifies the proposal creator and every member of the proposal team. |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `workflow_step` | string (uuid) |  |
    | `workflow_step_uuid` | string (uuid) |  |
    | `step` | any |  |
    | `call_uuid` | string (uuid) |  |
    | `trigger` | string | <br>_Enum: `step_started`, `step_completed`, `step_rejected`, `step_expired`, `deadline_approaching`_ |
    | `recipient` | string | <br>_Enum: `applicant`, `responsible_role`, `assigned_reviewers`, `call_managers`, `all_pool_reviewers`, `panel_chair`_ |
    | `days_before` | integer | Only for deadline_approaching: how many days before the step's deadline the reminder is sent. |
    | `is_enabled` | boolean |  |
    | `notified_proposal_roles` | array of strings | Only for an applicant audience: names of the proposal roles whose holders are notified. Empty notifies the proposal creator and every member of the proposal team. |

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/call-workflow-step-notification-rules/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      workflow_step="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      trigger="step_started" \
      recipient="applicant"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.call_workflow_step_notification_rule_request import CallWorkflowStepNotificationRuleRequest # (1)
    from waldur_api_client.api.call_workflow_step_notification_rules import call_workflow_step_notification_rules_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = CallWorkflowStepNotificationRuleRequest(
        workflow_step="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        trigger="step_started",
        recipient="applicant"
    )
    response = call_workflow_step_notification_rules_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`CallWorkflowStepNotificationRuleRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/call_workflow_step_notification_rule_request.py)
    2.  **API Source:** [`call_workflow_step_notification_rules_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/call_workflow_step_notification_rules/call_workflow_step_notification_rules_update.py)

=== "TypeScript"

    ```typescript
    import { callWorkflowStepNotificationRulesUpdate } from 'waldur-js-client';
    
    try {
      const response = await callWorkflowStepNotificationRulesUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "workflow_step": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "trigger": "step_started",
        "recipient": "applicant"
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
    | `workflow_step` | string (uuid) | ✓ |  |
    | `trigger` | string | ✓ | <br>_Enum: `step_started`, `step_completed`, `step_rejected`, `step_expired`, `deadline_approaching`_ |
    | `recipient` | string | ✓ | <br>_Enum: `applicant`, `responsible_role`, `assigned_reviewers`, `call_managers`, `all_pool_reviewers`, `panel_chair`_ |
    | `days_before` | integer |  | Only for deadline_approaching: how many days before the step's deadline the reminder is sent. |
    | `is_enabled` | boolean |  |  |
    | `notified_proposal_roles` | array of strings |  | Only for an applicant audience: names of the proposal roles whose holders are notified. Empty notifies the proposal creator and every member of the proposal team. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `workflow_step` | string (uuid) |  |
    | `workflow_step_uuid` | string (uuid) |  |
    | `step` | any |  |
    | `call_uuid` | string (uuid) |  |
    | `trigger` | string | <br>_Enum: `step_started`, `step_completed`, `step_rejected`, `step_expired`, `deadline_approaching`_ |
    | `recipient` | string | <br>_Enum: `applicant`, `responsible_role`, `assigned_reviewers`, `call_managers`, `all_pool_reviewers`, `panel_chair`_ |
    | `days_before` | integer | Only for deadline_approaching: how many days before the step's deadline the reminder is sent. |
    | `is_enabled` | boolean |  |
    | `notified_proposal_roles` | array of strings | Only for an applicant audience: names of the proposal roles whose holders are notified. Empty notifies the proposal creator and every member of the proposal team. |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/call-workflow-step-notification-rules/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_call_workflow_step_notification_rule_request import PatchedCallWorkflowStepNotificationRuleRequest # (1)
    from waldur_api_client.api.call_workflow_step_notification_rules import call_workflow_step_notification_rules_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedCallWorkflowStepNotificationRuleRequest()
    response = call_workflow_step_notification_rules_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedCallWorkflowStepNotificationRuleRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_call_workflow_step_notification_rule_request.py)
    2.  **API Source:** [`call_workflow_step_notification_rules_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/call_workflow_step_notification_rules/call_workflow_step_notification_rules_partial_update.py)

=== "TypeScript"

    ```typescript
    import { callWorkflowStepNotificationRulesPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await callWorkflowStepNotificationRulesPartialUpdate({
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
    | `workflow_step` | string (uuid) |  |  |
    | `trigger` | string |  | <br>_Enum: `step_started`, `step_completed`, `step_rejected`, `step_expired`, `deadline_approaching`_ |
    | `recipient` | string |  | <br>_Enum: `applicant`, `responsible_role`, `assigned_reviewers`, `call_managers`, `all_pool_reviewers`, `panel_chair`_ |
    | `days_before` | integer |  | Only for deadline_approaching: how many days before the step's deadline the reminder is sent. |
    | `is_enabled` | boolean |  |  |
    | `notified_proposal_roles` | array of strings |  | Only for an applicant audience: names of the proposal roles whose holders are notified. Empty notifies the proposal creator and every member of the proposal team. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `workflow_step` | string (uuid) |  |
    | `workflow_step_uuid` | string (uuid) |  |
    | `step` | any |  |
    | `call_uuid` | string (uuid) |  |
    | `trigger` | string | <br>_Enum: `step_started`, `step_completed`, `step_rejected`, `step_expired`, `deadline_approaching`_ |
    | `recipient` | string | <br>_Enum: `applicant`, `responsible_role`, `assigned_reviewers`, `call_managers`, `all_pool_reviewers`, `panel_chair`_ |
    | `days_before` | integer | Only for deadline_approaching: how many days before the step's deadline the reminder is sent. |
    | `is_enabled` | boolean |  |
    | `notified_proposal_roles` | array of strings | Only for an applicant audience: names of the proposal roles whose holders are notified. Empty notifies the proposal creator and every member of the proposal team. |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/call-workflow-step-notification-rules/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.call_workflow_step_notification_rules import call_workflow_step_notification_rules_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = call_workflow_step_notification_rules_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`call_workflow_step_notification_rules_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/call_workflow_step_notification_rules/call_workflow_step_notification_rules_destroy.py)

=== "TypeScript"

    ```typescript
    import { callWorkflowStepNotificationRulesDestroy } from 'waldur-js-client';
    
    try {
      const response = await callWorkflowStepNotificationRulesDestroy({
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
