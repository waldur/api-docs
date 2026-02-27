# OpenAPI schema diff - 8.0.4

## For version 8.0.4

### New Endpoints: 24

---------------------
GET /api/marketplace-offering-users/profile_field_warnings/  
HEAD /api/marketplace-offering-users/profile_field_warnings/  
POST /api/marketplace-provider-resources/{uuid}/set_keycloak_scopes/  
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

### Deleted Endpoints: None

---------------------------

### Modified Endpoints: 507

---------------------------
GET /api/access-subnets/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/access-subnets/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/admin/arrow/billing-sync-items/

- Modified query param: billing_sync
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: billing_sync_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/admin/arrow/billing-sync-items/

- Modified query param: billing_sync
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: billing_sync_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/admin/arrow/billing-syncs/

- Modified query param: customer_mapping
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_mapping_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/admin/arrow/billing-syncs/

- Modified query param: customer_mapping
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_mapping_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/admin/arrow/billing-syncs/pending_records/

- Modified query param: customer_mapping
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_mapping_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/admin/arrow/billing-syncs/pending_records/

- Modified query param: customer_mapping
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_mapping_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/admin/arrow/consumption-records/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: resource_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/admin/arrow/consumption-records/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: resource_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/admin/arrow/customer-mappings/

- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: waldur_customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: waldur_customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/admin/arrow/customer-mappings/

- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: waldur_customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: waldur_customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/admin/arrow/vendor-offering-mappings/

- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/admin/arrow/vendor-offering-mappings/

- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/admin/arrow/vendor-offering-mappings/vendor_choices/

- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/admin/arrow/vendor-offering-mappings/vendor_choices/

- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/assignment-batches/

- Modified query param: call_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: reviewer_pool_entry_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: reviewer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/assignment-batches/

- Modified query param: call_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: reviewer_pool_entry_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: reviewer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/assignment-items/

- Modified query param: batch_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: call_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: proposal_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: reviewer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/assignment-items/

- Modified query param: batch_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: call_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: proposal_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: reviewer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/aws-images/

- Modified query param: region
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/aws-images/

- Modified query param: region
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/aws-instances/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/aws-instances/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/aws-sizes/

- Modified query param: region
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/aws-sizes/

- Modified query param: region
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/azure-images/

- Modified query param: location
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: location_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/azure-images/

- Modified query param: location
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: location_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/azure-locations/

- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/azure-locations/

- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/azure-public-ips/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_group
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: resource_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/azure-public-ips/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_group
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: resource_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/azure-sizes/

- Modified query param: location
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: location_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/azure-sizes/

- Modified query param: location
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: location_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/azure-sql-databases/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_group
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: resource_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: server
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: server_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/azure-sql-databases/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_group
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: resource_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: server
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: server_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/azure-sql-servers/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_group
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: resource_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/azure-sql-servers/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_group
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: resource_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/azure-virtualmachines/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_group
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: resource_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/azure-virtualmachines/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_group
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: resource_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/backend-resource-requests/

- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/backend-resource-requests/

- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/backend-resources/

- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/backend-resources/

- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/billing-total-cost/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

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
                      - New property: keycloak_base_group
                      - New property: keycloak_enabled
                      - New property: keycloak_group_name_template
                      - New property: keycloak_sync_frequency
                      - New property: keycloak_username_label

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
                    - New property: keycloak_base_group
                    - New property: keycloak_enabled
                    - New property: keycloak_group_name_template
                    - New property: keycloak_sync_frequency
                    - New property: keycloak_username_label

GET /api/booking-resources/

- Modified query param: category_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: connected_customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: parent_offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: plan_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_manager_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/booking-resources/

- Modified query param: category_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: connected_customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: parent_offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: plan_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_manager_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/call-managing-organisations/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/call-managing-organisations/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/call-managing-organisations/{uuid}/list_users/

- Modified query param: role
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/call-proposal-project-role-mappings/

- Modified query param: call_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/call-proposal-project-role-mappings/

- Modified query param: call_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/call-reviewer-pools/

- Modified query param: call_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: reviewer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/call-reviewer-pools/

- Modified query param: call_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: reviewer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/chat-messages/

- Modified query param: thread
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/chat-quota/usage/

- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Required changed from false to true

GET /api/chat-threads/

- Modified query param: user
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/checklists-admin-question-dependencies/

- Modified query param: depends_on_question_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: question_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/checklists-admin-question-dependencies/

- Modified query param: depends_on_question_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: question_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/checklists-admin-question-options/

- Modified query param: question_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/checklists-admin-question-options/

- Modified query param: question_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/checklists-admin-questions/

- Modified query param: checklist_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/checklists-admin-questions/

- Modified query param: checklist_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/coi-detection-jobs/

- Modified query param: call_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/coi-detection-jobs/

- Modified query param: call_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/coi-disclosures/

- Modified query param: call_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: reviewer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/coi-disclosures/

- Modified query param: call_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: reviewer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/component-user-usage-limits/

- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: resource_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/component-user-usage-limits/

- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: resource_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/conflicts-of-interest/

- Modified query param: call_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: proposal_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: reviewer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: round_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/conflicts-of-interest/

- Modified query param: call_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: proposal_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: reviewer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: round_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/customer-credits/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/customer-credits/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/customer-credits/{uuid}/consumptions/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/customer-permissions-reviews/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: reviewer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/customer-permissions-reviews/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: reviewer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/customers/

- New query param: accounting_is_running
- New query param: has_resources
- New query param: is_call_managing_organization
- New query param: is_service_provider
- New query param: service_provider_uuid
- New query param: user_uuid
- Modified query param: organization_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/customers/

- New query param: accounting_is_running
- New query param: has_resources
- New query param: is_call_managing_organization
- New query param: is_service_provider
- New query param: service_provider_uuid
- New query param: user_uuid
- Modified query param: organization_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/customers/countries/

- New query param: accounting_is_running
- New query param: has_resources
- New query param: is_call_managing_organization
- New query param: is_service_provider
- New query param: service_provider_uuid
- New query param: user_uuid
- Modified query param: organization_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/customers/countries/

- New query param: accounting_is_running
- New query param: has_resources
- New query param: is_call_managing_organization
- New query param: is_service_provider
- New query param: service_provider_uuid
- New query param: user_uuid
- Modified query param: organization_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/customers/{uuid}/history/

