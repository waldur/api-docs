# Changelog

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/changelog/{version}/` | [Get changelog for a specific version](#get-changelog-for-a-specific-version) |
| **Other Actions** | | |
| <span class="http-badge http-get">GET</span> | `/api/changelog/compare/{from_version}/{to_version}/` | [Compare changelog between two versions](#compare-changelog-between-two-versions) |
| <span class="http-badge http-get">GET</span> | `/api/changelog/{version}/delta/` | [Get changelog delta for a version](#get-changelog-delta-for-a-version) |
| <span class="http-badge http-get">GET</span> | `/api/changelog/pending/` | [Get pending changelog](#get-pending-changelog) |
| <span class="http-badge http-get">GET</span> | `/api/changelog/releases/` | [List changelog releases](#list-changelog-releases) |

---
## Core CRUD


### Get changelog for a specific version

Returns the full changelog for a specific release version.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/changelog/string-value/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.changelog import changelog_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = changelog_retrieve.sync(
        version="string-value",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`changelog_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/changelog/changelog_retrieve.py)

=== "TypeScript"

    ```typescript
    import { changelogRetrieve } from 'waldur-js-client';
    
    try {
      const response = await changelogRetrieve({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "version": "string-value"
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
    | `version` | string | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `version` | string |
    | `date` | string |
    | `type` | string |
    | `summary` | string |
    | `entries` | array of objects |
    | `entries.id` | string |
    | `entries.type` | string |
    | `entries.category` | string |
    | `entries.title` | string |
    | `entries.description` | string |
    | `entries.scope` | string |
    | `entries.component` | array of strings |
    | `entries.highlight` | boolean |
    | `entries.impact` | object |
    | `entries.impact.risk` | string |
    | `entries.impact.affected_scope` | string |
    | `entries.impact.affected_resources` | object (free-form) |
    | `entries.impact.affected_users` | object (free-form) |
    | `entries.security` | any |
    | `entries.actions` | array of objects |
    | `entries.actions.type` | string |
    | `entries.actions.description` | string |
    | `entries.actions.automatic` | boolean |
    | `entries.actions.deadline` | string |
    | `entries.relevant_when` | object |
    | `entries.relevant_when.plugins` | array of strings |
    | `entries.relevant_when.feature_flags` | array of strings |
    | `entries.relevant_when.settings` | array of strings |
    | `entries.relevant` | boolean |
    | `entries.relevance_reasons` | array of strings |
    | `entries.affected_resources_count` | integer |
    | `entries.affected_users_count` | integer |
    | `entries.settings_analysis` | object (free-form) |
    | `entries.plugin_analysis` | object (free-form) |
    | `since_previous` | array of objects |
    | `since_previous.id` | string |
    | `since_previous.type` | string |
    | `since_previous.category` | string |
    | `since_previous.title` | string |
    | `since_previous.description` | string |
    | `since_previous.scope` | string |
    | `since_previous.component` | array of strings |
    | `since_previous.highlight` | boolean |
    | `since_previous.impact` | object |
    | `since_previous.impact.risk` | string |
    | `since_previous.impact.affected_scope` | string |
    | `since_previous.impact.affected_resources` | object (free-form) |
    | `since_previous.impact.affected_users` | object (free-form) |
    | `since_previous.security` | any |
    | `since_previous.actions` | array of objects |
    | `since_previous.actions.type` | string |
    | `since_previous.actions.description` | string |
    | `since_previous.actions.automatic` | boolean |
    | `since_previous.actions.deadline` | string |
    | `since_previous.relevant_when` | object |
    | `since_previous.relevant_when.plugins` | array of strings |
    | `since_previous.relevant_when.feature_flags` | array of strings |
    | `since_previous.relevant_when.settings` | array of strings |
    | `since_previous.relevant` | boolean |
    | `since_previous.relevance_reasons` | array of strings |
    | `since_previous.affected_resources_count` | integer |
    | `since_previous.affected_users_count` | integer |
    | `since_previous.settings_analysis` | object (free-form) |
    | `since_previous.plugin_analysis` | object (free-form) |
    | `component_activity` | object (free-form) |

---

## Other Actions


### Compare changelog between two versions

Returns merged delta entries between two arbitrary versions. Useful for seeing what changed between e.g. rc.5 and rc.12.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/changelog/compare/string-value/string-value/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.changelog import changelog_compare_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = changelog_compare_retrieve.sync(
        from_version="string-value",
        to_version="string-value",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`changelog_compare_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/changelog/changelog_compare_retrieve.py)

