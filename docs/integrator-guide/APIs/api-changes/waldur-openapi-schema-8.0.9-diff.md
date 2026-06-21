# OpenAPI schema diff - 8.0.9

## For version 8.0.9

### New Endpoints: 95

---------------------
PUT /_matrix/app/v1/transactions/{txn_id}  
POST /api-auth/token-exchange/  
POST /api/admin/matrix-appservice/setup/  
GET /api/admin/matrix-appservice/status/  
GET /api/admin/matrix/diagnostics/  
GET /api/admin/matrix/livekit/overview/  
GET /api/admin/matrix/livekit/participants/  
POST /api/admin/matrix/reprovision/  
POST /api/autoprovisioning-rules/{uuid}/test-match/  
POST /api/customers/{uuid}/update_default_affiliations/  
GET /api/marketplace-customer-usage/{uuid}/components-usage-by-project/  
GET /api/marketplace-customer-usage/{uuid}/components-usage-timeseries/  
GET /api/marketplace-customer-usage/{uuid}/components-usage/  
GET /api/marketplace-offering-groups/  
HEAD /api/marketplace-offering-groups/  
POST /api/marketplace-offering-groups/  
DELETE /api/marketplace-offering-groups/{uuid}/  
GET /api/marketplace-offering-groups/{uuid}/  
PATCH /api/marketplace-offering-groups/{uuid}/  
PUT /api/marketplace-offering-groups/{uuid}/  
POST /api/marketplace-offering-users/{uuid}/update_runtime_state/  
GET /api/marketplace-project-order-auto-approvals/  
HEAD /api/marketplace-project-order-auto-approvals/  
POST /api/marketplace-project-order-auto-approvals/  
DELETE /api/marketplace-project-order-auto-approvals/{uuid}/  
GET /api/marketplace-project-order-auto-approvals/{uuid}/  
PATCH /api/marketplace-project-order-auto-approvals/{uuid}/  
PUT /api/marketplace-project-order-auto-approvals/{uuid}/  
GET /api/marketplace-project-usage/{uuid}/components-usage-timeseries/  
GET /api/marketplace-project-usage/{uuid}/components-usage/  
GET /api/marketplace-provider-offerings/{uuid}/glauth_tree/  
POST /api/marketplace-provider-offerings/{uuid}/set_offering_group/  
POST /api/marketplace-provider-offerings/{uuid}/sync_resources/  
POST /api/marketplace-provider-offerings/{uuid}/update_type/  
POST /api/marketplace-provider-offerings/{uuid}/upload_markdown_image/  
POST /api/marketplace-provider-resources/{uuid}/adjust_dates/  
GET /api/marketplace-provider-resources/{uuid}/glauth_tree/  
POST /api/marketplace-provider-resources/{uuid}/set_endpoints/  
GET /api/marketplace-resource-limit-change-requests/  
HEAD /api/marketplace-resource-limit-change-requests/  
POST /api/marketplace-resource-limit-change-requests/  
GET /api/marketplace-resource-limit-change-requests/{uuid}/  
POST /api/marketplace-resource-limit-change-requests/{uuid}/approve/  
POST /api/marketplace-resource-limit-change-requests/{uuid}/cancel/  
POST /api/marketplace-resource-limit-change-requests/{uuid}/reject/  
POST /api/marketplace-resource-projects/{uuid}/recover/  
POST /api/marketplace-resources/{uuid}/adjust_dates/  
GET /api/marketplace-resources/{uuid}/glauth_tree/  
GET /api/marketplace-service-providers/{service_provider_uuid}/offerings/types/  
GET /api/marketplace-site-agent-logs/  
HEAD /api/marketplace-site-agent-logs/  
POST /api/marketplace-site-agent-logs/  
GET /api/marketplace-stats/user_affiliation_details/  
HEAD /api/marketplace-stats/user_affiliation_details/  
GET /api/matrix/credentials/  
GET /api/matrix/exports/  
HEAD /api/matrix/exports/  
GET /api/matrix/exports/{uuid}/  
GET /api/matrix/exports/{uuid}/download/{kind}/  
GET /api/matrix/rooms/  
HEAD /api/matrix/rooms/  
POST /api/matrix/rooms/  
GET /api/matrix/rooms/eligible_projects/  
HEAD /api/matrix/rooms/eligible_projects/  
DELETE /api/matrix/rooms/{uuid}/  
GET /api/matrix/rooms/{uuid}/  
POST /api/matrix/rooms/{uuid}/disable/  
POST /api/matrix/rooms/{uuid}/export_history/  
POST /api/matrix/rooms/{uuid}/join/  
POST /api/matrix/rooms/{uuid}/leave/  
GET /api/matrix/rooms/{uuid}/members/  
POST /api/matrix/rooms/{uuid}/reactivate/  
POST /api/matrix/rooms/{uuid}/retry/  
POST /api/matrix/rooms/{uuid}/sync_members/  
POST /api/openportal-unmanaged-projects/{uuid}/update_affiliation/  
POST /api/openstack-instances/{uuid}/diagnose_connectivity/  
POST /api/openstack-ports/{uuid}/set_allowed_address_pairs/  
GET /api/openstack-routers/{uuid}/effective_routes/  
GET /api/openstack-tenants/{uuid}/topology/  
GET /api/personal-access-tokens/available_binding_targets/  
HEAD /api/personal-access-tokens/available_binding_targets/  
POST /api/projects/{uuid}/update_affiliation/  
POST /api/proposal-proposals/{uuid}/advance_workflow_step/  
POST /api/proposal-proposals/{uuid}/complete_workflow_step/  
POST /api/proposal-proposals/{uuid}/reject_workflow_step/  
GET /api/proposal-proposals/{uuid}/workflow_states/  
POST /api/proposal-protected-calls/{uuid}/duplicate/  
POST /api/proposal-protected-calls/{uuid}/rounds-bulk-set/  
GET /api/proposal-protected-calls/{uuid}/workflow_steps/  
POST /api/proposal-protected-calls/{uuid}/workflow_steps/  
DELETE /api/proposal-protected-calls/{uuid}/workflow_steps/{obj_uuid}/  
GET /api/proposal-protected-calls/{uuid}/workflow_steps/{obj_uuid}/  
PATCH /api/proposal-protected-calls/{uuid}/workflow_steps/{obj_uuid}/  
PUT /api/proposal-protected-calls/{uuid}/workflow_steps/{obj_uuid}/  
POST /api/users/{uuid}/pull_scim_attributes/  

### Deleted Endpoints: 5

------------------------
GET /api/customers/{uuid}/components-usage/  
GET /api/openportal-unmanaged-projects/{uuid}/components-usage/  
POST /api/openportal-unmanaged-projects/{uuid}/update_affiliated_organizations/  
GET /api/projects/{uuid}/components-usage/  
POST /api/projects/{uuid}/update_affiliated_organizations/  

### Modified Endpoints: 692

---------------------------
POST /api/admin/arrow/billing-syncs/fetch_billing_export/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: data
              - Description changed from '' to 'Raw billing export data from Arrow API'

POST /api/admin/arrow/billing-syncs/fetch_consumption/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: data
              - Description changed from '' to 'Raw consumption data from Arrow API'

POST /api/admin/arrow/billing-syncs/sync_resource_historical_consumption/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: errors
          - Properties changed
            - Modified property: errors
              - Items changed
                - Properties changed
                  - New property: customer_id
                  - New property: error
                  - New property: period
                  - New property: subscription_id
                - AdditionalProperties changed
                  - Schema deleted
            - Modified property: preview_periods
              - Items changed
                - Required changed
                  - New required property: period
                - Properties changed
                  - New property: period
                  - New property: row_count
                  - New property: status
                - AdditionalProperties changed
                  - Schema deleted

POST /api/admin/arrow/billing-syncs/sync_resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: customers_created
            - Deleted property: errors
            - Deleted property: invoice_items_created
            - Deleted property: invoices_created
            - Deleted property: mappings_created
            - Deleted property: orders_created
            - Deleted property: projects_created

GET /api/admin/arrow/consumption-records/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: raw_data
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

GET /api/admin/arrow/consumption-records/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: raw_data
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

POST /api/admin/arrow/settings/validate_credentials/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: partner_info
              - Description changed from '' to 'Raw partner info data from Arrow API'

GET /api/affiliated-organizations/

- New query param: default_for_customer
- New query param: field

HEAD /api/affiliated-organizations/

- New query param: default_for_customer

GET /api/affiliated-organizations/report/

- New query param: default_for_customer

HEAD /api/affiliated-organizations/report/

- New query param: default_for_customer

GET /api/affiliated-organizations/{uuid}/

- New query param: field

GET /api/anonymous-chat-interactions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: assistant_blocks
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: injection_categories
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: offering_uuids
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: pii_categories
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

GET /api/anonymous-chat-interactions/by-session/{session_id}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: assistant_blocks
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: injection_categories
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: offering_uuids
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: pii_categories
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

GET /api/anonymous-chat-interactions/by-user/{user_slug}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: assistant_blocks
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: injection_categories
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: offering_uuids
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: pii_categories
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

GET /api/anonymous-chat-interactions/kpi/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: daily_volume
              - Items changed
                - Required changed
                  - New required property: count
                  - New required property: date
                - Properties changed
                  - New property: count
                  - New property: date
                - AdditionalProperties changed
                  - Schema deleted
            - Modified property: severity_by_day
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/SeverityByDay
              - Type changed from 'object' to ''
              - AdditionalProperties changed
                - Schema deleted

GET /api/anonymous-chat-interactions/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: assistant_blocks
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: injection_categories
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: offering_uuids
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: pii_categories
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

POST /api/assignment-batches/{uuid}/cancel/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'call.manager' to 'call'
    - Added /0/scopes/- with value: 'call.manager'

POST /api/assignment-batches/{uuid}/extend-deadline/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'call.manager' to 'call'
    - Added /0/scopes/- with value: 'call.manager'

POST /api/assignment-batches/{uuid}/send/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'call.manager' to 'call'
    - Added /0/scopes/- with value: 'call.manager'

POST /api/assignment-items/{uuid}/force-unblock/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'batch.call.manager' to 'batch.call'
    - Added /0/scopes/- with value: 'batch.call.manager'

POST /api/assignment-items/{uuid}/reassign/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'batch.call.manager' to 'batch.call'
    - Added /0/scopes/- with value: 'batch.call.manager'

GET /api/assignment-items/{uuid}/suggest_alternatives/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'batch.call.manager' to 'batch.call'
    - Added /0/scopes/- with value: 'batch.call.manager'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: suggestions
              - Items changed
                - Required changed
                  - New required property: affinity_score
                  - New required property: current_assignments
                  - New required property: max_assignments
                  - New required property: pool_entry_uuid
                  - New required property: reviewer_name
                - Properties changed
                  - New property: affinity_score
                  - New property: current_assignments
                  - New property: max_assignments
                  - New property: pool_entry_uuid
                  - New property: reviewer_name
                - AdditionalProperties changed
                  - Schema deleted

POST /api/aws-instances/{uuid}/resize/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/aws-instances/{uuid}/restart/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/aws-instances/{uuid}/start/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/aws-instances/{uuid}/stop/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/aws-volumes/{uuid}/attach/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/aws-volumes/{uuid}/detach/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/azure-sql-servers/{uuid}/create_database/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/azure-virtualmachines/{uuid}/restart/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/azure-virtualmachines/{uuid}/start/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/azure-virtualmachines/{uuid}/stop/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/backend-resource-requests/{uuid}/set_done/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: status

POST /api/backend-resource-requests/{uuid}/set_erred/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: status

POST /api/backend-resource-requests/{uuid}/start_processing/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: status

GET /api/backend-resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: backend_metadata
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

POST /api/backend-resources/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: backend_metadata
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: backend_metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/backend-resources/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: backend_metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

POST /api/backend-resources/{uuid}/import_resource/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: end_date_updated_at
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: auto_approved
                    - New property: auto_approved_by_rule_uuid
                    - New property: auto_approved_cost_limit_snapshot
                    - Modified property: attributes
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: offering_plugin_options
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
            - Modified property: offering_plugin_options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: auto_approved
                    - New property: auto_approved_by_rule_uuid
                    - New property: auto_approved_cost_limit_snapshot
                    - Modified property: attributes
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: offering_plugin_options
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true

GET /api/booking-offerings/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_group offering_group_title offering_group_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: offering_group
              - New property: offering_group_title
              - New property: offering_group_uuid
              - Modified property: backend_metadata
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - Modified property: cascade_config
                              - Properties changed
                                - Modified property: steps
                                  - Items changed
                                    - Properties changed
                                      - Modified property: choices
                                        - Type changed from '' to 'object'
                                        - AdditionalProperties changed from null to true
                                      - Modified property: choices_map
                                        - Type changed from '' to 'object'
                                        - AdditionalProperties changed from null to true
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: auto_ok_resource_projects
                      - New property: expose_inference_playground
                      - New property: initial_rolegroup_number
                      - New property: require_effective_id_for_highlighted_display
                      - New property: resource_project_role_group_template
                      - New property: resource_project_role_map
                      - New property: resource_role_group_template
                      - New property: resource_role_map
                      - New property: resource_slug_max_length
                      - New property: resource_slug_template
                      - Modified property: required_team_role_for_provisioning
                        - Nullable changed from false to true
                      - Modified property: resource_name_pattern
                        - Nullable changed from false to true
              - Modified property: resource_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - Modified property: cascade_config
                              - Properties changed
                                - Modified property: steps
                                  - Items changed
                                    - Properties changed
                                      - Modified property: choices
                                        - Type changed from '' to 'object'
                                        - AdditionalProperties changed from null to true
                                      - Modified property: choices_map
                                        - Type changed from '' to 'object'
                                        - AdditionalProperties changed from null to true
              - Modified property: software_catalogs
                - Items changed
                  - Properties changed
                    - Modified property: enabled_cpu_family
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: enabled_cpu_microarchitectures
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true

GET /api/booking-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_group offering_group_title offering_group_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_group
            - New property: offering_group_title
            - New property: offering_group_uuid
            - Modified property: backend_metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - Modified property: cascade_config
                            - Properties changed
                              - Modified property: steps
                                - Items changed
                                  - Properties changed
                                    - Modified property: choices
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
                                    - Modified property: choices_map
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: auto_ok_resource_projects
                    - New property: expose_inference_playground
                    - New property: initial_rolegroup_number
                    - New property: require_effective_id_for_highlighted_display
                    - New property: resource_project_role_group_template
                    - New property: resource_project_role_map
                    - New property: resource_role_group_template
                    - New property: resource_role_map
                    - New property: resource_slug_max_length
                    - New property: resource_slug_template
                    - Modified property: required_team_role_for_provisioning
                      - Nullable changed from false to true
                    - Modified property: resource_name_pattern
                      - Nullable changed from false to true
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - Modified property: cascade_config
                            - Properties changed
                              - Modified property: steps
                                - Items changed
                                  - Properties changed
                                    - Modified property: choices
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
                                    - Modified property: choices_map
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: enabled_cpu_family
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: enabled_cpu_microarchitectures
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true

GET /api/booking-resources/

- New query param: flavor_name
- New query param: image_name
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [end_date_updated_at]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: end_date_updated_at
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: auto_approved
                      - New property: auto_approved_by_rule_uuid
                      - New property: auto_approved_cost_limit_snapshot
                      - Modified property: attributes
                        - Type changed from '' to 'object'
                        - AdditionalProperties changed from null to true
                      - Modified property: offering_plugin_options
                        - Type changed from '' to 'object'
                        - AdditionalProperties changed from null to true
              - Modified property: offering_plugin_options
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: options
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: auto_approved
                      - New property: auto_approved_by_rule_uuid
                      - New property: auto_approved_cost_limit_snapshot
                      - Modified property: attributes
                        - Type changed from '' to 'object'
                        - AdditionalProperties changed from null to true
                      - Modified property: offering_plugin_options
                        - Type changed from '' to 'object'
                        - AdditionalProperties changed from null to true

HEAD /api/booking-resources/

- New query param: flavor_name
- New query param: image_name

GET /api/booking-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [end_date_updated_at]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: end_date_updated_at
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: auto_approved
                    - New property: auto_approved_by_rule_uuid
                    - New property: auto_approved_cost_limit_snapshot
                    - Modified property: attributes
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: offering_plugin_options
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
            - Modified property: offering_plugin_options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: auto_approved
                    - New property: auto_approved_by_rule_uuid
                    - New property: auto_approved_cost_limit_snapshot
                    - Modified property: attributes
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: offering_plugin_options
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true

POST /api/booking-resources/{uuid}/accept/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: order_uuid
          - Properties changed
            - New property: order_uuid
            - Deleted property: attributes
            - Deleted property: available_actions
            - Deleted property: backend_id
            - Deleted property: backend_metadata
            - Deleted property: can_terminate
            - Deleted property: category_icon
            - Deleted property: category_title
            - Deleted property: category_uuid
            - Deleted property: consumer_reviewed_by
            - Deleted property: consumer_reviewed_by_full_name
            - Deleted property: consumer_reviewed_by_username
            - Deleted property: created
            - Deleted property: created_by
            - Deleted property: created_by_full_name
            - Deleted property: created_by_username
            - Deleted property: creation_order
            - Deleted property: current_usages
            - Deleted property: customer_name
            - Deleted property: customer_slug
            - Deleted property: customer_uuid
            - Deleted property: description
            - Deleted property: downscaled
            - Deleted property: effective_id
            - Deleted property: end_date
            - Deleted property: end_date_requested_by
            - Deleted property: endpoints
            - Deleted property: error_message
            - Deleted property: error_traceback
            - Deleted property: is_limit_based
            - Deleted property: is_usage_based
            - Deleted property: last_sync
            - Deleted property: limit_usage
            - Deleted property: limits
            - Deleted property: modified
            - Deleted property: name
            - Deleted property: offering
            - Deleted property: offering_backend_id
            - Deleted property: offering_billable
            - Deleted property: offering_components
            - Deleted property: offering_description
            - Deleted property: offering_image
            - Deleted property: offering_name
            - Deleted property: offering_plugin_options
            - Deleted property: offering_shared
            - Deleted property: offering_slug
            - Deleted property: offering_state
            - Deleted property: offering_thumbnail
            - Deleted property: offering_type
            - Deleted property: offering_uuid
            - Deleted property: options
            - Deleted property: order_in_progress
            - Deleted property: parent_name
            - Deleted property: parent_offering_name
            - Deleted property: parent_offering_slug
            - Deleted property: parent_offering_uuid
            - Deleted property: parent_uuid
            - Deleted property: paused
            - Deleted property: plan
            - Deleted property: plan_description
            - Deleted property: plan_name
            - Deleted property: plan_unit
            - Deleted property: plan_uuid
            - Deleted property: project
            - Deleted property: project_description
            - Deleted property: project_effective_end_date
            - Deleted property: project_end_date
            - Deleted property: project_end_date_requested_by
            - Deleted property: project_is_in_grace_period
            - Deleted property: project_name
            - Deleted property: project_slug
            - Deleted property: project_uuid
            - Deleted property: provider_description
            - Deleted property: provider_name
            - Deleted property: provider_slug
            - Deleted property: provider_uuid
            - Deleted property: renewal_date
            - Deleted property: report
            - Deleted property: resource_type
            - Deleted property: resource_uuid
            - Deleted property: restrict_member_access
            - Deleted property: scope
            - Deleted property: service_settings_uuid
            - Deleted property: slots
            - Deleted property: slug
            - Deleted property: state
            - Deleted property: url
            - Deleted property: user_requires_reconsent
            - Deleted property: username
            - Deleted property: uuid

POST /api/booking-resources/{uuid}/reject/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: order_uuid
          - Properties changed
            - New property: order_uuid
            - Deleted property: attributes
            - Deleted property: available_actions
            - Deleted property: backend_id
            - Deleted property: backend_metadata
            - Deleted property: can_terminate
            - Deleted property: category_icon
            - Deleted property: category_title
            - Deleted property: category_uuid
            - Deleted property: consumer_reviewed_by
            - Deleted property: consumer_reviewed_by_full_name
            - Deleted property: consumer_reviewed_by_username
            - Deleted property: created
            - Deleted property: created_by
            - Deleted property: created_by_full_name
            - Deleted property: created_by_username
            - Deleted property: creation_order
            - Deleted property: current_usages
            - Deleted property: customer_name
            - Deleted property: customer_slug
            - Deleted property: customer_uuid
            - Deleted property: description
            - Deleted property: downscaled
            - Deleted property: effective_id
            - Deleted property: end_date
            - Deleted property: end_date_requested_by
            - Deleted property: endpoints
            - Deleted property: error_message
            - Deleted property: error_traceback
            - Deleted property: is_limit_based
            - Deleted property: is_usage_based
            - Deleted property: last_sync
            - Deleted property: limit_usage
            - Deleted property: limits
            - Deleted property: modified
            - Deleted property: name
            - Deleted property: offering
            - Deleted property: offering_backend_id
            - Deleted property: offering_billable
            - Deleted property: offering_components
            - Deleted property: offering_description
            - Deleted property: offering_image
            - Deleted property: offering_name
            - Deleted property: offering_plugin_options
            - Deleted property: offering_shared
            - Deleted property: offering_slug
            - Deleted property: offering_state
            - Deleted property: offering_thumbnail
            - Deleted property: offering_type
            - Deleted property: offering_uuid
            - Deleted property: options
            - Deleted property: order_in_progress
            - Deleted property: parent_name
            - Deleted property: parent_offering_name
            - Deleted property: parent_offering_slug
            - Deleted property: parent_offering_uuid
            - Deleted property: parent_uuid
            - Deleted property: paused
            - Deleted property: plan
            - Deleted property: plan_description
            - Deleted property: plan_name
            - Deleted property: plan_unit
            - Deleted property: plan_uuid
            - Deleted property: project
            - Deleted property: project_description
            - Deleted property: project_effective_end_date
            - Deleted property: project_end_date
            - Deleted property: project_end_date_requested_by
            - Deleted property: project_is_in_grace_period
            - Deleted property: project_name
            - Deleted property: project_slug
            - Deleted property: project_uuid
            - Deleted property: provider_description
            - Deleted property: provider_name
            - Deleted property: provider_slug
            - Deleted property: provider_uuid
            - Deleted property: renewal_date
            - Deleted property: report
            - Deleted property: resource_type
            - Deleted property: resource_uuid
            - Deleted property: restrict_member_access
            - Deleted property: scope
            - Deleted property: service_settings_uuid
            - Deleted property: slots
            - Deleted property: slug
            - Deleted property: state
            - Deleted property: url
            - Deleted property: user_requires_reconsent
            - Deleted property: username
            - Deleted property: uuid

GET /api/broadcast-messages/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: emails
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: query
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/QueryOutput
                - ReadOnly changed from false to true

POST /api/broadcast-messages/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: query
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/BroadcastMessageQueryRequest
            - WriteOnly changed from false to true
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: emails
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: query
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/QueryOutput
              - ReadOnly changed from false to true

GET /api/broadcast-messages/recipients/

- Deleted query param: field
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: customers
            - New required property: email
            - New required property: offerings
          - Properties changed
            - New property: customers
            - New property: email
            - New property: full_name
            - New property: offerings
            - Deleted property: author_full_name
            - Deleted property: body
            - Deleted property: created
            - Deleted property: emails
            - Deleted property: query
            - Deleted property: send_at
            - Deleted property: state
            - Deleted property: subject
            - Deleted property: uuid

GET /api/broadcast-messages/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: emails
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: query
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/QueryOutput
              - ReadOnly changed from false to true

PATCH /api/broadcast-messages/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: query
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: emails
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: query
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/QueryOutput
              - ReadOnly changed from false to true

PUT /api/broadcast-messages/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: query
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/BroadcastMessageQueryRequest
            - WriteOnly changed from false to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: emails
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: query
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/QueryOutput
              - ReadOnly changed from false to true

PATCH /api/call-reviewer-pools/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'manager' to 'call'
    - Added /0/scopes/- with value: 'call.manager'

POST /api/call-reviewer-pools/{uuid}/force-accept/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'call.manager' to 'call'
    - Added /0/scopes/- with value: 'call.manager'

GET /api/celery-stats/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: active
              - AdditionalProperties changed
                - Items changed
                  - Properties changed
                    - Modified property: args
                      - Items changed
                        - Type changed from '' to 'object'
                        - AdditionalProperties changed from null to true
            - Modified property: reserved
              - AdditionalProperties changed
                - Items changed
                  - Properties changed
                    - Modified property: args
                      - Items changed
                        - Type changed from '' to 'object'
                        - AdditionalProperties changed from null to true
            - Modified property: scheduled
              - AdditionalProperties changed
                - Items changed
                  - Properties changed
                    - Modified property: request
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/CeleryTask
                          - Properties changed
                            - Modified property: args
                              - Items changed
                                - Type changed from '' to 'object'
                                - AdditionalProperties changed from null to true

GET /api/chat-messages/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - Deleted required property: action_taken
              - Deleted required property: injection_categories
              - Deleted required property: is_flagged
              - Deleted required property: pii_categories
              - Deleted required property: severity
            - Properties changed
              - Modified property: injection_categories
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: pii_categories
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

POST /api/chat-messages/{uuid}/feedback/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: action_taken
            - Deleted required property: injection_categories
            - Deleted required property: is_flagged
            - Deleted required property: pii_categories
            - Deleted required property: severity
          - Properties changed
            - Modified property: injection_categories
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: pii_categories
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/chat-sessions/current/

- New query param: field

GET /api/chat-threads/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: flags
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

GET /api/chat-threads/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: flags
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

POST /api/chat-tools/execute/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: arguments
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true

GET /api/checklists-admin-question-dependencies/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - Deleted required property: required_answer_value
            - Properties changed
              - Modified property: required_answer_value
                - Description changed from 'The answer value(s) that make this question visible' to ''

POST /api/checklists-admin-question-dependencies/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: required_answer_value
        - Properties changed
          - Modified property: required_answer_value
            - Description changed from 'The answer value(s) that make this question visible' to ''
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: required_answer_value
          - Properties changed
            - Modified property: required_answer_value
              - Description changed from 'The answer value(s) that make this question visible' to ''

GET /api/checklists-admin-question-dependencies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: required_answer_value
          - Properties changed
            - Modified property: required_answer_value
              - Description changed from 'The answer value(s) that make this question visible' to ''

PATCH /api/checklists-admin-question-dependencies/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: required_answer_value
            - Description changed from 'The answer value(s) that make this question visible' to ''
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: required_answer_value
          - Properties changed
            - Modified property: required_answer_value
              - Description changed from 'The answer value(s) that make this question visible' to ''

PUT /api/checklists-admin-question-dependencies/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: required_answer_value
        - Properties changed
          - Modified property: required_answer_value
            - Description changed from 'The answer value(s) that make this question visible' to ''
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: required_answer_value
          - Properties changed
            - Modified property: required_answer_value
              - Description changed from 'The answer value(s) that make this question visible' to ''

GET /api/checklists-admin-questions/

- Modified query param: checklist_type
  - Schema changed
    - New enum values: [workflow_step]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: likert_allow_na
              - New property: likert_high_label
              - New property: likert_low_label
              - New property: likert_scale_length
              - New property: rich_text_char_limit
              - New property: rich_text_toolbar_level
              - Modified property: allowed_file_types
                - Type changed from '' to 'array'
                - Description changed from 'List of allowed file extensions (e.g., ['.pdf', '.doc', '.docx']). If empty, all file types are allowed.' to ''
                - Items changed
                  - Schema added
              - Modified property: allowed_mime_types
                - Type changed from '' to 'array'
                - Description changed from 'List of allowed MIME types (e.g., ['application/pdf', 'application/msword']). If empty, MIME type validation is not enforced. When both extensions and MIME types are specified, files must match both criteria for security.' to ''
                - Items changed
                  - Schema added
              - Modified property: guidance_answer_value
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: question_type
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/QuestionTypeEnum
                    - New enum values: [likert rich_text]
              - Modified property: review_answer_value
                - Description changed from 'Answer value that trigger review.' to ''
                - Nullable changed from true to false

HEAD /api/checklists-admin-questions/

- Modified query param: checklist_type
  - Schema changed
    - New enum values: [workflow_step]

POST /api/checklists-admin-questions/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: likert_allow_na
          - New property: likert_high_label
          - New property: likert_low_label
          - New property: likert_scale_length
          - New property: rich_text_char_limit
          - New property: rich_text_toolbar_level
          - Modified property: allowed_file_types
            - Type changed from '' to 'array'
            - Description changed from 'List of allowed file extensions (e.g., ['.pdf', '.doc', '.docx']). If empty, all file types are allowed.' to ''
            - Items changed
              - Schema added
          - Modified property: allowed_mime_types
            - Type changed from '' to 'array'
            - Description changed from 'List of allowed MIME types (e.g., ['application/pdf', 'application/msword']). If empty, MIME type validation is not enforced. When both extensions and MIME types are specified, files must match both criteria for security.' to ''
            - Items changed
              - Schema added
          - Modified property: guidance_answer_value
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: question_type
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/QuestionTypeEnum
                - New enum values: [likert rich_text]
          - Modified property: review_answer_value
            - Description changed from 'Answer value that trigger review.' to ''
            - Nullable changed from true to false
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: likert_allow_na
            - New property: likert_high_label
            - New property: likert_low_label
            - New property: likert_scale_length
            - New property: rich_text_char_limit
            - New property: rich_text_toolbar_level
            - Modified property: allowed_file_types
              - Type changed from '' to 'array'
              - Description changed from 'List of allowed file extensions (e.g., ['.pdf', '.doc', '.docx']). If empty, all file types are allowed.' to ''
              - Items changed
                - Schema added
            - Modified property: allowed_mime_types
              - Type changed from '' to 'array'
              - Description changed from 'List of allowed MIME types (e.g., ['application/pdf', 'application/msword']). If empty, MIME type validation is not enforced. When both extensions and MIME types are specified, files must match both criteria for security.' to ''
              - Items changed
                - Schema added
            - Modified property: guidance_answer_value
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: question_type
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/QuestionTypeEnum
                  - New enum values: [likert rich_text]
            - Modified property: review_answer_value
              - Description changed from 'Answer value that trigger review.' to ''
              - Nullable changed from true to false

GET /api/checklists-admin-questions/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: likert_allow_na
            - New property: likert_high_label
            - New property: likert_low_label
            - New property: likert_scale_length
            - New property: rich_text_char_limit
            - New property: rich_text_toolbar_level
            - Modified property: allowed_file_types
              - Type changed from '' to 'array'
              - Description changed from 'List of allowed file extensions (e.g., ['.pdf', '.doc', '.docx']). If empty, all file types are allowed.' to ''
              - Items changed
                - Schema added
            - Modified property: allowed_mime_types
              - Type changed from '' to 'array'
              - Description changed from 'List of allowed MIME types (e.g., ['application/pdf', 'application/msword']). If empty, MIME type validation is not enforced. When both extensions and MIME types are specified, files must match both criteria for security.' to ''
              - Items changed
                - Schema added
            - Modified property: guidance_answer_value
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: question_type
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/QuestionTypeEnum
                  - New enum values: [likert rich_text]
            - Modified property: review_answer_value
              - Description changed from 'Answer value that trigger review.' to ''
              - Nullable changed from true to false

PATCH /api/checklists-admin-questions/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: likert_allow_na
          - New property: likert_high_label
          - New property: likert_low_label
          - New property: likert_scale_length
          - New property: rich_text_char_limit
          - New property: rich_text_toolbar_level
          - Modified property: allowed_file_types
            - Type changed from '' to 'array'
            - Description changed from 'List of allowed file extensions (e.g., ['.pdf', '.doc', '.docx']). If empty, all file types are allowed.' to ''
            - Items changed
              - Schema added
          - Modified property: allowed_mime_types
            - Type changed from '' to 'array'
            - Description changed from 'List of allowed MIME types (e.g., ['application/pdf', 'application/msword']). If empty, MIME type validation is not enforced. When both extensions and MIME types are specified, files must match both criteria for security.' to ''
            - Items changed
              - Schema added
          - Modified property: guidance_answer_value
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: question_type
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/QuestionTypeEnum
                - New enum values: [likert rich_text]
          - Modified property: review_answer_value
            - Description changed from 'Answer value that trigger review.' to ''
            - Nullable changed from true to false
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: likert_allow_na
            - New property: likert_high_label
            - New property: likert_low_label
            - New property: likert_scale_length
            - New property: rich_text_char_limit
            - New property: rich_text_toolbar_level
            - Modified property: allowed_file_types
              - Type changed from '' to 'array'
              - Description changed from 'List of allowed file extensions (e.g., ['.pdf', '.doc', '.docx']). If empty, all file types are allowed.' to ''
              - Items changed
                - Schema added
            - Modified property: allowed_mime_types
              - Type changed from '' to 'array'
              - Description changed from 'List of allowed MIME types (e.g., ['application/pdf', 'application/msword']). If empty, MIME type validation is not enforced. When both extensions and MIME types are specified, files must match both criteria for security.' to ''
              - Items changed
                - Schema added
            - Modified property: guidance_answer_value
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: question_type
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/QuestionTypeEnum
                  - New enum values: [likert rich_text]
            - Modified property: review_answer_value
              - Description changed from 'Answer value that trigger review.' to ''
              - Nullable changed from true to false

PUT /api/checklists-admin-questions/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: likert_allow_na
          - New property: likert_high_label
          - New property: likert_low_label
          - New property: likert_scale_length
          - New property: rich_text_char_limit
          - New property: rich_text_toolbar_level
          - Modified property: allowed_file_types
            - Type changed from '' to 'array'
            - Description changed from 'List of allowed file extensions (e.g., ['.pdf', '.doc', '.docx']). If empty, all file types are allowed.' to ''
            - Items changed
              - Schema added
          - Modified property: allowed_mime_types
            - Type changed from '' to 'array'
            - Description changed from 'List of allowed MIME types (e.g., ['application/pdf', 'application/msword']). If empty, MIME type validation is not enforced. When both extensions and MIME types are specified, files must match both criteria for security.' to ''
            - Items changed
              - Schema added
          - Modified property: guidance_answer_value
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: question_type
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/QuestionTypeEnum
                - New enum values: [likert rich_text]
          - Modified property: review_answer_value
            - Description changed from 'Answer value that trigger review.' to ''
            - Nullable changed from true to false
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: likert_allow_na
            - New property: likert_high_label
            - New property: likert_low_label
            - New property: likert_scale_length
            - New property: rich_text_char_limit
            - New property: rich_text_toolbar_level
            - Modified property: allowed_file_types
              - Type changed from '' to 'array'
              - Description changed from 'List of allowed file extensions (e.g., ['.pdf', '.doc', '.docx']). If empty, all file types are allowed.' to ''
              - Items changed
                - Schema added
            - Modified property: allowed_mime_types
              - Type changed from '' to 'array'
              - Description changed from 'List of allowed MIME types (e.g., ['application/pdf', 'application/msword']). If empty, MIME type validation is not enforced. When both extensions and MIME types are specified, files must match both criteria for security.' to ''
              - Items changed
                - Schema added
            - Modified property: guidance_answer_value
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: question_type
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/QuestionTypeEnum
                  - New enum values: [likert rich_text]
            - Modified property: review_answer_value
              - Description changed from 'Answer value that trigger review.' to ''
              - Nullable changed from true to false

GET /api/checklists-admin/

- Modified query param: checklist_type
  - Schema changed
    - New enum values: [workflow_step]
- Modified query param: checklist_type__in
  - Schema changed
    - Items changed
      - New enum values: [workflow_step]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: checklist_type
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/ChecklistTypeEnum
                    - New enum values: [workflow_step]

HEAD /api/checklists-admin/

- Modified query param: checklist_type
  - Schema changed
    - New enum values: [workflow_step]
- Modified query param: checklist_type__in
  - Schema changed
    - Items changed
      - New enum values: [workflow_step]

POST /api/checklists-admin/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: checklist_type
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/ChecklistTypeEnum
                - New enum values: [workflow_step]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: checklist_type
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ChecklistTypeEnum
                  - New enum values: [workflow_step]

GET /api/checklists-admin/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: checklist_type
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ChecklistTypeEnum
                  - New enum values: [workflow_step]

PATCH /api/checklists-admin/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: checklist_type
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/ChecklistTypeEnum
                - New enum values: [workflow_step]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: checklist_type
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ChecklistTypeEnum
                  - New enum values: [workflow_step]

PUT /api/checklists-admin/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: checklist_type
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/ChecklistTypeEnum
                - New enum values: [workflow_step]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: checklist_type
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ChecklistTypeEnum
                  - New enum values: [workflow_step]

GET /api/checklists-admin/{uuid}/questions/

- Modified query param: checklist_type
  - Schema changed
    - New enum values: [workflow_step]
- Modified query param: checklist_type__in
  - Schema changed
    - Items changed
      - New enum values: [workflow_step]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: likert_allow_na
              - New property: likert_high_label
              - New property: likert_low_label
              - New property: likert_scale_length
              - New property: rich_text_char_limit
              - New property: rich_text_toolbar_level
              - Modified property: allowed_file_types
                - Type changed from '' to 'array'
                - Description changed from 'List of allowed file extensions (e.g., ['.pdf', '.doc', '.docx']). If empty, all file types are allowed.' to ''
                - Items changed
                  - Schema added
              - Modified property: allowed_mime_types
                - Type changed from '' to 'array'
                - Description changed from 'List of allowed MIME types (e.g., ['application/pdf', 'application/msword']). If empty, MIME type validation is not enforced. When both extensions and MIME types are specified, files must match both criteria for security.' to ''
                - Items changed
                  - Schema added
              - Modified property: guidance_answer_value
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: question_type
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/QuestionTypeEnum
                    - New enum values: [likert rich_text]
              - Modified property: review_answer_value
                - Description changed from 'Answer value that trigger review.' to ''
                - Nullable changed from true to false

GET /api/coi-disclosures/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: personal_relationships
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

POST /api/coi-disclosures/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: personal_relationships
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: personal_relationships
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/coi-disclosures/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: personal_relationships
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/conflicts-of-interest/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: evidence_data
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

GET /api/conflicts-of-interest/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: evidence_data
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PATCH /api/conflicts-of-interest/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: evidence_data
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PUT /api/conflicts-of-interest/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: evidence_data
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

POST /api/conflicts-of-interest/{uuid}/dismiss/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: evidence_data
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

POST /api/conflicts-of-interest/{uuid}/recuse/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: evidence_data
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

POST /api/conflicts-of-interest/{uuid}/waive/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: evidence_data
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

POST /api/customer-credits/{uuid}/apply_compensations/

- Responses changed
  - Modified response: 200
    - Description changed from '' to 'No response body'
    - Content changed
      - Deleted media type: application/json

POST /api/customer-credits/{uuid}/clear_compensations/

- Responses changed
  - Modified response: 200
    - Description changed from '' to 'No response body'
    - Content changed
      - Deleted media type: application/json

GET /api/customers/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [default_affiliations]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: default_affiliations
              - Modified property: user_affiliations
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: user_email_patterns
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: user_identity_sources
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

