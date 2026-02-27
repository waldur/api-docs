# OpenAPI schema diff - 8.0.2

## For version 8.0.2

### New Endpoints: 40

---------------------
GET /api/chat-messages/  
HEAD /api/chat-messages/  
POST /api/chat-messages/  
GET /api/chat-messages/{uuid}/  
POST /api/chat-messages/{uuid}/edit/  
GET /api/chat-messages/{uuid}/history/  
GET /api/chat-sessions/  
HEAD /api/chat-sessions/  
GET /api/chat-sessions/current/  
HEAD /api/chat-sessions/current/  
GET /api/chat-sessions/{uuid}/  
GET /api/chat-threads/  
HEAD /api/chat-threads/  
POST /api/chat-threads/  
GET /api/chat-threads/{uuid}/  
PATCH /api/chat-threads/{uuid}/  
PUT /api/chat-threads/{uuid}/  
POST /api/chat-threads/{uuid}/archive/  
POST /api/chat-threads/{uuid}/unarchive/  
POST /api/customers/{uuid}/contact/  
GET /api/marketplace-software-catalogs/discover/  
HEAD /api/marketplace-software-catalogs/discover/  
POST /api/marketplace-software-catalogs/import_catalog/  
POST /api/marketplace-software-catalogs/{uuid}/update_catalog/  
GET /api/openstack-external-networks/  
HEAD /api/openstack-external-networks/  
GET /api/openstack-external-networks/{uuid}/  
GET /api/openstack/discovery/  
POST /api/openstack/discovery/  
POST /api/openstack/discovery/discover_external_networks/  
POST /api/openstack/discovery/discover_flavors/  
POST /api/openstack/discovery/discover_instance_availability_zones/  
POST /api/openstack/discovery/discover_volume_availability_zones/  
POST /api/openstack/discovery/discover_volume_types/  
POST /api/openstack/discovery/preview_service_attributes/  
POST /api/openstack/discovery/validate_credentials/  
DELETE /api/openstack/discovery/{id}/  
GET /api/openstack/discovery/{id}/  
PATCH /api/openstack/discovery/{id}/  
PUT /api/openstack/discovery/{id}/  

### Deleted Endpoints: None

---------------------------

### Modified Endpoints: 80

--------------------------
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
                      - New property: disabled_resource_actions
                      - Modified property: latest_date_for_resource_termination
                        - Format changed from 'date' to ''
                        - Description changed from 'If set, it will be used as a latest date for resource termination' to 'If set, it will be used as a latest date for resource termination. Format: YYYY-MM-DD'
              - Modified property: software_catalogs
                - Items changed
                  - Properties changed
                    - Modified property: catalog
                      - Property 'AllOf' changed
                        - Schemas added: #/components/schemas/CatalogSummary
                      - Type changed from 'object' to ''
                      - Properties changed
                        - Deleted property: description
                        - Deleted property: name
                        - Deleted property: uuid
                        - Deleted property: version
                    - Modified property: partition
                      - Property 'AllOf' changed
                        - Schemas added: #/components/schemas/PartitionSummary
                      - Type changed from 'object' to ''
                      - Nullable changed from false to true
                      - Properties changed
                        - Deleted property: partition_name
                        - Deleted property: priority_tier
                        - Deleted property: qos
                        - Deleted property: uuid

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
                    - New property: disabled_resource_actions
                    - Modified property: latest_date_for_resource_termination
                      - Format changed from 'date' to ''
                      - Description changed from 'If set, it will be used as a latest date for resource termination' to 'If set, it will be used as a latest date for resource termination. Format: YYYY-MM-DD'
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: catalog
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/CatalogSummary
                    - Type changed from 'object' to ''
                    - Properties changed
                      - Deleted property: description
                      - Deleted property: name
                      - Deleted property: uuid
                      - Deleted property: version
                  - Modified property: partition
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/PartitionSummary
                    - Type changed from 'object' to ''
                    - Nullable changed from false to true
                    - Properties changed
                      - Deleted property: partition_name
                      - Deleted property: priority_tier
                      - Deleted property: qos
                      - Deleted property: uuid

POST /api/chat/stream/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: thread_uuid
          - New property: update_thread_name

GET /api/customers/

- New query param: current_user_has_project_create_permission

HEAD /api/customers/

- New query param: current_user_has_project_create_permission

GET /api/customers/countries/

