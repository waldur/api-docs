# OpenAPI schema diff - 8.0.3

## For version 8.0.3

### New Endpoints: 21

---------------------
POST /api/identity-bridge/  
POST /api/identity-bridge/remove/  
GET /api/identity-bridge/stats/  
POST /api/marketplace-orders/{uuid}/set_consumer_info/  
POST /api/marketplace-orders/{uuid}/set_provider_info/  
POST /api/marketplace-provider-offerings/{uuid}/update_backend_id_rules/  
POST /api/marketplace-provider-resources/{uuid}/set_state_ok/  
POST /api/marketplace-resources/{uuid}/estimate_renewal/  
GET /api/system-logs/  
HEAD /api/system-logs/  
GET /api/system-logs/instances/  
HEAD /api/system-logs/instances/  
GET /api/system-logs/stats/  
HEAD /api/system-logs/stats/  
GET /api/system-logs/{id}/  
PATCH /api/user-group-invitations/{uuid}/  
PUT /api/user-group-invitations/{uuid}/  
POST /api/user-invitations/check-duplicates/  
GET /api/users/{uuid}/identity_bridge_status/  
POST /api/users/{uuid}/send_notification/  
POST /api/users/{uuid}/update_actions/  

### Deleted Endpoints: 12

-------------------------
HEAD /api/chat-messages/  
POST /api/chat-messages/  
GET /api/chat-messages/{uuid}/  
GET /api/chat-messages/{uuid}/history/  
HEAD /api/chat-sessions/  
HEAD /api/chat-sessions/current/  
HEAD /api/chat-threads/  
POST /api/chat-threads/  
PATCH /api/chat-threads/{uuid}/  
PUT /api/chat-threads/{uuid}/  
PATCH /api/openstack-server-groups/{uuid}/  
PUT /api/openstack-server-groups/{uuid}/  

### Modified Endpoints: 114

---------------------------
POST /api/admin/arrow/billing-syncs/sync_resource_historical_consumption/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: dry_run
          - New property: force
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: dry_run
            - New property: periods_no_data
            - New property: preview_periods

POST /api/admin/arrow/billing-syncs/trigger_sync/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: resource_uuid

GET /api/admin/arrow/settings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: invoice_item_prefix

POST /api/admin/arrow/settings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: invoice_item_prefix
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: invoice_item_prefix

POST /api/admin/arrow/settings/discover_customers/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: export_types
          - Properties changed
            - New property: export_types

GET /api/admin/arrow/settings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: invoice_item_prefix

PATCH /api/admin/arrow/settings/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: invoice_item_prefix
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: invoice_item_prefix

PUT /api/admin/arrow/settings/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: invoice_item_prefix
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: invoice_item_prefix

GET /api/admin/arrow/vendor-offering-mappings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: plan_name
              - New required property: plan_uuid
            - Properties changed
              - New property: plan
              - New property: plan_name
              - New property: plan_uuid
              - Modified property: offering
                - Format changed from 'uri' to 'uuid'
                - Description changed from 'Waldur marketplace offering for this vendor' to ''

POST /api/admin/arrow/vendor-offering-mappings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: plan
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: plan_name
            - New required property: plan_uuid
          - Properties changed
            - New property: plan
            - New property: plan_name
            - New property: plan_uuid

GET /api/admin/arrow/vendor-offering-mappings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: plan_name
            - New required property: plan_uuid
          - Properties changed
            - New property: plan
            - New property: plan_name
            - New property: plan_uuid
            - Modified property: offering
              - Format changed from 'uri' to 'uuid'
              - Description changed from 'Waldur marketplace offering for this vendor' to ''

PATCH /api/admin/arrow/vendor-offering-mappings/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: plan
          - Modified property: offering
            - Format changed from 'uri' to 'uuid'
            - Description changed from 'Waldur marketplace offering for this vendor' to ''
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: plan_name
            - New required property: plan_uuid
          - Properties changed
            - New property: plan
            - New property: plan_name
            - New property: plan_uuid
            - Modified property: offering
              - Format changed from 'uri' to 'uuid'
              - Description changed from 'Waldur marketplace offering for this vendor' to ''

PUT /api/admin/arrow/vendor-offering-mappings/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: plan
          - Modified property: offering
            - Format changed from 'uri' to 'uuid'
            - Description changed from 'Waldur marketplace offering for this vendor' to ''
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: plan_name
            - New required property: plan_uuid
          - Properties changed
            - New property: plan
            - New property: plan_name
            - New property: plan_uuid
            - Modified property: offering
              - Format changed from 'uri' to 'uuid'
              - Description changed from 'Waldur marketplace offering for this vendor' to ''

