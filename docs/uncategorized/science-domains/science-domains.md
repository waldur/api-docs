# Science Domains

## Operations Summary

| Method | Endpoint | Description |
|:--- |:--- |:--- |
| **Core CRUD** | | |
| <span class="http-badge http-get">GET</span> | `/api/science-domains/` | [List Science Domains](#list-science-domains) |
| <span class="http-badge http-get">GET</span> | `/api/science-domains/{uuid}/` | [Retrieve](#retrieve) |
| <span class="http-badge http-post">POST</span> | `/api/science-domains/` | [Create](#create) |
| <span class="http-badge http-put">PUT</span> | `/api/science-domains/{uuid}/` | [Update](#update) |
| <span class="http-badge http-patch">PATCH</span> | `/api/science-domains/{uuid}/` | [Partial Update](#partial-update) |
| <span class="http-badge http-delete">DELETE</span> | `/api/science-domains/{uuid}/` | [Delete](#delete) |
| **Other Actions** | | |
| <span class="http-badge http-get">GET</span> | `/api/science-domains/presets/` | [List available science domain presets](#list-available-science-domain-presets) |
| <span class="http-badge http-post">POST</span> | `/api/science-domains/load_preset/` | [Load a science domain preset](#load-a-science-domain-preset) |

---
## Core CRUD


### List Science Domains


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/science-domains/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.science_domain_o_enum import ScienceDomainOEnum # (1)
    from waldur_api_client.api.science_domains import science_domains_list # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = science_domains_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`ScienceDomainOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/science_domain_o_enum.py)
    2.  **API Source:** [`science_domains_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/science_domains/science_domains_list.py)

=== "TypeScript"

    ```typescript
    import { scienceDomainsList } from 'waldur-js-client';
    
    try {
      const response = await scienceDomainsList({
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
    | `name` | string | Name |
    | `name_exact` | string | Name (exact) |
    | `o` | array | Ordering<br><br> |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `code` | string | Domain code (e.g. '1'). Auto-derived if left blank. |
    | `name` | string |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `subdomains_count` | integer | Number of sub-domains in this domain |

---

### Retrieve


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/science-domains/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.science_domains import science_domains_retrieve # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = science_domains_retrieve.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`science_domains_retrieve`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/science_domains/science_domains_retrieve.py)

=== "TypeScript"

    ```typescript
    import { scienceDomainsRetrieve } from 'waldur-js-client';
    
    try {
      const response = await scienceDomainsRetrieve({
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
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `code` | string | Domain code (e.g. '1'). Auto-derived if left blank. |
    | `name` | string |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `subdomains_count` | integer | Number of sub-domains in this domain |

---

### Create


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/science-domains/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-science-domain"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.science_domain_request import ScienceDomainRequest # (1)
    from waldur_api_client.api.science_domains import science_domains_create # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ScienceDomainRequest(
        name="my-awesome-science-domain"
    )
    response = science_domains_create.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ScienceDomainRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/science_domain_request.py)
    2.  **API Source:** [`science_domains_create`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/science_domains/science_domains_create.py)

=== "TypeScript"

    ```typescript
    import { scienceDomainsCreate } from 'waldur-js-client';
    
    try {
      const response = await scienceDomainsCreate({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "name": "my-awesome-science-domain"
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
    | `code` | string |  | Domain code (e.g. '1'). Auto-derived if left blank. |
    | `name` | string | ✓ |  |


=== "Responses"

    **`201`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `code` | string | Domain code (e.g. '1'). Auto-derived if left blank. |
    | `name` | string |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `subdomains_count` | integer | Number of sub-domains in this domain |

---

### Update


=== "HTTPie"

    ```bash
    http \
      PUT \
      https://api.example.com/api/science-domains/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN" \
      name="my-awesome-science-domain"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.science_domain_request import ScienceDomainRequest # (1)
    from waldur_api_client.api.science_domains import science_domains_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = ScienceDomainRequest(
        name="my-awesome-science-domain"
    )
    response = science_domains_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`ScienceDomainRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/science_domain_request.py)
    2.  **API Source:** [`science_domains_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/science_domains/science_domains_update.py)

=== "TypeScript"

    ```typescript
    import { scienceDomainsUpdate } from 'waldur-js-client';
    
    try {
      const response = await scienceDomainsUpdate({
      auth: "Token YOUR_API_TOKEN",
      path: {
        "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      },
      body: {
        "name": "my-awesome-science-domain"
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
    | `code` | string |  | Domain code (e.g. '1'). Auto-derived if left blank. |
    | `name` | string | ✓ |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `code` | string | Domain code (e.g. '1'). Auto-derived if left blank. |
    | `name` | string |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `subdomains_count` | integer | Number of sub-domains in this domain |

---

### Partial Update


=== "HTTPie"

    ```bash
    http \
      PATCH \
      https://api.example.com/api/science-domains/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.patched_science_domain_request import PatchedScienceDomainRequest # (1)
    from waldur_api_client.api.science_domains import science_domains_partial_update # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = PatchedScienceDomainRequest()
    response = science_domains_partial_update.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`PatchedScienceDomainRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/patched_science_domain_request.py)
    2.  **API Source:** [`science_domains_partial_update`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/science_domains/science_domains_partial_update.py)

=== "TypeScript"

    ```typescript
    import { scienceDomainsPartialUpdate } from 'waldur-js-client';
    
    try {
      const response = await scienceDomainsPartialUpdate({
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

    | Field | Type | Required | Description |
    |---|---|---|---|
    | `code` | string |  | Domain code (e.g. '1'). Auto-derived if left blank. |
    | `name` | string |  |  |


=== "Responses"

    **`200`** - 
    
    | Field | Type | Description |
    |---|---|---|
    | `uuid` | string (uuid) |  |
    | `url` | string (uri) |  |
    | `code` | string | Domain code (e.g. '1'). Auto-derived if left blank. |
    | `name` | string |  |
    | `created` | string (date-time) |  |
    | `modified` | string (date-time) |  |
    | `subdomains_count` | integer | Number of sub-domains in this domain |

---

### Delete


=== "HTTPie"

    ```bash
    http \
      DELETE \
      https://api.example.com/api/science-domains/a1b2c3d4-e5f6-7890-abcd-ef1234567890/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.api.science_domains import science_domains_destroy # (1)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = science_domains_destroy.sync(
        uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        client=client
    )
    
    print(response)
    ```
    
    
    1.  **API Source:** [`science_domains_destroy`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/science_domains/science_domains_destroy.py)

=== "TypeScript"

    ```typescript
    import { scienceDomainsDestroy } from 'waldur-js-client';
    
    try {
      const response = await scienceDomainsDestroy({
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

    **`204`** - No response body
    

---

## Other Actions


### List available science domain presets


=== "HTTPie"

    ```bash
    http \
      GET \
      https://api.example.com/api/science-domains/presets/ \
      Authorization:"Token YOUR_API_TOKEN"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.science_domain_o_enum import ScienceDomainOEnum # (1)
    from waldur_api_client.api.science_domains import science_domains_presets_list # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    response = science_domains_presets_list.sync(client=client)
    
    for item in response:
        print(item)
    ```
    
    
    1.  **Model Source:** [`ScienceDomainOEnum`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/science_domain_o_enum.py)
    2.  **API Source:** [`science_domains_presets_list`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/science_domains/science_domains_presets_list.py)

=== "TypeScript"

    ```typescript
    import { scienceDomainsPresetsList } from 'waldur-js-client';
    
    try {
      const response = await scienceDomainsPresetsList({
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
    | `name` | string | Name |
    | `name_exact` | string | Name (exact) |
    | `o` | array | Ordering<br><br> |
    | `page` | integer | A page number within the paginated result set. |
    | `page_size` | integer | Number of results to return per page. |


=== "Responses"

    **`200`** - 
    
    The response body is an array of objects, where each object has the following structure:
    
    | Field | Type |
    |---|---|
    | `name` | string |
    | `label` | string |
    | `description` | string |

---

### Load a science domain preset


=== "HTTPie"

    ```bash
    http \
      POST \
      https://api.example.com/api/science-domains/load_preset/ \
      Authorization:"Token YOUR_API_TOKEN" \
      preset="cscs"
    ```

=== "Python"

    ```python
    from waldur_api_client.client import AuthenticatedClient
    from waldur_api_client.models.load_science_domain_preset_request import LoadScienceDomainPresetRequest # (1)
    from waldur_api_client.api.science_domains import science_domains_load_preset # (2)
    
    client = AuthenticatedClient(
        base_url="https://api.example.com", token="YOUR_API_TOKEN"
    )
    
    body_data = LoadScienceDomainPresetRequest(
        preset="cscs"
    )
    response = science_domains_load_preset.sync(
        client=client,
        body=body_data
    )
    
    print(response)
    ```
    
    
    1.  **Model Source:** [`LoadScienceDomainPresetRequest`](https://github.com/waldur/py-client/blob/main/waldur_api_client/models/load_science_domain_preset_request.py)
    2.  **API Source:** [`science_domains_load_preset`](https://github.com/waldur/py-client/blob/main/waldur_api_client/api/science_domains/science_domains_load_preset.py)

=== "TypeScript"

    ```typescript
    import { scienceDomainsLoadPreset } from 'waldur-js-client';
    
    try {
      const response = await scienceDomainsLoadPreset({
      auth: "Token YOUR_API_TOKEN",
      body: {
        "preset": "cscs"
      }
    });
      console.log('Success:', response);
    } catch (error) {
      console.error('Error:', error);
    }
    ```


=== "Request Body (required)"

    | Field | Type | Required |
    |---|---|---|
    | `preset` | string | ✓ |


=== "Responses"

    **`200`** - 
    
    | Field | Type |
    |---|---|
    | `created_domains` | integer |
    | `created_subdomains` | integer |
    | `skipped_domains` | integer |
    | `skipped_subdomains` | integer |

---