- New query param: accounting_is_running
- New query param: has_resources
- New query param: is_call_managing_organization
- New query param: is_service_provider
- New query param: service_provider_uuid
- New query param: user_uuid
- Modified query param: organization_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/customers/{uuid}/list_users/

- Modified query param: role
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/data-access-logs/

- Modified query param: accessor_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/data-access-logs/

- Modified query param: accessor_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/digitalocean-droplets/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/digitalocean-droplets/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/event-subscription-queues/

- Modified query param: event_subscription_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/event-subscription-queues/

- Modified query param: event_subscription_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/events-stats/

- New query param: event_type
- New query param: feature
- New query param: scope

HEAD /api/events-stats/

- New query param: event_type
- New query param: feature
- New query param: scope

GET /api/events/

- New query param: event_type
- New query param: feature
- New query param: scope
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/events/

- New query param: event_type
- New query param: feature
- New query param: scope
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/expertise-categories/

- Modified query param: parent_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/expertise-categories/

- Modified query param: parent_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/financial-reports/

- New query param: accounting_is_running
- New query param: customer_uuid
- New query param: month
- New query param: year
- Modified query param: organization_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/financial-reports/

- New query param: accounting_is_running
- New query param: customer_uuid
- New query param: month
- New query param: year
- Modified query param: organization_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/freeipa-profiles/

- Modified query param: user
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/freeipa-profiles/

- Modified query param: user
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/hooks-email/

- Modified query param: author_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/hooks-email/

- Modified query param: author_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/hooks-web/

- Modified query param: author_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/hooks-web/

- Modified query param: author_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/hooks/

- New query param: author_uuid
- New query param: is_active

HEAD /api/hooks/

- New query param: author_uuid
- New query param: is_active

GET /api/invoice-items/

- Modified query param: credit_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/invoice-items/

- Modified query param: credit_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/invoice-items/costs/

- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/invoice-items/costs/

- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/invoice-items/customer_costs_for_period/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/invoice-items/customer_costs_for_period/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/invoice-items/project_costs_for_period/

- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/invoice-items/project_costs_for_period/

- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/invoice-items/total_price/

- Modified query param: credit_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/invoice-items/total_price/

- Modified query param: credit_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/invoices/

- New query param: accounting_is_running
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/invoices/

- New query param: accounting_is_running
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/invoices/{uuid}/history/

- New query param: accounting_is_running
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/invoices/{uuid}/items/

- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uuid'
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uuid'
- Modified query param: provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uuid'

GET /api/invoices/{uuid}/stats/

- New query param: accounting_is_running
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uuid'

GET /api/keycloak-user-group-memberships/

- Modified query param: group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: role_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/keycloak-user-group-memberships/

- Modified query param: group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: role_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/keys/

- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/keys/

- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/keys/{uuid}/history/

- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/lexis-links/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/lexis-links/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/maintenance-announcement-template-offerings/

- Modified query param: maintenance_template_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/maintenance-announcement-template-offerings/

- Modified query param: maintenance_template_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/maintenance-announcements-template/

- Modified query param: service_provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/maintenance-announcements-template/

- Modified query param: service_provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/maintenance-announcements/

- Modified query param: service_provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/maintenance-announcements/

- Modified query param: service_provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-categories/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/marketplace-categories/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-category-columns/

- Modified query param: category_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/marketplace-category-columns/

- Modified query param: category_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-category-component-usages/

- New query param: scope

HEAD /api/marketplace-category-component-usages/

- New query param: scope

GET /api/marketplace-component-usages/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: resource_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/marketplace-component-usages/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: resource_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-component-user-usages/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: resource_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/marketplace-component-user-usages/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: resource_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-course-accounts/

- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/marketplace-course-accounts/

- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

POST /api/marketplace-course-accounts/create_bulk/

- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-customer-component-usage-policies/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: scope
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: scope_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/marketplace-customer-component-usage-policies/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: scope
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: scope_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-customer-estimated-cost-policies/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: scope
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: scope_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/marketplace-customer-estimated-cost-policies/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: scope
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: scope_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-customer-service-accounts/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/marketplace-customer-service-accounts/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-global-categories/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-integration-statuses/

- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: parent_offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/marketplace-integration-statuses/

- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: parent_offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-offering-estimated-cost-policies/

- Modified query param: scope
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: scope_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/marketplace-offering-estimated-cost-policies/

- Modified query param: scope
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: scope_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-offering-files/

- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: parent_offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/marketplace-offering-files/

- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: parent_offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-offering-permissions-log/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: role_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user_url
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'

HEAD /api/marketplace-offering-permissions-log/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: role_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user_url
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'

GET /api/marketplace-offering-permissions/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: role_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user_url
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'

HEAD /api/marketplace-offering-permissions/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: role_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user_url
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'

GET /api/marketplace-offering-referrals/

- New query param: scope

HEAD /api/marketplace-offering-referrals/

- New query param: scope

GET /api/marketplace-offering-terms-of-service/

- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/marketplace-offering-terms-of-service/

- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-offering-usage-policies/

- Modified query param: scope
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: scope_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/marketplace-offering-usage-policies/

- Modified query param: scope
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: scope_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-offering-user-checklist-completions/

- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
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
                      - New property: is_profile_complete
                      - New property: missing_profile_attributes
                      - New property: user_organization_registry_code

HEAD /api/marketplace-offering-user-checklist-completions/

- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

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
                    - New property: is_profile_complete
                    - New property: missing_profile_attributes
                    - New property: user_organization_registry_code

GET /api/marketplace-offering-user-roles/

- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: parent_offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: scope_type
              - New property: scope_type_label

HEAD /api/marketplace-offering-user-roles/

- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: parent_offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

POST /api/marketplace-offering-user-roles/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: scope_type
          - New property: scope_type_label
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: scope_type
            - New property: scope_type_label

GET /api/marketplace-offering-user-roles/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: scope_type
            - New property: scope_type_label

PATCH /api/marketplace-offering-user-roles/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: scope_type
          - New property: scope_type_label
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: scope_type
            - New property: scope_type_label

PUT /api/marketplace-offering-user-roles/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: scope_type
          - New property: scope_type_label
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: scope_type
            - New property: scope_type_label

GET /api/marketplace-offering-users/

- New query param: has_complete_profile
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [is_profile_complete missing_profile_attributes user_organization_registry_code]
- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: parent_offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: is_profile_complete
              - New property: missing_profile_attributes
              - New property: user_organization_registry_code