POST /api/customers/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: user_affiliations
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_email_patterns
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_identity_sources
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: user_affiliations
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_email_patterns
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_identity_sources
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: user_affiliations
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_email_patterns
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_identity_sources
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: default_affiliations
            - Modified property: user_affiliations
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_email_patterns
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_identity_sources
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/customers/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [default_affiliations]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: default_affiliations
            - Modified property: user_affiliations
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_email_patterns
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_identity_sources
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PATCH /api/customers/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: user_affiliations
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_email_patterns
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_identity_sources
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: user_affiliations
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_email_patterns
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_identity_sources
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: user_affiliations
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_email_patterns
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_identity_sources
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: default_affiliations
            - Modified property: user_affiliations
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_email_patterns
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_identity_sources
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PUT /api/customers/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: user_affiliations
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_email_patterns
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_identity_sources
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: user_affiliations
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_email_patterns
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_identity_sources
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: user_affiliations
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_email_patterns
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_identity_sources
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: default_affiliations
            - Modified property: user_affiliations
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_email_patterns
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_identity_sources
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/customers/{uuid}/project-digest-config/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: available_sections
              - Items changed
                - Required changed
                  - New required property: key
                  - New required property: title
                - Properties changed
                  - New property: key
                  - New property: title
                - AdditionalProperties changed
                  - Schema deleted

PATCH /api/customers/{uuid}/update-project-digest-config/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: available_sections
              - Items changed
                - Required changed
                  - New required property: key
                  - New required property: title
                - Properties changed
                  - New property: key
                  - New property: title
                - AdditionalProperties changed
                  - Schema deleted

PUT /api/customers/{uuid}/update-project-digest-config/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: available_sections
              - Items changed
                - Required changed
                  - New required property: key
                  - New required property: title
                - Properties changed
                  - New property: key
                  - New property: title
                - AdditionalProperties changed
                  - Schema deleted

POST /api/debug/pubsub/metrics_reset/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: status
              - Description changed from 'Operation status' to ''
              - ReadOnly changed from true to false

POST /api/digitalocean-droplets/{uuid}/resize/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/digitalocean-droplets/{uuid}/restart/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/digitalocean-droplets/{uuid}/start/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/digitalocean-droplets/{uuid}/stop/

- Responses changed
  - New response: 202
  - Deleted response: 200

GET /api/event-subscriptions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: observable_objects
                - Type changed from '' to 'array'
                - Items changed
                  - Schema added

POST /api/event-subscriptions/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: observable_objects
            - Type changed from '' to 'array'
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: observable_objects
              - Type changed from '' to 'array'
              - Items changed
                - Schema added

GET /api/event-subscriptions/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: observable_objects
              - Type changed from '' to 'array'
              - Items changed
                - Schema added

POST /api/event-subscriptions/{uuid}/create_queue/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: object_type
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/ObservableObjectTypeEnum
                - New enum values: [offering_resources_sync]

GET /api/events/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: context
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

GET /api/events/count/

- Deleted query param: field
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: count
          - Properties changed
            - New property: count
            - Deleted property: context
            - Deleted property: created
            - Deleted property: event_type
            - Deleted property: message
            - Deleted property: uuid

GET /api/events/event_groups/

- Deleted query param: field
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: context
            - Deleted property: created
            - Deleted property: event_type
            - Deleted property: message
            - Deleted property: uuid
          - AdditionalProperties changed
            - Schema added

GET /api/events/scope_types/

- Deleted query param: field
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Type changed from 'object' to 'array'
          - Items changed
            - Schema added
          - Properties changed
            - Deleted property: context
            - Deleted property: created
            - Deleted property: event_type
            - Deleted property: message
            - Deleted property: uuid

GET /api/events/{id}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: context
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/google-auth/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: allowed_domains
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

GET /api/google-auth/callback/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

GET /api/google-auth/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: allowed_domains
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/google-auth/{uuid}/authorize/

- Deleted query param: field
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: request_url
          - Properties changed
            - New property: request_url
            - Deleted property: allowed_domains
            - Deleted property: calendar_refresh_token
            - Deleted property: calendar_token
            - Deleted property: created
            - Deleted property: customer
            - Deleted property: customer_abbreviation
            - Deleted property: customer_country
            - Deleted property: customer_image
            - Deleted property: customer_name
            - Deleted property: customer_native_name
            - Deleted property: customer_slug
            - Deleted property: customer_uuid
            - Deleted property: description
            - Deleted property: enable_notifications
            - Deleted property: google_auth_url
            - Deleted property: image
            - Deleted property: offering_count
            - Deleted property: organization_groups
            - Deleted property: url
            - Deleted property: uuid

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
                  - New enum values: [openstack_floating_ip openstack_network openstack_port openstack_rbac openstack_router openstack_security_group openstack_subnet]
              - Modified property: event_types
                - Items changed
                  - New enum values: [marketplace_offering_options_updated marketplace_offering_resource_options_updated marketplace_resource_limit_change_request_created marketplace_resource_limit_change_request_approved marketplace_resource_limit_change_request_rejected openstack_instance_security_groups_changed openstack_load_balancer_created openstack_load_balancer_updated openstack_load_balancer_deleted openstack_load_balancer_security_groups_changed openstack_listener_created openstack_listener_updated openstack_listener_deleted openstack_pool_created openstack_pool_updated openstack_pool_deleted openstack_pool_member_created openstack_pool_member_updated openstack_pool_member_deleted openstack_port_security_enabled openstack_port_security_disabled openstack_port_allowed_address_pairs_changed openstack_port_security_groups_changed openstack_rbac_policy_created openstack_rbac_policy_deleted openstack_router_interface_added openstack_router_interface_removed openstack_subnet_host_routes_changed openstack_security_group_rules_changed proposal_workflow_advanced resource_rescue_failed resource_rescue_scheduled resource_rescue_succeeded resource_unrescue_failed resource_unrescue_scheduled resource_unrescue_succeeded]

POST /api/hooks-email/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_groups
            - Items changed
              - New enum values: [openstack_floating_ip openstack_network openstack_port openstack_rbac openstack_router openstack_security_group openstack_subnet]
          - Modified property: event_types
            - Items changed
              - New enum values: [marketplace_offering_options_updated marketplace_offering_resource_options_updated marketplace_resource_limit_change_request_created marketplace_resource_limit_change_request_approved marketplace_resource_limit_change_request_rejected openstack_instance_security_groups_changed openstack_load_balancer_created openstack_load_balancer_updated openstack_load_balancer_deleted openstack_load_balancer_security_groups_changed openstack_listener_created openstack_listener_updated openstack_listener_deleted openstack_pool_created openstack_pool_updated openstack_pool_deleted openstack_pool_member_created openstack_pool_member_updated openstack_pool_member_deleted openstack_port_security_enabled openstack_port_security_disabled openstack_port_allowed_address_pairs_changed openstack_port_security_groups_changed openstack_rbac_policy_created openstack_rbac_policy_deleted openstack_router_interface_added openstack_router_interface_removed openstack_subnet_host_routes_changed openstack_security_group_rules_changed proposal_workflow_advanced resource_rescue_failed resource_rescue_scheduled resource_rescue_succeeded resource_unrescue_failed resource_unrescue_scheduled resource_unrescue_succeeded]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [openstack_floating_ip openstack_network openstack_port openstack_rbac openstack_router openstack_security_group openstack_subnet]
            - Modified property: event_types
              - Items changed
                - New enum values: [marketplace_offering_options_updated marketplace_offering_resource_options_updated marketplace_resource_limit_change_request_created marketplace_resource_limit_change_request_approved marketplace_resource_limit_change_request_rejected openstack_instance_security_groups_changed openstack_load_balancer_created openstack_load_balancer_updated openstack_load_balancer_deleted openstack_load_balancer_security_groups_changed openstack_listener_created openstack_listener_updated openstack_listener_deleted openstack_pool_created openstack_pool_updated openstack_pool_deleted openstack_pool_member_created openstack_pool_member_updated openstack_pool_member_deleted openstack_port_security_enabled openstack_port_security_disabled openstack_port_allowed_address_pairs_changed openstack_port_security_groups_changed openstack_rbac_policy_created openstack_rbac_policy_deleted openstack_router_interface_added openstack_router_interface_removed openstack_subnet_host_routes_changed openstack_security_group_rules_changed proposal_workflow_advanced resource_rescue_failed resource_rescue_scheduled resource_rescue_succeeded resource_unrescue_failed resource_unrescue_scheduled resource_unrescue_succeeded]

GET /api/hooks-email/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [openstack_floating_ip openstack_network openstack_port openstack_rbac openstack_router openstack_security_group openstack_subnet]
            - Modified property: event_types
              - Items changed
                - New enum values: [marketplace_offering_options_updated marketplace_offering_resource_options_updated marketplace_resource_limit_change_request_created marketplace_resource_limit_change_request_approved marketplace_resource_limit_change_request_rejected openstack_instance_security_groups_changed openstack_load_balancer_created openstack_load_balancer_updated openstack_load_balancer_deleted openstack_load_balancer_security_groups_changed openstack_listener_created openstack_listener_updated openstack_listener_deleted openstack_pool_created openstack_pool_updated openstack_pool_deleted openstack_pool_member_created openstack_pool_member_updated openstack_pool_member_deleted openstack_port_security_enabled openstack_port_security_disabled openstack_port_allowed_address_pairs_changed openstack_port_security_groups_changed openstack_rbac_policy_created openstack_rbac_policy_deleted openstack_router_interface_added openstack_router_interface_removed openstack_subnet_host_routes_changed openstack_security_group_rules_changed proposal_workflow_advanced resource_rescue_failed resource_rescue_scheduled resource_rescue_succeeded resource_unrescue_failed resource_unrescue_scheduled resource_unrescue_succeeded]

PATCH /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_groups
            - Items changed
              - New enum values: [openstack_floating_ip openstack_network openstack_port openstack_rbac openstack_router openstack_security_group openstack_subnet]
          - Modified property: event_types
            - Items changed
              - New enum values: [marketplace_offering_options_updated marketplace_offering_resource_options_updated marketplace_resource_limit_change_request_created marketplace_resource_limit_change_request_approved marketplace_resource_limit_change_request_rejected openstack_instance_security_groups_changed openstack_load_balancer_created openstack_load_balancer_updated openstack_load_balancer_deleted openstack_load_balancer_security_groups_changed openstack_listener_created openstack_listener_updated openstack_listener_deleted openstack_pool_created openstack_pool_updated openstack_pool_deleted openstack_pool_member_created openstack_pool_member_updated openstack_pool_member_deleted openstack_port_security_enabled openstack_port_security_disabled openstack_port_allowed_address_pairs_changed openstack_port_security_groups_changed openstack_rbac_policy_created openstack_rbac_policy_deleted openstack_router_interface_added openstack_router_interface_removed openstack_subnet_host_routes_changed openstack_security_group_rules_changed proposal_workflow_advanced resource_rescue_failed resource_rescue_scheduled resource_rescue_succeeded resource_unrescue_failed resource_unrescue_scheduled resource_unrescue_succeeded]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [openstack_floating_ip openstack_network openstack_port openstack_rbac openstack_router openstack_security_group openstack_subnet]
            - Modified property: event_types
              - Items changed
                - New enum values: [marketplace_offering_options_updated marketplace_offering_resource_options_updated marketplace_resource_limit_change_request_created marketplace_resource_limit_change_request_approved marketplace_resource_limit_change_request_rejected openstack_instance_security_groups_changed openstack_load_balancer_created openstack_load_balancer_updated openstack_load_balancer_deleted openstack_load_balancer_security_groups_changed openstack_listener_created openstack_listener_updated openstack_listener_deleted openstack_pool_created openstack_pool_updated openstack_pool_deleted openstack_pool_member_created openstack_pool_member_updated openstack_pool_member_deleted openstack_port_security_enabled openstack_port_security_disabled openstack_port_allowed_address_pairs_changed openstack_port_security_groups_changed openstack_rbac_policy_created openstack_rbac_policy_deleted openstack_router_interface_added openstack_router_interface_removed openstack_subnet_host_routes_changed openstack_security_group_rules_changed proposal_workflow_advanced resource_rescue_failed resource_rescue_scheduled resource_rescue_succeeded resource_unrescue_failed resource_unrescue_scheduled resource_unrescue_succeeded]

PUT /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_groups
            - Items changed
              - New enum values: [openstack_floating_ip openstack_network openstack_port openstack_rbac openstack_router openstack_security_group openstack_subnet]
          - Modified property: event_types
            - Items changed
              - New enum values: [marketplace_offering_options_updated marketplace_offering_resource_options_updated marketplace_resource_limit_change_request_created marketplace_resource_limit_change_request_approved marketplace_resource_limit_change_request_rejected openstack_instance_security_groups_changed openstack_load_balancer_created openstack_load_balancer_updated openstack_load_balancer_deleted openstack_load_balancer_security_groups_changed openstack_listener_created openstack_listener_updated openstack_listener_deleted openstack_pool_created openstack_pool_updated openstack_pool_deleted openstack_pool_member_created openstack_pool_member_updated openstack_pool_member_deleted openstack_port_security_enabled openstack_port_security_disabled openstack_port_allowed_address_pairs_changed openstack_port_security_groups_changed openstack_rbac_policy_created openstack_rbac_policy_deleted openstack_router_interface_added openstack_router_interface_removed openstack_subnet_host_routes_changed openstack_security_group_rules_changed proposal_workflow_advanced resource_rescue_failed resource_rescue_scheduled resource_rescue_succeeded resource_unrescue_failed resource_unrescue_scheduled resource_unrescue_succeeded]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [openstack_floating_ip openstack_network openstack_port openstack_rbac openstack_router openstack_security_group openstack_subnet]
            - Modified property: event_types
              - Items changed
                - New enum values: [marketplace_offering_options_updated marketplace_offering_resource_options_updated marketplace_resource_limit_change_request_created marketplace_resource_limit_change_request_approved marketplace_resource_limit_change_request_rejected openstack_instance_security_groups_changed openstack_load_balancer_created openstack_load_balancer_updated openstack_load_balancer_deleted openstack_load_balancer_security_groups_changed openstack_listener_created openstack_listener_updated openstack_listener_deleted openstack_pool_created openstack_pool_updated openstack_pool_deleted openstack_pool_member_created openstack_pool_member_updated openstack_pool_member_deleted openstack_port_security_enabled openstack_port_security_disabled openstack_port_allowed_address_pairs_changed openstack_port_security_groups_changed openstack_rbac_policy_created openstack_rbac_policy_deleted openstack_router_interface_added openstack_router_interface_removed openstack_subnet_host_routes_changed openstack_security_group_rules_changed proposal_workflow_advanced resource_rescue_failed resource_rescue_scheduled resource_rescue_succeeded resource_unrescue_failed resource_unrescue_scheduled resource_unrescue_succeeded]

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
                  - New enum values: [openstack_floating_ip openstack_network openstack_port openstack_rbac openstack_router openstack_security_group openstack_subnet]
              - Modified property: event_types
                - Items changed
                  - New enum values: [marketplace_offering_options_updated marketplace_offering_resource_options_updated marketplace_resource_limit_change_request_created marketplace_resource_limit_change_request_approved marketplace_resource_limit_change_request_rejected openstack_instance_security_groups_changed openstack_load_balancer_created openstack_load_balancer_updated openstack_load_balancer_deleted openstack_load_balancer_security_groups_changed openstack_listener_created openstack_listener_updated openstack_listener_deleted openstack_pool_created openstack_pool_updated openstack_pool_deleted openstack_pool_member_created openstack_pool_member_updated openstack_pool_member_deleted openstack_port_security_enabled openstack_port_security_disabled openstack_port_allowed_address_pairs_changed openstack_port_security_groups_changed openstack_rbac_policy_created openstack_rbac_policy_deleted openstack_router_interface_added openstack_router_interface_removed openstack_subnet_host_routes_changed openstack_security_group_rules_changed proposal_workflow_advanced resource_rescue_failed resource_rescue_scheduled resource_rescue_succeeded resource_unrescue_failed resource_unrescue_scheduled resource_unrescue_succeeded]

POST /api/hooks-web/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_groups
            - Items changed
              - New enum values: [openstack_floating_ip openstack_network openstack_port openstack_rbac openstack_router openstack_security_group openstack_subnet]
          - Modified property: event_types
            - Items changed
              - New enum values: [marketplace_offering_options_updated marketplace_offering_resource_options_updated marketplace_resource_limit_change_request_created marketplace_resource_limit_change_request_approved marketplace_resource_limit_change_request_rejected openstack_instance_security_groups_changed openstack_load_balancer_created openstack_load_balancer_updated openstack_load_balancer_deleted openstack_load_balancer_security_groups_changed openstack_listener_created openstack_listener_updated openstack_listener_deleted openstack_pool_created openstack_pool_updated openstack_pool_deleted openstack_pool_member_created openstack_pool_member_updated openstack_pool_member_deleted openstack_port_security_enabled openstack_port_security_disabled openstack_port_allowed_address_pairs_changed openstack_port_security_groups_changed openstack_rbac_policy_created openstack_rbac_policy_deleted openstack_router_interface_added openstack_router_interface_removed openstack_subnet_host_routes_changed openstack_security_group_rules_changed proposal_workflow_advanced resource_rescue_failed resource_rescue_scheduled resource_rescue_succeeded resource_unrescue_failed resource_unrescue_scheduled resource_unrescue_succeeded]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [openstack_floating_ip openstack_network openstack_port openstack_rbac openstack_router openstack_security_group openstack_subnet]
            - Modified property: event_types
              - Items changed
                - New enum values: [marketplace_offering_options_updated marketplace_offering_resource_options_updated marketplace_resource_limit_change_request_created marketplace_resource_limit_change_request_approved marketplace_resource_limit_change_request_rejected openstack_instance_security_groups_changed openstack_load_balancer_created openstack_load_balancer_updated openstack_load_balancer_deleted openstack_load_balancer_security_groups_changed openstack_listener_created openstack_listener_updated openstack_listener_deleted openstack_pool_created openstack_pool_updated openstack_pool_deleted openstack_pool_member_created openstack_pool_member_updated openstack_pool_member_deleted openstack_port_security_enabled openstack_port_security_disabled openstack_port_allowed_address_pairs_changed openstack_port_security_groups_changed openstack_rbac_policy_created openstack_rbac_policy_deleted openstack_router_interface_added openstack_router_interface_removed openstack_subnet_host_routes_changed openstack_security_group_rules_changed proposal_workflow_advanced resource_rescue_failed resource_rescue_scheduled resource_rescue_succeeded resource_unrescue_failed resource_unrescue_scheduled resource_unrescue_succeeded]

GET /api/hooks-web/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [openstack_floating_ip openstack_network openstack_port openstack_rbac openstack_router openstack_security_group openstack_subnet]
            - Modified property: event_types
              - Items changed
                - New enum values: [marketplace_offering_options_updated marketplace_offering_resource_options_updated marketplace_resource_limit_change_request_created marketplace_resource_limit_change_request_approved marketplace_resource_limit_change_request_rejected openstack_instance_security_groups_changed openstack_load_balancer_created openstack_load_balancer_updated openstack_load_balancer_deleted openstack_load_balancer_security_groups_changed openstack_listener_created openstack_listener_updated openstack_listener_deleted openstack_pool_created openstack_pool_updated openstack_pool_deleted openstack_pool_member_created openstack_pool_member_updated openstack_pool_member_deleted openstack_port_security_enabled openstack_port_security_disabled openstack_port_allowed_address_pairs_changed openstack_port_security_groups_changed openstack_rbac_policy_created openstack_rbac_policy_deleted openstack_router_interface_added openstack_router_interface_removed openstack_subnet_host_routes_changed openstack_security_group_rules_changed proposal_workflow_advanced resource_rescue_failed resource_rescue_scheduled resource_rescue_succeeded resource_unrescue_failed resource_unrescue_scheduled resource_unrescue_succeeded]

PATCH /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_groups
            - Items changed
              - New enum values: [openstack_floating_ip openstack_network openstack_port openstack_rbac openstack_router openstack_security_group openstack_subnet]
          - Modified property: event_types
            - Items changed
              - New enum values: [marketplace_offering_options_updated marketplace_offering_resource_options_updated marketplace_resource_limit_change_request_created marketplace_resource_limit_change_request_approved marketplace_resource_limit_change_request_rejected openstack_instance_security_groups_changed openstack_load_balancer_created openstack_load_balancer_updated openstack_load_balancer_deleted openstack_load_balancer_security_groups_changed openstack_listener_created openstack_listener_updated openstack_listener_deleted openstack_pool_created openstack_pool_updated openstack_pool_deleted openstack_pool_member_created openstack_pool_member_updated openstack_pool_member_deleted openstack_port_security_enabled openstack_port_security_disabled openstack_port_allowed_address_pairs_changed openstack_port_security_groups_changed openstack_rbac_policy_created openstack_rbac_policy_deleted openstack_router_interface_added openstack_router_interface_removed openstack_subnet_host_routes_changed openstack_security_group_rules_changed proposal_workflow_advanced resource_rescue_failed resource_rescue_scheduled resource_rescue_succeeded resource_unrescue_failed resource_unrescue_scheduled resource_unrescue_succeeded]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [openstack_floating_ip openstack_network openstack_port openstack_rbac openstack_router openstack_security_group openstack_subnet]
            - Modified property: event_types
              - Items changed
                - New enum values: [marketplace_offering_options_updated marketplace_offering_resource_options_updated marketplace_resource_limit_change_request_created marketplace_resource_limit_change_request_approved marketplace_resource_limit_change_request_rejected openstack_instance_security_groups_changed openstack_load_balancer_created openstack_load_balancer_updated openstack_load_balancer_deleted openstack_load_balancer_security_groups_changed openstack_listener_created openstack_listener_updated openstack_listener_deleted openstack_pool_created openstack_pool_updated openstack_pool_deleted openstack_pool_member_created openstack_pool_member_updated openstack_pool_member_deleted openstack_port_security_enabled openstack_port_security_disabled openstack_port_allowed_address_pairs_changed openstack_port_security_groups_changed openstack_rbac_policy_created openstack_rbac_policy_deleted openstack_router_interface_added openstack_router_interface_removed openstack_subnet_host_routes_changed openstack_security_group_rules_changed proposal_workflow_advanced resource_rescue_failed resource_rescue_scheduled resource_rescue_succeeded resource_unrescue_failed resource_unrescue_scheduled resource_unrescue_succeeded]

PUT /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_groups
            - Items changed
              - New enum values: [openstack_floating_ip openstack_network openstack_port openstack_rbac openstack_router openstack_security_group openstack_subnet]
          - Modified property: event_types
            - Items changed
              - New enum values: [marketplace_offering_options_updated marketplace_offering_resource_options_updated marketplace_resource_limit_change_request_created marketplace_resource_limit_change_request_approved marketplace_resource_limit_change_request_rejected openstack_instance_security_groups_changed openstack_load_balancer_created openstack_load_balancer_updated openstack_load_balancer_deleted openstack_load_balancer_security_groups_changed openstack_listener_created openstack_listener_updated openstack_listener_deleted openstack_pool_created openstack_pool_updated openstack_pool_deleted openstack_pool_member_created openstack_pool_member_updated openstack_pool_member_deleted openstack_port_security_enabled openstack_port_security_disabled openstack_port_allowed_address_pairs_changed openstack_port_security_groups_changed openstack_rbac_policy_created openstack_rbac_policy_deleted openstack_router_interface_added openstack_router_interface_removed openstack_subnet_host_routes_changed openstack_security_group_rules_changed proposal_workflow_advanced resource_rescue_failed resource_rescue_scheduled resource_rescue_succeeded resource_unrescue_failed resource_unrescue_scheduled resource_unrescue_succeeded]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [openstack_floating_ip openstack_network openstack_port openstack_rbac openstack_router openstack_security_group openstack_subnet]
            - Modified property: event_types
              - Items changed
                - New enum values: [marketplace_offering_options_updated marketplace_offering_resource_options_updated marketplace_resource_limit_change_request_created marketplace_resource_limit_change_request_approved marketplace_resource_limit_change_request_rejected openstack_instance_security_groups_changed openstack_load_balancer_created openstack_load_balancer_updated openstack_load_balancer_deleted openstack_load_balancer_security_groups_changed openstack_listener_created openstack_listener_updated openstack_listener_deleted openstack_pool_created openstack_pool_updated openstack_pool_deleted openstack_pool_member_created openstack_pool_member_updated openstack_pool_member_deleted openstack_port_security_enabled openstack_port_security_disabled openstack_port_allowed_address_pairs_changed openstack_port_security_groups_changed openstack_rbac_policy_created openstack_rbac_policy_deleted openstack_router_interface_added openstack_router_interface_removed openstack_subnet_host_routes_changed openstack_security_group_rules_changed proposal_workflow_advanced resource_rescue_failed resource_rescue_scheduled resource_rescue_succeeded resource_unrescue_failed resource_unrescue_scheduled resource_unrescue_succeeded]

GET /api/identity-providers/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - Deleted required property: auth_url
              - Deleted required property: client_id
              - Deleted required property: client_secret
              - Deleted required property: discovery_url
              - Deleted required property: logout_url
              - Deleted required property: token_url
              - Deleted required property: userinfo_url
            - Properties changed
              - Modified property: allowed_redirects
                - Type changed from '' to 'array'
                - Description changed from 'List of allowed redirect URLs for OAuth authentication. URLs must be exact matches (origin only: scheme + domain + port). HTTPS required except for localhost. No wildcards, paths, query params, or fragments. Example: ["https://portal1.example.com", "https://portal2.example.com:8443"]. If empty, falls back to HOMEPORT_URL setting.' to ''
                - Items changed
                  - Schema added
              - Modified property: attribute_mapping
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: protected_fields
                - Type changed from '' to 'array'
                - Items changed
                  - Schema added

POST /api/identity-providers/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: allowed_redirects
            - Type changed from '' to 'array'
            - Description changed from 'List of allowed redirect URLs for OAuth authentication. URLs must be exact matches (origin only: scheme + domain + port). HTTPS required except for localhost. No wildcards, paths, query params, or fragments. Example: ["https://portal1.example.com", "https://portal2.example.com:8443"]. If empty, falls back to HOMEPORT_URL setting.' to ''
            - Items changed
              - Schema added
          - Modified property: attribute_mapping
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: protected_fields
            - Type changed from '' to 'array'
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: auth_url
            - Deleted required property: client_id
            - Deleted required property: client_secret
            - Deleted required property: discovery_url
            - Deleted required property: logout_url
            - Deleted required property: token_url
            - Deleted required property: userinfo_url
          - Properties changed
            - Modified property: allowed_redirects
              - Type changed from '' to 'array'
              - Description changed from 'List of allowed redirect URLs for OAuth authentication. URLs must be exact matches (origin only: scheme + domain + port). HTTPS required except for localhost. No wildcards, paths, query params, or fragments. Example: ["https://portal1.example.com", "https://portal2.example.com:8443"]. If empty, falls back to HOMEPORT_URL setting.' to ''
              - Items changed
                - Schema added
            - Modified property: attribute_mapping
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: protected_fields
              - Type changed from '' to 'array'
              - Items changed
                - Schema added

POST /api/identity-providers/discover_metadata/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: endpoints
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/OidcEndpoints
              - Type changed from 'object' to ''
              - AdditionalProperties changed
                - Schema deleted

GET /api/identity-providers/{provider}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: auth_url
            - Deleted required property: client_id
            - Deleted required property: client_secret
            - Deleted required property: discovery_url
            - Deleted required property: logout_url
            - Deleted required property: token_url
            - Deleted required property: userinfo_url
          - Properties changed
            - Modified property: allowed_redirects
              - Type changed from '' to 'array'
              - Description changed from 'List of allowed redirect URLs for OAuth authentication. URLs must be exact matches (origin only: scheme + domain + port). HTTPS required except for localhost. No wildcards, paths, query params, or fragments. Example: ["https://portal1.example.com", "https://portal2.example.com:8443"]. If empty, falls back to HOMEPORT_URL setting.' to ''
              - Items changed
                - Schema added
            - Modified property: attribute_mapping
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: protected_fields
              - Type changed from '' to 'array'
              - Items changed
                - Schema added

PATCH /api/identity-providers/{provider}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: allowed_redirects
            - Type changed from '' to 'array'
            - Description changed from 'List of allowed redirect URLs for OAuth authentication. URLs must be exact matches (origin only: scheme + domain + port). HTTPS required except for localhost. No wildcards, paths, query params, or fragments. Example: ["https://portal1.example.com", "https://portal2.example.com:8443"]. If empty, falls back to HOMEPORT_URL setting.' to ''
            - Items changed
              - Schema added
          - Modified property: attribute_mapping
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: protected_fields
            - Type changed from '' to 'array'
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: auth_url
            - Deleted required property: client_id
            - Deleted required property: client_secret
            - Deleted required property: discovery_url
            - Deleted required property: logout_url
            - Deleted required property: token_url
            - Deleted required property: userinfo_url
          - Properties changed
            - Modified property: allowed_redirects
              - Type changed from '' to 'array'
              - Description changed from 'List of allowed redirect URLs for OAuth authentication. URLs must be exact matches (origin only: scheme + domain + port). HTTPS required except for localhost. No wildcards, paths, query params, or fragments. Example: ["https://portal1.example.com", "https://portal2.example.com:8443"]. If empty, falls back to HOMEPORT_URL setting.' to ''
              - Items changed
                - Schema added
            - Modified property: attribute_mapping
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: protected_fields
              - Type changed from '' to 'array'
              - Items changed
                - Schema added

PUT /api/identity-providers/{provider}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: allowed_redirects
            - Type changed from '' to 'array'
            - Description changed from 'List of allowed redirect URLs for OAuth authentication. URLs must be exact matches (origin only: scheme + domain + port). HTTPS required except for localhost. No wildcards, paths, query params, or fragments. Example: ["https://portal1.example.com", "https://portal2.example.com:8443"]. If empty, falls back to HOMEPORT_URL setting.' to ''
            - Items changed
              - Schema added
          - Modified property: attribute_mapping
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: protected_fields
            - Type changed from '' to 'array'
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: auth_url
            - Deleted required property: client_id
            - Deleted required property: client_secret
            - Deleted required property: discovery_url
            - Deleted required property: logout_url
            - Deleted required property: token_url
            - Deleted required property: userinfo_url
          - Properties changed
            - Modified property: allowed_redirects
              - Type changed from '' to 'array'
              - Description changed from 'List of allowed redirect URLs for OAuth authentication. URLs must be exact matches (origin only: scheme + domain + port). HTTPS required except for localhost. No wildcards, paths, query params, or fragments. Example: ["https://portal1.example.com", "https://portal2.example.com:8443"]. If empty, falls back to HOMEPORT_URL setting.' to ''
              - Items changed
                - Schema added
            - Modified property: attribute_mapping
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: protected_fields
              - Type changed from '' to 'array'
              - Items changed
                - Schema added

GET /api/invoice-items/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: details
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

GET /api/invoice-items/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: details
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/invoice-items/{uuid}/consumptions/

- OperationID changed from 'invoice_items_consumptions_retrieve' to 'invoice_items_consumptions_list'
- New query param: credit_uuid
- New query param: customer_uuid
- New query param: month
- New query param: offering_uuid
- New query param: page
- New query param: page_size
- New query param: project_uuid
- New query param: resource_uuid
- New query param: start_month
- New query param: start_year
- New query param: year
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Type changed from 'object' to 'array'
          - Items changed
            - Schema added
          - Required changed
            - Deleted required property: customer_name
            - Deleted required property: customer_uuid
            - Deleted required property: invoice
            - Deleted required property: offering_component_type
            - Deleted required property: offering_name
            - Deleted required property: offering_uuid
            - Deleted required property: price
            - Deleted required property: project_name
            - Deleted required property: project_uuid
            - Deleted required property: uuid
          - Properties changed
            - Deleted property: article_code
            - Deleted property: customer_name
            - Deleted property: customer_uuid
            - Deleted property: details
            - Deleted property: end
            - Deleted property: invoice
            - Deleted property: measured_unit
            - Deleted property: name
            - Deleted property: offering_component_type
            - Deleted property: offering_name
            - Deleted property: offering_uuid
            - Deleted property: price
            - Deleted property: project_name
            - Deleted property: project_uuid
            - Deleted property: quantity
            - Deleted property: resource
            - Deleted property: start
            - Deleted property: unit
            - Deleted property: unit_price
            - Deleted property: uuid
    - Headers changed
      - New header: x-result-count

POST /api/invoice-items/{uuid}/create_compensation/

- Responses changed
  - New response: 201
  - Deleted response: 200

POST /api/invoice-items/{uuid}/migrate_to/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: invoice_item_uuid
            - Deleted required property: invoice
          - Properties changed
            - New property: invoice_item_uuid
            - Deleted property: invoice

POST /api/invoice/send-financial-report-by-mail/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/invoices/import_usage/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: errors
              - Items changed
                - Required changed
                  - New required property: customer_name
                  - New required property: reason
                - Properties changed
                  - New property: customer_name
                  - New property: reason
                - AdditionalProperties changed
                  - Schema deleted

POST /api/invoices/{uuid}/paid/

- Responses changed
  - Modified response: 200
    - Description changed from '' to 'No response body'
    - Content changed
      - Deleted media type: application/json

POST /api/invoices/{uuid}/send_notification/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: detail
          - Properties changed
            - New property: detail
            - Deleted property: backend_id
            - Deleted property: compensations
            - Deleted property: customer
            - Deleted property: customer_details
            - Deleted property: due_date
            - Deleted property: incurred_costs
            - Deleted property: invoice_date
            - Deleted property: issuer_details
            - Deleted property: items
            - Deleted property: month
            - Deleted property: number
            - Deleted property: payment_url
            - Deleted property: price
            - Deleted property: reference_number
            - Deleted property: state
            - Deleted property: tax
            - Deleted property: total
            - Deleted property: url
            - Deleted property: uuid
            - Deleted property: year

GET /api/managed-rancher-cluster-resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [end_date_updated_at]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: end_date_updated_at
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: auto_approved
                      - New property: auto_approved_by_rule_uuid
                      - New property: auto_approved_cost_limit_snapshot
                      - Modified property: attributes
                        - Type changed from '' to 'object'
                        - AdditionalProperties changed from null to true
                      - Modified property: offering_plugin_options
                        - Type changed from '' to 'object'
                        - AdditionalProperties changed from null to true
              - Modified property: offering_plugin_options
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: options
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: auto_approved
                      - New property: auto_approved_by_rule_uuid
                      - New property: auto_approved_cost_limit_snapshot
                      - Modified property: attributes
                        - Type changed from '' to 'object'
                        - AdditionalProperties changed from null to true
                      - Modified property: offering_plugin_options
                        - Type changed from '' to 'object'
                        - AdditionalProperties changed from null to true

GET /api/managed-rancher-cluster-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [end_date_updated_at]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: end_date_updated_at
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: auto_approved
                    - New property: auto_approved_by_rule_uuid
                    - New property: auto_approved_cost_limit_snapshot
                    - Modified property: attributes
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: offering_plugin_options
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
            - Modified property: offering_plugin_options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: auto_approved
                    - New property: auto_approved_by_rule_uuid
                    - New property: auto_approved_cost_limit_snapshot
                    - Modified property: attributes
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: offering_plugin_options
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true

POST /api/managed-rancher-cluster-resources/{uuid}/add_node/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: annotations
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: labels
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/marketplace-attributes/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: default
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

POST /api/marketplace-attributes/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: default
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: default
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/marketplace-attributes/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: default
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PATCH /api/marketplace-attributes/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: default
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: default
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PUT /api/marketplace-attributes/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: default
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: default
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/marketplace-categories/

- New query param: o
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: sections
                - Items changed
                  - Properties changed
                    - Modified property: attributes
                      - Items changed
                        - Properties changed
                          - Modified property: default
                            - Type changed from '' to 'object'
                            - AdditionalProperties changed from null to true

HEAD /api/marketplace-categories/

- New query param: o

POST /api/marketplace-categories/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: sections
              - Items changed
                - Properties changed
                  - Modified property: attributes
                    - Items changed
                      - Properties changed
                        - Modified property: default
                          - Type changed from '' to 'object'
                          - AdditionalProperties changed from null to true

GET /api/marketplace-categories/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: sections
              - Items changed
                - Properties changed
                  - Modified property: attributes
                    - Items changed
                      - Properties changed
                        - Modified property: default
                          - Type changed from '' to 'object'
                          - AdditionalProperties changed from null to true

PATCH /api/marketplace-categories/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: sections
              - Items changed
                - Properties changed
                  - Modified property: attributes
                    - Items changed
                      - Properties changed
                        - Modified property: default
                          - Type changed from '' to 'object'
                          - AdditionalProperties changed from null to true

PUT /api/marketplace-categories/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: sections
              - Items changed
                - Properties changed
                  - Modified property: attributes
                    - Items changed
                      - Properties changed
                        - Modified property: default
                          - Type changed from '' to 'object'
                          - AdditionalProperties changed from null to true

GET /api/marketplace-customer-component-usage-policies/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: options
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

POST /api/marketplace-customer-component-usage-policies/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: options
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/marketplace-customer-component-usage-policies/actions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Type changed from 'object' to 'array'
          - Items changed
            - Schema added
          - Required changed
            - Deleted required property: actions
            - Deleted required property: affected_resources_count
            - Deleted required property: component_limits_set
            - Deleted required property: created
            - Deleted required property: created_by_full_name
            - Deleted required property: created_by_username
            - Deleted required property: fired_datetime
            - Deleted required property: has_fired
            - Deleted required property: scope
            - Deleted required property: scope_name
            - Deleted required property: scope_uuid
            - Deleted required property: url
            - Deleted required property: uuid
          - Properties changed
            - Deleted property: actions
            - Deleted property: affected_resources_count
            - Deleted property: component_limits_set
            - Deleted property: created
            - Deleted property: created_by_full_name
            - Deleted property: created_by_username
            - Deleted property: fired_datetime
            - Deleted property: has_fired
            - Deleted property: options
            - Deleted property: scope
            - Deleted property: scope_name
            - Deleted property: scope_uuid
            - Deleted property: url
            - Deleted property: uuid

GET /api/marketplace-customer-component-usage-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PATCH /api/marketplace-customer-component-usage-policies/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: options
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PUT /api/marketplace-customer-component-usage-policies/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: options
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/marketplace-customer-estimated-cost-policies/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: options
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

POST /api/marketplace-customer-estimated-cost-policies/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: options
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/marketplace-customer-estimated-cost-policies/actions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Type changed from 'object' to 'array'
          - Items changed
            - Schema added
          - Required changed
            - Deleted required property: actions
            - Deleted required property: affected_resources_count
            - Deleted required property: billing_price_estimate
            - Deleted required property: created
            - Deleted required property: created_by_full_name
            - Deleted required property: created_by_username
            - Deleted required property: customer_credit
            - Deleted required property: fired_datetime
            - Deleted required property: has_fired
            - Deleted required property: limit_cost
            - Deleted required property: period_name
            - Deleted required property: scope
            - Deleted required property: scope_name
            - Deleted required property: scope_uuid
            - Deleted required property: url
            - Deleted required property: uuid
          - Properties changed
            - Deleted property: actions
            - Deleted property: affected_resources_count
            - Deleted property: billing_price_estimate
            - Deleted property: created
            - Deleted property: created_by_full_name
            - Deleted property: created_by_username
            - Deleted property: customer_credit
            - Deleted property: fired_datetime
            - Deleted property: has_fired
            - Deleted property: limit_cost
            - Deleted property: options
            - Deleted property: period
            - Deleted property: period_name
            - Deleted property: scope
            - Deleted property: scope_name
            - Deleted property: scope_uuid
            - Deleted property: url
            - Deleted property: uuid