POST /api/backend-resources/{uuid}/import_resource/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message
                    - New property: consumer_message_attachment
                    - New property: consumer_rejection_comment
                    - New property: created_by_email
                    - New property: created_by_organization
                    - New property: created_by_organization_registry_code
                    - New property: provider_message
                    - New property: provider_message_attachment
                    - New property: provider_message_url
                    - New property: provider_rejection_comment
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message
                    - New property: consumer_message_attachment
                    - New property: consumer_rejection_comment
                    - New property: created_by_email
                    - New property: created_by_organization
                    - New property: created_by_organization_registry_code
                    - New property: provider_message
                    - New property: provider_message_attachment
                    - New property: provider_message_url
                    - New property: provider_rejection_comment

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
                      - New property: enable_provider_consumer_messaging
                      - New property: notify_about_provider_consumer_messages
                      - New property: restrict_deletion_with_active_resources

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
                    - New property: enable_provider_consumer_messaging
                    - New property: notify_about_provider_consumer_messages
                    - New property: restrict_deletion_with_active_resources

GET /api/booking-resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: consumer_message
                      - New property: consumer_message_attachment
                      - New property: consumer_rejection_comment
                      - New property: created_by_email
                      - New property: created_by_organization
                      - New property: created_by_organization_registry_code
                      - New property: provider_message
                      - New property: provider_message_attachment
                      - New property: provider_message_url
                      - New property: provider_rejection_comment
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: consumer_message
                      - New property: consumer_message_attachment
                      - New property: consumer_rejection_comment
                      - New property: created_by_email
                      - New property: created_by_organization
                      - New property: created_by_organization_registry_code
                      - New property: provider_message
                      - New property: provider_message_attachment
                      - New property: provider_message_url
                      - New property: provider_rejection_comment

GET /api/booking-resources/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message
                    - New property: consumer_message_attachment
                    - New property: consumer_rejection_comment
                    - New property: created_by_email
                    - New property: created_by_organization
                    - New property: created_by_organization_registry_code
                    - New property: provider_message
                    - New property: provider_message_attachment
                    - New property: provider_message_url
                    - New property: provider_rejection_comment
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message
                    - New property: consumer_message_attachment
                    - New property: consumer_rejection_comment
                    - New property: created_by_email
                    - New property: created_by_organization
                    - New property: created_by_organization_registry_code
                    - New property: provider_message
                    - New property: provider_message_attachment
                    - New property: provider_message_url
                    - New property: provider_rejection_comment

GET /api/chat-messages/

- New query param: include_history
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: replaces
            - Properties changed
              - Modified property: replaces
                - Nullable changed from true to false
                - ReadOnly changed from false to true
              - Modified property: role
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/MessageRoleEnum
                - Type changed from 'string' to ''
                - Deleted enum values: [user assistant]
                - ReadOnly changed from false to true
              - Modified property: thread
                - ReadOnly changed from false to true

POST /api/chat-messages/{uuid}/edit/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: replaces
          - Properties changed
            - Modified property: replaces
              - Nullable changed from true to false
              - ReadOnly changed from false to true
            - Modified property: role
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/MessageRoleEnum
              - Type changed from 'string' to ''
              - Deleted enum values: [user assistant]
              - ReadOnly changed from false to true
            - Modified property: thread
              - ReadOnly changed from false to true

GET /api/chat-threads/

- New query param: created
- New query param: modified
- New query param: o
- New query param: query
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [modified user_full_name user_username]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: modified
              - New property: user_full_name
              - New property: user_username

GET /api/chat-threads/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [modified user_full_name user_username]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: modified
            - New property: user_full_name
            - New property: user_username

POST /api/chat/stream/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: mode

POST /api/customers/{uuid}/contact/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: homepage
          - Deleted property: address
          - Deleted property: country
          - Deleted property: postal
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: homepage
            - Deleted property: address
            - Deleted property: country
            - Deleted property: postal

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
                  - New enum values: [user_group_invitation_updated]

POST /api/hooks-email/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [user_group_invitation_updated]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [user_group_invitation_updated]

GET /api/hooks-email/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [user_group_invitation_updated]

PATCH /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [user_group_invitation_updated]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [user_group_invitation_updated]

PUT /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [user_group_invitation_updated]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [user_group_invitation_updated]

GET /api/hooks-web/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: event_types
                - Items changed
                  - New enum values: [user_group_invitation_updated]

POST /api/hooks-web/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [user_group_invitation_updated]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [user_group_invitation_updated]