HEAD /api/marketplace-offering-users/

- New query param: has_complete_profile
- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: parent_offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

POST /api/marketplace-offering-users/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: is_profile_complete
            - New property: missing_profile_attributes
            - New property: user_organization_registry_code

GET /api/marketplace-offering-users/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [is_profile_complete missing_profile_attributes user_organization_registry_code]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: is_profile_complete
            - New property: missing_profile_attributes
            - New property: user_organization_registry_code

PATCH /api/marketplace-offering-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: is_profile_complete
            - New property: missing_profile_attributes
            - New property: user_organization_registry_code

PUT /api/marketplace-offering-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: is_profile_complete
            - New property: missing_profile_attributes
            - New property: user_organization_registry_code

GET /api/marketplace-orders/

- Modified query param: category_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: parent_offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: resource_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_manager_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/marketplace-orders/

- Modified query param: category_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: parent_offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: resource_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_manager_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

POST /api/marketplace-orders/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: attributes
            - Property 'OneOf' changed
              - Schemas deleted: #/components/schemas/AzureVirtualMachineCreateOrderAttributes, #/components/schemas/AzureSQLServerCreateOrderAttributes, #/components/schemas/MarketplaceOpenPortalCreateOrderAttributes, #/components/schemas/MarketplaceOpenPortalRemoteCreateOrderAttributes, #/components/schemas/OpenStackTenantCreateOrderAttributes, #/components/schemas/OpenStackInstanceCreateOrderAttributes, #/components/schemas/OpenStackVolumeCreateOrderAttributes, #/components/schemas/SlurmInvoicesSlurmPackageCreateOrderAttributes, #/components/schemas/VMwareVirtualMachineCreateOrderAttributes

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
                    - New property: keycloak_base_group
                    - New property: keycloak_enabled
                    - New property: keycloak_group_name_template
                    - New property: keycloak_sync_frequency
                    - New property: keycloak_username_label

GET /api/marketplace-plan-components/

- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: plan_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/marketplace-plan-components/

- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: plan_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-plans/

- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: parent_offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/marketplace-plans/

- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: parent_offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-plans/usage_stats/

- Modified query param: customer_provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Description changed from 'Filter by service provider's customer UUID.' to 'Filter by offering customer provider UUID.'
- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: parent_offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/marketplace-plans/usage_stats/

- Modified query param: customer_provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Description changed from 'Filter by service provider's customer UUID.' to 'Filter by offering customer provider UUID.'
- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: parent_offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-plans/{uuid}/history/

- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: parent_offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-project-estimated-cost-policies/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: scope
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: scope_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/marketplace-project-estimated-cost-policies/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: scope
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: scope_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-project-service-accounts/

- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/marketplace-project-service-accounts/

- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-project-update-requests/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/marketplace-project-update-requests/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-provider-offerings/

- New query param: importable
- Modified query param: allowed_customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: category_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: category_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: organization_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Style changed from 'form' to ''
  - Explode changed from true to null
  - Schema changed
    - Type changed from 'array' to 'string'
    - Format changed from '' to 'uuid'
    - Items changed
      - Schema deleted
- Modified query param: parent_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: scope_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_manager_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
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
                      - New property: keycloak_base_group
                      - New property: keycloak_enabled
                      - New property: keycloak_group_name_template
                      - New property: keycloak_sync_frequency
                      - New property: keycloak_username_label

HEAD /api/marketplace-provider-offerings/

- New query param: importable
- Modified query param: allowed_customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: category_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: category_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: organization_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Style changed from 'form' to ''
  - Explode changed from true to null
  - Schema changed
    - Type changed from 'array' to 'string'
    - Format changed from '' to 'uuid'
    - Items changed
      - Schema deleted
- Modified query param: parent_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: scope_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_manager_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

POST /api/marketplace-provider-offerings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: keycloak_base_group
              - New property: keycloak_enabled
              - New property: keycloak_group_name_template
              - New property: keycloak_sync_frequency
              - New property: keycloak_username_label
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: keycloak_base_group
              - New property: keycloak_enabled
              - New property: keycloak_group_name_template
              - New property: keycloak_sync_frequency
              - New property: keycloak_username_label
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: keycloak_base_group
              - New property: keycloak_enabled
              - New property: keycloak_group_name_template
              - New property: keycloak_sync_frequency
              - New property: keycloak_username_label
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
                    - New property: keycloak_base_group
                    - New property: keycloak_enabled
                    - New property: keycloak_group_name_template
                    - New property: keycloak_sync_frequency
                    - New property: keycloak_username_label

GET /api/marketplace-provider-offerings/groups/

- Modified query param: allowed_customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: category_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: category_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: organization_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Style changed from 'form' to ''
  - Explode changed from true to null
  - Schema changed
    - Type changed from 'array' to 'string'
    - Format changed from '' to 'uuid'
    - Items changed
      - Schema deleted
- Modified query param: parent_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: scope_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_manager_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/marketplace-provider-offerings/groups/

- Modified query param: allowed_customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: category_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: category_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: organization_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Style changed from 'form' to ''
  - Explode changed from true to null
  - Schema changed
    - Type changed from 'array' to 'string'
    - Format changed from '' to 'uuid'
    - Items changed
      - Schema deleted
- Modified query param: parent_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: scope_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_manager_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

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
                    - New property: keycloak_base_group
                    - New property: keycloak_enabled
                    - New property: keycloak_group_name_template
                    - New property: keycloak_sync_frequency
                    - New property: keycloak_username_label

GET /api/marketplace-provider-offerings/{uuid}/component_stats/

- New query param: importable
- Modified query param: allowed_customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: category_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: category_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: organization_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Style changed from 'form' to ''
  - Explode changed from true to null
  - Schema changed
    - Type changed from 'array' to 'string'
    - Format changed from '' to 'uuid'
    - Items changed
      - Schema deleted
- Modified query param: parent_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: scope_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_manager_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-provider-offerings/{uuid}/costs/

- New query param: importable
- Modified query param: allowed_customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: category_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: category_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: organization_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Style changed from 'form' to ''
  - Explode changed from true to null
  - Schema changed
    - Type changed from 'array' to 'string'
    - Format changed from '' to 'uuid'
    - Items changed
      - Schema deleted
- Modified query param: parent_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: scope_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_manager_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-provider-offerings/{uuid}/customers/