- New query param: current_user_has_project_create_permission

HEAD /api/customers/countries/

- New query param: current_user_has_project_create_permission

GET /api/customers/{uuid}/history/

- New query param: current_user_has_project_create_permission

GET /api/financial-reports/

- New query param: current_user_has_project_create_permission

HEAD /api/financial-reports/

- New query param: current_user_has_project_create_permission

GET /api/hooks-email/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: event_groups
                - Items changed
                  - New enum values: [chat onboarding]
              - Modified property: event_types
                - Items changed
                  - New enum values: [chat_session_accessed chat_thread_accessed onboarding_verification_deleted onboarding_verification_deleted_by_task]

POST /api/hooks-email/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_groups
            - Items changed
              - New enum values: [chat onboarding]
          - Modified property: event_types
            - Items changed
              - New enum values: [chat_session_accessed chat_thread_accessed onboarding_verification_deleted onboarding_verification_deleted_by_task]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [chat onboarding]
            - Modified property: event_types
              - Items changed
                - New enum values: [chat_session_accessed chat_thread_accessed onboarding_verification_deleted onboarding_verification_deleted_by_task]

GET /api/hooks-email/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [chat onboarding]
            - Modified property: event_types
              - Items changed
                - New enum values: [chat_session_accessed chat_thread_accessed onboarding_verification_deleted onboarding_verification_deleted_by_task]

PATCH /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_groups
            - Items changed
              - New enum values: [chat onboarding]
          - Modified property: event_types
            - Items changed
              - New enum values: [chat_session_accessed chat_thread_accessed onboarding_verification_deleted onboarding_verification_deleted_by_task]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [chat onboarding]
            - Modified property: event_types
              - Items changed
                - New enum values: [chat_session_accessed chat_thread_accessed onboarding_verification_deleted onboarding_verification_deleted_by_task]

PUT /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_groups
            - Items changed
              - New enum values: [chat onboarding]
          - Modified property: event_types
            - Items changed
              - New enum values: [chat_session_accessed chat_thread_accessed onboarding_verification_deleted onboarding_verification_deleted_by_task]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [chat onboarding]
            - Modified property: event_types
              - Items changed
                - New enum values: [chat_session_accessed chat_thread_accessed onboarding_verification_deleted onboarding_verification_deleted_by_task]

GET /api/hooks-web/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: event_groups
                - Items changed
                  - New enum values: [chat onboarding]
              - Modified property: event_types
                - Items changed
                  - New enum values: [chat_session_accessed chat_thread_accessed onboarding_verification_deleted onboarding_verification_deleted_by_task]

POST /api/hooks-web/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_groups
            - Items changed
              - New enum values: [chat onboarding]
          - Modified property: event_types
            - Items changed
              - New enum values: [chat_session_accessed chat_thread_accessed onboarding_verification_deleted onboarding_verification_deleted_by_task]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [chat onboarding]
            - Modified property: event_types
              - Items changed
                - New enum values: [chat_session_accessed chat_thread_accessed onboarding_verification_deleted onboarding_verification_deleted_by_task]

GET /api/hooks-web/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [chat onboarding]
            - Modified property: event_types
              - Items changed
                - New enum values: [chat_session_accessed chat_thread_accessed onboarding_verification_deleted onboarding_verification_deleted_by_task]

PATCH /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_groups
            - Items changed
              - New enum values: [chat onboarding]
          - Modified property: event_types
            - Items changed
              - New enum values: [chat_session_accessed chat_thread_accessed onboarding_verification_deleted onboarding_verification_deleted_by_task]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [chat onboarding]
            - Modified property: event_types
              - Items changed
                - New enum values: [chat_session_accessed chat_thread_accessed onboarding_verification_deleted onboarding_verification_deleted_by_task]

PUT /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_groups
            - Items changed
              - New enum values: [chat onboarding]
          - Modified property: event_types
            - Items changed
              - New enum values: [chat_session_accessed chat_thread_accessed onboarding_verification_deleted onboarding_verification_deleted_by_task]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [chat onboarding]
            - Modified property: event_types
              - Items changed
                - New enum values: [chat_session_accessed chat_thread_accessed onboarding_verification_deleted onboarding_verification_deleted_by_task]

GET /api/invoices/

- Modified query param: state
  - Schema changed
    - Items changed
      - New enum values: [pending_finalization]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: state
                - New enum values: [pending_finalization]

