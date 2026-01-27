# Version

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/version/` | [Get application version](#get-application-version) |

---

### Get application version

Retrieves the current installed version of the application and the latest available version from GitHub (if available). Requires staff or support user permissions.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/version/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.version import version_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = version_retrieve.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`version_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/version/version_retrieve.py)

=== "TypeScript"

    ```typescript
    import { versionRetrieve } from 'waldur-js-client';
    
    try {
      const response = await versionRetrieve({
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
    | `version` | string | Current installed version of the application |
    | `latest_version` | string | Latest available version from GitHub, if available. |

---
