# Rancher Role Templates

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/rancher-role-templates/` | [List Rancher Role Templates](#list-rancher-role-templates) |
| <span class="http-badge http-get">GET</span> | `/api/rancher-role-templates/{uuid}/` | [Retrieve](#retrieve) |

---

### List Rancher Role Templates


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/rancher-role-templates/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.role_template_o_enum import RoleTemplateOEnum # (1)
    from waldur_api_client.api.rancher_role_templates import rancher_role_templates_list # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = rancher_role_templates_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`RoleTemplateOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/role_template_o_enum.py)
    2.  **API Source:** [`rancher_role_templates_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/rancher_role_templates/rancher_role_templates_list.py)

=== "TypeScript"

    ```typescript
    import { rancherRoleTemplatesList } from 'waldur-js-client';
    
    try {
      const response = await rancherRoleTemplatesList({
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
    | `scope_type` | string |  |
    | `settings_uuid` | string (uuid) |  |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `url` | string (uri) |  |
    | `uuid` | string (uuid) |  |
    | `name` | string | Role internal name |
    | `scope_type` | any |  |
    | `display_name` | string | Role public name |
    | `settings` | string (uri) |  |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/rancher-role-templates/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.rancher_role_templates import rancher_role_templates_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = rancher_role_templates_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`rancher_role_templates_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/rancher_role_templates/rancher_role_templates_retrieve.py)

=== "TypeScript"

    ```typescript
    import { rancherRoleTemplatesRetrieve } from 'waldur-js-client';
    
    try {
      const response = await rancherRoleTemplatesRetrieve({
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
    | `name` | string | Role internal name |
    | `scope_type` | any |  |
    | `display_name` | string | Role public name |
    | `settings` | string (uri) |  |

---
