# OpenAPI schema diff - 8.0.5

## For version 8.0.5

### New Endpoints: 1

--------------------
POST /api/marketplace-component-usages/{uuid}/set_user_usages/  

### Deleted Endpoints: 1

------------------------
POST /api/chat-messages/{uuid}/edit/  

### Modified Endpoints: 79

--------------------------
POST /api/backend-resources/{uuid}/import_resource/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: current_usages
              - Description changed from '' to 'Dictionary mapping component types to their latest reported usage amounts.'
              - AdditionalProperties changed
                - Type changed from 'integer' to 'number'
                - Format changed from '' to 'double'
            - Modified property: is_limit_based
              - Description changed from '' to 'Returns True if the resource has limit-based components with user-adjustable quotas.'
            - Modified property: is_usage_based
              - Description changed from '' to 'Returns True if the resource has usage-based components that track variable consumption.'
            - Modified property: limit_usage
              - Description changed from '' to 'Dictionary mapping limit-based component types to their consumed usage. For monthly periods, maps from current_usages; for longer periods, aggregates historical usage.'

GET /api/booking-offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: resource_name_pattern

GET /api/booking-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: resource_name_pattern

GET /api/booking-resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: current_usages
                - Description changed from '' to 'Dictionary mapping component types to their latest reported usage amounts.'
                - AdditionalProperties changed
                  - Type changed from 'integer' to 'number'
                  - Format changed from '' to 'double'
              - Modified property: is_limit_based
                - Description changed from '' to 'Returns True if the resource has limit-based components with user-adjustable quotas.'
              - Modified property: is_usage_based
                - Description changed from '' to 'Returns True if the resource has usage-based components that track variable consumption.'
              - Modified property: limit_usage
                - Description changed from '' to 'Dictionary mapping limit-based component types to their consumed usage. For monthly periods, maps from current_usages; for longer periods, aggregates historical usage.'

GET /api/booking-resources/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: current_usages
              - Description changed from '' to 'Dictionary mapping component types to their latest reported usage amounts.'
              - AdditionalProperties changed
                - Type changed from 'integer' to 'number'
                - Format changed from '' to 'double'
            - Modified property: is_limit_based
              - Description changed from '' to 'Returns True if the resource has limit-based components with user-adjustable quotas.'
            - Modified property: is_usage_based
              - Description changed from '' to 'Returns True if the resource has usage-based components that track variable consumption.'
            - Modified property: limit_usage
              - Description changed from '' to 'Dictionary mapping limit-based component types to their consumed usage. For monthly periods, maps from current_usages; for longer periods, aggregates historical usage.'

GET /api/chat-messages/

- New query param: is_flagged
- Deleted query param: page
- Deleted query param: page_size
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: injection_categories
              - New required property: injection_score
              - New required property: injection_severity
              - New required property: is_flagged
            - Properties changed
              - New property: injection_categories
              - New property: injection_score
              - New property: injection_severity
              - New property: is_flagged

GET /api/chat-threads/

- New query param: is_flagged
- New query param: max_severity
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [is_flagged max_severity]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: is_flagged
              - New property: max_severity

GET /api/chat-threads/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [is_flagged max_severity]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: is_flagged
            - New property: max_severity

POST /api/chat/stream/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: edit_message_uuid
          - Modified property: input
            - MaxLength changed from null to 50000
          - Modified property: mode
            - Property 'OneOf' changed
              - Modified schema: #/components/schemas/ChatRequestModeEnum
                - New enum values: [edit]
            - Description changed from ''reload': replace the last assistant response. Omit for normal new-message behavior.' to ''reload': replace the last assistant response. 'edit': edit a user message and re-stream. Omit for normal new-message behavior.'
          - Modified property: thread_uuid
            - Description changed from 'Existing thread UUID. If omitted, a new thread is created when storage is enabled.' to 'Existing thread UUID. If omitted, a new thread is created.'

GET /api/hooks-email/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: event_types
                - Items changed
                  - New enum values: [chat_injection_detected]

POST /api/hooks-email/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [chat_injection_detected]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [chat_injection_detected]

GET /api/hooks-email/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [chat_injection_detected]

PATCH /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [chat_injection_detected]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [chat_injection_detected]

PUT /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [chat_injection_detected]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [chat_injection_detected]

GET /api/hooks-web/

- Modified query param: content_type
  - Schema changed
    - Type changed from 'integer' to 'string'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: event_types
                - Items changed
                  - New enum values: [chat_injection_detected]