- New query param: importable
- Modified query param: allowed_customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: category_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: category_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: organization_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Style changed from 'form' to ''
  - Explode changed from true to null
  - Schema changed
    - Type changed from 'array' to 'string'
    - Format changed from '' to 'uuid'
    - Items changed
      - Schema deleted
- Modified query param: parent_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: scope_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_manager_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-provider-offerings/{uuid}/history/

- New query param: importable
- Modified query param: allowed_customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: category_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: category_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: organization_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Style changed from 'form' to ''
  - Explode changed from true to null
  - Schema changed
    - Type changed from 'array' to 'string'
    - Format changed from '' to 'uuid'
    - Items changed
      - Schema deleted
- Modified query param: parent_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: scope_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_manager_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-provider-offerings/{uuid}/list_course_accounts/

- New query param: importable
- Modified query param: allowed_customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: category_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: category_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: organization_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Style changed from 'form' to ''
  - Explode changed from true to null
  - Schema changed
    - Type changed from 'array' to 'string'
    - Format changed from '' to 'uuid'
    - Items changed
      - Schema deleted
- Modified query param: parent_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: scope_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_manager_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-provider-offerings/{uuid}/list_customer_service_accounts/

- New query param: importable
- Modified query param: allowed_customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: category_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: category_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: organization_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Style changed from 'form' to ''
  - Explode changed from true to null
  - Schema changed
    - Type changed from 'array' to 'string'
    - Format changed from '' to 'uuid'
    - Items changed
      - Schema deleted
- Modified query param: parent_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: scope_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_manager_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-provider-offerings/{uuid}/list_project_service_accounts/

- New query param: importable
- Modified query param: allowed_customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: category_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: category_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: organization_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Style changed from 'form' to ''
  - Explode changed from true to null
  - Schema changed
    - Type changed from 'array' to 'string'
    - Format changed from '' to 'uuid'
    - Items changed
      - Schema deleted
- Modified query param: parent_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: scope_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_manager_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-provider-offerings/{uuid}/list_users/

- Modified query param: role
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user
  - Extensions changed
    - New extension: x-waldur-operation-id

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
                    - New property: keycloak_base_group
                    - New property: keycloak_enabled
                    - New property: keycloak_group_name_template
                    - New property: keycloak_sync_frequency
                    - New property: keycloak_username_label

PATCH /api/marketplace-provider-offerings/{uuid}/update-user-attribute-config/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: expose_active_isds
          - New property: expose_organization_registry_code
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: expose_active_isds
            - New property: expose_organization_registry_code

POST /api/marketplace-provider-offerings/{uuid}/update-user-attribute-config/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: expose_active_isds
          - New property: expose_organization_registry_code
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: expose_active_isds
            - New property: expose_organization_registry_code

PUT /api/marketplace-provider-offerings/{uuid}/update-user-attribute-config/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: expose_active_isds
          - New property: expose_organization_registry_code
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: expose_active_isds
            - New property: expose_organization_registry_code

POST /api/marketplace-provider-offerings/{uuid}/update_integration/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: keycloak_base_group
              - New property: keycloak_enabled
              - New property: keycloak_group_name_template
              - New property: keycloak_sync_frequency
              - New property: keycloak_username_label

GET /api/marketplace-provider-offerings/{uuid}/user-attribute-config/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: expose_active_isds
            - New property: expose_organization_registry_code

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
                    - New property: keycloak_base_group
                    - New property: keycloak_enabled
                    - New property: keycloak_group_name_template
                    - New property: keycloak_sync_frequency
                    - New property: keycloak_username_label

GET /api/marketplace-provider-resources/

- New query param: scope
- Modified query param: category_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: parent_offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: plan_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_manager_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/marketplace-provider-resources/

- New query param: scope
- Modified query param: category_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: parent_offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: plan_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_manager_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-provider-resources/{uuid}/history/

- New query param: scope
- Modified query param: category_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: parent_offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: plan_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_manager_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

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
                    - New property: keycloak_base_group
                    - New property: keycloak_enabled
                    - New property: keycloak_group_name_template
                    - New property: keycloak_sync_frequency
                    - New property: keycloak_username_label

GET /api/marketplace-public-offerings/

- Modified query param: allowed_customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: category_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: category_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: organization_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Style changed from 'form' to ''
  - Explode changed from true to null
  - Schema changed
    - Type changed from 'array' to 'string'
    - Format changed from '' to 'uuid'
    - Items changed
      - Schema deleted
- Modified query param: parent_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: scope_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_manager_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
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
                      - New property: keycloak_base_group
                      - New property: keycloak_enabled
                      - New property: keycloak_group_name_template
                      - New property: keycloak_sync_frequency
                      - New property: keycloak_username_label

HEAD /api/marketplace-public-offerings/

- Modified query param: allowed_customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: category_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: category_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: organization_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Style changed from 'form' to ''
  - Explode changed from true to null
  - Schema changed
    - Type changed from 'array' to 'string'
    - Format changed from '' to 'uuid'
    - Items changed
      - Schema deleted
- Modified query param: parent_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: scope_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_manager_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

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
                    - New property: keycloak_base_group
                    - New property: keycloak_enabled
                    - New property: keycloak_group_name_template
                    - New property: keycloak_sync_frequency
                    - New property: keycloak_username_label

GET /api/marketplace-resource-users/

- Modified query param: resource
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: resource_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: role_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/marketplace-resource-users/

- Modified query param: resource
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: resource_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: role_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-resources/

- New query param: scope
- Modified query param: category_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: parent_offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: plan_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_manager_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/marketplace-resources/

- New query param: scope
- Modified query param: category_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: parent_offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: plan_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_manager_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-resources/{uuid}/history/

- New query param: scope
- Modified query param: category_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: parent_offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: plan_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_manager_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

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
                    - New property: keycloak_base_group
                    - New property: keycloak_enabled
                    - New property: keycloak_group_name_template
                    - New property: keycloak_sync_frequency
                    - New property: keycloak_username_label

GET /api/marketplace-robot-accounts/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: resource_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
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
                      - New property: keycloak_base_group
                      - New property: keycloak_enabled
                      - New property: keycloak_group_name_template
                      - New property: keycloak_sync_frequency
                      - New property: keycloak_username_label

