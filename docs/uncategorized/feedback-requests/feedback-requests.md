# Feedback Requests

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/feedback-requests/` | [List Feedback Requests](#list-feedback-requests) |
| <span class="http-badge http-get">GET</span> | `/api/feedback-requests/{uuid}/` | [Retrieve](#retrieve) |
| **Other Actions** | | |
| <span class="http-badge http-get">GET</span> | `/api/feedback-requests/{uuid}/checklist/` | [Get checklist with questions and existing answers](#get-checklist-with-questions-and-existing-answers) |
| <span class="http-badge http-get">GET</span> | `/api/feedback-requests/{uuid}/completion_status/` | [Get checklist completion status](#get-checklist-completion-status) |
| <span class="http-badge http-post">POST</span> | `/api/feedback-requests/{uuid}/dismiss/` | [Dismiss](#dismiss) |
| <span class="http-badge http-post">POST</span> | `/api/feedback-requests/{uuid}/later/` | [Later](#later) |
| <span class="http-badge http-post">POST</span> | `/api/feedback-requests/{uuid}/submit_answers/` | [Submit answers. A complete submission marks the request answered](#submit-answers-a-complete-submission-marks-the-request-answered) |

---
## Core CRUD


### List Feedback Requests


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/feedback-requests/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.feedback_request_o_enum import FeedbackRequestOEnum # (1)
    from waldur_api_client.models.feedback_state_enum import FeedbackStateEnum # (2)
    from waldur_api_client.api.feedback_requests import feedback_requests_list # (3)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = feedback_requests_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`FeedbackRequestOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/feedback_request_o_enum.py)
    2.  **Model Source:** [`FeedbackStateEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/feedback_state_enum.py)
    3.  **API Source:** [`feedback_requests_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/feedback_requests/feedback_requests_list.py)

=== "TypeScript"

    ```typescript
    import { feedbackRequestsList } from 'waldur-js-client';
    
    try {
      const response = await feedbackRequestsList({
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
    | `answered_after` | string (date) |  |
    | `answered_before` | string (date) |  |
    | `customer_uuid` | string (uuid) |  |
    | `o` | array | Ordering<br><br> |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `state` | array |  |
    | `survey_uuid` | string (uuid) |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `survey_uuid` | string (uuid) |  |
    | `survey_name` | string |  |
    | `user_uuid` | string (uuid) |  |
    | `user_full_name` | string |  |
    | `user_username` | string | Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters |
    | `user_email` | string (email) |  |
    | `organization_names` | array of strings |  |
    | `state` | any |  |
    | `prompt_count` | integer |  |
    | `snoozed_until` | string (date-time) |  |
    | `answered_at` | string (date-time) |  |
    | `answers` | array of objects |  |
    | `answers.question_uuid` | string |  |
    | `answers.question` | string | Question description. |
    | `answers.question_type` | string |  |
    | `answers.answer` | any | Human-readable answer value; select-type option UUIDs are resolved to their labels. |
    | `answers.min_value` | string (decimal) |  |
    | `answers.max_value` | string (decimal) |  |
    | `answers.likert_scale_length` | integer |  |
    | `answers.likert_low_label` | string |  |
    | `answers.likert_high_label` | string |  |
    | `answers.modified` | string (date-time) | When this answer was last saved. |


=== "Authorization"

    Any signed-in user.
    
    The caller's own feedback requests; staff and support see all.

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/feedback-requests/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.feedback_requests import feedback_requests_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = feedback_requests_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`feedback_requests_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/feedback_requests/feedback_requests_retrieve.py)