HEAD /api/hooks-web/

- Modified query param: content_type
  - Schema changed
    - Type changed from 'integer' to 'string'

POST /api/hooks-web/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [chat_injection_detected]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [chat_injection_detected]

GET /api/hooks-web/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [chat_injection_detected]

PATCH /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [chat_injection_detected]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [chat_injection_detected]

PUT /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [chat_injection_detected]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [chat_injection_detected]

GET /api/invoice-items/costs/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: items

GET /api/managed-rancher-cluster-resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: current_usages
                - Description changed from '' to 'Dictionary mapping component types to their latest reported usage amounts.'
                - AdditionalProperties changed
                  - Type changed from 'integer' to 'number'
                  - Format changed from '' to 'double'
              - Modified property: is_limit_based
                - Description changed from '' to 'Returns True if the resource has limit-based components with user-adjustable quotas.'
              - Modified property: is_usage_based
                - Description changed from '' to 'Returns True if the resource has usage-based components that track variable consumption.'
              - Modified property: limit_usage
                - Description changed from '' to 'Dictionary mapping limit-based component types to their consumed usage. For monthly periods, maps from current_usages; for longer periods, aggregates historical usage.'

GET /api/managed-rancher-cluster-resources/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: current_usages
              - Description changed from '' to 'Dictionary mapping component types to their latest reported usage amounts.'
              - AdditionalProperties changed
                - Type changed from 'integer' to 'number'
                - Format changed from '' to 'double'
            - Modified property: is_limit_based
              - Description changed from '' to 'Returns True if the resource has limit-based components with user-adjustable quotas.'
            - Modified property: is_usage_based
              - Description changed from '' to 'Returns True if the resource has usage-based components that track variable consumption.'
            - Modified property: limit_usage
              - Description changed from '' to 'Dictionary mapping limit-based component types to their consumed usage. For monthly periods, maps from current_usages; for longer periods, aggregates historical usage.'

GET /api/marketplace-categories/

- Modified query param: customers_offerings_state
  - Schema changed
    - Items changed
      - Type changed from 'string' to 'integer'

HEAD /api/marketplace-categories/

- Modified query param: customers_offerings_state
  - Schema changed
    - Items changed
      - Type changed from 'string' to 'integer'

GET /api/marketplace-course-accounts/

- Modified query param: state
  - Schema changed
    - Items changed
      - Type changed from 'string' to ''

HEAD /api/marketplace-course-accounts/

- Modified query param: state
  - Schema changed
    - Items changed
      - Type changed from 'string' to ''

POST /api/marketplace-course-accounts/create_bulk/

- Modified query param: state
  - Schema changed
    - Items changed
      - Type changed from 'string' to ''

GET /api/marketplace-customer-service-accounts/

- Modified query param: state
  - Schema changed
    - Items changed
      - Type changed from 'string' to ''

HEAD /api/marketplace-customer-service-accounts/

- Modified query param: state
  - Schema changed
    - Items changed
      - Type changed from 'string' to ''

GET /api/marketplace-orders/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: resource_name_pattern

GET /api/marketplace-project-service-accounts/

- Modified query param: state
  - Schema changed
    - Items changed
      - Type changed from 'string' to ''

HEAD /api/marketplace-project-service-accounts/

- Modified query param: state
  - Schema changed
    - Items changed
      - Type changed from 'string' to ''

GET /api/marketplace-provider-offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: resource_name_pattern

POST /api/marketplace-provider-offerings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: resource_name_pattern
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: resource_name_pattern
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: resource_name_pattern
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: resource_name_pattern

GET /api/marketplace-provider-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: resource_name_pattern

POST /api/marketplace-provider-offerings/{uuid}/import_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: current_usages
              - Description changed from '' to 'Dictionary mapping component types to their latest reported usage amounts.'
              - AdditionalProperties changed
                - Type changed from 'integer' to 'number'
                - Format changed from '' to 'double'
            - Modified property: is_limit_based
              - Description changed from '' to 'Returns True if the resource has limit-based components with user-adjustable quotas.'
            - Modified property: is_usage_based
              - Description changed from '' to 'Returns True if the resource has usage-based components that track variable consumption.'
            - Modified property: limit_usage
              - Description changed from '' to 'Dictionary mapping limit-based component types to their consumed usage. For monthly periods, maps from current_usages; for longer periods, aggregates historical usage.'

POST /api/marketplace-provider-offerings/{uuid}/move_offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: resource_name_pattern

