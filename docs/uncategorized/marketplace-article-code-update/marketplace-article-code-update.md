# Marketplace Article Code Update

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-article-code-update/apply/` | [Apply article code replacements](#apply-article-code-replacements) |
| <span class="http-badge http-post">POST</span> | `/api/marketplace-article-code-update/preview/` | [Preview article code replacements](#preview-article-code-replacements) |

---

### Apply article code replacements


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-article-code-update/apply/ \
      Authorization:"Token YOUR_API_TOKEN" \
      search="string-value" \
      component_uuids:='[]'
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.article_code_update_apply_request import ArticleCodeUpdateApplyRequest # (1)
    from waldur_api_client.api.marketplace_article_code_update import marketplace_article_code_update_apply # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ArticleCodeUpdateApplyRequest(
        search="string-value",
        component_uuids=[]
    )
    response = marketplace_article_code_update_apply.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ArticleCodeUpdateApplyRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/article_code_update_apply_request.py)
    2.  **API Source:** [`marketplace_article_code_update_apply`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_article_code_update/marketplace_article_code_update_apply.py)

=== "TypeScript"

    ```typescript
    import { marketplaceArticleCodeUpdateApply } from 'waldur-js-client';
    
    try {
      const response = await marketplaceArticleCodeUpdateApply({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "search": "string-value",
        "component_uuids": []
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
    | `search` | string | ✓ | Substring to search for in article codes. |
    | `replace` | string |  | Replacement string.<br>_Constraints: default: ``_ |
    | `offering_category_uuid` | string (uuid) |  | Filter by offering category UUID. |
    | `offering_customer_uuid` | string (uuid) |  | Filter by service provider (customer) UUID. |
    | `offering_state` | any |  | Filter by offering state. |
    | `offering_name` | string |  | Filter by offering name (case-insensitive substring match). |
    | `component_uuids` | array of string (uuid)s | ✓ | UUIDs of components to update (from preview results). |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `updated_count` | integer |

---

### Preview article code replacements


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/marketplace-article-code-update/preview/ \
      Authorization:"Token YOUR_API_TOKEN" \
      search="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.article_code_update_preview_request import ArticleCodeUpdatePreviewRequest # (1)
    from waldur_api_client.api.marketplace_article_code_update import marketplace_article_code_update_preview # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ArticleCodeUpdatePreviewRequest(
        search="string-value"
    )
    response = marketplace_article_code_update_preview.sync(
        client=client,
        body=body_data
    )
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`ArticleCodeUpdatePreviewRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/article_code_update_preview_request.py)
    2.  **API Source:** [`marketplace_article_code_update_preview`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/marketplace_article_code_update/marketplace_article_code_update_preview.py)

=== "TypeScript"

    ```typescript
    import { marketplaceArticleCodeUpdatePreview } from 'waldur-js-client';
    
    try {
      const response = await marketplaceArticleCodeUpdatePreview({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "search": "string-value"
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
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |


=== "Request Body (required)"

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `search` | string | ✓ | Substring to search for in article codes. |
    | `replace` | string |  | Replacement string.<br>_Constraints: default: ``_ |
    | `offering_category_uuid` | string (uuid) |  | Filter by offering category UUID. |
    | `offering_customer_uuid` | string (uuid) |  | Filter by service provider (customer) UUID. |
    | `offering_state` | any |  | Filter by offering state. |
    | `offering_name` | string |  | Filter by offering name (case-insensitive substring match). |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `component_uuid` | string (uuid) |
    | `component_type` | string |
    | `component_name` | string |
    | `offering_uuid` | string (uuid) |
    | `offering_name` | string |
    | `offering_customer_name` | string |
    | `old_article_code` | string |
    | `new_article_code` | string |

---