GET /api/marketplace-customer-estimated-cost-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PATCH /api/marketplace-customer-estimated-cost-policies/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: options
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PUT /api/marketplace-customer-estimated-cost-policies/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: options
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/marketplace-offering-estimated-cost-policies/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: options
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

POST /api/marketplace-offering-estimated-cost-policies/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: options
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/marketplace-offering-estimated-cost-policies/actions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Type changed from 'object' to 'array'
          - Items changed
            - Schema added
          - Required changed
            - Deleted required property: actions
            - Deleted required property: affected_resources_count
            - Deleted required property: created
            - Deleted required property: created_by_full_name
            - Deleted required property: created_by_username
            - Deleted required property: fired_datetime
            - Deleted required property: has_fired
            - Deleted required property: limit_cost
            - Deleted required property: period_name
            - Deleted required property: scope
            - Deleted required property: scope_name
            - Deleted required property: scope_uuid
            - Deleted required property: url
            - Deleted required property: uuid
          - Properties changed
            - Deleted property: actions
            - Deleted property: affected_resources_count
            - Deleted property: apply_to_all
            - Deleted property: created
            - Deleted property: created_by_full_name
            - Deleted property: created_by_username
            - Deleted property: fired_datetime
            - Deleted property: has_fired
            - Deleted property: limit_cost
            - Deleted property: options
            - Deleted property: organization_groups
            - Deleted property: period
            - Deleted property: period_name
            - Deleted property: scope
            - Deleted property: scope_name
            - Deleted property: scope_uuid
            - Deleted property: url
            - Deleted property: uuid

GET /api/marketplace-offering-estimated-cost-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PATCH /api/marketplace-offering-estimated-cost-policies/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: options
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PUT /api/marketplace-offering-estimated-cost-policies/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: options
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

POST /api/marketplace-offering-profiles/{uuid}/add_role/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: created
            - New required property: modified
            - New required property: name
            - New required property: offerings_count
            - New required property: roles
            - New required property: uuid
            - Deleted required property: role
          - Properties changed
            - New property: created
            - New property: description
            - New property: modified
            - New property: name
            - New property: offerings_count
            - New property: roles
            - New property: uuid
            - Deleted property: role

POST /api/marketplace-offering-profiles/{uuid}/remove_role/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: created
            - New required property: modified
            - New required property: name
            - New required property: offerings_count
            - New required property: roles
            - New required property: uuid
            - Deleted required property: role
          - Properties changed
            - New property: created
            - New property: description
            - New property: modified
            - New property: name
            - New property: offerings_count
            - New property: roles
            - New property: uuid
            - Deleted property: role

GET /api/marketplace-offering-usage-policies/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: options
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

POST /api/marketplace-offering-usage-policies/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: options
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/marketplace-offering-usage-policies/actions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Type changed from 'object' to 'array'
          - Items changed
            - Schema added
          - Required changed
            - Deleted required property: actions
            - Deleted required property: affected_resources_count
            - Deleted required property: component_limits_set
            - Deleted required property: created
            - Deleted required property: created_by_full_name
            - Deleted required property: created_by_username
            - Deleted required property: fired_datetime
            - Deleted required property: has_fired
            - Deleted required property: period_name
            - Deleted required property: scope
            - Deleted required property: scope_name
            - Deleted required property: scope_uuid
            - Deleted required property: url
            - Deleted required property: uuid
          - Properties changed
            - Deleted property: actions
            - Deleted property: affected_resources_count
            - Deleted property: apply_to_all
            - Deleted property: component_limits_set
            - Deleted property: created
            - Deleted property: created_by_full_name
            - Deleted property: created_by_username
            - Deleted property: fired_datetime
            - Deleted property: has_fired
            - Deleted property: options
            - Deleted property: organization_groups
            - Deleted property: period
            - Deleted property: period_name
            - Deleted property: scope
            - Deleted property: scope_name
            - Deleted property: scope_uuid
            - Deleted property: url
            - Deleted property: uuid

GET /api/marketplace-offering-usage-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PATCH /api/marketplace-offering-usage-policies/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: options
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PUT /api/marketplace-offering-usage-policies/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: options
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

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
                  - Schemas added: #/components/schemas/UserChecklistCompletionOfferingUser
                  - Schemas deleted: #/components/schemas/OfferingUser
                - Nullable changed from false to true

GET /api/marketplace-offering-user-checklist-completions/{id}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering_user
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/UserChecklistCompletionOfferingUser
                - Schemas deleted: #/components/schemas/OfferingUser
              - Nullable changed from false to true

GET /api/marketplace-offering-users/

- New query param: runtime_state
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [runtime_state]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: runtime_state
              - Modified property: user_active_isds
                - Type changed from '' to 'array'
                - Items changed
                  - Schema added
              - Modified property: user_affiliations
                - Type changed from '' to 'array'
                - Items changed
                  - Schema added
              - Modified property: user_eduperson_assurance
                - Type changed from '' to 'array'
                - Items changed
                  - Schema added
              - Modified property: user_nationalities
                - Type changed from '' to 'array'
                - Items changed
                  - Schema added

HEAD /api/marketplace-offering-users/

- New query param: runtime_state

POST /api/marketplace-offering-users/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: runtime_state
            - Modified property: user_active_isds
              - Type changed from '' to 'array'
              - Items changed
                - Schema added
            - Modified property: user_affiliations
              - Type changed from '' to 'array'
              - Items changed
                - Schema added
            - Modified property: user_eduperson_assurance
              - Type changed from '' to 'array'
              - Items changed
                - Schema added
            - Modified property: user_nationalities
              - Type changed from '' to 'array'
              - Items changed
                - Schema added

GET /api/marketplace-offering-users/checklist-template/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: checklist
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/ChecklistShort
              - Type changed from 'object' to ''
              - AdditionalProperties changed
                - Schema deleted
            - Modified property: initial_visible_questions
              - Items changed
                - Properties changed
                  - New property: likert_allow_na
                  - New property: likert_high_label
                  - New property: likert_low_label
                  - New property: likert_scale_length
                  - New property: rich_text_char_limit
                  - New property: rich_text_toolbar_level
                  - Modified property: allowed_file_types
                    - Type changed from '' to 'array'
                    - Description changed from 'List of allowed file extensions (e.g., ['.pdf', '.doc', '.docx']). If empty, all file types are allowed.' to ''
                    - Items changed
                      - Schema added
                  - Modified property: allowed_mime_types
                    - Type changed from '' to 'array'
                    - Description changed from 'List of allowed MIME types (e.g., ['application/pdf', 'application/msword']). If empty, MIME type validation is not enforced. When both extensions and MIME types are specified, files must match both criteria for security.' to ''
                    - Items changed
                      - Schema added
                  - Modified property: guidance_answer_value
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: question_type
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/QuestionTypeEnum
                        - New enum values: [likert rich_text]
                  - Modified property: review_answer_value
                    - Description changed from 'Answer value that trigger review.' to ''
                    - Nullable changed from true to false
            - Modified property: questions
              - Items changed
                - Properties changed
                  - New property: likert_allow_na
                  - New property: likert_high_label
                  - New property: likert_low_label
                  - New property: likert_scale_length
                  - New property: rich_text_char_limit
                  - New property: rich_text_toolbar_level
                  - Modified property: allowed_file_types
                    - Type changed from '' to 'array'
                    - Description changed from 'List of allowed file extensions (e.g., ['.pdf', '.doc', '.docx']). If empty, all file types are allowed.' to ''
                    - Items changed
                      - Schema added
                  - Modified property: allowed_mime_types
                    - Type changed from '' to 'array'
                    - Description changed from 'List of allowed MIME types (e.g., ['application/pdf', 'application/msword']). If empty, MIME type validation is not enforced. When both extensions and MIME types are specified, files must match both criteria for security.' to ''
                    - Items changed
                      - Schema added
                  - Modified property: guidance_answer_value
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: question_type
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/QuestionTypeEnum
                        - New enum values: [likert rich_text]
                  - Modified property: review_answer_value
                    - Description changed from 'Answer value that trigger review.' to ''
                    - Nullable changed from true to false

GET /api/marketplace-offering-users/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [runtime_state]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: runtime_state
            - Modified property: user_active_isds
              - Type changed from '' to 'array'
              - Items changed
                - Schema added
            - Modified property: user_affiliations
              - Type changed from '' to 'array'
              - Items changed
                - Schema added
            - Modified property: user_eduperson_assurance
              - Type changed from '' to 'array'
              - Items changed
                - Schema added
            - Modified property: user_nationalities
              - Type changed from '' to 'array'
              - Items changed
                - Schema added

PATCH /api/marketplace-offering-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: runtime_state
            - Modified property: user_active_isds
              - Type changed from '' to 'array'
              - Items changed
                - Schema added
            - Modified property: user_affiliations
              - Type changed from '' to 'array'
              - Items changed
                - Schema added
            - Modified property: user_eduperson_assurance
              - Type changed from '' to 'array'
              - Items changed
                - Schema added
            - Modified property: user_nationalities
              - Type changed from '' to 'array'
              - Items changed
                - Schema added

PUT /api/marketplace-offering-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: runtime_state
            - Modified property: user_active_isds
              - Type changed from '' to 'array'
              - Items changed
                - Schema added
            - Modified property: user_affiliations
              - Type changed from '' to 'array'
              - Items changed
                - Schema added
            - Modified property: user_eduperson_assurance
              - Type changed from '' to 'array'
              - Items changed
                - Schema added
            - Modified property: user_nationalities
              - Type changed from '' to 'array'
              - Items changed
                - Schema added

GET /api/marketplace-offering-users/{uuid}/checklist/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: checklist
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/ChecklistShort
              - Type changed from 'object' to ''
              - AdditionalProperties changed
                - Schema deleted
            - Modified property: questions
              - Items changed
                - Required changed
                  - New required property: likert_allow_na
                  - New required property: likert_high_label
                  - New required property: likert_low_label
                  - New required property: likert_scale_length
                  - New required property: rich_text_char_limit
                  - New required property: rich_text_toolbar_level
                - Properties changed
                  - New property: likert_allow_na
                  - New property: likert_high_label
                  - New property: likert_low_label
                  - New property: likert_scale_length
                  - New property: rich_text_char_limit
                  - New property: rich_text_toolbar_level
                  - Modified property: allowed_file_types
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: allowed_mime_types
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: dependencies_info
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/QuestionDependencyInfo
                    - Type changed from 'object' to ''
                    - AdditionalProperties changed
                      - Schema deleted
                  - Modified property: existing_answer
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/Answer
                    - Type changed from 'object' to ''
                    - AdditionalProperties changed
                      - Schema deleted
                  - Modified property: question_type
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/QuestionTypeEnum
                        - New enum values: [likert rich_text]

GET /api/marketplace-offering-users/{uuid}/checklist_review/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: checklist
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/ChecklistShort
              - Type changed from 'object' to ''
              - AdditionalProperties changed
                - Schema deleted
            - Modified property: questions
              - Items changed
                - Required changed
                  - New required property: likert_allow_na
                  - New required property: likert_high_label
                  - New required property: likert_low_label
                  - New required property: likert_scale_length
                  - New required property: rich_text_char_limit
                  - New required property: rich_text_toolbar_level
                - Properties changed
                  - New property: likert_allow_na
                  - New property: likert_high_label
                  - New property: likert_low_label
                  - New property: likert_scale_length
                  - New property: rich_text_char_limit
                  - New property: rich_text_toolbar_level
                  - Modified property: allowed_file_types
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: allowed_mime_types
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: dependencies_info
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/QuestionDependencyInfo
                    - Type changed from 'object' to ''
                    - AdditionalProperties changed
                      - Schema deleted
                  - Modified property: existing_answer
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/Answer
                    - Type changed from 'object' to ''
                    - AdditionalProperties changed
                      - Schema deleted
                  - Modified property: question_type
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/QuestionTypeEnum
                        - New enum values: [likert rich_text]
                  - Modified property: review_answer_value
                    - Description changed from 'Answer value that trigger review.' to ''
                    - Nullable changed from true to false

GET /api/marketplace-orders/

- New query param: was_auto_approved
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [auto_approved auto_approved_by_rule_uuid auto_approved_cost_limit_snapshot]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: auto_approved
              - New property: auto_approved_by_rule_uuid
              - New property: auto_approved_cost_limit_snapshot
              - Modified property: attributes
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: offering_plugin_options
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

HEAD /api/marketplace-orders/

- New query param: was_auto_approved

POST /api/marketplace-orders/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: attributes
            - Property 'OneOf' changed
              - Modified schema: #/components/schemas/OpenStackTenantCreateOrderAttributes
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: direction
                                - Property 'AllOf' changed
                                  - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                                  - Schemas deleted: #/components/schemas/DirectionEnum
                              - Modified property: protocol
                                - Property 'OneOf' changed
                                  - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                                - Type changed from '' to 'string'
                                - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                                - MaxLength changed from null to 40
              - Modified schema: #/components/schemas/OpenStackInstanceCreateOrderAttributes
                - Properties changed
                  - New property: config_drive
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: auto_approved
            - New property: auto_approved_by_rule_uuid
            - New property: auto_approved_cost_limit_snapshot
            - Modified property: attributes
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: offering_plugin_options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/marketplace-orders/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [auto_approved auto_approved_by_rule_uuid auto_approved_cost_limit_snapshot]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: auto_approved
            - New property: auto_approved_by_rule_uuid
            - New property: auto_approved_cost_limit_snapshot
            - Modified property: attributes
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: offering_plugin_options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PATCH /api/marketplace-orders/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: attributes
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: attributes
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PUT /api/marketplace-orders/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: attributes
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: attributes
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

POST /api/marketplace-orders/{uuid}/approve_by_provider/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: attributes
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true

GET /api/marketplace-orders/{uuid}/offering/

- New query param: field
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: config_drive_default
            - New property: offering_group
            - New property: offering_group_title
            - New property: offering_group_uuid
            - Modified property: backend_metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - Modified property: cascade_config
                            - Properties changed
                              - Modified property: steps
                                - Items changed
                                  - Properties changed
                                    - Modified property: choices
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
                                    - Modified property: choices_map
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: auto_ok_resource_projects
                    - New property: expose_inference_playground
                    - New property: initial_rolegroup_number
                    - New property: require_effective_id_for_highlighted_display
                    - New property: resource_project_role_group_template
                    - New property: resource_project_role_map
                    - New property: resource_role_group_template
                    - New property: resource_role_map
                    - New property: resource_slug_max_length
                    - New property: resource_slug_template
                    - Modified property: required_team_role_for_provisioning
                      - Nullable changed from false to true
                    - Modified property: resource_name_pattern
                      - Nullable changed from false to true
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - Modified property: cascade_config
                            - Properties changed
                              - Modified property: steps
                                - Items changed
                                  - Properties changed
                                    - Modified property: choices
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
                                    - Modified property: choices_map
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: enabled_cpu_family
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: enabled_cpu_microarchitectures
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true

GET /api/marketplace-orders/{uuid}/resource/

- New query param: field
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: end_date_updated_at
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: auto_approved
                    - New property: auto_approved_by_rule_uuid
                    - New property: auto_approved_cost_limit_snapshot
                    - Modified property: attributes
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: offering_plugin_options
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
            - Modified property: offering_plugin_options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: auto_approved
                    - New property: auto_approved_by_rule_uuid
                    - New property: auto_approved_cost_limit_snapshot
                    - Modified property: attributes
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: offering_plugin_options
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true

POST /api/marketplace-orders/{uuid}/set_backend_id/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Example changed from map[status:Order backend_id has been changed.] to null
          - Required changed
            - New required property: status
        - Examples changed
          - New example: Success

GET /api/marketplace-project-estimated-cost-policies/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: options
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

POST /api/marketplace-project-estimated-cost-policies/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: options
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/marketplace-project-estimated-cost-policies/actions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Type changed from 'object' to 'array'
          - Items changed
            - Schema added
          - Required changed
            - Deleted required property: actions
            - Deleted required property: affected_resources_count
            - Deleted required property: billing_price_estimate
            - Deleted required property: created
            - Deleted required property: created_by_full_name
            - Deleted required property: created_by_username
            - Deleted required property: customer_credit
            - Deleted required property: fired_datetime
            - Deleted required property: has_fired
            - Deleted required property: limit_cost
            - Deleted required property: period_name
            - Deleted required property: project_credit
            - Deleted required property: scope
            - Deleted required property: scope_name
            - Deleted required property: scope_uuid
            - Deleted required property: url
            - Deleted required property: uuid
          - Properties changed
            - Deleted property: actions
            - Deleted property: affected_resources_count
            - Deleted property: billing_price_estimate
            - Deleted property: created
            - Deleted property: created_by_full_name
            - Deleted property: created_by_username
            - Deleted property: customer_credit
            - Deleted property: fired_datetime
            - Deleted property: has_fired
            - Deleted property: limit_cost
            - Deleted property: options
            - Deleted property: period
            - Deleted property: period_name
            - Deleted property: project_credit
            - Deleted property: scope
            - Deleted property: scope_name
            - Deleted property: scope_uuid
            - Deleted property: url
            - Deleted property: uuid

GET /api/marketplace-project-estimated-cost-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PATCH /api/marketplace-project-estimated-cost-policies/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: options
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PUT /api/marketplace-project-estimated-cost-policies/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: options
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/marketplace-provider-offerings/

- New query param: offering_group_uuid
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_group offering_group_title offering_group_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: offering_group
              - New property: offering_group_title
              - New property: offering_group_uuid
              - Modified property: backend_id_rules
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: backend_metadata
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - Modified property: cascade_config
                              - Properties changed
                                - Modified property: steps
                                  - Items changed
                                    - Properties changed
                                      - Modified property: choices
                                        - Type changed from '' to 'object'
                                        - AdditionalProperties changed from null to true
                                      - Modified property: choices_map
                                        - Type changed from '' to 'object'
                                        - AdditionalProperties changed from null to true
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: auto_ok_resource_projects
                      - New property: expose_inference_playground
                      - New property: initial_rolegroup_number
                      - New property: require_effective_id_for_highlighted_display
                      - New property: resource_project_role_group_template
                      - New property: resource_project_role_map
                      - New property: resource_role_group_template
                      - New property: resource_role_map
                      - New property: resource_slug_max_length
                      - New property: resource_slug_template
                      - Modified property: required_team_role_for_provisioning
                        - Nullable changed from false to true
                      - Modified property: resource_name_pattern
                        - Nullable changed from false to true
              - Modified property: resource_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - Modified property: cascade_config
                              - Properties changed
                                - Modified property: steps
                                  - Items changed
                                    - Properties changed
                                      - Modified property: choices
                                        - Type changed from '' to 'object'
                                        - AdditionalProperties changed from null to true
                                      - Modified property: choices_map
                                        - Type changed from '' to 'object'
                                        - AdditionalProperties changed from null to true
              - Modified property: secret_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedSecretOptions
                    - Properties changed
                      - Modified property: environ
                        - Type changed from '' to 'array'
                        - Items changed
                          - Schema added
              - Modified property: software_catalogs
                - Items changed
                  - Properties changed
                    - Modified property: enabled_cpu_family
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: enabled_cpu_microarchitectures
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true

HEAD /api/marketplace-provider-offerings/

- New query param: offering_group_uuid

POST /api/marketplace-provider-offerings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: offering_group
          - Modified property: attributes
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: backend_id_rules
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: backend_metadata
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: options
            - Properties changed
              - Modified property: options
                - AdditionalProperties changed
                  - Properties changed
                    - Modified property: cascade_config
                      - Properties changed
                        - Modified property: steps
                          - Items changed
                            - Properties changed
                              - Modified property: choices
                                - Type changed from '' to 'object'
                                - AdditionalProperties changed from null to true
                              - Modified property: choices_map
                                - Type changed from '' to 'object'
                                - AdditionalProperties changed from null to true
          - Modified property: plugin_options
            - Properties changed
              - New property: auto_ok_resource_projects
              - New property: expose_inference_playground
              - New property: initial_rolegroup_number
              - New property: require_effective_id_for_highlighted_display
              - New property: resource_project_role_group_template
              - New property: resource_project_role_map
              - New property: resource_role_group_template
              - New property: resource_role_map
              - New property: resource_slug_max_length
              - New property: resource_slug_template
              - Modified property: required_team_role_for_provisioning
                - Nullable changed from false to true
              - Modified property: resource_name_pattern
                - Nullable changed from false to true
                - MinLength changed from 1 to 0
          - Modified property: resource_options
            - Properties changed
              - Modified property: options
                - AdditionalProperties changed
                  - Properties changed
                    - Modified property: cascade_config
                      - Properties changed
                        - Modified property: steps
                          - Items changed
                            - Properties changed
                              - Modified property: choices
                                - Type changed from '' to 'object'
                                - AdditionalProperties changed from null to true
                              - Modified property: choices_map
                                - Type changed from '' to 'object'
                                - AdditionalProperties changed from null to true
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: offering_group
          - Modified property: attributes
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: backend_id_rules
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: backend_metadata
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: options
            - Properties changed
              - Modified property: options
                - AdditionalProperties changed
                  - Properties changed
                    - Modified property: cascade_config
                      - Properties changed
                        - Modified property: steps
                          - Items changed
                            - Properties changed
                              - Modified property: choices
                                - Type changed from '' to 'object'
                                - AdditionalProperties changed from null to true
                              - Modified property: choices_map
                                - Type changed from '' to 'object'
                                - AdditionalProperties changed from null to true
          - Modified property: plugin_options
            - Properties changed
              - New property: auto_ok_resource_projects
              - New property: expose_inference_playground
              - New property: initial_rolegroup_number
              - New property: require_effective_id_for_highlighted_display
              - New property: resource_project_role_group_template
              - New property: resource_project_role_map
              - New property: resource_role_group_template
              - New property: resource_role_map
              - New property: resource_slug_max_length
              - New property: resource_slug_template
              - Modified property: required_team_role_for_provisioning
                - Nullable changed from false to true
              - Modified property: resource_name_pattern
                - Nullable changed from false to true
                - MinLength changed from 1 to 0
          - Modified property: resource_options
            - Properties changed
              - Modified property: options
                - AdditionalProperties changed
                  - Properties changed
                    - Modified property: cascade_config
                      - Properties changed
                        - Modified property: steps
                          - Items changed
                            - Properties changed
                              - Modified property: choices
                                - Type changed from '' to 'object'
                                - AdditionalProperties changed from null to true
                              - Modified property: choices_map
                                - Type changed from '' to 'object'
                                - AdditionalProperties changed from null to true
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: offering_group
          - Modified property: attributes
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: backend_id_rules
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: backend_metadata
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: options
            - Properties changed
              - Modified property: options
                - AdditionalProperties changed
                  - Properties changed
                    - Modified property: cascade_config
                      - Properties changed
                        - Modified property: steps
                          - Items changed
                            - Properties changed
                              - Modified property: choices
                                - Type changed from '' to 'object'
                                - AdditionalProperties changed from null to true
                              - Modified property: choices_map
                                - Type changed from '' to 'object'
                                - AdditionalProperties changed from null to true
          - Modified property: plugin_options
            - Properties changed
              - New property: auto_ok_resource_projects
              - New property: expose_inference_playground
              - New property: initial_rolegroup_number
              - New property: require_effective_id_for_highlighted_display
              - New property: resource_project_role_group_template
              - New property: resource_project_role_map
              - New property: resource_role_group_template
              - New property: resource_role_map
              - New property: resource_slug_max_length
              - New property: resource_slug_template
              - Modified property: required_team_role_for_provisioning
                - Nullable changed from false to true
              - Modified property: resource_name_pattern
                - Nullable changed from false to true
                - MinLength changed from 1 to 0
          - Modified property: resource_options
            - Properties changed
              - Modified property: options
                - AdditionalProperties changed
                  - Properties changed
                    - Modified property: cascade_config
                      - Properties changed
                        - Modified property: steps
                          - Items changed
                            - Properties changed
                              - Modified property: choices
                                - Type changed from '' to 'object'
                                - AdditionalProperties changed from null to true
                              - Modified property: choices_map
                                - Type changed from '' to 'object'
                                - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_group
            - New property: offering_group_title
            - New property: offering_group_uuid
            - Modified property: backend_id_rules
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: backend_metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - Modified property: cascade_config
                            - Properties changed
                              - Modified property: steps
                                - Items changed
                                  - Properties changed
                                    - Modified property: choices
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
                                    - Modified property: choices_map
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: auto_ok_resource_projects
                    - New property: expose_inference_playground
                    - New property: initial_rolegroup_number
                    - New property: require_effective_id_for_highlighted_display
                    - New property: resource_project_role_group_template
                    - New property: resource_project_role_map
                    - New property: resource_role_group_template
                    - New property: resource_role_map
                    - New property: resource_slug_max_length
                    - New property: resource_slug_template
                    - Modified property: required_team_role_for_provisioning
                      - Nullable changed from false to true
                    - Modified property: resource_name_pattern
                      - Nullable changed from false to true
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - Modified property: cascade_config
                            - Properties changed
                              - Modified property: steps
                                - Items changed
                                  - Properties changed
                                    - Modified property: choices
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
                                    - Modified property: choices_map
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - Modified property: environ
                      - Type changed from '' to 'array'
                      - Items changed
                        - Schema added
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: enabled_cpu_family
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: enabled_cpu_microarchitectures
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true

GET /api/marketplace-provider-offerings/groups/

- New query param: offering_group_uuid

HEAD /api/marketplace-provider-offerings/groups/

- New query param: offering_group_uuid

POST /api/marketplace-provider-offerings/import_offering/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: offering_data
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/OfferingExportDataRequest
                - Properties changed
                  - Modified property: offering
                    - Properties changed
                      - Modified property: attributes
                        - Type changed from '' to 'object'
                        - AdditionalProperties changed from null to true
                      - Modified property: options
                        - Type changed from '' to 'object'
                        - AdditionalProperties changed from null to true
                  - Modified property: plugin_options
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: resource_options
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: secret_options
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true

GET /api/marketplace-provider-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_group offering_group_title offering_group_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_group
            - New property: offering_group_title
            - New property: offering_group_uuid
            - Modified property: backend_id_rules
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: backend_metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - Modified property: cascade_config
                            - Properties changed
                              - Modified property: steps
                                - Items changed
                                  - Properties changed
                                    - Modified property: choices
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
                                    - Modified property: choices_map
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: auto_ok_resource_projects
                    - New property: expose_inference_playground
                    - New property: initial_rolegroup_number
                    - New property: require_effective_id_for_highlighted_display
                    - New property: resource_project_role_group_template
                    - New property: resource_project_role_map
                    - New property: resource_role_group_template
                    - New property: resource_role_map
                    - New property: resource_slug_max_length
                    - New property: resource_slug_template
                    - Modified property: required_team_role_for_provisioning
                      - Nullable changed from false to true
                    - Modified property: resource_name_pattern
                      - Nullable changed from false to true
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - Modified property: cascade_config
                            - Properties changed
                              - Modified property: steps
                                - Items changed
                                  - Properties changed
                                    - Modified property: choices
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
                                    - Modified property: choices_map
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - Modified property: environ
                      - Type changed from '' to 'array'
                      - Items changed
                        - Schema added
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: enabled_cpu_family
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: enabled_cpu_microarchitectures
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true

POST /api/marketplace-provider-offerings/{uuid}/add_software_catalog/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: enabled_cpu_family
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: enabled_cpu_microarchitectures
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true

GET /api/marketplace-provider-offerings/{uuid}/component_stats/

- New query param: offering_group_uuid

GET /api/marketplace-provider-offerings/{uuid}/costs/

- New query param: offering_group_uuid

GET /api/marketplace-provider-offerings/{uuid}/customers/

- New query param: offering_group_uuid

POST /api/marketplace-provider-offerings/{uuid}/export_offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: export_data
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingExportData
                  - Properties changed
                    - Modified property: offering
                      - Properties changed
                        - Modified property: attributes
                          - Type changed from '' to 'object'
                          - AdditionalProperties changed from null to true
                        - Modified property: options
                          - Type changed from '' to 'object'
                          - AdditionalProperties changed from null to true
                    - Modified property: plugin_options
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: resource_options
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: secret_options
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true

GET /api/marketplace-provider-offerings/{uuid}/history/

- New query param: offering_group_uuid

POST /api/marketplace-provider-offerings/{uuid}/import_resource/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: additional_details
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: end_date_updated_at
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: auto_approved
                    - New property: auto_approved_by_rule_uuid
                    - New property: auto_approved_cost_limit_snapshot
                    - Modified property: attributes
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: offering_plugin_options
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
            - Modified property: offering_plugin_options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: auto_approved
                    - New property: auto_approved_by_rule_uuid
                    - New property: auto_approved_cost_limit_snapshot
                    - Modified property: attributes
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: offering_plugin_options
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true

GET /api/marketplace-provider-offerings/{uuid}/list_course_accounts/

- New query param: offering_group_uuid

GET /api/marketplace-provider-offerings/{uuid}/list_customer_projects/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [affiliation affiliation_code affiliation_name affiliation_uuid project_metadata]
      - Deleted enum values: [affiliated_organizations]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: affiliation
              - New property: affiliation_code
              - New property: affiliation_name
              - New property: affiliation_uuid
              - New property: project_metadata
              - Deleted property: affiliated_organizations
              - Modified property: kind
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/ProjectKindEnum
                  - Schemas deleted: #/components/schemas/KindEnum
              - Modified property: termination_metadata
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: user_affiliations
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: user_email_patterns
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: user_identity_sources
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

GET /api/marketplace-provider-offerings/{uuid}/list_customer_service_accounts/

- New query param: offering_group_uuid

GET /api/marketplace-provider-offerings/{uuid}/list_customer_users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [can_use_personal_access_tokens is_admin_deactivated should_protect_user_details]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: can_use_personal_access_tokens
              - New property: is_admin_deactivated
              - New property: should_protect_user_details
              - Modified property: active_isds
                - Type changed from '' to 'array'
                - Description changed from 'List of ISDs that have asserted this user exists. User is deactivated when this becomes empty.' to ''
                - ReadOnly changed from true to false
                - Items changed
                  - Schema added
              - Modified property: affiliations
                - Type changed from '' to 'array'
                - Description changed from 'Person's affiliation within organization such as student, faculty, staff.' to ''
                - ReadOnly changed from true to false
                - Items changed
                  - Schema added
              - Modified property: attribute_sources
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: eduperson_assurance
                - Type changed from '' to 'array'
                - Description changed from 'REFEDS assurance profile URIs from identity provider' to ''
                - Items changed
                  - Schema added
              - Modified property: managed_isds
                - Type changed from '' to 'array'
                - Description changed from 'List of ISD source identifiers this user can manage via Identity Bridge. E.g., ['isd:puhuri', 'isd:fenix']. Non-empty list implies identity manager role.' to ''
                - Items changed
                  - Schema added
              - Modified property: nationalities
                - Type changed from '' to 'array'
                - Description changed from 'List of all citizenships (ISO 3166-1 alpha-2 codes)' to ''
                - Items changed
                  - Schema added
              - Modified property: permissions
                - Items changed
                  - Properties changed
                    - New property: project_uuid

GET /api/marketplace-provider-offerings/{uuid}/list_project_service_accounts/

- New query param: offering_group_uuid

POST /api/marketplace-provider-offerings/{uuid}/move_offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: config_drive_default
            - New property: offering_group
            - New property: offering_group_title
            - New property: offering_group_uuid
            - Modified property: backend_metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - Modified property: cascade_config
                            - Properties changed
                              - Modified property: steps
                                - Items changed
                                  - Properties changed
                                    - Modified property: choices
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
                                    - Modified property: choices_map
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: auto_ok_resource_projects
                    - New property: expose_inference_playground
                    - New property: initial_rolegroup_number
                    - New property: require_effective_id_for_highlighted_display
                    - New property: resource_project_role_group_template
                    - New property: resource_project_role_map
                    - New property: resource_role_group_template
                    - New property: resource_role_map
                    - New property: resource_slug_max_length
                    - New property: resource_slug_template
                    - Modified property: required_team_role_for_provisioning
                      - Nullable changed from false to true
                    - Modified property: resource_name_pattern
                      - Nullable changed from false to true
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - Modified property: cascade_config
                            - Properties changed
                              - Modified property: steps
                                - Items changed
                                  - Properties changed
                                    - Modified property: choices
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
                                    - Modified property: choices_map
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: enabled_cpu_family
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: enabled_cpu_microarchitectures
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true

GET /api/marketplace-provider-offerings/{uuid}/orders/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [auto_approved auto_approved_by_rule_uuid auto_approved_cost_limit_snapshot]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: auto_approved
              - New property: auto_approved_by_rule_uuid
              - New property: auto_approved_cost_limit_snapshot
              - Modified property: attributes
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: offering_plugin_options
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

GET /api/marketplace-provider-offerings/{uuid}/orders/{order_uuid}/

- New query param: field
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: auto_approved
            - New property: auto_approved_by_rule_uuid
            - New property: auto_approved_cost_limit_snapshot
            - Modified property: attributes
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: offering_plugin_options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

POST /api/marketplace-provider-offerings/{uuid}/refresh_offering_usernames/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: status
              - Description changed from 'Status of the resource response' to ''
              - ReadOnly changed from true to false

POST /api/marketplace-provider-offerings/{uuid}/set_backend_metadata/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: backend_metadata
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true

POST /api/marketplace-provider-offerings/{uuid}/update_backend_id_rules/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: backend_id_rules
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true

POST /api/marketplace-provider-offerings/{uuid}/update_integration/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: auto_ok_resource_projects
              - New property: expose_inference_playground
              - New property: initial_rolegroup_number
              - New property: require_effective_id_for_highlighted_display
              - New property: resource_project_role_group_template
              - New property: resource_project_role_map
              - New property: resource_role_group_template
              - New property: resource_role_map
              - New property: resource_slug_max_length
              - New property: resource_slug_template
              - Modified property: required_team_role_for_provisioning
                - Nullable changed from false to true
              - Modified property: resource_name_pattern
                - Nullable changed from false to true
                - MinLength changed from 1 to 0
          - Modified property: secret_options
            - Properties changed
              - Modified property: environ
                - Type changed from '' to 'array'
                - Items changed
                  - Schema added
          - Modified property: service_attributes
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true

POST /api/marketplace-provider-offerings/{uuid}/update_options/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: options
            - Properties changed
              - Modified property: options
                - AdditionalProperties changed
                  - Properties changed
                    - Modified property: cascade_config
                      - Properties changed
                        - Modified property: steps
                          - Items changed
                            - Properties changed
                              - Modified property: choices
                                - Type changed from '' to 'object'
                                - AdditionalProperties changed from null to true
                              - Modified property: choices_map
                                - Type changed from '' to 'object'
                                - AdditionalProperties changed from null to true

POST /api/marketplace-provider-offerings/{uuid}/update_overview/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: backend_id

POST /api/marketplace-provider-offerings/{uuid}/update_resource_options/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: resource_options
            - Properties changed
              - Modified property: options
                - AdditionalProperties changed
                  - Properties changed
                    - Modified property: cascade_config
                      - Properties changed
                        - Modified property: steps
                          - Items changed
                            - Properties changed
                              - Modified property: choices
                                - Type changed from '' to 'object'
                                - AdditionalProperties changed from null to true
                              - Modified property: choices_map
                                - Type changed from '' to 'object'
                                - AdditionalProperties changed from null to true

PATCH /api/marketplace-provider-offerings/{uuid}/update_software_catalog/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: enabled_cpu_family
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: enabled_cpu_microarchitectures
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: enabled_cpu_family
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: enabled_cpu_microarchitectures
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/marketplace-provider-offerings/{uuid}/user_has_resource_access/

- Deleted query param: field
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: has_access
          - Properties changed
            - New property: has_access
            - Deleted property: access_url
            - Deleted property: attributes
            - Deleted property: backend_id
            - Deleted property: backend_id_rules
            - Deleted property: backend_metadata
            - Deleted property: billable
            - Deleted property: billing_type_classification
            - Deleted property: category
            - Deleted property: category_title
            - Deleted property: category_uuid
            - Deleted property: citation_count
            - Deleted property: compliance_checklist
            - Deleted property: components
            - Deleted property: country
            - Deleted property: created
            - Deleted property: customer
            - Deleted property: customer_name
            - Deleted property: customer_uuid
            - Deleted property: datacite_doi
            - Deleted property: description
            - Deleted property: documentation_url
            - Deleted property: effective_available_limits
            - Deleted property: endpoints
            - Deleted property: files
            - Deleted property: full_description
            - Deleted property: getting_started
            - Deleted property: google_calendar_is_public
            - Deleted property: google_calendar_link
            - Deleted property: has_compliance_requirements
            - Deleted property: helpdesk_url
            - Deleted property: image
            - Deleted property: integration_guide
            - Deleted property: integration_status
            - Deleted property: latitude
            - Deleted property: longitude
            - Deleted property: name
            - Deleted property: options
            - Deleted property: order_count
            - Deleted property: organization_groups
            - Deleted property: parent_description
            - Deleted property: parent_name
            - Deleted property: parent_uuid
            - Deleted property: partitions
            - Deleted property: paused_reason
            - Deleted property: plans
            - Deleted property: plugin_options
            - Deleted property: privacy_policy_link
            - Deleted property: profile_name
            - Deleted property: profile_uuid
            - Deleted property: project
            - Deleted property: project_name
            - Deleted property: project_uuid
            - Deleted property: quotas
            - Deleted property: resource_options
            - Deleted property: scope
            - Deleted property: scope_error_message
            - Deleted property: scope_name
            - Deleted property: scope_state
            - Deleted property: scope_uuid
            - Deleted property: screenshots
            - Deleted property: secret_options
            - Deleted property: service_attributes
            - Deleted property: shared
            - Deleted property: slug
            - Deleted property: software_catalogs
            - Deleted property: state
            - Deleted property: tags
            - Deleted property: thumbnail
            - Deleted property: total_cost
            - Deleted property: total_cost_estimated
            - Deleted property: total_customers
            - Deleted property: type
            - Deleted property: url
            - Deleted property: uuid
            - Deleted property: vendor_details

GET /api/marketplace-provider-resource-projects/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: is_removed
              - New required property: removed_by
              - New required property: removed_by_username
              - New required property: removed_date
              - New required property: termination_metadata
            - Properties changed
              - New property: is_removed
              - New property: removed_by
              - New property: removed_by_username
              - New property: removed_date
              - New property: termination_metadata
              - Modified property: current_usages
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: limits
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

GET /api/marketplace-provider-resource-projects/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: is_removed
            - New required property: removed_by
            - New required property: removed_by_username
            - New required property: removed_date
            - New required property: termination_metadata
          - Properties changed
            - New property: is_removed
            - New property: removed_by
            - New property: removed_by_username
            - New property: removed_date
            - New property: termination_metadata
            - Modified property: current_usages
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: limits
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PATCH /api/marketplace-provider-resource-projects/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: limits
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: is_removed
            - New required property: removed_by
            - New required property: removed_by_username
            - New required property: removed_date
            - New required property: termination_metadata
          - Properties changed
            - New property: is_removed
            - New property: removed_by
            - New property: removed_by_username
            - New property: removed_date
            - New property: termination_metadata
            - Modified property: current_usages
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: limits
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PUT /api/marketplace-provider-resource-projects/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: limits
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: is_removed
            - New required property: removed_by
            - New required property: removed_by_username
            - New required property: removed_date
            - New required property: termination_metadata
          - Properties changed
            - New property: is_removed
            - New property: removed_by
            - New property: removed_by_username
            - New property: removed_date
            - New property: termination_metadata
            - Modified property: current_usages
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: limits
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