GET /api/hooks-web/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [user_group_invitation_updated]

PATCH /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [user_group_invitation_updated]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [user_group_invitation_updated]

PUT /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [user_group_invitation_updated]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [user_group_invitation_updated]

GET /api/managed-rancher-cluster-resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: consumer_message
                      - New property: consumer_message_attachment
                      - New property: consumer_rejection_comment
                      - New property: created_by_email
                      - New property: created_by_organization
                      - New property: created_by_organization_registry_code
                      - New property: provider_message
                      - New property: provider_message_attachment
                      - New property: provider_message_url
                      - New property: provider_rejection_comment
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: consumer_message
                      - New property: consumer_message_attachment
                      - New property: consumer_rejection_comment
                      - New property: created_by_email
                      - New property: created_by_organization
                      - New property: created_by_organization_registry_code
                      - New property: provider_message
                      - New property: provider_message_attachment
                      - New property: provider_message_url
                      - New property: provider_rejection_comment

GET /api/managed-rancher-cluster-resources/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message
                    - New property: consumer_message_attachment
                    - New property: consumer_rejection_comment
                    - New property: created_by_email
                    - New property: created_by_organization
                    - New property: created_by_organization_registry_code
                    - New property: provider_message
                    - New property: provider_message_attachment
                    - New property: provider_message_url
                    - New property: provider_rejection_comment
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message
                    - New property: consumer_message_attachment
                    - New property: consumer_rejection_comment
                    - New property: created_by_email
                    - New property: created_by_organization
                    - New property: created_by_organization_registry_code
                    - New property: provider_message
                    - New property: provider_message_attachment
                    - New property: provider_message_url
                    - New property: provider_rejection_comment

GET /api/marketplace-offering-user-checklist-completions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: offering_user
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingUser
                    - Properties changed
                      - New property: user_active_isds
                      - New property: user_first_name
                      - New property: user_last_name

GET /api/marketplace-offering-user-checklist-completions/{id}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering_user
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingUser
                  - Properties changed
                    - New property: user_active_isds
                    - New property: user_first_name
                    - New property: user_last_name

GET /api/marketplace-offering-users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [user_active_isds user_first_name user_last_name]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: user_active_isds
              - New property: user_first_name
              - New property: user_last_name

POST /api/marketplace-offering-users/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_active_isds
            - New property: user_first_name
            - New property: user_last_name

GET /api/marketplace-offering-users/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [user_active_isds user_first_name user_last_name]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_active_isds
            - New property: user_first_name
            - New property: user_last_name

PATCH /api/marketplace-offering-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_active_isds
            - New property: user_first_name
            - New property: user_last_name

PUT /api/marketplace-offering-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_active_isds
            - New property: user_first_name
            - New property: user_last_name

GET /api/marketplace-orders/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [consumer_message consumer_message_attachment consumer_rejection_comment created_by_email created_by_organization created_by_organization_registry_code provider_message provider_message_attachment provider_message_url provider_rejection_comment]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: consumer_message
              - New property: consumer_message_attachment
              - New property: consumer_rejection_comment
              - New property: created_by_email
              - New property: created_by_organization
              - New property: created_by_organization_registry_code
              - New property: provider_message
              - New property: provider_message_attachment
              - New property: provider_message_url
              - New property: provider_rejection_comment

POST /api/marketplace-orders/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: consumer_message
            - New property: consumer_message_attachment
            - New property: consumer_rejection_comment
            - New property: created_by_email
            - New property: created_by_organization
            - New property: created_by_organization_registry_code
            - New property: provider_message
            - New property: provider_message_attachment
            - New property: provider_message_url
            - New property: provider_rejection_comment

GET /api/marketplace-orders/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [consumer_message consumer_message_attachment consumer_rejection_comment created_by_email created_by_organization created_by_organization_registry_code provider_message provider_message_attachment provider_message_url provider_rejection_comment]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: consumer_message
            - New property: consumer_message_attachment
            - New property: consumer_rejection_comment
            - New property: created_by_email
            - New property: created_by_organization
            - New property: created_by_organization_registry_code
            - New property: provider_message
            - New property: provider_message_attachment
            - New property: provider_message_url
            - New property: provider_rejection_comment

POST /api/marketplace-orders/{uuid}/approve_by_consumer/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Type changed from 'string' to 'object'
          - Example changed from 'Order has been approved and is being processed.' to null
          - Required changed
            - New required property: detail
          - Properties changed
            - New property: detail

POST /api/marketplace-orders/{uuid}/approve_by_provider/

