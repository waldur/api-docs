# Marketplace Script Dry Run

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-script-dry-run/{uuid}/async_run/` | [Async run](#async-run) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-script-dry-run/{uuid}/run/` | [Run](#run) |

---

### Async run


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-script-dry-run/a1b2c3d4-e5f6-7890-abcd-ef1234567890/async_run/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.dry_run_request import DryRunRequest # (1)
    from waldur_api_client.api.marketplace_script_dry_run import marketplace_script_dry_run_async_run # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = DryRunRequest()
    response = marketplace_script_dry_run_async_run.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`DryRunRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/dry_run_request.py)
    2.  **API Source:** [`marketplace_script_dry_run_async_run`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_script_dry_run/marketplace_script_dry_run_async_run.py)

=== "TypeScript"

    ```typescript
    import { marketplaceScriptDryRunAsyncRun } from 'waldur-js-client';
    
    try {
      const response = await marketplaceScriptDryRunAsyncRun({
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

    | Field | Type | Required |
    |---|---|---|
    | `plan` | string (uri) |  |
    | `type` | any |  |
    | `attributes` | object (free-form) |  |
    | `order_offering` | string (uri) |  |


=== "Responses"

    **`202`** - 
    
    | Field | Type |
    |---|---|
    | `uuid` | string (uuid) |

---

### Run


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-script-dry-run/a1b2c3d4-e5f6-7890-abcd-ef1234567890/run/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.dry_run_request import DryRunRequest # (1)
    from waldur_api_client.api.marketplace_script_dry_run import marketplace_script_dry_run_run # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = DryRunRequest()
    response = marketplace_script_dry_run_run.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`DryRunRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/dry_run_request.py)
    2.  **API Source:** [`marketplace_script_dry_run_run`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_script_dry_run/marketplace_script_dry_run_run.py)

=== "TypeScript"

    ```typescript
    import { marketplaceScriptDryRunRun } from 'waldur-js-client';
    
    try {
      const response = await marketplaceScriptDryRunRun({
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

    | Field | Type | Required |
    |---|---|---|
    | `plan` | string (uri) |  |
    | `type` | any |  |
    | `attributes` | object (free-form) |  |
    | `order_offering` | string (uri) |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `output` | string |

---