POST /api/marketplace-provider-offerings/{uuid}/update_integration/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: resource_name_pattern

GET /api/marketplace-provider-offerings/{uuid}/user_has_resource_access/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: resource_name_pattern

GET /api/marketplace-provider-resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: current_usages
                - Description changed from '' to 'Dictionary mapping component types to their latest reported usage amounts.'
                - AdditionalProperties changed
                  - Type changed from 'integer' to 'number'
                  - Format changed from '' to 'double'
              - Modified property: is_limit_based
                - Description changed from '' to 'Returns True if the resource has limit-based components with user-adjustable quotas.'
              - Modified property: is_usage_based
                - Description changed from '' to 'Returns True if the resource has usage-based components that track variable consumption.'
              - Modified property: limit_usage
                - Description changed from '' to 'Dictionary mapping limit-based component types to their consumed usage. For monthly periods, maps from current_usages; for longer periods, aggregates historical usage.'

GET /api/marketplace-provider-resources/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: current_usages
              - Description changed from '' to 'Dictionary mapping component types to their latest reported usage amounts.'
              - AdditionalProperties changed
                - Type changed from 'integer' to 'number'
                - Format changed from '' to 'double'
            - Modified property: is_limit_based
              - Description changed from '' to 'Returns True if the resource has limit-based components with user-adjustable quotas.'
            - Modified property: is_usage_based
              - Description changed from '' to 'Returns True if the resource has usage-based components that track variable consumption.'
            - Modified property: limit_usage
              - Description changed from '' to 'Dictionary mapping limit-based component types to their consumed usage. For monthly periods, maps from current_usages; for longer periods, aggregates historical usage.'

POST /api/marketplace-provider-resources/{uuid}/move_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: current_usages
              - Description changed from '' to 'Dictionary mapping component types to their latest reported usage amounts.'
              - AdditionalProperties changed
                - Type changed from 'integer' to 'number'
                - Format changed from '' to 'double'
            - Modified property: is_limit_based
              - Description changed from '' to 'Returns True if the resource has limit-based components with user-adjustable quotas.'
            - Modified property: is_usage_based
              - Description changed from '' to 'Returns True if the resource has usage-based components that track variable consumption.'
            - Modified property: limit_usage
              - Description changed from '' to 'Dictionary mapping limit-based component types to their consumed usage. For monthly periods, maps from current_usages; for longer periods, aggregates historical usage.'

GET /api/marketplace-provider-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: resource_name_pattern

POST /api/marketplace-provider-resources/{uuid}/restore/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: current_usages
              - Description changed from '' to 'Dictionary mapping component types to their latest reported usage amounts.'
              - AdditionalProperties changed
                - Type changed from 'integer' to 'number'
                - Format changed from '' to 'double'
            - Modified property: is_limit_based
              - Description changed from '' to 'Returns True if the resource has limit-based components with user-adjustable quotas.'
            - Modified property: is_usage_based
              - Description changed from '' to 'Returns True if the resource has usage-based components that track variable consumption.'
            - Modified property: limit_usage
              - Description changed from '' to 'Dictionary mapping limit-based component types to their consumed usage. For monthly periods, maps from current_usages; for longer periods, aggregates historical usage.'

GET /api/marketplace-public-offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: resource_name_pattern

GET /api/marketplace-public-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: resource_name_pattern

GET /api/marketplace-resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: current_usages
                - Description changed from '' to 'Dictionary mapping component types to their latest reported usage amounts.'
                - AdditionalProperties changed
                  - Type changed from 'integer' to 'number'
                  - Format changed from '' to 'double'
              - Modified property: is_limit_based
                - Description changed from '' to 'Returns True if the resource has limit-based components with user-adjustable quotas.'
              - Modified property: is_usage_based
                - Description changed from '' to 'Returns True if the resource has usage-based components that track variable consumption.'
              - Modified property: limit_usage
                - Description changed from '' to 'Dictionary mapping limit-based component types to their consumed usage. For monthly periods, maps from current_usages; for longer periods, aggregates historical usage.'

POST /api/marketplace-resources/suggest_name/

- Description changed from 'Generates a suggested name for a new resource based on the project and offering.' to 'Generates a suggested name for a new resource based on the project and offering. If the offering has a `resource_name_pattern` in `plugin_options`, it is used as a Python format string with variables: `{customer_name}`, `{customer_slug}`, `{project_name}`, `{project_slug}`, `{offering_name}`, `{offering_slug}`, `{plan_name}`, `{counter}`, and `{attributes[KEY]}` for any order form value.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: attributes
          - New property: plan

