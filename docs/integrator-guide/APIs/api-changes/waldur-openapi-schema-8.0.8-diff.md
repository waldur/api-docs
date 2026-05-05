# OpenAPI schema diff - 8.0.8

## For version 8.0.8

### New Endpoints: 144

----------------------
GET /api/affiliated-organizations/  
HEAD /api/affiliated-organizations/  
POST /api/affiliated-organizations/  
GET /api/affiliated-organizations/report/  
HEAD /api/affiliated-organizations/report/  
DELETE /api/affiliated-organizations/{uuid}/  
GET /api/affiliated-organizations/{uuid}/  
PATCH /api/affiliated-organizations/{uuid}/  
PUT /api/affiliated-organizations/{uuid}/  
GET /api/affiliated-organizations/{uuid}/stats/  
GET /api/anonymous-chat-feedbacks/  
GET /api/anonymous-chat-feedbacks/{interaction_uuid}/  
GET /api/anonymous-chat-interactions/  
GET /api/anonymous-chat-interactions/budget/  
GET /api/anonymous-chat-interactions/by-session/{session_id}/  
GET /api/anonymous-chat-interactions/by-user/  
GET /api/anonymous-chat-interactions/by-user/{user_slug}/  
GET /api/anonymous-chat-interactions/kpi/  
GET /api/anonymous-chat-interactions/{uuid}/  
POST /api/chat-messages/{uuid}/feedback/  
GET /api/chat-system-prompts/  
HEAD /api/chat-system-prompts/  
POST /api/chat-system-prompts/  
DELETE /api/chat-system-prompts/{uuid}/  
GET /api/chat-system-prompts/{uuid}/  
PATCH /api/chat-system-prompts/{uuid}/  
PUT /api/chat-system-prompts/{uuid}/  
POST /api/chat-system-prompts/{uuid}/activate/  
POST /api/chat-system-prompts/{uuid}/deactivate/  
GET /api/customers/{uuid}/components-usage/  
POST /api/marketplace-chat/click/  
POST /api/marketplace-chat/feedback/  
POST /api/marketplace-chat/stream/  
GET /api/marketplace-component-usage-monthly/  
HEAD /api/marketplace-component-usage-monthly/  
GET /api/marketplace-offering-profiles/  
HEAD /api/marketplace-offering-profiles/  
POST /api/marketplace-offering-profiles/  
DELETE /api/marketplace-offering-profiles/{uuid}/  
GET /api/marketplace-offering-profiles/{uuid}/  
PATCH /api/marketplace-offering-profiles/{uuid}/  
PUT /api/marketplace-offering-profiles/{uuid}/  
POST /api/marketplace-offering-profiles/{uuid}/add_role/  
POST /api/marketplace-offering-profiles/{uuid}/remove_role/  
GET /api/marketplace-offering-roles/  
HEAD /api/marketplace-offering-roles/  
POST /api/marketplace-offering-roles/  
DELETE /api/marketplace-offering-roles/{uuid}/  
GET /api/marketplace-offering-roles/{uuid}/  
PATCH /api/marketplace-offering-roles/{uuid}/  
PUT /api/marketplace-offering-roles/{uuid}/  
POST /api/marketplace-provider-offerings/{uuid}/set_profile/  
GET /api/marketplace-provider-resource-projects/  
HEAD /api/marketplace-provider-resource-projects/  
GET /api/marketplace-provider-resource-projects/{uuid}/  
PATCH /api/marketplace-provider-resource-projects/{uuid}/  
PUT /api/marketplace-provider-resource-projects/{uuid}/  
POST /api/marketplace-provider-resource-projects/{uuid}/add_user/  
POST /api/marketplace-provider-resource-projects/{uuid}/delete_user/  
GET /api/marketplace-provider-resource-projects/{uuid}/list_users/  
POST /api/marketplace-provider-resource-projects/{uuid}/set_backend_id/  
POST /api/marketplace-provider-resource-projects/{uuid}/set_state_erred/  
POST /api/marketplace-provider-resource-projects/{uuid}/set_state_ok/  
POST /api/marketplace-provider-resource-projects/{uuid}/update_user/  
POST /api/marketplace-provider-resources/{uuid}/add_user/  
POST /api/marketplace-provider-resources/{uuid}/delete_user/  
GET /api/marketplace-provider-resources/{uuid}/list_users/  
POST /api/marketplace-provider-resources/{uuid}/update_user/  
GET /api/marketplace-resource-projects/  
HEAD /api/marketplace-resource-projects/  
POST /api/marketplace-resource-projects/  
DELETE /api/marketplace-resource-projects/{uuid}/  
GET /api/marketplace-resource-projects/{uuid}/  
PATCH /api/marketplace-resource-projects/{uuid}/  
PUT /api/marketplace-resource-projects/{uuid}/  
POST /api/marketplace-resource-projects/{uuid}/add_user/  
POST /api/marketplace-resource-projects/{uuid}/delete_user/  
GET /api/marketplace-resource-projects/{uuid}/list_users/  
POST /api/marketplace-resource-projects/{uuid}/update_user/  
POST /api/marketplace-resources/{uuid}/add_user/  
POST /api/marketplace-resources/{uuid}/delete_user/  
GET /api/marketplace-resources/{uuid}/list_users/  
GET /api/marketplace-resources/{uuid}/team_members/  
POST /api/marketplace-resources/{uuid}/update_user/  
GET /api/openportal-accounting-summary/  
HEAD /api/openportal-accounting-summary/  
GET /api/openportal-accounting-summary/{uuid}/  
GET /api/openportal-project-storage-reports/  
HEAD /api/openportal-project-storage-reports/  
GET /api/openportal-project-storage-reports/{id}/  
GET /api/openportal-project-usage-reports/  
HEAD /api/openportal-project-usage-reports/  
GET /api/openportal-project-usage-reports/{id}/  
GET /api/openportal-unmanaged-projects/{uuid}/components-usage/  
POST /api/openportal-unmanaged-projects/{uuid}/update_affiliated_organizations/  
GET /api/openportal/access_for_email/  
GET /api/openportal/offering_mapping/  
GET /api/openportal/project_mapping/  
GET /api/openportal/user_mapping/  
POST /api/openstack-health-monitors/{uuid}/pull/  
GET /api/openstack-hypervisor-inventories/  
HEAD /api/openstack-hypervisor-inventories/  
GET /api/openstack-hypervisor-inventories/{uuid}/  
GET /api/openstack-hypervisors/  
HEAD /api/openstack-hypervisors/  
GET /api/openstack-hypervisors/allocation_candidates/  
HEAD /api/openstack-hypervisors/allocation_candidates/  
GET /api/openstack-hypervisors/summary/  
HEAD /api/openstack-hypervisors/summary/  
GET /api/openstack-hypervisors/{uuid}/  
GET /api/openstack-instances/{uuid}/placement_allocations/  
POST /api/openstack-instances/{uuid}/rescue/  
POST /api/openstack-instances/{uuid}/unrescue/  
POST /api/openstack-listeners/{uuid}/pull/  
POST /api/openstack-loadbalancers/{uuid}/pull/  
POST /api/openstack-loadbalancers/{uuid}/set_security_groups/  
POST /api/openstack-pool-members/{uuid}/pull/  
POST /api/openstack-pools/{uuid}/pull/  
GET /api/openstack-routers/{uuid}/available_external_networks/  
POST /api/openstack-routers/{uuid}/remove_external_gateway/  
POST /api/openstack-routers/{uuid}/set_external_gateway/  
GET /api/projects/{uuid}/components-usage/  
POST /api/projects/{uuid}/update_affiliated_organizations/  
GET /api/role-availabilities/  
HEAD /api/role-availabilities/  
DELETE /api/role-availabilities/{uuid}/  
GET /api/role-availabilities/{uuid}/  
GET /api/science-domains/  
HEAD /api/science-domains/  
POST /api/science-domains/  
POST /api/science-domains/load_preset/  
GET /api/science-domains/presets/  
HEAD /api/science-domains/presets/  
DELETE /api/science-domains/{uuid}/  
GET /api/science-domains/{uuid}/  
PATCH /api/science-domains/{uuid}/  
PUT /api/science-domains/{uuid}/  
GET /api/science-sub-domains/  
HEAD /api/science-sub-domains/  
POST /api/science-sub-domains/  
DELETE /api/science-sub-domains/{uuid}/  
GET /api/science-sub-domains/{uuid}/  
PATCH /api/science-sub-domains/{uuid}/  
PUT /api/science-sub-domains/{uuid}/  

### Deleted Endpoints: 38

-------------------------
GET /api/marketplace-offering-user-roles/  
HEAD /api/marketplace-offering-user-roles/  
POST /api/marketplace-offering-user-roles/  
DELETE /api/marketplace-offering-user-roles/{uuid}/  
GET /api/marketplace-offering-user-roles/{uuid}/  
PATCH /api/marketplace-offering-user-roles/{uuid}/  
PUT /api/marketplace-offering-user-roles/{uuid}/  
POST /api/marketplace-provider-resources/{uuid}/set_keycloak_scopes/  
GET /api/marketplace-resource-users/  
HEAD /api/marketplace-resource-users/  
POST /api/marketplace-resource-users/  
DELETE /api/marketplace-resource-users/{uuid}/  
GET /api/marketplace-resource-users/{uuid}/  
GET /api/offering-keycloak-groups/  
HEAD /api/offering-keycloak-groups/  
POST /api/offering-keycloak-groups/import_remote/  
GET /api/offering-keycloak-groups/remote_group_members/  
HEAD /api/offering-keycloak-groups/remote_group_members/  
GET /api/offering-keycloak-groups/remote_groups/  
HEAD /api/offering-keycloak-groups/remote_groups/  
GET /api/offering-keycloak-groups/search_remote_users/  
HEAD /api/offering-keycloak-groups/search_remote_users/  
GET /api/offering-keycloak-groups/sync_status/  
HEAD /api/offering-keycloak-groups/sync_status/  
POST /api/offering-keycloak-groups/test_connection/  
DELETE /api/offering-keycloak-groups/{uuid}/  
GET /api/offering-keycloak-groups/{uuid}/  
POST /api/offering-keycloak-groups/{uuid}/pull_members/  
POST /api/offering-keycloak-groups/{uuid}/set_backend_id/  
GET /api/offering-keycloak-memberships/  
HEAD /api/offering-keycloak-memberships/  
POST /api/offering-keycloak-memberships/  
DELETE /api/offering-keycloak-memberships/{uuid}/  
GET /api/offering-keycloak-memberships/{uuid}/  
GET /api/proposal-protected-calls/{uuid}/applicant_attribute_config/  
DELETE /api/proposal-protected-calls/{uuid}/delete_applicant_attribute_config/  
PATCH /api/proposal-protected-calls/{uuid}/update_applicant_attribute_config/  
POST /api/proposal-protected-calls/{uuid}/update_applicant_attribute_config/  

### Modified Endpoints: 431

---------------------------
GET /api/aws-instances/

- Deleted query param: uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''

HEAD /api/aws-instances/

- Deleted query param: uuid

POST /api/aws-instances/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/aws-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PATCH /api/aws-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PUT /api/aws-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

POST /api/aws-instances/{uuid}/restart/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/aws-instances/{uuid}/start/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/aws-instances/{uuid}/stop/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

GET /api/aws-volumes/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''

POST /api/aws-volumes/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/aws-volumes/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PATCH /api/aws-volumes/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PUT /api/aws-volumes/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

POST /api/aws-volumes/{uuid}/detach/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

GET /api/azure-public-ips/

- Deleted query param: uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''

HEAD /api/azure-public-ips/

- Deleted query param: uuid

POST /api/azure-public-ips/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/azure-public-ips/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PATCH /api/azure-public-ips/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PUT /api/azure-public-ips/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/azure-resource-groups/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''

GET /api/azure-resource-groups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/azure-sql-databases/

- Deleted query param: uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''

HEAD /api/azure-sql-databases/

- Deleted query param: uuid

POST /api/azure-sql-databases/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/azure-sql-databases/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PATCH /api/azure-sql-databases/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PUT /api/azure-sql-databases/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/azure-sql-servers/

- Deleted query param: uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''

HEAD /api/azure-sql-servers/

- Deleted query param: uuid

POST /api/azure-sql-servers/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/azure-sql-servers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PATCH /api/azure-sql-servers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PUT /api/azure-sql-servers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/azure-virtualmachines/

- Deleted query param: uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''

HEAD /api/azure-virtualmachines/

- Deleted query param: uuid

POST /api/azure-virtualmachines/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/azure-virtualmachines/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PATCH /api/azure-virtualmachines/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PUT /api/azure-virtualmachines/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

POST /api/azure-virtualmachines/{uuid}/restart/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/azure-virtualmachines/{uuid}/start/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/azure-virtualmachines/{uuid}/stop/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/backend-resources/{uuid}/import_resource/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: project_is_in_grace_period
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: error_updated_at
                    - New property: output_updated_at
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: offering_uuid
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Schemas deleted: #/components/schemas/BlankEnum
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: error_updated_at
                    - New property: output_updated_at

GET /api/booking-offerings/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [profile_name profile_uuid]
      - Deleted enum values: [roles]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: profile_name
              - New property: profile_uuid
              - Deleted property: roles
              - Modified property: components
                - Items changed
                  - Properties changed
                    - New property: offering_uuid
                    - Modified property: limit_period
                      - Property 'OneOf' changed
                        - Schemas deleted: #/components/schemas/BlankEnum
              - Modified property: plans
                - Items changed
                  - Properties changed
                    - Modified property: future_prices
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'string'
                        - Format changed from 'double' to ''
                    - Modified property: minimal_price
                      - Type changed from 'number' to 'string'
                      - Format changed from 'double' to ''
                    - Modified property: prices
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'string'
                        - Format changed from 'double' to ''
                    - Modified property: quotas
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'integer'
                        - Format changed from 'double' to ''
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: create_orders_on_resource_project_change
                      - New property: enable_resource_projects
                      - New property: resource_projects_limits_required
                      - New property: usage_poll_interval_minutes
                      - Deleted property: keycloak_base_group
                      - Deleted property: keycloak_enabled
                      - Deleted property: keycloak_group_name_template
                      - Deleted property: keycloak_sync_frequency
                      - Deleted property: keycloak_username_label
              - Modified property: scope_name
                - Format changed from 'uuid' to ''

GET /api/booking-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [profile_name profile_uuid]
      - Deleted enum values: [roles]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: profile_name
            - New property: profile_uuid
            - Deleted property: roles
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: offering_uuid
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Schemas deleted: #/components/schemas/BlankEnum
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: future_prices
                    - AdditionalProperties changed
                      - Type changed from 'number' to 'string'
                      - Format changed from 'double' to ''
                  - Modified property: minimal_price
                    - Type changed from 'number' to 'string'
                    - Format changed from 'double' to ''
                  - Modified property: prices
                    - AdditionalProperties changed
                      - Type changed from 'number' to 'string'
                      - Format changed from 'double' to ''
                  - Modified property: quotas
                    - AdditionalProperties changed
                      - Type changed from 'number' to 'integer'
                      - Format changed from 'double' to ''
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: create_orders_on_resource_project_change
                    - New property: enable_resource_projects
                    - New property: resource_projects_limits_required
                    - New property: usage_poll_interval_minutes
                    - Deleted property: keycloak_base_group
                    - Deleted property: keycloak_enabled
                    - Deleted property: keycloak_group_name_template
                    - Deleted property: keycloak_sync_frequency
                    - Deleted property: keycloak_username_label
            - Modified property: scope_name
              - Format changed from 'uuid' to ''

GET /api/booking-resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [project_is_in_grace_period]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: project_is_in_grace_period
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: error_updated_at
                      - New property: output_updated_at
              - Modified property: offering_components
                - Items changed
                  - Properties changed
                    - New property: offering_uuid
                    - Modified property: limit_period
                      - Property 'OneOf' changed
                        - Schemas deleted: #/components/schemas/BlankEnum
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: error_updated_at
                      - New property: output_updated_at

