# Affiliated Organizations

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/affiliated-organizations/` | [List Affiliated Organizations](#list-affiliated-organizations) |
| <span class="http-badge http-get">GET</span> | `/api/affiliated-organizations/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/affiliated-organizations/` | [Create](#create) |
| <span class="http-badge http-put">PUT</span> | `/api/affiliated-organizations/{uuid}/` | [Update](#update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/affiliated-organizations/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-delete">DELETE</span> | `/api/affiliated-organizations/{uuid}/` | [Delete](#delete) |
| **Other Actions** | | |
| <span class="http-badge http-get">GET</span> | `/api/affiliated-organizations/report/` | [Get affiliated organizations report](#get-affiliated-organizations-report) |
| <span class="http-badge http-get">GET</span> | `/api/affiliated-organizations/{uuid}/stats/` | [Get affiliated organization statistics](#get-affiliated-organization-statistics) |

---
## Core CRUD


### List Affiliated Organizations


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/affiliated-organizations/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.affiliated_organizations import affiliated_organizations_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = affiliated_organizations_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`affiliated_organizations_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/affiliated_organizations/affiliated_organizations_list.py)

=== "TypeScript"

    ```typescript
    import { affiliatedOrganizationsList } from 'waldur-js-client';
    
    try {
      const response = await affiliatedOrganizationsList({
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
    | `abbreviation` | string | Abbreviation |
    | `code` | string | Code |
    | `country` | string | Country |
    | `name` | string | Name |
    | `name_exact` | string | Name (exact) |
    | `o` | string | Which field to use when ordering the results. |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `query` | string | Search |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `name` | string |  |
    | `code` | string | Unique short identifier, e.g. CERN, EMBL. |
    | `abbreviation` | string |  |
    | `description` | string |  |
    | `email` | string (email) |  |
    | `homepage` | string (uri) |  |
    | `country` | string |  |
    | `address` | string |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `projects_count` | integer | Number of active projects affiliated with this organization |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/affiliated-organizations/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.affiliated_organizations import affiliated_organizations_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = affiliated_organizations_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`affiliated_organizations_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/affiliated_organizations/affiliated_organizations_retrieve.py)

=== "TypeScript"

    ```typescript
    import { affiliatedOrganizationsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await affiliatedOrganizationsRetrieve({
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
    | `name` | string |  |
    | `code` | string | Unique short identifier, e.g. CERN, EMBL. |
    | `abbreviation` | string |  |
    | `description` | string |  |
    | `email` | string (email) |  |
    | `homepage` | string (uri) |  |
    | `country` | string |  |
    | `address` | string |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `projects_count` | integer | Number of active projects affiliated with this organization |

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/affiliated-organizations/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-affiliated-organization" \
      code="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.affiliated_organization_request import AffiliatedOrganizationRequest # (1)
    from waldur_api_client.api.affiliated_organizations import affiliated_organizations_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = AffiliatedOrganizationRequest(
        name="my-awesome-affiliated-organization",
        code="string-value"
    )
    response = affiliated_organizations_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`AffiliatedOrganizationRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/affiliated_organization_request.py)
    2.  **API Source:** [`affiliated_organizations_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/affiliated_organizations/affiliated_organizations_create.py)

=== "TypeScript"

    ```typescript
    import { affiliatedOrganizationsCreate } from 'waldur-js-client';
    
    try {
      const response = await affiliatedOrganizationsCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "name": "my-awesome-affiliated-organization",
        "code": "string-value"
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
    | `code` | string | ✓ | Unique short identifier, e.g. CERN, EMBL. |
    | `abbreviation` | string |  |  |
    | `description` | string |  |  |
    | `email` | string (email) |  |  |
    | `homepage` | string (uri) |  |  |
    | `country` | string |  |  |
    | `address` | string |  |  |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `name` | string |  |
    | `code` | string | Unique short identifier, e.g. CERN, EMBL. |
    | `abbreviation` | string |  |
    | `description` | string |  |
    | `email` | string (email) |  |
    | `homepage` | string (uri) |  |
    | `country` | string |  |
    | `address` | string |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `projects_count` | integer | Number of active projects affiliated with this organization |

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/affiliated-organizations/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-affiliated-organization" \
      code="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.affiliated_organization_request import AffiliatedOrganizationRequest # (1)
    from waldur_api_client.api.affiliated_organizations import affiliated_organizations_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = AffiliatedOrganizationRequest(
        name="my-awesome-affiliated-organization",
        code="string-value"
    )
    response = affiliated_organizations_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`AffiliatedOrganizationRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/affiliated_organization_request.py)
    2.  **API Source:** [`affiliated_organizations_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/affiliated_organizations/affiliated_organizations_update.py)

=== "TypeScript"

    ```typescript
    import { affiliatedOrganizationsUpdate } from 'waldur-js-client';
    
    try {
      const response = await affiliatedOrganizationsUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "name": "my-awesome-affiliated-organization",
        "code": "string-value"
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
    | `code` | string | ✓ | Unique short identifier, e.g. CERN, EMBL. |
    | `abbreviation` | string |  |  |
    | `description` | string |  |  |
    | `email` | string (email) |  |  |
    | `homepage` | string (uri) |  |  |
    | `country` | string |  |  |
    | `address` | string |  |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `name` | string |  |
    | `code` | string | Unique short identifier, e.g. CERN, EMBL. |
    | `abbreviation` | string |  |
    | `description` | string |  |
    | `email` | string (email) |  |
    | `homepage` | string (uri) |  |
    | `country` | string |  |
    | `address` | string |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `projects_count` | integer | Number of active projects affiliated with this organization |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/affiliated-organizations/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_affiliated_organization_request import PatchedAffiliatedOrganizationRequest # (1)
    from waldur_api_client.api.affiliated_organizations import affiliated_organizations_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedAffiliatedOrganizationRequest()
    response = affiliated_organizations_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedAffiliatedOrganizationRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_affiliated_organization_request.py)
    2.  **API Source:** [`affiliated_organizations_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/affiliated_organizations/affiliated_organizations_partial_update.py)