- Request body changed
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Type changed from 'string' to 'object'
          - Example changed from 'Order has been approved and is being processed.' to null
          - Required changed
            - New required property: detail
          - Properties changed
            - New property: detail

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
                    - New property: enable_provider_consumer_messaging
                    - New property: notify_about_provider_consumer_messages
                    - New property: restrict_deletion_with_active_resources

POST /api/marketplace-orders/{uuid}/reject_by_consumer/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: consumer_rejection_comment

POST /api/marketplace-orders/{uuid}/reject_by_provider/

- Request body changed

POST /api/marketplace-orders/{uuid}/set_state_erred/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: consumer_rejection_comment

GET /api/marketplace-provider-offerings/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [backend_id_rules]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: backend_id_rules
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: enable_provider_consumer_messaging
                      - New property: notify_about_provider_consumer_messages
                      - New property: restrict_deletion_with_active_resources

POST /api/marketplace-provider-offerings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: backend_id_rules
          - Modified property: plugin_options
            - Properties changed
              - New property: enable_provider_consumer_messaging
              - New property: notify_about_provider_consumer_messages
              - New property: restrict_deletion_with_active_resources
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: backend_id_rules
          - Modified property: plugin_options
            - Properties changed
              - New property: enable_provider_consumer_messaging
              - New property: notify_about_provider_consumer_messages
              - New property: restrict_deletion_with_active_resources
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: backend_id_rules
          - Modified property: plugin_options
            - Properties changed
              - New property: enable_provider_consumer_messaging
              - New property: notify_about_provider_consumer_messages
              - New property: restrict_deletion_with_active_resources
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: backend_id_rules
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: enable_provider_consumer_messaging
                    - New property: notify_about_provider_consumer_messages
                    - New property: restrict_deletion_with_active_resources

GET /api/marketplace-provider-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [backend_id_rules]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: backend_id_rules
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: enable_provider_consumer_messaging
                    - New property: notify_about_provider_consumer_messages
                    - New property: restrict_deletion_with_active_resources

POST /api/marketplace-provider-offerings/{uuid}/activate/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/check_unique_backend_id/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: use_offering_rules
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: errors
            - New property: is_valid_format

POST /api/marketplace-provider-offerings/{uuid}/draft/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/import_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message
                    - New property: consumer_message_attachment
                    - New property: consumer_rejection_comment
                    - New property: created_by_email
                    - New property: created_by_organization
                    - New property: created_by_organization_registry_code
                    - New property: provider_message
                    - New property: provider_message_attachment
                    - New property: provider_message_url
                    - New property: provider_rejection_comment
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message
                    - New property: consumer_message_attachment
                    - New property: consumer_rejection_comment
                    - New property: created_by_email
                    - New property: created_by_organization
                    - New property: created_by_organization_registry_code
                    - New property: provider_message
                    - New property: provider_message_attachment
                    - New property: provider_message_url
                    - New property: provider_rejection_comment

GET /api/marketplace-provider-offerings/{uuid}/list_customer_users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [active_isds attribute_sources is_identity_manager managed_isds organization_registry_code]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: active_isds
              - New property: attribute_sources
              - New property: is_identity_manager
              - New property: managed_isds
              - New property: organization_registry_code

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
                    - New property: enable_provider_consumer_messaging
                    - New property: notify_about_provider_consumer_messages
                    - New property: restrict_deletion_with_active_resources

GET /api/marketplace-provider-offerings/{uuid}/orders/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [consumer_message consumer_message_attachment consumer_rejection_comment created_by_email created_by_organization created_by_organization_registry_code provider_message provider_message_attachment provider_message_url provider_rejection_comment]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: consumer_message
              - New property: consumer_message_attachment
              - New property: consumer_rejection_comment
              - New property: created_by_email
              - New property: created_by_organization
              - New property: created_by_organization_registry_code
              - New property: provider_message
              - New property: provider_message_attachment
              - New property: provider_message_url
              - New property: provider_rejection_comment

