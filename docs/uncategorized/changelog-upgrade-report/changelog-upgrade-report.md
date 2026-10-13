# Changelog Upgrade Report

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/changelog-upgrade-report/` | [Get upgrade report](#get-upgrade-report) |

---

### Get upgrade report

Returns a Markdown upgrade report, maintenance announcement text and upgrade commands covering every changelog entry pending for this deployment, regardless of any table filters or pagination.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/changelog-upgrade-report/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.changelog_upgrade_report import changelog_upgrade_report_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = changelog_upgrade_report_retrieve.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`changelog_upgrade_report_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/changelog_upgrade_report/changelog_upgrade_report_retrieve.py)

=== "TypeScript"

    ```typescript
    import { changelogUpgradeReportRetrieve } from 'waldur-js-client';
    
    try {
      const response = await changelogUpgradeReportRetrieve({
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
    | `current_version` | string |  |
    | `latest_version` | string |  |
    | `entry_count` | integer |  |
    | `commands` | object |  |
    | `commands.helm` | string |  |
    | `commands.docker_compose` | string |  |
    | `report` | string | Markdown upgrade report |
    | `announcement` | string | Markdown text for a maintenance announcement |
    | `announcement_type` | string | <br>_Enum: `information`, `warning`_ |

---