HEAD /api/invoices/

- Modified query param: state
  - Schema changed
    - Items changed
      - New enum values: [pending_finalization]

GET /api/invoices/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - New enum values: [pending_finalization]

GET /api/invoices/{uuid}/history/

- Modified query param: state
  - Schema changed
    - Items changed
      - New enum values: [pending_finalization]

POST /api/invoices/{uuid}/paid/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - New enum values: [pending_finalization]

GET /api/invoices/{uuid}/stats/

- Modified query param: state
  - Schema changed
    - Items changed
      - New enum values: [pending_finalization]

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
                    - New property: disabled_resource_actions
                    - Modified property: latest_date_for_resource_termination
                      - Format changed from 'date' to ''
                      - Description changed from 'If set, it will be used as a latest date for resource termination' to 'If set, it will be used as a latest date for resource termination. Format: YYYY-MM-DD'
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: catalog
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/CatalogSummary
                    - Type changed from 'object' to ''
                    - Properties changed
                      - Deleted property: description
                      - Deleted property: name
                      - Deleted property: uuid
                      - Deleted property: version
                  - Modified property: partition
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/PartitionSummary
                    - Type changed from 'object' to ''
                    - Nullable changed from false to true
                    - Properties changed
                      - Deleted property: partition_name
                      - Deleted property: priority_tier
                      - Deleted property: qos
                      - Deleted property: uuid

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
                      - New property: disabled_resource_actions
                      - Modified property: latest_date_for_resource_termination
                        - Format changed from 'date' to ''
                        - Description changed from 'If set, it will be used as a latest date for resource termination' to 'If set, it will be used as a latest date for resource termination. Format: YYYY-MM-DD'
              - Modified property: software_catalogs
                - Items changed
                  - Properties changed
                    - Modified property: catalog
                      - Property 'AllOf' changed
                        - Schemas added: #/components/schemas/CatalogSummary
                      - Type changed from 'object' to ''
                      - Properties changed
                        - Deleted property: description
                        - Deleted property: name
                        - Deleted property: uuid
                        - Deleted property: version
                    - Modified property: partition
                      - Property 'AllOf' changed
                        - Schemas added: #/components/schemas/PartitionSummary
                      - Type changed from 'object' to ''
                      - Nullable changed from false to true
                      - Properties changed
                        - Deleted property: partition_name
                        - Deleted property: priority_tier
                        - Deleted property: qos
                        - Deleted property: uuid

POST /api/marketplace-provider-offerings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: disabled_resource_actions
              - Modified property: latest_date_for_resource_termination
                - Format changed from 'date' to ''
                - Description changed from 'If set, it will be used as a latest date for resource termination' to 'If set, it will be used as a latest date for resource termination. Format: YYYY-MM-DD'
                - MinLength changed from 0 to 1
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: disabled_resource_actions
              - Modified property: latest_date_for_resource_termination
                - Format changed from 'date' to ''
                - Description changed from 'If set, it will be used as a latest date for resource termination' to 'If set, it will be used as a latest date for resource termination. Format: YYYY-MM-DD'
                - MinLength changed from 0 to 1
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: disabled_resource_actions
              - Modified property: latest_date_for_resource_termination
                - Format changed from 'date' to ''
                - Description changed from 'If set, it will be used as a latest date for resource termination' to 'If set, it will be used as a latest date for resource termination. Format: YYYY-MM-DD'
                - MinLength changed from 0 to 1
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
                    - New property: disabled_resource_actions
                    - Modified property: latest_date_for_resource_termination
                      - Format changed from 'date' to ''
                      - Description changed from 'If set, it will be used as a latest date for resource termination' to 'If set, it will be used as a latest date for resource termination. Format: YYYY-MM-DD'
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: catalog
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/CatalogSummary
                    - Type changed from 'object' to ''
                    - Properties changed
                      - Deleted property: description
                      - Deleted property: name
                      - Deleted property: uuid
                      - Deleted property: version
                  - Modified property: partition
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/PartitionSummary
                    - Type changed from 'object' to ''
                    - Nullable changed from false to true
                    - Properties changed
                      - Deleted property: partition_name
                      - Deleted property: priority_tier
                      - Deleted property: qos
                      - Deleted property: uuid

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
                    - New property: disabled_resource_actions
                    - Modified property: latest_date_for_resource_termination
                      - Format changed from 'date' to ''
                      - Description changed from 'If set, it will be used as a latest date for resource termination' to 'If set, it will be used as a latest date for resource termination. Format: YYYY-MM-DD'
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: catalog
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/CatalogSummary
                    - Type changed from 'object' to ''
                    - Properties changed
                      - Deleted property: description
                      - Deleted property: name
                      - Deleted property: uuid
                      - Deleted property: version
                  - Modified property: partition
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/PartitionSummary
                    - Type changed from 'object' to ''
                    - Nullable changed from false to true
                    - Properties changed
                      - Deleted property: partition_name
                      - Deleted property: priority_tier
                      - Deleted property: qos
                      - Deleted property: uuid

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
                    - New property: disabled_resource_actions
                    - Modified property: latest_date_for_resource_termination
                      - Format changed from 'date' to ''
                      - Description changed from 'If set, it will be used as a latest date for resource termination' to 'If set, it will be used as a latest date for resource termination. Format: YYYY-MM-DD'
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: catalog
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/CatalogSummary
                    - Type changed from 'object' to ''
                    - Properties changed
                      - Deleted property: description
                      - Deleted property: name
                      - Deleted property: uuid
                      - Deleted property: version
                  - Modified property: partition
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/PartitionSummary
                    - Type changed from 'object' to ''
                    - Nullable changed from false to true
                    - Properties changed
                      - Deleted property: partition_name
                      - Deleted property: priority_tier
                      - Deleted property: qos
                      - Deleted property: uuid