=== "TypeScript"

    ```typescript
    import { feedbackRequestsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await feedbackRequestsRetrieve({
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
    | `created` | string (date-time) |  |
    | `survey_uuid` | string (uuid) |  |
    | `survey_name` | string |  |
    | `user_uuid` | string (uuid) |  |
    | `user_full_name` | string |  |
    | `user_username` | string | Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters |
    | `user_email` | string (email) |  |
    | `organization_names` | array of strings |  |
    | `state` | any |  |
    | `prompt_count` | integer |  |
    | `snoozed_until` | string (date-time) |  |
    | `answered_at` | string (date-time) |  |
    | `answers` | array of objects |  |
    | `answers.question_uuid` | string |  |
    | `answers.question` | string | Question description. |
    | `answers.question_type` | string |  |
    | `answers.answer` | any | Human-readable answer value; select-type option UUIDs are resolved to their labels. |
    | `answers.min_value` | string (decimal) |  |
    | `answers.max_value` | string (decimal) |  |
    | `answers.likert_scale_length` | integer |  |
    | `answers.likert_low_label` | string |  |
    | `answers.likert_high_label` | string |  |
    | `answers.modified` | string (date-time) | When this answer was last saved. |


=== "Authorization"

    Any signed-in user.
    
    The caller's own feedback requests; staff and support see all.

---

## Other Actions


### Get checklist with questions and existing answers

Get checklist with questions and existing answers.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/feedback-requests/a1b2c3d4-e5f6-7890-abcd-ef1234567890/checklist/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.feedback_requests import feedback_requests_checklist_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = feedback_requests_checklist_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`feedback_requests_checklist_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/feedback_requests/feedback_requests_checklist_retrieve.py)

=== "TypeScript"

    ```typescript
    import { feedbackRequestsChecklistRetrieve } from 'waldur-js-client';
    
    try {
      const response = await feedbackRequestsChecklistRetrieve({
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

    | Name | Type | Description |
    |---|---|---|
    | `include_all` | boolean | If true, returns all questions including hidden ones (for dynamic form visibility). Default: false. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `checklist` | any |  |
    | `completion` | object |  |
    | `completion.uuid` | string (uuid) |  |
    | `completion.is_completed` | boolean | Whether all required questions have been answered |
    | `completion.completion_percentage` | number (double) |  |
    | `completion.unanswered_required_questions` | array of anys |  |
    | `completion.checklist_name` | string |  |
    | `completion.checklist_description` | string |  |
    | `completion.created` | string (date-time) |  |
    | `completion.modified` | string (date-time) |  |
    | `questions` | array of objects |  |
    | `questions.uuid` | string (uuid) |  |
    | `questions.description` | string |  |
    | `questions.user_guidance` | string |  |
    | `questions.question_type` | any | Type of question and expected answer format |
    | `questions.required` | boolean |  |
    | `questions.order` | integer |  |
    | `questions.existing_answer` | any |  |
    | `questions.question_options` | array of anys |  |
    | `questions.min_value` | string (decimal) | Minimum value allowed for NUMBER, YEAR, and RATING type questions |
    | `questions.max_value` | string (decimal) | Maximum value allowed for NUMBER, YEAR, and RATING type questions |
    | `questions.allowed_file_types` | object (free-form) | List of allowed file extensions (e.g., ['.pdf', '.doc', '.docx']). If empty, all file types are allowed. |
    | `questions.allowed_mime_types` | object (free-form) | List of allowed MIME types (e.g., ['application/pdf', 'application/msword']). If empty, MIME type validation is not enforced. When both extensions and MIME types are specified, files must match both criteria for security. |
    | `questions.max_file_size_mb` | integer | Maximum file size in megabytes. If not set, no size limit is enforced. |
    | `questions.max_files_count` | integer | Maximum number of files allowed for MULTIPLE_FILES type questions. If not set, no count limit is enforced. |
    | `questions.likert_scale_length` | any | Number of points on the Likert scale (3, 5, or 7). Required for LIKERT type questions. |
    | `questions.likert_low_label` | string | Label for the lowest point on the Likert scale (e.g. 'Strongly disagree'). Optional. |
    | `questions.likert_high_label` | string | Label for the highest point on the Likert scale (e.g. 'Strongly agree'). Optional. |
    | `questions.likert_allow_na` | boolean | Allow respondents to choose 'N/A' as an answer for LIKERT type questions. |
    | `questions.rich_text_char_limit` | integer | Maximum number of characters allowed in RICH_TEXT type answers. If not set, no limit is enforced. |
    | `questions.rich_text_toolbar_level` | any | Toolbar level for the rich text editor: 'minimal', 'standard', or 'extended'. |
    | `questions.dependencies_info` | any |  |
    
    ---
    
    **`400`** - 
    
    
    ---
    
    **`404`** - 
    


=== "Authorization"

    The caller's own feedback request.

---

### Get checklist completion status

Get checklist completion status.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/feedback-requests/a1b2c3d4-e5f6-7890-abcd-ef1234567890/completion_status/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.feedback_requests import feedback_requests_completion_status_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = feedback_requests_completion_status_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`feedback_requests_completion_status_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/feedback_requests/feedback_requests_completion_status_retrieve.py)