GET /api/marketplace-resources/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: current_usages
              - Description changed from '' to 'Dictionary mapping component types to their latest reported usage amounts.'
              - AdditionalProperties changed
                - Type changed from 'integer' to 'number'
                - Format changed from '' to 'double'
            - Modified property: is_limit_based
              - Description changed from '' to 'Returns True if the resource has limit-based components with user-adjustable quotas.'
            - Modified property: is_usage_based
              - Description changed from '' to 'Returns True if the resource has usage-based components that track variable consumption.'
            - Modified property: limit_usage
              - Description changed from '' to 'Dictionary mapping limit-based component types to their consumed usage. For monthly periods, maps from current_usages; for longer periods, aggregates historical usage.'

POST /api/marketplace-resources/{uuid}/move_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: current_usages
              - Description changed from '' to 'Dictionary mapping component types to their latest reported usage amounts.'
              - AdditionalProperties changed
                - Type changed from 'integer' to 'number'
                - Format changed from '' to 'double'
            - Modified property: is_limit_based
              - Description changed from '' to 'Returns True if the resource has limit-based components with user-adjustable quotas.'
            - Modified property: is_usage_based
              - Description changed from '' to 'Returns True if the resource has usage-based components that track variable consumption.'
            - Modified property: limit_usage
              - Description changed from '' to 'Dictionary mapping limit-based component types to their consumed usage. For monthly periods, maps from current_usages; for longer periods, aggregates historical usage.'

GET /api/marketplace-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: resource_name_pattern

POST /api/marketplace-resources/{uuid}/restore/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: current_usages
              - Description changed from '' to 'Dictionary mapping component types to their latest reported usage amounts.'
              - AdditionalProperties changed
                - Type changed from 'integer' to 'number'
                - Format changed from '' to 'double'
            - Modified property: is_limit_based
              - Description changed from '' to 'Returns True if the resource has limit-based components with user-adjustable quotas.'
            - Modified property: is_usage_based
              - Description changed from '' to 'Returns True if the resource has usage-based components that track variable consumption.'
            - Modified property: limit_usage
              - Description changed from '' to 'Dictionary mapping limit-based component types to their consumed usage. For monthly periods, maps from current_usages; for longer periods, aggregates historical usage.'

GET /api/marketplace-robot-accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: offering_plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: resource_name_pattern

GET /api/marketplace-robot-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: resource_name_pattern

POST /api/marketplace-robot-accounts/{uuid}/set_state_creating/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: resource_name_pattern

POST /api/marketplace-robot-accounts/{uuid}/set_state_deleted/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: resource_name_pattern

POST /api/marketplace-robot-accounts/{uuid}/set_state_erred/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: resource_name_pattern

POST /api/marketplace-robot-accounts/{uuid}/set_state_ok/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: resource_name_pattern

POST /api/marketplace-robot-accounts/{uuid}/set_state_request_deletion/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: resource_name_pattern

POST /api/marketplace-script-dry-run/{uuid}/async_run/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: resource_name_pattern

POST /api/marketplace-script-dry-run/{uuid}/run/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: resource_name_pattern

GET /api/marketplace-service-providers/{service_provider_uuid}/course_accounts/

- Modified query param: state
  - Schema changed
    - Items changed
      - Type changed from 'string' to ''

GET /api/marketplace-service-providers/{service_provider_uuid}/project_service_accounts/

- Modified query param: state
  - Schema changed
    - Items changed
      - Type changed from 'string' to ''

GET /api/metadata/events/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - AdditionalProperties changed
                - Items changed
                  - New enum values: [chat_injection_detected]

GET /api/onboarding-verifications/available_checklists/

- Modified query param: checklist_type
  - Schema changed
    - Default changed from 'all' to null
    - MinLength changed from 1 to 0

HEAD /api/onboarding-verifications/available_checklists/

- Modified query param: checklist_type
  - Schema changed
    - Default changed from 'all' to null
    - MinLength changed from 1 to 0

GET /api/onboarding-verifications/{uuid}/checklist/

- Modified query param: checklist_type
  - Schema changed
    - Default changed from 'intent' to null
    - MinLength changed from 1 to 0

GET /api/onboarding-verifications/{uuid}/completion_status/

- Modified query param: checklist_type
  - Schema changed
    - Default changed from 'intent' to null
    - MinLength changed from 1 to 0

