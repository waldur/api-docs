# Web Shell Ticket

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-post">POST</span> | `/api/web-shell-ticket/` | [Open a web shell session](#open-a-web-shell-session) |

---

### Open a web shell session

Returns a single-use link that opens `waldur shell` in the browser as the calling staff user. Only available when the deployment runs with DEBUG and WALDUR_CORE['WEB_SHELL_ENABLED'].


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/web-shell-ticket/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.web_shell_ticket import web_shell_ticket # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = web_shell_ticket.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`web_shell_ticket`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/web_shell_ticket/web_shell_ticket.py)

=== "TypeScript"

    ```typescript
    import { webShellTicket } from 'waldur-js-client';
    
    try {
      const response = await webShellTicket({
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
    | `url` | string | Single-use link that opens the web shell. Valid for one minute; the ticket is in the URL fragment. |

---