=== "TypeScript"

    ```typescript
    import { feedbackRequestsCompletionStatusRetrieve } from 'waldur-js-client';
    
    try {
      const response = await feedbackRequestsCompletionStatusRetrieve({
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
    | `is_completed` | boolean | Whether all required questions have been answered |
    | `completion_percentage` | number (double) |  |
    | `unanswered_required_questions` | array of anys |  |
    | `checklist_name` | string |  |
    | `checklist_description` | string |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    
    ---
    
    **`400`** - 
    
    
    ---
    
    **`404`** - 
    


=== "Authorization"

    The caller's own feedback request.

---

### Dismiss


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/feedback-requests/a1b2c3d4-e5f6-7890-abcd-ef1234567890/dismiss/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.feedback_requests import feedback_requests_dismiss # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = feedback_requests_dismiss.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`feedback_requests_dismiss`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/feedback_requests/feedback_requests_dismiss.py)

=== "TypeScript"

    ```typescript
    import { feedbackRequestsDismiss } from 'waldur-js-client';
    
    try {
      const response = await feedbackRequestsDismiss({
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
    


=== "Authorization"

    The caller's own feedback request.

---

### Later

Postpone the prompt. Answers given so far are kept as a draft, leaving out any that are not valid; the request stays pending.


=== "HTTPie"

    ```bash
    echo '[{"question_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "answer_data": null}]' | http \
      POST \
      https://api.example.com/api/feedback-requests/a1b2c3d4-e5f6-7890-abcd-ef1234567890/later/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.feedback_requests import feedback_requests_later # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = feedback_requests_later.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`feedback_requests_later`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/feedback_requests/feedback_requests_later.py)

=== "TypeScript"

    ```typescript
    import { feedbackRequestsLater } from 'waldur-js-client';
    
    try {
      const response = await feedbackRequestsLater({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: [{"question_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "answer_data": null}]
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

    The request body is an array of objects, where each object has the following structure:
    
    | Field | Type | Required |
    |---|---|---|
    | `question_uuid` | string (uuid) | ✓ |
    | `answer_data` | any | ✓ |


=== "Responses"

    **`200`** - No response body
    


=== "Authorization"

    The caller's own feedback request.

---

### Submit answers. A complete submission marks the request answered

Submit answers. A complete submission marks the request answered.


=== "HTTPie"

    ```bash
    echo '[{"question_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "answer_data": null}]' | http \
      POST \
      https://api.example.com/api/feedback-requests/a1b2c3d4-e5f6-7890-abcd-ef1234567890/submit_answers/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.feedback_requests import feedback_requests_submit_answers # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = feedback_requests_submit_answers.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`feedback_requests_submit_answers`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/feedback_requests/feedback_requests_submit_answers.py)

=== "TypeScript"

    ```typescript
    import { feedbackRequestsSubmitAnswers } from 'waldur-js-client';
    
    try {
      const response = await feedbackRequestsSubmitAnswers({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: [{"question_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "answer_data": null}]
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

    The request body is an array of objects, where each object has the following structure:
    
    | Field | Type | Required |
    |---|---|---|
    | `question_uuid` | string (uuid) | ✓ |
    | `answer_data` | any | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `detail` | string |  |
    | `completion` | object |  |
    | `completion.uuid` | string (uuid) |  |
    | `completion.is_completed` | boolean | Whether all required questions have been answered |
    | `completion.completion_percentage` | number (double) |  |
    | `completion.unanswered_required_questions` | array of anys |  |
    | `completion.checklist_name` | string |  |
    | `completion.checklist_description` | string |  |
    | `completion.created` | string (date-time) |  |
    | `completion.modified` | string (date-time) |  |


=== "Authorization"

    The caller's own feedback request.

---