POST /api/marketplace-provider-offerings/{uuid}/update_integration/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: disabled_resource_actions
              - Modified property: latest_date_for_resource_termination
                - Format changed from 'date' to ''
                - Description changed from 'If set, it will be used as a latest date for resource termination' to 'If set, it will be used as a latest date for resource termination. Format: YYYY-MM-DD'
                - MinLength changed from 0 to 1

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
                    - New property: disabled_resource_actions
                    - Modified property: latest_date_for_resource_termination
                      - Format changed from 'date' to ''
                      - Description changed from 'If set, it will be used as a latest date for resource termination' to 'If set, it will be used as a latest date for resource termination. Format: YYYY-MM-DD'
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: catalog
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/CatalogSummary
                    - Type changed from 'object' to ''
                    - Properties changed
                      - Deleted property: description
                      - Deleted property: name
                      - Deleted property: uuid
                      - Deleted property: version
                  - Modified property: partition
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/PartitionSummary
                    - Type changed from 'object' to ''
                    - Nullable changed from false to true
                    - Properties changed
                      - Deleted property: partition_name
                      - Deleted property: priority_tier
                      - Deleted property: qos
                      - Deleted property: uuid

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
                    - New property: disabled_resource_actions
                    - Modified property: latest_date_for_resource_termination
                      - Format changed from 'date' to ''
                      - Description changed from 'If set, it will be used as a latest date for resource termination' to 'If set, it will be used as a latest date for resource termination. Format: YYYY-MM-DD'
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: catalog
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/CatalogSummary
                    - Type changed from 'object' to ''
                    - Properties changed
                      - Deleted property: description
                      - Deleted property: name
                      - Deleted property: uuid
                      - Deleted property: version
                  - Modified property: partition
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/PartitionSummary
                    - Type changed from 'object' to ''
                    - Nullable changed from false to true
                    - Properties changed
                      - Deleted property: partition_name
                      - Deleted property: priority_tier
                      - Deleted property: qos
                      - Deleted property: uuid

POST /api/marketplace-provider-resources/{uuid}/update_options/