=== "TypeScript"

    ```typescript
    import { changelogCompareRetrieve } from 'waldur-js-client';
    
    try {
      const response = await changelogCompareRetrieve({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "from_version": "string-value",
        "to_version": "string-value"
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
    | `from_version` | string | ✓ |
    | `to_version` | string | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `current_version` | string |
    | `latest_version` | string |
    | `versions_behind` | integer |
    | `impact_analysis_status` | string |
    | `impact_analysis_computed_at` | string (date-time) |
    | `releases` | array of objects |
    | `releases.version` | string |
    | `releases.date` | string |
    | `releases.type` | string |
    | `releases.summary` | string |
    | `releases.entries` | array of objects |
    | `releases.entries.id` | string |
    | `releases.entries.type` | string |
    | `releases.entries.category` | string |
    | `releases.entries.title` | string |
    | `releases.entries.description` | string |
    | `releases.entries.scope` | string |
    | `releases.entries.component` | array of strings |
    | `releases.entries.highlight` | boolean |
    | `releases.entries.impact` | object |
    | `releases.entries.impact.risk` | string |
    | `releases.entries.impact.affected_scope` | string |
    | `releases.entries.impact.affected_resources` | object (free-form) |
    | `releases.entries.impact.affected_users` | object (free-form) |
    | `releases.entries.security` | any |
    | `releases.entries.actions` | array of objects |
    | `releases.entries.actions.type` | string |
    | `releases.entries.actions.description` | string |
    | `releases.entries.actions.automatic` | boolean |
    | `releases.entries.actions.deadline` | string |
    | `releases.entries.relevant_when` | object |
    | `releases.entries.relevant_when.plugins` | array of strings |
    | `releases.entries.relevant_when.feature_flags` | array of strings |
    | `releases.entries.relevant_when.settings` | array of strings |
    | `releases.entries.relevant` | boolean |
    | `releases.entries.relevance_reasons` | array of strings |
    | `releases.entries.affected_resources_count` | integer |
    | `releases.entries.affected_users_count` | integer |
    | `releases.entries.settings_analysis` | object (free-form) |
    | `releases.entries.plugin_analysis` | object (free-form) |
    | `releases.since_previous` | array of objects |
    | `releases.since_previous.id` | string |
    | `releases.since_previous.type` | string |
    | `releases.since_previous.category` | string |
    | `releases.since_previous.title` | string |
    | `releases.since_previous.description` | string |
    | `releases.since_previous.scope` | string |
    | `releases.since_previous.component` | array of strings |
    | `releases.since_previous.highlight` | boolean |
    | `releases.since_previous.impact` | object |
    | `releases.since_previous.impact.risk` | string |
    | `releases.since_previous.impact.affected_scope` | string |
    | `releases.since_previous.impact.affected_resources` | object (free-form) |
    | `releases.since_previous.impact.affected_users` | object (free-form) |
    | `releases.since_previous.security` | any |
    | `releases.since_previous.actions` | array of objects |
    | `releases.since_previous.actions.type` | string |
    | `releases.since_previous.actions.description` | string |
    | `releases.since_previous.actions.automatic` | boolean |
    | `releases.since_previous.actions.deadline` | string |
    | `releases.since_previous.relevant_when` | object |
    | `releases.since_previous.relevant_when.plugins` | array of strings |
    | `releases.since_previous.relevant_when.feature_flags` | array of strings |
    | `releases.since_previous.relevant_when.settings` | array of strings |
    | `releases.since_previous.relevant` | boolean |
    | `releases.since_previous.relevance_reasons` | array of strings |
    | `releases.since_previous.affected_resources_count` | integer |
    | `releases.since_previous.affected_users_count` | integer |
    | `releases.since_previous.settings_analysis` | object (free-form) |
    | `releases.since_previous.plugin_analysis` | object (free-form) |
    | `releases.component_activity` | object (free-form) |

---

### Get changelog delta for a version

Returns only the incremental changes since the previous version (since_previous entries).


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/changelog/string-value/delta/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.changelog import changelog_delta_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = changelog_delta_retrieve.sync(
        version="string-value",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`changelog_delta_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/changelog/changelog_delta_retrieve.py)

