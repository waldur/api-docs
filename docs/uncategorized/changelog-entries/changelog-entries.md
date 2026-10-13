# Changelog Entries

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| <span class="http-badge http-get">GET</span> | `/api/changelog-entries/` | [List changelog entries](#list-changelog-entries) |

---

### List changelog entries

Returns a flat, paginated list of changelog entries for all pending versions, or, with `release`, the entries that release introduced. Supports filtering by type, risk, scope, version, and text search. Compatible with the standard Waldur table component.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/changelog-entries/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.changelog_entry_list_category_enum import ChangelogEntryListCategoryEnum # (1)
    from waldur_api_client.models.changelog_entry_list_o_enum import ChangelogEntryListOEnum # (2)
    from waldur_api_client.models.changelog_entry_list_risk_enum import ChangelogEntryListRiskEnum # (3)
    from waldur_api_client.models.changelog_entry_list_scope_enum import ChangelogEntryListScopeEnum # (4)
    from waldur_api_client.models.changelog_entry_list_type_enum import ChangelogEntryListTypeEnum # (5)
    from waldur_api_client.api.changelog_entries import changelog_entries_retrieve # (6)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = changelog_entries_retrieve.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ChangelogEntryListCategoryEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/changelog_entry_list_category_enum.py)
    2.  **Model Source:** [`ChangelogEntryListOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/changelog_entry_list_o_enum.py)
    3.  **Model Source:** [`ChangelogEntryListRiskEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/changelog_entry_list_risk_enum.py)
    4.  **Model Source:** [`ChangelogEntryListScopeEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/changelog_entry_list_scope_enum.py)
    5.  **Model Source:** [`ChangelogEntryListTypeEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/changelog_entry_list_type_enum.py)
    6.  **API Source:** [`changelog_entries_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/changelog_entries/changelog_entries_retrieve.py)

=== "TypeScript"

    ```typescript
    import { changelogEntriesRetrieve } from 'waldur-js-client';
    
    try {
      const response = await changelogEntriesRetrieve({
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
    | `category` | string | Filter by category<br>_Enum: `ai_assistant`, `auth`, `identity`, `infrastructure`, `invoices`, `marketplace`, `notifications`, `openstack`, `policy`, `proposal`, `reporting`, `slurm`, `support`, `ui`_ |
    | `highlight` | boolean | Filter highlighted entries only |
    | `o` | string | Sort by a field; prefix with - to reverse. Type and risk sort most consequential first (breaking, high). Without it, relevant entries come first, then by risk.<br>_Enum: `-category`, `-risk`, `-title`, `-type`, `-version`, `category`, `risk`, `title`, `type`, `version`_ |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |
    | `release` | string | List what this release introduced instead of the pending entries |
    | `relevant_only` | boolean | Show only relevant entries |
    | `risk` | string | Filter by risk level<br>_Enum: `high`, `low`, `medium`, `none`_ |
    | `scope` | string | Filter by scope<br>_Enum: `core`, `dev`, `infra`, `plugin`_ |
    | `search` | string | Full-text search in title and description |
    | `type` | string | Filter by entry type<br>_Enum: `breaking`, `deprecation`, `feature`, `fix`, `improvement`, `security`_ |
    | `version` | string | Filter by release version |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `count` | integer |
    | `current_version` | string |
    | `latest_version` | string |
    | `versions_behind` | integer |
    | `results` | array of objects |
    | `results.id` | string |
    | `results.type` | string |
    | `results.category` | string |
    | `results.title` | string |
    | `results.description` | string |
    | `results.scope` | string |
    | `results.component` | array of strings |
    | `results.highlight` | boolean |
    | `results.impact` | object |
    | `results.impact.risk` | string |
    | `results.impact.affected_scope` | string |
    | `results.impact.affected_resources` | object (free-form) |
    | `results.impact.affected_users` | object (free-form) |
    | `results.security` | any |
    | `results.actions` | array of objects |
    | `results.actions.type` | string |
    | `results.actions.description` | string |
    | `results.actions.automatic` | boolean |
    | `results.actions.deadline` | string |
    | `results.relevant_when` | object |
    | `results.relevant_when.plugins` | array of strings |
    | `results.relevant_when.feature_flags` | array of strings |
    | `results.relevant_when.settings` | array of strings |
    | `results.relevant` | boolean |
    | `results.relevance_reasons` | array of strings |
    | `results.affected_resources_count` | integer |
    | `results.affected_users_count` | integer |
    | `results.settings_analysis` | object (free-form) |
    | `results.plugin_analysis` | object (free-form) |
    | `results.version` | string |
    | `results.release_date` | string |
    | `results.release_type` | string |

---