- Responses changed
  - New response: 409

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
                      - New property: disabled_resource_actions
                      - Modified property: latest_date_for_resource_termination
                        - Format changed from 'date' to ''
                        - Description changed from 'If set, it will be used as a latest date for resource termination' to 'If set, it will be used as a latest date for resource termination. Format: YYYY-MM-DD'
              - Modified property: software_catalogs
                - Items changed
                  - Properties changed
                    - Modified property: catalog
                      - Property 'AllOf' changed
                        - Schemas added: #/components/schemas/CatalogSummary
                      - Type changed from 'object' to ''
                      - Properties changed
                        - Deleted property: description
                        - Deleted property: name
                        - Deleted property: uuid
                        - Deleted property: version
                    - Modified property: partition
                      - Property 'AllOf' changed
                        - Schemas added: #/components/schemas/PartitionSummary
                      - Type changed from 'object' to ''
                      - Nullable changed from false to true
                      - Properties changed
                        - Deleted property: partition_name
                        - Deleted property: priority_tier
                        - Deleted property: qos
                        - Deleted property: uuid

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
                    - New property: disabled_resource_actions
                    - Modified property: latest_date_for_resource_termination
                      - Format changed from 'date' to ''
                      - Description changed from 'If set, it will be used as a latest date for resource termination' to 'If set, it will be used as a latest date for resource termination. Format: YYYY-MM-DD'
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: catalog
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/CatalogSummary
                    - Type changed from 'object' to ''
                    - Properties changed
                      - Deleted property: description
                      - Deleted property: name
                      - Deleted property: uuid
                      - Deleted property: version
                  - Modified property: partition
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/PartitionSummary
                    - Type changed from 'object' to ''
                    - Nullable changed from false to true
                    - Properties changed
                      - Deleted property: partition_name
                      - Deleted property: priority_tier
                      - Deleted property: qos
                      - Deleted property: uuid

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
                    - New property: disabled_resource_actions
                    - Modified property: latest_date_for_resource_termination
                      - Format changed from 'date' to ''
                      - Description changed from 'If set, it will be used as a latest date for resource termination' to 'If set, it will be used as a latest date for resource termination. Format: YYYY-MM-DD'
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: catalog
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/CatalogSummary
                    - Type changed from 'object' to ''
                    - Properties changed
                      - Deleted property: description
                      - Deleted property: name
                      - Deleted property: uuid
                      - Deleted property: version
                  - Modified property: partition
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/PartitionSummary
                    - Type changed from 'object' to ''
                    - Nullable changed from false to true
                    - Properties changed
                      - Deleted property: partition_name
                      - Deleted property: priority_tier
                      - Deleted property: qos
                      - Deleted property: uuid

POST /api/marketplace-resources/{uuid}/update_options/

- Responses changed
  - New response: 409

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
                      - New property: disabled_resource_actions
                      - Modified property: latest_date_for_resource_termination
                        - Format changed from 'date' to ''
                        - Description changed from 'If set, it will be used as a latest date for resource termination' to 'If set, it will be used as a latest date for resource termination. Format: YYYY-MM-DD'

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
                    - New property: disabled_resource_actions
                    - Modified property: latest_date_for_resource_termination
                      - Format changed from 'date' to ''
                      - Description changed from 'If set, it will be used as a latest date for resource termination' to 'If set, it will be used as a latest date for resource termination. Format: YYYY-MM-DD'

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
                    - New property: disabled_resource_actions
                    - Modified property: latest_date_for_resource_termination
                      - Format changed from 'date' to ''
                      - Description changed from 'If set, it will be used as a latest date for resource termination' to 'If set, it will be used as a latest date for resource termination. Format: YYYY-MM-DD'

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
                    - New property: disabled_resource_actions
                    - Modified property: latest_date_for_resource_termination
                      - Format changed from 'date' to ''
                      - Description changed from 'If set, it will be used as a latest date for resource termination' to 'If set, it will be used as a latest date for resource termination. Format: YYYY-MM-DD'

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
                    - New property: disabled_resource_actions
                    - Modified property: latest_date_for_resource_termination
                      - Format changed from 'date' to ''
                      - Description changed from 'If set, it will be used as a latest date for resource termination' to 'If set, it will be used as a latest date for resource termination. Format: YYYY-MM-DD'

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
                    - New property: disabled_resource_actions
                    - Modified property: latest_date_for_resource_termination
                      - Format changed from 'date' to ''
                      - Description changed from 'If set, it will be used as a latest date for resource termination' to 'If set, it will be used as a latest date for resource termination. Format: YYYY-MM-DD'

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
                    - New property: disabled_resource_actions
                    - Modified property: latest_date_for_resource_termination
                      - Format changed from 'date' to ''
                      - Description changed from 'If set, it will be used as a latest date for resource termination' to 'If set, it will be used as a latest date for resource termination. Format: YYYY-MM-DD'

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
                    - New property: disabled_resource_actions
                    - Modified property: latest_date_for_resource_termination
                      - Format changed from 'date' to ''
                      - Description changed from 'If set, it will be used as a latest date for resource termination' to 'If set, it will be used as a latest date for resource termination. Format: YYYY-MM-DD'
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: catalog
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/CatalogSummary
                    - Type changed from 'object' to ''
                    - Properties changed
                      - Deleted property: description
                      - Deleted property: name
                      - Deleted property: uuid
                      - Deleted property: version
                  - Modified property: partition
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/PartitionSummary
                    - Type changed from 'object' to ''
                    - Nullable changed from false to true
                    - Properties changed
                      - Deleted property: partition_name
                      - Deleted property: priority_tier
                      - Deleted property: qos
                      - Deleted property: uuid

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
                    - New property: disabled_resource_actions
                    - Modified property: latest_date_for_resource_termination
                      - Format changed from 'date' to ''
                      - Description changed from 'If set, it will be used as a latest date for resource termination' to 'If set, it will be used as a latest date for resource termination. Format: YYYY-MM-DD'
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: catalog
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/CatalogSummary
                    - Type changed from 'object' to ''
                    - Properties changed
                      - Deleted property: description
                      - Deleted property: name
                      - Deleted property: uuid
                      - Deleted property: version
                  - Modified property: partition
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/PartitionSummary
                    - Type changed from 'object' to ''
                    - Nullable changed from false to true
                    - Properties changed
                      - Deleted property: partition_name
                      - Deleted property: priority_tier
                      - Deleted property: qos
                      - Deleted property: uuid