HEAD /api/marketplace-robot-accounts/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: resource_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

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
                    - New property: keycloak_base_group
                    - New property: keycloak_enabled
                    - New property: keycloak_group_name_template
                    - New property: keycloak_sync_frequency
                    - New property: keycloak_username_label

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
                    - New property: keycloak_base_group
                    - New property: keycloak_enabled
                    - New property: keycloak_group_name_template
                    - New property: keycloak_sync_frequency
                    - New property: keycloak_username_label

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
                    - New property: keycloak_base_group
                    - New property: keycloak_enabled
                    - New property: keycloak_group_name_template
                    - New property: keycloak_sync_frequency
                    - New property: keycloak_username_label

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
                    - New property: keycloak_base_group
                    - New property: keycloak_enabled
                    - New property: keycloak_group_name_template
                    - New property: keycloak_sync_frequency
                    - New property: keycloak_username_label

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
                    - New property: keycloak_base_group
                    - New property: keycloak_enabled
                    - New property: keycloak_group_name_template
                    - New property: keycloak_sync_frequency
                    - New property: keycloak_username_label

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
                    - New property: keycloak_base_group
                    - New property: keycloak_enabled
                    - New property: keycloak_group_name_template
                    - New property: keycloak_sync_frequency
                    - New property: keycloak_username_label

GET /api/marketplace-runtime-states/

- Modified query param: category_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-screenshots/

- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: parent_offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/marketplace-screenshots/

- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: parent_offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

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
                    - New property: keycloak_base_group
                    - New property: keycloak_enabled
                    - New property: keycloak_group_name_template
                    - New property: keycloak_sync_frequency
                    - New property: keycloak_username_label

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
                    - New property: keycloak_base_group
                    - New property: keycloak_enabled
                    - New property: keycloak_group_name_template
                    - New property: keycloak_sync_frequency
                    - New property: keycloak_username_label

GET /api/marketplace-service-providers/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/marketplace-service-providers/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-service-providers/{service_provider_uuid}/compliance/offering_users/

- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-service-providers/{service_provider_uuid}/course_accounts/

- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-service-providers/{service_provider_uuid}/customer_projects/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-service-providers/{service_provider_uuid}/customers/

- Modified query param: organization_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-service-providers/{service_provider_uuid}/keys/

- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-service-providers/{service_provider_uuid}/offerings/

- Modified query param: allowed_customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: category_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: category_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: organization_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Style changed from 'form' to ''
  - Explode changed from true to null
  - Schema changed
    - Type changed from 'array' to 'string'
    - Format changed from '' to 'uuid'
    - Items changed
      - Schema deleted
- Modified query param: parent_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource_project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: scope_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_manager_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-service-providers/{service_provider_uuid}/project_permissions/

- Modified query param: role_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user_url
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'

GET /api/marketplace-service-providers/{service_provider_uuid}/project_service_accounts/

- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-service-providers/{service_provider_uuid}/projects/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-service-providers/{service_provider_uuid}/user_customers/

- Modified query param: organization_group_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-service-providers/{service_provider_uuid}/users/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [active_isds birth_date civil_number country_of_residence eduperson_assurance gender identity_source job_title nationalities nationality organization_country organization_registry_code organization_type personal_title place_of_birth]
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: active_isds
              - New property: birth_date
              - New property: civil_number
              - New property: country_of_residence
              - New property: eduperson_assurance
              - New property: gender
              - New property: identity_source
              - New property: job_title
              - New property: nationalities
              - New property: nationality
              - New property: organization_country
              - New property: organization_registry_code
              - New property: organization_type
              - New property: personal_title
              - New property: place_of_birth

GET /api/marketplace-service-providers/{uuid}/list_users/

- Modified query param: role
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-site-agent-identities/

- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: offering
                - Description changed from 'UUID of an offering with type 'Marketplace.Slurm'. Only site-agent offerings are accepted.' to 'UUID of an offering with a site-agent compatible type.'

HEAD /api/marketplace-site-agent-identities/

- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

POST /api/marketplace-site-agent-identities/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: offering
            - Description changed from 'UUID of an offering with type 'Marketplace.Slurm'. Only site-agent offerings are accepted.' to 'UUID of an offering with a site-agent compatible type.'
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering
              - Description changed from 'UUID of an offering with type 'Marketplace.Slurm'. Only site-agent offerings are accepted.' to 'UUID of an offering with a site-agent compatible type.'

GET /api/marketplace-site-agent-identities/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering
              - Description changed from 'UUID of an offering with type 'Marketplace.Slurm'. Only site-agent offerings are accepted.' to 'UUID of an offering with a site-agent compatible type.'

PUT /api/marketplace-site-agent-identities/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: offering
            - Description changed from 'UUID of an offering with type 'Marketplace.Slurm'. Only site-agent offerings are accepted.' to 'UUID of an offering with a site-agent compatible type.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: offering
              - Description changed from 'UUID of an offering with type 'Marketplace.Slurm'. Only site-agent offerings are accepted.' to 'UUID of an offering with a site-agent compatible type.'

GET /api/marketplace-site-agent-processors/

- Modified query param: service_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/marketplace-site-agent-processors/

- Modified query param: service_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-site-agent-services/

- Modified query param: identity_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/marketplace-site-agent-services/

- Modified query param: identity_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-slurm-periodic-usage-policies/

- Modified query param: scope
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: scope_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/marketplace-slurm-periodic-usage-policies/

- Modified query param: scope
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: scope_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-slurm-periodic-usage-policies/{uuid}/command-history/

- Modified query param: scope
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: scope_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-slurm-periodic-usage-policies/{uuid}/evaluation-logs/

- Modified query param: scope
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: scope_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-software-packages/

- New query param: is_extension
- New query param: name_exact
- Modified query param: catalog_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/marketplace-software-packages/

- New query param: is_extension
- New query param: name_exact
- Modified query param: catalog_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-software-targets/

- Modified query param: catalog_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: package_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: version_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/marketplace-software-targets/

- Modified query param: catalog_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: package_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: version_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-software-versions/

- Modified query param: catalog_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: package_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/marketplace-software-versions/

- Modified query param: catalog_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: package_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-tags/

- Modified query param: created_by
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/marketplace-tags/

- Modified query param: created_by
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/marketplace-user-offering-consents/

- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/marketplace-user-offering-consents/

- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/onboarding-justifications/

- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: verification_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/onboarding-justifications/

- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: verification_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/onboarding-question-metadata/