GET /api/booking-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [project_is_in_grace_period]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: project_is_in_grace_period
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: error_updated_at
                    - New property: output_updated_at
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: offering_uuid
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Schemas deleted: #/components/schemas/BlankEnum
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: error_updated_at
                    - New property: output_updated_at

POST /api/booking-resources/{uuid}/accept/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/booking-resources/{uuid}/reject/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

GET /api/chat-messages/

- New query param: feedback_score
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: blocks
              - New required property: feedback_category
              - New required property: feedback_comment
              - New required property: feedback_score
              - New required property: feedback_submitted_at
              - New required property: warning
              - Deleted required property: content_display
              - Deleted required property: tool_calls
            - Properties changed
              - New property: blocks
              - New property: feedback_category
              - New property: feedback_comment
              - New property: feedback_score
              - New property: feedback_submitted_at
              - New property: warning
              - Deleted property: content
              - Deleted property: content_display
              - Deleted property: tool_calls

GET /api/chat-threads/

- New query param: has_feedback
- New query param: scope
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [has_feedback]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: has_feedback

GET /api/chat-threads/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [has_feedback]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_feedback

POST /api/chat-threads/{uuid}/archive/

- Request body changed

POST /api/chat-threads/{uuid}/unarchive/

- Request body changed

POST /api/chat/stream/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/x-ndjson
        - Schema changed
          - Properties changed
            - New property: category_uuid
            - New property: customer_uuid
            - New property: network
            - New property: ssh_key_name
            - New property: state
            - New property: system_volume_size
            - Deleted property: h
            - Deleted property: n
            - Deleted property: r
            - Modified property: k
              - Description changed from 'Component key (e.g. 'markdown', 'code', 'table', 'vm_order').' to 'Component key (e.g. 'markdown', 'code', 'vm_order', 'resource_list').'
            - Modified property: project_uuid
              - Description changed from 'Project UUID.' to 'Project UUID. Present when k='vm_order' or k='resource_list'.'

POST /api/customer-credits/{uuid}/apply_compensations/

- Request body changed

POST /api/customer-credits/{uuid}/clear_compensations/

- Request body changed

GET /api/customers/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [project_slug_template]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: project_slug_template

POST /api/customers/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: project_slug_template
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: project_slug_template
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: project_slug_template
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: project_slug_template

GET /api/customers/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [project_slug_template]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: project_slug_template

PATCH /api/customers/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: project_slug_template
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: project_slug_template
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: project_slug_template
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: project_slug_template

PUT /api/customers/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: project_slug_template
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: project_slug_template
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: project_slug_template
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: project_slug_template

GET /api/digitalocean-droplets/

- Deleted query param: uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''

HEAD /api/digitalocean-droplets/

- Deleted query param: uuid

POST /api/digitalocean-droplets/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/digitalocean-droplets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PATCH /api/digitalocean-droplets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PUT /api/digitalocean-droplets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

POST /api/digitalocean-droplets/{uuid}/restart/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/digitalocean-droplets/{uuid}/start/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/digitalocean-droplets/{uuid}/stop/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

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
                  - New enum values: [chat_feedback_submitted]
                  - Deleted enum values: [marketplace_offering_role_created marketplace_offering_role_deleted marketplace_offering_role_updated marketplace_resource_user_created marketplace_resource_user_deleted]

POST /api/hooks-email/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [chat_feedback_submitted]
              - Deleted enum values: [marketplace_offering_role_created marketplace_offering_role_deleted marketplace_offering_role_updated marketplace_resource_user_created marketplace_resource_user_deleted]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [chat_feedback_submitted]
                - Deleted enum values: [marketplace_offering_role_created marketplace_offering_role_deleted marketplace_offering_role_updated marketplace_resource_user_created marketplace_resource_user_deleted]

GET /api/hooks-email/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [chat_feedback_submitted]
                - Deleted enum values: [marketplace_offering_role_created marketplace_offering_role_deleted marketplace_offering_role_updated marketplace_resource_user_created marketplace_resource_user_deleted]

PATCH /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [chat_feedback_submitted]
              - Deleted enum values: [marketplace_offering_role_created marketplace_offering_role_deleted marketplace_offering_role_updated marketplace_resource_user_created marketplace_resource_user_deleted]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [chat_feedback_submitted]
                - Deleted enum values: [marketplace_offering_role_created marketplace_offering_role_deleted marketplace_offering_role_updated marketplace_resource_user_created marketplace_resource_user_deleted]

PUT /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [chat_feedback_submitted]
              - Deleted enum values: [marketplace_offering_role_created marketplace_offering_role_deleted marketplace_offering_role_updated marketplace_resource_user_created marketplace_resource_user_deleted]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [chat_feedback_submitted]
                - Deleted enum values: [marketplace_offering_role_created marketplace_offering_role_deleted marketplace_offering_role_updated marketplace_resource_user_created marketplace_resource_user_deleted]

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
                  - New enum values: [chat_feedback_submitted]
                  - Deleted enum values: [marketplace_offering_role_created marketplace_offering_role_deleted marketplace_offering_role_updated marketplace_resource_user_created marketplace_resource_user_deleted]

POST /api/hooks-web/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [chat_feedback_submitted]
              - Deleted enum values: [marketplace_offering_role_created marketplace_offering_role_deleted marketplace_offering_role_updated marketplace_resource_user_created marketplace_resource_user_deleted]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [chat_feedback_submitted]
                - Deleted enum values: [marketplace_offering_role_created marketplace_offering_role_deleted marketplace_offering_role_updated marketplace_resource_user_created marketplace_resource_user_deleted]

GET /api/hooks-web/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [chat_feedback_submitted]
                - Deleted enum values: [marketplace_offering_role_created marketplace_offering_role_deleted marketplace_offering_role_updated marketplace_resource_user_created marketplace_resource_user_deleted]

PATCH /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [chat_feedback_submitted]
              - Deleted enum values: [marketplace_offering_role_created marketplace_offering_role_deleted marketplace_offering_role_updated marketplace_resource_user_created marketplace_resource_user_deleted]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [chat_feedback_submitted]
                - Deleted enum values: [marketplace_offering_role_created marketplace_offering_role_deleted marketplace_offering_role_updated marketplace_resource_user_created marketplace_resource_user_deleted]

PUT /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [chat_feedback_submitted]
              - Deleted enum values: [marketplace_offering_role_created marketplace_offering_role_deleted marketplace_offering_role_updated marketplace_resource_user_created marketplace_resource_user_deleted]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [chat_feedback_submitted]
                - Deleted enum values: [marketplace_offering_role_created marketplace_offering_role_deleted marketplace_offering_role_updated marketplace_resource_user_created marketplace_resource_user_deleted]

GET /api/hooks/

- New query param: author_email
- New query param: author_fullname
- New query param: author_username
- New query param: last_published
- New query param: query
- Modified query param: author_uuid
  - Description changed from 'Filter by author UUID.' to ''
- Modified query param: is_active
  - Description changed from 'Filter by active status.' to ''

HEAD /api/hooks/

- New query param: author_email
- New query param: author_fullname
- New query param: author_username
- New query param: last_published
- New query param: query
- Modified query param: author_uuid
  - Description changed from 'Filter by author UUID.' to ''
- Modified query param: is_active
  - Description changed from 'Filter by active status.' to ''

POST /api/identity-bridge/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: address
          - Modified property: gender
            - Property 'OneOf' changed
              - Schemas added: #/components/schemas/IdentityBridgeRequestGenderEnum, #/components/schemas/NullEnum
            - Type changed from 'integer' to ''

POST /api/invoices/{uuid}/send_notification/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

GET /api/keys/

- Deleted query param: uuid

HEAD /api/keys/

- Deleted query param: uuid

GET /api/keys/{uuid}/history/

- Deleted query param: uuid

GET /api/maintenance-announcements-template/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: affected_offerings
                - Items changed
                  - Required changed
                    - New required property: maintenance_template
                    - New required property: offering_uuid
                    - Deleted required property: impact_level_display
                    - Deleted required property: maintenance
                  - Properties changed
                    - New property: maintenance_template
                    - New property: offering_uuid
                    - Deleted property: impact_level_display
                    - Deleted property: maintenance

POST /api/maintenance-announcements-template/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: affected_offerings
              - Items changed
                - Required changed
                  - New required property: maintenance_template
                  - New required property: offering_uuid
                  - Deleted required property: impact_level_display
                  - Deleted required property: maintenance
                - Properties changed
                  - New property: maintenance_template
                  - New property: offering_uuid
                  - Deleted property: impact_level_display
                  - Deleted property: maintenance

GET /api/maintenance-announcements-template/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: affected_offerings
              - Items changed
                - Required changed
                  - New required property: maintenance_template
                  - New required property: offering_uuid
                  - Deleted required property: impact_level_display
                  - Deleted required property: maintenance
                - Properties changed
                  - New property: maintenance_template
                  - New property: offering_uuid
                  - Deleted property: impact_level_display
                  - Deleted property: maintenance

PATCH /api/maintenance-announcements-template/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: affected_offerings
              - Items changed
                - Required changed
                  - New required property: maintenance_template
                  - New required property: offering_uuid
                  - Deleted required property: impact_level_display
                  - Deleted required property: maintenance
                - Properties changed
                  - New property: maintenance_template
                  - New property: offering_uuid
                  - Deleted property: impact_level_display
                  - Deleted property: maintenance

PUT /api/maintenance-announcements-template/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: affected_offerings
              - Items changed
                - Required changed
                  - New required property: maintenance_template
                  - New required property: offering_uuid
                  - Deleted required property: impact_level_display
                  - Deleted required property: maintenance
                - Properties changed
                  - New property: maintenance_template
                  - New property: offering_uuid
                  - Deleted property: impact_level_display
                  - Deleted property: maintenance

GET /api/managed-rancher-cluster-resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [project_is_in_grace_period]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: project_is_in_grace_period
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: error_updated_at
                      - New property: output_updated_at
              - Modified property: offering_components
                - Items changed
                  - Properties changed
                    - New property: offering_uuid
                    - Modified property: limit_period
                      - Property 'OneOf' changed
                        - Schemas deleted: #/components/schemas/BlankEnum
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: error_updated_at
                      - New property: output_updated_at

GET /api/managed-rancher-cluster-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [project_is_in_grace_period]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: project_is_in_grace_period
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: error_updated_at
                    - New property: output_updated_at
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: offering_uuid
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Schemas deleted: #/components/schemas/BlankEnum
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: error_updated_at
                    - New property: output_updated_at

GET /api/marketplace-course-accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: project_end_date
                - Nullable changed from false to true
              - Modified property: project_start_date
                - Nullable changed from false to true

POST /api/marketplace-course-accounts/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: project_end_date
              - Nullable changed from false to true
            - Modified property: project_start_date
              - Nullable changed from false to true

POST /api/marketplace-course-accounts/create_bulk/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: project_end_date
                - Nullable changed from false to true
              - Modified property: project_start_date
                - Nullable changed from false to true

GET /api/marketplace-course-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: project_end_date
              - Nullable changed from false to true
            - Modified property: project_start_date
              - Nullable changed from false to true

POST /api/marketplace-course-accounts/{uuid}/retry/

- Responses changed
  - Modified response: 202
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: project_end_date
              - Nullable changed from false to true
            - Modified property: project_start_date
              - Nullable changed from false to true

GET /api/marketplace-customer-estimated-cost-policies/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: customer_credit
                - Type changed from 'integer' to 'string'
                - Nullable changed from false to true

POST /api/marketplace-customer-estimated-cost-policies/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: customer_credit
              - Type changed from 'integer' to 'string'
              - Nullable changed from false to true

GET /api/marketplace-customer-estimated-cost-policies/actions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: customer_credit
              - Type changed from 'integer' to 'string'
              - Nullable changed from false to true

GET /api/marketplace-customer-estimated-cost-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: customer_credit
              - Type changed from 'integer' to 'string'
              - Nullable changed from false to true

PATCH /api/marketplace-customer-estimated-cost-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: customer_credit
              - Type changed from 'integer' to 'string'
              - Nullable changed from false to true

PUT /api/marketplace-customer-estimated-cost-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: customer_credit
              - Type changed from 'integer' to 'string'
              - Nullable changed from false to true

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
                      - New property: offering_has_active_tos
                      - New property: user_address

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
                    - New property: offering_has_active_tos
                    - New property: user_address

GET /api/marketplace-offering-users/

- New query param: offering_has_active_tos
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_has_active_tos user_address]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: offering_has_active_tos
              - New property: user_address

HEAD /api/marketplace-offering-users/

- New query param: offering_has_active_tos

POST /api/marketplace-offering-users/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_has_active_tos
            - New property: user_address

GET /api/marketplace-offering-users/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_has_active_tos user_address]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_has_active_tos
            - New property: user_address

PATCH /api/marketplace-offering-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_has_active_tos
            - New property: user_address

PUT /api/marketplace-offering-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_has_active_tos
            - New property: user_address

GET /api/marketplace-orders/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [error_updated_at output_updated_at]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: error_updated_at
              - New property: output_updated_at

POST /api/marketplace-orders/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: error_updated_at
            - New property: output_updated_at

GET /api/marketplace-orders/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [error_updated_at output_updated_at]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: error_updated_at
            - New property: output_updated_at

GET /api/marketplace-orders/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: profile_name
            - New property: profile_uuid
            - Deleted property: roles
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: offering_uuid
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Schemas deleted: #/components/schemas/BlankEnum
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: future_prices
                    - AdditionalProperties changed
                      - Type changed from 'number' to 'string'
                      - Format changed from 'double' to ''
                  - Modified property: minimal_price
                    - Type changed from 'number' to 'string'
                    - Format changed from 'double' to ''
                  - Modified property: prices
                    - AdditionalProperties changed
                      - Type changed from 'number' to 'string'
                      - Format changed from 'double' to ''
                  - Modified property: quotas
                    - AdditionalProperties changed
                      - Type changed from 'number' to 'integer'
                      - Format changed from 'double' to ''
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: create_orders_on_resource_project_change
                    - New property: enable_resource_projects
                    - New property: resource_projects_limits_required
                    - New property: usage_poll_interval_minutes
                    - Deleted property: keycloak_base_group
                    - Deleted property: keycloak_enabled
                    - Deleted property: keycloak_group_name_template
                    - Deleted property: keycloak_sync_frequency
                    - Deleted property: keycloak_username_label
            - Modified property: scope_name
              - Format changed from 'uuid' to ''

GET /api/marketplace-orders/{uuid}/resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: project_is_in_grace_period
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: error_updated_at
                    - New property: output_updated_at
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: offering_uuid
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Schemas deleted: #/components/schemas/BlankEnum
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: error_updated_at
                    - New property: output_updated_at

POST /api/marketplace-orders/{uuid}/set_consumer_info/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/permission from 'ORDER.APPROVE' to 'ORDER.SET_CONSUMER_INFO'

GET /api/marketplace-plans/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: future_prices
                - AdditionalProperties changed
                  - Type changed from 'number' to 'string'
                  - Format changed from 'double' to ''
              - Modified property: minimal_price
                - Type changed from 'number' to 'string'
                - Format changed from 'double' to ''
              - Modified property: prices
                - AdditionalProperties changed
                  - Type changed from 'number' to 'string'
                  - Format changed from 'double' to ''
              - Modified property: quotas
                - AdditionalProperties changed
                  - Type changed from 'number' to 'integer'
                  - Format changed from 'double' to ''

POST /api/marketplace-plans/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: future_prices
              - AdditionalProperties changed
                - Type changed from 'number' to 'string'
                - Format changed from 'double' to ''
            - Modified property: minimal_price
              - Type changed from 'number' to 'string'
              - Format changed from 'double' to ''
            - Modified property: prices
              - AdditionalProperties changed
                - Type changed from 'number' to 'string'
                - Format changed from 'double' to ''
            - Modified property: quotas
              - AdditionalProperties changed
                - Type changed from 'number' to 'integer'
                - Format changed from 'double' to ''

