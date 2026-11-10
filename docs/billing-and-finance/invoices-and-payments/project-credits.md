# Project Credits

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/project-credits/` | [List Project Credits](#list-project-credits) |
| <span class="http-badge http-get">GET</span> | `/api/project-credits/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/project-credits/` | [Create](#create) |
| <span class="http-badge http-put">PUT</span> | `/api/project-credits/{uuid}/` | [Update](#update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/project-credits/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-delete">DELETE</span> | `/api/project-credits/{uuid}/` | [Delete](#delete) |
| **Other Actions** | | |
| <span class="http-badge http-get">GET</span> | `/api/project-credits/{uuid}/earlier_invoices/` | [Earlier invoices of the project and what credit paid of them](#earlier-invoices-of-the-project-and-what-credit-paid-of-them) |
| <span class="http-badge http-post">POST</span> | `/api/project-credits/{uuid}/pay_earlier_invoices/` | [Pay earlier invoices from the project credit](#pay-earlier-invoices-from-the-project-credit) |

---
## Core CRUD


### List Project Credits


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/project-credits/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.project_credit_o_enum import ProjectCreditOEnum # (1)
    from waldur_api_client.api.project_credits import project_credits_list # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = project_credits_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`ProjectCreditOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/project_credit_o_enum.py)
    2.  **API Source:** [`project_credits_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/project_credits/project_credits_list.py)

=== "TypeScript"

    ```typescript
    import { projectCreditsList } from 'waldur-js-client';
    
    try {
      const response = await projectCreditsList({
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
    | `customer_name` | string |  |
    | `customer_slug` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `o` | array | Ordering<br><br> |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `project_name` | string |  |
    | `project_uuid` | string (uuid) |  |
    | `query` | string |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `value` | string (decimal) |  |
    | `project` | string (uri) |  |
    | `project_name` | string |  |
    | `project_uuid` | string (uuid) |  |
    | `project_slug` | string |  |
    | `customer_name` | string |  |
    | `customer_slug` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_credit` | string (decimal) |  |
    | `allocated_customer_credit` | string |  |
    | `consumption_last_month` | number (double) | Credit drawn by this project in the previous month.  None when that month has no invoice at all — no billing period is not the same statement as "drew nothing", and callers should be able to tell them apart. |
    | `creditable_cost_this_month` | string (decimal) |  |
    | `spendable_value` | string (decimal) |  |
    | `is_limited_by_organization_credit` | boolean | True when the organization balance, not this allocation, is binding. |
    | `offerings` | array of objects |  |
    | `offerings.uuid` | string (uuid) |  |
    | `offerings.url` | string (uri) |  |
    | `offerings.type` | string |  |
    | `offerings.name` | string |  |
    | `end_date` | string (date) |  |
    | `expected_consumption` | string (decimal) |  |
    | `minimal_consumption` | number (double) |  |
    | `minimal_consumption_logic` | string | <br>_Enum: `fixed`, `linear`_ |
    | `grace_coefficient` | string (decimal) |  |
    | `apply_as_minimal_consumption` | boolean |  |
    | `mark_unused_credit_as_spent_on_project_termination` | boolean |  |
    | `pay_earlier_invoices` | boolean | Also pay the cost of earlier, closed invoices of the project that no credit covered. Staff only. |
    | `earlier_invoices_from` | string (date) | First month of earlier invoices to pay, as its first day. Empty: from the first invoice. |
    | `earlier_invoices_until` | string (date) | Last month of earlier invoices to pay, as its first day. Empty: up to the last closed invoice. |
    | `earlier_invoices_compensate_in` | any | Which invoice a payment of an earlier invoice is written on: the current month's, or the paid month's own, which changes an invoice already issued. |


=== "Authorization"

    Any signed-in user.
    
    Returns only objects the caller holds a role on; staff and support see all.

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/project-credits/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.project_credits import project_credits_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = project_credits_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`project_credits_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/project_credits/project_credits_retrieve.py)

=== "TypeScript"

    ```typescript
    import { projectCreditsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await projectCreditsRetrieve({
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
    | `url` | string (uri) |  |
    | `value` | string (decimal) |  |
    | `project` | string (uri) |  |
    | `project_name` | string |  |
    | `project_uuid` | string (uuid) |  |
    | `project_slug` | string |  |
    | `customer_name` | string |  |
    | `customer_slug` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_credit` | string (decimal) |  |
    | `allocated_customer_credit` | string |  |
    | `consumption_last_month` | number (double) | Credit drawn by this project in the previous month.  None when that month has no invoice at all — no billing period is not the same statement as "drew nothing", and callers should be able to tell them apart. |
    | `creditable_cost_this_month` | string (decimal) |  |
    | `spendable_value` | string (decimal) |  |
    | `is_limited_by_organization_credit` | boolean | True when the organization balance, not this allocation, is binding. |
    | `offerings` | array of objects |  |
    | `offerings.uuid` | string (uuid) |  |
    | `offerings.url` | string (uri) |  |
    | `offerings.type` | string |  |
    | `offerings.name` | string |  |
    | `end_date` | string (date) |  |
    | `expected_consumption` | string (decimal) |  |
    | `minimal_consumption` | number (double) |  |
    | `minimal_consumption_logic` | string | <br>_Enum: `fixed`, `linear`_ |
    | `grace_coefficient` | string (decimal) |  |
    | `apply_as_minimal_consumption` | boolean |  |
    | `mark_unused_credit_as_spent_on_project_termination` | boolean |  |
    | `pay_earlier_invoices` | boolean | Also pay the cost of earlier, closed invoices of the project that no credit covered. Staff only. |
    | `earlier_invoices_from` | string (date) | First month of earlier invoices to pay, as its first day. Empty: from the first invoice. |
    | `earlier_invoices_until` | string (date) | Last month of earlier invoices to pay, as its first day. Empty: up to the last closed invoice. |
    | `earlier_invoices_compensate_in` | any | Which invoice a payment of an earlier invoice is written on: the current month's, or the paid month's own, which changes an invoice already issued. |


=== "Authorization"

    Any signed-in user.
    
    Returns only objects the caller holds a role on; staff and support see all.

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/project-credits/ \
      Authorization:"Token YOUR_API_TOKEN" \
      project="https://api.example.com/api/project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.project_credit_request import ProjectCreditRequest # (1)
    from waldur_api_client.api.project_credits import project_credits_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ProjectCreditRequest(
        project="https://api.example.com/api/project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    )
    response = project_credits_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ProjectCreditRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/project_credit_request.py)
    2.  **API Source:** [`project_credits_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/project_credits/project_credits_create.py)

=== "TypeScript"

    ```typescript
    import { projectCreditsCreate } from 'waldur-js-client';
    
    try {
      const response = await projectCreditsCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "project": "https://api.example.com/api/project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
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
    | `value` | string (decimal) |  |  |
    | `project` | string (uri) | ✓ |  |
    | `end_date` | string (date) |  |  |
    | `expected_consumption` | string (decimal) |  |  |
    | `minimal_consumption_logic` | string |  | <br>_Enum: `fixed`, `linear`_ |
    | `grace_coefficient` | string (decimal) |  |  |
    | `apply_as_minimal_consumption` | boolean |  |  |
    | `mark_unused_credit_as_spent_on_project_termination` | boolean |  |  |
    | `pay_earlier_invoices` | boolean |  | Also pay the cost of earlier, closed invoices of the project that no credit covered. Staff only. |
    | `earlier_invoices_from` | string (date) |  | First month of earlier invoices to pay, as its first day. Empty: from the first invoice. |
    | `earlier_invoices_until` | string (date) |  | Last month of earlier invoices to pay, as its first day. Empty: up to the last closed invoice. |
    | `earlier_invoices_compensate_in` | any |  | Which invoice a payment of an earlier invoice is written on: the current month's, or the paid month's own, which changes an invoice already issued. |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `value` | string (decimal) |  |
    | `project` | string (uri) |  |
    | `project_name` | string |  |
    | `project_uuid` | string (uuid) |  |
    | `project_slug` | string |  |
    | `customer_name` | string |  |
    | `customer_slug` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_credit` | string (decimal) |  |
    | `allocated_customer_credit` | string |  |
    | `consumption_last_month` | number (double) | Credit drawn by this project in the previous month.  None when that month has no invoice at all — no billing period is not the same statement as "drew nothing", and callers should be able to tell them apart. |
    | `creditable_cost_this_month` | string (decimal) |  |
    | `spendable_value` | string (decimal) |  |
    | `is_limited_by_organization_credit` | boolean | True when the organization balance, not this allocation, is binding. |
    | `offerings` | array of objects |  |
    | `offerings.uuid` | string (uuid) |  |
    | `offerings.url` | string (uri) |  |
    | `offerings.type` | string |  |
    | `offerings.name` | string |  |
    | `end_date` | string (date) |  |
    | `expected_consumption` | string (decimal) |  |
    | `minimal_consumption` | number (double) |  |
    | `minimal_consumption_logic` | string | <br>_Enum: `fixed`, `linear`_ |
    | `grace_coefficient` | string (decimal) |  |
    | `apply_as_minimal_consumption` | boolean |  |
    | `mark_unused_credit_as_spent_on_project_termination` | boolean |  |
    | `pay_earlier_invoices` | boolean | Also pay the cost of earlier, closed invoices of the project that no credit covered. Staff only. |
    | `earlier_invoices_from` | string (date) | First month of earlier invoices to pay, as its first day. Empty: from the first invoice. |
    | `earlier_invoices_until` | string (date) | Last month of earlier invoices to pay, as its first day. Empty: up to the last closed invoice. |
    | `earlier_invoices_compensate_in` | any | Which invoice a payment of an earlier invoice is written on: the current month's, or the paid month's own, which changes an invoice already issued. |


=== "Authorization"

    For the `project` named in the request, the `CUSTOMER.OWNER` role on its customer.
    
    A request acting as staff always meets the permission and role requirements.

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/project-credits/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      project="https://api.example.com/api/project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.project_credit_request import ProjectCreditRequest # (1)
    from waldur_api_client.api.project_credits import project_credits_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ProjectCreditRequest(
        project="https://api.example.com/api/project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
    )
    response = project_credits_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ProjectCreditRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/project_credit_request.py)
    2.  **API Source:** [`project_credits_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/project_credits/project_credits_update.py)

=== "TypeScript"

    ```typescript
    import { projectCreditsUpdate } from 'waldur-js-client';
    
    try {
      const response = await projectCreditsUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "project": "https://api.example.com/api/project/a1b2c3d4-e5f6-7890-abcd-ef1234567890/"
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
    | `value` | string (decimal) |  |  |
    | `project` | string (uri) | ✓ |  |
    | `end_date` | string (date) |  |  |
    | `expected_consumption` | string (decimal) |  |  |
    | `minimal_consumption_logic` | string |  | <br>_Enum: `fixed`, `linear`_ |
    | `grace_coefficient` | string (decimal) |  |  |
    | `apply_as_minimal_consumption` | boolean |  |  |
    | `mark_unused_credit_as_spent_on_project_termination` | boolean |  |  |
    | `pay_earlier_invoices` | boolean |  | Also pay the cost of earlier, closed invoices of the project that no credit covered. Staff only. |
    | `earlier_invoices_from` | string (date) |  | First month of earlier invoices to pay, as its first day. Empty: from the first invoice. |
    | `earlier_invoices_until` | string (date) |  | Last month of earlier invoices to pay, as its first day. Empty: up to the last closed invoice. |
    | `earlier_invoices_compensate_in` | any |  | Which invoice a payment of an earlier invoice is written on: the current month's, or the paid month's own, which changes an invoice already issued. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `value` | string (decimal) |  |
    | `project` | string (uri) |  |
    | `project_name` | string |  |
    | `project_uuid` | string (uuid) |  |
    | `project_slug` | string |  |
    | `customer_name` | string |  |
    | `customer_slug` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_credit` | string (decimal) |  |
    | `allocated_customer_credit` | string |  |
    | `consumption_last_month` | number (double) | Credit drawn by this project in the previous month.  None when that month has no invoice at all — no billing period is not the same statement as "drew nothing", and callers should be able to tell them apart. |
    | `creditable_cost_this_month` | string (decimal) |  |
    | `spendable_value` | string (decimal) |  |
    | `is_limited_by_organization_credit` | boolean | True when the organization balance, not this allocation, is binding. |
    | `offerings` | array of objects |  |
    | `offerings.uuid` | string (uuid) |  |
    | `offerings.url` | string (uri) |  |
    | `offerings.type` | string |  |
    | `offerings.name` | string |  |
    | `end_date` | string (date) |  |
    | `expected_consumption` | string (decimal) |  |
    | `minimal_consumption` | number (double) |  |
    | `minimal_consumption_logic` | string | <br>_Enum: `fixed`, `linear`_ |
    | `grace_coefficient` | string (decimal) |  |
    | `apply_as_minimal_consumption` | boolean |  |
    | `mark_unused_credit_as_spent_on_project_termination` | boolean |  |
    | `pay_earlier_invoices` | boolean | Also pay the cost of earlier, closed invoices of the project that no credit covered. Staff only. |
    | `earlier_invoices_from` | string (date) | First month of earlier invoices to pay, as its first day. Empty: from the first invoice. |
    | `earlier_invoices_until` | string (date) | Last month of earlier invoices to pay, as its first day. Empty: up to the last closed invoice. |
    | `earlier_invoices_compensate_in` | any | Which invoice a payment of an earlier invoice is written on: the current month's, or the paid month's own, which changes an invoice already issued. |


=== "Authorization"

    The `CUSTOMER.OWNER` role on the customer.
    
    A request acting as staff always meets the permission and role requirements.

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/project-credits/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_project_credit_request import PatchedProjectCreditRequest # (1)
    from waldur_api_client.api.project_credits import project_credits_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedProjectCreditRequest()
    response = project_credits_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedProjectCreditRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_project_credit_request.py)
    2.  **API Source:** [`project_credits_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/project_credits/project_credits_partial_update.py)

=== "TypeScript"

    ```typescript
    import { projectCreditsPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await projectCreditsPartialUpdate({
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
    | `value` | string (decimal) |  |  |
    | `project` | string (uri) |  |  |
    | `end_date` | string (date) |  |  |
    | `expected_consumption` | string (decimal) |  |  |
    | `minimal_consumption_logic` | string |  | <br>_Enum: `fixed`, `linear`_ |
    | `grace_coefficient` | string (decimal) |  |  |
    | `apply_as_minimal_consumption` | boolean |  |  |
    | `mark_unused_credit_as_spent_on_project_termination` | boolean |  |  |
    | `pay_earlier_invoices` | boolean |  | Also pay the cost of earlier, closed invoices of the project that no credit covered. Staff only. |
    | `earlier_invoices_from` | string (date) |  | First month of earlier invoices to pay, as its first day. Empty: from the first invoice. |
    | `earlier_invoices_until` | string (date) |  | Last month of earlier invoices to pay, as its first day. Empty: up to the last closed invoice. |
    | `earlier_invoices_compensate_in` | any |  | Which invoice a payment of an earlier invoice is written on: the current month's, or the paid month's own, which changes an invoice already issued. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `value` | string (decimal) |  |
    | `project` | string (uri) |  |
    | `project_name` | string |  |
    | `project_uuid` | string (uuid) |  |
    | `project_slug` | string |  |
    | `customer_name` | string |  |
    | `customer_slug` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_credit` | string (decimal) |  |
    | `allocated_customer_credit` | string |  |
    | `consumption_last_month` | number (double) | Credit drawn by this project in the previous month.  None when that month has no invoice at all — no billing period is not the same statement as "drew nothing", and callers should be able to tell them apart. |
    | `creditable_cost_this_month` | string (decimal) |  |
    | `spendable_value` | string (decimal) |  |
    | `is_limited_by_organization_credit` | boolean | True when the organization balance, not this allocation, is binding. |
    | `offerings` | array of objects |  |
    | `offerings.uuid` | string (uuid) |  |
    | `offerings.url` | string (uri) |  |
    | `offerings.type` | string |  |
    | `offerings.name` | string |  |
    | `end_date` | string (date) |  |
    | `expected_consumption` | string (decimal) |  |
    | `minimal_consumption` | number (double) |  |
    | `minimal_consumption_logic` | string | <br>_Enum: `fixed`, `linear`_ |
    | `grace_coefficient` | string (decimal) |  |
    | `apply_as_minimal_consumption` | boolean |  |
    | `mark_unused_credit_as_spent_on_project_termination` | boolean |  |
    | `pay_earlier_invoices` | boolean | Also pay the cost of earlier, closed invoices of the project that no credit covered. Staff only. |
    | `earlier_invoices_from` | string (date) | First month of earlier invoices to pay, as its first day. Empty: from the first invoice. |
    | `earlier_invoices_until` | string (date) | Last month of earlier invoices to pay, as its first day. Empty: up to the last closed invoice. |
    | `earlier_invoices_compensate_in` | any | Which invoice a payment of an earlier invoice is written on: the current month's, or the paid month's own, which changes an invoice already issued. |


=== "Authorization"

    The `CUSTOMER.OWNER` role on the customer.
    
    A request acting as staff always meets the permission and role requirements.

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/project-credits/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.project_credits import project_credits_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = project_credits_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`project_credits_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/project_credits/project_credits_destroy.py)

=== "TypeScript"

    ```typescript
    import { projectCreditsDestroy } from 'waldur-js-client';
    
    try {
      const response = await projectCreditsDestroy({
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

    The `CUSTOMER.OWNER` role on the customer.
    
    A request acting as staff always meets the permission and role requirements.

---

## Other Actions


### Earlier invoices of the project and what credit paid of them

Per closed month of the project, the cost the credit could pay and how much of it credit paid, either on the month's own invoice or later. This is the cost a period-Total cost policy that takes credit into account keeps counting. Every closed month is listed; in_period marks those the credit pays, by its earlier_invoices_from / earlier_invoices_until, which can be previewed with other bounds.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/project-credits/a1b2c3d4-e5f6-7890-abcd-ef1234567890/earlier_invoices/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.project_credits import project_credits_earlier_invoices_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = project_credits_earlier_invoices_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`project_credits_earlier_invoices_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/project_credits/project_credits_earlier_invoices_retrieve.py)

=== "TypeScript"

    ```typescript
    import { projectCreditsEarlierInvoicesRetrieve } from 'waldur-js-client';
    
    try {
      const response = await projectCreditsEarlierInvoicesRetrieve({
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
    | `earlier_invoices_from` | string (date) | First month the credit pays, as its first day, to preview other bounds. Defaults to the credit's own. |
    | `earlier_invoices_until` | string (date) | Last month the credit pays, as its first day, to preview other bounds. Defaults to the credit's own. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `months` | array of objects |  |
    | `months.period` | string (date) | The month, as its first day. |
    | `months.cost` | string (decimal) | Cost the credit could pay: the project's items on offerings the credit covers, net of volume discounts, before tax. |
    | `months.covered` | string (decimal) | What paid for it: the credit compensation on the month's invoice, later payments of the month, and staff refunds of its items. |
    | `months.uncovered` | string (decimal) | Cost that nothing paid for yet. |
    | `months.in_period` | boolean | Whether the month is within the months the credit pays. |
    | `uncovered` | string (decimal) | Uncovered cost of every month listed: what a period-Total cost policy that takes credit into account counts of them. |
    | `uncovered_in_period` | string (decimal) | Uncovered cost of the months the credit pays. |
    | `payable_now` | string (decimal) | What the allocation would pay now: the uncovered cost of the months it pays, capped by what is left of the allocation and of the organization credit after this month's usage so far. |


=== "Authorization"

    Who may see a project's costs month by month: whoever sees the organization's accounting (staff, support, owners, CUSTOMER.VIEW_ACCOUNTING), and the project's own roles while the organization displays billing info in projects, as they then see the project's invoice items (`filter_project_invoice_items`).

---

### Pay earlier invoices from the project credit

Pays the uncovered cost of the project's earlier, closed invoices from what is left of the credit after this month's usage so far, and turns on pay_earlier_invoices so that each month end pays more. With dry_run, returns the compensations it would write and the balances before and after, and changes nothing.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/project-credits/a1b2c3d4-e5f6-7890-abcd-ef1234567890/pay_earlier_invoices/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.pay_earlier_invoices_request_request import PayEarlierInvoicesRequestRequest # (1)
    from waldur_api_client.api.project_credits import project_credits_pay_earlier_invoices # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PayEarlierInvoicesRequestRequest()
    response = project_credits_pay_earlier_invoices.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PayEarlierInvoicesRequestRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/pay_earlier_invoices_request_request.py)
    2.  **API Source:** [`project_credits_pay_earlier_invoices`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/project_credits/project_credits_pay_earlier_invoices.py)

=== "TypeScript"

    ```typescript
    import { projectCreditsPayEarlierInvoices } from 'waldur-js-client';
    
    try {
      const response = await projectCreditsPayEarlierInvoices({
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
    | `dry_run` | boolean |  | Return what would be written without writing anything.<br>_Constraints: default: `False`_ |
    | `compensate_in` | any |  | Which invoice the compensations go on. Defaults to the credit's earlier_invoices_compensate_in; a payment that is not a dry run also stores it there. |
    | `earlier_invoices_from` | string (date) |  | First month to pay, as its first day. Defaults to the credit's own; a payment that is not a dry run also stores it. |
    | `earlier_invoices_until` | string (date) |  | Last month to pay, as its first day. Defaults to the credit's own; a payment that is not a dry run also stores it. |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `dry_run` | boolean |  |
    | `compensate_in` | string | <br>_Enum: `current_month`, `incurred_month`_ |
    | `payments` | array of objects |  |
    | `payments.period` | string (date) | The month the compensation pays. |
    | `payments.invoice_period` | string (date) | The month of the invoice the compensation is written on. |
    | `payments.invoice_uuid` | string (uuid) | That invoice; null in a dry run while the current month has no invoice yet. |
    | `payments.resource_name` | string |  |
    | `payments.resource_uuid` | string (uuid) |  |
    | `payments.item_name` | string | The cost item the compensation pays. |
    | `payments.amount` | string (decimal) |  |
    | `total` | string (decimal) |  |
    | `project_credit_before` | string (decimal) |  |
    | `project_credit_after` | string (decimal) |  |
    | `customer_credit_before` | string (decimal) |  |
    | `customer_credit_after` | string (decimal) |  |


=== "Authorization"

    Staff only.

---
