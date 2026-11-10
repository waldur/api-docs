# Export Pdf

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-post">POST</span> | `/api/export-pdf/` | [Export a table or chart as PDF](#export-a-table-or-chart-as-pdf) |

---

### Export a table or chart as PDF

Renders the title with either a table (columns and rows of text) or a chart (a base64-encoded PNG) as a PDF. Nothing is read from the database: the PDF holds only what the request sends. A table may have at most 10000 rows, 100 columns, 50000 cells and 1000000 characters; an image at most 5 MB and 25000000 pixels.


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/export-pdf/ \
      Authorization:"Token YOUR_API_TOKEN" \
      title="string-value"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.export_pdf_request import ExportPdfRequest # (1)
    from waldur_api_client.api.export_pdf import export_pdf # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ExportPdfRequest(
        title="string-value"
    )
    response = export_pdf.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ExportPdfRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/export_pdf_request.py)
    2.  **API Source:** [`export_pdf`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/export_pdf/export_pdf.py)

=== "TypeScript"

    ```typescript
    import { exportPdf } from 'waldur-js-client';
    
    try {
      const response = await exportPdf({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "title": "string-value"
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
    | `title` | string | ✓ |  |
    | `columns` | array of strings |  | Header row of a table export. |
    | `rows` | array of arrays |  | Rows of a table export, each with one cell per column. |
    | `image` | string |  | Base64-encoded PNG of a chart export. |


=== "Responses"

    **`200`** - 
    


=== "Authorization"

    Any signed-in user.

---
