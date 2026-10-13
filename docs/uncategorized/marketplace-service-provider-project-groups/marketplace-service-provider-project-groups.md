# Marketplace Service Provider Project Groups

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-service-provider-project-groups/` | [List Marketplace Service Provider Project Groups](#list-marketplace-service-provider-project-groups) |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-service-provider-project-groups/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-service-provider-project-groups/` | [Adopt a POSIX project group with a given GID](#adopt-a-posix-project-group-with-a-given-gid) |
| **Other Actions** | | |
| <span class="http-badge http-get">GET</span> | `/api/marketplace-service-provider-project-groups/adoptable_projects/` | [Projects a group can be adopted for](#projects-a-group-can-be-adopted-for) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-service-provider-project-groups/import_groups/` | [Adopt several POSIX project groups at once](#adopt-several-posix-project-groups-at-once) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-service-provider-project-groups/{uuid}/set_gid/` | [Set the GID of a POSIX project group](#set-the-gid-of-a-posix-project-group) |

---
## Core CRUD


### List Marketplace Service Provider Project Groups


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-service-provider-project-groups/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.service_provider_project_group_o_enum import ServiceProviderProjectGroupOEnum # (1)
    from waldur_api_client.api.marketplace_service_provider_project_groups import marketplace_service_provider_project_groups_list # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_service_provider_project_groups_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`ServiceProviderProjectGroupOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/service_provider_project_group_o_enum.py)
    2.  **API Source:** [`marketplace_service_provider_project_groups_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_service_provider_project_groups/marketplace_service_provider_project_groups_list.py)

=== "TypeScript"

    ```typescript
    import { marketplaceServiceProviderProjectGroupsList } from 'waldur-js-client';
    
    try {
      const response = await marketplaceServiceProviderProjectGroupsList({
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
    | `created` | string (date-time) | Created after |
    | `created_before` | string (date-time) | Created before |
    | `customer_uuid` | string (uuid) | UUID of the project's organization |
    | `gid` | integer |  |
    | `in_use` | boolean | In use |
    | `modified` | string (date-time) | Modified after |
    | `modified_before` | string (date-time) | Modified before |
    | `name` | string |  |
    | `o` | array | Ordering<br><br> |
    | `offering_uuid` | string (uuid) | Groups of projects with a non-terminated resource on this offering |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `project_uuid` | string (uuid) | Project UUID |
    | `provider_offering_uuid` | string (uuid) | Every group of the service provider that owns this offering |
    | `query` | string | Search by group name, project name or slug, organization name or GID |
    | `service_provider_uuid` | string (uuid) | Service provider UUID |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `gid` | integer |  |
    | `in_use` | boolean | The project has a non-terminated resource on an offering of the provider. An unused group keeps its GID. |
    | `service_provider_uuid` | string (uuid) |  |
    | `service_provider_name` | string |  |
    | `project_uuid` | string (uuid) |  |
    | `project_name` | string |  |
    | `project_slug` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `customer_slug` | string |  |
    | `offerings` | array of objects | The provider's offerings where the project has a non-terminated resource. |
    | `offerings.uuid` | string |  |
    | `offerings.name` | string |  |
    | `members` | array of strings | Sorted usernames of the live accounts at the provider of the users holding an active role in the project. |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-service-provider-project-groups/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_service_provider_project_groups import marketplace_service_provider_project_groups_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_service_provider_project_groups_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`marketplace_service_provider_project_groups_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_service_provider_project_groups/marketplace_service_provider_project_groups_retrieve.py)

=== "TypeScript"

    ```typescript
    import { marketplaceServiceProviderProjectGroupsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await marketplaceServiceProviderProjectGroupsRetrieve({
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
    | `name` | string |  |
    | `gid` | integer |  |
    | `in_use` | boolean | The project has a non-terminated resource on an offering of the provider. An unused group keeps its GID. |
    | `service_provider_uuid` | string (uuid) |  |
    | `service_provider_name` | string |  |
    | `project_uuid` | string (uuid) |  |
    | `project_name` | string |  |
    | `project_slug` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `customer_slug` | string |  |
    | `offerings` | array of objects | The provider's offerings where the project has a non-terminated resource. |
    | `offerings.uuid` | string |  |
    | `offerings.name` | string |  |
    | `members` | array of strings | Sorted usernames of the live accounts at the provider of the users holding an active role in the project. |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Adopt a POSIX project group with a given GID

Create the service provider's group for a project, pinned to a GID the directory already uses. Works for a project that has no resource at the provider yet; the allocator never hands the GID out afterwards. Refused with 400 when the project already has a group (use set_gid), when another consumer in the provider's pools holds the GID, or when the GID is outside the range project groups draw from and allow_outside_range is not set.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-service-provider-project-groups/ \
      Authorization:"Token YOUR_API_TOKEN" \
      project="string-value" \
      gid=123 \
      service_provider="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.service_provider_project_group_create_request import ServiceProviderProjectGroupCreateRequest # (1)
    from waldur_api_client.api.marketplace_service_provider_project_groups import marketplace_service_provider_project_groups_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ServiceProviderProjectGroupCreateRequest(
        project="string-value",
        gid=123,
        service_provider="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    response = marketplace_service_provider_project_groups_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ServiceProviderProjectGroupCreateRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/service_provider_project_group_create_request.py)
    2.  **API Source:** [`marketplace_service_provider_project_groups_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_service_provider_project_groups/marketplace_service_provider_project_groups_create.py)

=== "TypeScript"

    ```typescript
    import { marketplaceServiceProviderProjectGroupsCreate } from 'waldur-js-client';
    
    try {
      const response = await marketplaceServiceProviderProjectGroupsCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "project": "string-value",
        "gid": 123,
        "service_provider": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
    | `project` | string | ✓ | Project UUID, or its slug when exactly one project with that slug has a resource or order at the service provider. |
    | `gid` | integer (int64) | ✓ |  |
    | `name` | string |  | Group name, matching ^[a-z_][a-z0-9_-]{0,31}$; derived from the project slug when omitted. |
    | `service_provider` | string (uuid) | ✓ |  |
    | `allow_outside_range` | boolean |  | Accept a GID outside the range project groups draw from, e.g. one a directory assigned before Waldur managed it.<br>_Constraints: default: `False`_ |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `gid` | integer |  |
    | `in_use` | boolean | The project has a non-terminated resource on an offering of the provider. An unused group keeps its GID. |
    | `service_provider_uuid` | string (uuid) |  |
    | `service_provider_name` | string |  |
    | `project_uuid` | string (uuid) |  |
    | `project_name` | string |  |
    | `project_slug` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `customer_slug` | string |  |
    | `offerings` | array of objects | The provider's offerings where the project has a non-terminated resource. |
    | `offerings.uuid` | string |  |
    | `offerings.name` | string |  |
    | `members` | array of strings | Sorted usernames of the live accounts at the provider of the users holding an active role in the project. |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

## Other Actions


### Projects a group can be adopted for

Projects with a resource or an order, in any state, on an offering of the service provider: the projects its owners may adopt a group for. Staff may adopt for any project. Filter by name, slug or organization name with query.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/marketplace-service-provider-project-groups/adoptable_projects/ \
      Authorization:"Token YOUR_API_TOKEN" \
      service_provider_uuid=="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.marketplace_service_provider_project_groups import marketplace_service_provider_project_groups_adoptable_projects_list # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = marketplace_service_provider_project_groups_adoptable_projects_list.sync(
        client=client,
        service_provider_uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **API Source:** [`marketplace_service_provider_project_groups_adoptable_projects_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_service_provider_project_groups/marketplace_service_provider_project_groups_adoptable_projects_list.py)

=== "TypeScript"

    ```typescript
    import { marketplaceServiceProviderProjectGroupsAdoptableProjectsList } from 'waldur-js-client';
    
    try {
      const response = await marketplaceServiceProviderProjectGroupsAdoptableProjectsList({
      auth: "Token YOUR_API_TOKEN",
      query: {
        "service_provider_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Query Parameters"

    | Name | Type | Required | Description |
    |---|---|---|---|
    | `page` | integer |  | A page number within the paginated result set. |
    | `page_size` | integer |  | Number of results to return per page. |
    | `query` | string |  |  |
    | `service_provider_uuid` | string | ✓ |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `slug` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `group_name` | string | The project's group at the provider, if it has one. |

---

### Adopt several POSIX project groups at once

Pin the groups of several projects in one step, e.g. the groups a directory held before Waldur managed it. A project without a group gets one; a project with a group has its GID set. All or nothing: any refused entry leaves every group unchanged.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-service-provider-project-groups/import_groups/ \
      Authorization:"Token YOUR_API_TOKEN" \
      service_provider="a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
      groups:='[]'
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.service_provider_project_group_import_request import ServiceProviderProjectGroupImportRequest # (1)
    from waldur_api_client.models.service_provider_project_group_o_enum import ServiceProviderProjectGroupOEnum # (2)
    from waldur_api_client.api.marketplace_service_provider_project_groups import marketplace_service_provider_project_groups_import_groups # (3)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ServiceProviderProjectGroupImportRequest(
        service_provider="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        groups=[]
    )
    response = marketplace_service_provider_project_groups_import_groups.sync(
        client=client,
        body=body_data
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`ServiceProviderProjectGroupImportRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/service_provider_project_group_import_request.py)
    2.  **Model Source:** [`ServiceProviderProjectGroupOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/service_provider_project_group_o_enum.py)
    3.  **API Source:** [`marketplace_service_provider_project_groups_import_groups`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_service_provider_project_groups/marketplace_service_provider_project_groups_import_groups.py)

=== "TypeScript"

    ```typescript
    import { marketplaceServiceProviderProjectGroupsImportGroups } from 'waldur-js-client';
    
    try {
      const response = await marketplaceServiceProviderProjectGroupsImportGroups({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "service_provider": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "groups": []
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Query Parameters"

    | Name | Type | Description |
    |---|---|---|
    | `created` | string (date-time) | Created after |
    | `created_before` | string (date-time) | Created before |
    | `customer_uuid` | string (uuid) | UUID of the project's organization |
    | `gid` | integer |  |
    | `in_use` | boolean | In use |
    | `modified` | string (date-time) | Modified after |
    | `modified_before` | string (date-time) | Modified before |
    | `name` | string |  |
    | `o` | array | Ordering<br><br> |
    | `offering_uuid` | string (uuid) | Groups of projects with a non-terminated resource on this offering |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `project_uuid` | string (uuid) | Project UUID |
    | `provider_offering_uuid` | string (uuid) | Every group of the service provider that owns this offering |
    | `query` | string | Search by group name, project name or slug, organization name or GID |
    | `service_provider_uuid` | string (uuid) | Service provider UUID |


=== "Request Body (required)"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `service_provider` | string (uuid) | ✓ |  |
    | `groups` | array of objects | ✓ |  |
    | `groups.project` | string | ✓ | Project UUID, or its slug when exactly one project with that slug has a resource or order at the service provider. |
    | `groups.gid` | integer (int64) | ✓ |  |
    | `groups.name` | string |  | Group name, matching ^[a-z_][a-z0-9_-]{0,31}$; derived from the project slug when omitted. |
    | `allow_outside_range` | boolean |  | Accept a GID outside the range project groups draw from, e.g. one a directory assigned before Waldur managed it.<br>_Constraints: default: `False`_ |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `gid` | integer |  |
    | `in_use` | boolean | The project has a non-terminated resource on an offering of the provider. An unused group keeps its GID. |
    | `service_provider_uuid` | string (uuid) |  |
    | `service_provider_name` | string |  |
    | `project_uuid` | string (uuid) |  |
    | `project_name` | string |  |
    | `project_slug` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `customer_slug` | string |  |
    | `offerings` | array of objects | The provider's offerings where the project has a non-terminated resource. |
    | `offerings.uuid` | string |  |
    | `offerings.name` | string |  |
    | `members` | array of strings | Sorted usernames of the live accounts at the provider of the users holding an active role in the project. |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---

### Set the GID of a POSIX project group

Move the group to another GID, e.g. one assigned outside Waldur. The previous GID is released but never handed out again automatically, since files may still carry it; renumbering them is the operator's job. Refused with 400 on the same conditions as adopting a group. Recorded as an event with both GIDs.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-service-provider-project-groups/a1b2c3d4-e5f6-7890-abcd-ef1234567890/set_gid/ \
      Authorization:"Token YOUR_API_TOKEN" \
      gid=123
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.project_group_gid_request import ProjectGroupGidRequest # (1)
    from waldur_api_client.api.marketplace_service_provider_project_groups import marketplace_service_provider_project_groups_set_gid # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ProjectGroupGidRequest(
        gid=123
    )
    response = marketplace_service_provider_project_groups_set_gid.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ProjectGroupGidRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/project_group_gid_request.py)
    2.  **API Source:** [`marketplace_service_provider_project_groups_set_gid`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_service_provider_project_groups/marketplace_service_provider_project_groups_set_gid.py)

=== "TypeScript"

    ```typescript
    import { marketplaceServiceProviderProjectGroupsSetGid } from 'waldur-js-client';
    
    try {
      const response = await marketplaceServiceProviderProjectGroupsSetGid({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "gid": 123
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
    | `gid` | integer (int64) | ✓ |  |
    | `allow_outside_range` | boolean |  | Accept a GID outside the range project groups draw from, e.g. one a directory assigned before Waldur managed it.<br>_Constraints: default: `False`_ |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string |  |
    | `gid` | integer |  |
    | `in_use` | boolean | The project has a non-terminated resource on an offering of the provider. An unused group keeps its GID. |
    | `service_provider_uuid` | string (uuid) |  |
    | `service_provider_name` | string |  |
    | `project_uuid` | string (uuid) |  |
    | `project_name` | string |  |
    | `project_slug` | string |  |
    | `customer_uuid` | string (uuid) |  |
    | `customer_name` | string |  |
    | `customer_slug` | string |  |
    | `offerings` | array of objects | The provider's offerings where the project has a non-terminated resource. |
    | `offerings.uuid` | string |  |
    | `offerings.name` | string |  |
    | `members` | array of strings | Sorted usernames of the live accounts at the provider of the users holding an active role in the project. |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |

---