GET /api/openportal-managed-projects/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: project_template_data
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/ProjectTemplate
                    - Properties changed
                      - Modified property: offerings_data
                        - Items changed
                          - Properties changed
                            - Modified property: plugin_options
                              - Property 'AllOf' changed
                                - Modified schema: #/components/schemas/MergedPluginOptions
                                  - Properties changed
                                    - New property: resource_name_pattern

GET /api/openportal-managed-projects/{identifier}/{destination}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: project_template_data
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ProjectTemplate
                  - Properties changed
                    - Modified property: offerings_data
                      - Items changed
                        - Properties changed
                          - Modified property: plugin_options
                            - Property 'AllOf' changed
                              - Modified schema: #/components/schemas/MergedPluginOptions
                                - Properties changed
                                  - New property: resource_name_pattern

GET /api/openportal-project-template/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: offerings_data
                - Items changed
                  - Properties changed
                    - Modified property: plugin_options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/MergedPluginOptions
                          - Properties changed
                            - New property: resource_name_pattern

POST /api/openportal-project-template/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offerings_data
              - Items changed
                - Properties changed
                  - Modified property: plugin_options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/MergedPluginOptions
                        - Properties changed
                          - New property: resource_name_pattern

GET /api/openportal-project-template/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offerings_data
              - Items changed
                - Properties changed
                  - Modified property: plugin_options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/MergedPluginOptions
                        - Properties changed
                          - New property: resource_name_pattern

PATCH /api/openportal-project-template/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offerings_data
              - Items changed
                - Properties changed
                  - Modified property: plugin_options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/MergedPluginOptions
                        - Properties changed
                          - New property: resource_name_pattern

PUT /api/openportal-project-template/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offerings_data
              - Items changed
                - Properties changed
                  - Modified property: plugin_options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/MergedPluginOptions
                        - Properties changed
                          - New property: resource_name_pattern

GET /api/override-settings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: LLM_INJECTION_ALLOWLIST
            - Deleted property: LLM_CHAT_STORAGE_ENABLED
            - Modified property: DEFAULT_IDP
              - Property 'OneOf' changed
                - Schemas added: #/components/schemas/DEFAULTIDPEnum, #/components/schemas/BlankEnum
              - Type changed from 'string' to ''
            - Modified property: DEFAULT_OFFERING_USER_ATTRIBUTES
              - Items changed
                - Property 'OneOf' changed
                  - Schemas added: #/components/schemas/UserAttributeEnum, #/components/schemas/BlankEnum
                - Type changed from 'string' to ''
            - Modified property: DISABLED_OFFERING_TYPES
              - Items changed
                - Property 'OneOf' changed
                  - Schemas added: #/components/schemas/OfferingTypeEnum, #/components/schemas/BlankEnum
                - Type changed from 'string' to ''
            - Modified property: ENABLED_USER_PROFILE_ATTRIBUTES
              - Items changed
                - Property 'OneOf' changed
                  - Schemas added: #/components/schemas/UserAttributeEnum, #/components/schemas/BlankEnum
                - Type changed from 'string' to ''
            - Modified property: FEDERATED_IDENTITY_DEACTIVATION_POLICY
              - New enum values: [all_isds_removed any_isd_removed]
            - Modified property: FEDERATED_IDENTITY_SYNC_ALLOWED_ATTRIBUTES
              - Items changed
                - Property 'OneOf' changed
                  - Schemas added: #/components/schemas/UserAttributeEnum, #/components/schemas/BlankEnum
                - Type changed from 'string' to ''
            - Modified property: FONT_FAMILY
              - New enum values: [Inter Maven Pro]
            - Modified property: INVITATION_ALLOWED_FIELDS
              - Items changed
                - Property 'OneOf' changed
                  - Schemas added: #/components/schemas/UserAttributeEnum, #/components/schemas/BlankEnum
                - Type changed from 'string' to ''
            - Modified property: LOGIN_PAGE_LAYOUT
              - New enum values: [split-screen centered-card minimal full-hero gradient stacked right-split glassmorphism neumorphism animated-gradient video-background bottom-sheet tabbed wizard stats news carousel logo-watermark brand-pattern duotone diagonal time-based seasonal weather]
            - Modified property: MAINTENANCE_ANNOUNCEMENT_NOTIFY_SYSTEM
              - Items changed
                - Property 'OneOf' changed
                  - Schemas added: #/components/schemas/NotifySystemEnum, #/components/schemas/BlankEnum
                - Type changed from 'string' to ''
            - Modified property: MANDATORY_USER_ATTRIBUTES
              - Items changed
                - Property 'OneOf' changed
                  - Schemas added: #/components/schemas/UserAttributeEnum, #/components/schemas/BlankEnum
                - Type changed from 'string' to ''
            - Modified property: ONBOARDING_VALIDATION_METHODS
              - Items changed
                - Property 'OneOf' changed
                  - Schemas added: #/components/schemas/OnboardingValidationEnum, #/components/schemas/BlankEnum
                - Type changed from 'string' to ''
            - Modified property: RESTRICTED_OFFERING_VISIBILITY_MODE
              - New enum values: [show_all show_restricted_disabled hide_inaccessible require_membership]
            - Modified property: SCRIPT_RUN_MODE
              - New enum values: [docker k8s]
            - Modified property: SIDEBAR_STYLE
              - New enum values: [primary accent accent-light dark light auto]
            - Modified property: WALDUR_SUPPORT_ACTIVE_BACKEND_TYPE
              - New enum values: [atlassian zammad smax]
            - Modified property: ZAMMAD_ARTICLE_TYPE
              - New enum values: [email phone web note sms chat fax twitter status twitter direct-message facebook feed post facebook feed comment telegram personal-message]