- Modified query param: checklist_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: question_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/onboarding-question-metadata/

- Modified query param: checklist_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: question_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/onboarding-verifications/

- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/onboarding-verifications/

- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/openportal-allocation-user-usage/

- Modified query param: allocation
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: allocation_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/openportal-allocation-user-usage/

- Modified query param: allocation
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: allocation_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/openportal-allocations/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/openportal-allocations/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/openportal-associations/

- Modified query param: allocation
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: allocation_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/openportal-associations/

- Modified query param: allocation
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: allocation_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/openportal-managed-projects/

- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: project_template
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: project_template_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
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
                                    - New property: keycloak_base_group
                                    - New property: keycloak_enabled
                                    - New property: keycloak_group_name_template
                                    - New property: keycloak_sync_frequency
                                    - New property: keycloak_username_label

HEAD /api/openportal-managed-projects/

- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: project_template
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: project_template_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

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
                                  - New property: keycloak_base_group
                                  - New property: keycloak_enabled
                                  - New property: keycloak_group_name_template
                                  - New property: keycloak_sync_frequency
                                  - New property: keycloak_username_label

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
                            - New property: keycloak_base_group
                            - New property: keycloak_enabled
                            - New property: keycloak_group_name_template
                            - New property: keycloak_sync_frequency
                            - New property: keycloak_username_label

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
                          - New property: keycloak_base_group
                          - New property: keycloak_enabled
                          - New property: keycloak_group_name_template
                          - New property: keycloak_sync_frequency
                          - New property: keycloak_username_label

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
                          - New property: keycloak_base_group
                          - New property: keycloak_enabled
                          - New property: keycloak_group_name_template
                          - New property: keycloak_sync_frequency
                          - New property: keycloak_username_label

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
                          - New property: keycloak_base_group
                          - New property: keycloak_enabled
                          - New property: keycloak_group_name_template
                          - New property: keycloak_sync_frequency
                          - New property: keycloak_username_label

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
                          - New property: keycloak_base_group
                          - New property: keycloak_enabled
                          - New property: keycloak_group_name_template
                          - New property: keycloak_sync_frequency
                          - New property: keycloak_username_label

GET /api/openportal-projectinfo/

- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/openportal-projectinfo/

- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

DELETE /api/openportal-projectinfo/{project}/

- Modified path param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'

GET /api/openportal-projectinfo/{project}/

- Modified path param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'

PATCH /api/openportal-projectinfo/{project}/

- Modified path param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'

PUT /api/openportal-projectinfo/{project}/

- Modified path param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'

PUT /api/openportal-projectinfo/{project}/set_allowed_destinations/

- Modified path param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'

PUT /api/openportal-projectinfo/{project}/set_shortname/

- Modified path param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'

GET /api/openportal-remote-allocations/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/openportal-remote-allocations/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/openportal-remote-associations/

- Modified query param: allocation
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: allocation_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/openportal-remote-associations/

- Modified query param: allocation
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: allocation_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/openportal-unmanaged-projects/

- New query param: accounting_is_running
- New query param: user_uuid
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/openportal-unmanaged-projects/

- New query param: accounting_is_running
- New query param: user_uuid
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/openportal-unmanaged-projects/{uuid}/list_users/

- Modified query param: role
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/openportal-userinfo/

- Modified query param: user
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/openportal-userinfo/

- Modified query param: user
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

DELETE /api/openportal-userinfo/{user}/

- Modified path param: user
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'

GET /api/openportal-userinfo/{user}/

- Modified path param: user
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'

PATCH /api/openportal-userinfo/{user}/

- Modified path param: user
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'

PUT /api/openportal-userinfo/{user}/

- Modified path param: user
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'

PUT /api/openportal-userinfo/{user}/set_shortname/

- Modified path param: user
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'

GET /api/openstack-backups/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: instance
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: instance_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/openstack-backups/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: instance
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: instance_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

POST /api/openstack-backups/{uuid}/restore/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: server_group
              - Properties changed
                - Modified property: policy
                  - Property 'AllOf' changed
                    - Modified schema: #/components/schemas/PolicyEnum
                      - New enum values: [anti-affinity soft-affinity soft-anti-affinity]

GET /api/openstack-external-networks/

- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/openstack-external-networks/

- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/openstack-flavors/

- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/openstack-flavors/

- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/openstack-floating-ips/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/openstack-floating-ips/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/openstack-images/

- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/openstack-images/

- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/openstack-instance-availability-zones/

- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/openstack-instance-availability-zones/

- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/openstack-instances/

- New query param: o
- Modified query param: attach_volume_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: server_group
                - Properties changed
                  - Modified property: policy
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/PolicyEnum
                        - New enum values: [anti-affinity soft-affinity soft-anti-affinity]

HEAD /api/openstack-instances/

- New query param: o
- Modified query param: attach_volume_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/openstack-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: server_group
              - Properties changed
                - Modified property: policy
                  - Property 'AllOf' changed
                    - Modified schema: #/components/schemas/PolicyEnum
                      - New enum values: [anti-affinity soft-affinity soft-anti-affinity]

PATCH /api/openstack-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: server_group
              - Properties changed
                - Modified property: policy
                  - Property 'AllOf' changed
                    - Modified schema: #/components/schemas/PolicyEnum
                      - New enum values: [anti-affinity soft-affinity soft-anti-affinity]

PUT /api/openstack-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: server_group
              - Properties changed
                - Modified property: policy
                  - Property 'AllOf' changed
                    - Modified schema: #/components/schemas/PolicyEnum
                      - New enum values: [anti-affinity soft-affinity soft-anti-affinity]

GET /api/openstack-marketplace-tenants/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/openstack-marketplace-tenants/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/openstack-migrations/

- Modified query param: dst_resource_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: src_resource_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/openstack-migrations/

- Modified query param: dst_resource_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: src_resource_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/openstack-network-rbac-policies/

- Modified query param: network
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: network_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: target_tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: target_tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/openstack-network-rbac-policies/

- Modified query param: network
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: network_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: target_tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: target_tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/openstack-networks/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/openstack-networks/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/openstack-ports/

- Modified query param: network_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/openstack-ports/

- Modified query param: network_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/openstack-routers/

- Modified query param: tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/openstack-routers/