=== "TypeScript"

    ```typescript
    import { changelogDeltaRetrieve } from 'waldur-js-client';
    
    try {
      const response = await changelogDeltaRetrieve({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "version": "string-value"
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
    | `version` | string | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `version` | string |
    | `date` | string |
    | `type` | string |
    | `summary` | string |
    | `entries` | array of objects |
    | `entries.id` | string |
    | `entries.type` | string |
    | `entries.category` | string |
    | `entries.title` | string |
    | `entries.description` | string |
    | `entries.scope` | string |
    | `entries.component` | array of strings |
    | `entries.highlight` | boolean |
    | `entries.impact` | object |
    | `entries.impact.risk` | string |
    | `entries.impact.affected_scope` | string |
    | `entries.impact.affected_resources` | object (free-form) |
    | `entries.impact.affected_users` | object (free-form) |
    | `entries.security` | any |
    | `entries.actions` | array of objects |
    | `entries.actions.type` | string |
    | `entries.actions.description` | string |
    | `entries.actions.automatic` | boolean |
    | `entries.actions.deadline` | string |
    | `entries.relevant_when` | object |
    | `entries.relevant_when.plugins` | array of strings |
    | `entries.relevant_when.feature_flags` | array of strings |
    | `entries.relevant_when.settings` | array of strings |
    | `entries.relevant` | boolean |
    | `entries.relevance_reasons` | array of strings |
    | `entries.affected_resources_count` | integer |
    | `entries.affected_users_count` | integer |
    | `entries.settings_analysis` | object (free-form) |
    | `entries.plugin_analysis` | object (free-form) |
    | `since_previous` | array of objects |
    | `since_previous.id` | string |
    | `since_previous.type` | string |
    | `since_previous.category` | string |
    | `since_previous.title` | string |
    | `since_previous.description` | string |
    | `since_previous.scope` | string |
    | `since_previous.component` | array of strings |
    | `since_previous.highlight` | boolean |
    | `since_previous.impact` | object |
    | `since_previous.impact.risk` | string |
    | `since_previous.impact.affected_scope` | string |
    | `since_previous.impact.affected_resources` | object (free-form) |
    | `since_previous.impact.affected_users` | object (free-form) |
    | `since_previous.security` | any |
    | `since_previous.actions` | array of objects |
    | `since_previous.actions.type` | string |
    | `since_previous.actions.description` | string |
    | `since_previous.actions.automatic` | boolean |
    | `since_previous.actions.deadline` | string |
    | `since_previous.relevant_when` | object |
    | `since_previous.relevant_when.plugins` | array of strings |
    | `since_previous.relevant_when.feature_flags` | array of strings |
    | `since_previous.relevant_when.settings` | array of strings |
    | `since_previous.relevant` | boolean |
    | `since_previous.relevance_reasons` | array of strings |
    | `since_previous.affected_resources_count` | integer |
    | `since_previous.affected_users_count` | integer |
    | `since_previous.settings_analysis` | object (free-form) |
    | `since_previous.plugin_analysis` | object (free-form) |
    | `component_activity` | object (free-form) |

---

### Get pending changelog

Returns the changelog entries this deployment has not seen yet, grouped by each newer version, with relevance matching and impact analysis results.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/changelog/pending/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.changelog import changelog_pending_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = changelog_pending_retrieve.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`changelog_pending_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/changelog/changelog_pending_retrieve.py)