POST /api/override-settings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: LLM_INJECTION_ALLOWLIST
          - Deleted property: LLM_CHAT_STORAGE_ENABLED
          - Modified property: DEFAULT_IDP
            - Property 'OneOf' changed
              - Schemas added: #/components/schemas/DEFAULTIDPEnum, #/components/schemas/BlankEnum
            - Type changed from 'string' to ''
          - Modified property: DEFAULT_OFFERING_USER_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Schemas added: #/components/schemas/UserAttributeEnum, #/components/schemas/BlankEnum
              - Type changed from 'string' to ''
              - MinLength changed from 1 to 0
          - Modified property: DISABLED_OFFERING_TYPES
            - Items changed
              - Property 'OneOf' changed
                - Schemas added: #/components/schemas/OfferingTypeEnum, #/components/schemas/BlankEnum
              - Type changed from 'string' to ''
              - MinLength changed from 1 to 0
          - Modified property: ENABLED_USER_PROFILE_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Schemas added: #/components/schemas/UserAttributeEnum, #/components/schemas/BlankEnum
              - Type changed from 'string' to ''
              - MinLength changed from 1 to 0
          - Modified property: FEDERATED_IDENTITY_DEACTIVATION_POLICY
            - New enum values: [all_isds_removed any_isd_removed]
          - Modified property: FEDERATED_IDENTITY_SYNC_ALLOWED_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Schemas added: #/components/schemas/UserAttributeEnum, #/components/schemas/BlankEnum
              - Type changed from 'string' to ''
              - MinLength changed from 1 to 0
          - Modified property: FONT_FAMILY
            - New enum values: [Inter Maven Pro]
          - Modified property: INVITATION_ALLOWED_FIELDS
            - Items changed
              - Property 'OneOf' changed
                - Schemas added: #/components/schemas/UserAttributeEnum, #/components/schemas/BlankEnum
              - Type changed from 'string' to ''
              - MinLength changed from 1 to 0
          - Modified property: LOGIN_PAGE_LAYOUT
            - New enum values: [split-screen centered-card minimal full-hero gradient stacked right-split glassmorphism neumorphism animated-gradient video-background bottom-sheet tabbed wizard stats news carousel logo-watermark brand-pattern duotone diagonal time-based seasonal weather]
          - Modified property: MAINTENANCE_ANNOUNCEMENT_NOTIFY_SYSTEM
            - Items changed
              - Property 'OneOf' changed
                - Schemas added: #/components/schemas/NotifySystemEnum, #/components/schemas/BlankEnum
              - Type changed from 'string' to ''
              - MinLength changed from 1 to 0
          - Modified property: MANDATORY_USER_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Schemas added: #/components/schemas/UserAttributeEnum, #/components/schemas/BlankEnum
              - Type changed from 'string' to ''
              - MinLength changed from 1 to 0
          - Modified property: ONBOARDING_VALIDATION_METHODS
            - Items changed
              - Property 'OneOf' changed
                - Schemas added: #/components/schemas/OnboardingValidationEnum, #/components/schemas/BlankEnum
              - Type changed from 'string' to ''
              - MinLength changed from 1 to 0
          - Modified property: RESTRICTED_OFFERING_VISIBILITY_MODE
            - New enum values: [show_all show_restricted_disabled hide_inaccessible require_membership]
          - Modified property: SCRIPT_RUN_MODE
            - New enum values: [docker k8s]
          - Modified property: SIDEBAR_STYLE
            - New enum values: [primary accent accent-light dark light auto]
          - Modified property: WALDUR_SUPPORT_ACTIVE_BACKEND_TYPE
            - New enum values: [atlassian zammad smax]
          - Modified property: ZAMMAD_ARTICLE_TYPE
            - New enum values: [email phone web note sms chat fax twitter status twitter direct-message facebook feed post facebook feed comment telegram personal-message]
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: LLM_INJECTION_ALLOWLIST
          - Deleted property: LLM_CHAT_STORAGE_ENABLED
          - Modified property: DEFAULT_IDP
            - Property 'OneOf' changed
              - Schemas added: #/components/schemas/DEFAULTIDPEnum, #/components/schemas/BlankEnum
            - Type changed from 'string' to ''
          - Modified property: DEFAULT_OFFERING_USER_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Schemas added: #/components/schemas/UserAttributeEnum, #/components/schemas/BlankEnum
              - Type changed from 'string' to ''
              - MinLength changed from 1 to 0
          - Modified property: DISABLED_OFFERING_TYPES
            - Items changed
              - Property 'OneOf' changed
                - Schemas added: #/components/schemas/OfferingTypeEnum, #/components/schemas/BlankEnum
              - Type changed from 'string' to ''
              - MinLength changed from 1 to 0
          - Modified property: ENABLED_USER_PROFILE_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Schemas added: #/components/schemas/UserAttributeEnum, #/components/schemas/BlankEnum
              - Type changed from 'string' to ''
              - MinLength changed from 1 to 0
          - Modified property: FEDERATED_IDENTITY_DEACTIVATION_POLICY
            - New enum values: [all_isds_removed any_isd_removed]
          - Modified property: FEDERATED_IDENTITY_SYNC_ALLOWED_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Schemas added: #/components/schemas/UserAttributeEnum, #/components/schemas/BlankEnum
              - Type changed from 'string' to ''
              - MinLength changed from 1 to 0
          - Modified property: FONT_FAMILY
            - New enum values: [Inter Maven Pro]
          - Modified property: INVITATION_ALLOWED_FIELDS
            - Items changed
              - Property 'OneOf' changed
                - Schemas added: #/components/schemas/UserAttributeEnum, #/components/schemas/BlankEnum
              - Type changed from 'string' to ''
              - MinLength changed from 1 to 0
          - Modified property: LOGIN_PAGE_LAYOUT
            - New enum values: [split-screen centered-card minimal full-hero gradient stacked right-split glassmorphism neumorphism animated-gradient video-background bottom-sheet tabbed wizard stats news carousel logo-watermark brand-pattern duotone diagonal time-based seasonal weather]
          - Modified property: MAINTENANCE_ANNOUNCEMENT_NOTIFY_SYSTEM
            - Items changed
              - Property 'OneOf' changed
                - Schemas added: #/components/schemas/NotifySystemEnum, #/components/schemas/BlankEnum
              - Type changed from 'string' to ''
              - MinLength changed from 1 to 0
          - Modified property: MANDATORY_USER_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Schemas added: #/components/schemas/UserAttributeEnum, #/components/schemas/BlankEnum
              - Type changed from 'string' to ''
              - MinLength changed from 1 to 0
          - Modified property: ONBOARDING_VALIDATION_METHODS
            - Items changed
              - Property 'OneOf' changed
                - Schemas added: #/components/schemas/OnboardingValidationEnum, #/components/schemas/BlankEnum
              - Type changed from 'string' to ''
              - MinLength changed from 1 to 0
          - Modified property: RESTRICTED_OFFERING_VISIBILITY_MODE
            - New enum values: [show_all show_restricted_disabled hide_inaccessible require_membership]
          - Modified property: SCRIPT_RUN_MODE
            - New enum values: [docker k8s]
          - Modified property: SIDEBAR_STYLE
            - New enum values: [primary accent accent-light dark light auto]
          - Modified property: WALDUR_SUPPORT_ACTIVE_BACKEND_TYPE
            - New enum values: [atlassian zammad smax]
          - Modified property: ZAMMAD_ARTICLE_TYPE
            - New enum values: [email phone web note sms chat fax twitter status twitter direct-message facebook feed post facebook feed comment telegram personal-message]
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: LLM_INJECTION_ALLOWLIST
          - Deleted property: LLM_CHAT_STORAGE_ENABLED
          - Modified property: DEFAULT_IDP
            - Property 'OneOf' changed
              - Schemas added: #/components/schemas/DEFAULTIDPEnum, #/components/schemas/BlankEnum
            - Type changed from 'string' to ''
          - Modified property: DEFAULT_OFFERING_USER_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Schemas added: #/components/schemas/UserAttributeEnum, #/components/schemas/BlankEnum
              - Type changed from 'string' to ''
              - MinLength changed from 1 to 0
          - Modified property: DISABLED_OFFERING_TYPES
            - Items changed
              - Property 'OneOf' changed
                - Schemas added: #/components/schemas/OfferingTypeEnum, #/components/schemas/BlankEnum
              - Type changed from 'string' to ''
              - MinLength changed from 1 to 0
          - Modified property: ENABLED_USER_PROFILE_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Schemas added: #/components/schemas/UserAttributeEnum, #/components/schemas/BlankEnum
              - Type changed from 'string' to ''
              - MinLength changed from 1 to 0
          - Modified property: FEDERATED_IDENTITY_DEACTIVATION_POLICY
            - New enum values: [all_isds_removed any_isd_removed]
          - Modified property: FEDERATED_IDENTITY_SYNC_ALLOWED_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Schemas added: #/components/schemas/UserAttributeEnum, #/components/schemas/BlankEnum
              - Type changed from 'string' to ''
              - MinLength changed from 1 to 0
          - Modified property: FONT_FAMILY
            - New enum values: [Inter Maven Pro]
          - Modified property: INVITATION_ALLOWED_FIELDS
            - Items changed
              - Property 'OneOf' changed
                - Schemas added: #/components/schemas/UserAttributeEnum, #/components/schemas/BlankEnum
              - Type changed from 'string' to ''
              - MinLength changed from 1 to 0
          - Modified property: LOGIN_PAGE_LAYOUT
            - New enum values: [split-screen centered-card minimal full-hero gradient stacked right-split glassmorphism neumorphism animated-gradient video-background bottom-sheet tabbed wizard stats news carousel logo-watermark brand-pattern duotone diagonal time-based seasonal weather]
          - Modified property: MAINTENANCE_ANNOUNCEMENT_NOTIFY_SYSTEM
            - Items changed
              - Property 'OneOf' changed
                - Schemas added: #/components/schemas/NotifySystemEnum, #/components/schemas/BlankEnum
              - Type changed from 'string' to ''
              - MinLength changed from 1 to 0
          - Modified property: MANDATORY_USER_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Schemas added: #/components/schemas/UserAttributeEnum, #/components/schemas/BlankEnum
              - Type changed from 'string' to ''
              - MinLength changed from 1 to 0
          - Modified property: ONBOARDING_VALIDATION_METHODS
            - Items changed
              - Property 'OneOf' changed
                - Schemas added: #/components/schemas/OnboardingValidationEnum, #/components/schemas/BlankEnum
              - Type changed from 'string' to ''
              - MinLength changed from 1 to 0
          - Modified property: RESTRICTED_OFFERING_VISIBILITY_MODE
            - New enum values: [show_all show_restricted_disabled hide_inaccessible require_membership]
          - Modified property: SCRIPT_RUN_MODE
            - New enum values: [docker k8s]
          - Modified property: SIDEBAR_STYLE
            - New enum values: [primary accent accent-light dark light auto]
          - Modified property: WALDUR_SUPPORT_ACTIVE_BACKEND_TYPE
            - New enum values: [atlassian zammad smax]
          - Modified property: ZAMMAD_ARTICLE_TYPE
            - New enum values: [email phone web note sms chat fax twitter status twitter direct-message facebook feed post facebook feed comment telegram personal-message]

GET /api/promotions-campaigns/{uuid}/resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: current_usages
                - Description changed from '' to 'Dictionary mapping component types to their latest reported usage amounts.'
                - AdditionalProperties changed
                  - Type changed from 'integer' to 'number'
                  - Format changed from '' to 'double'
              - Modified property: is_limit_based
                - Description changed from '' to 'Returns True if the resource has limit-based components with user-adjustable quotas.'
              - Modified property: is_usage_based
                - Description changed from '' to 'Returns True if the resource has usage-based components that track variable consumption.'
              - Modified property: limit_usage
                - Description changed from '' to 'Dictionary mapping limit-based component types to their consumed usage. For monthly periods, maps from current_usages; for longer periods, aggregates historical usage.'