- Modified query param: tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/openstack-security-groups/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/openstack-security-groups/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/openstack-server-groups/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: policy
                - Property 'OneOf' changed
                  - Modified schema: #/components/schemas/PolicyEnum
                    - New enum values: [anti-affinity soft-affinity soft-anti-affinity]
                - Description changed from 'Server group policy determining the rules for scheduling servers in this group' to 'affinity — all instances are placed on the same hypervisor. anti-affinity — all instances are placed on different hypervisors. soft-affinity — instances are placed on the same hypervisor if possible, but not enforced. soft-anti-affinity — instances are placed on different hypervisors if possible, but not enforced.'

HEAD /api/openstack-server-groups/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

POST /api/openstack-server-groups/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: policy
            - Property 'OneOf' changed
              - Modified schema: #/components/schemas/PolicyEnum
                - New enum values: [anti-affinity soft-affinity soft-anti-affinity]
            - Description changed from 'Server group policy determining the rules for scheduling servers in this group' to 'affinity — all instances are placed on the same hypervisor. anti-affinity — all instances are placed on different hypervisors. soft-affinity — instances are placed on the same hypervisor if possible, but not enforced. soft-anti-affinity — instances are placed on different hypervisors if possible, but not enforced.'
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: policy
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/PolicyEnum
                  - New enum values: [anti-affinity soft-affinity soft-anti-affinity]
              - Description changed from 'Server group policy determining the rules for scheduling servers in this group' to 'affinity — all instances are placed on the same hypervisor. anti-affinity — all instances are placed on different hypervisors. soft-affinity — instances are placed on the same hypervisor if possible, but not enforced. soft-anti-affinity — instances are placed on different hypervisors if possible, but not enforced.'

GET /api/openstack-server-groups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: policy
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/PolicyEnum
                  - New enum values: [anti-affinity soft-affinity soft-anti-affinity]
              - Description changed from 'Server group policy determining the rules for scheduling servers in this group' to 'affinity — all instances are placed on the same hypervisor. anti-affinity — all instances are placed on different hypervisors. soft-affinity — instances are placed on the same hypervisor if possible, but not enforced. soft-anti-affinity — instances are placed on different hypervisors if possible, but not enforced.'

GET /api/openstack-snapshots/

- Modified query param: backup
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: backup_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: source_volume
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: source_volume_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/openstack-snapshots/

- Modified query param: backup
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: backup_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: source_volume
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: source_volume_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/openstack-subnets/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: network
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: network_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/openstack-subnets/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: network
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: network_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/openstack-tenants/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/openstack-tenants/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/openstack-tenants/{uuid}/backend_instances/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/openstack-tenants/{uuid}/backend_volumes/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

POST /api/openstack-tenants/{uuid}/create_server_group/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: policy
            - Property 'OneOf' changed
              - Modified schema: #/components/schemas/PolicyEnum
                - New enum values: [anti-affinity soft-affinity soft-anti-affinity]
            - Description changed from 'Server group policy determining the rules for scheduling servers in this group' to 'affinity — all instances are placed on the same hypervisor. anti-affinity — all instances are placed on different hypervisors. soft-affinity — instances are placed on the same hypervisor if possible, but not enforced. soft-anti-affinity — instances are placed on different hypervisors if possible, but not enforced.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: policy
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/PolicyEnum
                  - New enum values: [anti-affinity soft-affinity soft-anti-affinity]
              - Description changed from 'Server group policy determining the rules for scheduling servers in this group' to 'affinity — all instances are placed on the same hypervisor. anti-affinity — all instances are placed on different hypervisors. soft-affinity — instances are placed on the same hypervisor if possible, but not enforced. soft-anti-affinity — instances are placed on different hypervisors if possible, but not enforced.'

GET /api/openstack-volume-availability-zones/

- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/openstack-volume-availability-zones/

- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/openstack-volume-types/

- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/openstack-volume-types/

- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/openstack-volumes/

- Modified query param: attach_instance_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: instance
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: instance_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: snapshot
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: snapshot_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/openstack-volumes/

- Modified query param: attach_instance_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: instance
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: instance_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: snapshot
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: snapshot_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: tenant
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: tenant_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/organization-groups/

- Modified query param: parent
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/organization-groups/

- Modified query param: parent
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/override-settings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: ENFORCE_OFFERING_USER_PROFILE_COMPLETENESS
            - New property: FONT_FAMILY
            - New property: LLM_CHAT_HISTORY_LIMIT
            - Deleted property: SITE_LOGO

POST /api/override-settings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: ENFORCE_OFFERING_USER_PROFILE_COMPLETENESS
          - New property: FONT_FAMILY
          - New property: LLM_CHAT_HISTORY_LIMIT
          - Deleted property: SITE_LOGO
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: ENFORCE_OFFERING_USER_PROFILE_COMPLETENESS
          - New property: FONT_FAMILY
          - New property: LLM_CHAT_HISTORY_LIMIT
          - Deleted property: SITE_LOGO
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: ENFORCE_OFFERING_USER_PROFILE_COMPLETENESS
          - New property: FONT_FAMILY
          - New property: LLM_CHAT_HISTORY_LIMIT
          - Deleted property: SITE_LOGO

GET /api/payment-profiles/

- Modified query param: organization
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: organization_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/payment-profiles/

- Modified query param: organization
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: organization_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/payments/

- Modified query param: profile
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: profile_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/payments/

- Modified query param: profile
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: profile_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/project-credits/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/project-credits/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/project-permissions-reviews/

- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: reviewer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/project-permissions-reviews/

- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: reviewer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/projects/

- New query param: accounting_is_running
- New query param: user_uuid
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/projects/

- New query param: accounting_is_running
- New query param: user_uuid
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/projects/{uuid}/list_users/

- Modified query param: role
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/promotions-campaigns/

- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/promotions-campaigns/

- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/proposal-proposals/

- Modified query param: call_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: created_by_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: organization_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: round
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: round_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/proposal-proposals/

- Modified query param: call_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: created_by_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: organization_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: round
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: round_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/proposal-proposals/{uuid}/list_users/

- Modified query param: role
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/proposal-protected-calls/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offerings_provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/proposal-protected-calls/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offerings_provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/proposal-protected-calls/available_compliance_checklists/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offerings_provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/proposal-protected-calls/available_compliance_checklists/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offerings_provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/proposal-protected-calls/{uuid}/conflicts/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offerings_provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/proposal-protected-calls/{uuid}/list_users/