GET /api/marketplace-provider-offerings/{uuid}/orders/{order_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: consumer_message
            - New property: consumer_message_attachment
            - New property: consumer_rejection_comment
            - New property: created_by_email
            - New property: created_by_organization
            - New property: created_by_organization_registry_code
            - New property: provider_message
            - New property: provider_message_attachment
            - New property: provider_message_url
            - New property: provider_rejection_comment

POST /api/marketplace-provider-offerings/{uuid}/update_integration/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: enable_provider_consumer_messaging
              - New property: notify_about_provider_consumer_messages
              - New property: restrict_deletion_with_active_resources

GET /api/marketplace-provider-offerings/{uuid}/user_has_resource_access/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [backend_id_rules]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: backend_id_rules
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: enable_provider_consumer_messaging
                    - New property: notify_about_provider_consumer_messages
                    - New property: restrict_deletion_with_active_resources

GET /api/marketplace-provider-resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: consumer_message
                      - New property: consumer_message_attachment
                      - New property: consumer_rejection_comment
                      - New property: created_by_email
                      - New property: created_by_organization
                      - New property: created_by_organization_registry_code
                      - New property: provider_message
                      - New property: provider_message_attachment
                      - New property: provider_message_url
                      - New property: provider_rejection_comment
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: consumer_message
                      - New property: consumer_message_attachment
                      - New property: consumer_rejection_comment
                      - New property: created_by_email
                      - New property: created_by_organization
                      - New property: created_by_organization_registry_code
                      - New property: provider_message
                      - New property: provider_message_attachment
                      - New property: provider_message_url
                      - New property: provider_rejection_comment

GET /api/marketplace-provider-resources/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message
                    - New property: consumer_message_attachment
                    - New property: consumer_rejection_comment
                    - New property: created_by_email
                    - New property: created_by_organization
                    - New property: created_by_organization_registry_code
                    - New property: provider_message
                    - New property: provider_message_attachment
                    - New property: provider_message_url
                    - New property: provider_rejection_comment
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message
                    - New property: consumer_message_attachment
                    - New property: consumer_rejection_comment
                    - New property: created_by_email
                    - New property: created_by_organization
                    - New property: created_by_organization_registry_code
                    - New property: provider_message
                    - New property: provider_message_attachment
                    - New property: provider_message_url
                    - New property: provider_rejection_comment

POST /api/marketplace-provider-resources/{uuid}/move_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message
                    - New property: consumer_message_attachment
                    - New property: consumer_rejection_comment
                    - New property: created_by_email
                    - New property: created_by_organization
                    - New property: created_by_organization_registry_code
                    - New property: provider_message
                    - New property: provider_message_attachment
                    - New property: provider_message_url
                    - New property: provider_rejection_comment
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message
                    - New property: consumer_message_attachment
                    - New property: consumer_rejection_comment
                    - New property: created_by_email
                    - New property: created_by_organization
                    - New property: created_by_organization_registry_code
                    - New property: provider_message
                    - New property: provider_message_attachment
                    - New property: provider_message_url
                    - New property: provider_rejection_comment

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
                    - New property: enable_provider_consumer_messaging
                    - New property: notify_about_provider_consumer_messages
                    - New property: restrict_deletion_with_active_resources

POST /api/marketplace-provider-resources/{uuid}/restore/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message
                    - New property: consumer_message_attachment
                    - New property: consumer_rejection_comment
                    - New property: created_by_email
                    - New property: created_by_organization
                    - New property: created_by_organization_registry_code
                    - New property: provider_message
                    - New property: provider_message_attachment
                    - New property: provider_message_url
                    - New property: provider_rejection_comment
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message
                    - New property: consumer_message_attachment
                    - New property: consumer_rejection_comment
                    - New property: created_by_email
                    - New property: created_by_organization
                    - New property: created_by_organization_registry_code
                    - New property: provider_message
                    - New property: provider_message_attachment
                    - New property: provider_message_url
                    - New property: provider_rejection_comment

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
                      - New property: enable_provider_consumer_messaging
                      - New property: notify_about_provider_consumer_messages
                      - New property: restrict_deletion_with_active_resources

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
                    - New property: enable_provider_consumer_messaging
                    - New property: notify_about_provider_consumer_messages
                    - New property: restrict_deletion_with_active_resources

GET /api/marketplace-resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: consumer_message
                      - New property: consumer_message_attachment
                      - New property: consumer_rejection_comment
                      - New property: created_by_email
                      - New property: created_by_organization
                      - New property: created_by_organization_registry_code
                      - New property: provider_message
                      - New property: provider_message_attachment
                      - New property: provider_message_url
                      - New property: provider_rejection_comment
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: consumer_message
                      - New property: consumer_message_attachment
                      - New property: consumer_rejection_comment
                      - New property: created_by_email
                      - New property: created_by_organization
                      - New property: created_by_organization_registry_code
                      - New property: provider_message
                      - New property: provider_message_attachment
                      - New property: provider_message_url
                      - New property: provider_rejection_comment

GET /api/marketplace-resources/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message
                    - New property: consumer_message_attachment
                    - New property: consumer_rejection_comment
                    - New property: created_by_email
                    - New property: created_by_organization
                    - New property: created_by_organization_registry_code
                    - New property: provider_message
                    - New property: provider_message_attachment
                    - New property: provider_message_url
                    - New property: provider_rejection_comment
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message
                    - New property: consumer_message_attachment
                    - New property: consumer_rejection_comment
                    - New property: created_by_email
                    - New property: created_by_organization
                    - New property: created_by_organization_registry_code
                    - New property: provider_message
                    - New property: provider_message_attachment
                    - New property: provider_message_url
                    - New property: provider_rejection_comment

POST /api/marketplace-resources/{uuid}/move_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message
                    - New property: consumer_message_attachment
                    - New property: consumer_rejection_comment
                    - New property: created_by_email
                    - New property: created_by_organization
                    - New property: created_by_organization_registry_code
                    - New property: provider_message
                    - New property: provider_message_attachment
                    - New property: provider_message_url
                    - New property: provider_rejection_comment
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message
                    - New property: consumer_message_attachment
                    - New property: consumer_rejection_comment
                    - New property: created_by_email
                    - New property: created_by_organization
                    - New property: created_by_organization_registry_code
                    - New property: provider_message
                    - New property: provider_message_attachment
                    - New property: provider_message_url
                    - New property: provider_rejection_comment

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
                    - New property: enable_provider_consumer_messaging
                    - New property: notify_about_provider_consumer_messages
                    - New property: restrict_deletion_with_active_resources

POST /api/marketplace-resources/{uuid}/restore/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message
                    - New property: consumer_message_attachment
                    - New property: consumer_rejection_comment
                    - New property: created_by_email
                    - New property: created_by_organization
                    - New property: created_by_organization_registry_code
                    - New property: provider_message
                    - New property: provider_message_attachment
                    - New property: provider_message_url
                    - New property: provider_rejection_comment
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message
                    - New property: consumer_message_attachment
                    - New property: consumer_rejection_comment
                    - New property: created_by_email
                    - New property: created_by_organization
                    - New property: created_by_organization_registry_code
                    - New property: provider_message
                    - New property: provider_message_attachment
                    - New property: provider_message_url
                    - New property: provider_rejection_comment

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
                      - New property: enable_provider_consumer_messaging
                      - New property: notify_about_provider_consumer_messages
                      - New property: restrict_deletion_with_active_resources

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
                    - New property: enable_provider_consumer_messaging
                    - New property: notify_about_provider_consumer_messages
                    - New property: restrict_deletion_with_active_resources

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
                    - New property: enable_provider_consumer_messaging
                    - New property: notify_about_provider_consumer_messages
                    - New property: restrict_deletion_with_active_resources

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
                    - New property: enable_provider_consumer_messaging
                    - New property: notify_about_provider_consumer_messages
                    - New property: restrict_deletion_with_active_resources

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
                    - New property: enable_provider_consumer_messaging
                    - New property: notify_about_provider_consumer_messages
                    - New property: restrict_deletion_with_active_resources

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
                    - New property: enable_provider_consumer_messaging
                    - New property: notify_about_provider_consumer_messages
                    - New property: restrict_deletion_with_active_resources

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
                    - New property: enable_provider_consumer_messaging
                    - New property: notify_about_provider_consumer_messages
                    - New property: restrict_deletion_with_active_resources

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
                    - New property: enable_provider_consumer_messaging
                    - New property: notify_about_provider_consumer_messages
                    - New property: restrict_deletion_with_active_resources

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
                    - New property: enable_provider_consumer_messaging
                    - New property: notify_about_provider_consumer_messages
                    - New property: restrict_deletion_with_active_resources

POST /api/marketplace-slurm-periodic-usage-policies/{uuid}/report-command-result/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: mode
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/SlurmCommandResultModeEnum
              - Schemas deleted: #/components/schemas/ModeEnum

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
                  - New enum values: [user_group_invitation_updated]

GET /api/onboarding-justifications/

- New query param: o
- New query param: query
- New query param: validation_decision

HEAD /api/onboarding-justifications/

- New query param: o
- New query param: query
- New query param: validation_decision

GET /api/onboarding-verifications/

- New query param: o
- New query param: query
- New query param: validation_method
- Modified query param: status
  - Description changed from '' to 'Verification status

'

- Style changed from '' to 'form'
- Explode changed from null to true
- Schema changed
  - Type changed from 'string' to 'array'
  - Items changed
    - Schema added

HEAD /api/onboarding-verifications/

- New query param: o
- New query param: query
- New query param: validation_method
- Modified query param: status
  - Description changed from '' to 'Verification status

'

- Style changed from '' to 'form'
- Explode changed from null to true
- Schema changed
  - Type changed from 'string' to 'array'
  - Items changed
    - Schema added

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
                            - New property: backend_id_rules
                            - Modified property: plugin_options
                              - Property 'AllOf' changed
                                - Modified schema: #/components/schemas/MergedPluginOptions
                                  - Properties changed
                                    - New property: enable_provider_consumer_messaging
                                    - New property: notify_about_provider_consumer_messages
                                    - New property: restrict_deletion_with_active_resources

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
                          - New property: backend_id_rules
                          - Modified property: plugin_options
                            - Property 'AllOf' changed
                              - Modified schema: #/components/schemas/MergedPluginOptions
                                - Properties changed
                                  - New property: enable_provider_consumer_messaging
                                  - New property: notify_about_provider_consumer_messages
                                  - New property: restrict_deletion_with_active_resources

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
                    - New property: backend_id_rules
                    - Modified property: plugin_options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/MergedPluginOptions
                          - Properties changed
                            - New property: enable_provider_consumer_messaging
                            - New property: notify_about_provider_consumer_messages
                            - New property: restrict_deletion_with_active_resources

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
                  - New property: backend_id_rules
                  - Modified property: plugin_options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/MergedPluginOptions
                        - Properties changed
                          - New property: enable_provider_consumer_messaging
                          - New property: notify_about_provider_consumer_messages
                          - New property: restrict_deletion_with_active_resources

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
                  - New property: backend_id_rules
                  - Modified property: plugin_options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/MergedPluginOptions
                        - Properties changed
                          - New property: enable_provider_consumer_messaging
                          - New property: notify_about_provider_consumer_messages
                          - New property: restrict_deletion_with_active_resources

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
                  - New property: backend_id_rules
                  - Modified property: plugin_options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/MergedPluginOptions
                        - Properties changed
                          - New property: enable_provider_consumer_messaging
                          - New property: notify_about_provider_consumer_messages
                          - New property: restrict_deletion_with_active_resources

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
                  - New property: backend_id_rules
                  - Modified property: plugin_options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/MergedPluginOptions
                        - Properties changed
                          - New property: enable_provider_consumer_messaging
                          - New property: notify_about_provider_consumer_messages
                          - New property: restrict_deletion_with_active_resources

GET /api/override-settings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: ALLOW_SERVICE_PROVIDER_OFFERING_MANAGEMENT
            - New property: DISCLAIMER_AREA_LOGO
            - New property: DISCLAIMER_AREA_TEXT
            - New property: ENABLE_PROJECT_DIGEST
            - New property: FEDERATED_IDENTITY_DEACTIVATION_POLICY
            - New property: FEDERATED_IDENTITY_SYNC_ALLOWED_ATTRIBUTES
            - New property: FEDERATED_IDENTITY_SYNC_ENABLED
            - New property: OIDC_MATCHMAKING_BY_EMAIL
            - New property: REMOTE_EDUTEAMS_REFRESH_TOKEN
            - New property: SYSTEM_LOG_ENABLED
            - New property: SYSTEM_LOG_MAX_ROWS_PER_SOURCE

POST /api/override-settings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: ALLOW_SERVICE_PROVIDER_OFFERING_MANAGEMENT
          - New property: DISCLAIMER_AREA_LOGO
          - New property: DISCLAIMER_AREA_TEXT
          - New property: ENABLE_PROJECT_DIGEST
          - New property: FEDERATED_IDENTITY_DEACTIVATION_POLICY
          - New property: FEDERATED_IDENTITY_SYNC_ALLOWED_ATTRIBUTES
          - New property: FEDERATED_IDENTITY_SYNC_ENABLED
          - New property: OIDC_MATCHMAKING_BY_EMAIL
          - New property: REMOTE_EDUTEAMS_REFRESH_TOKEN
          - New property: SYSTEM_LOG_ENABLED
          - New property: SYSTEM_LOG_MAX_ROWS_PER_SOURCE
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: ALLOW_SERVICE_PROVIDER_OFFERING_MANAGEMENT
          - New property: DISCLAIMER_AREA_LOGO
          - New property: DISCLAIMER_AREA_TEXT
          - New property: ENABLE_PROJECT_DIGEST
          - New property: FEDERATED_IDENTITY_DEACTIVATION_POLICY
          - New property: FEDERATED_IDENTITY_SYNC_ALLOWED_ATTRIBUTES
          - New property: FEDERATED_IDENTITY_SYNC_ENABLED
          - New property: OIDC_MATCHMAKING_BY_EMAIL
          - New property: REMOTE_EDUTEAMS_REFRESH_TOKEN
          - New property: SYSTEM_LOG_ENABLED
          - New property: SYSTEM_LOG_MAX_ROWS_PER_SOURCE
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: ALLOW_SERVICE_PROVIDER_OFFERING_MANAGEMENT
          - New property: DISCLAIMER_AREA_LOGO
          - New property: DISCLAIMER_AREA_TEXT
          - New property: ENABLE_PROJECT_DIGEST
          - New property: FEDERATED_IDENTITY_DEACTIVATION_POLICY
          - New property: FEDERATED_IDENTITY_SYNC_ALLOWED_ATTRIBUTES
          - New property: FEDERATED_IDENTITY_SYNC_ENABLED
          - New property: OIDC_MATCHMAKING_BY_EMAIL
          - New property: REMOTE_EDUTEAMS_REFRESH_TOKEN
          - New property: SYSTEM_LOG_ENABLED
          - New property: SYSTEM_LOG_MAX_ROWS_PER_SOURCE

GET /api/promotions-campaigns/{uuid}/orders/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [consumer_message consumer_message_attachment consumer_rejection_comment created_by_email created_by_organization created_by_organization_registry_code provider_message provider_message_attachment provider_message_url provider_rejection_comment]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: consumer_message
              - New property: consumer_message_attachment
              - New property: consumer_rejection_comment
              - New property: created_by_email
              - New property: created_by_organization
              - New property: created_by_organization_registry_code
              - New property: provider_message
              - New property: provider_message_attachment
              - New property: provider_message_url
              - New property: provider_rejection_comment

GET /api/promotions-campaigns/{uuid}/resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: consumer_message
                      - New property: consumer_message_attachment
                      - New property: consumer_rejection_comment
                      - New property: created_by_email
                      - New property: created_by_organization
                      - New property: created_by_organization_registry_code
                      - New property: provider_message
                      - New property: provider_message_attachment
                      - New property: provider_message_url
                      - New property: provider_rejection_comment
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: consumer_message
                      - New property: consumer_message_attachment
                      - New property: consumer_rejection_comment
                      - New property: created_by_email
                      - New property: created_by_organization
                      - New property: created_by_organization_registry_code
                      - New property: provider_message
                      - New property: provider_message_attachment
                      - New property: provider_message_url
                      - New property: provider_rejection_comment

GET /api/user-actions/

- New query param: user_uuid

HEAD /api/user-actions/

- New query param: user_uuid

GET /api/user-group-invitations/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: custom_text

POST /api/user-group-invitations/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: custom_text
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: custom_text

GET /api/user-group-invitations/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: custom_text

GET /api/users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [active_isds attribute_sources is_identity_manager managed_isds organization_registry_code]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: active_isds
              - New property: attribute_sources
              - New property: is_identity_manager
              - New property: managed_isds
              - New property: organization_registry_code

POST /api/users/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: is_identity_manager
          - New property: managed_isds
          - New property: organization_registry_code
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: is_identity_manager
          - New property: managed_isds
          - New property: organization_registry_code
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: is_identity_manager
          - New property: managed_isds
          - New property: organization_registry_code
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: active_isds
            - New property: attribute_sources
            - New property: is_identity_manager
            - New property: managed_isds
            - New property: organization_registry_code

GET /api/users/me/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [active_isds attribute_sources is_identity_manager managed_isds organization_registry_code]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: active_isds
            - New property: attribute_sources
            - New property: is_identity_manager
            - New property: managed_isds
            - New property: organization_registry_code

GET /api/users/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [active_isds attribute_sources is_identity_manager managed_isds organization_registry_code]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: active_isds
            - New property: attribute_sources
            - New property: is_identity_manager
            - New property: managed_isds
            - New property: organization_registry_code

PATCH /api/users/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: is_identity_manager
          - New property: managed_isds
          - New property: organization_registry_code
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: is_identity_manager
          - New property: managed_isds
          - New property: organization_registry_code
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: is_identity_manager
          - New property: managed_isds
          - New property: organization_registry_code
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: active_isds
            - New property: attribute_sources
            - New property: is_identity_manager
            - New property: managed_isds
            - New property: organization_registry_code

PUT /api/users/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: is_identity_manager
          - New property: managed_isds
          - New property: organization_registry_code
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: is_identity_manager
          - New property: managed_isds
          - New property: organization_registry_code
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: is_identity_manager
          - New property: managed_isds
          - New property: organization_registry_code
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: active_isds
            - New property: attribute_sources
            - New property: is_identity_manager
            - New property: managed_isds
            - New property: organization_registry_code