GET /api/marketplace-plans/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: future_prices
              - AdditionalProperties changed
                - Type changed from 'number' to 'string'
                - Format changed from 'double' to ''
            - Modified property: minimal_price
              - Type changed from 'number' to 'string'
              - Format changed from 'double' to ''
            - Modified property: prices
              - AdditionalProperties changed
                - Type changed from 'number' to 'string'
                - Format changed from 'double' to ''
            - Modified property: quotas
              - AdditionalProperties changed
                - Type changed from 'number' to 'integer'
                - Format changed from 'double' to ''

PATCH /api/marketplace-plans/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: future_prices
              - AdditionalProperties changed
                - Type changed from 'number' to 'string'
                - Format changed from 'double' to ''
            - Modified property: minimal_price
              - Type changed from 'number' to 'string'
              - Format changed from 'double' to ''
            - Modified property: prices
              - AdditionalProperties changed
                - Type changed from 'number' to 'string'
                - Format changed from 'double' to ''
            - Modified property: quotas
              - AdditionalProperties changed
                - Type changed from 'number' to 'integer'
                - Format changed from 'double' to ''

PUT /api/marketplace-plans/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: future_prices
              - AdditionalProperties changed
                - Type changed from 'number' to 'string'
                - Format changed from 'double' to ''
            - Modified property: minimal_price
              - Type changed from 'number' to 'string'
              - Format changed from 'double' to ''
            - Modified property: prices
              - AdditionalProperties changed
                - Type changed from 'number' to 'string'
                - Format changed from 'double' to ''
            - Modified property: quotas
              - AdditionalProperties changed
                - Type changed from 'number' to 'integer'
                - Format changed from 'double' to ''

GET /api/marketplace-project-estimated-cost-policies/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: customer_credit
                - Type changed from 'number' to 'string'
                - Format changed from 'double' to ''
              - Modified property: project_credit
                - Type changed from 'number' to 'string'
                - Format changed from 'double' to ''

POST /api/marketplace-project-estimated-cost-policies/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: customer_credit
              - Type changed from 'number' to 'string'
              - Format changed from 'double' to ''
            - Modified property: project_credit
              - Type changed from 'number' to 'string'
              - Format changed from 'double' to ''

GET /api/marketplace-project-estimated-cost-policies/actions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: customer_credit
              - Type changed from 'number' to 'string'
              - Format changed from 'double' to ''
            - Modified property: project_credit
              - Type changed from 'number' to 'string'
              - Format changed from 'double' to ''

GET /api/marketplace-project-estimated-cost-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: customer_credit
              - Type changed from 'number' to 'string'
              - Format changed from 'double' to ''
            - Modified property: project_credit
              - Type changed from 'number' to 'string'
              - Format changed from 'double' to ''

PATCH /api/marketplace-project-estimated-cost-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: customer_credit
              - Type changed from 'number' to 'string'
              - Format changed from 'double' to ''
            - Modified property: project_credit
              - Type changed from 'number' to 'string'
              - Format changed from 'double' to ''

PUT /api/marketplace-project-estimated-cost-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: customer_credit
              - Type changed from 'number' to 'string'
              - Format changed from 'double' to ''
            - Modified property: project_credit
              - Type changed from 'number' to 'string'
              - Format changed from 'double' to ''

GET /api/marketplace-provider-offerings/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [profile_name profile_uuid]
      - Deleted enum values: [roles]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: profile_name
              - New property: profile_uuid
              - Deleted property: roles
              - Modified property: components
                - Items changed
                  - Properties changed
                    - New property: offering_uuid
                    - Modified property: limit_period
                      - Property 'OneOf' changed
                        - Schemas deleted: #/components/schemas/BlankEnum
              - Modified property: plans
                - Items changed
                  - Properties changed
                    - Modified property: future_prices
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'string'
                        - Format changed from 'double' to ''
                    - Modified property: minimal_price
                      - Type changed from 'number' to 'string'
                      - Format changed from 'double' to ''
                    - Modified property: prices
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'string'
                        - Format changed from 'double' to ''
                    - Modified property: quotas
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'integer'
                        - Format changed from 'double' to ''
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: create_orders_on_resource_project_change
                      - New property: enable_resource_projects
                      - New property: resource_projects_limits_required
                      - New property: usage_poll_interval_minutes
                      - Deleted property: keycloak_base_group
                      - Deleted property: keycloak_enabled
                      - Deleted property: keycloak_group_name_template
                      - Deleted property: keycloak_sync_frequency
                      - Deleted property: keycloak_username_label
              - Modified property: scope_name
                - Format changed from 'uuid' to ''

POST /api/marketplace-provider-offerings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: components
            - Items changed
              - Properties changed
                - Modified property: limit_period
                  - Property 'OneOf' changed
                    - Schemas deleted: #/components/schemas/BlankEnum
          - Modified property: plugin_options
            - Properties changed
              - New property: create_orders_on_resource_project_change
              - New property: enable_resource_projects
              - New property: resource_projects_limits_required
              - New property: usage_poll_interval_minutes
              - Deleted property: keycloak_base_group
              - Deleted property: keycloak_enabled
              - Deleted property: keycloak_group_name_template
              - Deleted property: keycloak_sync_frequency
              - Deleted property: keycloak_username_label
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: components
            - Items changed
              - Properties changed
                - Modified property: limit_period
                  - Property 'OneOf' changed
                    - Schemas deleted: #/components/schemas/BlankEnum
          - Modified property: plugin_options
            - Properties changed
              - New property: create_orders_on_resource_project_change
              - New property: enable_resource_projects
              - New property: resource_projects_limits_required
              - New property: usage_poll_interval_minutes
              - Deleted property: keycloak_base_group
              - Deleted property: keycloak_enabled
              - Deleted property: keycloak_group_name_template
              - Deleted property: keycloak_sync_frequency
              - Deleted property: keycloak_username_label
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: components
            - Items changed
              - Properties changed
                - Modified property: limit_period
                  - Property 'OneOf' changed
                    - Schemas deleted: #/components/schemas/BlankEnum
          - Modified property: plugin_options
            - Properties changed
              - New property: create_orders_on_resource_project_change
              - New property: enable_resource_projects
              - New property: resource_projects_limits_required
              - New property: usage_poll_interval_minutes
              - Deleted property: keycloak_base_group
              - Deleted property: keycloak_enabled
              - Deleted property: keycloak_group_name_template
              - Deleted property: keycloak_sync_frequency
              - Deleted property: keycloak_username_label
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: profile_name
            - New property: profile_uuid
            - Deleted property: roles
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: offering_uuid
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Schemas deleted: #/components/schemas/BlankEnum
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: future_prices
                    - AdditionalProperties changed
                      - Type changed from 'number' to 'string'
                      - Format changed from 'double' to ''
                  - Modified property: minimal_price
                    - Type changed from 'number' to 'string'
                    - Format changed from 'double' to ''
                  - Modified property: prices
                    - AdditionalProperties changed
                      - Type changed from 'number' to 'string'
                      - Format changed from 'double' to ''
                  - Modified property: quotas
                    - AdditionalProperties changed
                      - Type changed from 'number' to 'integer'
                      - Format changed from 'double' to ''
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: create_orders_on_resource_project_change
                    - New property: enable_resource_projects
                    - New property: resource_projects_limits_required
                    - New property: usage_poll_interval_minutes
                    - Deleted property: keycloak_base_group
                    - Deleted property: keycloak_enabled
                    - Deleted property: keycloak_group_name_template
                    - Deleted property: keycloak_sync_frequency
                    - Deleted property: keycloak_username_label
            - Modified property: scope_name
              - Format changed from 'uuid' to ''

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
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - Modified property: limit_period
                          - MinLength changed from 1 to 0

GET /api/marketplace-provider-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [profile_name profile_uuid]
      - Deleted enum values: [roles]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: profile_name
            - New property: profile_uuid
            - Deleted property: roles
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: offering_uuid
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Schemas deleted: #/components/schemas/BlankEnum
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: future_prices
                    - AdditionalProperties changed
                      - Type changed from 'number' to 'string'
                      - Format changed from 'double' to ''
                  - Modified property: minimal_price
                    - Type changed from 'number' to 'string'
                    - Format changed from 'double' to ''
                  - Modified property: prices
                    - AdditionalProperties changed
                      - Type changed from 'number' to 'string'
                      - Format changed from 'double' to ''
                  - Modified property: quotas
                    - AdditionalProperties changed
                      - Type changed from 'number' to 'integer'
                      - Format changed from 'double' to ''
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: create_orders_on_resource_project_change
                    - New property: enable_resource_projects
                    - New property: resource_projects_limits_required
                    - New property: usage_poll_interval_minutes
                    - Deleted property: keycloak_base_group
                    - Deleted property: keycloak_enabled
                    - Deleted property: keycloak_group_name_template
                    - Deleted property: keycloak_sync_frequency
                    - Deleted property: keycloak_username_label
            - Modified property: scope_name
              - Format changed from 'uuid' to ''

POST /api/marketplace-provider-offerings/{uuid}/create_offering_component/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: limit_period
            - Property 'OneOf' changed
              - Schemas deleted: #/components/schemas/BlankEnum

POST /api/marketplace-provider-offerings/{uuid}/import_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: project_is_in_grace_period
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: error_updated_at
                    - New property: output_updated_at
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: offering_uuid
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Schemas deleted: #/components/schemas/BlankEnum
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: error_updated_at
                    - New property: output_updated_at

GET /api/marketplace-provider-offerings/{uuid}/list_course_accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: project_end_date
                - Nullable changed from false to true
              - Modified property: project_start_date
                - Nullable changed from false to true

GET /api/marketplace-provider-offerings/{uuid}/list_customer_projects/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [affiliated_organizations science_domain_code science_domain_name science_domain_uuid science_sub_domain science_sub_domain_code science_sub_domain_name]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: affiliated_organizations
              - New property: science_domain_code
              - New property: science_domain_name
              - New property: science_domain_uuid
              - New property: science_sub_domain
              - New property: science_sub_domain_code
              - New property: science_sub_domain_name

GET /api/marketplace-provider-offerings/{uuid}/list_customer_users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [address]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: address
              - Modified property: permissions
                - Items changed
                  - Properties changed
                    - New property: resource_uuid

POST /api/marketplace-provider-offerings/{uuid}/move_offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: profile_name
            - New property: profile_uuid
            - Deleted property: roles
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: offering_uuid
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Schemas deleted: #/components/schemas/BlankEnum
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: future_prices
                    - AdditionalProperties changed
                      - Type changed from 'number' to 'string'
                      - Format changed from 'double' to ''
                  - Modified property: minimal_price
                    - Type changed from 'number' to 'string'
                    - Format changed from 'double' to ''
                  - Modified property: prices
                    - AdditionalProperties changed
                      - Type changed from 'number' to 'string'
                      - Format changed from 'double' to ''
                  - Modified property: quotas
                    - AdditionalProperties changed
                      - Type changed from 'number' to 'integer'
                      - Format changed from 'double' to ''
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: create_orders_on_resource_project_change
                    - New property: enable_resource_projects
                    - New property: resource_projects_limits_required
                    - New property: usage_poll_interval_minutes
                    - Deleted property: keycloak_base_group
                    - Deleted property: keycloak_enabled
                    - Deleted property: keycloak_group_name_template
                    - Deleted property: keycloak_sync_frequency
                    - Deleted property: keycloak_username_label
            - Modified property: scope_name
              - Format changed from 'uuid' to ''

GET /api/marketplace-provider-offerings/{uuid}/orders/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [error_updated_at output_updated_at]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: error_updated_at
              - New property: output_updated_at