GET /api/marketplace-service-providers/{service_provider_uuid}/customers/

- New query param: current_user_has_project_create_permission

GET /api/marketplace-service-providers/{service_provider_uuid}/user_customers/

- New query param: current_user_has_project_create_permission

GET /api/marketplace-slurm-periodic-usage-policies/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: warnings
            - Properties changed
              - New property: warnings

POST /api/marketplace-slurm-periodic-usage-policies/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: warnings
          - Properties changed
            - New property: warnings

GET /api/marketplace-slurm-periodic-usage-policies/actions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: warnings
          - Properties changed
            - New property: warnings

GET /api/marketplace-slurm-periodic-usage-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: warnings
          - Properties changed
            - New property: warnings

PATCH /api/marketplace-slurm-periodic-usage-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: warnings
          - Properties changed
            - New property: warnings

PUT /api/marketplace-slurm-periodic-usage-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: warnings
          - Properties changed
            - New property: warnings

GET /api/marketplace-software-catalogs/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: target_count
              - New required property: version_count
            - Properties changed
              - New property: target_count
              - New property: version_count

POST /api/marketplace-software-catalogs/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: target_count
            - New required property: version_count
          - Properties changed
            - New property: target_count
            - New property: version_count

GET /api/marketplace-software-catalogs/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: target_count
            - New required property: version_count
          - Properties changed
            - New property: target_count
            - New property: version_count

PATCH /api/marketplace-software-catalogs/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: target_count
            - New required property: version_count
          - Properties changed
            - New property: target_count
            - New property: version_count

PUT /api/marketplace-software-catalogs/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: target_count
            - New required property: version_count
          - Properties changed
            - New property: target_count
            - New property: version_count

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
                  - New enum values: [chat_session_accessed chat_thread_accessed onboarding_verification_deleted onboarding_verification_deleted_by_task]

