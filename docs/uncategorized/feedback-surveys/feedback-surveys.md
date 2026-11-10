# Feedback Surveys

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/feedback-surveys/` | [List Feedback Surveys](#list-feedback-surveys) |
| <span class="http-badge http-get">GET</span> | `/api/feedback-surveys/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/feedback-surveys/` | [Create](#create) |
| <span class="http-badge http-put">PUT</span> | `/api/feedback-surveys/{uuid}/` | [Update](#update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/feedback-surveys/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-delete">DELETE</span> | `/api/feedback-surveys/{uuid}/` | [Delete](#delete) |
| **Other Actions** | | |
| <span class="http-badge http-get">GET</span> | `/api/feedback-surveys/{uuid}/summary/` | [Summary](#summary) |
| <span class="http-badge http-post">POST</span> | `/api/feedback-surveys/prompt/` | [Prompt](#prompt) |

---
## Core CRUD


### List Feedback Surveys


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/feedback-surveys/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.feedback_survey_o_enum import FeedbackSurveyOEnum # (1)
    from waldur_api_client.api.feedback_surveys import feedback_surveys_list # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = feedback_surveys_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`FeedbackSurveyOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/feedback_survey_o_enum.py)
    2.  **API Source:** [`feedback_surveys_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/feedback_surveys/feedback_surveys_list.py)

=== "TypeScript"

    ```typescript
    import { feedbackSurveysList } from 'waldur-js-client';
    
    try {
      const response = await feedbackSurveysList({
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
    | `name` | string |  |
    | `o` | array | Ordering<br><br> |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `name` | string |  |
    | `intro` | string | Markdown text shown above the questions. |
    | `checklist` | string (uuid) |  |
    | `checklist_name` | string |  |
    | `starts_at` | string (date-time) |  |
    | `ends_at` | string (date-time) |  |
    | `is_active` | boolean |  |
    | `is_open` | boolean |  |
    | `audience` | any |  |
    | `max_prompts` | integer | How many times a user is prompted at most. |
    | `snooze_days` | integer | Days the prompt stays hidden after it is shown or postponed. |


=== "Authorization"

    Staff or support only.

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/feedback-surveys/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.feedback_surveys import feedback_surveys_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = feedback_surveys_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`feedback_surveys_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/feedback_surveys/feedback_surveys_retrieve.py)

=== "TypeScript"

    ```typescript
    import { feedbackSurveysRetrieve } from 'waldur-js-client';
    
    try {
      const response = await feedbackSurveysRetrieve({
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
    | `name` | string |  |
    | `intro` | string | Markdown text shown above the questions. |
    | `checklist` | string (uuid) |  |
    | `checklist_name` | string |  |
    | `starts_at` | string (date-time) |  |
    | `ends_at` | string (date-time) |  |
    | `is_active` | boolean |  |
    | `is_open` | boolean |  |
    | `audience` | any |  |
    | `max_prompts` | integer | How many times a user is prompted at most. |
    | `snooze_days` | integer | Days the prompt stays hidden after it is shown or postponed. |


=== "Authorization"

    Staff or support only.

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/feedback-surveys/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-feedback-survey" \
      checklist="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      starts_at="2023-10-01T12:00:00Z" \
      ends_at="2023-10-01T12:00:00Z" \
      audience_query=null
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.feedback_survey_request import FeedbackSurveyRequest # (1)
    from waldur_api_client.api.feedback_surveys import feedback_surveys_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = FeedbackSurveyRequest(
        name="my-awesome-feedback-survey",
        checklist="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        starts_at="2023-10-01T12:00:00Z",
        ends_at="2023-10-01T12:00:00Z",
        audience_query=null
    )
    response = feedback_surveys_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`FeedbackSurveyRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/feedback_survey_request.py)
    2.  **API Source:** [`feedback_surveys_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/feedback_surveys/feedback_surveys_create.py)

=== "TypeScript"

    ```typescript
    import { feedbackSurveysCreate } from 'waldur-js-client';
    
    try {
      const response = await feedbackSurveysCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "name": "my-awesome-feedback-survey",
        "checklist": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "starts_at": "2023-10-01T12:00:00Z",
        "ends_at": "2023-10-01T12:00:00Z",
        "audience_query": null
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
    | `name` | string | ✓ |  |
    | `intro` | string |  | Markdown text shown above the questions. |
    | `checklist` | string (uuid) | ✓ |  |
    | `starts_at` | string (date-time) | ✓ |  |
    | `ends_at` | string (date-time) | ✓ |  |
    | `is_active` | boolean |  |  |
    | `audience_query` | any | ✓ | <br>_Constraints: write-only_ |
    | `max_prompts` | integer |  | How many times a user is prompted at most. |
    | `snooze_days` | integer |  | Days the prompt stays hidden after it is shown or postponed. |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `name` | string |  |
    | `intro` | string | Markdown text shown above the questions. |
    | `checklist` | string (uuid) |  |
    | `checklist_name` | string |  |
    | `starts_at` | string (date-time) |  |
    | `ends_at` | string (date-time) |  |
    | `is_active` | boolean |  |
    | `is_open` | boolean |  |
    | `audience` | any |  |
    | `max_prompts` | integer | How many times a user is prompted at most. |
    | `snooze_days` | integer | Days the prompt stays hidden after it is shown or postponed. |


=== "Authorization"

    Staff only.

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/feedback-surveys/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-feedback-survey" \
      checklist="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      starts_at="2023-10-01T12:00:00Z" \
      ends_at="2023-10-01T12:00:00Z" \
      audience_query=null
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.feedback_survey_request import FeedbackSurveyRequest # (1)
    from waldur_api_client.api.feedback_surveys import feedback_surveys_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = FeedbackSurveyRequest(
        name="my-awesome-feedback-survey",
        checklist="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        starts_at="2023-10-01T12:00:00Z",
        ends_at="2023-10-01T12:00:00Z",
        audience_query=null
    )
    response = feedback_surveys_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`FeedbackSurveyRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/feedback_survey_request.py)
    2.  **API Source:** [`feedback_surveys_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/feedback_surveys/feedback_surveys_update.py)

=== "TypeScript"

    ```typescript
    import { feedbackSurveysUpdate } from 'waldur-js-client';
    
    try {
      const response = await feedbackSurveysUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "name": "my-awesome-feedback-survey",
        "checklist": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "starts_at": "2023-10-01T12:00:00Z",
        "ends_at": "2023-10-01T12:00:00Z",
        "audience_query": null
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
    | `name` | string | ✓ |  |
    | `intro` | string |  | Markdown text shown above the questions. |
    | `checklist` | string (uuid) | ✓ |  |
    | `starts_at` | string (date-time) | ✓ |  |
    | `ends_at` | string (date-time) | ✓ |  |
    | `is_active` | boolean |  |  |
    | `audience_query` | any | ✓ | <br>_Constraints: write-only_ |
    | `max_prompts` | integer |  | How many times a user is prompted at most. |
    | `snooze_days` | integer |  | Days the prompt stays hidden after it is shown or postponed. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `name` | string |  |
    | `intro` | string | Markdown text shown above the questions. |
    | `checklist` | string (uuid) |  |
    | `checklist_name` | string |  |
    | `starts_at` | string (date-time) |  |
    | `ends_at` | string (date-time) |  |
    | `is_active` | boolean |  |
    | `is_open` | boolean |  |
    | `audience` | any |  |
    | `max_prompts` | integer | How many times a user is prompted at most. |
    | `snooze_days` | integer | Days the prompt stays hidden after it is shown or postponed. |


=== "Authorization"

    Staff only.

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/feedback-surveys/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_feedback_survey_request import PatchedFeedbackSurveyRequest # (1)
    from waldur_api_client.api.feedback_surveys import feedback_surveys_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedFeedbackSurveyRequest()
    response = feedback_surveys_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedFeedbackSurveyRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_feedback_survey_request.py)
    2.  **API Source:** [`feedback_surveys_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/feedback_surveys/feedback_surveys_partial_update.py)

=== "TypeScript"

    ```typescript
    import { feedbackSurveysPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await feedbackSurveysPartialUpdate({
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
    | `name` | string |  |  |
    | `intro` | string |  | Markdown text shown above the questions. |
    | `checklist` | string (uuid) |  |  |
    | `starts_at` | string (date-time) |  |  |
    | `ends_at` | string (date-time) |  |  |
    | `is_active` | boolean |  |  |
    | `audience_query` | any |  | <br>_Constraints: write-only_ |
    | `max_prompts` | integer |  | How many times a user is prompted at most. |
    | `snooze_days` | integer |  | Days the prompt stays hidden after it is shown or postponed. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `created` | string (date-time) |  |
    | `name` | string |  |
    | `intro` | string | Markdown text shown above the questions. |
    | `checklist` | string (uuid) |  |
    | `checklist_name` | string |  |
    | `starts_at` | string (date-time) |  |
    | `ends_at` | string (date-time) |  |
    | `is_active` | boolean |  |
    | `is_open` | boolean |  |
    | `audience` | any |  |
    | `max_prompts` | integer | How many times a user is prompted at most. |
    | `snooze_days` | integer | Days the prompt stays hidden after it is shown or postponed. |


=== "Authorization"

    Staff only.

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/feedback-surveys/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.feedback_surveys import feedback_surveys_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = feedback_surveys_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`feedback_surveys_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/feedback_surveys/feedback_surveys_destroy.py)

=== "TypeScript"

    ```typescript
    import { feedbackSurveysDestroy } from 'waldur-js-client';
    
    try {
      const response = await feedbackSurveysDestroy({
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

    Staff only.

---

## Other Actions


### Summary


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/feedback-surveys/a1b2c3d4-e5f6-7890-abcd-ef1234567890/summary/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.feedback_surveys import feedback_surveys_summary_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = feedback_surveys_summary_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`feedback_surveys_summary_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/feedback_surveys/feedback_surveys_summary_retrieve.py)

=== "TypeScript"

    ```typescript
    import { feedbackSurveysSummaryRetrieve } from 'waldur-js-client';
    
    try {
      const response = await feedbackSurveysSummaryRetrieve({
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
    | `prompted` | integer |
    | `answered` | integer |
    | `dismissed` | integer |
    | `pending` | integer |
    | `expired` | integer |
    | `questions` | array of objects |
    | `questions.question_uuid` | string |
    | `questions.question` | string |
    | `questions.question_type` | string |
    | `questions.answer_count` | integer |
    | `questions.mean` | number (double) |
    | `questions.distribution` | array of objects |
    | `questions.distribution.value` | string |
    | `questions.distribution.label` | string |
    | `questions.distribution.count` | integer |


=== "Authorization"

    Staff or support only.

---

### Prompt

Return the survey to show the current user now, if any, and count it as a prompt.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/feedback-surveys/prompt/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.feedback_surveys import feedback_surveys_prompt # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = feedback_surveys_prompt.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`feedback_surveys_prompt`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/feedback_surveys/feedback_surveys_prompt.py)

=== "TypeScript"

    ```typescript
    import { feedbackSurveysPrompt } from 'waldur-js-client';
    
    try {
      const response = await feedbackSurveysPrompt({
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
    | `request_uuid` | string (uuid) |  |
    | `survey` | object |  |
    | `survey.uuid` | string (uuid) |  |
    | `survey.name` | string |  |
    | `survey.intro` | string | Markdown text shown above the questions. |
    | `survey.ends_at` | string (date-time) |  |
    
    ---
    
    **`204`** - No response body
    


=== "Authorization"

    The caller's own pending feedback request, if any.

---