POST /api/marketplace-provider-resource-projects/{uuid}/set_backend_id/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: status
            - Deleted required property: backend_id
          - Properties changed
            - New property: status
            - Deleted property: backend_id

POST /api/marketplace-provider-resource-projects/{uuid}/set_state_erred/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: status
          - Properties changed
            - New property: status
            - Deleted property: error_message

POST /api/marketplace-provider-resource-projects/{uuid}/set_state_ok/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: status
          - Properties changed
            - New property: status
          - AdditionalProperties changed
            - Schema deleted

GET /api/marketplace-provider-resources/

- New query param: flavor_name
- New query param: image_name
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [end_date_updated_at]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: end_date_updated_at
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: auto_approved
                      - New property: auto_approved_by_rule_uuid
                      - New property: auto_approved_cost_limit_snapshot
                      - Modified property: attributes
                        - Type changed from '' to 'object'
                        - AdditionalProperties changed from null to true
                      - Modified property: offering_plugin_options
                        - Type changed from '' to 'object'
                        - AdditionalProperties changed from null to true
              - Modified property: offering_plugin_options
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: options
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: auto_approved
                      - New property: auto_approved_by_rule_uuid
                      - New property: auto_approved_cost_limit_snapshot
                      - Modified property: attributes
                        - Type changed from '' to 'object'
                        - AdditionalProperties changed from null to true
                      - Modified property: offering_plugin_options
                        - Type changed from '' to 'object'
                        - AdditionalProperties changed from null to true

HEAD /api/marketplace-provider-resources/

- New query param: flavor_name
- New query param: image_name

GET /api/marketplace-provider-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [end_date_updated_at]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: end_date_updated_at
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: auto_approved
                    - New property: auto_approved_by_rule_uuid
                    - New property: auto_approved_cost_limit_snapshot
                    - Modified property: attributes
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: offering_plugin_options
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
            - Modified property: offering_plugin_options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: auto_approved
                    - New property: auto_approved_by_rule_uuid
                    - New property: auto_approved_cost_limit_snapshot
                    - Modified property: attributes
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: offering_plugin_options
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true

GET /api/marketplace-provider-resources/{uuid}/history/

- New query param: flavor_name
- New query param: image_name

POST /api/marketplace-provider-resources/{uuid}/move_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: end_date_updated_at
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: auto_approved
                    - New property: auto_approved_by_rule_uuid
                    - New property: auto_approved_cost_limit_snapshot
                    - Modified property: attributes
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: offering_plugin_options
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
            - Modified property: offering_plugin_options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: auto_approved
                    - New property: auto_approved_by_rule_uuid
                    - New property: auto_approved_cost_limit_snapshot
                    - Modified property: attributes
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: offering_plugin_options
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true

GET /api/marketplace-provider-resources/{uuid}/offering/

- New query param: field
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: config_drive_default
            - New property: offering_group
            - New property: offering_group_title
            - New property: offering_group_uuid
            - Modified property: backend_metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - Modified property: cascade_config
                            - Properties changed
                              - Modified property: steps
                                - Items changed
                                  - Properties changed
                                    - Modified property: choices
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
                                    - Modified property: choices_map
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: auto_ok_resource_projects
                    - New property: expose_inference_playground
                    - New property: initial_rolegroup_number
                    - New property: require_effective_id_for_highlighted_display
                    - New property: resource_project_role_group_template
                    - New property: resource_project_role_map
                    - New property: resource_role_group_template
                    - New property: resource_role_map
                    - New property: resource_slug_max_length
                    - New property: resource_slug_template
                    - Modified property: required_team_role_for_provisioning
                      - Nullable changed from false to true
                    - Modified property: resource_name_pattern
                      - Nullable changed from false to true
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - Modified property: cascade_config
                            - Properties changed
                              - Modified property: steps
                                - Items changed
                                  - Properties changed
                                    - Modified property: choices
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
                                    - Modified property: choices_map
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: enabled_cpu_family
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: enabled_cpu_microarchitectures
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true

POST /api/marketplace-provider-resources/{uuid}/restore/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: order_uuid
          - Properties changed
            - New property: order_uuid
            - Deleted property: attributes
            - Deleted property: available_actions
            - Deleted property: backend_id
            - Deleted property: backend_metadata
            - Deleted property: can_terminate
            - Deleted property: category_icon
            - Deleted property: category_title
            - Deleted property: category_uuid
            - Deleted property: created
            - Deleted property: creation_order
            - Deleted property: current_usages
            - Deleted property: customer_name
            - Deleted property: customer_slug
            - Deleted property: customer_uuid
            - Deleted property: description
            - Deleted property: downscaled
            - Deleted property: effective_id
            - Deleted property: end_date
            - Deleted property: end_date_requested_by
            - Deleted property: endpoints
            - Deleted property: error_message
            - Deleted property: error_traceback
            - Deleted property: is_limit_based
            - Deleted property: is_usage_based
            - Deleted property: last_sync
            - Deleted property: limit_usage
            - Deleted property: limits
            - Deleted property: modified
            - Deleted property: name
            - Deleted property: offering
            - Deleted property: offering_backend_id
            - Deleted property: offering_billable
            - Deleted property: offering_components
            - Deleted property: offering_description
            - Deleted property: offering_image
            - Deleted property: offering_name
            - Deleted property: offering_plugin_options
            - Deleted property: offering_shared
            - Deleted property: offering_slug
            - Deleted property: offering_state
            - Deleted property: offering_thumbnail
            - Deleted property: offering_type
            - Deleted property: offering_uuid
            - Deleted property: options
            - Deleted property: order_in_progress
            - Deleted property: parent_name
            - Deleted property: parent_offering_name
            - Deleted property: parent_offering_slug
            - Deleted property: parent_offering_uuid
            - Deleted property: parent_uuid
            - Deleted property: paused
            - Deleted property: plan
            - Deleted property: plan_description
            - Deleted property: plan_name
            - Deleted property: plan_unit
            - Deleted property: plan_uuid
            - Deleted property: project
            - Deleted property: project_description
            - Deleted property: project_effective_end_date
            - Deleted property: project_end_date
            - Deleted property: project_end_date_requested_by
            - Deleted property: project_is_in_grace_period
            - Deleted property: project_name
            - Deleted property: project_slug
            - Deleted property: project_uuid
            - Deleted property: provider_description
            - Deleted property: provider_name
            - Deleted property: provider_slug
            - Deleted property: provider_uuid
            - Deleted property: renewal_date
            - Deleted property: report
            - Deleted property: resource_type
            - Deleted property: resource_uuid
            - Deleted property: restrict_member_access
            - Deleted property: scope
            - Deleted property: service_settings_uuid
            - Deleted property: slug
            - Deleted property: state
            - Deleted property: url
            - Deleted property: user_requires_reconsent
            - Deleted property: username
            - Deleted property: uuid

POST /api/marketplace-provider-resources/{uuid}/set_backend_id/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: status
              - Description changed from 'Status of the resource response' to ''
              - ReadOnly changed from true to false

POST /api/marketplace-provider-resources/{uuid}/set_backend_metadata/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: backend_metadata
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: status
              - Description changed from 'Status of the resource response' to ''
              - ReadOnly changed from true to false

POST /api/marketplace-provider-resources/{uuid}/set_downscaled/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: status

POST /api/marketplace-provider-resources/{uuid}/set_effective_id/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: status
              - Description changed from 'Status of the resource response' to ''
              - ReadOnly changed from true to false

POST /api/marketplace-provider-resources/{uuid}/set_limits/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: limits
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: status
              - Description changed from 'Status of the resource response' to ''
              - ReadOnly changed from true to false

POST /api/marketplace-provider-resources/{uuid}/set_paused/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: status

POST /api/marketplace-provider-resources/{uuid}/set_restrict_member_access/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: status

POST /api/marketplace-provider-resources/{uuid}/set_slug/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: status

POST /api/marketplace-provider-resources/{uuid}/set_state_ok/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: status
              - Description changed from 'Status of the resource response' to ''
              - ReadOnly changed from true to false

POST /api/marketplace-provider-resources/{uuid}/submit_report/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: status
              - Description changed from 'Status of the resource response' to ''
              - ReadOnly changed from true to false

GET /api/marketplace-provider-resources/{uuid}/team/

- Description changed from 'Returns a list of users connected to the project of this resource, including their project roles and offering-specific usernames.' to 'Returns project users for this resource from the service provider perspective. When ENFORCE_USER_CONSENT_FOR_OFFERINGS is enabled and the offering has active Terms of Service, only users with active consent are returned (staff and support still see the full team).'
- Modified query param: has_consent
  - Description changed from 'When true, return only users who have active consent for this offering.' to 'When ENFORCE_USER_CONSENT_FOR_OFFERINGS is disabled, passing true returns only users who have active consent for this offering.'

POST /api/marketplace-provider-resources/{uuid}/terminate/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: attributes
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true

POST /api/marketplace-provider-resources/{uuid}/update_options/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: options
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: status
              - Description changed from 'Status of the resource response' to ''
              - ReadOnly changed from true to false

POST /api/marketplace-provider-resources/{uuid}/update_options_direct/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: options
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: status
              - Description changed from 'Status of the resource response' to ''
              - ReadOnly changed from true to false

GET /api/marketplace-public-offerings/