GET /api/metadata/permissions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: permission_map
              - AdditionalProperties changed
                - New enum values: [CUSTOMER.CONTACT_UPDATE]
            - Modified property: permissions
              - AdditionalProperties changed
                - New enum values: [CUSTOMER.CONTACT_UPDATE]

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
                                    - New property: disabled_resource_actions
                                    - Modified property: latest_date_for_resource_termination
                                      - Format changed from 'date' to ''
                                      - Description changed from 'If set, it will be used as a latest date for resource termination' to 'If set, it will be used as a latest date for resource termination. Format: YYYY-MM-DD'
                            - Modified property: software_catalogs
                              - Items changed
                                - Properties changed
                                  - Modified property: catalog
                                    - Property 'AllOf' changed
                                      - Schemas added: #/components/schemas/CatalogSummary
                                    - Type changed from 'object' to ''
                                    - Properties changed
                                      - Deleted property: description
                                      - Deleted property: name
                                      - Deleted property: uuid
                                      - Deleted property: version
                                  - Modified property: partition
                                    - Property 'AllOf' changed
                                      - Schemas added: #/components/schemas/PartitionSummary
                                    - Type changed from 'object' to ''
                                    - Nullable changed from false to true
                                    - Properties changed
                                      - Deleted property: partition_name
                                      - Deleted property: priority_tier
                                      - Deleted property: qos
                                      - Deleted property: uuid

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
                                  - New property: disabled_resource_actions
                                  - Modified property: latest_date_for_resource_termination
                                    - Format changed from 'date' to ''
                                    - Description changed from 'If set, it will be used as a latest date for resource termination' to 'If set, it will be used as a latest date for resource termination. Format: YYYY-MM-DD'
                          - Modified property: software_catalogs
                            - Items changed
                              - Properties changed
                                - Modified property: catalog
                                  - Property 'AllOf' changed
                                    - Schemas added: #/components/schemas/CatalogSummary
                                  - Type changed from 'object' to ''
                                  - Properties changed
                                    - Deleted property: description
                                    - Deleted property: name
                                    - Deleted property: uuid
                                    - Deleted property: version
                                - Modified property: partition
                                  - Property 'AllOf' changed
                                    - Schemas added: #/components/schemas/PartitionSummary
                                  - Type changed from 'object' to ''
                                  - Nullable changed from false to true
                                  - Properties changed
                                    - Deleted property: partition_name
                                    - Deleted property: priority_tier
                                    - Deleted property: qos
                                    - Deleted property: uuid

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
                            - New property: disabled_resource_actions
                            - Modified property: latest_date_for_resource_termination
                              - Format changed from 'date' to ''
                              - Description changed from 'If set, it will be used as a latest date for resource termination' to 'If set, it will be used as a latest date for resource termination. Format: YYYY-MM-DD'
                    - Modified property: software_catalogs
                      - Items changed
                        - Properties changed
                          - Modified property: catalog
                            - Property 'AllOf' changed
                              - Schemas added: #/components/schemas/CatalogSummary
                            - Type changed from 'object' to ''
                            - Properties changed
                              - Deleted property: description
                              - Deleted property: name
                              - Deleted property: uuid
                              - Deleted property: version
                          - Modified property: partition
                            - Property 'AllOf' changed
                              - Schemas added: #/components/schemas/PartitionSummary
                            - Type changed from 'object' to ''
                            - Nullable changed from false to true
                            - Properties changed
                              - Deleted property: partition_name
                              - Deleted property: priority_tier
                              - Deleted property: qos
                              - Deleted property: uuid

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
                          - New property: disabled_resource_actions
                          - Modified property: latest_date_for_resource_termination
                            - Format changed from 'date' to ''
                            - Description changed from 'If set, it will be used as a latest date for resource termination' to 'If set, it will be used as a latest date for resource termination. Format: YYYY-MM-DD'
                  - Modified property: software_catalogs
                    - Items changed
                      - Properties changed
                        - Modified property: catalog
                          - Property 'AllOf' changed
                            - Schemas added: #/components/schemas/CatalogSummary
                          - Type changed from 'object' to ''
                          - Properties changed
                            - Deleted property: description
                            - Deleted property: name
                            - Deleted property: uuid
                            - Deleted property: version
                        - Modified property: partition
                          - Property 'AllOf' changed
                            - Schemas added: #/components/schemas/PartitionSummary
                          - Type changed from 'object' to ''
                          - Nullable changed from false to true
                          - Properties changed
                            - Deleted property: partition_name
                            - Deleted property: priority_tier
                            - Deleted property: qos
                            - Deleted property: uuid

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
                          - New property: disabled_resource_actions
                          - Modified property: latest_date_for_resource_termination
                            - Format changed from 'date' to ''
                            - Description changed from 'If set, it will be used as a latest date for resource termination' to 'If set, it will be used as a latest date for resource termination. Format: YYYY-MM-DD'
                  - Modified property: software_catalogs
                    - Items changed
                      - Properties changed
                        - Modified property: catalog
                          - Property 'AllOf' changed
                            - Schemas added: #/components/schemas/CatalogSummary
                          - Type changed from 'object' to ''
                          - Properties changed
                            - Deleted property: description
                            - Deleted property: name
                            - Deleted property: uuid
                            - Deleted property: version
                        - Modified property: partition
                          - Property 'AllOf' changed
                            - Schemas added: #/components/schemas/PartitionSummary
                          - Type changed from 'object' to ''
                          - Nullable changed from false to true
                          - Properties changed
                            - Deleted property: partition_name
                            - Deleted property: priority_tier
                            - Deleted property: qos
                            - Deleted property: uuid

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
                          - New property: disabled_resource_actions
                          - Modified property: latest_date_for_resource_termination
                            - Format changed from 'date' to ''
                            - Description changed from 'If set, it will be used as a latest date for resource termination' to 'If set, it will be used as a latest date for resource termination. Format: YYYY-MM-DD'
                  - Modified property: software_catalogs
                    - Items changed
                      - Properties changed
                        - Modified property: catalog
                          - Property 'AllOf' changed
                            - Schemas added: #/components/schemas/CatalogSummary
                          - Type changed from 'object' to ''
                          - Properties changed
                            - Deleted property: description
                            - Deleted property: name
                            - Deleted property: uuid
                            - Deleted property: version
                        - Modified property: partition
                          - Property 'AllOf' changed
                            - Schemas added: #/components/schemas/PartitionSummary
                          - Type changed from 'object' to ''
                          - Nullable changed from false to true
                          - Properties changed
                            - Deleted property: partition_name
                            - Deleted property: priority_tier
                            - Deleted property: qos
                            - Deleted property: uuid

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
                          - New property: disabled_resource_actions
                          - Modified property: latest_date_for_resource_termination
                            - Format changed from 'date' to ''
                            - Description changed from 'If set, it will be used as a latest date for resource termination' to 'If set, it will be used as a latest date for resource termination. Format: YYYY-MM-DD'
                  - Modified property: software_catalogs
                    - Items changed
                      - Properties changed
                        - Modified property: catalog
                          - Property 'AllOf' changed
                            - Schemas added: #/components/schemas/CatalogSummary
                          - Type changed from 'object' to ''
                          - Properties changed
                            - Deleted property: description
                            - Deleted property: name
                            - Deleted property: uuid
                            - Deleted property: version
                        - Modified property: partition
                          - Property 'AllOf' changed
                            - Schemas added: #/components/schemas/PartitionSummary
                          - Type changed from 'object' to ''
                          - Nullable changed from false to true
                          - Properties changed
                            - Deleted property: partition_name
                            - Deleted property: priority_tier
                            - Deleted property: qos
                            - Deleted property: uuid