=== "TypeScript"

    ```typescript
    import { affiliatedOrganizationsPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await affiliatedOrganizationsPartialUpdate({
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
    | `code` | string |  | Unique short identifier, e.g. CERN, EMBL. |
    | `abbreviation` | string |  |  |
    | `description` | string |  |  |
    | `email` | string (email) |  |  |
    | `homepage` | string (uri) |  |  |
    | `country` | string |  |  |
    | `address` | string |  |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `name` | string |  |
    | `code` | string | Unique short identifier, e.g. CERN, EMBL. |
    | `abbreviation` | string |  |
    | `description` | string |  |
    | `email` | string (email) |  |
    | `homepage` | string (uri) |  |
    | `country` | string |  |
    | `address` | string |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `projects_count` | integer | Number of active projects affiliated with this organization |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/affiliated-organizations/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.affiliated_organizations import affiliated_organizations_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = affiliated_organizations_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`affiliated_organizations_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/affiliated_organizations/affiliated_organizations_destroy.py)

=== "TypeScript"

    ```typescript
    import { affiliatedOrganizationsDestroy } from 'waldur-js-client';
    
    try {
      const response = await affiliatedOrganizationsDestroy({
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


### Get affiliated organizations report

Staff-only report showing aggregated data for all affiliated organizations plus an unaffiliated row.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/affiliated-organizations/report/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.affiliated_organizations import affiliated_organizations_report_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = affiliated_organizations_report_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`affiliated_organizations_report_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/affiliated_organizations/affiliated_organizations_report_list.py)

=== "TypeScript"

    ```typescript
    import { affiliatedOrganizationsReportList } from 'waldur-js-client';
    
    try {
      const response = await affiliatedOrganizationsReportList({
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
    | `abbreviation` | string | Abbreviation |
    | `code` | string | Code |
    | `country` | string | Country |
    | `name` | string | Name |
    | `name_exact` | string | Name (exact) |
    | `o` | string | Which field to use when ordering the results. |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `query` | string | Search |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `org_uuid` | string (uuid) |
    | `org_name` | string |
    | `org_abbreviation` | string |
    | `projects_count` | integer |
    | `resources_count` | integer |
    | `estimated_cost` | string (decimal) |

---

### Get affiliated organization statistics

Returns permission-filtered statistics for this affiliated organization.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/affiliated-organizations/a1b2c3d4-e5f6-7890-abcd-ef1234567890/stats/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.affiliated_organizations import affiliated_organizations_stats_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = affiliated_organizations_stats_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`affiliated_organizations_stats_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/affiliated_organizations/affiliated_organizations_stats_retrieve.py)

=== "TypeScript"

    ```typescript
    import { affiliatedOrganizationsStatsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await affiliatedOrganizationsStatsRetrieve({
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
    | `active_projects_count` | integer |
    | `resources_count` | integer |
    | `estimated_monthly_cost` | string (decimal) |

---