- Modified query param: role
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/proposal-protected-calls/{uuid}/proposals/{proposal_uuid}/compliance-answers/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offerings_provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/proposal-protected-calls/{uuid}/proposed-assignments/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offerings_provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

POST /api/proposal-protected-calls/{uuid}/reviewer-pool/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offerings_provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/proposal-protected-calls/{uuid}/suggestions/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offerings_provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/proposal-public-calls/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offerings_provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/proposal-public-calls/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offerings_provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/proposal-requested-offerings/

- Modified query param: call
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: call_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: organization_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/proposal-requested-offerings/

- Modified query param: call
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: call_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: organization_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/proposal-requested-resources/

- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: proposal
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: proposal_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: resource_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/proposal-requested-resources/

- Modified query param: offering
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: proposal
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: proposal_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: resource
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: resource_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/proposal-reviews/

- Modified query param: call_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: organization_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: proposal
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: proposal_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: reviewer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: round_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/proposal-reviews/

- Modified query param: call_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: organization_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: proposal
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: proposal_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: reviewer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: round_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/provider-invoice-items/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/provider-invoice-items/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: offering_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/public-maintenance-announcements/

- Modified query param: service_provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/public-maintenance-announcements/

- Modified query param: service_provider_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/rancher-apps/

- Modified query param: cluster_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: namespace_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: template_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/rancher-apps/

- Modified query param: cluster_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: namespace_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: template_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/rancher-cluster-security-groups/

- Modified query param: cluster_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/rancher-cluster-security-groups/

- Modified query param: cluster_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/rancher-clusters/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/rancher-clusters/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/rancher-hpas/

- Modified query param: cluster_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: namespace_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: workload_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/rancher-hpas/

- Modified query param: cluster_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: namespace_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: workload_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/rancher-ingresses/

- Modified query param: cluster_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: namespace_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: rancher_project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/rancher-ingresses/

- Modified query param: cluster_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: namespace_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: rancher_project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/rancher-namespaces/

- Modified query param: cluster_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/rancher-namespaces/

- Modified query param: cluster_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/rancher-nodes/

- Modified query param: cluster_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/rancher-nodes/

- Modified query param: cluster_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/rancher-projects/

- Modified query param: cluster_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/rancher-projects/

- Modified query param: cluster_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/rancher-role-templates/

- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/rancher-role-templates/

- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/rancher-services/

- Modified query param: cluster_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: namespace_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: rancher_project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/rancher-services/

- Modified query param: cluster_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: namespace_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: rancher_project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/rancher-templates/

- Modified query param: catalog_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: cluster_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/rancher-templates/

- Modified query param: catalog_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: cluster_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/rancher-users/

- Modified query param: cluster_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/rancher-users/

- Modified query param: cluster_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/rancher-workloads/

- Modified query param: cluster_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: namespace_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/rancher-workloads/

- Modified query param: cluster_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: namespace_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/reviewer-bids/

- Modified query param: call_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: proposal_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: reviewer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/reviewer-bids/

- Modified query param: call_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: proposal_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: reviewer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/reviewer-bids/my-bids/

- Modified query param: call_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: proposal_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: reviewer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/reviewer-bids/my-bids/

- Modified query param: call_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: proposal_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: reviewer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/reviewer-profiles/

- Modified query param: expertise_category_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/reviewer-profiles/

- Modified query param: expertise_category_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/reviewer-suggestions/

- Modified query param: call_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: reviewer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/reviewer-suggestions/

- Modified query param: call_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: reviewer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/service-settings/

- New query param: scope
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/service-settings/

- New query param: scope
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/slurm-allocation-user-usage/

- Modified query param: allocation
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: allocation_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/slurm-allocation-user-usage/

- Modified query param: allocation
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: allocation_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/slurm-allocations/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/slurm-allocations/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/slurm-associations/

- Modified query param: allocation
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: allocation_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/slurm-associations/

- Modified query param: allocation
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: allocation_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/support-attachments/

- Modified query param: issue
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: issue_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/support-attachments/

- Modified query param: issue
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: issue_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/support-comments/

- New query param: resource
- Modified query param: author_user
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: issue
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: issue_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/support-comments/

- New query param: resource
- Modified query param: author_user
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: issue
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: issue_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/support-feedbacks/

- Modified query param: issue
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: issue_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/support-feedbacks/

- Modified query param: issue
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: issue_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/support-issues/

- New query param: resource
- Modified query param: assignee
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: caller
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: reporter
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: resource_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/support-issues/

- New query param: resource
- Modified query param: assignee
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: caller
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: reporter
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: resource_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/user-actions/

- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/user-actions/

- Modified query param: user_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/user-group-invitations/

- New query param: scope
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: role_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/user-group-invitations/

- New query param: scope
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: role_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/user-invitations/

- New query param: scope
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: role_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/user-invitations/

- New query param: scope
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: role_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/user-permission-requests/

- New query param: scope
- Modified query param: created_by
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: invitation
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/user-permission-requests/

- New query param: scope
- Modified query param: created_by
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: invitation
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/user-permissions/

- Modified query param: role_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user_url
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'

HEAD /api/user-permissions/

- Modified query param: role_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: user_url
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'

GET /api/users/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/users/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/users/user_active_status_count/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/users/user_active_status_count/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/users/user_language_count/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/users/user_language_count/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/users/user_registration_trend/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/users/user_registration_trend/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/users/{uuid}/data_access_history/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/users/{uuid}/history/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/vmware-clusters/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/vmware-clusters/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/vmware-datastores/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/vmware-datastores/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/vmware-disks/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: vm
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: vm_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/vmware-disks/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: vm
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: vm_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/vmware-folders/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/vmware-folders/

- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/vmware-networks/

- Modified query param: customer_pair_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/vmware-networks/

- Modified query param: customer_pair_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/vmware-ports/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: network
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: network_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: vm
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: vm_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/vmware-ports/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: network
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: network_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: vm
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: vm_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/vmware-templates/

- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/vmware-templates/

- Modified query param: settings
  - Extensions changed
    - New extension: x-waldur-operation-id
  - Schema changed
    - Format changed from '' to 'uri'
- Modified query param: settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

GET /api/vmware-virtual-machine/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id

HEAD /api/vmware-virtual-machine/

- Modified query param: customer
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: customer_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: project_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
- Modified query param: service_settings_uuid
  - Extensions changed
    - New extension: x-waldur-operation-id