- New query param: offering_group_uuid
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [config_drive_default offering_group offering_group_title offering_group_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: config_drive_default
              - New property: offering_group
              - New property: offering_group_title
              - New property: offering_group_uuid
              - Modified property: backend_metadata
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - Modified property: cascade_config
                              - Properties changed
                                - Modified property: steps
                                  - Items changed
                                    - Properties changed
                                      - Modified property: choices
                                        - Type changed from '' to 'object'
                                        - AdditionalProperties changed from null to true
                                      - Modified property: choices_map
                                        - Type changed from '' to 'object'
                                        - AdditionalProperties changed from null to true
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: auto_ok_resource_projects
                      - New property: expose_inference_playground
                      - New property: initial_rolegroup_number
                      - New property: require_effective_id_for_highlighted_display
                      - New property: resource_project_role_group_template
                      - New property: resource_project_role_map
                      - New property: resource_role_group_template
                      - New property: resource_role_map
                      - New property: resource_slug_max_length
                      - New property: resource_slug_template
                      - Modified property: required_team_role_for_provisioning
                        - Nullable changed from false to true
                      - Modified property: resource_name_pattern
                        - Nullable changed from false to true
              - Modified property: resource_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - Modified property: cascade_config
                              - Properties changed
                                - Modified property: steps
                                  - Items changed
                                    - Properties changed
                                      - Modified property: choices
                                        - Type changed from '' to 'object'
                                        - AdditionalProperties changed from null to true
                                      - Modified property: choices_map
                                        - Type changed from '' to 'object'
                                        - AdditionalProperties changed from null to true
              - Modified property: software_catalogs
                - Items changed
                  - Properties changed
                    - Modified property: enabled_cpu_family
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: enabled_cpu_microarchitectures
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true

HEAD /api/marketplace-public-offerings/

- New query param: offering_group_uuid

GET /api/marketplace-public-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [config_drive_default offering_group offering_group_title offering_group_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: config_drive_default
            - New property: offering_group
            - New property: offering_group_title
            - New property: offering_group_uuid
            - Modified property: backend_metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - Modified property: cascade_config
                            - Properties changed
                              - Modified property: steps
                                - Items changed
                                  - Properties changed
                                    - Modified property: choices
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
                                    - Modified property: choices_map
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: auto_ok_resource_projects
                    - New property: expose_inference_playground
                    - New property: initial_rolegroup_number
                    - New property: require_effective_id_for_highlighted_display
                    - New property: resource_project_role_group_template
                    - New property: resource_project_role_map
                    - New property: resource_role_group_template
                    - New property: resource_role_map
                    - New property: resource_slug_max_length
                    - New property: resource_slug_template
                    - Modified property: required_team_role_for_provisioning
                      - Nullable changed from false to true
                    - Modified property: resource_name_pattern
                      - Nullable changed from false to true
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - Modified property: cascade_config
                            - Properties changed
                              - Modified property: steps
                                - Items changed
                                  - Properties changed
                                    - Modified property: choices
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
                                    - Modified property: choices_map
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: enabled_cpu_family
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: enabled_cpu_microarchitectures
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true

GET /api/marketplace-resource-projects/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: is_removed
              - New required property: removed_by
              - New required property: removed_by_username
              - New required property: removed_date
              - New required property: termination_metadata
            - Properties changed
              - New property: is_removed
              - New property: removed_by
              - New property: removed_by_username
              - New property: removed_date
              - New property: termination_metadata
              - Modified property: current_usages
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: limits
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

POST /api/marketplace-resource-projects/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: limits
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: is_removed
            - New required property: removed_by
            - New required property: removed_by_username
            - New required property: removed_date
            - New required property: termination_metadata
          - Properties changed
            - New property: is_removed
            - New property: removed_by
            - New property: removed_by_username
            - New property: removed_date
            - New property: termination_metadata
            - Modified property: current_usages
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: limits
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

DELETE /api/marketplace-resource-projects/{uuid}/

- New query param: force

GET /api/marketplace-resource-projects/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: is_removed
            - New required property: removed_by
            - New required property: removed_by_username
            - New required property: removed_date
            - New required property: termination_metadata
          - Properties changed
            - New property: is_removed
            - New property: removed_by
            - New property: removed_by_username
            - New property: removed_date
            - New property: termination_metadata
            - Modified property: current_usages
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: limits
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PATCH /api/marketplace-resource-projects/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: limits
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: is_removed
            - New required property: removed_by
            - New required property: removed_by_username
            - New required property: removed_date
            - New required property: termination_metadata
          - Properties changed
            - New property: is_removed
            - New property: removed_by
            - New property: removed_by_username
            - New property: removed_date
            - New property: termination_metadata
            - Modified property: current_usages
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: limits
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PUT /api/marketplace-resource-projects/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: limits
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: is_removed
            - New required property: removed_by
            - New required property: removed_by_username
            - New required property: removed_date
            - New required property: termination_metadata
          - Properties changed
            - New property: is_removed
            - New property: removed_by
            - New property: removed_by_username
            - New property: removed_date
            - New property: termination_metadata
            - Modified property: current_usages
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: limits
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/marketplace-resources/

- New query param: flavor_name
- New query param: image_name
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [end_date_updated_at]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: end_date_updated_at
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: auto_approved
                      - New property: auto_approved_by_rule_uuid
                      - New property: auto_approved_cost_limit_snapshot
                      - Modified property: attributes
                        - Type changed from '' to 'object'
                        - AdditionalProperties changed from null to true
                      - Modified property: offering_plugin_options
                        - Type changed from '' to 'object'
                        - AdditionalProperties changed from null to true
              - Modified property: offering_plugin_options
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: options
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: auto_approved
                      - New property: auto_approved_by_rule_uuid
                      - New property: auto_approved_cost_limit_snapshot
                      - Modified property: attributes
                        - Type changed from '' to 'object'
                        - AdditionalProperties changed from null to true
                      - Modified property: offering_plugin_options
                        - Type changed from '' to 'object'
                        - AdditionalProperties changed from null to true

HEAD /api/marketplace-resources/

- New query param: flavor_name
- New query param: image_name

POST /api/marketplace-resources/suggest_name/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: attributes
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true

GET /api/marketplace-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [end_date_updated_at]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: end_date_updated_at
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: auto_approved
                    - New property: auto_approved_by_rule_uuid
                    - New property: auto_approved_cost_limit_snapshot
                    - Modified property: attributes
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: offering_plugin_options
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
            - Modified property: offering_plugin_options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: auto_approved
                    - New property: auto_approved_by_rule_uuid
                    - New property: auto_approved_cost_limit_snapshot
                    - Modified property: attributes
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: offering_plugin_options
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true

GET /api/marketplace-resources/{uuid}/history/

- New query param: flavor_name
- New query param: image_name

POST /api/marketplace-resources/{uuid}/move_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: end_date_updated_at
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: auto_approved
                    - New property: auto_approved_by_rule_uuid
                    - New property: auto_approved_cost_limit_snapshot
                    - Modified property: attributes
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: offering_plugin_options
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
            - Modified property: offering_plugin_options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: auto_approved
                    - New property: auto_approved_by_rule_uuid
                    - New property: auto_approved_cost_limit_snapshot
                    - Modified property: attributes
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: offering_plugin_options
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true

GET /api/marketplace-resources/{uuid}/offering/

- New query param: field
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: config_drive_default
            - New property: offering_group
            - New property: offering_group_title
            - New property: offering_group_uuid
            - Modified property: backend_metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - Modified property: cascade_config
                            - Properties changed
                              - Modified property: steps
                                - Items changed
                                  - Properties changed
                                    - Modified property: choices
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
                                    - Modified property: choices_map
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: auto_ok_resource_projects
                    - New property: expose_inference_playground
                    - New property: initial_rolegroup_number
                    - New property: require_effective_id_for_highlighted_display
                    - New property: resource_project_role_group_template
                    - New property: resource_project_role_map
                    - New property: resource_role_group_template
                    - New property: resource_role_map
                    - New property: resource_slug_max_length
                    - New property: resource_slug_template
                    - Modified property: required_team_role_for_provisioning
                      - Nullable changed from false to true
                    - Modified property: resource_name_pattern
                      - Nullable changed from false to true
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - Modified property: cascade_config
                            - Properties changed
                              - Modified property: steps
                                - Items changed
                                  - Properties changed
                                    - Modified property: choices
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
                                    - Modified property: choices_map
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: enabled_cpu_family
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: enabled_cpu_microarchitectures
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true

POST /api/marketplace-resources/{uuid}/restore/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: order_uuid
          - Properties changed
            - New property: order_uuid
            - Deleted property: attributes
            - Deleted property: available_actions
            - Deleted property: backend_id
            - Deleted property: backend_metadata
            - Deleted property: can_terminate
            - Deleted property: category_icon
            - Deleted property: category_title
            - Deleted property: category_uuid
            - Deleted property: created
            - Deleted property: creation_order
            - Deleted property: current_usages
            - Deleted property: customer_name
            - Deleted property: customer_slug
            - Deleted property: customer_uuid
            - Deleted property: description
            - Deleted property: downscaled
            - Deleted property: effective_id
            - Deleted property: end_date
            - Deleted property: end_date_requested_by
            - Deleted property: endpoints
            - Deleted property: error_message
            - Deleted property: error_traceback
            - Deleted property: is_limit_based
            - Deleted property: is_usage_based
            - Deleted property: last_sync
            - Deleted property: limit_usage
            - Deleted property: limits
            - Deleted property: modified
            - Deleted property: name
            - Deleted property: offering
            - Deleted property: offering_backend_id
            - Deleted property: offering_billable
            - Deleted property: offering_components
            - Deleted property: offering_description
            - Deleted property: offering_image
            - Deleted property: offering_name
            - Deleted property: offering_plugin_options
            - Deleted property: offering_shared
            - Deleted property: offering_slug
            - Deleted property: offering_state
            - Deleted property: offering_thumbnail
            - Deleted property: offering_type
            - Deleted property: offering_uuid
            - Deleted property: options
            - Deleted property: order_in_progress
            - Deleted property: parent_name
            - Deleted property: parent_offering_name
            - Deleted property: parent_offering_slug
            - Deleted property: parent_offering_uuid
            - Deleted property: parent_uuid
            - Deleted property: paused
            - Deleted property: plan
            - Deleted property: plan_description
            - Deleted property: plan_name
            - Deleted property: plan_unit
            - Deleted property: plan_uuid
            - Deleted property: project
            - Deleted property: project_description
            - Deleted property: project_effective_end_date
            - Deleted property: project_end_date
            - Deleted property: project_end_date_requested_by
            - Deleted property: project_is_in_grace_period
            - Deleted property: project_name
            - Deleted property: project_slug
            - Deleted property: project_uuid
            - Deleted property: provider_description
            - Deleted property: provider_name
            - Deleted property: provider_slug
            - Deleted property: provider_uuid
            - Deleted property: renewal_date
            - Deleted property: report
            - Deleted property: resource_type
            - Deleted property: resource_uuid
            - Deleted property: restrict_member_access
            - Deleted property: scope
            - Deleted property: service_settings_uuid
            - Deleted property: slug
            - Deleted property: state
            - Deleted property: url
            - Deleted property: user_requires_reconsent
            - Deleted property: username
            - Deleted property: uuid

POST /api/marketplace-resources/{uuid}/set_downscaled/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: status

POST /api/marketplace-resources/{uuid}/set_paused/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: status

POST /api/marketplace-resources/{uuid}/set_restrict_member_access/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: status

POST /api/marketplace-resources/{uuid}/set_slug/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: status

GET /api/marketplace-resources/{uuid}/team/

- Description changed from 'Returns a list of users connected to the project of this resource, including their project roles and offering-specific usernames.' to 'Returns project users for this resource, including project roles and offering-specific usernames. Use has_consent=true to list only users with active Terms of Service consent for the offering.'

GET /api/marketplace-resources/{uuid}/team_members/

- New query param: field
- New query param: flavor_name
- New query param: image_name
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - Deleted required property: expiration_time
              - Deleted required property: full_name
              - Deleted required property: resource_projects
              - Deleted required property: role_name
              - Deleted required property: role_uuid
              - Deleted required property: url
              - Deleted required property: username
              - Deleted required property: uuid
            - Properties changed
              - Modified property: resource_projects
                - Items changed
                  - Required changed
                    - Deleted required property: name
                    - Deleted required property: role_name
                    - Deleted required property: role_uuid
                    - Deleted required property: url
                    - Deleted required property: uuid

POST /api/marketplace-resources/{uuid}/terminate/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: attributes
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true

POST /api/marketplace-resources/{uuid}/update_options/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: options
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: status
              - Description changed from 'Status of the resource response' to ''
              - ReadOnly changed from true to false

GET /api/marketplace-robot-accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: keys
                - Type changed from '' to 'array'
                - Items changed
                  - Schema added
              - Modified property: offering_plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: auto_ok_resource_projects
                      - New property: expose_inference_playground
                      - New property: initial_rolegroup_number
                      - New property: require_effective_id_for_highlighted_display
                      - New property: resource_project_role_group_template
                      - New property: resource_project_role_map
                      - New property: resource_role_group_template
                      - New property: resource_role_map
                      - New property: resource_slug_max_length
                      - New property: resource_slug_template
                      - Modified property: required_team_role_for_provisioning
                        - Nullable changed from false to true
                      - Modified property: resource_name_pattern
                        - Nullable changed from false to true

POST /api/marketplace-robot-accounts/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: keys
            - Type changed from '' to 'array'
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: keys
              - Type changed from '' to 'array'
              - Items changed
                - Schema added

GET /api/marketplace-robot-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: keys
              - Type changed from '' to 'array'
              - Items changed
                - Schema added
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: auto_ok_resource_projects
                    - New property: expose_inference_playground
                    - New property: initial_rolegroup_number
                    - New property: require_effective_id_for_highlighted_display
                    - New property: resource_project_role_group_template
                    - New property: resource_project_role_map
                    - New property: resource_role_group_template
                    - New property: resource_role_map
                    - New property: resource_slug_max_length
                    - New property: resource_slug_template
                    - Modified property: required_team_role_for_provisioning
                      - Nullable changed from false to true
                    - Modified property: resource_name_pattern
                      - Nullable changed from false to true

PATCH /api/marketplace-robot-accounts/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: keys
            - Type changed from '' to 'array'
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: keys
              - Type changed from '' to 'array'
              - Items changed
                - Schema added

PUT /api/marketplace-robot-accounts/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: keys
            - Type changed from '' to 'array'
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: keys
              - Type changed from '' to 'array'
              - Items changed
                - Schema added

POST /api/marketplace-robot-accounts/{uuid}/set_state_creating/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: keys
              - Type changed from '' to 'array'
              - Items changed
                - Schema added
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: auto_ok_resource_projects
                    - New property: expose_inference_playground
                    - New property: initial_rolegroup_number
                    - New property: require_effective_id_for_highlighted_display
                    - New property: resource_project_role_group_template
                    - New property: resource_project_role_map
                    - New property: resource_role_group_template
                    - New property: resource_role_map
                    - New property: resource_slug_max_length
                    - New property: resource_slug_template
                    - Modified property: required_team_role_for_provisioning
                      - Nullable changed from false to true
                    - Modified property: resource_name_pattern
                      - Nullable changed from false to true

POST /api/marketplace-robot-accounts/{uuid}/set_state_deleted/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: keys
              - Type changed from '' to 'array'
              - Items changed
                - Schema added
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: auto_ok_resource_projects
                    - New property: expose_inference_playground
                    - New property: initial_rolegroup_number
                    - New property: require_effective_id_for_highlighted_display
                    - New property: resource_project_role_group_template
                    - New property: resource_project_role_map
                    - New property: resource_role_group_template
                    - New property: resource_role_map
                    - New property: resource_slug_max_length
                    - New property: resource_slug_template
                    - Modified property: required_team_role_for_provisioning
                      - Nullable changed from false to true
                    - Modified property: resource_name_pattern
                      - Nullable changed from false to true

POST /api/marketplace-robot-accounts/{uuid}/set_state_erred/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: keys
              - Type changed from '' to 'array'
              - Items changed
                - Schema added
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: auto_ok_resource_projects
                    - New property: expose_inference_playground
                    - New property: initial_rolegroup_number
                    - New property: require_effective_id_for_highlighted_display
                    - New property: resource_project_role_group_template
                    - New property: resource_project_role_map
                    - New property: resource_role_group_template
                    - New property: resource_role_map
                    - New property: resource_slug_max_length
                    - New property: resource_slug_template
                    - Modified property: required_team_role_for_provisioning
                      - Nullable changed from false to true
                    - Modified property: resource_name_pattern
                      - Nullable changed from false to true

POST /api/marketplace-robot-accounts/{uuid}/set_state_ok/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: keys
              - Type changed from '' to 'array'
              - Items changed
                - Schema added
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: auto_ok_resource_projects
                    - New property: expose_inference_playground
                    - New property: initial_rolegroup_number
                    - New property: require_effective_id_for_highlighted_display
                    - New property: resource_project_role_group_template
                    - New property: resource_project_role_map
                    - New property: resource_role_group_template
                    - New property: resource_role_map
                    - New property: resource_slug_max_length
                    - New property: resource_slug_template
                    - Modified property: required_team_role_for_provisioning
                      - Nullable changed from false to true
                    - Modified property: resource_name_pattern
                      - Nullable changed from false to true

POST /api/marketplace-robot-accounts/{uuid}/set_state_request_deletion/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: keys
              - Type changed from '' to 'array'
              - Items changed
                - Schema added
            - Modified property: offering_plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: auto_ok_resource_projects
                    - New property: expose_inference_playground
                    - New property: initial_rolegroup_number
                    - New property: require_effective_id_for_highlighted_display
                    - New property: resource_project_role_group_template
                    - New property: resource_project_role_map
                    - New property: resource_role_group_template
                    - New property: resource_role_map
                    - New property: resource_slug_max_length
                    - New property: resource_slug_template
                    - Modified property: required_team_role_for_provisioning
                      - Nullable changed from false to true
                    - Modified property: resource_name_pattern
                      - Nullable changed from false to true

GET /api/marketplace-script-async-dry-run/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: order_attributes
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

GET /api/marketplace-script-async-dry-run/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: order_attributes
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

POST /api/marketplace-script-dry-run/{uuid}/async_run/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: attributes
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/marketplace-script-dry-run/{uuid}/run/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: attributes
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: output
          - Properties changed
            - New property: output
            - Deleted property: access_url
            - Deleted property: attributes
            - Deleted property: backend_id
            - Deleted property: backend_metadata
            - Deleted property: billable
            - Deleted property: billing_type_classification
            - Deleted property: category
            - Deleted property: category_title
            - Deleted property: category_uuid
            - Deleted property: citation_count
            - Deleted property: compliance_checklist
            - Deleted property: components
            - Deleted property: country
            - Deleted property: created
            - Deleted property: customer
            - Deleted property: customer_name
            - Deleted property: customer_uuid
            - Deleted property: datacite_doi
            - Deleted property: description
            - Deleted property: documentation_url
            - Deleted property: effective_available_limits
            - Deleted property: endpoints
            - Deleted property: files
            - Deleted property: full_description
            - Deleted property: getting_started
            - Deleted property: google_calendar_is_public
            - Deleted property: google_calendar_link
            - Deleted property: has_compliance_requirements
            - Deleted property: helpdesk_url
            - Deleted property: image
            - Deleted property: integration_guide
            - Deleted property: is_accessible
            - Deleted property: latitude
            - Deleted property: longitude
            - Deleted property: name
            - Deleted property: options
            - Deleted property: order_count
            - Deleted property: organization_groups
            - Deleted property: parent_description
            - Deleted property: parent_name
            - Deleted property: parent_uuid
            - Deleted property: partitions
            - Deleted property: paused_reason
            - Deleted property: plans
            - Deleted property: plugin_options
            - Deleted property: privacy_policy_link
            - Deleted property: profile_name
            - Deleted property: profile_uuid
            - Deleted property: project
            - Deleted property: project_name
            - Deleted property: project_uuid
            - Deleted property: promotion_campaigns
            - Deleted property: quotas
            - Deleted property: resource_options
            - Deleted property: scope
            - Deleted property: scope_error_message
            - Deleted property: scope_name
            - Deleted property: scope_state
            - Deleted property: scope_uuid
            - Deleted property: screenshots
            - Deleted property: shared
            - Deleted property: slug
            - Deleted property: software_catalogs
            - Deleted property: state
            - Deleted property: tags
            - Deleted property: thumbnail
            - Deleted property: total_cost
            - Deleted property: total_cost_estimated
            - Deleted property: total_customers
            - Deleted property: type
            - Deleted property: url
            - Deleted property: user_has_consent
            - Deleted property: uuid
            - Deleted property: vendor_details

GET /api/marketplace-service-providers/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: allowed_domains
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

POST /api/marketplace-service-providers/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: allowed_domains
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: allowed_domains
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: allowed_domains
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: allowed_domains
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/marketplace-service-providers/{service_provider_uuid}/customer_projects/

- New query param: affiliation_name
- New query param: affiliation_uuid
- New query param: has_affiliation
- Deleted query param: affiliated_organization_name
- Deleted query param: affiliated_organization_uuid
- Deleted query param: has_affiliated_organization

GET /api/marketplace-service-providers/{service_provider_uuid}/offerings/

- New query param: offering_group_uuid
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_group_title offering_group_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: offering_group_title
              - New property: offering_group_uuid
              - Modified property: options
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: resource_options
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: secret_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedSecretOptions
                    - Properties changed
                      - Modified property: environ
                        - Type changed from '' to 'array'
                        - Items changed
                          - Schema added

GET /api/marketplace-service-providers/{service_provider_uuid}/projects/

- New query param: affiliation_name
- New query param: affiliation_uuid
- New query param: has_affiliation
- Deleted query param: affiliated_organization_name
- Deleted query param: affiliated_organization_uuid
- Deleted query param: has_affiliated_organization
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [affiliation affiliation_code affiliation_name affiliation_uuid project_metadata]
      - Deleted enum values: [affiliated_organizations]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: affiliation
              - New property: affiliation_code
              - New property: affiliation_name
              - New property: affiliation_uuid
              - New property: project_metadata
              - Deleted property: affiliated_organizations
              - Modified property: kind
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/ProjectKindEnum
                  - Schemas deleted: #/components/schemas/KindEnum
              - Modified property: termination_metadata
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: user_affiliations
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: user_email_patterns
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: user_identity_sources
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

GET /api/marketplace-service-providers/{service_provider_uuid}/users/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: active_isds
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: affiliations
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: eduperson_assurance
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: nationalities
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

GET /api/marketplace-service-providers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: allowed_domains
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PATCH /api/marketplace-service-providers/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: allowed_domains
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: allowed_domains
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: allowed_domains
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: allowed_domains
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PUT /api/marketplace-service-providers/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: allowed_domains
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: allowed_domains
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: allowed_domains
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: allowed_domains
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/marketplace-site-agent-connection-stats/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: agents
              - Items changed
                - Properties changed
                  - Modified property: event_subscriptions
                    - Items changed
                      - Properties changed
                        - Modified property: observable_objects
                          - Type changed from '' to 'object'
                          - AdditionalProperties changed from null to true

GET /api/marketplace-site-agent-identities/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: dependencies
                - Type changed from '' to 'array'
                - Items changed
                  - Schema added
              - Modified property: services
                - Items changed
                  - Properties changed
                    - Modified property: statistics
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true

POST /api/marketplace-site-agent-identities/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: dependencies
            - Type changed from '' to 'array'
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: dependencies
              - Type changed from '' to 'array'
              - Items changed
                - Schema added
            - Modified property: services
              - Items changed
                - Properties changed
                  - Modified property: statistics
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true

POST /api/marketplace-site-agent-identities/cleanup_orphaned/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: items
              - Items changed
                - Required changed
                  - New required property: name
                  - New required property: uuid
                - Properties changed
                  - New property: created
                  - New property: identity__name
                  - New property: modified
                  - New property: name
                  - New property: offering__name
                  - New property: state
                  - New property: uuid
                - AdditionalProperties changed
                  - Schema deleted

GET /api/marketplace-site-agent-identities/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: dependencies
              - Type changed from '' to 'array'
              - Items changed
                - Schema added
            - Modified property: services
              - Items changed
                - Properties changed
                  - Modified property: statistics
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true

PUT /api/marketplace-site-agent-identities/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: dependencies
            - Type changed from '' to 'array'
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: dependencies
              - Type changed from '' to 'array'
              - Items changed
                - Schema added
            - Modified property: services
              - Items changed
                - Properties changed
                  - Modified property: statistics
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true

POST /api/marketplace-site-agent-identities/{uuid}/register_event_subscription/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: observable_object_type
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/ObservableObjectTypeEnum
                - New enum values: [offering_resources_sync]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: observable_objects
              - Type changed from '' to 'array'
              - Items changed
                - Schema added
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: observable_objects
              - Type changed from '' to 'array'
              - Items changed
                - Schema added

POST /api/marketplace-site-agent-identities/{uuid}/register_service/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: statistics
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: statistics
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/marketplace-site-agent-services/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: statistics
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

POST /api/marketplace-site-agent-services/cleanup_stale/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: items
              - Items changed
                - Required changed
                  - New required property: name
                  - New required property: uuid
                - Properties changed
                  - New property: created
                  - New property: identity__name
                  - New property: modified
                  - New property: name
                  - New property: offering__name
                  - New property: state
                  - New property: uuid
                - AdditionalProperties changed
                  - Schema deleted

GET /api/marketplace-site-agent-services/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: statistics
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

POST /api/marketplace-site-agent-services/{uuid}/set_statistics/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: statistics
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: statistics
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/marketplace-site-agent-stats/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: identities
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/AgentStatsIdentities
              - Type changed from 'object' to ''
              - AdditionalProperties changed
                - Schema deleted
            - Modified property: processors
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/AgentStatsProcessors
              - Type changed from 'object' to ''
              - AdditionalProperties changed
                - Schema deleted
            - Modified property: services
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/AgentStatsServices
              - Type changed from 'object' to ''
              - AdditionalProperties changed
                - Schema deleted

GET /api/marketplace-site-agent-task-stats/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: active_tasks
              - Items changed
                - Required changed
                  - New required property: id
                  - New required property: name
                  - New required property: worker
                - Properties changed
                  - New property: args
                  - New property: id
                  - New property: name
                  - New property: worker
                - AdditionalProperties changed
                  - Schema deleted
            - Modified property: reserved_tasks
              - Items changed
                - Required changed
                  - New required property: id
                  - New required property: name
                - Properties changed
                  - New property: id
                  - New property: name
                - AdditionalProperties changed
                  - Schema deleted
            - Modified property: scheduled_tasks
              - Items changed
                - Required changed
                  - New required property: eta
                  - New required property: id
                  - New required property: name
                - Properties changed
                  - New property: eta
                  - New property: id
                  - New property: name
                - AdditionalProperties changed
                  - Schema deleted

GET /api/marketplace-slurm-periodic-usage-policies/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: options
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: tres_billing_weights
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

POST /api/marketplace-slurm-periodic-usage-policies/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: options
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: tres_billing_weights
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: tres_billing_weights
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/marketplace-slurm-periodic-usage-policies/actions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Type changed from 'object' to 'array'
          - Items changed
            - Schema added
          - Required changed
            - Deleted required property: actions
            - Deleted required property: affected_resources_count
            - Deleted required property: component_limits_set
            - Deleted required property: created
            - Deleted required property: created_by_full_name
            - Deleted required property: created_by_username
            - Deleted required property: fired_datetime
            - Deleted required property: has_fired
            - Deleted required property: period_name
            - Deleted required property: scope
            - Deleted required property: scope_name
            - Deleted required property: scope_uuid
            - Deleted required property: url
            - Deleted required property: uuid
            - Deleted required property: warnings
          - Properties changed
            - Deleted property: actions
            - Deleted property: affected_resources_count
            - Deleted property: apply_to_all
            - Deleted property: carryover_enabled
            - Deleted property: carryover_factor
            - Deleted property: component_limits_set
            - Deleted property: created
            - Deleted property: created_by_full_name
            - Deleted property: created_by_username
            - Deleted property: fired_datetime
            - Deleted property: grace_ratio
            - Deleted property: has_fired
            - Deleted property: limit_type
            - Deleted property: options
            - Deleted property: organization_groups
            - Deleted property: period
            - Deleted property: period_name
            - Deleted property: qos_strategy
            - Deleted property: raw_usage_reset
            - Deleted property: scope
            - Deleted property: scope_name
            - Deleted property: scope_uuid
            - Deleted property: tres_billing_enabled
            - Deleted property: tres_billing_weights
            - Deleted property: url
            - Deleted property: uuid
            - Deleted property: warnings

POST /api/marketplace-slurm-periodic-usage-policies/preview_impact/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: command_history
              - Items changed
                - Properties changed
                  - Modified property: parameters
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true

GET /api/marketplace-slurm-periodic-usage-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: tres_billing_weights
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PATCH /api/marketplace-slurm-periodic-usage-policies/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: options
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: tres_billing_weights
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: tres_billing_weights
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PUT /api/marketplace-slurm-periodic-usage-policies/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: options
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: tres_billing_weights
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: tres_billing_weights
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/marketplace-slurm-periodic-usage-policies/{uuid}/command-history/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: parameters
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

GET /api/marketplace-slurm-periodic-usage-policies/{uuid}/evaluation-logs/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: actions_taken
            - Properties changed
              - Modified property: actions_taken
                - Type changed from '' to 'array'
                - Description changed from 'List of actions taken during this evaluation (e.g. ['pause', 'notify'])' to ''
                - ReadOnly changed from false to true
                - Items changed
                  - Schema added
              - Modified property: new_state
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: previous_state
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: site_agent_response
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

GET /api/marketplace-software-catalogs/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: metadata
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

POST /api/marketplace-software-catalogs/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: metadata
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/marketplace-software-catalogs/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PATCH /api/marketplace-software-catalogs/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: metadata
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PUT /api/marketplace-software-catalogs/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: metadata
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/marketplace-software-packages/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: categories
              - New required property: licenses
              - New required property: maintainers
            - Properties changed
              - Modified property: categories
                - Type changed from '' to 'array'
                - Description changed from 'Package categories (e.g., ['bio', 'hpc', 'build-tools'])' to ''
                - ReadOnly changed from false to true
                - Items changed
                  - Schema added
              - Modified property: licenses
                - Type changed from '' to 'array'
                - Description changed from 'Software licenses (e.g., ['GPL-3.0', 'MIT'])' to ''
                - ReadOnly changed from false to true
                - Items changed
                  - Schema added
              - Modified property: maintainers
                - Type changed from '' to 'array'
                - Description changed from 'Package maintainers' to ''
                - ReadOnly changed from false to true
                - Items changed
                  - Schema added
              - Modified property: versions
                - Items changed
                  - Properties changed
                    - New property: module_version
                    - Modified property: module
                      - Property 'AllOf' changed
                        - Schemas added: #/components/schemas/SoftwareModule
                      - Type changed from 'object' to ''
                      - Nullable changed from false to true
                      - AdditionalProperties changed
                        - Schema deleted
                    - Modified property: targets
                      - Items changed
                        - Properties changed
                          - Modified property: gpu_architectures
                            - Type changed from '' to 'object'
                            - AdditionalProperties changed from null to true
                          - Modified property: metadata
                            - Type changed from '' to 'object'
                            - AdditionalProperties changed from null to true
                    - Modified property: toolchain
                      - Property 'AllOf' changed
                        - Schemas added: #/components/schemas/SoftwareToolchain
                      - Type changed from 'object' to ''
                      - Nullable changed from false to true
                      - AdditionalProperties changed
                        - Schema deleted

POST /api/marketplace-software-packages/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: categories
          - Deleted property: licenses
          - Deleted property: maintainers
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: categories
            - New required property: licenses
            - New required property: maintainers
          - Properties changed
            - Modified property: categories
              - Type changed from '' to 'array'
              - Description changed from 'Package categories (e.g., ['bio', 'hpc', 'build-tools'])' to ''
              - ReadOnly changed from false to true
              - Items changed
                - Schema added
            - Modified property: licenses
              - Type changed from '' to 'array'
              - Description changed from 'Software licenses (e.g., ['GPL-3.0', 'MIT'])' to ''
              - ReadOnly changed from false to true
              - Items changed
                - Schema added
            - Modified property: maintainers
              - Type changed from '' to 'array'
              - Description changed from 'Package maintainers' to ''
              - ReadOnly changed from false to true
              - Items changed
                - Schema added
            - Modified property: versions
              - Items changed
                - Properties changed
                  - New property: module_version
                  - Modified property: module
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/SoftwareModule
                    - Type changed from 'object' to ''
                    - Nullable changed from false to true
                    - AdditionalProperties changed
                      - Schema deleted
                  - Modified property: targets
                    - Items changed
                      - Properties changed
                        - Modified property: gpu_architectures
                          - Type changed from '' to 'object'
                          - AdditionalProperties changed from null to true
                        - Modified property: metadata
                          - Type changed from '' to 'object'
                          - AdditionalProperties changed from null to true
                  - Modified property: toolchain
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/SoftwareToolchain
                    - Type changed from 'object' to ''
                    - Nullable changed from false to true
                    - AdditionalProperties changed
                      - Schema deleted

GET /api/marketplace-software-packages/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: categories
            - New required property: licenses
            - New required property: maintainers
          - Properties changed
            - Modified property: categories
              - Type changed from '' to 'array'
              - Description changed from 'Package categories (e.g., ['bio', 'hpc', 'build-tools'])' to ''
              - ReadOnly changed from false to true
              - Items changed
                - Schema added
            - Modified property: licenses
              - Type changed from '' to 'array'
              - Description changed from 'Software licenses (e.g., ['GPL-3.0', 'MIT'])' to ''
              - ReadOnly changed from false to true
              - Items changed
                - Schema added
            - Modified property: maintainers
              - Type changed from '' to 'array'
              - Description changed from 'Package maintainers' to ''
              - ReadOnly changed from false to true
              - Items changed
                - Schema added
            - Modified property: versions
              - Items changed
                - Properties changed
                  - New property: module_version
                  - Modified property: module
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/SoftwareModule
                    - Type changed from 'object' to ''
                    - Nullable changed from false to true
                    - AdditionalProperties changed
                      - Schema deleted
                  - Modified property: targets
                    - Items changed
                      - Properties changed
                        - Modified property: gpu_architectures
                          - Type changed from '' to 'object'
                          - AdditionalProperties changed from null to true
                        - Modified property: metadata
                          - Type changed from '' to 'object'
                          - AdditionalProperties changed from null to true
                  - Modified property: toolchain
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/SoftwareToolchain
                    - Type changed from 'object' to ''
                    - Nullable changed from false to true
                    - AdditionalProperties changed
                      - Schema deleted

PATCH /api/marketplace-software-packages/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: categories
          - Deleted property: licenses
          - Deleted property: maintainers
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: categories
            - New required property: licenses
            - New required property: maintainers
          - Properties changed
            - Modified property: categories
              - Type changed from '' to 'array'
              - Description changed from 'Package categories (e.g., ['bio', 'hpc', 'build-tools'])' to ''
              - ReadOnly changed from false to true
              - Items changed
                - Schema added
            - Modified property: licenses
              - Type changed from '' to 'array'
              - Description changed from 'Software licenses (e.g., ['GPL-3.0', 'MIT'])' to ''
              - ReadOnly changed from false to true
              - Items changed
                - Schema added
            - Modified property: maintainers
              - Type changed from '' to 'array'
              - Description changed from 'Package maintainers' to ''
              - ReadOnly changed from false to true
              - Items changed
                - Schema added
            - Modified property: versions
              - Items changed
                - Properties changed
                  - New property: module_version
                  - Modified property: module
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/SoftwareModule
                    - Type changed from 'object' to ''
                    - Nullable changed from false to true
                    - AdditionalProperties changed
                      - Schema deleted
                  - Modified property: targets
                    - Items changed
                      - Properties changed
                        - Modified property: gpu_architectures
                          - Type changed from '' to 'object'
                          - AdditionalProperties changed from null to true
                        - Modified property: metadata
                          - Type changed from '' to 'object'
                          - AdditionalProperties changed from null to true
                  - Modified property: toolchain
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/SoftwareToolchain
                    - Type changed from 'object' to ''
                    - Nullable changed from false to true
                    - AdditionalProperties changed
                      - Schema deleted

PUT /api/marketplace-software-packages/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: categories
          - Deleted property: licenses
          - Deleted property: maintainers
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: categories
            - New required property: licenses
            - New required property: maintainers
          - Properties changed
            - Modified property: categories
              - Type changed from '' to 'array'
              - Description changed from 'Package categories (e.g., ['bio', 'hpc', 'build-tools'])' to ''
              - ReadOnly changed from false to true
              - Items changed
                - Schema added
            - Modified property: licenses
              - Type changed from '' to 'array'
              - Description changed from 'Software licenses (e.g., ['GPL-3.0', 'MIT'])' to ''
              - ReadOnly changed from false to true
              - Items changed
                - Schema added
            - Modified property: maintainers
              - Type changed from '' to 'array'
              - Description changed from 'Package maintainers' to ''
              - ReadOnly changed from false to true
              - Items changed
                - Schema added
            - Modified property: versions
              - Items changed
                - Properties changed
                  - New property: module_version
                  - Modified property: module
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/SoftwareModule
                    - Type changed from 'object' to ''
                    - Nullable changed from false to true
                    - AdditionalProperties changed
                      - Schema deleted
                  - Modified property: targets
                    - Items changed
                      - Properties changed
                        - Modified property: gpu_architectures
                          - Type changed from '' to 'object'
                          - AdditionalProperties changed from null to true
                        - Modified property: metadata
                          - Type changed from '' to 'object'
                          - AdditionalProperties changed from null to true
                  - Modified property: toolchain
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/SoftwareToolchain
                    - Type changed from 'object' to ''
                    - Nullable changed from false to true
                    - AdditionalProperties changed
                      - Schema deleted

GET /api/marketplace-software-targets/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: gpu_architectures
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: metadata
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

POST /api/marketplace-software-targets/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: gpu_architectures
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/marketplace-software-targets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: gpu_architectures
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PATCH /api/marketplace-software-targets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: gpu_architectures
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PUT /api/marketplace-software-targets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: gpu_architectures
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/marketplace-software-versions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: module_version
            - Properties changed
              - New property: module_version
              - Modified property: dependencies
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: metadata
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: module
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/SoftwareModule
                - Type changed from 'object' to ''
                - Nullable changed from false to true
                - AdditionalProperties changed
                  - Schema deleted
              - Modified property: toolchain
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/SoftwareToolchain
                - Type changed from 'object' to ''
                - Nullable changed from false to true
                - AdditionalProperties changed
                  - Schema deleted

POST /api/marketplace-software-versions/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: module_version
          - Properties changed
            - New property: module_version
            - Modified property: dependencies
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: module
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/SoftwareModule
              - Type changed from 'object' to ''
              - Nullable changed from false to true
              - AdditionalProperties changed
                - Schema deleted
            - Modified property: toolchain
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/SoftwareToolchain
              - Type changed from 'object' to ''
              - Nullable changed from false to true
              - AdditionalProperties changed
                - Schema deleted

GET /api/marketplace-software-versions/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: module_version
          - Properties changed
            - New property: module_version
            - Modified property: dependencies
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: module
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/SoftwareModule
              - Type changed from 'object' to ''
              - Nullable changed from false to true
              - AdditionalProperties changed
                - Schema deleted
            - Modified property: toolchain
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/SoftwareToolchain
              - Type changed from 'object' to ''
              - Nullable changed from false to true
              - AdditionalProperties changed
                - Schema deleted

PATCH /api/marketplace-software-versions/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: module_version
          - Properties changed
            - New property: module_version
            - Modified property: dependencies
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: module
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/SoftwareModule
              - Type changed from 'object' to ''
              - Nullable changed from false to true
              - AdditionalProperties changed
                - Schema deleted
            - Modified property: toolchain
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/SoftwareToolchain
              - Type changed from 'object' to ''
              - Nullable changed from false to true
              - AdditionalProperties changed
                - Schema deleted

PUT /api/marketplace-software-versions/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: module_version
          - Properties changed
            - New property: module_version
            - Modified property: dependencies
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: module
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/SoftwareModule
              - Type changed from 'object' to ''
              - Nullable changed from false to true
              - AdditionalProperties changed
                - Schema deleted
            - Modified property: toolchain
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/SoftwareToolchain
              - Type changed from 'object' to ''
              - Nullable changed from false to true
              - AdditionalProperties changed
                - Schema deleted

GET /api/marketplace-stats/provider_customers/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: monthly
              - Items changed
                - Required changed
                  - New required property: customer_count
                  - New required property: month
                - Properties changed
                  - New property: customer_count
                  - New property: month
                - AdditionalProperties changed
                  - Schema deleted
            - Modified property: top_by_resources
              - Items changed
                - Required changed
                  - New required property: customer_name
                  - New required property: customer_uuid
                  - New required property: resource_count
                - Properties changed
                  - New property: customer_name
                  - New property: customer_uuid
                  - New property: resource_count
                - AdditionalProperties changed
                  - Schema deleted
            - Modified property: top_by_revenue
              - Items changed
                - Required changed
                  - New required property: customer_name
                  - New required property: customer_uuid
                  - New required property: revenue
                - Properties changed
                  - New property: customer_name
                  - New property: customer_uuid
                  - New property: revenue
                - AdditionalProperties changed
                  - Schema deleted

GET /api/marketplace-stats/provider_offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offerings
              - Items changed
                - Required changed
                  - New required property: active_resources
                  - New required property: category_name
                  - New required property: offering_name
                  - New required property: offering_uuid
                  - New required property: plans
                  - New required property: revenue
                  - New required property: state
                  - New required property: total_resources
                - Properties changed
                  - New property: active_resources
                  - New property: category_name
                  - New property: offering_name
                  - New property: offering_uuid
                  - New property: plans
                  - New property: revenue
                  - New property: state
                  - New property: total_resources
                - AdditionalProperties changed
                  - Schema deleted

GET /api/marketplace-stats/provider_resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: by_offering
              - Items changed
                - Required changed
                  - New required property: count
                  - New required property: offering_name
                  - New required property: offering_uuid
                - Properties changed
                  - New property: count
                  - New property: offering_name
                  - New property: offering_uuid
                - AdditionalProperties changed
                  - Schema deleted
            - Modified property: monthly
              - Items changed
                - Required changed
                  - New required property: count
                  - New required property: month
                - Properties changed
                  - New property: count
                  - New property: month
                - AdditionalProperties changed
                  - Schema deleted

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
                  - New enum values: [marketplace_offering_options_updated marketplace_offering_resource_options_updated marketplace_resource_limit_change_request_created marketplace_resource_limit_change_request_approved marketplace_resource_limit_change_request_rejected openstack_instance_security_groups_changed openstack_load_balancer_created openstack_load_balancer_updated openstack_load_balancer_deleted openstack_load_balancer_security_groups_changed openstack_listener_created openstack_listener_updated openstack_listener_deleted openstack_pool_created openstack_pool_updated openstack_pool_deleted openstack_pool_member_created openstack_pool_member_updated openstack_pool_member_deleted openstack_port_security_enabled openstack_port_security_disabled openstack_port_allowed_address_pairs_changed openstack_port_security_groups_changed openstack_rbac_policy_created openstack_rbac_policy_deleted openstack_router_interface_added openstack_router_interface_removed openstack_subnet_host_routes_changed openstack_security_group_rules_changed proposal_workflow_advanced resource_rescue_failed resource_rescue_scheduled resource_rescue_succeeded resource_unrescue_failed resource_unrescue_scheduled resource_unrescue_succeeded]

GET /api/metadata/features/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: features
              - Description changed from 'List of feature sections with descriptions' to ''
              - Items changed
                - Required changed
                  - New required property: description
                  - New required property: items
                  - New required property: key
                - Properties changed
                  - New property: description
                  - New property: items
                  - New property: key
                - AdditionalProperties changed
                  - Schema deleted

GET /api/metadata/permissions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: permission_descriptions
              - Items changed
                - Required changed
                  - New required property: label
                  - New required property: options
                - Properties changed
                  - New property: label
                  - New property: options
                - AdditionalProperties changed
                  - Schema deleted

GET /api/metadata/settings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: settings
              - Description changed from 'List of settings sections with configuration items' to ''
              - Items changed
                - Required changed
                  - New required property: description
                  - New required property: items
                - Properties changed
                  - New property: description
                  - New property: items
                - AdditionalProperties changed
                  - Schema deleted

GET /api/onboarding-verifications/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: raw_response
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: verified_company_data
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: verified_user_roles
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

POST /api/onboarding-verifications/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: raw_response
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: verified_company_data
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: verified_user_roles
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/onboarding-verifications/checklist-template/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: checklist
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/ChecklistShort
              - Type changed from 'object' to ''
              - AdditionalProperties changed
                - Schema deleted
            - Modified property: initial_visible_questions
              - Items changed
                - Properties changed
                  - New property: likert_allow_na
                  - New property: likert_high_label
                  - New property: likert_low_label
                  - New property: likert_scale_length
                  - New property: rich_text_char_limit
                  - New property: rich_text_toolbar_level
                  - Modified property: allowed_file_types
                    - Type changed from '' to 'array'
                    - Description changed from 'List of allowed file extensions (e.g., ['.pdf', '.doc', '.docx']). If empty, all file types are allowed.' to ''
                    - Items changed
                      - Schema added
                  - Modified property: allowed_mime_types
                    - Type changed from '' to 'array'
                    - Description changed from 'List of allowed MIME types (e.g., ['application/pdf', 'application/msword']). If empty, MIME type validation is not enforced. When both extensions and MIME types are specified, files must match both criteria for security.' to ''
                    - Items changed
                      - Schema added
                  - Modified property: guidance_answer_value
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: question_type
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/QuestionTypeEnum
                        - New enum values: [likert rich_text]
                  - Modified property: review_answer_value
                    - Description changed from 'Answer value that trigger review.' to ''
                    - Nullable changed from true to false
            - Modified property: questions
              - Items changed
                - Properties changed
                  - New property: likert_allow_na
                  - New property: likert_high_label
                  - New property: likert_low_label
                  - New property: likert_scale_length
                  - New property: rich_text_char_limit
                  - New property: rich_text_toolbar_level
                  - Modified property: allowed_file_types
                    - Type changed from '' to 'array'
                    - Description changed from 'List of allowed file extensions (e.g., ['.pdf', '.doc', '.docx']). If empty, all file types are allowed.' to ''
                    - Items changed
                      - Schema added
                  - Modified property: allowed_mime_types
                    - Type changed from '' to 'array'
                    - Description changed from 'List of allowed MIME types (e.g., ['application/pdf', 'application/msword']). If empty, MIME type validation is not enforced. When both extensions and MIME types are specified, files must match both criteria for security.' to ''
                    - Items changed
                      - Schema added
                  - Modified property: guidance_answer_value
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: question_type
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/QuestionTypeEnum
                        - New enum values: [likert rich_text]
                  - Modified property: review_answer_value
                    - Description changed from 'Answer value that trigger review.' to ''
                    - Nullable changed from true to false

POST /api/onboarding-verifications/start_verification/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: raw_response
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: verified_company_data
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: verified_user_roles
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/onboarding-verifications/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: raw_response
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: verified_company_data
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: verified_user_roles
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PATCH /api/onboarding-verifications/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: raw_response
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: verified_company_data
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: verified_user_roles
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PUT /api/onboarding-verifications/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: raw_response
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: verified_company_data
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: verified_user_roles
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/onboarding-verifications/{uuid}/checklist/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: checklist
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/ChecklistShort
              - Type changed from 'object' to ''
              - AdditionalProperties changed
                - Schema deleted
            - Modified property: questions
              - Items changed
                - Required changed
                  - New required property: likert_allow_na
                  - New required property: likert_high_label
                  - New required property: likert_low_label
                  - New required property: likert_scale_length
                  - New required property: rich_text_char_limit
                  - New required property: rich_text_toolbar_level
                - Properties changed
                  - New property: likert_allow_na
                  - New property: likert_high_label
                  - New property: likert_low_label
                  - New property: likert_scale_length
                  - New property: rich_text_char_limit
                  - New property: rich_text_toolbar_level
                  - Modified property: allowed_file_types
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: allowed_mime_types
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: dependencies_info
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/QuestionDependencyInfo
                    - Type changed from 'object' to ''
                    - AdditionalProperties changed
                      - Schema deleted
                  - Modified property: existing_answer
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/Answer
                    - Type changed from 'object' to ''
                    - AdditionalProperties changed
                      - Schema deleted
                  - Modified property: question_type
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/QuestionTypeEnum
                        - New enum values: [likert rich_text]

POST /api/onboarding-verifications/{uuid}/create_customer/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: default_affiliations
            - Modified property: user_affiliations
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_email_patterns
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_identity_sources
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

POST /api/onboarding-verifications/{uuid}/run_validation/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: raw_response
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: verified_company_data
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: verified_user_roles
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

POST /api/onboarding-verifications/{uuid}/submit_answers/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: raw_response
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: verified_company_data
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: verified_user_roles
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

POST /api/openportal-allocations/{uuid}/set_limits/

- Responses changed
  - New response: 202
  - Deleted response: 200

GET /api/openportal-managed-projects/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: details
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/ManagedProjectDetails
                - Description changed from 'Details of the project as provided by the remote OpenPortal.' to ''
              - Modified property: project_template_data
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/ProjectTemplate
                    - Properties changed
                      - Modified property: allocation_units_mapping
                        - Type changed from '' to 'object'
                        - AdditionalProperties changed from null to true
                      - Modified property: role_mapping
                        - Type changed from '' to 'object'
                        - AdditionalProperties changed from null to true

GET /api/openportal-managed-projects/{identifier}/{destination}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: details
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/ManagedProjectDetails
              - Description changed from 'Details of the project as provided by the remote OpenPortal.' to ''
            - Modified property: project_template_data
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ProjectTemplate
                  - Properties changed
                    - Modified property: allocation_units_mapping
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: role_mapping
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true

GET /api/openportal-project-template/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: allocation_units_mapping
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: role_mapping
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

POST /api/openportal-project-template/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: allocation_units_mapping
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: role_mapping
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: allocation_units_mapping
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: role_mapping
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/openportal-project-template/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: allocation_units_mapping
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: role_mapping
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PATCH /api/openportal-project-template/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: allocation_units_mapping
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: role_mapping
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: allocation_units_mapping
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: role_mapping
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PUT /api/openportal-project-template/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: allocation_units_mapping
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: role_mapping
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: allocation_units_mapping
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: role_mapping
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

POST /api/openportal-remote-allocations/{uuid}/set_limits/

- Responses changed
  - New response: 202
  - Deleted response: 200

GET /api/openportal-unmanaged-projects/

- New query param: affiliation_name
- New query param: affiliation_uuid
- New query param: has_affiliation
- Deleted query param: affiliated_organization_name
- Deleted query param: affiliated_organization_uuid
- Deleted query param: has_affiliated_organization
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [affiliation affiliation_code affiliation_name affiliation_uuid project_metadata]
      - Deleted enum values: [affiliated_organizations]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: affiliation
              - New property: affiliation_code
              - New property: affiliation_name
              - New property: affiliation_uuid
              - New property: project_metadata
              - Deleted property: affiliated_organizations
              - Modified property: kind
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/ProjectKindEnum
                  - Schemas deleted: #/components/schemas/KindEnum
              - Modified property: termination_metadata
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: user_affiliations
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: user_email_patterns
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: user_identity_sources
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

HEAD /api/openportal-unmanaged-projects/

- New query param: affiliation_name
- New query param: affiliation_uuid
- New query param: has_affiliation
- Deleted query param: affiliated_organization_name
- Deleted query param: affiliated_organization_uuid
- Deleted query param: has_affiliated_organization

POST /api/openportal-unmanaged-projects/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: affiliation_uuid
          - Modified property: kind
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/ProjectKindEnum
              - Schemas deleted: #/components/schemas/KindEnum
          - Modified property: user_affiliations
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_email_patterns
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_identity_sources
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: affiliation_uuid
          - Modified property: kind
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/ProjectKindEnum
              - Schemas deleted: #/components/schemas/KindEnum
          - Modified property: user_affiliations
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_email_patterns
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_identity_sources
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: affiliation_uuid
          - Modified property: kind
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/ProjectKindEnum
              - Schemas deleted: #/components/schemas/KindEnum
          - Modified property: user_affiliations
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_email_patterns
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_identity_sources
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: affiliation
            - New property: affiliation_code
            - New property: affiliation_name
            - New property: affiliation_uuid
            - New property: project_metadata
            - Deleted property: affiliated_organizations
            - Modified property: kind
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/ProjectKindEnum
                - Schemas deleted: #/components/schemas/KindEnum
            - Modified property: termination_metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_affiliations
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_email_patterns
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_identity_sources
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/openportal-unmanaged-projects/checklist-template/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: checklist
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/ChecklistShort
              - Type changed from 'object' to ''
              - AdditionalProperties changed
                - Schema deleted
            - Modified property: initial_visible_questions
              - Items changed
                - Properties changed
                  - New property: likert_allow_na
                  - New property: likert_high_label
                  - New property: likert_low_label
                  - New property: likert_scale_length
                  - New property: rich_text_char_limit
                  - New property: rich_text_toolbar_level
                  - Modified property: allowed_file_types
                    - Type changed from '' to 'array'
                    - Description changed from 'List of allowed file extensions (e.g., ['.pdf', '.doc', '.docx']). If empty, all file types are allowed.' to ''
                    - Items changed
                      - Schema added
                  - Modified property: allowed_mime_types
                    - Type changed from '' to 'array'
                    - Description changed from 'List of allowed MIME types (e.g., ['application/pdf', 'application/msword']). If empty, MIME type validation is not enforced. When both extensions and MIME types are specified, files must match both criteria for security.' to ''
                    - Items changed
                      - Schema added
                  - Modified property: guidance_answer_value
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: question_type
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/QuestionTypeEnum
                        - New enum values: [likert rich_text]
                  - Modified property: review_answer_value
                    - Description changed from 'Answer value that trigger review.' to ''
                    - Nullable changed from true to false
            - Modified property: questions
              - Items changed
                - Properties changed
                  - New property: likert_allow_na
                  - New property: likert_high_label
                  - New property: likert_low_label
                  - New property: likert_scale_length
                  - New property: rich_text_char_limit
                  - New property: rich_text_toolbar_level
                  - Modified property: allowed_file_types
                    - Type changed from '' to 'array'
                    - Description changed from 'List of allowed file extensions (e.g., ['.pdf', '.doc', '.docx']). If empty, all file types are allowed.' to ''
                    - Items changed
                      - Schema added
                  - Modified property: allowed_mime_types
                    - Type changed from '' to 'array'
                    - Description changed from 'List of allowed MIME types (e.g., ['application/pdf', 'application/msword']). If empty, MIME type validation is not enforced. When both extensions and MIME types are specified, files must match both criteria for security.' to ''
                    - Items changed
                      - Schema added
                  - Modified property: guidance_answer_value
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: question_type
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/QuestionTypeEnum
                        - New enum values: [likert rich_text]
                  - Modified property: review_answer_value
                    - Description changed from 'Answer value that trigger review.' to ''
                    - Nullable changed from true to false

GET /api/openportal-unmanaged-projects/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [affiliation affiliation_code affiliation_name affiliation_uuid project_metadata]
      - Deleted enum values: [affiliated_organizations]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: affiliation
            - New property: affiliation_code
            - New property: affiliation_name
            - New property: affiliation_uuid
            - New property: project_metadata
            - Deleted property: affiliated_organizations
            - Modified property: kind
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/ProjectKindEnum
                - Schemas deleted: #/components/schemas/KindEnum
            - Modified property: termination_metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_affiliations
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_email_patterns
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_identity_sources
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PATCH /api/openportal-unmanaged-projects/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: affiliation_uuid
          - Modified property: kind
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/ProjectKindEnum
              - Schemas deleted: #/components/schemas/KindEnum
          - Modified property: user_affiliations
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_email_patterns
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_identity_sources
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: affiliation_uuid
          - Modified property: kind
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/ProjectKindEnum
              - Schemas deleted: #/components/schemas/KindEnum
          - Modified property: user_affiliations
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_email_patterns
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_identity_sources
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: affiliation_uuid
          - Modified property: kind
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/ProjectKindEnum
              - Schemas deleted: #/components/schemas/KindEnum
          - Modified property: user_affiliations
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_email_patterns
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_identity_sources
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: affiliation
            - New property: affiliation_code
            - New property: affiliation_name
            - New property: affiliation_uuid
            - New property: project_metadata
            - Deleted property: affiliated_organizations
            - Modified property: kind
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/ProjectKindEnum
                - Schemas deleted: #/components/schemas/KindEnum
            - Modified property: termination_metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_affiliations
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_email_patterns
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_identity_sources
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PUT /api/openportal-unmanaged-projects/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: affiliation_uuid
          - Modified property: kind
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/ProjectKindEnum
              - Schemas deleted: #/components/schemas/KindEnum
          - Modified property: user_affiliations
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_email_patterns
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_identity_sources
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: affiliation_uuid
          - Modified property: kind
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/ProjectKindEnum
              - Schemas deleted: #/components/schemas/KindEnum
          - Modified property: user_affiliations
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_email_patterns
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_identity_sources
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: affiliation_uuid
          - Modified property: kind
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/ProjectKindEnum
              - Schemas deleted: #/components/schemas/KindEnum
          - Modified property: user_affiliations
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_email_patterns
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_identity_sources
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: affiliation
            - New property: affiliation_code
            - New property: affiliation_name
            - New property: affiliation_uuid
            - New property: project_metadata
            - Deleted property: affiliated_organizations
            - Modified property: kind
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/ProjectKindEnum
                - Schemas deleted: #/components/schemas/KindEnum
            - Modified property: termination_metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_affiliations
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_email_patterns
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_identity_sources
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/openportal-unmanaged-projects/{uuid}/checklist/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: checklist
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/ChecklistShort
              - Type changed from 'object' to ''
              - AdditionalProperties changed
                - Schema deleted
            - Modified property: questions
              - Items changed
                - Required changed
                  - New required property: likert_allow_na
                  - New required property: likert_high_label
                  - New required property: likert_low_label
                  - New required property: likert_scale_length
                  - New required property: rich_text_char_limit
                  - New required property: rich_text_toolbar_level
                - Properties changed
                  - New property: likert_allow_na
                  - New property: likert_high_label
                  - New property: likert_low_label
                  - New property: likert_scale_length
                  - New property: rich_text_char_limit
                  - New property: rich_text_toolbar_level
                  - Modified property: allowed_file_types
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: allowed_mime_types
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: dependencies_info
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/QuestionDependencyInfo
                    - Type changed from 'object' to ''
                    - AdditionalProperties changed
                      - Schema deleted
                  - Modified property: existing_answer
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/Answer
                    - Type changed from 'object' to ''
                    - AdditionalProperties changed
                      - Schema deleted
                  - Modified property: question_type
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/QuestionTypeEnum
                        - New enum values: [likert rich_text]

POST /api/openportal-unmanaged-projects/{uuid}/move_project/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: affiliation
            - New property: affiliation_code
            - New property: affiliation_name
            - New property: affiliation_uuid
            - New property: project_metadata
            - Deleted property: affiliated_organizations
            - Modified property: kind
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/ProjectKindEnum
                - Schemas deleted: #/components/schemas/KindEnum
            - Modified property: termination_metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_affiliations
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_email_patterns
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_identity_sources
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

POST /api/openportal-unmanaged-projects/{uuid}/recover/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: affiliation
            - New property: affiliation_code
            - New property: affiliation_name
            - New property: affiliation_uuid
            - New property: project_metadata
            - Deleted property: affiliated_organizations
            - Modified property: kind
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/ProjectKindEnum
                - Schemas deleted: #/components/schemas/KindEnum
            - Modified property: termination_metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_affiliations
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_email_patterns
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_identity_sources
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/openportal/offering_mapping/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: *
            - Deleted required property: description
            - Deleted required property: name
            - Deleted required property: slug
            - Deleted required property: uuid
          - Properties changed
            - New property: *
            - Deleted property: description
            - Deleted property: name
            - Deleted property: slug
            - Deleted property: uuid

GET /api/openportal/project_mapping/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: *
            - Deleted required property: customer_name
            - Deleted required property: customer_uuid
            - Deleted required property: name
            - Deleted required property: uuid
          - Properties changed
            - New property: *
            - Deleted property: customer_name
            - Deleted property: customer_uuid
            - Deleted property: name
            - Deleted property: uuid

GET /api/openportal/user_mapping/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: *
            - Deleted required property: email
            - Deleted required property: full_name
            - Deleted required property: username
            - Deleted required property: uuid
          - Properties changed
            - New property: *
            - Deleted property: email
            - Deleted property: full_name
            - Deleted property: username
            - Deleted property: uuid

GET /api/openstack-backups/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: instance_ports
                - Items changed
                  - Properties changed
                    - Modified property: security_groups
                      - Items changed
                        - Properties changed
                          - Modified property: rules
                            - Items changed
                              - Properties changed
                                - Modified property: direction
                                  - Property 'AllOf' changed
                                    - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                                    - Schemas deleted: #/components/schemas/DirectionEnum
                                - Modified property: protocol
                                  - Property 'OneOf' changed
                                    - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                                  - Type changed from '' to 'string'
                                  - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                                  - MaxLength changed from null to 40
              - Modified property: instance_security_groups
                - Items changed
                  - Properties changed
                    - Modified property: rules
                      - Items changed
                        - Properties changed
                          - Modified property: direction
                            - Property 'AllOf' changed
                              - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                              - Schemas deleted: #/components/schemas/DirectionEnum
                          - Modified property: protocol
                            - Property 'OneOf' changed
                              - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                            - Type changed from '' to 'string'
                            - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                            - MaxLength changed from null to 40
              - Modified property: metadata
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: restorations
                - Items changed
                  - Properties changed
                    - Modified property: ports
                      - Items changed
                        - Properties changed
                          - Modified property: security_groups
                            - Items changed
                              - Properties changed
                                - Modified property: rules
                                  - Items changed
                                    - Properties changed
                                      - Modified property: direction
                                        - Property 'AllOf' changed
                                          - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                                          - Schemas deleted: #/components/schemas/DirectionEnum
                                      - Modified property: protocol
                                        - Property 'OneOf' changed
                                          - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                                        - Type changed from '' to 'string'
                                        - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                                        - MaxLength changed from null to 40
                    - Modified property: security_groups
                      - Items changed
                        - Properties changed
                          - Modified property: rules
                            - Items changed
                              - Properties changed
                                - Modified property: direction
                                  - Property 'AllOf' changed
                                    - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                                    - Schemas deleted: #/components/schemas/DirectionEnum
                                - Modified property: protocol
                                  - Property 'OneOf' changed
                                    - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                                  - Type changed from '' to 'string'
                                  - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                                  - MaxLength changed from null to 40

GET /api/openstack-backups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: direction
                                - Property 'AllOf' changed
                                  - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                                  - Schemas deleted: #/components/schemas/DirectionEnum
                              - Modified property: protocol
                                - Property 'OneOf' changed
                                  - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                                - Type changed from '' to 'string'
                                - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                                - MaxLength changed from null to 40
            - Modified property: instance_security_groups
              - Items changed
                - Properties changed
                  - Modified property: rules
                    - Items changed
                      - Properties changed
                        - Modified property: direction
                          - Property 'AllOf' changed
                            - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                            - Schemas deleted: #/components/schemas/DirectionEnum
                        - Modified property: protocol
                          - Property 'OneOf' changed
                            - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                          - Type changed from '' to 'string'
                          - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                          - MaxLength changed from null to 40
            - Modified property: metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: security_groups
                          - Items changed
                            - Properties changed
                              - Modified property: rules
                                - Items changed
                                  - Properties changed
                                    - Modified property: direction
                                      - Property 'AllOf' changed
                                        - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                                        - Schemas deleted: #/components/schemas/DirectionEnum
                                    - Modified property: protocol
                                      - Property 'OneOf' changed
                                        - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                                      - Type changed from '' to 'string'
                                      - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                                      - MaxLength changed from null to 40
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: direction
                                - Property 'AllOf' changed
                                  - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                                  - Schemas deleted: #/components/schemas/DirectionEnum
                              - Modified property: protocol
                                - Property 'OneOf' changed
                                  - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                                - Type changed from '' to 'string'
                                - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                                - MaxLength changed from null to 40

PATCH /api/openstack-backups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: direction
                                - Property 'AllOf' changed
                                  - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                                  - Schemas deleted: #/components/schemas/DirectionEnum
                              - Modified property: protocol
                                - Property 'OneOf' changed
                                  - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                                - Type changed from '' to 'string'
                                - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                                - MaxLength changed from null to 40
            - Modified property: instance_security_groups
              - Items changed
                - Properties changed
                  - Modified property: rules
                    - Items changed
                      - Properties changed
                        - Modified property: direction
                          - Property 'AllOf' changed
                            - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                            - Schemas deleted: #/components/schemas/DirectionEnum
                        - Modified property: protocol
                          - Property 'OneOf' changed
                            - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                          - Type changed from '' to 'string'
                          - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                          - MaxLength changed from null to 40
            - Modified property: metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: security_groups
                          - Items changed
                            - Properties changed
                              - Modified property: rules
                                - Items changed
                                  - Properties changed
                                    - Modified property: direction
                                      - Property 'AllOf' changed
                                        - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                                        - Schemas deleted: #/components/schemas/DirectionEnum
                                    - Modified property: protocol
                                      - Property 'OneOf' changed
                                        - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                                      - Type changed from '' to 'string'
                                      - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                                      - MaxLength changed from null to 40
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: direction
                                - Property 'AllOf' changed
                                  - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                                  - Schemas deleted: #/components/schemas/DirectionEnum
                              - Modified property: protocol
                                - Property 'OneOf' changed
                                  - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                                - Type changed from '' to 'string'
                                - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                                - MaxLength changed from null to 40

PUT /api/openstack-backups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: direction
                                - Property 'AllOf' changed
                                  - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                                  - Schemas deleted: #/components/schemas/DirectionEnum
                              - Modified property: protocol
                                - Property 'OneOf' changed
                                  - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                                - Type changed from '' to 'string'
                                - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                                - MaxLength changed from null to 40
            - Modified property: instance_security_groups
              - Items changed
                - Properties changed
                  - Modified property: rules
                    - Items changed
                      - Properties changed
                        - Modified property: direction
                          - Property 'AllOf' changed
                            - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                            - Schemas deleted: #/components/schemas/DirectionEnum
                        - Modified property: protocol
                          - Property 'OneOf' changed
                            - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                          - Type changed from '' to 'string'
                          - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                          - MaxLength changed from null to 40
            - Modified property: metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: security_groups
                          - Items changed
                            - Properties changed
                              - Modified property: rules
                                - Items changed
                                  - Properties changed
                                    - Modified property: direction
                                      - Property 'AllOf' changed
                                        - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                                        - Schemas deleted: #/components/schemas/DirectionEnum
                                    - Modified property: protocol
                                      - Property 'OneOf' changed
                                        - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                                      - Type changed from '' to 'string'
                                      - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                                      - MaxLength changed from null to 40
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: direction
                                - Property 'AllOf' changed
                                  - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                                  - Schemas deleted: #/components/schemas/DirectionEnum
                              - Modified property: protocol
                                - Property 'OneOf' changed
                                  - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                                - Type changed from '' to 'string'
                                - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                                - MaxLength changed from null to 40

POST /api/openstack-backups/{uuid}/restore/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: config_drive
            - Modified property: action_details
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: direction
                                - Property 'AllOf' changed
                                  - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                                  - Schemas deleted: #/components/schemas/DirectionEnum
                              - Modified property: protocol
                                - Property 'OneOf' changed
                                  - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                                - Type changed from '' to 'string'
                                - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                                - MaxLength changed from null to 40
            - Modified property: security_groups
              - Items changed
                - Properties changed
                  - Modified property: rules
                    - Items changed
                      - Properties changed
                        - Modified property: direction
                          - Property 'AllOf' changed
                            - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                            - Schemas deleted: #/components/schemas/DirectionEnum
                        - Modified property: protocol
                          - Property 'OneOf' changed
                            - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                          - Type changed from '' to 'string'
                          - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                          - MaxLength changed from null to 40

GET /api/openstack-external-networks/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: subnets
                - Items changed
                  - Properties changed
                    - Modified property: allocation_pools
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: dns_nameservers
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true

GET /api/openstack-external-networks/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: subnets
              - Items changed
                - Properties changed
                  - Modified property: allocation_pools
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: dns_nameservers
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true

GET /api/openstack-flavors/usage_stats/

- Deleted query param: field
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: backend_id
            - Deleted property: cores
            - Deleted property: disk
            - Deleted property: display_name
            - Deleted property: name
            - Deleted property: ram
            - Deleted property: settings
            - Deleted property: url
            - Deleted property: uuid
          - AdditionalProperties changed
            - Schema added

POST /api/openstack-floating-ips/{uuid}/attach_to_port/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/openstack-floating-ips/{uuid}/detach_from_port/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/openstack-floating-ips/{uuid}/update_description/

- Responses changed
  - New response: 202
  - Deleted response: 200

GET /api/openstack-hypervisors/

- New query param: trait
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: traits
            - Properties changed
              - New property: traits

HEAD /api/openstack-hypervisors/

- New query param: trait

GET /api/openstack-hypervisors/allocation_candidates/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: provider_summaries
              - AdditionalProperties changed
                - Required changed
                  - New required property: resources
                  - New required property: traits
                - Properties changed
                  - New property: resources
                  - New property: traits
                - AdditionalProperties changed
                  - Schema deleted

GET /api/openstack-hypervisors/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: traits
          - Properties changed
            - New property: traits

GET /api/openstack-images/usage_stats/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: created_instances_count
            - New required property: running_instances_count
            - Deleted required property: backend_id
            - Deleted required property: is_rescue_image
            - Deleted required property: settings
            - Deleted required property: url
            - Deleted required property: uuid
          - Properties changed
            - New property: created_instances_count
            - New property: running_instances_count
            - Deleted property: backend_created_at
            - Deleted property: backend_id
            - Deleted property: hw_rescue_bus
            - Deleted property: hw_rescue_device
            - Deleted property: is_rescue_image
            - Deleted property: min_disk
            - Deleted property: min_ram
            - Deleted property: settings
            - Deleted property: url
            - Deleted property: uuid
            - Modified property: name
              - ReadOnly changed from false to true
              - MaxLength changed from 150 to null

GET /api/openstack-instances/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [config_drive]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: config_drive
              - Modified property: action_details
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: ports
                - Items changed
                  - Properties changed
                    - Modified property: security_groups
                      - Items changed
                        - Properties changed
                          - Modified property: rules
                            - Items changed
                              - Properties changed
                                - Modified property: direction
                                  - Property 'AllOf' changed
                                    - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                                    - Schemas deleted: #/components/schemas/DirectionEnum
                                - Modified property: protocol
                                  - Property 'OneOf' changed
                                    - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                                  - Type changed from '' to 'string'
                                  - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                                  - MaxLength changed from null to 40
              - Modified property: security_groups
                - Items changed
                  - Properties changed
                    - Modified property: rules
                      - Items changed
                        - Properties changed
                          - Modified property: direction
                            - Property 'AllOf' changed
                              - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                              - Schemas deleted: #/components/schemas/DirectionEnum
                          - Modified property: protocol
                            - Property 'OneOf' changed
                              - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                            - Type changed from '' to 'string'
                            - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                            - MaxLength changed from null to 40

GET /api/openstack-instances/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [config_drive]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: config_drive
            - Modified property: action_details
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: direction
                                - Property 'AllOf' changed
                                  - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                                  - Schemas deleted: #/components/schemas/DirectionEnum
                              - Modified property: protocol
                                - Property 'OneOf' changed
                                  - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                                - Type changed from '' to 'string'
                                - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                                - MaxLength changed from null to 40
            - Modified property: security_groups
              - Items changed
                - Properties changed
                  - Modified property: rules
                    - Items changed
                      - Properties changed
                        - Modified property: direction
                          - Property 'AllOf' changed
                            - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                            - Schemas deleted: #/components/schemas/DirectionEnum
                        - Modified property: protocol
                          - Property 'OneOf' changed
                            - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                          - Type changed from '' to 'string'
                          - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                          - MaxLength changed from null to 40

PATCH /api/openstack-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: config_drive
            - Modified property: action_details
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: direction
                                - Property 'AllOf' changed
                                  - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                                  - Schemas deleted: #/components/schemas/DirectionEnum
                              - Modified property: protocol
                                - Property 'OneOf' changed
                                  - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                                - Type changed from '' to 'string'
                                - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                                - MaxLength changed from null to 40
            - Modified property: security_groups
              - Items changed
                - Properties changed
                  - Modified property: rules
                    - Items changed
                      - Properties changed
                        - Modified property: direction
                          - Property 'AllOf' changed
                            - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                            - Schemas deleted: #/components/schemas/DirectionEnum
                        - Modified property: protocol
                          - Property 'OneOf' changed
                            - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                          - Type changed from '' to 'string'
                          - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                          - MaxLength changed from null to 40

PUT /api/openstack-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: config_drive
            - Modified property: action_details
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: direction
                                - Property 'AllOf' changed
                                  - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                                  - Schemas deleted: #/components/schemas/DirectionEnum
                              - Modified property: protocol
                                - Property 'OneOf' changed
                                  - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                                - Type changed from '' to 'string'
                                - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                                - MaxLength changed from null to 40
            - Modified property: security_groups
              - Items changed
                - Properties changed
                  - Modified property: rules
                    - Items changed
                      - Properties changed
                        - Modified property: direction
                          - Property 'AllOf' changed
                            - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                            - Schemas deleted: #/components/schemas/DirectionEnum
                        - Modified property: protocol
                          - Property 'OneOf' changed
                            - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                          - Type changed from '' to 'string'
                          - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                          - MaxLength changed from null to 40

POST /api/openstack-instances/{uuid}/backup/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: direction
                                - Property 'AllOf' changed
                                  - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                                  - Schemas deleted: #/components/schemas/DirectionEnum
                              - Modified property: protocol
                                - Property 'OneOf' changed
                                  - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                                - Type changed from '' to 'string'
                                - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                                - MaxLength changed from null to 40
            - Modified property: instance_security_groups
              - Items changed
                - Properties changed
                  - Modified property: rules
                    - Items changed
                      - Properties changed
                        - Modified property: direction
                          - Property 'AllOf' changed
                            - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                            - Schemas deleted: #/components/schemas/DirectionEnum
                        - Modified property: protocol
                          - Property 'OneOf' changed
                            - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                          - Type changed from '' to 'string'
                          - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                          - MaxLength changed from null to 40
            - Modified property: metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: security_groups
                          - Items changed
                            - Properties changed
                              - Modified property: rules
                                - Items changed
                                  - Properties changed
                                    - Modified property: direction
                                      - Property 'AllOf' changed
                                        - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                                        - Schemas deleted: #/components/schemas/DirectionEnum
                                    - Modified property: protocol
                                      - Property 'OneOf' changed
                                        - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                                      - Type changed from '' to 'string'
                                      - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                                      - MaxLength changed from null to 40
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: direction
                                - Property 'AllOf' changed
                                  - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                                  - Schemas deleted: #/components/schemas/DirectionEnum
                              - Modified property: protocol
                                - Property 'OneOf' changed
                                  - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                                - Type changed from '' to 'string'
                                - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                                - MaxLength changed from null to 40

POST /api/openstack-instances/{uuid}/change_flavor/

- Responses changed
  - New response: 202
  - Deleted response: 200

GET /api/openstack-instances/{uuid}/ports/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: security_groups
                - Items changed
                  - Properties changed
                    - Modified property: rules
                      - Items changed
                        - Properties changed
                          - Modified property: direction
                            - Property 'AllOf' changed
                              - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                              - Schemas deleted: #/components/schemas/DirectionEnum
                          - Modified property: protocol
                            - Property 'OneOf' changed
                              - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                            - Type changed from '' to 'string'
                            - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                            - MaxLength changed from null to 40

POST /api/openstack-instances/{uuid}/rescue/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/openstack-instances/{uuid}/restart/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/openstack-instances/{uuid}/start/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/openstack-instances/{uuid}/stop/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/openstack-instances/{uuid}/unrescue/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/openstack-instances/{uuid}/update_allowed_address_pairs/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/openstack-instances/{uuid}/update_floating_ips/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/openstack-instances/{uuid}/update_ports/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/openstack-instances/{uuid}/update_security_groups/

- Responses changed
  - New response: 202
  - Deleted response: 200

GET /api/openstack-loadbalancers/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: vip_security_groups
                - Items changed
                  - Properties changed
                    - New property: name
                    - New property: url
                    - New property: uuid
                  - AdditionalProperties changed
                    - Schema deleted

GET /api/openstack-loadbalancers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: vip_security_groups
              - Items changed
                - Properties changed
                  - New property: name
                  - New property: url
                  - New property: uuid
                - AdditionalProperties changed
                  - Schema deleted

POST /api/openstack-loadbalancers/{uuid}/attach_floating_ip/

- Responses changed
  - Modified response: 202
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: status
              - Description changed from 'Message that execution of the operation was scheduled.' to ''

POST /api/openstack-loadbalancers/{uuid}/detach_floating_ip/

- Responses changed
  - Modified response: 202
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: status
              - Description changed from 'Message that execution of the operation was scheduled.' to ''

POST /api/openstack-loadbalancers/{uuid}/set_security_groups/

- Responses changed
  - Modified response: 202
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: status
              - Description changed from 'Message that execution of the operation was scheduled.' to ''

GET /api/openstack-network-rbac-policies/

- New query param: direction
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: direction
              - New property: source_tenant_name
              - New property: source_tenant_uuid
              - New property: target_label

HEAD /api/openstack-network-rbac-policies/

- New query param: direction

POST /api/openstack-network-rbac-policies/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: direction
            - New property: source_tenant_name
            - New property: source_tenant_uuid
            - New property: target_label

GET /api/openstack-network-rbac-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: direction
            - New property: source_tenant_name
            - New property: source_tenant_uuid
            - New property: target_label

PATCH /api/openstack-network-rbac-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: direction
            - New property: source_tenant_name
            - New property: source_tenant_uuid
            - New property: target_label

PUT /api/openstack-network-rbac-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: direction
            - New property: source_tenant_name
            - New property: source_tenant_uuid
            - New property: target_label

GET /api/openstack-networks/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [port_security_enabled]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: port_security_enabled
              - Modified property: rbac_policies
                - Items changed
                  - Properties changed
                    - New property: direction
                    - New property: source_tenant_name
                    - New property: source_tenant_uuid
                    - New property: target_label
              - Modified property: subnets
                - Items changed
                  - Properties changed
                    - New property: port_security_enabled

GET /api/openstack-networks/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [port_security_enabled]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: port_security_enabled
            - Modified property: rbac_policies
              - Items changed
                - Properties changed
                  - New property: direction
                  - New property: source_tenant_name
                  - New property: source_tenant_uuid
                  - New property: target_label
            - Modified property: subnets
              - Items changed
                - Properties changed
                  - New property: port_security_enabled

PATCH /api/openstack-networks/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: port_security_enabled
            - Modified property: rbac_policies
              - Items changed
                - Properties changed
                  - New property: direction
                  - New property: source_tenant_name
                  - New property: source_tenant_uuid
                  - New property: target_label
            - Modified property: subnets
              - Items changed
                - Properties changed
                  - New property: port_security_enabled

PUT /api/openstack-networks/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: port_security_enabled
            - Modified property: rbac_policies
              - Items changed
                - Properties changed
                  - New property: direction
                  - New property: source_tenant_name
                  - New property: source_tenant_uuid
                  - New property: target_label
            - Modified property: subnets
              - Items changed
                - Properties changed
                  - New property: port_security_enabled

POST /api/openstack-networks/{uuid}/create_subnet/

- Responses changed
  - New response: 201
  - Deleted response: 200

POST /api/openstack-networks/{uuid}/rbac_policy_create/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: direction
            - New required property: source_tenant_name
            - New required property: source_tenant_uuid
            - New required property: target_label
          - Properties changed
            - New property: direction
            - New property: source_tenant_name
            - New property: source_tenant_uuid
            - New property: target_label

POST /api/openstack-networks/{uuid}/set_mtu/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/openstack-ports/{uuid}/update_security_groups/

- Responses changed
  - New response: 202
  - Deleted response: 200

GET /api/openstack-routers/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: external_fixed_ips
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: ports
                - Items changed
                  - Properties changed
                    - Modified property: security_groups
                      - Items changed
                        - Properties changed
                          - Modified property: rules
                            - Items changed
                              - Properties changed
                                - Modified property: direction
                                  - Property 'AllOf' changed
                                    - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                                    - Schemas deleted: #/components/schemas/DirectionEnum
                                - Modified property: protocol
                                  - Property 'OneOf' changed
                                    - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                                  - Type changed from '' to 'string'
                                  - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                                  - MaxLength changed from null to 40

GET /api/openstack-routers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: external_fixed_ips
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: direction
                                - Property 'AllOf' changed
                                  - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                                  - Schemas deleted: #/components/schemas/DirectionEnum
                              - Modified property: protocol
                                - Property 'OneOf' changed
                                  - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                                - Type changed from '' to 'string'
                                - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                                - MaxLength changed from null to 40

POST /api/openstack-routers/{uuid}/add_router_interface/

- Responses changed
  - New response: 202
  - Deleted response: 200

GET /api/openstack-routers/{uuid}/available_external_networks/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: subnets
                - Items changed
                  - Required changed
                    - New required property: backend_id
                    - New required property: cidr
                    - New required property: name
                  - Properties changed
                    - New property: backend_id
                    - New property: cidr
                    - New property: name
                  - AdditionalProperties changed
                    - Schema deleted

POST /api/openstack-routers/{uuid}/remove_external_gateway/

- Responses changed
  - Modified response: 202
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/openstack-routers/{uuid}/remove_router_interface/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/openstack-routers/{uuid}/set_external_gateway/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: external_fixed_ips
            - Items changed
              - Required changed
                - New required property: ip_address
              - Properties changed
                - New property: ip_address
                - New property: subnet_id
              - AdditionalProperties changed
                - Schema deleted
- Responses changed
  - Modified response: 202
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/openstack-routers/{uuid}/set_routes/

- Responses changed
  - New response: 202
  - Deleted response: 200

GET /api/openstack-security-groups/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: rules
                - Items changed
                  - Properties changed
                    - Modified property: direction
                      - Property 'AllOf' changed
                        - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                        - Schemas deleted: #/components/schemas/DirectionEnum
                    - Modified property: protocol
                      - Property 'OneOf' changed
                        - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                      - Type changed from '' to 'string'
                      - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                      - MaxLength changed from null to 40

GET /api/openstack-security-groups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: rules
              - Items changed
                - Properties changed
                  - Modified property: direction
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                      - Schemas deleted: #/components/schemas/DirectionEnum
                  - Modified property: protocol
                    - Property 'OneOf' changed
                      - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                    - Type changed from '' to 'string'
                    - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                    - MaxLength changed from null to 40

POST /api/openstack-security-groups/{uuid}/set_rules/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Items changed
          - Properties changed
            - Modified property: direction
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                - Schemas deleted: #/components/schemas/DirectionEnum
            - Modified property: protocol
              - Property 'OneOf' changed
                - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
              - Type changed from '' to 'string'
              - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
              - MaxLength changed from null to 40
- Responses changed
  - New response: 202
  - Deleted response: 200

GET /api/openstack-snapshots/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: action_details
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: metadata
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

GET /api/openstack-snapshots/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: action_details
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PATCH /api/openstack-snapshots/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: metadata
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: action_details
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PUT /api/openstack-snapshots/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: metadata
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: action_details
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

POST /api/openstack-snapshots/{uuid}/restore/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: action_details
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/openstack-subnets/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [port_security_enabled]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: port_security_enabled

GET /api/openstack-subnets/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [port_security_enabled]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: port_security_enabled

PATCH /api/openstack-subnets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: port_security_enabled

PUT /api/openstack-subnets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: port_security_enabled

POST /api/openstack-subnets/{uuid}/connect/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/openstack-subnets/{uuid}/disconnect/

- Responses changed
  - New response: 202
  - Deleted response: 200

PATCH /api/openstack-tenants/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: security_groups
            - Items changed
              - Properties changed
                - Modified property: rules
                  - Items changed
                    - Properties changed
                      - Modified property: direction
                        - Property 'AllOf' changed
                          - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                          - Schemas deleted: #/components/schemas/DirectionEnum
                      - Modified property: protocol
                        - Property 'OneOf' changed
                          - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                        - Type changed from '' to 'string'
                        - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                        - MaxLength changed from null to 40

PUT /api/openstack-tenants/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: security_groups
            - Items changed
              - Properties changed
                - Modified property: rules
                  - Items changed
                    - Properties changed
                      - Modified property: direction
                        - Property 'AllOf' changed
                          - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                          - Schemas deleted: #/components/schemas/DirectionEnum
                      - Modified property: protocol
                        - Property 'OneOf' changed
                          - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                        - Type changed from '' to 'string'
                        - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                        - MaxLength changed from null to 40

POST /api/openstack-tenants/{uuid}/change_password/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/openstack-tenants/{uuid}/create_network/

- Responses changed
  - New response: 201
  - Deleted response: 200

POST /api/openstack-tenants/{uuid}/create_security_group/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: rules
            - Items changed
              - Properties changed
                - Modified property: direction
                  - Property 'AllOf' changed
                    - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                    - Schemas deleted: #/components/schemas/DirectionEnum
                - Modified property: protocol
                  - Property 'OneOf' changed
                    - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                  - Type changed from '' to 'string'
                  - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                  - MaxLength changed from null to 40
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: rules
              - Items changed
                - Properties changed
                  - Modified property: direction
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                      - Schemas deleted: #/components/schemas/DirectionEnum
                  - Modified property: protocol
                    - Property 'OneOf' changed
                      - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                    - Type changed from '' to 'string'
                    - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                    - MaxLength changed from null to 40

POST /api/openstack-tenants/{uuid}/create_server_group/

- Responses changed
  - New response: 201
  - Deleted response: 200

POST /api/openstack-tenants/{uuid}/pull_quotas/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/openstack-tenants/{uuid}/pull_security_groups/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/openstack-tenants/{uuid}/pull_server_groups/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/openstack-tenants/{uuid}/push_security_groups/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Items changed
          - Properties changed
            - Modified property: rules
              - Items changed
                - Properties changed
                  - Modified property: direction
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                      - Schemas deleted: #/components/schemas/DirectionEnum
                  - Modified property: protocol
                    - Property 'OneOf' changed
                      - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                    - Type changed from '' to 'string'
                    - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                    - MaxLength changed from null to 40
- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/openstack-tenants/{uuid}/set_quotas/

- Description changed from 'A quota can be set for a particular tenant. Only staff users and service provider owners/managers can do that.
In order to set quota submit POST request to /api/openstack-tenants/<uuid>/set_quotas/.
The quota values are propagated to the backend.

The following quotas are supported. All values are expected to be integers:

- instances - maximal number of created instances.
- ram - maximal size of ram for allocation. In MiB_.
- storage - maximal size of storage for allocation. In MiB_.
- vcpu - maximal number of virtual cores for allocation.
- security_group_count - maximal number of created security groups.
- security_group_rule_count - maximal number of created security groups rules.
- volumes - maximal number of created volumes.
- snapshots - maximal number of created snapshots.

It is possible to update quotas by one or by submitting all the fields in one request.
Waldur will attempt to update the provided quotas. Please note, that if provided quotas are
conflicting with the backend (e.g. requested number of instances is below of the already existing ones),
some quotas might not be applied.

.. _MiB: <http://en.wikipedia.org/wiki/Mebibyte>

Response code of a successful request is **202 ACCEPTED**.
In case tenant is in a non-stable status, the response would be **409 CONFLICT**.
In this case REST client is advised to repeat the request after some time.
On successful completion the task will synchronize quotas with the backend.
' to 'A quota can be set for a particular tenant. Only staff users and service provider owners/managers can do that.
In order to set quota submit POST request to /api/openstack-tenants/<uuid>/set_quotas/.
The quota values are propagated to the backend.

The following quotas are supported. All values are expected to be integers:

- instances - maximal number of created instances.
- ram - maximal size of ram for allocation. In MiB_.
- storage - maximal size of storage for allocation. In MiB_.
- vcpu - maximal number of virtual cores for allocation.
- security_group_count - maximal number of created security groups.
- security_group_rule_count - maximal number of created security groups rules.
- volumes - maximal number of created volumes.
- snapshots - maximal number of created snapshots.
- floating_ip_count - maximal number of floating IPs. Use 0 to deny, -1 for unlimited.
- network_count - maximal number of networks. Use 0 to deny, -1 for unlimited.
- subnet_count - maximal number of subnets. Use 0 to deny, -1 for unlimited.
- port_count - maximal number of ports. Use 0 to deny, -1 for unlimited.
- gigabytes_<volume_type_name> - maximal storage for a specific Cinder volume type, in GB.
  For example, gigabytes_ssd or gigabytes___DEFAULT__. Use -1 for unlimited.

It is possible to update quotas by one or by submitting all the fields in one request.
Waldur will attempt to update the provided quotas. Please note, that if provided quotas are
conflicting with the backend (e.g. requested number of instances is below of the already existing ones),
some quotas might not be applied.

.. _MiB: <http://en.wikipedia.org/wiki/Mebibyte>

Response code of a successful request is **202 ACCEPTED**.
In case tenant is in a non-stable status, the response would be **409 CONFLICT**.
In this case REST client is advised to repeat the request after some time.
On successful completion the task will synchronize quotas with the backend.
'

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: floating_ip_count
          - New property: network_count
          - New property: port_count
          - New property: subnet_count
          - Modified property: ram
            - Description changed from '' to 'In MiB'
          - Modified property: storage
            - Description changed from '' to 'In MiB'
        - AdditionalProperties changed
          - Schema added
      - Examples changed
        - Modified example: Openstack-tenant-set-quotas
          - Value changed from map[instances:30 ram:100000 security_group_count:100 security_group_rule_count:100 snapshots:20 storage:1e+06 vcpu:30 volumes:10] to map[floating_ip_count:50 gigabytes___DEFAULT__:1000 gigabytes_ssd:500 instances:30 network_count:10 port_count:100 ram:100000 security_group_count:100 security_group_rule_count:100 snapshots:20 storage:1e+06 subnet_count:20 vcpu:30 volumes:10]
- Responses changed
  - New response: 202
  - Deleted response: 200

GET /api/openstack-volumes/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: action_details
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: metadata
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

GET /api/openstack-volumes/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: action_details
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PATCH /api/openstack-volumes/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: action_details
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PUT /api/openstack-volumes/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: action_details
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

POST /api/openstack-volumes/{uuid}/attach/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/openstack-volumes/{uuid}/detach/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/openstack-volumes/{uuid}/extend/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/openstack-volumes/{uuid}/retype/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/openstack-volumes/{uuid}/snapshot/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: metadata
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: action_details
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/override-settings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: AFFILIATION_REQUIRED_AT_PROJECT_CREATION
            - New property: ENABLE_MARKDOWN_IMAGE_UPLOAD
            - New property: JIRA_WEBHOOK_SHARED_SECRET
            - New property: MAINTENANCE_ANNOUNCEMENT_TRAILING_BUFFER_MINUTES
            - New property: MARKDOWN_IMAGE_MAX_SIZE_MB
            - New property: MATRIX_APPSERVICE_AS_TOKEN
            - New property: MATRIX_APPSERVICE_HS_TOKEN
            - New property: MATRIX_APPSERVICE_SENDER_LOCALPART
            - New property: MATRIX_ENABLED
            - New property: MATRIX_EXPORT_MEDIA
            - New property: MATRIX_HISTORY_EXPORT_ENABLED
            - New property: MATRIX_HOMESERVER_DOMAIN
            - New property: MATRIX_HOMESERVER_PUBLIC_URL
            - New property: MATRIX_HOMESERVER_URL
            - New property: MATRIX_LIVEKIT_KEY
            - New property: MATRIX_LIVEKIT_SECRET
            - New property: MATRIX_LIVEKIT_URL
            - New property: MATRIX_LOGIN_METHOD
            - New property: MATRIX_OIDC_PROVIDER_URL
            - New property: MATRIX_USER_ID_FORMAT
            - New property: MATRIX_USER_REGISTRATION_SECRET
            - New property: ONLY_ONE_PROJECT_MANAGER
            - New property: OPENSTACK_LOG_CALLS_ENABLED
            - New property: OPENSTACK_LOG_CALLS_THRESHOLD_MS
            - New property: SCIM_INBOUND_ALLOWED_ATTRIBUTES
            - New property: SCIM_INBOUND_ENABLED
            - New property: SCIM_INBOUND_SOURCE_NAME
            - New property: SCIM_PULL_API_KEY
            - New property: SCIM_PULL_API_URL
            - New property: SCIM_PULL_SOURCE_NAME
            - New property: SITE_AGENT_LOG_MAX_ROWS_PER_IDENTITY
            - New property: SMAX_CERTIFICATE
            - New property: SMAX_WEBHOOK_SHARED_SECRET
            - New property: ZAMMAD_WEBHOOK_SHARED_SECRET

POST /api/override-settings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: AFFILIATION_REQUIRED_AT_PROJECT_CREATION
          - New property: ENABLE_MARKDOWN_IMAGE_UPLOAD
          - New property: JIRA_WEBHOOK_SHARED_SECRET
          - New property: MAINTENANCE_ANNOUNCEMENT_TRAILING_BUFFER_MINUTES
          - New property: MARKDOWN_IMAGE_MAX_SIZE_MB
          - New property: MATRIX_APPSERVICE_AS_TOKEN
          - New property: MATRIX_APPSERVICE_HS_TOKEN
          - New property: MATRIX_APPSERVICE_SENDER_LOCALPART
          - New property: MATRIX_ENABLED
          - New property: MATRIX_EXPORT_MEDIA
          - New property: MATRIX_HISTORY_EXPORT_ENABLED
          - New property: MATRIX_HOMESERVER_DOMAIN
          - New property: MATRIX_HOMESERVER_PUBLIC_URL
          - New property: MATRIX_HOMESERVER_URL
          - New property: MATRIX_LIVEKIT_KEY
          - New property: MATRIX_LIVEKIT_SECRET
          - New property: MATRIX_LIVEKIT_URL
          - New property: MATRIX_LOGIN_METHOD
          - New property: MATRIX_OIDC_PROVIDER_URL
          - New property: MATRIX_USER_ID_FORMAT
          - New property: MATRIX_USER_REGISTRATION_SECRET
          - New property: ONLY_ONE_PROJECT_MANAGER
          - New property: OPENSTACK_LOG_CALLS_ENABLED
          - New property: OPENSTACK_LOG_CALLS_THRESHOLD_MS
          - New property: SCIM_INBOUND_ALLOWED_ATTRIBUTES
          - New property: SCIM_INBOUND_ENABLED
          - New property: SCIM_INBOUND_SOURCE_NAME
          - New property: SCIM_PULL_API_KEY
          - New property: SCIM_PULL_API_URL
          - New property: SCIM_PULL_SOURCE_NAME
          - New property: SITE_AGENT_LOG_MAX_ROWS_PER_IDENTITY
          - New property: SMAX_CERTIFICATE
          - New property: SMAX_WEBHOOK_SHARED_SECRET
          - New property: ZAMMAD_WEBHOOK_SHARED_SECRET
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: AFFILIATION_REQUIRED_AT_PROJECT_CREATION
          - New property: ENABLE_MARKDOWN_IMAGE_UPLOAD
          - New property: JIRA_WEBHOOK_SHARED_SECRET
          - New property: MAINTENANCE_ANNOUNCEMENT_TRAILING_BUFFER_MINUTES
          - New property: MARKDOWN_IMAGE_MAX_SIZE_MB
          - New property: MATRIX_APPSERVICE_AS_TOKEN
          - New property: MATRIX_APPSERVICE_HS_TOKEN
          - New property: MATRIX_APPSERVICE_SENDER_LOCALPART
          - New property: MATRIX_ENABLED
          - New property: MATRIX_EXPORT_MEDIA
          - New property: MATRIX_HISTORY_EXPORT_ENABLED
          - New property: MATRIX_HOMESERVER_DOMAIN
          - New property: MATRIX_HOMESERVER_PUBLIC_URL
          - New property: MATRIX_HOMESERVER_URL
          - New property: MATRIX_LIVEKIT_KEY
          - New property: MATRIX_LIVEKIT_SECRET
          - New property: MATRIX_LIVEKIT_URL
          - New property: MATRIX_LOGIN_METHOD
          - New property: MATRIX_OIDC_PROVIDER_URL
          - New property: MATRIX_USER_ID_FORMAT
          - New property: MATRIX_USER_REGISTRATION_SECRET
          - New property: ONLY_ONE_PROJECT_MANAGER
          - New property: OPENSTACK_LOG_CALLS_ENABLED
          - New property: OPENSTACK_LOG_CALLS_THRESHOLD_MS
          - New property: SCIM_INBOUND_ALLOWED_ATTRIBUTES
          - New property: SCIM_INBOUND_ENABLED
          - New property: SCIM_INBOUND_SOURCE_NAME
          - New property: SCIM_PULL_API_KEY
          - New property: SCIM_PULL_API_URL
          - New property: SCIM_PULL_SOURCE_NAME
          - New property: SITE_AGENT_LOG_MAX_ROWS_PER_IDENTITY
          - New property: SMAX_CERTIFICATE
          - New property: SMAX_WEBHOOK_SHARED_SECRET
          - New property: ZAMMAD_WEBHOOK_SHARED_SECRET
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: AFFILIATION_REQUIRED_AT_PROJECT_CREATION
          - New property: ENABLE_MARKDOWN_IMAGE_UPLOAD
          - New property: JIRA_WEBHOOK_SHARED_SECRET
          - New property: MAINTENANCE_ANNOUNCEMENT_TRAILING_BUFFER_MINUTES
          - New property: MARKDOWN_IMAGE_MAX_SIZE_MB
          - New property: MATRIX_APPSERVICE_AS_TOKEN
          - New property: MATRIX_APPSERVICE_HS_TOKEN
          - New property: MATRIX_APPSERVICE_SENDER_LOCALPART
          - New property: MATRIX_ENABLED
          - New property: MATRIX_EXPORT_MEDIA
          - New property: MATRIX_HISTORY_EXPORT_ENABLED
          - New property: MATRIX_HOMESERVER_DOMAIN
          - New property: MATRIX_HOMESERVER_PUBLIC_URL
          - New property: MATRIX_HOMESERVER_URL
          - New property: MATRIX_LIVEKIT_KEY
          - New property: MATRIX_LIVEKIT_SECRET
          - New property: MATRIX_LIVEKIT_URL
          - New property: MATRIX_LOGIN_METHOD
          - New property: MATRIX_OIDC_PROVIDER_URL
          - New property: MATRIX_USER_ID_FORMAT
          - New property: MATRIX_USER_REGISTRATION_SECRET
          - New property: ONLY_ONE_PROJECT_MANAGER
          - New property: OPENSTACK_LOG_CALLS_ENABLED
          - New property: OPENSTACK_LOG_CALLS_THRESHOLD_MS
          - New property: SCIM_INBOUND_ALLOWED_ATTRIBUTES
          - New property: SCIM_INBOUND_ENABLED
          - New property: SCIM_INBOUND_SOURCE_NAME
          - New property: SCIM_PULL_API_KEY
          - New property: SCIM_PULL_API_URL
          - New property: SCIM_PULL_SOURCE_NAME
          - New property: SITE_AGENT_LOG_MAX_ROWS_PER_IDENTITY
          - New property: SMAX_CERTIFICATE
          - New property: SMAX_WEBHOOK_SHARED_SECRET
          - New property: ZAMMAD_WEBHOOK_SHARED_SECRET

POST /api/payment-profiles/{uuid}/enable/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: status
          - Properties changed
            - New property: status
            - Deleted property: attributes
            - Deleted property: is_active
            - Deleted property: name
            - Deleted property: organization
            - Deleted property: organization_uuid
            - Deleted property: payment_type
            - Deleted property: payment_type_display
            - Deleted property: url
            - Deleted property: uuid

POST /api/payments/{uuid}/link_to_invoice/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: detail
            - Deleted required property: invoice
          - Properties changed
            - New property: detail
            - Deleted property: invoice

POST /api/payments/{uuid}/unlink_from_invoice/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: detail
            - Deleted required property: customer_uuid
            - Deleted required property: date_of_payment
            - Deleted required property: invoice
            - Deleted required property: invoice_period
            - Deleted required property: invoice_uuid
            - Deleted required property: profile
            - Deleted required property: url
            - Deleted required property: uuid
          - Properties changed
            - New property: detail
            - Deleted property: customer_uuid
            - Deleted property: date_of_payment
            - Deleted property: invoice
            - Deleted property: invoice_period
            - Deleted property: invoice_uuid
            - Deleted property: profile
            - Deleted property: proof
            - Deleted property: sum
            - Deleted property: url
            - Deleted property: uuid

GET /api/personal-access-tokens/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: allowed_scopes
            - Properties changed
              - New property: allowed_scopes

POST /api/personal-access-tokens/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: allowed_scopes
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: allowed_scopes
          - Properties changed
            - New property: allowed_scopes

GET /api/personal-access-tokens/available_scopes/

- Description changed from 'Return permissions the current user can delegate to a PAT.' to 'Return permissions the current user can delegate to a PAT.

Staff users can delegate any permission (they bypass UserRole checks).
For other users only the permissions granted by their active roles are
offered, plus SUPPORT.ACCESS for support users — mirroring what the
create serializer would accept.'

GET /api/personal-access-tokens/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: allowed_scopes
          - Properties changed
            - New property: allowed_scopes

POST /api/personal-access-tokens/{uuid}/rotate/

- Description changed from 'Atomically revoke the old token and create a new one with the same scopes.' to 'Atomically revoke the old token and create a new one with the same scopes and bindings.'
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: allowed_scopes
          - Properties changed
            - New property: allowed_scopes

GET /api/projects/

- New query param: affiliation_name
- New query param: affiliation_uuid
- New query param: has_affiliation
- Deleted query param: affiliated_organization_name
- Deleted query param: affiliated_organization_uuid
- Deleted query param: has_affiliated_organization
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [affiliation affiliation_code affiliation_name affiliation_uuid project_metadata]
      - Deleted enum values: [affiliated_organizations]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: affiliation
              - New property: affiliation_code
              - New property: affiliation_name
              - New property: affiliation_uuid
              - New property: project_metadata
              - Deleted property: affiliated_organizations
              - Modified property: kind
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/ProjectKindEnum
                  - Schemas deleted: #/components/schemas/KindEnum
              - Modified property: termination_metadata
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: user_affiliations
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: user_email_patterns
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: user_identity_sources
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

HEAD /api/projects/

- New query param: affiliation_name
- New query param: affiliation_uuid
- New query param: has_affiliation
- Deleted query param: affiliated_organization_name
- Deleted query param: affiliated_organization_uuid
- Deleted query param: has_affiliated_organization

POST /api/projects/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: affiliation_uuid
          - Modified property: kind
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/ProjectKindEnum
              - Schemas deleted: #/components/schemas/KindEnum
          - Modified property: user_affiliations
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_email_patterns
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_identity_sources
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: affiliation_uuid
          - Modified property: kind
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/ProjectKindEnum
              - Schemas deleted: #/components/schemas/KindEnum
          - Modified property: user_affiliations
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_email_patterns
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_identity_sources
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: affiliation_uuid
          - Modified property: kind
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/ProjectKindEnum
              - Schemas deleted: #/components/schemas/KindEnum
          - Modified property: user_affiliations
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_email_patterns
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_identity_sources
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: affiliation
            - New property: affiliation_code
            - New property: affiliation_name
            - New property: affiliation_uuid
            - New property: project_metadata
            - Deleted property: affiliated_organizations
            - Modified property: kind
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/ProjectKindEnum
                - Schemas deleted: #/components/schemas/KindEnum
            - Modified property: termination_metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_affiliations
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_email_patterns
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_identity_sources
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/projects/checklist-template/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: checklist
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/ChecklistShort
              - Type changed from 'object' to ''
              - AdditionalProperties changed
                - Schema deleted
            - Modified property: initial_visible_questions
              - Items changed
                - Properties changed
                  - New property: likert_allow_na
                  - New property: likert_high_label
                  - New property: likert_low_label
                  - New property: likert_scale_length
                  - New property: rich_text_char_limit
                  - New property: rich_text_toolbar_level
                  - Modified property: allowed_file_types
                    - Type changed from '' to 'array'
                    - Description changed from 'List of allowed file extensions (e.g., ['.pdf', '.doc', '.docx']). If empty, all file types are allowed.' to ''
                    - Items changed
                      - Schema added
                  - Modified property: allowed_mime_types
                    - Type changed from '' to 'array'
                    - Description changed from 'List of allowed MIME types (e.g., ['application/pdf', 'application/msword']). If empty, MIME type validation is not enforced. When both extensions and MIME types are specified, files must match both criteria for security.' to ''
                    - Items changed
                      - Schema added
                  - Modified property: guidance_answer_value
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: question_type
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/QuestionTypeEnum
                        - New enum values: [likert rich_text]
                  - Modified property: review_answer_value
                    - Description changed from 'Answer value that trigger review.' to ''
                    - Nullable changed from true to false
            - Modified property: questions
              - Items changed
                - Properties changed
                  - New property: likert_allow_na
                  - New property: likert_high_label
                  - New property: likert_low_label
                  - New property: likert_scale_length
                  - New property: rich_text_char_limit
                  - New property: rich_text_toolbar_level
                  - Modified property: allowed_file_types
                    - Type changed from '' to 'array'
                    - Description changed from 'List of allowed file extensions (e.g., ['.pdf', '.doc', '.docx']). If empty, all file types are allowed.' to ''
                    - Items changed
                      - Schema added
                  - Modified property: allowed_mime_types
                    - Type changed from '' to 'array'
                    - Description changed from 'List of allowed MIME types (e.g., ['application/pdf', 'application/msword']). If empty, MIME type validation is not enforced. When both extensions and MIME types are specified, files must match both criteria for security.' to ''
                    - Items changed
                      - Schema added
                  - Modified property: guidance_answer_value
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: question_type
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/QuestionTypeEnum
                        - New enum values: [likert rich_text]
                  - Modified property: review_answer_value
                    - Description changed from 'Answer value that trigger review.' to ''
                    - Nullable changed from true to false

GET /api/projects/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [affiliation affiliation_code affiliation_name affiliation_uuid project_metadata]
      - Deleted enum values: [affiliated_organizations]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: affiliation
            - New property: affiliation_code
            - New property: affiliation_name
            - New property: affiliation_uuid
            - New property: project_metadata
            - Deleted property: affiliated_organizations
            - Modified property: kind
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/ProjectKindEnum
                - Schemas deleted: #/components/schemas/KindEnum
            - Modified property: termination_metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_affiliations
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_email_patterns
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_identity_sources
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PATCH /api/projects/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: affiliation_uuid
          - Modified property: kind
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/ProjectKindEnum
              - Schemas deleted: #/components/schemas/KindEnum
          - Modified property: user_affiliations
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_email_patterns
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_identity_sources
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: affiliation_uuid
          - Modified property: kind
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/ProjectKindEnum
              - Schemas deleted: #/components/schemas/KindEnum
          - Modified property: user_affiliations
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_email_patterns
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_identity_sources
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: affiliation_uuid
          - Modified property: kind
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/ProjectKindEnum
              - Schemas deleted: #/components/schemas/KindEnum
          - Modified property: user_affiliations
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_email_patterns
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_identity_sources
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: affiliation
            - New property: affiliation_code
            - New property: affiliation_name
            - New property: affiliation_uuid
            - New property: project_metadata
            - Deleted property: affiliated_organizations
            - Modified property: kind
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/ProjectKindEnum
                - Schemas deleted: #/components/schemas/KindEnum
            - Modified property: termination_metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_affiliations
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_email_patterns
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_identity_sources
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PUT /api/projects/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: affiliation_uuid
          - Modified property: kind
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/ProjectKindEnum
              - Schemas deleted: #/components/schemas/KindEnum
          - Modified property: user_affiliations
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_email_patterns
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_identity_sources
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: affiliation_uuid
          - Modified property: kind
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/ProjectKindEnum
              - Schemas deleted: #/components/schemas/KindEnum
          - Modified property: user_affiliations
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_email_patterns
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_identity_sources
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: affiliation_uuid
          - Modified property: kind
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/ProjectKindEnum
              - Schemas deleted: #/components/schemas/KindEnum
          - Modified property: user_affiliations
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_email_patterns
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_identity_sources
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: affiliation
            - New property: affiliation_code
            - New property: affiliation_name
            - New property: affiliation_uuid
            - New property: project_metadata
            - Deleted property: affiliated_organizations
            - Modified property: kind
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/ProjectKindEnum
                - Schemas deleted: #/components/schemas/KindEnum
            - Modified property: termination_metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_affiliations
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_email_patterns
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_identity_sources
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/projects/{uuid}/checklist/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: checklist
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/ChecklistShort
              - Type changed from 'object' to ''
              - AdditionalProperties changed
                - Schema deleted
            - Modified property: questions
              - Items changed
                - Required changed
                  - New required property: likert_allow_na
                  - New required property: likert_high_label
                  - New required property: likert_low_label
                  - New required property: likert_scale_length
                  - New required property: rich_text_char_limit
                  - New required property: rich_text_toolbar_level
                - Properties changed
                  - New property: likert_allow_na
                  - New property: likert_high_label
                  - New property: likert_low_label
                  - New property: likert_scale_length
                  - New property: rich_text_char_limit
                  - New property: rich_text_toolbar_level
                  - Modified property: allowed_file_types
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: allowed_mime_types
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: dependencies_info
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/QuestionDependencyInfo
                    - Type changed from 'object' to ''
                    - AdditionalProperties changed
                      - Schema deleted
                  - Modified property: existing_answer
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/Answer
                    - Type changed from 'object' to ''
                    - AdditionalProperties changed
                      - Schema deleted
                  - Modified property: question_type
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/QuestionTypeEnum
                        - New enum values: [likert rich_text]

POST /api/projects/{uuid}/move_project/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: affiliation
            - New property: affiliation_code
            - New property: affiliation_name
            - New property: affiliation_uuid
            - New property: project_metadata
            - Deleted property: affiliated_organizations
            - Modified property: kind
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/ProjectKindEnum
                - Schemas deleted: #/components/schemas/KindEnum
            - Modified property: termination_metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_affiliations
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_email_patterns
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_identity_sources
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

POST /api/projects/{uuid}/recover/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: affiliation
            - New property: affiliation_code
            - New property: affiliation_name
            - New property: affiliation_uuid
            - New property: project_metadata
            - Deleted property: affiliated_organizations
            - Modified property: kind
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/ProjectKindEnum
                - Schemas deleted: #/components/schemas/KindEnum
            - Modified property: termination_metadata
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_affiliations
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_email_patterns
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_identity_sources
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/promotions-campaigns/{uuid}/orders/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [auto_approved auto_approved_by_rule_uuid auto_approved_cost_limit_snapshot]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: auto_approved
              - New property: auto_approved_by_rule_uuid
              - New property: auto_approved_cost_limit_snapshot
              - Modified property: attributes
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: offering_plugin_options
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

GET /api/promotions-campaigns/{uuid}/resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [end_date_updated_at]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: end_date_updated_at
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: auto_approved
                      - New property: auto_approved_by_rule_uuid
                      - New property: auto_approved_cost_limit_snapshot
                      - Modified property: attributes
                        - Type changed from '' to 'object'
                        - AdditionalProperties changed from null to true
                      - Modified property: offering_plugin_options
                        - Type changed from '' to 'object'
                        - AdditionalProperties changed from null to true
              - Modified property: offering_plugin_options
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: options
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: auto_approved
                      - New property: auto_approved_by_rule_uuid
                      - New property: auto_approved_cost_limit_snapshot
                      - Modified property: attributes
                        - Type changed from '' to 'object'
                        - AdditionalProperties changed from null to true
                      - Modified property: offering_plugin_options
                        - Type changed from '' to 'object'
                        - AdditionalProperties changed from null to true

GET /api/proposal-proposals/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: awaiting_manual_advance
            - Properties changed
              - New property: awaiting_manual_advance
              - Modified property: applicant_active_isds
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: applicant_affiliations
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: applicant_eduperson_assurance
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: applicant_nationalities
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: can_submit
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/ProposalCanSubmitResponse
                - Type changed from 'object' to ''
                - AdditionalProperties changed
                  - Schema deleted
              - Modified property: compliance_status
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/ProposalComplianceStatus
                - Type changed from 'object' to ''
                - AdditionalProperties changed
                  - Schema deleted

POST /api/proposal-proposals/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: awaiting_manual_advance
          - Properties changed
            - New property: awaiting_manual_advance
            - Modified property: applicant_active_isds
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: applicant_affiliations
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: applicant_eduperson_assurance
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: applicant_nationalities
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: can_submit
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/ProposalCanSubmitResponse
              - Type changed from 'object' to ''
              - AdditionalProperties changed
                - Schema deleted
            - Modified property: compliance_status
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/ProposalComplianceStatus
              - Type changed from 'object' to ''
              - AdditionalProperties changed
                - Schema deleted

GET /api/proposal-proposals/checklist-template/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: checklist
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/ChecklistShort
              - Type changed from 'object' to ''
              - AdditionalProperties changed
                - Schema deleted
            - Modified property: initial_visible_questions
              - Items changed
                - Properties changed
                  - New property: likert_allow_na
                  - New property: likert_high_label
                  - New property: likert_low_label
                  - New property: likert_scale_length
                  - New property: rich_text_char_limit
                  - New property: rich_text_toolbar_level
                  - Modified property: allowed_file_types
                    - Type changed from '' to 'array'
                    - Description changed from 'List of allowed file extensions (e.g., ['.pdf', '.doc', '.docx']). If empty, all file types are allowed.' to ''
                    - Items changed
                      - Schema added
                  - Modified property: allowed_mime_types
                    - Type changed from '' to 'array'
                    - Description changed from 'List of allowed MIME types (e.g., ['application/pdf', 'application/msword']). If empty, MIME type validation is not enforced. When both extensions and MIME types are specified, files must match both criteria for security.' to ''
                    - Items changed
                      - Schema added
                  - Modified property: guidance_answer_value
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: question_type
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/QuestionTypeEnum
                        - New enum values: [likert rich_text]
                  - Modified property: review_answer_value
                    - Description changed from 'Answer value that trigger review.' to ''
                    - Nullable changed from true to false
            - Modified property: questions
              - Items changed
                - Properties changed
                  - New property: likert_allow_na
                  - New property: likert_high_label
                  - New property: likert_low_label
                  - New property: likert_scale_length
                  - New property: rich_text_char_limit
                  - New property: rich_text_toolbar_level
                  - Modified property: allowed_file_types
                    - Type changed from '' to 'array'
                    - Description changed from 'List of allowed file extensions (e.g., ['.pdf', '.doc', '.docx']). If empty, all file types are allowed.' to ''
                    - Items changed
                      - Schema added
                  - Modified property: allowed_mime_types
                    - Type changed from '' to 'array'
                    - Description changed from 'List of allowed MIME types (e.g., ['application/pdf', 'application/msword']). If empty, MIME type validation is not enforced. When both extensions and MIME types are specified, files must match both criteria for security.' to ''
                    - Items changed
                      - Schema added
                  - Modified property: guidance_answer_value
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: question_type
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/QuestionTypeEnum
                        - New enum values: [likert rich_text]
                  - Modified property: review_answer_value
                    - Description changed from 'Answer value that trigger review.' to ''
                    - Nullable changed from true to false

GET /api/proposal-proposals/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: awaiting_manual_advance
          - Properties changed
            - New property: awaiting_manual_advance
            - Modified property: applicant_active_isds
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: applicant_affiliations
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: applicant_eduperson_assurance
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: applicant_nationalities
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: can_submit
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/ProposalCanSubmitResponse
              - Type changed from 'object' to ''
              - AdditionalProperties changed
                - Schema deleted
            - Modified property: compliance_status
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/ProposalComplianceStatus
              - Type changed from 'object' to ''
              - AdditionalProperties changed
                - Schema deleted

GET /api/proposal-proposals/{uuid}/checklist/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: checklist
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/ChecklistShort
              - Type changed from 'object' to ''
              - AdditionalProperties changed
                - Schema deleted
            - Modified property: questions
              - Items changed
                - Required changed
                  - New required property: likert_allow_na
                  - New required property: likert_high_label
                  - New required property: likert_low_label
                  - New required property: likert_scale_length
                  - New required property: rich_text_char_limit
                  - New required property: rich_text_toolbar_level
                - Properties changed
                  - New property: likert_allow_na
                  - New property: likert_high_label
                  - New property: likert_low_label
                  - New property: likert_scale_length
                  - New property: rich_text_char_limit
                  - New property: rich_text_toolbar_level
                  - Modified property: allowed_file_types
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: allowed_mime_types
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: dependencies_info
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/QuestionDependencyInfo
                    - Type changed from 'object' to ''
                    - AdditionalProperties changed
                      - Schema deleted
                  - Modified property: existing_answer
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/Answer
                    - Type changed from 'object' to ''
                    - AdditionalProperties changed
                      - Schema deleted
                  - Modified property: question_type
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/QuestionTypeEnum
                        - New enum values: [likert rich_text]

GET /api/proposal-proposals/{uuid}/checklist_review/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: checklist
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/ChecklistShort
              - Type changed from 'object' to ''
              - AdditionalProperties changed
                - Schema deleted
            - Modified property: questions
              - Items changed
                - Required changed
                  - New required property: likert_allow_na
                  - New required property: likert_high_label
                  - New required property: likert_low_label
                  - New required property: likert_scale_length
                  - New required property: rich_text_char_limit
                  - New required property: rich_text_toolbar_level
                - Properties changed
                  - New property: likert_allow_na
                  - New property: likert_high_label
                  - New property: likert_low_label
                  - New property: likert_scale_length
                  - New property: rich_text_char_limit
                  - New property: rich_text_toolbar_level
                  - Modified property: allowed_file_types
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: allowed_mime_types
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: dependencies_info
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/QuestionDependencyInfo
                    - Type changed from 'object' to ''
                    - AdditionalProperties changed
                      - Schema deleted
                  - Modified property: existing_answer
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/Answer
                    - Type changed from 'object' to ''
                    - AdditionalProperties changed
                      - Schema deleted
                  - Modified property: question_type
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/QuestionTypeEnum
                        - New enum values: [likert rich_text]
                  - Modified property: review_answer_value
                    - Description changed from 'Answer value that trigger review.' to ''
                    - Nullable changed from true to false

GET /api/proposal-proposals/{uuid}/resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: attributes
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: limits
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: requested_offering
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/NestedRequestedOffering
                    - Properties changed
                      - Modified property: attributes
                        - Type changed from '' to 'object'
                        - AdditionalProperties changed from null to true
                      - Modified property: options
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/OfferingOptions
                            - Properties changed
                              - Modified property: options
                                - AdditionalProperties changed
                                  - Properties changed
                                    - Modified property: cascade_config
                                      - Properties changed
                                        - Modified property: steps
                                          - Items changed
                                            - Properties changed
                                              - Modified property: choices
                                                - Type changed from '' to 'object'
                                                - AdditionalProperties changed from null to true
                                              - Modified property: choices_map
                                                - Type changed from '' to 'object'
                                                - AdditionalProperties changed from null to true

POST /api/proposal-proposals/{uuid}/resources/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: attributes
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: limits
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: attributes
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: limits
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - Modified property: attributes
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - Modified property: cascade_config
                                    - Properties changed
                                      - Modified property: steps
                                        - Items changed
                                          - Properties changed
                                            - Modified property: choices
                                              - Type changed from '' to 'object'
                                              - AdditionalProperties changed from null to true
                                            - Modified property: choices_map
                                              - Type changed from '' to 'object'
                                              - AdditionalProperties changed from null to true

DELETE /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Responses changed
  - New response: 200
  - Deleted response: 204

GET /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: attributes
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: limits
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - Modified property: attributes
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - Modified property: cascade_config
                                    - Properties changed
                                      - Modified property: steps
                                        - Items changed
                                          - Properties changed
                                            - Modified property: choices
                                              - Type changed from '' to 'object'
                                              - AdditionalProperties changed from null to true
                                            - Modified property: choices_map
                                              - Type changed from '' to 'object'
                                              - AdditionalProperties changed from null to true

PATCH /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: attributes
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: limits
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: attributes
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: limits
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - Modified property: attributes
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - Modified property: cascade_config
                                    - Properties changed
                                      - Modified property: steps
                                        - Items changed
                                          - Properties changed
                                            - Modified property: choices
                                              - Type changed from '' to 'object'
                                              - AdditionalProperties changed from null to true
                                            - Modified property: choices_map
                                              - Type changed from '' to 'object'
                                              - AdditionalProperties changed from null to true

PUT /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: attributes
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: limits
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: attributes
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: limits
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - Modified property: attributes
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - Modified property: cascade_config
                                    - Properties changed
                                      - Modified property: steps
                                        - Items changed
                                          - Properties changed
                                            - Modified property: choices
                                              - Type changed from '' to 'object'
                                              - AdditionalProperties changed from null to true
                                            - Modified property: choices_map
                                              - Type changed from '' to 'object'
                                              - AdditionalProperties changed from null to true

GET /api/proposal-protected-calls/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: offerings
                - Items changed
                  - Properties changed
                    - Modified property: attributes
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - Modified property: cascade_config
                                    - Properties changed
                                      - Modified property: steps
                                        - Items changed
                                          - Properties changed
                                            - Modified property: choices
                                              - Type changed from '' to 'object'
                                              - AdditionalProperties changed from null to true
                                            - Modified property: choices_map
                                              - Type changed from '' to 'object'
                                              - AdditionalProperties changed from null to true
              - Modified property: resource_templates
                - Items changed
                  - Properties changed
                    - Modified property: attributes
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: limits
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed
                        - Schema added
              - Modified property: user_affiliations
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: user_assurance_levels
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: user_email_patterns
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: user_identity_sources
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: user_nationalities
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: user_organization_types
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

POST /api/proposal-protected-calls/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: user_affiliations
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_assurance_levels
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_email_patterns
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_identity_sources
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_nationalities
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_organization_types
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: attributes
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - Modified property: cascade_config
                                  - Properties changed
                                    - Modified property: steps
                                      - Items changed
                                        - Properties changed
                                          - Modified property: choices
                                            - Type changed from '' to 'object'
                                            - AdditionalProperties changed from null to true
                                          - Modified property: choices_map
                                            - Type changed from '' to 'object'
                                            - AdditionalProperties changed from null to true
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: attributes
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: limits
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed
                      - Schema added
            - Modified property: user_affiliations
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_assurance_levels
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_email_patterns
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_identity_sources
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_nationalities
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_organization_types
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/proposal-protected-calls/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: attributes
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - Modified property: cascade_config
                                  - Properties changed
                                    - Modified property: steps
                                      - Items changed
                                        - Properties changed
                                          - Modified property: choices
                                            - Type changed from '' to 'object'
                                            - AdditionalProperties changed from null to true
                                          - Modified property: choices_map
                                            - Type changed from '' to 'object'
                                            - AdditionalProperties changed from null to true
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: attributes
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: limits
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed
                      - Schema added
            - Modified property: user_affiliations
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_assurance_levels
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_email_patterns
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_identity_sources
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_nationalities
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_organization_types
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PATCH /api/proposal-protected-calls/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: user_affiliations
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_assurance_levels
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_email_patterns
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_identity_sources
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_nationalities
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_organization_types
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: attributes
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - Modified property: cascade_config
                                  - Properties changed
                                    - Modified property: steps
                                      - Items changed
                                        - Properties changed
                                          - Modified property: choices
                                            - Type changed from '' to 'object'
                                            - AdditionalProperties changed from null to true
                                          - Modified property: choices_map
                                            - Type changed from '' to 'object'
                                            - AdditionalProperties changed from null to true
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: attributes
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: limits
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed
                      - Schema added
            - Modified property: user_affiliations
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_assurance_levels
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_email_patterns
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_identity_sources
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_nationalities
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_organization_types
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PUT /api/proposal-protected-calls/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: user_affiliations
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_assurance_levels
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_email_patterns
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_identity_sources
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_nationalities
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_organization_types
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: attributes
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - Modified property: cascade_config
                                  - Properties changed
                                    - Modified property: steps
                                      - Items changed
                                        - Properties changed
                                          - Modified property: choices
                                            - Type changed from '' to 'object'
                                            - AdditionalProperties changed from null to true
                                          - Modified property: choices_map
                                            - Type changed from '' to 'object'
                                            - AdditionalProperties changed from null to true
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: attributes
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: limits
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed
                      - Schema added
            - Modified property: user_affiliations
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_assurance_levels
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_email_patterns
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_identity_sources
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_nationalities
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: user_organization_types
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/proposal-protected-calls/{uuid}/affinity-matrix/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'manager' to '*'
    - Added /0/scopes/- with value: 'manager'

GET /api/proposal-protected-calls/{uuid}/coi-configuration/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'manager' to '*'
    - Added /0/scopes/- with value: 'manager'

PATCH /api/proposal-protected-calls/{uuid}/coi-configuration/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'manager' to '*'
    - Added /0/scopes/- with value: 'manager'

GET /api/proposal-protected-calls/{uuid}/compliance_overview/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: checklist
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/CallComplianceChecklistInfo
              - Type changed from 'object' to ''
              - AdditionalProperties changed
                - Schema deleted
            - Modified property: proposals
              - Items changed
                - Type changed from '' to 'object'
                - Required changed
                  - New required property: compliance
                  - New required property: created_by
                  - New required property: created_by_uuid
                  - New required property: name
                  - New required property: state
                  - New required property: uuid
                - Properties changed
                  - New property: compliance
                  - New property: created_by
                  - New property: created_by_uuid
                  - New property: name
                  - New property: state
                  - New property: uuid

POST /api/proposal-protected-calls/{uuid}/compute-affinities/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'manager' to '*'
    - Added /0/scopes/- with value: 'manager'

GET /api/proposal-protected-calls/{uuid}/conflict-summary/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'manager' to '*'
    - Added /0/scopes/- with value: 'manager'

GET /api/proposal-protected-calls/{uuid}/conflicts/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'manager' to '*'
    - Added /0/scopes/- with value: 'manager'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: evidence_data
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

POST /api/proposal-protected-calls/{uuid}/create-manual-assignment/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'manager' to '*'
    - Added /0/scopes/- with value: 'manager'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: skipped_proposals
              - Items changed
                - Required changed
                  - New required property: proposal_name
                  - New required property: proposal_uuid
                  - New required property: reason
                - Properties changed
                  - New property: proposal_name
                  - New property: proposal_uuid
                  - New property: reason
                - AdditionalProperties changed
                  - Schema deleted

POST /api/proposal-protected-calls/{uuid}/detect-conflicts/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'manager' to '*'
    - Added /0/scopes/- with value: 'manager'

POST /api/proposal-protected-calls/{uuid}/generate-assignments/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'manager' to '*'
    - Added /0/scopes/- with value: 'manager'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: skipped_proposals
              - Items changed
                - Required changed
                  - New required property: proposal_name
                  - New required property: proposal_uuid
                  - New required property: reason
                - Properties changed
                  - New property: proposal_name
                  - New property: proposal_uuid
                  - New property: reason
                - AdditionalProperties changed
                  - Schema deleted

POST /api/proposal-protected-calls/{uuid}/generate-suggestions/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'manager' to '*'
    - Added /0/scopes/- with value: 'manager'

POST /api/proposal-protected-calls/{uuid}/invite-by-email/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'manager' to '*'
    - Added /0/scopes/- with value: 'manager'

GET /api/proposal-protected-calls/{uuid}/matching-configuration/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'manager' to '*'
    - Added /0/scopes/- with value: 'manager'

PATCH /api/proposal-protected-calls/{uuid}/matching-configuration/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'manager' to '*'
    - Added /0/scopes/- with value: 'manager'

GET /api/proposal-protected-calls/{uuid}/offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: attributes
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - Modified property: cascade_config
                              - Properties changed
                                - Modified property: steps
                                  - Items changed
                                    - Properties changed
                                      - Modified property: choices
                                        - Type changed from '' to 'object'
                                        - AdditionalProperties changed from null to true
                                      - Modified property: choices_map
                                        - Type changed from '' to 'object'
                                        - AdditionalProperties changed from null to true

POST /api/proposal-protected-calls/{uuid}/offerings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: attributes
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: attributes
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - Modified property: cascade_config
                            - Properties changed
                              - Modified property: steps
                                - Items changed
                                  - Properties changed
                                    - Modified property: choices
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
                                    - Modified property: choices_map
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true

DELETE /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Responses changed
  - New response: 200
  - Deleted response: 204

GET /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: attributes
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - Modified property: cascade_config
                            - Properties changed
                              - Modified property: steps
                                - Items changed
                                  - Properties changed
                                    - Modified property: choices
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
                                    - Modified property: choices_map
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true

PATCH /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: attributes
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: attributes
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - Modified property: cascade_config
                            - Properties changed
                              - Modified property: steps
                                - Items changed
                                  - Properties changed
                                    - Modified property: choices
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
                                    - Modified property: choices_map
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true

PUT /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: attributes
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: attributes
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - Modified property: cascade_config
                            - Properties changed
                              - Modified property: steps
                                - Items changed
                                  - Properties changed
                                    - Modified property: choices
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
                                    - Modified property: choices_map
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true

GET /api/proposal-protected-calls/{uuid}/proposals/{proposal_uuid}/compliance-answers/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: answer_data
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

GET /api/proposal-protected-calls/{uuid}/proposed-assignments/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'manager' to '*'
    - Added /0/scopes/- with value: 'manager'

GET /api/proposal-protected-calls/{uuid}/resource_templates/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: attributes
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: limits
                - Type changed from '' to 'object'
                - AdditionalProperties changed
                  - Schema added

POST /api/proposal-protected-calls/{uuid}/resource_templates/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: attributes
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: limits
            - Type changed from '' to 'object'
            - AdditionalProperties changed
              - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: attributes
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: limits
              - Type changed from '' to 'object'
              - AdditionalProperties changed
                - Schema added

DELETE /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/

- Responses changed
  - New response: 200
  - Deleted response: 204

GET /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: attributes
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: limits
              - Type changed from '' to 'object'
              - AdditionalProperties changed
                - Schema added

PATCH /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: attributes
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: limits
            - Type changed from '' to 'object'
            - AdditionalProperties changed
              - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: attributes
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: limits
              - Type changed from '' to 'object'
              - AdditionalProperties changed
                - Schema added

PUT /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: attributes
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: limits
            - Type changed from '' to 'object'
            - AdditionalProperties changed
              - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: attributes
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: limits
              - Type changed from '' to 'object'
              - AdditionalProperties changed
                - Schema added

GET /api/proposal-protected-calls/{uuid}/reviewer-pool/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'manager' to '*'
    - Added /0/scopes/- with value: 'manager'

POST /api/proposal-protected-calls/{uuid}/reviewer-pool/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'manager' to '*'
    - Added /0/scopes/- with value: 'manager'

DELETE /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/

- Responses changed
  - New response: 200
  - Deleted response: 204

POST /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/close/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: user_affiliations
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_assurance_levels
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_email_patterns
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_identity_sources
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_nationalities
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: user_organization_types
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Type changed from 'object' to 'string'
          - Properties changed
            - Deleted property: applicant_visibility_config
            - Deleted property: backend_id
            - Deleted property: compliance_checklist
            - Deleted property: compliance_checklist_name
            - Deleted property: created
            - Deleted property: created_by
            - Deleted property: customer_name
            - Deleted property: customer_uuid
            - Deleted property: description
            - Deleted property: documents
            - Deleted property: end_date
            - Deleted property: external_url
            - Deleted property: fixed_duration_in_days
            - Deleted property: has_eligibility_restrictions
            - Deleted property: manager
            - Deleted property: manager_uuid
            - Deleted property: name
            - Deleted property: offerings
            - Deleted property: proposal_slug_template
            - Deleted property: reference_code
            - Deleted property: resource_templates
            - Deleted property: reviewer_identity_visible_to_submitters
            - Deleted property: reviews_visible_to_submitters
            - Deleted property: rounds
            - Deleted property: slug
            - Deleted property: start_date
            - Deleted property: state
            - Deleted property: url
            - Deleted property: user_affiliations
            - Deleted property: user_assurance_levels
            - Deleted property: user_email_patterns
            - Deleted property: user_identity_sources
            - Deleted property: user_nationalities
            - Deleted property: user_organization_types
            - Deleted property: uuid

POST /api/proposal-protected-calls/{uuid}/send-all-assignments/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'manager' to '*'
    - Added /0/scopes/- with value: 'manager'

POST /api/proposal-protected-calls/{uuid}/send-invitations/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'manager' to '*'
    - Added /0/scopes/- with value: 'manager'

GET /api/proposal-protected-calls/{uuid}/suggestions/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'manager' to '*'
    - Added /0/scopes/- with value: 'manager'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: matched_keywords
                - Type changed from '' to 'array'
                - Description changed from 'Keywords from reviewer's expertise that matched the source text' to ''
                - Items changed
                  - Schema added
              - Modified property: top_matching_proposals
                - Type changed from '' to 'array'
                - Description changed from 'Top proposals with highest affinity: [{uuid, name, slug, affinity}, ...]' to ''
                - Items changed
                  - Schema added

GET /api/proposal-public-calls/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: offerings
                - Items changed
                  - Properties changed
                    - Modified property: attributes
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - Modified property: cascade_config
                                    - Properties changed
                                      - Modified property: steps
                                        - Items changed
                                          - Properties changed
                                            - Modified property: choices
                                              - Type changed from '' to 'object'
                                              - AdditionalProperties changed from null to true
                                            - Modified property: choices_map
                                              - Type changed from '' to 'object'
                                              - AdditionalProperties changed from null to true
              - Modified property: resource_templates
                - Items changed
                  - Properties changed
                    - Modified property: attributes
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: limits
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed
                        - Schema added

GET /api/proposal-public-calls/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: attributes
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - Modified property: cascade_config
                                  - Properties changed
                                    - Modified property: steps
                                      - Items changed
                                        - Properties changed
                                          - Modified property: choices
                                            - Type changed from '' to 'object'
                                            - AdditionalProperties changed from null to true
                                          - Modified property: choices_map
                                            - Type changed from '' to 'object'
                                            - AdditionalProperties changed from null to true
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: attributes
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: limits
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed
                      - Schema added

GET /api/proposal-requested-offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: attributes
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - Modified property: cascade_config
                              - Properties changed
                                - Modified property: steps
                                  - Items changed
                                    - Properties changed
                                      - Modified property: choices
                                        - Type changed from '' to 'object'
                                        - AdditionalProperties changed from null to true
                                      - Modified property: choices_map
                                        - Type changed from '' to 'object'
                                        - AdditionalProperties changed from null to true

GET /api/proposal-requested-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: attributes
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - Modified property: cascade_config
                            - Properties changed
                              - Modified property: steps
                                - Items changed
                                  - Properties changed
                                    - Modified property: choices
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true
                                    - Modified property: choices_map
                                      - Type changed from '' to 'object'
                                      - AdditionalProperties changed from null to true

GET /api/proposal-requested-resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: attributes
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: limits
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: requested_offering
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/NestedRequestedOffering
                    - Properties changed
                      - Modified property: attributes
                        - Type changed from '' to 'object'
                        - AdditionalProperties changed from null to true
                      - Modified property: options
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/OfferingOptions
                            - Properties changed
                              - Modified property: options
                                - AdditionalProperties changed
                                  - Properties changed
                                    - Modified property: cascade_config
                                      - Properties changed
                                        - Modified property: steps
                                          - Items changed
                                            - Properties changed
                                              - Modified property: choices
                                                - Type changed from '' to 'object'
                                                - AdditionalProperties changed from null to true
                                              - Modified property: choices_map
                                                - Type changed from '' to 'object'
                                                - AdditionalProperties changed from null to true

GET /api/proposal-requested-resources/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: attributes
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: limits
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - Modified property: attributes
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - Modified property: cascade_config
                                    - Properties changed
                                      - Modified property: steps
                                        - Items changed
                                          - Properties changed
                                            - Modified property: choices
                                              - Type changed from '' to 'object'
                                              - AdditionalProperties changed from null to true
                                            - Modified property: choices_map
                                              - Type changed from '' to 'object'
                                              - AdditionalProperties changed from null to true

GET /api/proposal-reviews/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: reviewer_image
            - Properties changed
              - New property: reviewer_image

POST /api/proposal-reviews/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: reviewer_image
          - Properties changed
            - New property: reviewer_image

GET /api/proposal-reviews/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: reviewer_image
          - Properties changed
            - New property: reviewer_image

PATCH /api/proposal-reviews/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: reviewer_image
          - Properties changed
            - New property: reviewer_image

PUT /api/proposal-reviews/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: reviewer_image
          - Properties changed
            - New property: reviewer_image

POST /api/query/

- Description changed from 'Execute a given SQL query against a read-only database replica. This is a powerful tool for diagnostics and reporting, but should be used with caution. Requires support user permissions.' to 'Execute a given SQL query against a read-only database replica. This is a powerful tool for diagnostics and reporting, but should be used with caution. Requires staff user permissions.'

POST /api/rancher-catalogs/{uuid}/refresh/

- Responses changed
  - Modified response: 200
    - Description changed from '' to 'No response body'
    - Content changed
      - Deleted media type: application/json

GET /api/rancher-cluster-security-groups/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: rules
                - Items changed
                  - Properties changed
                    - Modified property: direction
                      - Property 'AllOf' changed
                        - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                        - Schemas deleted: #/components/schemas/DirectionEnum
                    - Modified property: protocol
                      - Property 'OneOf' changed
                        - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                      - Type changed from '' to 'string'
                      - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                      - MaxLength changed from null to 40

GET /api/rancher-cluster-security-groups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: rules
              - Items changed
                - Properties changed
                  - Modified property: direction
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                      - Schemas deleted: #/components/schemas/DirectionEnum
                  - Modified property: protocol
                    - Property 'OneOf' changed
                      - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                    - Type changed from '' to 'string'
                    - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                    - MaxLength changed from null to 40

PATCH /api/rancher-cluster-security-groups/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: rules
            - Items changed
              - Properties changed
                - Modified property: direction
                  - Property 'AllOf' changed
                    - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                    - Schemas deleted: #/components/schemas/DirectionEnum
                - Modified property: protocol
                  - Property 'OneOf' changed
                    - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                  - Type changed from '' to 'string'
                  - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                  - MaxLength changed from null to 40
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: rules
              - Items changed
                - Properties changed
                  - Modified property: direction
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                      - Schemas deleted: #/components/schemas/DirectionEnum
                  - Modified property: protocol
                    - Property 'OneOf' changed
                      - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                    - Type changed from '' to 'string'
                    - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                    - MaxLength changed from null to 40

PUT /api/rancher-cluster-security-groups/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: rules
            - Items changed
              - Properties changed
                - Modified property: direction
                  - Property 'AllOf' changed
                    - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                    - Schemas deleted: #/components/schemas/DirectionEnum
                - Modified property: protocol
                  - Property 'OneOf' changed
                    - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                  - Type changed from '' to 'string'
                  - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                  - MaxLength changed from null to 40
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: rules
              - Items changed
                - Properties changed
                  - Modified property: direction
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/SecurityGroupRuleDirectionEnum
                      - Schemas deleted: #/components/schemas/DirectionEnum
                  - Modified property: protocol
                    - Property 'OneOf' changed
                      - Schemas deleted: #/components/schemas/SecurityGroupRuleProtocolEnum, #/components/schemas/BlankEnum
                    - Type changed from '' to 'string'
                    - Description changed from 'The network protocol (TCP, UDP, ICMP, or empty for any protocol)' to 'Network protocol: 'tcp', 'udp', 'icmp', empty (any) or an IANA protocol number 0-255 (e.g. '112' for VRRP).'
                    - MaxLength changed from null to 40

GET /api/rancher-clusters/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: capacity
                - Type changed from '' to 'object'
                - Description changed from 'Cluster capacity in the format {'cpu': '10', 'ram': '49125240Ki', 'pods': '330'}' to ''
                - AdditionalProperties changed
                  - Schema added
              - Modified property: nodes
                - Items changed
                  - Properties changed
                    - Modified property: annotations
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: initial_data
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: labels
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
              - Modified property: requested
                - Type changed from '' to 'object'
                - Description changed from 'Cluster requested resources in the format {'cpu': '1450m', 'memory': '884Mi', 'pods': '13'}' to ''
                - AdditionalProperties changed
                  - Schema added

GET /api/rancher-clusters/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: capacity
              - Type changed from '' to 'object'
              - Description changed from 'Cluster capacity in the format {'cpu': '10', 'ram': '49125240Ki', 'pods': '330'}' to ''
              - AdditionalProperties changed
                - Schema added
            - Modified property: nodes
              - Items changed
                - Properties changed
                  - Modified property: annotations
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: initial_data
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: labels
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
            - Modified property: requested
              - Type changed from '' to 'object'
              - Description changed from 'Cluster requested resources in the format {'cpu': '1450m', 'memory': '884Mi', 'pods': '13'}' to ''
              - AdditionalProperties changed
                - Schema added

PATCH /api/rancher-clusters/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: capacity
              - Type changed from '' to 'object'
              - Description changed from 'Cluster capacity in the format {'cpu': '10', 'ram': '49125240Ki', 'pods': '330'}' to ''
              - AdditionalProperties changed
                - Schema added
            - Modified property: nodes
              - Items changed
                - Properties changed
                  - Modified property: annotations
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: initial_data
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: labels
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
            - Modified property: requested
              - Type changed from '' to 'object'
              - Description changed from 'Cluster requested resources in the format {'cpu': '1450m', 'memory': '884Mi', 'pods': '13'}' to ''
              - AdditionalProperties changed
                - Schema added

PUT /api/rancher-clusters/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: capacity
              - Type changed from '' to 'object'
              - Description changed from 'Cluster capacity in the format {'cpu': '10', 'ram': '49125240Ki', 'pods': '330'}' to ''
              - AdditionalProperties changed
                - Schema added
            - Modified property: nodes
              - Items changed
                - Properties changed
                  - Modified property: annotations
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: initial_data
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: labels
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
            - Modified property: requested
              - Type changed from '' to 'object'
              - Description changed from 'Cluster requested resources in the format {'cpu': '1450m', 'memory': '884Mi', 'pods': '13'}' to ''
              - AdditionalProperties changed
                - Schema added

POST /api/rancher-clusters/{uuid}/create_management_security_group/

- Responses changed
  - New response: 201
  - Deleted response: 200

POST /api/rancher-clusters/{uuid}/import_yaml/

- Responses changed
  - Modified response: 200
    - Description changed from '' to 'No response body'
    - Content changed
      - Deleted media type: application/json

GET /api/rancher-hpas/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: metrics
                - Type changed from '' to 'array'
                - Items changed
                  - Schema added

POST /api/rancher-hpas/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: metrics
            - Type changed from '' to 'array'
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: metrics
              - Type changed from '' to 'array'
              - Items changed
                - Schema added

GET /api/rancher-hpas/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: metrics
              - Type changed from '' to 'array'
              - Items changed
                - Schema added

PATCH /api/rancher-hpas/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: metrics
            - Type changed from '' to 'array'
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: metrics
              - Type changed from '' to 'array'
              - Items changed
                - Schema added

PUT /api/rancher-hpas/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: metrics
            - Type changed from '' to 'array'
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: metrics
              - Type changed from '' to 'array'
              - Items changed
                - Schema added

GET /api/rancher-hpas/{uuid}/yaml/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: detail
            - Deleted required property: cluster
            - Deleted required property: cluster_name
            - Deleted required property: cluster_uuid
            - Deleted required property: created
            - Deleted required property: current_replicas
            - Deleted required property: desired_replicas
            - Deleted required property: metrics
            - Deleted required property: modified
            - Deleted required property: name
            - Deleted required property: namespace
            - Deleted required property: namespace_name
            - Deleted required property: namespace_uuid
            - Deleted required property: project
            - Deleted required property: project_name
            - Deleted required property: project_uuid
            - Deleted required property: runtime_state
            - Deleted required property: url
            - Deleted required property: uuid
            - Deleted required property: workload_name
            - Deleted required property: workload_uuid
          - Properties changed
            - New property: detail
            - Deleted property: cluster
            - Deleted property: cluster_name
            - Deleted property: cluster_uuid
            - Deleted property: created
            - Deleted property: current_replicas
            - Deleted property: description
            - Deleted property: desired_replicas
            - Deleted property: max_replicas
            - Deleted property: metrics
            - Deleted property: min_replicas
            - Deleted property: modified
            - Deleted property: name
            - Deleted property: namespace
            - Deleted property: namespace_name
            - Deleted property: namespace_uuid
            - Deleted property: project
            - Deleted property: project_name
            - Deleted property: project_uuid
            - Deleted property: runtime_state
            - Deleted property: url
            - Deleted property: uuid
            - Deleted property: workload
            - Deleted property: workload_name
            - Deleted property: workload_uuid

PUT /api/rancher-hpas/{uuid}/yaml/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: metrics
            - Type changed from '' to 'array'
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: detail
            - Deleted required property: cluster
            - Deleted required property: cluster_name
            - Deleted required property: cluster_uuid
            - Deleted required property: created
            - Deleted required property: current_replicas
            - Deleted required property: desired_replicas
            - Deleted required property: metrics
            - Deleted required property: modified
            - Deleted required property: name
            - Deleted required property: namespace
            - Deleted required property: namespace_name
            - Deleted required property: namespace_uuid
            - Deleted required property: project
            - Deleted required property: project_name
            - Deleted required property: project_uuid
            - Deleted required property: runtime_state
            - Deleted required property: url
            - Deleted required property: uuid
            - Deleted required property: workload_name
            - Deleted required property: workload_uuid
          - Properties changed
            - New property: detail
            - Deleted property: cluster
            - Deleted property: cluster_name
            - Deleted property: cluster_uuid
            - Deleted property: created
            - Deleted property: current_replicas
            - Deleted property: description
            - Deleted property: desired_replicas
            - Deleted property: max_replicas
            - Deleted property: metrics
            - Deleted property: min_replicas
            - Deleted property: modified
            - Deleted property: name
            - Deleted property: namespace
            - Deleted property: namespace_name
            - Deleted property: namespace_uuid
            - Deleted property: project
            - Deleted property: project_name
            - Deleted property: project_uuid
            - Deleted property: runtime_state
            - Deleted property: url
            - Deleted property: uuid
            - Deleted property: workload
            - Deleted property: workload_name
            - Deleted property: workload_uuid

GET /api/rancher-ingresses/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: rules
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

POST /api/rancher-ingresses/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: rules
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: rules
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/rancher-ingresses/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: rules
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PATCH /api/rancher-ingresses/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: rules
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: rules
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PUT /api/rancher-ingresses/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: rules
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: rules
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/rancher-ingresses/{uuid}/yaml/

- Deleted query param: field
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: detail
          - Properties changed
            - New property: detail
            - Deleted property: access_url
            - Deleted property: backend_id
            - Deleted property: created
            - Deleted property: customer
            - Deleted property: customer_abbreviation
            - Deleted property: customer_name
            - Deleted property: customer_native_name
            - Deleted property: customer_uuid
            - Deleted property: description
            - Deleted property: error_message
            - Deleted property: error_traceback
            - Deleted property: is_limit_based
            - Deleted property: is_usage_based
            - Deleted property: marketplace_category_name
            - Deleted property: marketplace_category_uuid
            - Deleted property: marketplace_offering_name
            - Deleted property: marketplace_offering_plugin_options
            - Deleted property: marketplace_offering_type
            - Deleted property: marketplace_offering_uuid
            - Deleted property: marketplace_plan_uuid
            - Deleted property: marketplace_resource_state
            - Deleted property: marketplace_resource_uuid
            - Deleted property: modified
            - Deleted property: name
            - Deleted property: namespace
            - Deleted property: namespace_name
            - Deleted property: project
            - Deleted property: project_name
            - Deleted property: project_uuid
            - Deleted property: rancher_project
            - Deleted property: rancher_project_name
            - Deleted property: resource_type
            - Deleted property: rules
            - Deleted property: runtime_state
            - Deleted property: service_name
            - Deleted property: service_settings
            - Deleted property: service_settings_error_message
            - Deleted property: service_settings_state
            - Deleted property: service_settings_uuid
            - Deleted property: state
            - Deleted property: url
            - Deleted property: uuid

PUT /api/rancher-ingresses/{uuid}/yaml/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: rules
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: detail
          - Properties changed
            - New property: detail
            - Deleted property: access_url
            - Deleted property: backend_id
            - Deleted property: created
            - Deleted property: customer
            - Deleted property: customer_abbreviation
            - Deleted property: customer_name
            - Deleted property: customer_native_name
            - Deleted property: customer_uuid
            - Deleted property: description
            - Deleted property: error_message
            - Deleted property: error_traceback
            - Deleted property: is_limit_based
            - Deleted property: is_usage_based
            - Deleted property: marketplace_category_name
            - Deleted property: marketplace_category_uuid
            - Deleted property: marketplace_offering_name
            - Deleted property: marketplace_offering_plugin_options
            - Deleted property: marketplace_offering_type
            - Deleted property: marketplace_offering_uuid
            - Deleted property: marketplace_plan_uuid
            - Deleted property: marketplace_resource_state
            - Deleted property: marketplace_resource_uuid
            - Deleted property: modified
            - Deleted property: name
            - Deleted property: namespace
            - Deleted property: namespace_name
            - Deleted property: project
            - Deleted property: project_name
            - Deleted property: project_uuid
            - Deleted property: rancher_project
            - Deleted property: rancher_project_name
            - Deleted property: resource_type
            - Deleted property: rules
            - Deleted property: runtime_state
            - Deleted property: service_name
            - Deleted property: service_settings
            - Deleted property: service_settings_error_message
            - Deleted property: service_settings_state
            - Deleted property: service_settings_uuid
            - Deleted property: state
            - Deleted property: url
            - Deleted property: uuid

GET /api/rancher-nodes/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: annotations
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: labels
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

GET /api/rancher-nodes/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: annotations
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: labels
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/rancher-projects/{uuid}/secrets/

- OperationID changed from 'rancher_projects_secrets_retrieve' to 'rancher_projects_secrets_list'
- New query param: page
- New query param: page_size
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Type changed from 'object' to 'array'
          - Items changed
            - Schema added
          - Required changed
            - Deleted required property: created
            - Deleted required property: modified
            - Deleted required property: name
            - Deleted required property: namespaces
            - Deleted required property: url
            - Deleted required property: uuid
          - Properties changed
            - Deleted property: cluster
            - Deleted property: created
            - Deleted property: description
            - Deleted property: modified
            - Deleted property: name
            - Deleted property: namespaces
            - Deleted property: runtime_state
            - Deleted property: url
            - Deleted property: uuid
    - Headers changed
      - New header: x-result-count

GET /api/rancher-services/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: selector
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

POST /api/rancher-services/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: selector
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: selector
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/rancher-services/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: selector
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PATCH /api/rancher-services/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: selector
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: selector
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PUT /api/rancher-services/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: selector
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: selector
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/rancher-services/{uuid}/yaml/

- Deleted query param: field
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: detail
          - Properties changed
            - New property: detail
            - Deleted property: access_url
            - Deleted property: backend_id
            - Deleted property: cluster_ip
            - Deleted property: created
            - Deleted property: customer
            - Deleted property: customer_abbreviation
            - Deleted property: customer_name
            - Deleted property: customer_native_name
            - Deleted property: customer_uuid
            - Deleted property: description
            - Deleted property: error_message
            - Deleted property: error_traceback
            - Deleted property: is_limit_based
            - Deleted property: is_usage_based
            - Deleted property: marketplace_category_name
            - Deleted property: marketplace_category_uuid
            - Deleted property: marketplace_offering_name
            - Deleted property: marketplace_offering_plugin_options
            - Deleted property: marketplace_offering_type
            - Deleted property: marketplace_offering_uuid
            - Deleted property: marketplace_plan_uuid
            - Deleted property: marketplace_resource_state
            - Deleted property: marketplace_resource_uuid
            - Deleted property: modified
            - Deleted property: name
            - Deleted property: namespace
            - Deleted property: namespace_name
            - Deleted property: project
            - Deleted property: project_name
            - Deleted property: project_uuid
            - Deleted property: resource_type
            - Deleted property: runtime_state
            - Deleted property: selector
            - Deleted property: service_name
            - Deleted property: service_settings
            - Deleted property: service_settings_error_message
            - Deleted property: service_settings_state
            - Deleted property: service_settings_uuid
            - Deleted property: state
            - Deleted property: target_workloads
            - Deleted property: url
            - Deleted property: uuid

PUT /api/rancher-services/{uuid}/yaml/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: selector
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: detail
          - Properties changed
            - New property: detail
            - Deleted property: access_url
            - Deleted property: backend_id
            - Deleted property: cluster_ip
            - Deleted property: created
            - Deleted property: customer
            - Deleted property: customer_abbreviation
            - Deleted property: customer_name
            - Deleted property: customer_native_name
            - Deleted property: customer_uuid
            - Deleted property: description
            - Deleted property: error_message
            - Deleted property: error_traceback
            - Deleted property: is_limit_based
            - Deleted property: is_usage_based
            - Deleted property: marketplace_category_name
            - Deleted property: marketplace_category_uuid
            - Deleted property: marketplace_offering_name
            - Deleted property: marketplace_offering_plugin_options
            - Deleted property: marketplace_offering_type
            - Deleted property: marketplace_offering_uuid
            - Deleted property: marketplace_plan_uuid
            - Deleted property: marketplace_resource_state
            - Deleted property: marketplace_resource_uuid
            - Deleted property: modified
            - Deleted property: name
            - Deleted property: namespace
            - Deleted property: namespace_name
            - Deleted property: project
            - Deleted property: project_name
            - Deleted property: project_uuid
            - Deleted property: resource_type
            - Deleted property: runtime_state
            - Deleted property: selector
            - Deleted property: service_name
            - Deleted property: service_settings
            - Deleted property: service_settings_error_message
            - Deleted property: service_settings_state
            - Deleted property: service_settings_uuid
            - Deleted property: state
            - Deleted property: target_workloads
            - Deleted property: url
            - Deleted property: uuid

GET /api/rancher-template-versions/{template_uuid}/{version}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: questions
              - Items changed
                - Properties changed
                  - Modified property: subquestions
                    - Items changed
                      - Properties changed
                        - Modified property: validate_
                          - Type changed from '' to 'object'
                          - AdditionalProperties changed from null to true
                  - Modified property: validate_
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true

GET /api/rancher-workloads/{uuid}/yaml/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: detail
            - Deleted required property: cluster_name
            - Deleted required property: cluster_uuid
            - Deleted required property: created
            - Deleted required property: modified
            - Deleted required property: name
            - Deleted required property: namespace_name
            - Deleted required property: namespace_uuid
            - Deleted required property: project_name
            - Deleted required property: project_uuid
            - Deleted required property: scale
            - Deleted required property: url
            - Deleted required property: uuid
          - Properties changed
            - New property: detail
            - Deleted property: cluster
            - Deleted property: cluster_name
            - Deleted property: cluster_uuid
            - Deleted property: created
            - Deleted property: modified
            - Deleted property: name
            - Deleted property: namespace
            - Deleted property: namespace_name
            - Deleted property: namespace_uuid
            - Deleted property: project
            - Deleted property: project_name
            - Deleted property: project_uuid
            - Deleted property: runtime_state
            - Deleted property: scale
            - Deleted property: url
            - Deleted property: uuid

PUT /api/rancher-workloads/{uuid}/yaml/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: detail
            - Deleted required property: cluster_name
            - Deleted required property: cluster_uuid
            - Deleted required property: created
            - Deleted required property: modified
            - Deleted required property: name
            - Deleted required property: namespace_name
            - Deleted required property: namespace_uuid
            - Deleted required property: project_name
            - Deleted required property: project_uuid
            - Deleted required property: scale
            - Deleted required property: url
            - Deleted required property: uuid
          - Properties changed
            - New property: detail
            - Deleted property: cluster
            - Deleted property: cluster_name
            - Deleted property: cluster_uuid
            - Deleted property: created
            - Deleted property: modified
            - Deleted property: name
            - Deleted property: namespace
            - Deleted property: namespace_name
            - Deleted property: namespace_uuid
            - Deleted property: project
            - Deleted property: project_name
            - Deleted property: project_uuid
            - Deleted property: runtime_state
            - Deleted property: scale
            - Deleted property: url
            - Deleted property: uuid

POST /api/remote-waldur-api/remote_categories/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: sections
                - Items changed
                  - Properties changed
                    - Modified property: attributes
                      - Items changed
                        - Properties changed
                          - Modified property: default
                            - Type changed from '' to 'object'
                            - AdditionalProperties changed from null to true

GET /api/reviewer-profiles/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: alternative_names
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: publications
                - Items changed
                  - Properties changed
                    - Modified property: coauthors
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true
                    - Modified property: external_ids
                      - Type changed from '' to 'object'
                      - AdditionalProperties changed from null to true

POST /api/reviewer-profiles/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: alternative_names
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: alternative_names
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: publications
              - Items changed
                - Properties changed
                  - Modified property: coauthors
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: external_ids
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true

GET /api/reviewer-profiles/me/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: alternative_names
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: publications
              - Items changed
                - Properties changed
                  - Modified property: coauthors
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: external_ids
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true

PATCH /api/reviewer-profiles/me/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: alternative_names
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: alternative_names
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: publications
              - Items changed
                - Properties changed
                  - Modified property: coauthors
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: external_ids
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true

POST /api/reviewer-profiles/me/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: alternative_names
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: alternative_names
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: publications
              - Items changed
                - Properties changed
                  - Modified property: coauthors
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: external_ids
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true

POST /api/reviewer-profiles/publish/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: alternative_names
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true

POST /api/reviewer-profiles/unpublish/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: alternative_names
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true

GET /api/reviewer-profiles/{reviewer_profile_uuid}/publications/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: coauthors
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: external_ids
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

POST /api/reviewer-profiles/{reviewer_profile_uuid}/publications/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: coauthors
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: external_ids
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: coauthors
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: external_ids
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/reviewer-profiles/{reviewer_profile_uuid}/publications/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: coauthors
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: external_ids
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PATCH /api/reviewer-profiles/{reviewer_profile_uuid}/publications/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: coauthors
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: external_ids
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: coauthors
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: external_ids
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PUT /api/reviewer-profiles/{reviewer_profile_uuid}/publications/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: coauthors
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
          - Modified property: external_ids
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: coauthors
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: external_ids
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/reviewer-profiles/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: alternative_names
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: publications
              - Items changed
                - Properties changed
                  - Modified property: coauthors
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: external_ids
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true

PATCH /api/reviewer-profiles/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: alternative_names
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: alternative_names
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: publications
              - Items changed
                - Properties changed
                  - Modified property: coauthors
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: external_ids
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true

PUT /api/reviewer-profiles/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: alternative_names
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: alternative_names
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: publications
              - Items changed
                - Properties changed
                  - Modified property: coauthors
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: external_ids
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true

POST /api/reviewer-profiles/{uuid}/connect-orcid/callback/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: alternative_names
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: publications
              - Items changed
                - Properties changed
                  - Modified property: coauthors
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true
                  - Modified property: external_ids
                    - Type changed from '' to 'object'
                    - AdditionalProperties changed from null to true

POST /api/reviewer-profiles/{uuid}/disconnect-orcid/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: alternative_names
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true

POST /api/reviewer-profiles/{uuid}/sync-orcid/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: alternative_names
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true

GET /api/reviewer-suggestions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: matched_keywords
                - Type changed from '' to 'array'
                - Description changed from 'Keywords from reviewer's expertise that matched the source text' to ''
                - Items changed
                  - Schema added
              - Modified property: top_matching_proposals
                - Type changed from '' to 'array'
                - Description changed from 'Top proposals with highest affinity: [{uuid, name, slug, affinity}, ...]' to ''
                - Items changed
                  - Schema added

DELETE /api/reviewer-suggestions/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'call.manager' to 'call'
    - Added /0/scopes/- with value: 'call.manager'

GET /api/reviewer-suggestions/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: matched_keywords
              - Type changed from '' to 'array'
              - Description changed from 'Keywords from reviewer's expertise that matched the source text' to ''
              - Items changed
                - Schema added
            - Modified property: top_matching_proposals
              - Type changed from '' to 'array'
              - Description changed from 'Top proposals with highest affinity: [{uuid, name, slug, affinity}, ...]' to ''
              - Items changed
                - Schema added

POST /api/reviewer-suggestions/{uuid}/confirm/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: matched_keywords
              - Type changed from '' to 'array'
              - Description changed from 'Keywords from reviewer's expertise that matched the source text' to ''
              - Items changed
                - Schema added
            - Modified property: top_matching_proposals
              - Type changed from '' to 'array'
              - Description changed from 'Top proposals with highest affinity: [{uuid, name, slug, affinity}, ...]' to ''
              - Items changed
                - Schema added

POST /api/reviewer-suggestions/{uuid}/reject/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: matched_keywords
              - Type changed from '' to 'array'
              - Description changed from 'Keywords from reviewer's expertise that matched the source text' to ''
              - Items changed
                - Schema added
            - Modified property: top_matching_proposals
              - Type changed from '' to 'array'
              - Description changed from 'Top proposals with highest affinity: [{uuid, name, slug, affinity}, ...]' to ''
              - Items changed
                - Schema added

POST /api/roles/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: permissions
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true

PUT /api/roles/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: permissions
            - Type changed from '' to 'object'
            - AdditionalProperties changed from null to true

POST /api/slurm-allocations/{uuid}/set_limits/

- Responses changed
  - New response: 202
  - Deleted response: 200

GET /api/slurm-jobs/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: report
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

POST /api/slurm-jobs/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: report
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/slurm-jobs/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: report
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PATCH /api/slurm-jobs/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: report
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PUT /api/slurm-jobs/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: report
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/stats/celery/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: active
              - AdditionalProperties changed
                - Items changed
                  - Properties changed
                    - Modified property: args
                      - Items changed
                        - Type changed from '' to 'object'
                        - AdditionalProperties changed from null to true
            - Modified property: reserved
              - AdditionalProperties changed
                - Items changed
                  - Properties changed
                    - Modified property: args
                      - Items changed
                        - Type changed from '' to 'object'
                        - AdditionalProperties changed from null to true
            - Modified property: scheduled
              - AdditionalProperties changed
                - Items changed
                  - Properties changed
                    - Modified property: request
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/CeleryTask
                          - Properties changed
                            - Modified property: args
                              - Items changed
                                - Type changed from '' to 'object'
                                - AdditionalProperties changed from null to true

POST /api/stats/query/

- Description changed from 'Execute a given SQL query against a read-only database replica. This is a powerful tool for diagnostics and reporting, but should be used with caution. Requires support user permissions.' to 'Execute a given SQL query against a read-only database replica. This is a powerful tool for diagnostics and reporting, but should be used with caution. Requires staff user permissions.'

GET /api/support-comments/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: author_image
            - Properties changed
              - New property: author_image

GET /api/support-comments/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: author_image
          - Properties changed
            - New property: author_image

PATCH /api/support-comments/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: author_image
          - Properties changed
            - New property: author_image

PUT /api/support-comments/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: author_image
          - Properties changed
            - New property: author_image

GET /api/support-issues/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - Deleted required property: link
              - Deleted required property: processing_log
            - Properties changed
              - Modified property: processing_log
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

POST /api/support-issues/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: link
            - Deleted required property: processing_log
          - Properties changed
            - Modified property: processing_log
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/support-issues/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: link
            - Deleted required property: processing_log
          - Properties changed
            - Modified property: processing_log
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PATCH /api/support-issues/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: link
            - Deleted required property: processing_log
          - Properties changed
            - Modified property: processing_log
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

PUT /api/support-issues/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: link
            - Deleted required property: processing_log
          - Properties changed
            - Modified property: processing_log
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

POST /api/support-issues/{uuid}/comment/

- Responses changed
  - New response: 201
  - Deleted response: 200

POST /api/support-issues/{uuid}/sync/

- Responses changed
  - Modified response: 200
    - Description changed from '' to 'No response body'
    - Content changed
      - Deleted media type: application/json

POST /api/support-request-types-admin/reorder/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: status
            - Deleted required property: backend_id
            - Deleted required property: backend_name
            - Deleted required property: is_synced
            - Deleted required property: issue_type_name
            - Deleted required property: name
            - Deleted required property: url
            - Deleted required property: uuid
          - Properties changed
            - New property: status
            - Deleted property: backend_id
            - Deleted property: backend_name
            - Deleted property: is_active
            - Deleted property: is_synced
            - Deleted property: issue_type_name
            - Deleted property: name
            - Deleted property: order
            - Deleted property: url
            - Deleted property: uuid

POST /api/support-request-types-admin/{uuid}/activate/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: status
            - Deleted required property: backend_id
            - Deleted required property: backend_name
            - Deleted required property: is_synced
            - Deleted required property: issue_type_name
            - Deleted required property: name
            - Deleted required property: url
            - Deleted required property: uuid
          - Properties changed
            - New property: status
            - Deleted property: backend_id
            - Deleted property: backend_name
            - Deleted property: is_active
            - Deleted property: is_synced
            - Deleted property: issue_type_name
            - Deleted property: name
            - Deleted property: order
            - Deleted property: url
            - Deleted property: uuid

POST /api/support-request-types-admin/{uuid}/deactivate/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: status
            - Deleted required property: backend_id
            - Deleted required property: backend_name
            - Deleted required property: is_synced
            - Deleted required property: issue_type_name
            - Deleted required property: name
            - Deleted required property: url
            - Deleted required property: uuid
          - Properties changed
            - New property: status
            - Deleted property: backend_id
            - Deleted property: backend_name
            - Deleted property: is_active
            - Deleted property: is_synced
            - Deleted property: issue_type_name
            - Deleted property: name
            - Deleted property: order
            - Deleted property: url
            - Deleted property: uuid

GET /api/system-logs/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: context
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true

GET /api/system-logs/{id}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: context
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true

GET /api/user-actions/summary/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: by_type
              - Description changed from '' to 'Map of action type string to count of actions'
              - AdditionalProperties changed
                - Type changed from '' to 'integer'
            - Modified property: by_urgency
              - Description changed from '' to 'Map of urgency level to count of actions'
              - AdditionalProperties changed
                - Type changed from '' to 'integer'

GET /api/user-group-invitations/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: user_affiliations
                - Type changed from '' to 'array'
                - Items changed
                  - Schema added
              - Modified property: user_email_patterns
                - Type changed from '' to 'array'
                - Items changed
                  - Schema added
              - Modified property: user_identity_sources
                - Type changed from '' to 'array'
                - Description changed from 'List of allowed identity sources (identity providers).' to ''
                - Items changed
                  - Schema added

POST /api/user-group-invitations/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: user_affiliations
            - Type changed from '' to 'array'
            - Items changed
              - Schema added
          - Modified property: user_email_patterns
            - Type changed from '' to 'array'
            - Items changed
              - Schema added
          - Modified property: user_identity_sources
            - Type changed from '' to 'array'
            - Description changed from 'List of allowed identity sources (identity providers).' to ''
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: user_affiliations
              - Type changed from '' to 'array'
              - Items changed
                - Schema added
            - Modified property: user_email_patterns
              - Type changed from '' to 'array'
              - Items changed
                - Schema added
            - Modified property: user_identity_sources
              - Type changed from '' to 'array'
              - Description changed from 'List of allowed identity sources (identity providers).' to ''
              - Items changed
                - Schema added

GET /api/user-group-invitations/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: user_affiliations
              - Type changed from '' to 'array'
              - Items changed
                - Schema added
            - Modified property: user_email_patterns
              - Type changed from '' to 'array'
              - Items changed
                - Schema added
            - Modified property: user_identity_sources
              - Type changed from '' to 'array'
              - Description changed from 'List of allowed identity sources (identity providers).' to ''
              - Items changed
                - Schema added

PATCH /api/user-group-invitations/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: user_affiliations
            - Type changed from '' to 'array'
            - Items changed
              - Schema added
          - Modified property: user_email_patterns
            - Type changed from '' to 'array'
            - Items changed
              - Schema added
          - Modified property: user_identity_sources
            - Type changed from '' to 'array'
            - Description changed from 'List of allowed identity sources (identity providers).' to ''
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: user_affiliations
              - Type changed from '' to 'array'
              - Items changed
                - Schema added
            - Modified property: user_email_patterns
              - Type changed from '' to 'array'
              - Items changed
                - Schema added
            - Modified property: user_identity_sources
              - Type changed from '' to 'array'
              - Description changed from 'List of allowed identity sources (identity providers).' to ''
              - Items changed
                - Schema added

PUT /api/user-group-invitations/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: user_affiliations
            - Type changed from '' to 'array'
            - Items changed
              - Schema added
          - Modified property: user_email_patterns
            - Type changed from '' to 'array'
            - Items changed
              - Schema added
          - Modified property: user_identity_sources
            - Type changed from '' to 'array'
            - Description changed from 'List of allowed identity sources (identity providers).' to ''
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: user_affiliations
              - Type changed from '' to 'array'
              - Items changed
                - Schema added
            - Modified property: user_email_patterns
              - Type changed from '' to 'array'
              - Items changed
                - Schema added
            - Modified property: user_identity_sources
              - Type changed from '' to 'array'
              - Description changed from 'List of allowed identity sources (identity providers).' to ''
              - Items changed
                - Schema added

POST /api/user-group-invitations/{uuid}/submit_request/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: project_created
            - New property: project_uuid

GET /api/user-permissions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: project_uuid

GET /api/user-permissions/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: project_uuid

GET /api/users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [can_use_personal_access_tokens is_admin_deactivated should_protect_user_details]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: can_use_personal_access_tokens
              - New property: is_admin_deactivated
              - New property: should_protect_user_details
              - Modified property: active_isds
                - Type changed from '' to 'array'
                - Description changed from 'List of ISDs that have asserted this user exists. User is deactivated when this becomes empty.' to ''
                - ReadOnly changed from true to false
                - Items changed
                  - Schema added
              - Modified property: affiliations
                - Type changed from '' to 'array'
                - Description changed from 'Person's affiliation within organization such as student, faculty, staff.' to ''
                - ReadOnly changed from true to false
                - Items changed
                  - Schema added
              - Modified property: attribute_sources
                - Type changed from '' to 'object'
                - AdditionalProperties changed from null to true
              - Modified property: eduperson_assurance
                - Type changed from '' to 'array'
                - Description changed from 'REFEDS assurance profile URIs from identity provider' to ''
                - Items changed
                  - Schema added
              - Modified property: managed_isds
                - Type changed from '' to 'array'
                - Description changed from 'List of ISD source identifiers this user can manage via Identity Bridge. E.g., ['isd:puhuri', 'isd:fenix']. Non-empty list implies identity manager role.' to ''
                - Items changed
                  - Schema added
              - Modified property: nationalities
                - Type changed from '' to 'array'
                - Description changed from 'List of all citizenships (ISO 3166-1 alpha-2 codes)' to ''
                - Items changed
                  - Schema added
              - Modified property: permissions
                - Items changed
                  - Properties changed
                    - New property: project_uuid

POST /api/users/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: active_isds
          - New property: affiliations
          - New property: can_use_personal_access_tokens
          - Modified property: eduperson_assurance
            - Type changed from '' to 'array'
            - Description changed from 'REFEDS assurance profile URIs from identity provider' to ''
            - Items changed
              - Schema added
          - Modified property: managed_isds
            - Type changed from '' to 'array'
            - Description changed from 'List of ISD source identifiers this user can manage via Identity Bridge. E.g., ['isd:puhuri', 'isd:fenix']. Non-empty list implies identity manager role.' to ''
            - Items changed
              - Schema added
          - Modified property: nationalities
            - Type changed from '' to 'array'
            - Description changed from 'List of all citizenships (ISO 3166-1 alpha-2 codes)' to ''
            - Items changed
              - Schema added
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: active_isds
          - New property: affiliations
          - New property: can_use_personal_access_tokens
          - Modified property: eduperson_assurance
            - Type changed from '' to 'array'
            - Description changed from 'REFEDS assurance profile URIs from identity provider' to ''
            - Items changed
              - Schema added
          - Modified property: managed_isds
            - Type changed from '' to 'array'
            - Description changed from 'List of ISD source identifiers this user can manage via Identity Bridge. E.g., ['isd:puhuri', 'isd:fenix']. Non-empty list implies identity manager role.' to ''
            - Items changed
              - Schema added
          - Modified property: nationalities
            - Type changed from '' to 'array'
            - Description changed from 'List of all citizenships (ISO 3166-1 alpha-2 codes)' to ''
            - Items changed
              - Schema added
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: active_isds
          - New property: affiliations
          - New property: can_use_personal_access_tokens
          - Modified property: eduperson_assurance
            - Type changed from '' to 'array'
            - Description changed from 'REFEDS assurance profile URIs from identity provider' to ''
            - Items changed
              - Schema added
          - Modified property: managed_isds
            - Type changed from '' to 'array'
            - Description changed from 'List of ISD source identifiers this user can manage via Identity Bridge. E.g., ['isd:puhuri', 'isd:fenix']. Non-empty list implies identity manager role.' to ''
            - Items changed
              - Schema added
          - Modified property: nationalities
            - Type changed from '' to 'array'
            - Description changed from 'List of all citizenships (ISO 3166-1 alpha-2 codes)' to ''
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: can_use_personal_access_tokens
            - New property: is_admin_deactivated
            - New property: should_protect_user_details
            - Modified property: active_isds
              - Type changed from '' to 'array'
              - Description changed from 'List of ISDs that have asserted this user exists. User is deactivated when this becomes empty.' to ''
              - ReadOnly changed from true to false
              - Items changed
                - Schema added
            - Modified property: affiliations
              - Type changed from '' to 'array'
              - Description changed from 'Person's affiliation within organization such as student, faculty, staff.' to ''
              - ReadOnly changed from true to false
              - Items changed
                - Schema added
            - Modified property: attribute_sources
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: eduperson_assurance
              - Type changed from '' to 'array'
              - Description changed from 'REFEDS assurance profile URIs from identity provider' to ''
              - Items changed
                - Schema added
            - Modified property: managed_isds
              - Type changed from '' to 'array'
              - Description changed from 'List of ISD source identifiers this user can manage via Identity Bridge. E.g., ['isd:puhuri', 'isd:fenix']. Non-empty list implies identity manager role.' to ''
              - Items changed
                - Schema added
            - Modified property: nationalities
              - Type changed from '' to 'array'
              - Description changed from 'List of all citizenships (ISO 3166-1 alpha-2 codes)' to ''
              - Items changed
                - Schema added
            - Modified property: permissions
              - Items changed
                - Properties changed
                  - New property: project_uuid

GET /api/users/me/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [can_use_personal_access_tokens is_admin_deactivated profile_completeness should_protect_user_details]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: can_use_personal_access_tokens
            - New property: is_admin_deactivated
            - New property: profile_completeness
            - New property: should_protect_user_details
            - Modified property: active_isds
              - Type changed from '' to 'array'
              - Description changed from 'List of ISDs that have asserted this user exists. User is deactivated when this becomes empty.' to ''
              - ReadOnly changed from true to false
              - Items changed
                - Schema added
            - Modified property: affiliations
              - Type changed from '' to 'array'
              - Description changed from 'Person's affiliation within organization such as student, faculty, staff.' to ''
              - ReadOnly changed from true to false
              - Items changed
                - Schema added
            - Modified property: attribute_sources
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: eduperson_assurance
              - Type changed from '' to 'array'
              - Description changed from 'REFEDS assurance profile URIs from identity provider' to ''
              - Items changed
                - Schema added
            - Modified property: ip_address
              - Nullable changed from true to false
            - Modified property: managed_isds
              - Type changed from '' to 'array'
              - Description changed from 'List of ISD source identifiers this user can manage via Identity Bridge. E.g., ['isd:puhuri', 'isd:fenix']. Non-empty list implies identity manager role.' to ''
              - Items changed
                - Schema added
            - Modified property: nationalities
              - Type changed from '' to 'array'
              - Description changed from 'List of all citizenships (ISO 3166-1 alpha-2 codes)' to ''
              - Items changed
                - Schema added
            - Modified property: permissions
              - Items changed
                - Properties changed
                  - New property: project_uuid

GET /api/users/profile_completeness/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: enforcement_enabled
            - Deleted required property: is_complete
            - Deleted required property: mandatory_fields
            - Deleted required property: missing_fields

GET /api/users/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [can_use_personal_access_tokens is_admin_deactivated should_protect_user_details]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: can_use_personal_access_tokens
            - New property: is_admin_deactivated
            - New property: should_protect_user_details
            - Modified property: active_isds
              - Type changed from '' to 'array'
              - Description changed from 'List of ISDs that have asserted this user exists. User is deactivated when this becomes empty.' to ''
              - ReadOnly changed from true to false
              - Items changed
                - Schema added
            - Modified property: affiliations
              - Type changed from '' to 'array'
              - Description changed from 'Person's affiliation within organization such as student, faculty, staff.' to ''
              - ReadOnly changed from true to false
              - Items changed
                - Schema added
            - Modified property: attribute_sources
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: eduperson_assurance
              - Type changed from '' to 'array'
              - Description changed from 'REFEDS assurance profile URIs from identity provider' to ''
              - Items changed
                - Schema added
            - Modified property: managed_isds
              - Type changed from '' to 'array'
              - Description changed from 'List of ISD source identifiers this user can manage via Identity Bridge. E.g., ['isd:puhuri', 'isd:fenix']. Non-empty list implies identity manager role.' to ''
              - Items changed
                - Schema added
            - Modified property: nationalities
              - Type changed from '' to 'array'
              - Description changed from 'List of all citizenships (ISO 3166-1 alpha-2 codes)' to ''
              - Items changed
                - Schema added
            - Modified property: permissions
              - Items changed
                - Properties changed
                  - New property: project_uuid

PATCH /api/users/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: active_isds
          - New property: affiliations
          - New property: can_use_personal_access_tokens
          - Modified property: eduperson_assurance
            - Type changed from '' to 'array'
            - Description changed from 'REFEDS assurance profile URIs from identity provider' to ''
            - Items changed
              - Schema added
          - Modified property: managed_isds
            - Type changed from '' to 'array'
            - Description changed from 'List of ISD source identifiers this user can manage via Identity Bridge. E.g., ['isd:puhuri', 'isd:fenix']. Non-empty list implies identity manager role.' to ''
            - Items changed
              - Schema added
          - Modified property: nationalities
            - Type changed from '' to 'array'
            - Description changed from 'List of all citizenships (ISO 3166-1 alpha-2 codes)' to ''
            - Items changed
              - Schema added
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: active_isds
          - New property: affiliations
          - New property: can_use_personal_access_tokens
          - Modified property: eduperson_assurance
            - Type changed from '' to 'array'
            - Description changed from 'REFEDS assurance profile URIs from identity provider' to ''
            - Items changed
              - Schema added
          - Modified property: managed_isds
            - Type changed from '' to 'array'
            - Description changed from 'List of ISD source identifiers this user can manage via Identity Bridge. E.g., ['isd:puhuri', 'isd:fenix']. Non-empty list implies identity manager role.' to ''
            - Items changed
              - Schema added
          - Modified property: nationalities
            - Type changed from '' to 'array'
            - Description changed from 'List of all citizenships (ISO 3166-1 alpha-2 codes)' to ''
            - Items changed
              - Schema added
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: active_isds
          - New property: affiliations
          - New property: can_use_personal_access_tokens
          - Modified property: eduperson_assurance
            - Type changed from '' to 'array'
            - Description changed from 'REFEDS assurance profile URIs from identity provider' to ''
            - Items changed
              - Schema added
          - Modified property: managed_isds
            - Type changed from '' to 'array'
            - Description changed from 'List of ISD source identifiers this user can manage via Identity Bridge. E.g., ['isd:puhuri', 'isd:fenix']. Non-empty list implies identity manager role.' to ''
            - Items changed
              - Schema added
          - Modified property: nationalities
            - Type changed from '' to 'array'
            - Description changed from 'List of all citizenships (ISO 3166-1 alpha-2 codes)' to ''
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: can_use_personal_access_tokens
            - New property: is_admin_deactivated
            - New property: should_protect_user_details
            - Modified property: active_isds
              - Type changed from '' to 'array'
              - Description changed from 'List of ISDs that have asserted this user exists. User is deactivated when this becomes empty.' to ''
              - ReadOnly changed from true to false
              - Items changed
                - Schema added
            - Modified property: affiliations
              - Type changed from '' to 'array'
              - Description changed from 'Person's affiliation within organization such as student, faculty, staff.' to ''
              - ReadOnly changed from true to false
              - Items changed
                - Schema added
            - Modified property: attribute_sources
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: eduperson_assurance
              - Type changed from '' to 'array'
              - Description changed from 'REFEDS assurance profile URIs from identity provider' to ''
              - Items changed
                - Schema added
            - Modified property: managed_isds
              - Type changed from '' to 'array'
              - Description changed from 'List of ISD source identifiers this user can manage via Identity Bridge. E.g., ['isd:puhuri', 'isd:fenix']. Non-empty list implies identity manager role.' to ''
              - Items changed
                - Schema added
            - Modified property: nationalities
              - Type changed from '' to 'array'
              - Description changed from 'List of all citizenships (ISO 3166-1 alpha-2 codes)' to ''
              - Items changed
                - Schema added
            - Modified property: permissions
              - Items changed
                - Properties changed
                  - New property: project_uuid

PUT /api/users/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: active_isds
          - New property: affiliations
          - New property: can_use_personal_access_tokens
          - Modified property: eduperson_assurance
            - Type changed from '' to 'array'
            - Description changed from 'REFEDS assurance profile URIs from identity provider' to ''
            - Items changed
              - Schema added
          - Modified property: managed_isds
            - Type changed from '' to 'array'
            - Description changed from 'List of ISD source identifiers this user can manage via Identity Bridge. E.g., ['isd:puhuri', 'isd:fenix']. Non-empty list implies identity manager role.' to ''
            - Items changed
              - Schema added
          - Modified property: nationalities
            - Type changed from '' to 'array'
            - Description changed from 'List of all citizenships (ISO 3166-1 alpha-2 codes)' to ''
            - Items changed
              - Schema added
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: active_isds
          - New property: affiliations
          - New property: can_use_personal_access_tokens
          - Modified property: eduperson_assurance
            - Type changed from '' to 'array'
            - Description changed from 'REFEDS assurance profile URIs from identity provider' to ''
            - Items changed
              - Schema added
          - Modified property: managed_isds
            - Type changed from '' to 'array'
            - Description changed from 'List of ISD source identifiers this user can manage via Identity Bridge. E.g., ['isd:puhuri', 'isd:fenix']. Non-empty list implies identity manager role.' to ''
            - Items changed
              - Schema added
          - Modified property: nationalities
            - Type changed from '' to 'array'
            - Description changed from 'List of all citizenships (ISO 3166-1 alpha-2 codes)' to ''
            - Items changed
              - Schema added
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: active_isds
          - New property: affiliations
          - New property: can_use_personal_access_tokens
          - Modified property: eduperson_assurance
            - Type changed from '' to 'array'
            - Description changed from 'REFEDS assurance profile URIs from identity provider' to ''
            - Items changed
              - Schema added
          - Modified property: managed_isds
            - Type changed from '' to 'array'
            - Description changed from 'List of ISD source identifiers this user can manage via Identity Bridge. E.g., ['isd:puhuri', 'isd:fenix']. Non-empty list implies identity manager role.' to ''
            - Items changed
              - Schema added
          - Modified property: nationalities
            - Type changed from '' to 'array'
            - Description changed from 'List of all citizenships (ISO 3166-1 alpha-2 codes)' to ''
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: can_use_personal_access_tokens
            - New property: is_admin_deactivated
            - New property: should_protect_user_details
            - Modified property: active_isds
              - Type changed from '' to 'array'
              - Description changed from 'List of ISDs that have asserted this user exists. User is deactivated when this becomes empty.' to ''
              - ReadOnly changed from true to false
              - Items changed
                - Schema added
            - Modified property: affiliations
              - Type changed from '' to 'array'
              - Description changed from 'Person's affiliation within organization such as student, faculty, staff.' to ''
              - ReadOnly changed from true to false
              - Items changed
                - Schema added
            - Modified property: attribute_sources
              - Type changed from '' to 'object'
              - AdditionalProperties changed from null to true
            - Modified property: eduperson_assurance
              - Type changed from '' to 'array'
              - Description changed from 'REFEDS assurance profile URIs from identity provider' to ''
              - Items changed
                - Schema added
            - Modified property: managed_isds
              - Type changed from '' to 'array'
              - Description changed from 'List of ISD source identifiers this user can manage via Identity Bridge. E.g., ['isd:puhuri', 'isd:fenix']. Non-empty list implies identity manager role.' to ''
              - Items changed
                - Schema added
            - Modified property: nationalities
              - Type changed from '' to 'array'
              - Description changed from 'List of all citizenships (ISO 3166-1 alpha-2 codes)' to ''
              - Items changed
                - Schema added
            - Modified property: permissions
              - Items changed
                - Properties changed
                  - New property: project_uuid

POST /api/vmware-disks/{uuid}/extend/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/vmware-virtual-machine/{uuid}/create_disk/

- Responses changed
  - New response: 201
  - Deleted response: 200

POST /api/vmware-virtual-machine/{uuid}/create_port/

- Responses changed
  - New response: 201
  - Deleted response: 200

POST /api/vmware-virtual-machine/{uuid}/reboot_guest/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/vmware-virtual-machine/{uuid}/reset/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/vmware-virtual-machine/{uuid}/shutdown_guest/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/vmware-virtual-machine/{uuid}/start/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/vmware-virtual-machine/{uuid}/stop/

- Responses changed
  - New response: 202
  - Deleted response: 200

POST /api/vmware-virtual-machine/{uuid}/suspend/

- Responses changed
  - New response: 202
  - Deleted response: 200