=== "TypeScript"

    ```typescript
    import { changelogPendingRetrieve } from 'waldur-js-client';
    
    try {
      const response = await changelogPendingRetrieve({
      auth: "Token YOUR_API_TOKEN"
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `current_version` | string |
    | `latest_version` | string |
    | `versions_behind` | integer |
    | `impact_analysis_status` | string |
    | `impact_analysis_computed_at` | string (date-time) |
    | `releases` | array of objects |
    | `releases.version` | string |
    | `releases.date` | string |
    | `releases.type` | string |
    | `releases.summary` | string |
    | `releases.entries` | array of objects |
    | `releases.entries.id` | string |
    | `releases.entries.type` | string |
    | `releases.entries.category` | string |
    | `releases.entries.title` | string |
    | `releases.entries.description` | string |
    | `releases.entries.scope` | string |
    | `releases.entries.component` | array of strings |
    | `releases.entries.highlight` | boolean |
    | `releases.entries.impact` | object |
    | `releases.entries.impact.risk` | string |
    | `releases.entries.impact.affected_scope` | string |
    | `releases.entries.impact.affected_resources` | object (free-form) |
    | `releases.entries.impact.affected_users` | object (free-form) |
    | `releases.entries.security` | any |
    | `releases.entries.actions` | array of objects |
    | `releases.entries.actions.type` | string |
    | `releases.entries.actions.description` | string |
    | `releases.entries.actions.automatic` | boolean |
    | `releases.entries.actions.deadline` | string |
    | `releases.entries.relevant_when` | object |
    | `releases.entries.relevant_when.plugins` | array of strings |
    | `releases.entries.relevant_when.feature_flags` | array of strings |
    | `releases.entries.relevant_when.settings` | array of strings |
    | `releases.entries.relevant` | boolean |
    | `releases.entries.relevance_reasons` | array of strings |
    | `releases.entries.affected_resources_count` | integer |
    | `releases.entries.affected_users_count` | integer |
    | `releases.entries.settings_analysis` | object (free-form) |
    | `releases.entries.plugin_analysis` | object (free-form) |
    | `releases.since_previous` | array of objects |
    | `releases.since_previous.id` | string |
    | `releases.since_previous.type` | string |
    | `releases.since_previous.category` | string |
    | `releases.since_previous.title` | string |
    | `releases.since_previous.description` | string |
    | `releases.since_previous.scope` | string |
    | `releases.since_previous.component` | array of strings |
    | `releases.since_previous.highlight` | boolean |
    | `releases.since_previous.impact` | object |
    | `releases.since_previous.impact.risk` | string |
    | `releases.since_previous.impact.affected_scope` | string |
    | `releases.since_previous.impact.affected_resources` | object (free-form) |
    | `releases.since_previous.impact.affected_users` | object (free-form) |
    | `releases.since_previous.security` | any |
    | `releases.since_previous.actions` | array of objects |
    | `releases.since_previous.actions.type` | string |
    | `releases.since_previous.actions.description` | string |
    | `releases.since_previous.actions.automatic` | boolean |
    | `releases.since_previous.actions.deadline` | string |
    | `releases.since_previous.relevant_when` | object |
    | `releases.since_previous.relevant_when.plugins` | array of strings |
    | `releases.since_previous.relevant_when.feature_flags` | array of strings |
    | `releases.since_previous.relevant_when.settings` | array of strings |
    | `releases.since_previous.relevant` | boolean |
    | `releases.since_previous.relevance_reasons` | array of strings |
    | `releases.since_previous.affected_resources_count` | integer |
    | `releases.since_previous.affected_users_count` | integer |
    | `releases.since_previous.settings_analysis` | object (free-form) |
    | `releases.since_previous.plugin_analysis` | object (free-form) |
    | `releases.component_activity` | object (free-form) |

---

### List changelog releases

Returns every release in the changelog index, newest first, each marked as the release this deployment runs, pending (newer) or older.


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/changelog/releases/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.changelog import changelog_releases_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = changelog_releases_retrieve.sync(client=client)
    
    print(response)
    ```
    
    
    1.  **API Source:** [`changelog_releases_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/changelog/changelog_releases_retrieve.py)

=== "TypeScript"

    ```typescript
    import { changelogReleasesRetrieve } from 'waldur-js-client';
    
    try {
      const response = await changelogReleasesRetrieve({
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
    | `releases` | array of objects |  |
    | `releases.version` | string |  |
    | `releases.date` | string |  |
    | `releases.type` | string |  |
    | `releases.status` | any | Relative to the version this deployment runs |
    | `releases.has_breaking` | boolean |  |
    | `releases.has_security` | boolean |  |
    | `releases.max_security_urgency` | string |  |

---