GET /api/marketplace-provider-offerings/{uuid}/orders/{order_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: error_updated_at
            - New property: output_updated_at

PATCH /api/marketplace-provider-offerings/{uuid}/update-user-attribute-config/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: expose_address
          - New property: expose_registration_method
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: expose_address
            - New property: expose_registration_method
            - Modified property: exposed_fields
              - Description changed from 'Return list of field names currently configured for exposure.' to ''

POST /api/marketplace-provider-offerings/{uuid}/update-user-attribute-config/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: expose_address
          - New property: expose_registration_method
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: expose_address
            - New property: expose_registration_method
            - Modified property: exposed_fields
              - Description changed from 'Return list of field names currently configured for exposure.' to ''

PUT /api/marketplace-provider-offerings/{uuid}/update-user-attribute-config/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: expose_address
          - New property: expose_registration_method
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: expose_address
            - New property: expose_registration_method
            - Modified property: exposed_fields
              - Description changed from 'Return list of field names currently configured for exposure.' to ''

POST /api/marketplace-provider-offerings/{uuid}/update_integration/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: create_orders_on_resource_project_change
              - New property: enable_resource_projects
              - New property: resource_projects_limits_required
              - New property: usage_poll_interval_minutes
              - Deleted property: keycloak_base_group
              - Deleted property: keycloak_enabled
              - Deleted property: keycloak_group_name_template
              - Deleted property: keycloak_sync_frequency
              - Deleted property: keycloak_username_label

POST /api/marketplace-provider-offerings/{uuid}/update_offering_component/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: limit_period
            - Property 'OneOf' changed
              - Schemas deleted: #/components/schemas/BlankEnum

GET /api/marketplace-provider-offerings/{uuid}/user-attribute-config/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: expose_address
            - New property: expose_registration_method
            - Modified property: exposed_fields
              - Description changed from 'Return list of field names currently configured for exposure.' to ''

GET /api/marketplace-provider-offerings/{uuid}/user_has_resource_access/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [profile_name profile_uuid]
      - Deleted enum values: [roles]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: profile_name
            - New property: profile_uuid
            - Deleted property: roles
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: offering_uuid
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Schemas deleted: #/components/schemas/BlankEnum
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: future_prices
                    - AdditionalProperties changed
                      - Type changed from 'number' to 'string'
                      - Format changed from 'double' to ''
                  - Modified property: minimal_price
                    - Type changed from 'number' to 'string'
                    - Format changed from 'double' to ''
                  - Modified property: prices
                    - AdditionalProperties changed
                      - Type changed from 'number' to 'string'
                      - Format changed from 'double' to ''
                  - Modified property: quotas
                    - AdditionalProperties changed
                      - Type changed from 'number' to 'integer'
                      - Format changed from 'double' to ''
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: create_orders_on_resource_project_change
                    - New property: enable_resource_projects
                    - New property: resource_projects_limits_required
                    - New property: usage_poll_interval_minutes
                    - Deleted property: keycloak_base_group
                    - Deleted property: keycloak_enabled
                    - Deleted property: keycloak_group_name_template
                    - Deleted property: keycloak_sync_frequency
                    - Deleted property: keycloak_username_label
            - Modified property: scope_name
              - Format changed from 'uuid' to ''

GET /api/marketplace-provider-resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [project_is_in_grace_period]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: project_is_in_grace_period
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: error_updated_at
                      - New property: output_updated_at
              - Modified property: offering_components
                - Items changed
                  - Properties changed
                    - New property: offering_uuid
                    - Modified property: limit_period
                      - Property 'OneOf' changed
                        - Schemas deleted: #/components/schemas/BlankEnum
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: error_updated_at
                      - New property: output_updated_at

GET /api/marketplace-provider-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [project_is_in_grace_period]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: project_is_in_grace_period
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: error_updated_at
                    - New property: output_updated_at
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: offering_uuid
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Schemas deleted: #/components/schemas/BlankEnum
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: error_updated_at
                    - New property: output_updated_at

POST /api/marketplace-provider-resources/{uuid}/move_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: project_is_in_grace_period
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: error_updated_at
                    - New property: output_updated_at
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: offering_uuid
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Schemas deleted: #/components/schemas/BlankEnum
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: error_updated_at
                    - New property: output_updated_at

GET /api/marketplace-provider-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: profile_name
            - New property: profile_uuid
            - Deleted property: roles
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: offering_uuid
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Schemas deleted: #/components/schemas/BlankEnum
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: future_prices
                    - AdditionalProperties changed
                      - Type changed from 'number' to 'string'
                      - Format changed from 'double' to ''
                  - Modified property: minimal_price
                    - Type changed from 'number' to 'string'
                    - Format changed from 'double' to ''
                  - Modified property: prices
                    - AdditionalProperties changed
                      - Type changed from 'number' to 'string'
                      - Format changed from 'double' to ''
                  - Modified property: quotas
                    - AdditionalProperties changed
                      - Type changed from 'number' to 'integer'
                      - Format changed from 'double' to ''
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: create_orders_on_resource_project_change
                    - New property: enable_resource_projects
                    - New property: resource_projects_limits_required
                    - New property: usage_poll_interval_minutes
                    - Deleted property: keycloak_base_group
                    - Deleted property: keycloak_enabled
                    - Deleted property: keycloak_group_name_template
                    - Deleted property: keycloak_sync_frequency
                    - Deleted property: keycloak_username_label
            - Modified property: scope_name
              - Format changed from 'uuid' to ''

POST /api/marketplace-provider-resources/{uuid}/restore/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: project_is_in_grace_period
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: error_updated_at
                    - New property: output_updated_at
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: offering_uuid
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Schemas deleted: #/components/schemas/BlankEnum
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: error_updated_at
                    - New property: output_updated_at

GET /api/marketplace-provider-resources/{uuid}/team/

- New query param: has_consent

GET /api/marketplace-public-offerings/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [profile_name profile_uuid]
      - Deleted enum values: [roles]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: profile_name
              - New property: profile_uuid
              - Deleted property: roles
              - Modified property: components
                - Items changed
                  - Properties changed
                    - New property: offering_uuid
                    - Modified property: limit_period
                      - Property 'OneOf' changed
                        - Schemas deleted: #/components/schemas/BlankEnum
              - Modified property: plans
                - Items changed
                  - Properties changed
                    - Modified property: future_prices
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'string'
                        - Format changed from 'double' to ''
                    - Modified property: minimal_price
                      - Type changed from 'number' to 'string'
                      - Format changed from 'double' to ''
                    - Modified property: prices
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'string'
                        - Format changed from 'double' to ''
                    - Modified property: quotas
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'integer'
                        - Format changed from 'double' to ''
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: create_orders_on_resource_project_change
                      - New property: enable_resource_projects
                      - New property: resource_projects_limits_required
                      - New property: usage_poll_interval_minutes
                      - Deleted property: keycloak_base_group
                      - Deleted property: keycloak_enabled
                      - Deleted property: keycloak_group_name_template
                      - Deleted property: keycloak_sync_frequency
                      - Deleted property: keycloak_username_label
              - Modified property: scope_name
                - Format changed from 'uuid' to ''

GET /api/marketplace-public-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [profile_name profile_uuid]
      - Deleted enum values: [roles]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: profile_name
            - New property: profile_uuid
            - Deleted property: roles
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: offering_uuid
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Schemas deleted: #/components/schemas/BlankEnum
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: future_prices
                    - AdditionalProperties changed
                      - Type changed from 'number' to 'string'
                      - Format changed from 'double' to ''
                  - Modified property: minimal_price
                    - Type changed from 'number' to 'string'
                    - Format changed from 'double' to ''
                  - Modified property: prices
                    - AdditionalProperties changed
                      - Type changed from 'number' to 'string'
                      - Format changed from 'double' to ''
                  - Modified property: quotas
                    - AdditionalProperties changed
                      - Type changed from 'number' to 'integer'
                      - Format changed from 'double' to ''
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: create_orders_on_resource_project_change
                    - New property: enable_resource_projects
                    - New property: resource_projects_limits_required
                    - New property: usage_poll_interval_minutes
                    - Deleted property: keycloak_base_group
                    - Deleted property: keycloak_enabled
                    - Deleted property: keycloak_group_name_template
                    - Deleted property: keycloak_sync_frequency
                    - Deleted property: keycloak_username_label
            - Modified property: scope_name
              - Format changed from 'uuid' to ''

GET /api/marketplace-public-offerings/{uuid}/plans/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: future_prices
                - AdditionalProperties changed
                  - Type changed from 'number' to 'string'
                  - Format changed from 'double' to ''
              - Modified property: minimal_price
                - Type changed from 'number' to 'string'
                - Format changed from 'double' to ''
              - Modified property: prices
                - AdditionalProperties changed
                  - Type changed from 'number' to 'string'
                  - Format changed from 'double' to ''
              - Modified property: quotas
                - AdditionalProperties changed
                  - Type changed from 'number' to 'integer'
                  - Format changed from 'double' to ''

GET /api/marketplace-public-offerings/{uuid}/plans/{plan_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: future_prices
              - AdditionalProperties changed
                - Type changed from 'number' to 'string'
                - Format changed from 'double' to ''
            - Modified property: minimal_price
              - Type changed from 'number' to 'string'
              - Format changed from 'double' to ''
            - Modified property: prices
              - AdditionalProperties changed
                - Type changed from 'number' to 'string'
                - Format changed from 'double' to ''
            - Modified property: quotas
              - AdditionalProperties changed
                - Type changed from 'number' to 'integer'
                - Format changed from 'double' to ''

GET /api/marketplace-resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [project_is_in_grace_period]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: project_is_in_grace_period
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: error_updated_at
                      - New property: output_updated_at
              - Modified property: offering_components
                - Items changed
                  - Properties changed
                    - New property: offering_uuid
                    - Modified property: limit_period
                      - Property 'OneOf' changed
                        - Schemas deleted: #/components/schemas/BlankEnum
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: error_updated_at
                      - New property: output_updated_at

GET /api/marketplace-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [project_is_in_grace_period]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: project_is_in_grace_period
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: error_updated_at
                    - New property: output_updated_at
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: offering_uuid
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Schemas deleted: #/components/schemas/BlankEnum
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: error_updated_at
                    - New property: output_updated_at

POST /api/marketplace-resources/{uuid}/move_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: project_is_in_grace_period
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: error_updated_at
                    - New property: output_updated_at
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: offering_uuid
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Schemas deleted: #/components/schemas/BlankEnum
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: error_updated_at
                    - New property: output_updated_at

GET /api/marketplace-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: profile_name
            - New property: profile_uuid
            - Deleted property: roles
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: offering_uuid
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Schemas deleted: #/components/schemas/BlankEnum
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: future_prices
                    - AdditionalProperties changed
                      - Type changed from 'number' to 'string'
                      - Format changed from 'double' to ''
                  - Modified property: minimal_price
                    - Type changed from 'number' to 'string'
                    - Format changed from 'double' to ''
                  - Modified property: prices
                    - AdditionalProperties changed
                      - Type changed from 'number' to 'string'
                      - Format changed from 'double' to ''
                  - Modified property: quotas
                    - AdditionalProperties changed
                      - Type changed from 'number' to 'integer'
                      - Format changed from 'double' to ''
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: create_orders_on_resource_project_change
                    - New property: enable_resource_projects
                    - New property: resource_projects_limits_required
                    - New property: usage_poll_interval_minutes
                    - Deleted property: keycloak_base_group
                    - Deleted property: keycloak_enabled
                    - Deleted property: keycloak_group_name_template
                    - Deleted property: keycloak_sync_frequency
                    - Deleted property: keycloak_username_label
            - Modified property: scope_name
              - Format changed from 'uuid' to ''

POST /api/marketplace-resources/{uuid}/restore/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: project_is_in_grace_period
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: error_updated_at
                    - New property: output_updated_at
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: offering_uuid
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Schemas deleted: #/components/schemas/BlankEnum
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: error_updated_at
                    - New property: output_updated_at

GET /api/marketplace-resources/{uuid}/team/

- New query param: has_consent

POST /api/marketplace-resources/{uuid}/update_limits/

- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: attachment

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
                      - New property: create_orders_on_resource_project_change
                      - New property: enable_resource_projects
                      - New property: resource_projects_limits_required
                      - New property: usage_poll_interval_minutes
                      - Deleted property: keycloak_base_group
                      - Deleted property: keycloak_enabled
                      - Deleted property: keycloak_group_name_template
                      - Deleted property: keycloak_sync_frequency
                      - Deleted property: keycloak_username_label

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
                    - New property: create_orders_on_resource_project_change
                    - New property: enable_resource_projects
                    - New property: resource_projects_limits_required
                    - New property: usage_poll_interval_minutes
                    - Deleted property: keycloak_base_group
                    - Deleted property: keycloak_enabled
                    - Deleted property: keycloak_group_name_template
                    - Deleted property: keycloak_sync_frequency
                    - Deleted property: keycloak_username_label

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
                    - New property: create_orders_on_resource_project_change
                    - New property: enable_resource_projects
                    - New property: resource_projects_limits_required
                    - New property: usage_poll_interval_minutes
                    - Deleted property: keycloak_base_group
                    - Deleted property: keycloak_enabled
                    - Deleted property: keycloak_group_name_template
                    - Deleted property: keycloak_sync_frequency
                    - Deleted property: keycloak_username_label

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
                    - New property: create_orders_on_resource_project_change
                    - New property: enable_resource_projects
                    - New property: resource_projects_limits_required
                    - New property: usage_poll_interval_minutes
                    - Deleted property: keycloak_base_group
                    - Deleted property: keycloak_enabled
                    - Deleted property: keycloak_group_name_template
                    - Deleted property: keycloak_sync_frequency
                    - Deleted property: keycloak_username_label

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
                    - New property: create_orders_on_resource_project_change
                    - New property: enable_resource_projects
                    - New property: resource_projects_limits_required
                    - New property: usage_poll_interval_minutes
                    - Deleted property: keycloak_base_group
                    - Deleted property: keycloak_enabled
                    - Deleted property: keycloak_group_name_template
                    - Deleted property: keycloak_sync_frequency
                    - Deleted property: keycloak_username_label

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
                    - New property: create_orders_on_resource_project_change
                    - New property: enable_resource_projects
                    - New property: resource_projects_limits_required
                    - New property: usage_poll_interval_minutes
                    - Deleted property: keycloak_base_group
                    - Deleted property: keycloak_enabled
                    - Deleted property: keycloak_group_name_template
                    - Deleted property: keycloak_sync_frequency
                    - Deleted property: keycloak_username_label

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
                    - New property: create_orders_on_resource_project_change
                    - New property: enable_resource_projects
                    - New property: resource_projects_limits_required
                    - New property: usage_poll_interval_minutes
                    - Deleted property: keycloak_base_group
                    - Deleted property: keycloak_enabled
                    - Deleted property: keycloak_group_name_template
                    - Deleted property: keycloak_sync_frequency
                    - Deleted property: keycloak_username_label

POST /api/marketplace-script-dry-run/{uuid}/async_run/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: profile_name
            - New property: profile_uuid
            - Deleted property: roles
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: offering_uuid
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Schemas deleted: #/components/schemas/BlankEnum
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: future_prices
                    - AdditionalProperties changed
                      - Type changed from 'number' to 'string'
                      - Format changed from 'double' to ''
                  - Modified property: minimal_price
                    - Type changed from 'number' to 'string'
                    - Format changed from 'double' to ''
                  - Modified property: prices
                    - AdditionalProperties changed
                      - Type changed from 'number' to 'string'
                      - Format changed from 'double' to ''
                  - Modified property: quotas
                    - AdditionalProperties changed
                      - Type changed from 'number' to 'integer'
                      - Format changed from 'double' to ''
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: create_orders_on_resource_project_change
                    - New property: enable_resource_projects
                    - New property: resource_projects_limits_required
                    - New property: usage_poll_interval_minutes
                    - Deleted property: keycloak_base_group
                    - Deleted property: keycloak_enabled
                    - Deleted property: keycloak_group_name_template
                    - Deleted property: keycloak_sync_frequency
                    - Deleted property: keycloak_username_label
            - Modified property: scope_name
              - Format changed from 'uuid' to ''

POST /api/marketplace-script-dry-run/{uuid}/run/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: profile_name
            - New property: profile_uuid
            - Deleted property: roles
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: offering_uuid
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Schemas deleted: #/components/schemas/BlankEnum
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: future_prices
                    - AdditionalProperties changed
                      - Type changed from 'number' to 'string'
                      - Format changed from 'double' to ''
                  - Modified property: minimal_price
                    - Type changed from 'number' to 'string'
                    - Format changed from 'double' to ''
                  - Modified property: prices
                    - AdditionalProperties changed
                      - Type changed from 'number' to 'string'
                      - Format changed from 'double' to ''
                  - Modified property: quotas
                    - AdditionalProperties changed
                      - Type changed from 'number' to 'integer'
                      - Format changed from 'double' to ''
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: create_orders_on_resource_project_change
                    - New property: enable_resource_projects
                    - New property: resource_projects_limits_required
                    - New property: usage_poll_interval_minutes
                    - Deleted property: keycloak_base_group
                    - Deleted property: keycloak_enabled
                    - Deleted property: keycloak_group_name_template
                    - Deleted property: keycloak_sync_frequency
                    - Deleted property: keycloak_username_label
            - Modified property: scope_name
              - Format changed from 'uuid' to ''

GET /api/marketplace-service-providers/{service_provider_uuid}/course_accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: project_end_date
                - Nullable changed from false to true
              - Modified property: project_start_date
                - Nullable changed from false to true

GET /api/marketplace-service-providers/{service_provider_uuid}/customer_projects/

- New query param: affiliated_organization_name
- New query param: affiliated_organization_uuid
- New query param: has_affiliated_organization
- New query param: science_domain_uuid
- New query param: science_sub_domain_uuid

GET /api/marketplace-service-providers/{service_provider_uuid}/keys/

- Deleted query param: uuid

GET /api/marketplace-service-providers/{service_provider_uuid}/offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: components
                - Items changed
                  - Properties changed
                    - New property: offering_uuid
                    - Modified property: limit_period
                      - Property 'OneOf' changed
                        - Schemas deleted: #/components/schemas/BlankEnum
              - Modified property: plans
                - Items changed
                  - Properties changed
                    - Modified property: future_prices
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'string'
                        - Format changed from 'double' to ''
                    - Modified property: minimal_price
                      - Type changed from 'number' to 'string'
                      - Format changed from 'double' to ''
                    - Modified property: prices
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'string'
                        - Format changed from 'double' to ''
                    - Modified property: quotas
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'integer'
                        - Format changed from 'double' to ''

GET /api/marketplace-service-providers/{service_provider_uuid}/projects/

- New query param: affiliated_organization_name
- New query param: affiliated_organization_uuid
- New query param: has_affiliated_organization
- New query param: science_domain_uuid
- New query param: science_sub_domain_uuid
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [affiliated_organizations science_domain_code science_domain_name science_domain_uuid science_sub_domain science_sub_domain_code science_sub_domain_name]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: affiliated_organizations
              - New property: science_domain_code
              - New property: science_domain_name
              - New property: science_domain_uuid
              - New property: science_sub_domain
              - New property: science_sub_domain_code
              - New property: science_sub_domain_name

GET /api/marketplace-service-providers/{service_provider_uuid}/users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [address]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: address

POST /api/marketplace-software-catalogs/{uuid}/update_catalog/

- Request body changed

GET /api/marketplace-software-packages/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: extensions
                - Items changed
                  - Required changed
                    - New required property: versions
                  - Properties changed
                    - New property: versions
              - Modified property: parent_softwares
                - Items changed
                  - Required changed
                    - New required property: versions
                  - Properties changed
                    - New property: versions

POST /api/marketplace-software-packages/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: extensions
              - Items changed
                - Required changed
                  - New required property: versions
                - Properties changed
                  - New property: versions
            - Modified property: parent_softwares
              - Items changed
                - Required changed
                  - New required property: versions
                - Properties changed
                  - New property: versions

GET /api/marketplace-software-packages/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: extensions
              - Items changed
                - Required changed
                  - New required property: versions
                - Properties changed
                  - New property: versions
            - Modified property: parent_softwares
              - Items changed
                - Required changed
                  - New required property: versions
                - Properties changed
                  - New property: versions

PATCH /api/marketplace-software-packages/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: extensions
              - Items changed
                - Required changed
                  - New required property: versions
                - Properties changed
                  - New property: versions
            - Modified property: parent_softwares
              - Items changed
                - Required changed
                  - New required property: versions
                - Properties changed
                  - New property: versions

PUT /api/marketplace-software-packages/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: extensions
              - Items changed
                - Required changed
                  - New required property: versions
                - Properties changed
                  - New property: versions
            - Modified property: parent_softwares
              - Items changed
                - Required changed
                  - New required property: versions
                - Properties changed
                  - New property: versions

GET /api/marketplace-stats/count_active_resources_grouped_by_offering/

- Deleted query param: limit

HEAD /api/marketplace-stats/count_active_resources_grouped_by_offering/

- Deleted query param: limit

GET /api/marketplace-stats/resources_missing_usage/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: created
                - Description changed from 'Creation date of the resource' to ''
                - ReadOnly changed from false to true
              - Modified property: customer_name
                - Description changed from 'Name of the customer organization' to ''
                - ReadOnly changed from false to true
              - Modified property: customer_uuid
                - Description changed from 'UUID of the customer organization' to ''
                - ReadOnly changed from false to true
              - Modified property: days_since_last_report
                - ReadOnly changed from false to true
              - Modified property: name
                - Description changed from 'Name of the resource' to ''
                - MaxLength changed from null to 150
              - Modified property: offering_name
                - Description changed from 'Name of the offering' to ''
                - ReadOnly changed from false to true
              - Modified property: offering_uuid
                - Description changed from 'UUID of the offering' to ''
                - ReadOnly changed from false to true
              - Modified property: project_name
                - Description changed from 'Name of the project' to ''
                - ReadOnly changed from false to true
              - Modified property: project_uuid
                - Description changed from 'UUID of the project' to ''
                - ReadOnly changed from false to true
              - Modified property: provider_name
                - Description changed from 'Name of the service provider' to ''
                - ReadOnly changed from false to true
              - Modified property: provider_uuid
                - Description changed from 'UUID of the service provider' to ''
                - ReadOnly changed from false to true
              - Modified property: state
                - Description changed from 'Current state of the resource' to ''
                - ReadOnly changed from false to true
              - Modified property: uuid
                - Description changed from 'UUID of the resource' to ''
                - ReadOnly changed from false to true

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
                  - New enum values: [chat_feedback_submitted]
                  - Deleted enum values: [marketplace_offering_role_created marketplace_offering_role_deleted marketplace_offering_role_updated marketplace_resource_user_created marketplace_resource_user_deleted]

GET /api/metadata/permissions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: permission_map
              - AdditionalProperties changed
                - New enum values: [ORDER.CREATE ORDER.SET_CONSUMER_INFO RESOURCE.CREATE_PERMISSION RESOURCE.UPDATE_PERMISSION RESOURCE.DELETE_PERMISSION RESOURCE_PROJECT.CREATE_PERMISSION RESOURCE_PROJECT.UPDATE_PERMISSION RESOURCE_PROJECT.DELETE_PERMISSION OPENSTACK_ROUTER.MANAGE_GATEWAY]
            - Modified property: permissions
              - AdditionalProperties changed
                - New enum values: [ORDER.CREATE ORDER.SET_CONSUMER_INFO RESOURCE.CREATE_PERMISSION RESOURCE.UPDATE_PERMISSION RESOURCE.DELETE_PERMISSION RESOURCE_PROJECT.CREATE_PERMISSION RESOURCE_PROJECT.UPDATE_PERMISSION RESOURCE_PROJECT.DELETE_PERMISSION OPENSTACK_ROUTER.MANAGE_GATEWAY]
            - Modified property: roles
              - AdditionalProperties changed
                - New enum values: [CUSTOMER.READER]

POST /api/onboarding-verifications/{uuid}/create_customer/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: project_slug_template

GET /api/openportal-allocations/

- Deleted query param: uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''

HEAD /api/openportal-allocations/

- Deleted query param: uuid

POST /api/openportal-allocations/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/openportal-allocations/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PATCH /api/openportal-allocations/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PUT /api/openportal-allocations/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/openportal-managed-projects/

- New query param: o
- New query param: query
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: project_data
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/BasicProject
                  - Schemas deleted: #/components/schemas/Project
              - Modified property: project_template_data
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/ProjectTemplate
                    - Properties changed
                      - Modified property: customer_data
                        - Property 'AllOf' changed
                          - Schemas added: #/components/schemas/BasicCustomer
                          - Schemas deleted: #/components/schemas/Customer
                      - Modified property: offerings_data
                        - Items changed
                          - Required changed
                            - New required property: name
                            - New required property: uuid
                          - Properties changed
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
                            - Deleted property: project
                            - Deleted property: project_name
                            - Deleted property: project_uuid
                            - Deleted property: quotas
                            - Deleted property: resource_options
                            - Deleted property: roles
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
                            - Deleted property: vendor_details
                      - Modified property: provider_data
                        - Property 'AllOf' changed
                          - Schemas added: #/components/schemas/BasicCustomer
                          - Schemas deleted: #/components/schemas/Customer

HEAD /api/openportal-managed-projects/

- New query param: o
- New query param: query

GET /api/openportal-managed-projects/{identifier}/{destination}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: project_data
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/BasicProject
                - Schemas deleted: #/components/schemas/Project
            - Modified property: project_template_data
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ProjectTemplate
                  - Properties changed
                    - Modified property: customer_data
                      - Property 'AllOf' changed
                        - Schemas added: #/components/schemas/BasicCustomer
                        - Schemas deleted: #/components/schemas/Customer
                    - Modified property: offerings_data
                      - Items changed
                        - Required changed
                          - New required property: name
                          - New required property: uuid
                        - Properties changed
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
                          - Deleted property: project
                          - Deleted property: project_name
                          - Deleted property: project_uuid
                          - Deleted property: quotas
                          - Deleted property: resource_options
                          - Deleted property: roles
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
                          - Deleted property: vendor_details
                    - Modified property: provider_data
                      - Property 'AllOf' changed
                        - Schemas added: #/components/schemas/BasicCustomer
                        - Schemas deleted: #/components/schemas/Customer

GET /api/openportal-project-template/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: customer_data
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/BasicCustomer
                  - Schemas deleted: #/components/schemas/Customer
              - Modified property: offerings_data
                - Items changed
                  - Required changed
                    - New required property: name
                    - New required property: uuid
                  - Properties changed
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
                    - Deleted property: project
                    - Deleted property: project_name
                    - Deleted property: project_uuid
                    - Deleted property: quotas
                    - Deleted property: resource_options
                    - Deleted property: roles
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
                    - Deleted property: vendor_details
              - Modified property: provider_data
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/BasicCustomer
                  - Schemas deleted: #/components/schemas/Customer

POST /api/openportal-project-template/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: customer_data
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/BasicCustomer
                - Schemas deleted: #/components/schemas/Customer
            - Modified property: offerings_data
              - Items changed
                - Required changed
                  - New required property: name
                  - New required property: uuid
                - Properties changed
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
                  - Deleted property: project
                  - Deleted property: project_name
                  - Deleted property: project_uuid
                  - Deleted property: quotas
                  - Deleted property: resource_options
                  - Deleted property: roles
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
                  - Deleted property: vendor_details
            - Modified property: provider_data
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/BasicCustomer
                - Schemas deleted: #/components/schemas/Customer

GET /api/openportal-project-template/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: customer_data
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/BasicCustomer
                - Schemas deleted: #/components/schemas/Customer
            - Modified property: offerings_data
              - Items changed
                - Required changed
                  - New required property: name
                  - New required property: uuid
                - Properties changed
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
                  - Deleted property: project
                  - Deleted property: project_name
                  - Deleted property: project_uuid
                  - Deleted property: quotas
                  - Deleted property: resource_options
                  - Deleted property: roles
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
                  - Deleted property: vendor_details
            - Modified property: provider_data
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/BasicCustomer
                - Schemas deleted: #/components/schemas/Customer

PATCH /api/openportal-project-template/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: customer_data
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/BasicCustomer
                - Schemas deleted: #/components/schemas/Customer
            - Modified property: offerings_data
              - Items changed
                - Required changed
                  - New required property: name
                  - New required property: uuid
                - Properties changed
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
                  - Deleted property: project
                  - Deleted property: project_name
                  - Deleted property: project_uuid
                  - Deleted property: quotas
                  - Deleted property: resource_options
                  - Deleted property: roles
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
                  - Deleted property: vendor_details
            - Modified property: provider_data
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/BasicCustomer
                - Schemas deleted: #/components/schemas/Customer

PUT /api/openportal-project-template/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: customer_data
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/BasicCustomer
                - Schemas deleted: #/components/schemas/Customer
            - Modified property: offerings_data
              - Items changed
                - Required changed
                  - New required property: name
                  - New required property: uuid
                - Properties changed
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
                  - Deleted property: project
                  - Deleted property: project_name
                  - Deleted property: project_uuid
                  - Deleted property: quotas
                  - Deleted property: resource_options
                  - Deleted property: roles
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
                  - Deleted property: vendor_details
            - Modified property: provider_data
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/BasicCustomer
                - Schemas deleted: #/components/schemas/Customer

GET /api/openportal-remote-allocations/

- Deleted query param: uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''

HEAD /api/openportal-remote-allocations/

- Deleted query param: uuid

POST /api/openportal-remote-allocations/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/openportal-remote-allocations/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PATCH /api/openportal-remote-allocations/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PUT /api/openportal-remote-allocations/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/openportal-unmanaged-projects/

- New query param: affiliated_organization_name
- New query param: affiliated_organization_uuid
- New query param: has_affiliated_organization
- New query param: science_domain_uuid
- New query param: science_sub_domain_uuid
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [affiliated_organizations science_domain_code science_domain_name science_domain_uuid science_sub_domain science_sub_domain_code science_sub_domain_name]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: affiliated_organizations
              - New property: science_domain_code
              - New property: science_domain_name
              - New property: science_domain_uuid
              - New property: science_sub_domain
              - New property: science_sub_domain_code
              - New property: science_sub_domain_name

HEAD /api/openportal-unmanaged-projects/

- New query param: affiliated_organization_name
- New query param: affiliated_organization_uuid
- New query param: has_affiliated_organization
- New query param: science_domain_uuid
- New query param: science_sub_domain_uuid

POST /api/openportal-unmanaged-projects/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: science_sub_domain
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: science_sub_domain
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: science_sub_domain
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: affiliated_organizations
            - New property: science_domain_code
            - New property: science_domain_name
            - New property: science_domain_uuid
            - New property: science_sub_domain
            - New property: science_sub_domain_code
            - New property: science_sub_domain_name

GET /api/openportal-unmanaged-projects/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [affiliated_organizations science_domain_code science_domain_name science_domain_uuid science_sub_domain science_sub_domain_code science_sub_domain_name]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: affiliated_organizations
            - New property: science_domain_code
            - New property: science_domain_name
            - New property: science_domain_uuid
            - New property: science_sub_domain
            - New property: science_sub_domain_code
            - New property: science_sub_domain_name

PATCH /api/openportal-unmanaged-projects/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: science_sub_domain
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: science_sub_domain
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: science_sub_domain
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: affiliated_organizations
            - New property: science_domain_code
            - New property: science_domain_name
            - New property: science_domain_uuid
            - New property: science_sub_domain
            - New property: science_sub_domain_code
            - New property: science_sub_domain_name

PUT /api/openportal-unmanaged-projects/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: science_sub_domain
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: science_sub_domain
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: science_sub_domain
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: affiliated_organizations
            - New property: science_domain_code
            - New property: science_domain_name
            - New property: science_domain_uuid
            - New property: science_sub_domain
            - New property: science_sub_domain_code
            - New property: science_sub_domain_name

POST /api/openportal-unmanaged-projects/{uuid}/move_project/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: affiliated_organizations
            - New property: science_domain_code
            - New property: science_domain_name
            - New property: science_domain_uuid
            - New property: science_sub_domain
            - New property: science_sub_domain_code
            - New property: science_sub_domain_name

POST /api/openportal-unmanaged-projects/{uuid}/recover/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: affiliated_organizations
            - New property: science_domain_code
            - New property: science_domain_name
            - New property: science_domain_uuid
            - New property: science_sub_domain
            - New property: science_sub_domain_code
            - New property: science_sub_domain_name

GET /api/openstack-backups/

- Deleted query param: uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''
              - Modified property: instance_ports
                - Items changed
                  - Properties changed
                    - Modified property: security_groups
                      - Items changed
                        - Properties changed
                          - Modified property: access_url
                            - Property 'OneOf' changed
                              - Schemas added: subschema #1, subschema #2
                            - Type changed from 'string' to ''
              - Modified property: restorations
                - Items changed
                  - Properties changed
                    - Modified property: ports
                      - Items changed
                        - Properties changed
                          - Modified property: security_groups
                            - Items changed
                              - Properties changed
                                - Modified property: access_url
                                  - Property 'OneOf' changed
                                    - Schemas added: subschema #1, subschema #2
                                  - Type changed from 'string' to ''

HEAD /api/openstack-backups/

- Deleted query param: uuid

GET /api/openstack-backups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: access_url
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: security_groups
                          - Items changed
                            - Properties changed
                              - Modified property: access_url
                                - Property 'OneOf' changed
                                  - Schemas added: subschema #1, subschema #2
                                - Type changed from 'string' to ''

PATCH /api/openstack-backups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: access_url
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: security_groups
                          - Items changed
                            - Properties changed
                              - Modified property: access_url
                                - Property 'OneOf' changed
                                  - Schemas added: subschema #1, subschema #2
                                - Type changed from 'string' to ''

PUT /api/openstack-backups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: access_url
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: security_groups
                          - Items changed
                            - Properties changed
                              - Modified property: access_url
                                - Property 'OneOf' changed
                                  - Schemas added: subschema #1, subschema #2
                                - Type changed from 'string' to ''

POST /api/openstack-backups/{uuid}/restore/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: access_url
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''

GET /api/openstack-floating-ips/

- Deleted query param: uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''

HEAD /api/openstack-floating-ips/

- Deleted query param: uuid

GET /api/openstack-floating-ips/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/openstack-health-monitors/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''

GET /api/openstack-health-monitors/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/openstack-images/

- New query param: is_rescue_image
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: is_rescue_image
            - Properties changed
              - New property: hw_rescue_bus
              - New property: hw_rescue_device
              - New property: is_rescue_image

HEAD /api/openstack-images/

- New query param: is_rescue_image

GET /api/openstack-images/usage_stats/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: is_rescue_image
          - Properties changed
            - New property: hw_rescue_bus
            - New property: hw_rescue_device
            - New property: is_rescue_image

GET /api/openstack-images/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: is_rescue_image
          - Properties changed
            - New property: hw_rescue_bus
            - New property: hw_rescue_device
            - New property: is_rescue_image

GET /api/openstack-instances/

- Deleted query param: uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''
              - Modified property: ports
                - Items changed
                  - Properties changed
                    - Modified property: security_groups
                      - Items changed
                        - Properties changed
                          - Modified property: access_url
                            - Property 'OneOf' changed
                              - Schemas added: subschema #1, subschema #2
                            - Type changed from 'string' to ''

HEAD /api/openstack-instances/

- Deleted query param: uuid

GET /api/openstack-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: access_url
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''

PATCH /api/openstack-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: access_url
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''

PUT /api/openstack-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: access_url
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''

POST /api/openstack-instances/{uuid}/backup/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: access_url
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: security_groups
                          - Items changed
                            - Properties changed
                              - Modified property: access_url
                                - Property 'OneOf' changed
                                  - Schemas added: subschema #1, subschema #2
                                - Type changed from 'string' to ''

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
                    - Modified property: access_url
                      - Property 'OneOf' changed
                        - Schemas added: subschema #1, subschema #2
                      - Type changed from 'string' to ''

GET /api/openstack-listeners/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''

GET /api/openstack-listeners/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/openstack-loadbalancers/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [vip_security_groups]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: vip_security_groups
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''

GET /api/openstack-loadbalancers/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [vip_security_groups]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: vip_security_groups
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/openstack-marketplace-tenants/

- Deleted query param: uuid

HEAD /api/openstack-marketplace-tenants/

- Deleted query param: uuid

GET /api/openstack-networks/

- Deleted query param: uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''

HEAD /api/openstack-networks/

- Deleted query param: uuid

GET /api/openstack-networks/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PATCH /api/openstack-networks/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PUT /api/openstack-networks/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

POST /api/openstack-networks/{uuid}/create_subnet/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/openstack-pool-members/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''

GET /api/openstack-pool-members/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/openstack-pools/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''

POST /api/openstack-pools/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: lb_algorithm
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: lb_algorithm

GET /api/openstack-pools/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/openstack-ports/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''

POST /api/openstack-ports/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/openstack-ports/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PATCH /api/openstack-ports/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PUT /api/openstack-ports/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/openstack-routers/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [enable_snat external_fixed_ips external_network_id external_network_name external_network_uuid has_external_gateway]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: enable_snat
              - New property: external_fixed_ips
              - New property: external_network_id
              - New property: external_network_name
              - New property: external_network_uuid
              - New property: has_external_gateway
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''
              - Modified property: ports
                - Items changed
                  - Properties changed
                    - Modified property: security_groups
                      - Items changed
                        - Properties changed
                          - Modified property: access_url
                            - Property 'OneOf' changed
                              - Schemas added: subschema #1, subschema #2
                            - Type changed from 'string' to ''

GET /api/openstack-routers/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [enable_snat external_fixed_ips external_network_id external_network_name external_network_uuid has_external_gateway]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: enable_snat
            - New property: external_fixed_ips
            - New property: external_network_id
            - New property: external_network_name
            - New property: external_network_uuid
            - New property: has_external_gateway
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: access_url
                          - Property 'OneOf' changed
                            - Schemas added: subschema #1, subschema #2
                          - Type changed from 'string' to ''

GET /api/openstack-security-groups/

- Deleted query param: uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''

HEAD /api/openstack-security-groups/

- Deleted query param: uuid

GET /api/openstack-security-groups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/openstack-server-groups/

- Deleted query param: uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''

HEAD /api/openstack-server-groups/

- Deleted query param: uuid

POST /api/openstack-server-groups/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/openstack-server-groups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/openstack-snapshots/

- Deleted query param: uuid
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [backups]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: backups
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''

HEAD /api/openstack-snapshots/

- Deleted query param: uuid

GET /api/openstack-snapshots/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [backups]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: backups
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PATCH /api/openstack-snapshots/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: backups
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PUT /api/openstack-snapshots/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: backups
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

POST /api/openstack-snapshots/{uuid}/restore/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/openstack-subnets/

- Deleted query param: uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''

HEAD /api/openstack-subnets/

- Deleted query param: uuid

GET /api/openstack-subnets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PATCH /api/openstack-subnets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PUT /api/openstack-subnets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

POST /api/openstack-subnets/{uuid}/connect/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/openstack-subnets/{uuid}/disconnect/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

GET /api/openstack-tenants/

- Deleted query param: uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''

HEAD /api/openstack-tenants/

- Deleted query param: uuid

GET /api/openstack-tenants/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PATCH /api/openstack-tenants/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PUT /api/openstack-tenants/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/openstack-tenants/{uuid}/backend_instances/

- Deleted query param: uuid

GET /api/openstack-tenants/{uuid}/backend_volumes/

- Deleted query param: uuid

POST /api/openstack-tenants/{uuid}/create_floating_ip/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

POST /api/openstack-tenants/{uuid}/create_network/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

POST /api/openstack-tenants/{uuid}/create_security_group/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

POST /api/openstack-tenants/{uuid}/create_server_group/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

POST /api/openstack-tenants/{uuid}/pull_security_groups/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

POST /api/openstack-tenants/{uuid}/pull_server_groups/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/openstack-volumes/

- Deleted query param: uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''

HEAD /api/openstack-volumes/

- Deleted query param: uuid

GET /api/openstack-volumes/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PATCH /api/openstack-volumes/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PUT /api/openstack-volumes/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

POST /api/openstack-volumes/{uuid}/snapshot/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: backups
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/override-settings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: AI_ASSISTANT_GLOBAL_DAILY_TOKEN_BUDGET
            - New property: AI_ASSISTANT_GLOBAL_REQUESTS_PER_MINUTE
            - New property: AI_ASSISTANT_STREAM_TIMEOUT_SECONDS
            - New property: AI_ASSISTANT_SYSTEM_PROMPT_CUSTOM_INSTRUCTIONS
            - New property: ANONYMOUS_CHAT_ARTIFACT_RETENTION_DAYS
            - New property: ANONYMOUS_CHAT_CATALOG_MAX_ENTRIES
            - New property: ANONYMOUS_CHAT_FEEDBACK_TOKEN_SECRET
            - New property: ANONYMOUS_CHAT_REVIEW_DAILY_TOKEN_BUDGET
            - New property: ANONYMOUS_CHAT_REVIEW_ENABLED
            - New property: ANONYMOUS_CHAT_USER_SLUG_SALT
            - New property: DEFAULT_CALL_USER_ATTRIBUTES
            - New property: SHOW_OFFERING_COVER_IMAGE
            - New property: USAGE_POLL_RECORD_RETENTION_MONTHS
            - Modified property: AI_ASSISTANT_ENABLED_ROLES
              - New enum values: [anonymous]
            - Modified property: DEFAULT_OFFERING_USER_ATTRIBUTES
              - Items changed
                - Property 'OneOf' changed
                  - Modified schema: #/components/schemas/UserAttributeEnum
                    - New enum values: [registration_method first_name last_name]
            - Modified property: ENABLED_REPORTING_SCREENS
              - Items changed
                - Property 'OneOf' changed
                  - Modified schema: #/components/schemas/ENABLEDREPORTINGSCREENSEnum
                    - New enum values: [offering-usage]
            - Modified property: ENABLED_USER_PROFILE_ATTRIBUTES
              - Items changed
                - Property 'OneOf' changed
                  - Modified schema: #/components/schemas/UserAttributeEnum
                    - New enum values: [registration_method first_name last_name]
            - Modified property: FEDERATED_IDENTITY_SYNC_ALLOWED_ATTRIBUTES
              - Items changed
                - Property 'OneOf' changed
                  - Modified schema: #/components/schemas/UserAttributeEnum
                    - New enum values: [registration_method first_name last_name]
            - Modified property: INVITATION_ALLOWED_FIELDS
              - Items changed
                - Property 'OneOf' changed
                  - Modified schema: #/components/schemas/UserAttributeEnum
                    - New enum values: [registration_method first_name last_name]
            - Modified property: MANDATORY_USER_ATTRIBUTES
              - Items changed
                - Property 'OneOf' changed
                  - Modified schema: #/components/schemas/UserAttributeEnum
                    - New enum values: [registration_method first_name last_name]

POST /api/override-settings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: AI_ASSISTANT_GLOBAL_DAILY_TOKEN_BUDGET
          - New property: AI_ASSISTANT_GLOBAL_REQUESTS_PER_MINUTE
          - New property: AI_ASSISTANT_STREAM_TIMEOUT_SECONDS
          - New property: AI_ASSISTANT_SYSTEM_PROMPT_CUSTOM_INSTRUCTIONS
          - New property: ANONYMOUS_CHAT_ARTIFACT_RETENTION_DAYS
          - New property: ANONYMOUS_CHAT_CATALOG_MAX_ENTRIES
          - New property: ANONYMOUS_CHAT_FEEDBACK_TOKEN_SECRET
          - New property: ANONYMOUS_CHAT_REVIEW_DAILY_TOKEN_BUDGET
          - New property: ANONYMOUS_CHAT_REVIEW_ENABLED
          - New property: ANONYMOUS_CHAT_USER_SLUG_SALT
          - New property: DEFAULT_CALL_USER_ATTRIBUTES
          - New property: SHOW_OFFERING_COVER_IMAGE
          - New property: USAGE_POLL_RECORD_RETENTION_MONTHS
          - Modified property: AI_ASSISTANT_ENABLED_ROLES
            - New enum values: [anonymous]
          - Modified property: DEFAULT_OFFERING_USER_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [registration_method first_name last_name]
          - Modified property: ENABLED_REPORTING_SCREENS
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/ENABLEDREPORTINGSCREENSEnum
                  - New enum values: [offering-usage]
          - Modified property: ENABLED_USER_PROFILE_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [registration_method first_name last_name]
          - Modified property: FEDERATED_IDENTITY_SYNC_ALLOWED_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [registration_method first_name last_name]
          - Modified property: INVITATION_ALLOWED_FIELDS
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [registration_method first_name last_name]
          - Modified property: MANDATORY_USER_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [registration_method first_name last_name]
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: AI_ASSISTANT_GLOBAL_DAILY_TOKEN_BUDGET
          - New property: AI_ASSISTANT_GLOBAL_REQUESTS_PER_MINUTE
          - New property: AI_ASSISTANT_STREAM_TIMEOUT_SECONDS
          - New property: AI_ASSISTANT_SYSTEM_PROMPT_CUSTOM_INSTRUCTIONS
          - New property: ANONYMOUS_CHAT_ARTIFACT_RETENTION_DAYS
          - New property: ANONYMOUS_CHAT_CATALOG_MAX_ENTRIES
          - New property: ANONYMOUS_CHAT_FEEDBACK_TOKEN_SECRET
          - New property: ANONYMOUS_CHAT_REVIEW_DAILY_TOKEN_BUDGET
          - New property: ANONYMOUS_CHAT_REVIEW_ENABLED
          - New property: ANONYMOUS_CHAT_USER_SLUG_SALT
          - New property: DEFAULT_CALL_USER_ATTRIBUTES
          - New property: SHOW_OFFERING_COVER_IMAGE
          - New property: USAGE_POLL_RECORD_RETENTION_MONTHS
          - Modified property: AI_ASSISTANT_ENABLED_ROLES
            - New enum values: [anonymous]
          - Modified property: DEFAULT_OFFERING_USER_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [registration_method first_name last_name]
          - Modified property: ENABLED_REPORTING_SCREENS
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/ENABLEDREPORTINGSCREENSEnum
                  - New enum values: [offering-usage]
          - Modified property: ENABLED_USER_PROFILE_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [registration_method first_name last_name]
          - Modified property: FEDERATED_IDENTITY_SYNC_ALLOWED_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [registration_method first_name last_name]
          - Modified property: INVITATION_ALLOWED_FIELDS
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [registration_method first_name last_name]
          - Modified property: MANDATORY_USER_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [registration_method first_name last_name]
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: AI_ASSISTANT_GLOBAL_DAILY_TOKEN_BUDGET
          - New property: AI_ASSISTANT_GLOBAL_REQUESTS_PER_MINUTE
          - New property: AI_ASSISTANT_STREAM_TIMEOUT_SECONDS
          - New property: AI_ASSISTANT_SYSTEM_PROMPT_CUSTOM_INSTRUCTIONS
          - New property: ANONYMOUS_CHAT_ARTIFACT_RETENTION_DAYS
          - New property: ANONYMOUS_CHAT_CATALOG_MAX_ENTRIES
          - New property: ANONYMOUS_CHAT_FEEDBACK_TOKEN_SECRET
          - New property: ANONYMOUS_CHAT_REVIEW_DAILY_TOKEN_BUDGET
          - New property: ANONYMOUS_CHAT_REVIEW_ENABLED
          - New property: ANONYMOUS_CHAT_USER_SLUG_SALT
          - New property: DEFAULT_CALL_USER_ATTRIBUTES
          - New property: SHOW_OFFERING_COVER_IMAGE
          - New property: USAGE_POLL_RECORD_RETENTION_MONTHS
          - Modified property: AI_ASSISTANT_ENABLED_ROLES
            - New enum values: [anonymous]
          - Modified property: DEFAULT_OFFERING_USER_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [registration_method first_name last_name]
          - Modified property: ENABLED_REPORTING_SCREENS
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/ENABLEDREPORTINGSCREENSEnum
                  - New enum values: [offering-usage]
          - Modified property: ENABLED_USER_PROFILE_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [registration_method first_name last_name]
          - Modified property: FEDERATED_IDENTITY_SYNC_ALLOWED_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [registration_method first_name last_name]
          - Modified property: INVITATION_ALLOWED_FIELDS
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [registration_method first_name last_name]
          - Modified property: MANDATORY_USER_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [registration_method first_name last_name]

POST /api/payment-profiles/{uuid}/enable/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/payments/{uuid}/unlink_from_invoice/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

GET /api/projects/

- New query param: affiliated_organization_name
- New query param: affiliated_organization_uuid
- New query param: has_affiliated_organization
- New query param: science_domain_uuid
- New query param: science_sub_domain_uuid
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [affiliated_organizations science_domain_code science_domain_name science_domain_uuid science_sub_domain science_sub_domain_code science_sub_domain_name]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: affiliated_organizations
              - New property: science_domain_code
              - New property: science_domain_name
              - New property: science_domain_uuid
              - New property: science_sub_domain
              - New property: science_sub_domain_code
              - New property: science_sub_domain_name

HEAD /api/projects/

- New query param: affiliated_organization_name
- New query param: affiliated_organization_uuid
- New query param: has_affiliated_organization
- New query param: science_domain_uuid
- New query param: science_sub_domain_uuid

POST /api/projects/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: science_sub_domain
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: science_sub_domain
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: science_sub_domain
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: affiliated_organizations
            - New property: science_domain_code
            - New property: science_domain_name
            - New property: science_domain_uuid
            - New property: science_sub_domain
            - New property: science_sub_domain_code
            - New property: science_sub_domain_name

GET /api/projects/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [affiliated_organizations science_domain_code science_domain_name science_domain_uuid science_sub_domain science_sub_domain_code science_sub_domain_name]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: affiliated_organizations
            - New property: science_domain_code
            - New property: science_domain_name
            - New property: science_domain_uuid
            - New property: science_sub_domain
            - New property: science_sub_domain_code
            - New property: science_sub_domain_name

PATCH /api/projects/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: science_sub_domain
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: science_sub_domain
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: science_sub_domain
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: affiliated_organizations
            - New property: science_domain_code
            - New property: science_domain_name
            - New property: science_domain_uuid
            - New property: science_sub_domain
            - New property: science_sub_domain_code
            - New property: science_sub_domain_name

PUT /api/projects/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: science_sub_domain
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: science_sub_domain
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: science_sub_domain
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: affiliated_organizations
            - New property: science_domain_code
            - New property: science_domain_name
            - New property: science_domain_uuid
            - New property: science_sub_domain
            - New property: science_sub_domain_code
            - New property: science_sub_domain_name

POST /api/projects/{uuid}/move_project/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: affiliated_organizations
            - New property: science_domain_code
            - New property: science_domain_name
            - New property: science_domain_uuid
            - New property: science_sub_domain
            - New property: science_sub_domain_code
            - New property: science_sub_domain_name

POST /api/projects/{uuid}/recover/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: affiliated_organizations
            - New property: science_domain_code
            - New property: science_domain_name
            - New property: science_domain_uuid
            - New property: science_sub_domain
            - New property: science_sub_domain_code
            - New property: science_sub_domain_name

GET /api/promotions-campaigns/{uuid}/orders/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [error_updated_at output_updated_at]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: error_updated_at
              - New property: output_updated_at

GET /api/promotions-campaigns/{uuid}/resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [project_is_in_grace_period]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: project_is_in_grace_period
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: error_updated_at
                      - New property: output_updated_at
              - Modified property: offering_components
                - Items changed
                  - Properties changed
                    - New property: offering_uuid
                    - Modified property: limit_period
                      - Property 'OneOf' changed
                        - Schemas deleted: #/components/schemas/BlankEnum
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: error_updated_at
                      - New property: output_updated_at

GET /api/proposal-proposals/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: applicant_active_isds
              - New required property: applicant_address
              - New required property: applicant_affiliations
              - New required property: applicant_birth_date
              - New required property: applicant_civil_number
              - New required property: applicant_country_of_residence
              - New required property: applicant_eduperson_assurance
              - New required property: applicant_email
              - New required property: applicant_first_name
              - New required property: applicant_full_name
              - New required property: applicant_gender
              - New required property: applicant_identity_source
              - New required property: applicant_job_title
              - New required property: applicant_last_name
              - New required property: applicant_nationalities
              - New required property: applicant_nationality
              - New required property: applicant_organization
              - New required property: applicant_organization_country
              - New required property: applicant_organization_registry_code
              - New required property: applicant_organization_type
              - New required property: applicant_personal_title
              - New required property: applicant_phone_number
              - New required property: applicant_place_of_birth
              - New required property: applicant_registration_method
              - New required property: applicant_username
              - New required property: science_domain_name
              - New required property: science_domain_uuid
              - New required property: science_sub_domain_name
            - Properties changed
              - New property: applicant_active_isds
              - New property: applicant_address
              - New property: applicant_affiliations
              - New property: applicant_birth_date
              - New property: applicant_civil_number
              - New property: applicant_country_of_residence
              - New property: applicant_eduperson_assurance
              - New property: applicant_email
              - New property: applicant_first_name
              - New property: applicant_full_name
              - New property: applicant_gender
              - New property: applicant_identity_source
              - New property: applicant_job_title
              - New property: applicant_last_name
              - New property: applicant_nationalities
              - New property: applicant_nationality
              - New property: applicant_organization
              - New property: applicant_organization_country
              - New property: applicant_organization_registry_code
              - New property: applicant_organization_type
              - New property: applicant_personal_title
              - New property: applicant_phone_number
              - New property: applicant_place_of_birth
              - New property: applicant_registration_method
              - New property: applicant_username
              - New property: science_domain_name
              - New property: science_domain_uuid
              - New property: science_sub_domain
              - New property: science_sub_domain_name

POST /api/proposal-proposals/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: science_sub_domain
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: applicant_active_isds
            - New required property: applicant_address
            - New required property: applicant_affiliations
            - New required property: applicant_birth_date
            - New required property: applicant_civil_number
            - New required property: applicant_country_of_residence
            - New required property: applicant_eduperson_assurance
            - New required property: applicant_email
            - New required property: applicant_first_name
            - New required property: applicant_full_name
            - New required property: applicant_gender
            - New required property: applicant_identity_source
            - New required property: applicant_job_title
            - New required property: applicant_last_name
            - New required property: applicant_nationalities
            - New required property: applicant_nationality
            - New required property: applicant_organization
            - New required property: applicant_organization_country
            - New required property: applicant_organization_registry_code
            - New required property: applicant_organization_type
            - New required property: applicant_personal_title
            - New required property: applicant_phone_number
            - New required property: applicant_place_of_birth
            - New required property: applicant_registration_method
            - New required property: applicant_username
            - New required property: science_domain_name
            - New required property: science_domain_uuid
            - New required property: science_sub_domain_name
          - Properties changed
            - New property: applicant_active_isds
            - New property: applicant_address
            - New property: applicant_affiliations
            - New property: applicant_birth_date
            - New property: applicant_civil_number
            - New property: applicant_country_of_residence
            - New property: applicant_eduperson_assurance
            - New property: applicant_email
            - New property: applicant_first_name
            - New property: applicant_full_name
            - New property: applicant_gender
            - New property: applicant_identity_source
            - New property: applicant_job_title
            - New property: applicant_last_name
            - New property: applicant_nationalities
            - New property: applicant_nationality
            - New property: applicant_organization
            - New property: applicant_organization_country
            - New property: applicant_organization_registry_code
            - New property: applicant_organization_type
            - New property: applicant_personal_title
            - New property: applicant_phone_number
            - New property: applicant_place_of_birth
            - New property: applicant_registration_method
            - New property: applicant_username
            - New property: science_domain_name
            - New property: science_domain_uuid
            - New property: science_sub_domain
            - New property: science_sub_domain_name

GET /api/proposal-proposals/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: applicant_active_isds
            - New required property: applicant_address
            - New required property: applicant_affiliations
            - New required property: applicant_birth_date
            - New required property: applicant_civil_number
            - New required property: applicant_country_of_residence
            - New required property: applicant_eduperson_assurance
            - New required property: applicant_email
            - New required property: applicant_first_name
            - New required property: applicant_full_name
            - New required property: applicant_gender
            - New required property: applicant_identity_source
            - New required property: applicant_job_title
            - New required property: applicant_last_name
            - New required property: applicant_nationalities
            - New required property: applicant_nationality
            - New required property: applicant_organization
            - New required property: applicant_organization_country
            - New required property: applicant_organization_registry_code
            - New required property: applicant_organization_type
            - New required property: applicant_personal_title
            - New required property: applicant_phone_number
            - New required property: applicant_place_of_birth
            - New required property: applicant_registration_method
            - New required property: applicant_username
            - New required property: science_domain_name
            - New required property: science_domain_uuid
            - New required property: science_sub_domain_name
          - Properties changed
            - New property: applicant_active_isds
            - New property: applicant_address
            - New property: applicant_affiliations
            - New property: applicant_birth_date
            - New property: applicant_civil_number
            - New property: applicant_country_of_residence
            - New property: applicant_eduperson_assurance
            - New property: applicant_email
            - New property: applicant_first_name
            - New property: applicant_full_name
            - New property: applicant_gender
            - New property: applicant_identity_source
            - New property: applicant_job_title
            - New property: applicant_last_name
            - New property: applicant_nationalities
            - New property: applicant_nationality
            - New property: applicant_organization
            - New property: applicant_organization_country
            - New property: applicant_organization_registry_code
            - New property: applicant_organization_type
            - New property: applicant_personal_title
            - New property: applicant_phone_number
            - New property: applicant_place_of_birth
            - New property: applicant_registration_method
            - New property: applicant_username
            - New property: science_domain_name
            - New property: science_domain_uuid
            - New property: science_sub_domain
            - New property: science_sub_domain_name

GET /api/proposal-proposals/{uuid}/resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: requested_offering
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/NestedRequestedOffering
                    - Properties changed
                      - Modified property: components
                        - Items changed
                          - Properties changed
                            - New property: offering_uuid
                            - Modified property: limit_period
                              - Property 'OneOf' changed
                                - Schemas deleted: #/components/schemas/BlankEnum
                      - Modified property: plan_details
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/BasePublicPlan
                            - Properties changed
                              - Modified property: future_prices
                                - AdditionalProperties changed
                                  - Type changed from 'number' to 'string'
                                  - Format changed from 'double' to ''
                              - Modified property: minimal_price
                                - Type changed from 'number' to 'string'
                                - Format changed from 'double' to ''
                              - Modified property: prices
                                - AdditionalProperties changed
                                  - Type changed from 'number' to 'string'
                                  - Format changed from 'double' to ''
                              - Modified property: quotas
                                - AdditionalProperties changed
                                  - Type changed from 'number' to 'integer'
                                  - Format changed from 'double' to ''

POST /api/proposal-proposals/{uuid}/resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: offering_uuid
                          - Modified property: limit_period
                            - Property 'OneOf' changed
                              - Schemas deleted: #/components/schemas/BlankEnum
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: future_prices
                              - AdditionalProperties changed
                                - Type changed from 'number' to 'string'
                                - Format changed from 'double' to ''
                            - Modified property: minimal_price
                              - Type changed from 'number' to 'string'
                              - Format changed from 'double' to ''
                            - Modified property: prices
                              - AdditionalProperties changed
                                - Type changed from 'number' to 'string'
                                - Format changed from 'double' to ''
                            - Modified property: quotas
                              - AdditionalProperties changed
                                - Type changed from 'number' to 'integer'
                                - Format changed from 'double' to ''

GET /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: offering_uuid
                          - Modified property: limit_period
                            - Property 'OneOf' changed
                              - Schemas deleted: #/components/schemas/BlankEnum
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: future_prices
                              - AdditionalProperties changed
                                - Type changed from 'number' to 'string'
                                - Format changed from 'double' to ''
                            - Modified property: minimal_price
                              - Type changed from 'number' to 'string'
                              - Format changed from 'double' to ''
                            - Modified property: prices
                              - AdditionalProperties changed
                                - Type changed from 'number' to 'string'
                                - Format changed from 'double' to ''
                            - Modified property: quotas
                              - AdditionalProperties changed
                                - Type changed from 'number' to 'integer'
                                - Format changed from 'double' to ''

PATCH /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: offering_uuid
                          - Modified property: limit_period
                            - Property 'OneOf' changed
                              - Schemas deleted: #/components/schemas/BlankEnum
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: future_prices
                              - AdditionalProperties changed
                                - Type changed from 'number' to 'string'
                                - Format changed from 'double' to ''
                            - Modified property: minimal_price
                              - Type changed from 'number' to 'string'
                              - Format changed from 'double' to ''
                            - Modified property: prices
                              - AdditionalProperties changed
                                - Type changed from 'number' to 'string'
                                - Format changed from 'double' to ''
                            - Modified property: quotas
                              - AdditionalProperties changed
                                - Type changed from 'number' to 'integer'
                                - Format changed from 'double' to ''

PUT /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: offering_uuid
                          - Modified property: limit_period
                            - Property 'OneOf' changed
                              - Schemas deleted: #/components/schemas/BlankEnum
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: future_prices
                              - AdditionalProperties changed
                                - Type changed from 'number' to 'string'
                                - Format changed from 'double' to ''
                            - Modified property: minimal_price
                              - Type changed from 'number' to 'string'
                              - Format changed from 'double' to ''
                            - Modified property: prices
                              - AdditionalProperties changed
                                - Type changed from 'number' to 'string'
                                - Format changed from 'double' to ''
                            - Modified property: quotas
                              - AdditionalProperties changed
                                - Type changed from 'number' to 'integer'
                                - Format changed from 'double' to ''

GET /api/proposal-protected-calls/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [applicant_visibility_config]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: applicant_visibility_config
              - Modified property: offerings
                - Items changed
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: offering_uuid
                          - Modified property: limit_period
                            - Property 'OneOf' changed
                              - Schemas deleted: #/components/schemas/BlankEnum
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: future_prices
                              - AdditionalProperties changed
                                - Type changed from 'number' to 'string'
                                - Format changed from 'double' to ''
                            - Modified property: minimal_price
                              - Type changed from 'number' to 'string'
                              - Format changed from 'double' to ''
                            - Modified property: prices
                              - AdditionalProperties changed
                                - Type changed from 'number' to 'string'
                                - Format changed from 'double' to ''
                            - Modified property: quotas
                              - AdditionalProperties changed
                                - Type changed from 'number' to 'integer'
                                - Format changed from 'double' to ''
              - Modified property: resource_templates
                - Items changed
                  - Properties changed
                    - Modified property: requested_offering_plan
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: future_prices
                              - AdditionalProperties changed
                                - Type changed from 'number' to 'string'
                                - Format changed from 'double' to ''
                            - Modified property: minimal_price
                              - Type changed from 'number' to 'string'
                              - Format changed from 'double' to ''
                            - Modified property: prices
                              - AdditionalProperties changed
                                - Type changed from 'number' to 'string'
                                - Format changed from 'double' to ''
                            - Modified property: quotas
                              - AdditionalProperties changed
                                - Type changed from 'number' to 'integer'
                                - Format changed from 'double' to ''

POST /api/proposal-protected-calls/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: applicant_visibility_config
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: applicant_visibility_config
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: offering_uuid
                        - Modified property: limit_period
                          - Property 'OneOf' changed
                            - Schemas deleted: #/components/schemas/BlankEnum
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: future_prices
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'string'
                              - Format changed from 'double' to ''
                          - Modified property: minimal_price
                            - Type changed from 'number' to 'string'
                            - Format changed from 'double' to ''
                          - Modified property: prices
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'string'
                              - Format changed from 'double' to ''
                          - Modified property: quotas
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'integer'
                              - Format changed from 'double' to ''
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: future_prices
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'string'
                              - Format changed from 'double' to ''
                          - Modified property: minimal_price
                            - Type changed from 'number' to 'string'
                            - Format changed from 'double' to ''
                          - Modified property: prices
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'string'
                              - Format changed from 'double' to ''
                          - Modified property: quotas
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'integer'
                              - Format changed from 'double' to ''

GET /api/proposal-protected-calls/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [applicant_visibility_config]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: applicant_visibility_config
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: offering_uuid
                        - Modified property: limit_period
                          - Property 'OneOf' changed
                            - Schemas deleted: #/components/schemas/BlankEnum
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: future_prices
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'string'
                              - Format changed from 'double' to ''
                          - Modified property: minimal_price
                            - Type changed from 'number' to 'string'
                            - Format changed from 'double' to ''
                          - Modified property: prices
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'string'
                              - Format changed from 'double' to ''
                          - Modified property: quotas
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'integer'
                              - Format changed from 'double' to ''
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: future_prices
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'string'
                              - Format changed from 'double' to ''
                          - Modified property: minimal_price
                            - Type changed from 'number' to 'string'
                            - Format changed from 'double' to ''
                          - Modified property: prices
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'string'
                              - Format changed from 'double' to ''
                          - Modified property: quotas
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'integer'
                              - Format changed from 'double' to ''

PATCH /api/proposal-protected-calls/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: applicant_visibility_config
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: applicant_visibility_config
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: offering_uuid
                        - Modified property: limit_period
                          - Property 'OneOf' changed
                            - Schemas deleted: #/components/schemas/BlankEnum
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: future_prices
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'string'
                              - Format changed from 'double' to ''
                          - Modified property: minimal_price
                            - Type changed from 'number' to 'string'
                            - Format changed from 'double' to ''
                          - Modified property: prices
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'string'
                              - Format changed from 'double' to ''
                          - Modified property: quotas
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'integer'
                              - Format changed from 'double' to ''
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: future_prices
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'string'
                              - Format changed from 'double' to ''
                          - Modified property: minimal_price
                            - Type changed from 'number' to 'string'
                            - Format changed from 'double' to ''
                          - Modified property: prices
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'string'
                              - Format changed from 'double' to ''
                          - Modified property: quotas
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'integer'
                              - Format changed from 'double' to ''

PUT /api/proposal-protected-calls/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: applicant_visibility_config
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: applicant_visibility_config
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: offering_uuid
                        - Modified property: limit_period
                          - Property 'OneOf' changed
                            - Schemas deleted: #/components/schemas/BlankEnum
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: future_prices
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'string'
                              - Format changed from 'double' to ''
                          - Modified property: minimal_price
                            - Type changed from 'number' to 'string'
                            - Format changed from 'double' to ''
                          - Modified property: prices
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'string'
                              - Format changed from 'double' to ''
                          - Modified property: quotas
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'integer'
                              - Format changed from 'double' to ''
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: future_prices
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'string'
                              - Format changed from 'double' to ''
                          - Modified property: minimal_price
                            - Type changed from 'number' to 'string'
                            - Format changed from 'double' to ''
                          - Modified property: prices
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'string'
                              - Format changed from 'double' to ''
                          - Modified property: quotas
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'integer'
                              - Format changed from 'double' to ''

POST /api/proposal-protected-calls/{uuid}/compute-affinities/

- Request body changed

GET /api/proposal-protected-calls/{uuid}/offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: components
                - Items changed
                  - Properties changed
                    - New property: offering_uuid
                    - Modified property: limit_period
                      - Property 'OneOf' changed
                        - Schemas deleted: #/components/schemas/BlankEnum
              - Modified property: plan_details
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/BasePublicPlan
                    - Properties changed
                      - Modified property: future_prices
                        - AdditionalProperties changed
                          - Type changed from 'number' to 'string'
                          - Format changed from 'double' to ''
                      - Modified property: minimal_price
                        - Type changed from 'number' to 'string'
                        - Format changed from 'double' to ''
                      - Modified property: prices
                        - AdditionalProperties changed
                          - Type changed from 'number' to 'string'
                          - Format changed from 'double' to ''
                      - Modified property: quotas
                        - AdditionalProperties changed
                          - Type changed from 'number' to 'integer'
                          - Format changed from 'double' to ''

POST /api/proposal-protected-calls/{uuid}/offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: offering_uuid
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Schemas deleted: #/components/schemas/BlankEnum
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: future_prices
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'string'
                        - Format changed from 'double' to ''
                    - Modified property: minimal_price
                      - Type changed from 'number' to 'string'
                      - Format changed from 'double' to ''
                    - Modified property: prices
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'string'
                        - Format changed from 'double' to ''
                    - Modified property: quotas
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'integer'
                        - Format changed from 'double' to ''

GET /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: offering_uuid
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Schemas deleted: #/components/schemas/BlankEnum
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: future_prices
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'string'
                        - Format changed from 'double' to ''
                    - Modified property: minimal_price
                      - Type changed from 'number' to 'string'
                      - Format changed from 'double' to ''
                    - Modified property: prices
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'string'
                        - Format changed from 'double' to ''
                    - Modified property: quotas
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'integer'
                        - Format changed from 'double' to ''

PATCH /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: offering_uuid
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Schemas deleted: #/components/schemas/BlankEnum
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: future_prices
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'string'
                        - Format changed from 'double' to ''
                    - Modified property: minimal_price
                      - Type changed from 'number' to 'string'
                      - Format changed from 'double' to ''
                    - Modified property: prices
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'string'
                        - Format changed from 'double' to ''
                    - Modified property: quotas
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'integer'
                        - Format changed from 'double' to ''

PUT /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: offering_uuid
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Schemas deleted: #/components/schemas/BlankEnum
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: future_prices
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'string'
                        - Format changed from 'double' to ''
                    - Modified property: minimal_price
                      - Type changed from 'number' to 'string'
                      - Format changed from 'double' to ''
                    - Modified property: prices
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'string'
                        - Format changed from 'double' to ''
                    - Modified property: quotas
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'integer'
                        - Format changed from 'double' to ''

GET /api/proposal-protected-calls/{uuid}/resource_templates/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: requested_offering_plan
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/BasePublicPlan
                    - Properties changed
                      - Modified property: future_prices
                        - AdditionalProperties changed
                          - Type changed from 'number' to 'string'
                          - Format changed from 'double' to ''
                      - Modified property: minimal_price
                        - Type changed from 'number' to 'string'
                        - Format changed from 'double' to ''
                      - Modified property: prices
                        - AdditionalProperties changed
                          - Type changed from 'number' to 'string'
                          - Format changed from 'double' to ''
                      - Modified property: quotas
                        - AdditionalProperties changed
                          - Type changed from 'number' to 'integer'
                          - Format changed from 'double' to ''

POST /api/proposal-protected-calls/{uuid}/resource_templates/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: requested_offering_plan
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: future_prices
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'string'
                        - Format changed from 'double' to ''
                    - Modified property: minimal_price
                      - Type changed from 'number' to 'string'
                      - Format changed from 'double' to ''
                    - Modified property: prices
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'string'
                        - Format changed from 'double' to ''
                    - Modified property: quotas
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'integer'
                        - Format changed from 'double' to ''

GET /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: requested_offering_plan
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: future_prices
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'string'
                        - Format changed from 'double' to ''
                    - Modified property: minimal_price
                      - Type changed from 'number' to 'string'
                      - Format changed from 'double' to ''
                    - Modified property: prices
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'string'
                        - Format changed from 'double' to ''
                    - Modified property: quotas
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'integer'
                        - Format changed from 'double' to ''

PATCH /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: requested_offering_plan
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: future_prices
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'string'
                        - Format changed from 'double' to ''
                    - Modified property: minimal_price
                      - Type changed from 'number' to 'string'
                      - Format changed from 'double' to ''
                    - Modified property: prices
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'string'
                        - Format changed from 'double' to ''
                    - Modified property: quotas
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'integer'
                        - Format changed from 'double' to ''

PUT /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: requested_offering_plan
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: future_prices
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'string'
                        - Format changed from 'double' to ''
                    - Modified property: minimal_price
                      - Type changed from 'number' to 'string'
                      - Format changed from 'double' to ''
                    - Modified property: prices
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'string'
                        - Format changed from 'double' to ''
                    - Modified property: quotas
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'integer'
                        - Format changed from 'double' to ''

POST /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/close/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: applicant_visibility_config
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: applicant_visibility_config
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: offering_uuid
                        - Modified property: limit_period
                          - Property 'OneOf' changed
                            - Schemas deleted: #/components/schemas/BlankEnum
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: future_prices
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'string'
                              - Format changed from 'double' to ''
                          - Modified property: minimal_price
                            - Type changed from 'number' to 'string'
                            - Format changed from 'double' to ''
                          - Modified property: prices
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'string'
                              - Format changed from 'double' to ''
                          - Modified property: quotas
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'integer'
                              - Format changed from 'double' to ''
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: future_prices
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'string'
                              - Format changed from 'double' to ''
                          - Modified property: minimal_price
                            - Type changed from 'number' to 'string'
                            - Format changed from 'double' to ''
                          - Modified property: prices
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'string'
                              - Format changed from 'double' to ''
                          - Modified property: quotas
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'integer'
                              - Format changed from 'double' to ''

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
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: offering_uuid
                          - Modified property: limit_period
                            - Property 'OneOf' changed
                              - Schemas deleted: #/components/schemas/BlankEnum
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: future_prices
                              - AdditionalProperties changed
                                - Type changed from 'number' to 'string'
                                - Format changed from 'double' to ''
                            - Modified property: minimal_price
                              - Type changed from 'number' to 'string'
                              - Format changed from 'double' to ''
                            - Modified property: prices
                              - AdditionalProperties changed
                                - Type changed from 'number' to 'string'
                                - Format changed from 'double' to ''
                            - Modified property: quotas
                              - AdditionalProperties changed
                                - Type changed from 'number' to 'integer'
                                - Format changed from 'double' to ''
              - Modified property: resource_templates
                - Items changed
                  - Properties changed
                    - Modified property: requested_offering_plan
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: future_prices
                              - AdditionalProperties changed
                                - Type changed from 'number' to 'string'
                                - Format changed from 'double' to ''
                            - Modified property: minimal_price
                              - Type changed from 'number' to 'string'
                              - Format changed from 'double' to ''
                            - Modified property: prices
                              - AdditionalProperties changed
                                - Type changed from 'number' to 'string'
                                - Format changed from 'double' to ''
                            - Modified property: quotas
                              - AdditionalProperties changed
                                - Type changed from 'number' to 'integer'
                                - Format changed from 'double' to ''

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
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: offering_uuid
                        - Modified property: limit_period
                          - Property 'OneOf' changed
                            - Schemas deleted: #/components/schemas/BlankEnum
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: future_prices
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'string'
                              - Format changed from 'double' to ''
                          - Modified property: minimal_price
                            - Type changed from 'number' to 'string'
                            - Format changed from 'double' to ''
                          - Modified property: prices
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'string'
                              - Format changed from 'double' to ''
                          - Modified property: quotas
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'integer'
                              - Format changed from 'double' to ''
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: future_prices
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'string'
                              - Format changed from 'double' to ''
                          - Modified property: minimal_price
                            - Type changed from 'number' to 'string'
                            - Format changed from 'double' to ''
                          - Modified property: prices
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'string'
                              - Format changed from 'double' to ''
                          - Modified property: quotas
                            - AdditionalProperties changed
                              - Type changed from 'number' to 'integer'
                              - Format changed from 'double' to ''

GET /api/proposal-requested-offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: components
                - Items changed
                  - Properties changed
                    - New property: offering_uuid
                    - Modified property: limit_period
                      - Property 'OneOf' changed
                        - Schemas deleted: #/components/schemas/BlankEnum
              - Modified property: plan_details
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/BasePublicPlan
                    - Properties changed
                      - Modified property: future_prices
                        - AdditionalProperties changed
                          - Type changed from 'number' to 'string'
                          - Format changed from 'double' to ''
                      - Modified property: minimal_price
                        - Type changed from 'number' to 'string'
                        - Format changed from 'double' to ''
                      - Modified property: prices
                        - AdditionalProperties changed
                          - Type changed from 'number' to 'string'
                          - Format changed from 'double' to ''
                      - Modified property: quotas
                        - AdditionalProperties changed
                          - Type changed from 'number' to 'integer'
                          - Format changed from 'double' to ''

GET /api/proposal-requested-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: offering_uuid
                  - Modified property: limit_period
                    - Property 'OneOf' changed
                      - Schemas deleted: #/components/schemas/BlankEnum
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: future_prices
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'string'
                        - Format changed from 'double' to ''
                    - Modified property: minimal_price
                      - Type changed from 'number' to 'string'
                      - Format changed from 'double' to ''
                    - Modified property: prices
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'string'
                        - Format changed from 'double' to ''
                    - Modified property: quotas
                      - AdditionalProperties changed
                        - Type changed from 'number' to 'integer'
                        - Format changed from 'double' to ''

GET /api/proposal-requested-resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: requested_offering
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/NestedRequestedOffering
                    - Properties changed
                      - Modified property: components
                        - Items changed
                          - Properties changed
                            - New property: offering_uuid
                            - Modified property: limit_period
                              - Property 'OneOf' changed
                                - Schemas deleted: #/components/schemas/BlankEnum
                      - Modified property: plan_details
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/BasePublicPlan
                            - Properties changed
                              - Modified property: future_prices
                                - AdditionalProperties changed
                                  - Type changed from 'number' to 'string'
                                  - Format changed from 'double' to ''
                              - Modified property: minimal_price
                                - Type changed from 'number' to 'string'
                                - Format changed from 'double' to ''
                              - Modified property: prices
                                - AdditionalProperties changed
                                  - Type changed from 'number' to 'string'
                                  - Format changed from 'double' to ''
                              - Modified property: quotas
                                - AdditionalProperties changed
                                  - Type changed from 'number' to 'integer'
                                  - Format changed from 'double' to ''

GET /api/proposal-requested-resources/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: offering_uuid
                          - Modified property: limit_period
                            - Property 'OneOf' changed
                              - Schemas deleted: #/components/schemas/BlankEnum
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: future_prices
                              - AdditionalProperties changed
                                - Type changed from 'number' to 'string'
                                - Format changed from 'double' to ''
                            - Modified property: minimal_price
                              - Type changed from 'number' to 'string'
                              - Format changed from 'double' to ''
                            - Modified property: prices
                              - AdditionalProperties changed
                                - Type changed from 'number' to 'string'
                                - Format changed from 'double' to ''
                            - Modified property: quotas
                              - AdditionalProperties changed
                                - Type changed from 'number' to 'integer'
                                - Format changed from 'double' to ''

GET /api/rancher-apps/

- Deleted query param: uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''

HEAD /api/rancher-apps/

- Deleted query param: uuid

POST /api/rancher-apps/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/rancher-apps/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PATCH /api/rancher-apps/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PUT /api/rancher-apps/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

POST /api/rancher-catalogs/{uuid}/refresh/

- Request body changed

GET /api/rancher-clusters/

- Deleted query param: uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''

HEAD /api/rancher-clusters/

- Deleted query param: uuid

GET /api/rancher-clusters/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PATCH /api/rancher-clusters/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PUT /api/rancher-clusters/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

POST /api/rancher-clusters/{uuid}/create_management_security_group/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/rancher-ingresses/

- Deleted query param: uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''

HEAD /api/rancher-ingresses/

- Deleted query param: uuid

POST /api/rancher-ingresses/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/rancher-ingresses/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PATCH /api/rancher-ingresses/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PUT /api/rancher-ingresses/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/rancher-ingresses/{uuid}/yaml/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PUT /api/rancher-ingresses/{uuid}/yaml/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/rancher-services/

- Deleted query param: uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''

HEAD /api/rancher-services/

- Deleted query param: uuid

POST /api/rancher-services/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/rancher-services/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PATCH /api/rancher-services/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PUT /api/rancher-services/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/rancher-services/{uuid}/yaml/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PUT /api/rancher-services/{uuid}/yaml/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/roles/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: content_type
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/RoleType
                    - New enum values: [resource resource_project]

POST /api/roles/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: content_type
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/RoleType
                  - New enum values: [resource resource_project]

GET /api/roles/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: content_type
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/RoleType
                  - New enum values: [resource resource_project]

PATCH /api/roles/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: content_type
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/RoleType
                  - New enum values: [resource resource_project]

PUT /api/roles/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: content_type
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/RoleType
                  - New enum values: [resource resource_project]

GET /api/slurm-allocations/

- Deleted query param: uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''

HEAD /api/slurm-allocations/

- Deleted query param: uuid

POST /api/slurm-allocations/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/slurm-allocations/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PATCH /api/slurm-allocations/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PUT /api/slurm-allocations/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/slurm-jobs/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''

POST /api/slurm-jobs/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/slurm-jobs/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PATCH /api/slurm-jobs/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PUT /api/slurm-jobs/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

POST /api/support-issues/{uuid}/sync/

- Request body changed

POST /api/support-request-types-admin/reorder/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - New required property: items
          - Deleted required property: issue_type_name
          - Deleted required property: name
        - Properties changed
          - New property: items
          - Deleted property: is_active
          - Deleted property: issue_type_name
          - Deleted property: name
          - Deleted property: order

POST /api/support-request-types-admin/{uuid}/activate/

- Request body changed

POST /api/support-request-types-admin/{uuid}/deactivate/

- Request body changed

GET /api/user-permissions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: resource_uuid

GET /api/user-permissions/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: resource_uuid

GET /api/users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [address]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: address
              - Modified property: permissions
                - Items changed
                  - Properties changed
                    - New property: resource_uuid

POST /api/users/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: address
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: address
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: address
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: address
            - Modified property: permissions
              - Items changed
                - Properties changed
                  - New property: resource_uuid

GET /api/users/me/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [address]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: address
            - Modified property: permissions
              - Items changed
                - Properties changed
                  - New property: resource_uuid

GET /api/users/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [address]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: address
            - Modified property: permissions
              - Items changed
                - Properties changed
                  - New property: resource_uuid

PATCH /api/users/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: address
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: address
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: address
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: address
            - Modified property: permissions
              - Items changed
                - Properties changed
                  - New property: resource_uuid

PUT /api/users/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: address
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: address
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: address
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: address
            - Modified property: permissions
              - Items changed
                - Properties changed
                  - New property: resource_uuid

GET /api/vmware-disks/

- Deleted query param: uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''

HEAD /api/vmware-disks/

- Deleted query param: uuid

GET /api/vmware-disks/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/vmware-ports/

- Deleted query param: uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''

HEAD /api/vmware-ports/

- Deleted query param: uuid

GET /api/vmware-ports/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/vmware-virtual-machine/

- Deleted query param: uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: access_url
                - Property 'OneOf' changed
                  - Schemas added: subschema #1, subschema #2
                - Type changed from 'string' to ''

HEAD /api/vmware-virtual-machine/

- Deleted query param: uuid

POST /api/vmware-virtual-machine/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

GET /api/vmware-virtual-machine/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PATCH /api/vmware-virtual-machine/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

PUT /api/vmware-virtual-machine/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

POST /api/vmware-virtual-machine/{uuid}/create_disk/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

POST /api/vmware-virtual-machine/{uuid}/create_port/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: access_url
              - Property 'OneOf' changed
                - Schemas added: subschema #1, subschema #2
              - Type changed from 'string' to ''

POST /api/vmware-virtual-machine/{uuid}/reboot_guest/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/vmware-virtual-machine/{uuid}/reset/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/vmware-virtual-machine/{uuid}/shutdown_guest/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/vmware-virtual-machine/{uuid}/start/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/vmware-virtual-machine/{uuid}/stop/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/vmware-virtual-machine/{uuid}/suspend/

- Responses changed
  - Modified response: 200
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