POST /api/openportal-unmanaged-projects/{uuid}/move_project/

- Description changed from 'Moves a project and its associated resources to a different customer. This is a staff-only action. You can choose whether to preserve existing project permissions for users. Terminated projects can also be moved.' to 'Moves a project and its associated resources to a different customer. You can choose whether to preserve existing project permissions for users. Terminated projects can also be moved.'

GET /api/openstack-tenants/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [external_network_ref_name external_network_ref_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: external_network_ref_name
              - New property: external_network_ref_uuid

GET /api/openstack-tenants/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [external_network_ref_name external_network_ref_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: external_network_ref_name
            - New property: external_network_ref_uuid

PATCH /api/openstack-tenants/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: external_network_ref_name
            - New property: external_network_ref_uuid

PUT /api/openstack-tenants/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: external_network_ref_name
            - New property: external_network_ref_uuid

POST /api/openstack-tenants/{uuid}/pull_security_groups/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: external_network_ref_name
            - New property: external_network_ref_uuid

POST /api/openstack-tenants/{uuid}/pull_server_groups/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: external_network_ref_name
            - New property: external_network_ref_uuid

GET /api/override-settings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: LLM_CHAT_SESSION_RETENTION_DAYS
            - New property: LLM_CHAT_STORAGE_ENABLED

POST /api/override-settings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: LLM_CHAT_SESSION_RETENTION_DAYS
          - New property: LLM_CHAT_STORAGE_ENABLED
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: LLM_CHAT_SESSION_RETENTION_DAYS
          - New property: LLM_CHAT_STORAGE_ENABLED
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: LLM_CHAT_SESSION_RETENTION_DAYS
          - New property: LLM_CHAT_STORAGE_ENABLED

POST /api/projects/{uuid}/move_project/

- Description changed from 'Moves a project and its associated resources to a different customer. This is a staff-only action. You can choose whether to preserve existing project permissions for users. Terminated projects can also be moved.' to 'Moves a project and its associated resources to a different customer. You can choose whether to preserve existing project permissions for users. Terminated projects can also be moved.'
