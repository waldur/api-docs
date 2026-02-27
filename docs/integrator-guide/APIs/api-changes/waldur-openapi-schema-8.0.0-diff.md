# OpenAPI schema diff - 8.0.0

## For version 8.0.0

### New Endpoints: 235

----------------------
GET /api/admin/arrow/billing-sync-items/  
HEAD /api/admin/arrow/billing-sync-items/  
GET /api/admin/arrow/billing-sync-items/{uuid}/  
GET /api/admin/arrow/billing-syncs/  
HEAD /api/admin/arrow/billing-syncs/  
POST /api/admin/arrow/billing-syncs/cleanup_consumption/  
GET /api/admin/arrow/billing-syncs/consumption_statistics/  
HEAD /api/admin/arrow/billing-syncs/consumption_statistics/  
GET /api/admin/arrow/billing-syncs/consumption_status/  
HEAD /api/admin/arrow/billing-syncs/consumption_status/  
POST /api/admin/arrow/billing-syncs/fetch_billing_export/  
POST /api/admin/arrow/billing-syncs/fetch_consumption/  
POST /api/admin/arrow/billing-syncs/fetch_license_info/  
POST /api/admin/arrow/billing-syncs/pause_sync/  
GET /api/admin/arrow/billing-syncs/pending_records/  
HEAD /api/admin/arrow/billing-syncs/pending_records/  
POST /api/admin/arrow/billing-syncs/reconcile/  
POST /api/admin/arrow/billing-syncs/resume_sync/  
POST /api/admin/arrow/billing-syncs/sync_resource_historical_consumption/  
POST /api/admin/arrow/billing-syncs/sync_resources/  
POST /api/admin/arrow/billing-syncs/trigger_consumption_sync/  
POST /api/admin/arrow/billing-syncs/trigger_reconciliation/  
POST /api/admin/arrow/billing-syncs/trigger_sync/  
GET /api/admin/arrow/billing-syncs/{uuid}/  
GET /api/admin/arrow/consumption-records/  
HEAD /api/admin/arrow/consumption-records/  
GET /api/admin/arrow/consumption-records/{uuid}/  
GET /api/admin/arrow/customer-mappings/  
HEAD /api/admin/arrow/customer-mappings/  
POST /api/admin/arrow/customer-mappings/  
GET /api/admin/arrow/customer-mappings/available_customers/  
HEAD /api/admin/arrow/customer-mappings/available_customers/  
POST /api/admin/arrow/customer-mappings/sync_from_arrow/  
DELETE /api/admin/arrow/customer-mappings/{uuid}/  
GET /api/admin/arrow/customer-mappings/{uuid}/  
PATCH /api/admin/arrow/customer-mappings/{uuid}/  
PUT /api/admin/arrow/customer-mappings/{uuid}/  
GET /api/admin/arrow/customer-mappings/{uuid}/billing_summary/  
GET /api/admin/arrow/customer-mappings/{uuid}/discover_licenses/  
GET /api/admin/arrow/customer-mappings/{uuid}/fetch_arrow_data/  
POST /api/admin/arrow/customer-mappings/{uuid}/import_license/  
POST /api/admin/arrow/customer-mappings/{uuid}/link_resource/  
GET /api/admin/arrow/settings/  
HEAD /api/admin/arrow/settings/  
POST /api/admin/arrow/settings/  
POST /api/admin/arrow/settings/discover_customers/  
POST /api/admin/arrow/settings/preview_settings/  
POST /api/admin/arrow/settings/save_settings/  
POST /api/admin/arrow/settings/validate_credentials/  
DELETE /api/admin/arrow/settings/{uuid}/  
GET /api/admin/arrow/settings/{uuid}/  
PATCH /api/admin/arrow/settings/{uuid}/  
PUT /api/admin/arrow/settings/{uuid}/  
GET /api/admin/arrow/vendor-offering-mappings/  
HEAD /api/admin/arrow/vendor-offering-mappings/  
POST /api/admin/arrow/vendor-offering-mappings/  
GET /api/admin/arrow/vendor-offering-mappings/vendor_choices/  
HEAD /api/admin/arrow/vendor-offering-mappings/vendor_choices/  
DELETE /api/admin/arrow/vendor-offering-mappings/{uuid}/  
GET /api/admin/arrow/vendor-offering-mappings/{uuid}/  
PATCH /api/admin/arrow/vendor-offering-mappings/{uuid}/  
PUT /api/admin/arrow/vendor-offering-mappings/{uuid}/  
POST /api/aws-instances/{uuid}/set_erred/  
POST /api/aws-instances/{uuid}/set_ok/  
POST /api/aws-volumes/{uuid}/set_erred/  
POST /api/aws-volumes/{uuid}/set_ok/  
POST /api/azure-public-ips/{uuid}/set_erred/  
POST /api/azure-public-ips/{uuid}/set_ok/  
POST /api/azure-sql-databases/{uuid}/set_erred/  
POST /api/azure-sql-databases/{uuid}/set_ok/  
POST /api/azure-sql-servers/{uuid}/set_erred/  
POST /api/azure-sql-servers/{uuid}/set_ok/  
POST /api/azure-virtualmachines/{uuid}/set_erred/  
POST /api/azure-virtualmachines/{uuid}/set_ok/  
POST /api/chat-quota/set_quota/  
GET /api/chat-quota/usage/  
GET /api/customers/{uuid}/history/  
GET /api/customers/{uuid}/history/at/  
GET /api/customers/{uuid}/project-digest-config/  
POST /api/customers/{uuid}/project-digest-config/preview/  
POST /api/customers/{uuid}/project-digest-config/send-test/  
PATCH /api/customers/{uuid}/update-project-digest-config/  
PUT /api/customers/{uuid}/update-project-digest-config/  
GET /api/data-access-logs/  
HEAD /api/data-access-logs/  
DELETE /api/data-access-logs/{uuid}/  
GET /api/data-access-logs/{uuid}/  
POST /api/digitalocean-droplets/{uuid}/set_erred/  
POST /api/digitalocean-droplets/{uuid}/set_ok/  
GET /api/event-subscription-queues/  
HEAD /api/event-subscription-queues/  
DELETE /api/event-subscription-queues/{uuid}/  
GET /api/event-subscription-queues/{uuid}/  
POST /api/event-subscriptions/{uuid}/create_queue/  
POST /api/identity-providers/discover_metadata/  
POST /api/identity-providers/generate-mapping/  
GET /api/invoices/{uuid}/history/  
GET /api/invoices/{uuid}/history/at/  
GET /api/keys/{uuid}/history/  
GET /api/keys/{uuid}/history/at/  
GET /api/maintenance-announcements/maintenance_stats/  
HEAD /api/maintenance-announcements/maintenance_stats/  
PATCH /api/marketplace-orders/{uuid}/  
PUT /api/marketplace-orders/{uuid}/  
GET /api/marketplace-plans/{uuid}/history/  
GET /api/marketplace-plans/{uuid}/history/at/  
DELETE /api/marketplace-provider-offerings/{uuid}/delete-user-attribute-config/  
POST /api/marketplace-provider-offerings/{uuid}/delete_tags/  
GET /api/marketplace-provider-offerings/{uuid}/history/  
GET /api/marketplace-provider-offerings/{uuid}/history/at/  
PATCH /api/marketplace-provider-offerings/{uuid}/update-user-attribute-config/  
POST /api/marketplace-provider-offerings/{uuid}/update-user-attribute-config/  
PUT /api/marketplace-provider-offerings/{uuid}/update-user-attribute-config/  
POST /api/marketplace-provider-offerings/{uuid}/update_tags/  
GET /api/marketplace-provider-offerings/{uuid}/user-attribute-config/  
GET /api/marketplace-provider-resources/{uuid}/history/  
GET /api/marketplace-provider-resources/{uuid}/history/at/  
GET /api/marketplace-resources/{uuid}/history/  
GET /api/marketplace-resources/{uuid}/history/at/  
POST /api/marketplace-service-providers/{uuid}/generate_site_agent_config/  
POST /api/marketplace-slurm-periodic-usage-policies/preview_impact/  
GET /api/marketplace-slurm-periodic-usage-policies/{uuid}/command-history/  
POST /api/marketplace-slurm-periodic-usage-policies/{uuid}/dry-run/  
POST /api/marketplace-slurm-periodic-usage-policies/{uuid}/evaluate/  
GET /api/marketplace-slurm-periodic-usage-policies/{uuid}/evaluation-logs/  
POST /api/marketplace-slurm-periodic-usage-policies/{uuid}/report-command-result/  
GET /api/marketplace-stats/aggregated_usage_trends/  
HEAD /api/marketplace-stats/aggregated_usage_trends/  
GET /api/marketplace-stats/customer_member_summary/  
HEAD /api/marketplace-stats/customer_member_summary/  
GET /api/marketplace-stats/offering_costs_summary/  
HEAD /api/marketplace-stats/offering_costs_summary/  
GET /api/marketplace-stats/order_stats/  
HEAD /api/marketplace-stats/order_stats/  
GET /api/marketplace-stats/project_classification_summary/  
HEAD /api/marketplace-stats/project_classification_summary/  
GET /api/marketplace-stats/provider_customers/  
HEAD /api/marketplace-stats/provider_customers/  
GET /api/marketplace-stats/provider_offerings/  
HEAD /api/marketplace-stats/provider_offerings/  
GET /api/marketplace-stats/provider_resources/  
HEAD /api/marketplace-stats/provider_resources/  
GET /api/marketplace-stats/resource_usage_by_creator_affiliation/  
HEAD /api/marketplace-stats/resource_usage_by_creator_affiliation/  
GET /api/marketplace-stats/resource_usage_by_customer/  
HEAD /api/marketplace-stats/resource_usage_by_customer/  
GET /api/marketplace-stats/resource_usage_by_organization_type/  
HEAD /api/marketplace-stats/resource_usage_by_organization_type/  
GET /api/marketplace-stats/resources_geography_summary/  
HEAD /api/marketplace-stats/resources_geography_summary/  
GET /api/marketplace-stats/resources_missing_usage/  
HEAD /api/marketplace-stats/resources_missing_usage/  
GET /api/marketplace-stats/user_job_title_count/  
HEAD /api/marketplace-stats/user_job_title_count/  
GET /api/marketplace-stats/user_organization_type_count/  
HEAD /api/marketplace-stats/user_organization_type_count/  
GET /api/marketplace-tags/  
HEAD /api/marketplace-tags/  
POST /api/marketplace-tags/  
DELETE /api/marketplace-tags/{uuid}/  
GET /api/marketplace-tags/{uuid}/  
PATCH /api/marketplace-tags/{uuid}/  
PUT /api/marketplace-tags/{uuid}/  
POST /api/openportal-allocations/{uuid}/set_erred/  
POST /api/openportal-allocations/{uuid}/set_ok/  
POST /api/openportal-remote-allocations/{uuid}/set_erred/  
POST /api/openportal-remote-allocations/{uuid}/set_ok/  
POST /api/openstack-backups/{uuid}/set_erred/  
POST /api/openstack-backups/{uuid}/set_ok/  
POST /api/openstack-floating-ips/{uuid}/set_erred/  
POST /api/openstack-floating-ips/{uuid}/set_ok/  
POST /api/openstack-instances/{uuid}/set_erred/  
POST /api/openstack-instances/{uuid}/set_ok/  
POST /api/openstack-networks/{uuid}/set_erred/  
POST /api/openstack-networks/{uuid}/set_ok/  
POST /api/openstack-ports/{uuid}/set_erred/  
POST /api/openstack-ports/{uuid}/set_ok/  
POST /api/openstack-routers/{uuid}/set_erred/  
POST /api/openstack-routers/{uuid}/set_ok/  
POST /api/openstack-security-groups/{uuid}/set_erred/  
POST /api/openstack-security-groups/{uuid}/set_ok/  
POST /api/openstack-server-groups/{uuid}/set_erred/  
POST /api/openstack-server-groups/{uuid}/set_ok/  
POST /api/openstack-snapshots/{uuid}/set_erred/  
POST /api/openstack-snapshots/{uuid}/set_ok/  
POST /api/openstack-subnets/{uuid}/set_erred/  
POST /api/openstack-subnets/{uuid}/set_ok/  
POST /api/openstack-tenants/{uuid}/set_erred/  
POST /api/openstack-tenants/{uuid}/set_ok/  
POST /api/openstack-volumes/{uuid}/set_erred/  
POST /api/openstack-volumes/{uuid}/set_ok/  
GET /api/proposal-protected-calls/{uuid}/applicant_attribute_config/  
DELETE /api/proposal-protected-calls/{uuid}/delete_applicant_attribute_config/  
PATCH /api/proposal-protected-calls/{uuid}/update_applicant_attribute_config/  
POST /api/proposal-protected-calls/{uuid}/update_applicant_attribute_config/  
GET /api/proposal-public-calls/{uuid}/check_eligibility/  
POST /api/rancher-apps/{uuid}/set_erred/  
POST /api/rancher-apps/{uuid}/set_ok/  
POST /api/rancher-clusters/{uuid}/set_erred/  
POST /api/rancher-clusters/{uuid}/set_ok/  
POST /api/rancher-hpas/{uuid}/set_erred/  
POST /api/rancher-hpas/{uuid}/set_ok/  
POST /api/rancher-ingresses/{uuid}/set_erred/  
POST /api/rancher-ingresses/{uuid}/set_ok/  
POST /api/rancher-nodes/{uuid}/set_erred/  
POST /api/rancher-nodes/{uuid}/set_ok/  
POST /api/rancher-services/{uuid}/set_erred/  
POST /api/rancher-services/{uuid}/set_ok/  
POST /api/slurm-allocations/{uuid}/set_erred/  
POST /api/slurm-allocations/{uuid}/set_ok/  
POST /api/slurm-jobs/{uuid}/set_erred/  
POST /api/slurm-jobs/{uuid}/set_ok/  
GET /api/stats/celery/  
GET /api/stats/database/  
POST /api/stats/query/  
GET /api/stats/table-growth/  
GET /api/users/profile_completeness/  
HEAD /api/users/profile_completeness/  
POST /api/users/scim_sync_all/  
GET /api/users/user_active_status_count/  
HEAD /api/users/user_active_status_count/  
GET /api/users/user_language_count/  
HEAD /api/users/user_language_count/  
GET /api/users/user_registration_trend/  
HEAD /api/users/user_registration_trend/  
GET /api/users/{uuid}/data_access/  
GET /api/users/{uuid}/data_access_history/  
GET /api/users/{uuid}/history/  
GET /api/users/{uuid}/history/at/  
POST /api/vmware-disks/{uuid}/set_erred/  
POST /api/vmware-disks/{uuid}/set_ok/  
POST /api/vmware-ports/{uuid}/set_erred/  
POST /api/vmware-ports/{uuid}/set_ok/  
POST /api/vmware-virtual-machine/{uuid}/set_erred/  
POST /api/vmware-virtual-machine/{uuid}/set_ok/  

### Deleted Endpoints: 1

------------------------
POST /api/chat/invoke/  

### Modified Endpoints: 201

---------------------------
POST /api/aws-instances/{uuid}/pull/

- Responses changed
  - Modified response: 202
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
  - Modified response: 409
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/aws-volumes/{uuid}/pull/

- Responses changed
  - Modified response: 202
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
  - Modified response: 409
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/azure-public-ips/{uuid}/pull/

- Responses changed
  - Modified response: 202
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
  - Modified response: 409
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/azure-sql-databases/{uuid}/pull/

- Responses changed
  - Modified response: 202
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
  - Modified response: 409
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/azure-sql-servers/{uuid}/pull/

- Responses changed
  - Modified response: 202
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
  - Modified response: 409
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/azure-virtualmachines/{uuid}/pull/

- Responses changed
  - Modified response: 202
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
  - Modified response: 409
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
            - New property: offering_backend_id

GET /api/booking-offerings/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [is_accessible tags]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: is_accessible
              - New property: tags
              - Modified property: options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - New property: storage_folder_config
                            - New property: validators
                            - Modified property: type
                              - New enum values: [storage_folder_manager]
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: slurm_periodic_policy_enabled
              - Modified property: resource_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - New property: storage_folder_config
                            - New property: validators
                            - Modified property: type
                              - New enum values: [storage_folder_manager]

GET /api/booking-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [is_accessible tags]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: is_accessible
            - New property: tags
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: storage_folder_config
                          - New property: validators
                          - Modified property: type
                            - New enum values: [storage_folder_manager]
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: slurm_periodic_policy_enabled
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: storage_folder_config
                          - New property: validators
                          - Modified property: type
                            - New enum values: [storage_folder_manager]

GET /api/booking-resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_backend_id]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: offering_backend_id

GET /api/booking-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_backend_id]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_backend_id

POST /api/digitalocean-droplets/{uuid}/pull/

- Responses changed
  - Modified response: 202
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
  - Modified response: 409
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
                  - New enum values: [slurm_policy_evaluation user_data_accessed]

POST /api/hooks-email/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [slurm_policy_evaluation user_data_accessed]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [slurm_policy_evaluation user_data_accessed]

GET /api/hooks-email/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [slurm_policy_evaluation user_data_accessed]

PATCH /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [slurm_policy_evaluation user_data_accessed]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [slurm_policy_evaluation user_data_accessed]

PUT /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [slurm_policy_evaluation user_data_accessed]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [slurm_policy_evaluation user_data_accessed]

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
                  - New enum values: [slurm_policy_evaluation user_data_accessed]

POST /api/hooks-web/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [slurm_policy_evaluation user_data_accessed]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [slurm_policy_evaluation user_data_accessed]

GET /api/hooks-web/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [slurm_policy_evaluation user_data_accessed]

PATCH /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [slurm_policy_evaluation user_data_accessed]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [slurm_policy_evaluation user_data_accessed]

PUT /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [slurm_policy_evaluation user_data_accessed]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [slurm_policy_evaluation user_data_accessed]

GET /api/invoice-items/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: offering_name
            - Properties changed
              - New property: offering_name

GET /api/invoice-items/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: offering_name
          - Properties changed
            - New property: offering_name

GET /api/invoice-items/{uuid}/consumptions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: offering_name
          - Properties changed
            - New property: offering_name

GET /api/managed-rancher-cluster-resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_backend_id]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: offering_backend_id

GET /api/managed-rancher-cluster-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_backend_id]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_backend_id

GET /api/marketplace-customer-component-usage-policies/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: component_limits_set
                - Items changed
                  - Properties changed
                    - Modified property: period
                      - Property 'AllOf' changed
                        - Schemas added: #/components/schemas/PolicyPeriodEnum
                        - Schemas deleted: #/components/schemas/PeriodEnum

POST /api/marketplace-customer-component-usage-policies/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: component_limits_set
            - Items changed
              - Properties changed
                - Modified property: period
                  - Property 'AllOf' changed
                    - Schemas added: #/components/schemas/PolicyPeriodEnum
                    - Schemas deleted: #/components/schemas/PeriodEnum
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: component_limits_set
              - Items changed
                - Properties changed
                  - Modified property: period
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/PolicyPeriodEnum
                      - Schemas deleted: #/components/schemas/PeriodEnum

GET /api/marketplace-customer-component-usage-policies/actions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: component_limits_set
              - Items changed
                - Properties changed
                  - Modified property: period
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/PolicyPeriodEnum
                      - Schemas deleted: #/components/schemas/PeriodEnum

GET /api/marketplace-customer-component-usage-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: component_limits_set
              - Items changed
                - Properties changed
                  - Modified property: period
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/PolicyPeriodEnum
                      - Schemas deleted: #/components/schemas/PeriodEnum

PATCH /api/marketplace-customer-component-usage-policies/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: component_limits_set
            - Items changed
              - Properties changed
                - Modified property: period
                  - Property 'AllOf' changed
                    - Schemas added: #/components/schemas/PolicyPeriodEnum
                    - Schemas deleted: #/components/schemas/PeriodEnum
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: component_limits_set
              - Items changed
                - Properties changed
                  - Modified property: period
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/PolicyPeriodEnum
                      - Schemas deleted: #/components/schemas/PeriodEnum

PUT /api/marketplace-customer-component-usage-policies/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: component_limits_set
            - Items changed
              - Properties changed
                - Modified property: period
                  - Property 'AllOf' changed
                    - Schemas added: #/components/schemas/PolicyPeriodEnum
                    - Schemas deleted: #/components/schemas/PeriodEnum
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: component_limits_set
              - Items changed
                - Properties changed
                  - Modified property: period
                    - Property 'AllOf' changed
                      - Schemas added: #/components/schemas/PolicyPeriodEnum
                      - Schemas deleted: #/components/schemas/PeriodEnum

GET /api/marketplace-customer-estimated-cost-policies/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: period
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/PolicyPeriodEnum
                  - Schemas deleted: #/components/schemas/PeriodEnum

POST /api/marketplace-customer-estimated-cost-policies/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: period
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/PolicyPeriodEnum
              - Schemas deleted: #/components/schemas/PeriodEnum
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: period
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/PolicyPeriodEnum
                - Schemas deleted: #/components/schemas/PeriodEnum

GET /api/marketplace-customer-estimated-cost-policies/actions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: period
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/PolicyPeriodEnum
                - Schemas deleted: #/components/schemas/PeriodEnum

GET /api/marketplace-customer-estimated-cost-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: period
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/PolicyPeriodEnum
                - Schemas deleted: #/components/schemas/PeriodEnum

PATCH /api/marketplace-customer-estimated-cost-policies/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: period
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/PolicyPeriodEnum
              - Schemas deleted: #/components/schemas/PeriodEnum
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: period
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/PolicyPeriodEnum
                - Schemas deleted: #/components/schemas/PeriodEnum

PUT /api/marketplace-customer-estimated-cost-policies/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: period
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/PolicyPeriodEnum
              - Schemas deleted: #/components/schemas/PeriodEnum
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: period
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/PolicyPeriodEnum
                - Schemas deleted: #/components/schemas/PeriodEnum

GET /api/marketplace-offering-estimated-cost-policies/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: period
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/PolicyPeriodEnum
                  - Schemas deleted: #/components/schemas/PeriodEnum

POST /api/marketplace-offering-estimated-cost-policies/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: period
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/PolicyPeriodEnum
              - Schemas deleted: #/components/schemas/PeriodEnum
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: period
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/PolicyPeriodEnum
                - Schemas deleted: #/components/schemas/PeriodEnum

GET /api/marketplace-offering-estimated-cost-policies/actions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: period
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/PolicyPeriodEnum
                - Schemas deleted: #/components/schemas/PeriodEnum

GET /api/marketplace-offering-estimated-cost-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: period
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/PolicyPeriodEnum
                - Schemas deleted: #/components/schemas/PeriodEnum

PATCH /api/marketplace-offering-estimated-cost-policies/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: period
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/PolicyPeriodEnum
              - Schemas deleted: #/components/schemas/PeriodEnum
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: period
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/PolicyPeriodEnum
                - Schemas deleted: #/components/schemas/PeriodEnum

PUT /api/marketplace-offering-estimated-cost-policies/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: period
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/PolicyPeriodEnum
              - Schemas deleted: #/components/schemas/PeriodEnum
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: period
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/PolicyPeriodEnum
                - Schemas deleted: #/components/schemas/PeriodEnum

GET /api/marketplace-offering-usage-policies/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: period
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/PolicyPeriodEnum
                  - Schemas deleted: #/components/schemas/PeriodEnum

POST /api/marketplace-offering-usage-policies/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: period
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/PolicyPeriodEnum
              - Schemas deleted: #/components/schemas/PeriodEnum
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: period
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/PolicyPeriodEnum
                - Schemas deleted: #/components/schemas/PeriodEnum

GET /api/marketplace-offering-usage-policies/actions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: period
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/PolicyPeriodEnum
                - Schemas deleted: #/components/schemas/PeriodEnum

GET /api/marketplace-offering-usage-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: period
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/PolicyPeriodEnum
                - Schemas deleted: #/components/schemas/PeriodEnum

PATCH /api/marketplace-offering-usage-policies/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: period
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/PolicyPeriodEnum
              - Schemas deleted: #/components/schemas/PeriodEnum
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: period
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/PolicyPeriodEnum
                - Schemas deleted: #/components/schemas/PeriodEnum

PUT /api/marketplace-offering-usage-policies/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: period
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/PolicyPeriodEnum
              - Schemas deleted: #/components/schemas/PeriodEnum
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: period
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/PolicyPeriodEnum
                - Schemas deleted: #/components/schemas/PeriodEnum

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
                      - New property: user_affiliations
                      - New property: user_birth_date
                      - New property: user_civil_number
                      - New property: user_country_of_residence
                      - New property: user_eduperson_assurance
                      - New property: user_gender
                      - New property: user_identity_source
                      - New property: user_job_title
                      - New property: user_nationalities
                      - New property: user_nationality
                      - New property: user_organization
                      - New property: user_organization_country
                      - New property: user_organization_type
                      - New property: user_personal_title
                      - New property: user_phone_number
                      - New property: user_place_of_birth

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
                    - New property: user_affiliations
                    - New property: user_birth_date
                    - New property: user_civil_number
                    - New property: user_country_of_residence
                    - New property: user_eduperson_assurance
                    - New property: user_gender
                    - New property: user_identity_source
                    - New property: user_job_title
                    - New property: user_nationalities
                    - New property: user_nationality
                    - New property: user_organization
                    - New property: user_organization_country
                    - New property: user_organization_type
                    - New property: user_personal_title
                    - New property: user_phone_number
                    - New property: user_place_of_birth

GET /api/marketplace-offering-users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [user_affiliations user_birth_date user_civil_number user_country_of_residence user_eduperson_assurance user_gender user_identity_source user_job_title user_nationalities user_nationality user_organization user_organization_country user_organization_type user_personal_title user_phone_number user_place_of_birth]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: user_affiliations
              - New property: user_birth_date
              - New property: user_civil_number
              - New property: user_country_of_residence
              - New property: user_eduperson_assurance
              - New property: user_gender
              - New property: user_identity_source
              - New property: user_job_title
              - New property: user_nationalities
              - New property: user_nationality
              - New property: user_organization
              - New property: user_organization_country
              - New property: user_organization_type
              - New property: user_personal_title
              - New property: user_phone_number
              - New property: user_place_of_birth

POST /api/marketplace-offering-users/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_affiliations
            - New property: user_birth_date
            - New property: user_civil_number
            - New property: user_country_of_residence
            - New property: user_eduperson_assurance
            - New property: user_gender
            - New property: user_identity_source
            - New property: user_job_title
            - New property: user_nationalities
            - New property: user_nationality
            - New property: user_organization
            - New property: user_organization_country
            - New property: user_organization_type
            - New property: user_personal_title
            - New property: user_phone_number
            - New property: user_place_of_birth

GET /api/marketplace-offering-users/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [user_affiliations user_birth_date user_civil_number user_country_of_residence user_eduperson_assurance user_gender user_identity_source user_job_title user_nationalities user_nationality user_organization user_organization_country user_organization_type user_personal_title user_phone_number user_place_of_birth]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_affiliations
            - New property: user_birth_date
            - New property: user_civil_number
            - New property: user_country_of_residence
            - New property: user_eduperson_assurance
            - New property: user_gender
            - New property: user_identity_source
            - New property: user_job_title
            - New property: user_nationalities
            - New property: user_nationality
            - New property: user_organization
            - New property: user_organization_country
            - New property: user_organization_type
            - New property: user_personal_title
            - New property: user_phone_number
            - New property: user_place_of_birth

PATCH /api/marketplace-offering-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_affiliations
            - New property: user_birth_date
            - New property: user_civil_number
            - New property: user_country_of_residence
            - New property: user_eduperson_assurance
            - New property: user_gender
            - New property: user_identity_source
            - New property: user_job_title
            - New property: user_nationalities
            - New property: user_nationality
            - New property: user_organization
            - New property: user_organization_country
            - New property: user_organization_type
            - New property: user_personal_title
            - New property: user_phone_number
            - New property: user_place_of_birth

PUT /api/marketplace-offering-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_affiliations
            - New property: user_birth_date
            - New property: user_civil_number
            - New property: user_country_of_residence
            - New property: user_eduperson_assurance
            - New property: user_gender
            - New property: user_identity_source
            - New property: user_job_title
            - New property: user_nationalities
            - New property: user_nationality
            - New property: user_organization
            - New property: user_organization_country
            - New property: user_organization_type
            - New property: user_personal_title
            - New property: user_phone_number
            - New property: user_place_of_birth

GET /api/marketplace-orders/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: is_accessible
            - New property: tags
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: storage_folder_config
                          - New property: validators
                          - Modified property: type
                            - New enum values: [storage_folder_manager]
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: slurm_periodic_policy_enabled
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: storage_folder_config
                          - New property: validators
                          - Modified property: type
                            - New enum values: [storage_folder_manager]

GET /api/marketplace-plan-components/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: offering_uuid
              - New required property: plan_uuid
            - Properties changed
              - New property: offering_uuid
              - New property: plan_uuid

GET /api/marketplace-plan-components/{id}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: offering_uuid
            - New required property: plan_uuid
          - Properties changed
            - New property: offering_uuid
            - New property: plan_uuid

GET /api/marketplace-project-estimated-cost-policies/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: period
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/PolicyPeriodEnum
                  - Schemas deleted: #/components/schemas/PeriodEnum

POST /api/marketplace-project-estimated-cost-policies/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: period
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/PolicyPeriodEnum
              - Schemas deleted: #/components/schemas/PeriodEnum
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: period
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/PolicyPeriodEnum
                - Schemas deleted: #/components/schemas/PeriodEnum

GET /api/marketplace-project-estimated-cost-policies/actions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: period
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/PolicyPeriodEnum
                - Schemas deleted: #/components/schemas/PeriodEnum

GET /api/marketplace-project-estimated-cost-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: period
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/PolicyPeriodEnum
                - Schemas deleted: #/components/schemas/PeriodEnum

PATCH /api/marketplace-project-estimated-cost-policies/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: period
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/PolicyPeriodEnum
              - Schemas deleted: #/components/schemas/PeriodEnum
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: period
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/PolicyPeriodEnum
                - Schemas deleted: #/components/schemas/PeriodEnum

PUT /api/marketplace-project-estimated-cost-policies/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: period
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/PolicyPeriodEnum
              - Schemas deleted: #/components/schemas/PeriodEnum
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: period
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/PolicyPeriodEnum
                - Schemas deleted: #/components/schemas/PeriodEnum

GET /api/marketplace-provider-offerings/

- New query param: tag
- New query param: tag_name
- New query param: tag_names_and
- New query param: tags_and
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [tags]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: tags
              - Modified property: options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - New property: storage_folder_config
                            - New property: validators
                            - Modified property: type
                              - New enum values: [storage_folder_manager]
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: slurm_periodic_policy_enabled
              - Modified property: resource_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - New property: storage_folder_config
                            - New property: validators
                            - Modified property: type
                              - New enum values: [storage_folder_manager]

HEAD /api/marketplace-provider-offerings/

- New query param: tag
- New query param: tag_name
- New query param: tag_names_and
- New query param: tags_and

POST /api/marketplace-provider-offerings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: plugin_options
          - Modified property: options
            - Properties changed
              - Modified property: options
                - AdditionalProperties changed
                  - Properties changed
                    - New property: storage_folder_config
                    - New property: validators
                    - Modified property: type
                      - New enum values: [storage_folder_manager]
          - Modified property: resource_options
            - Properties changed
              - Modified property: options
                - AdditionalProperties changed
                  - Properties changed
                    - New property: storage_folder_config
                    - New property: validators
                    - Modified property: type
                      - New enum values: [storage_folder_manager]
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: plugin_options
          - Modified property: options
            - Properties changed
              - Modified property: options
                - AdditionalProperties changed
                  - Properties changed
                    - New property: storage_folder_config
                    - New property: validators
                    - Modified property: type
                      - New enum values: [storage_folder_manager]
          - Modified property: resource_options
            - Properties changed
              - Modified property: options
                - AdditionalProperties changed
                  - Properties changed
                    - New property: storage_folder_config
                    - New property: validators
                    - Modified property: type
                      - New enum values: [storage_folder_manager]
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: plugin_options
          - Modified property: options
            - Properties changed
              - Modified property: options
                - AdditionalProperties changed
                  - Properties changed
                    - New property: storage_folder_config
                    - New property: validators
                    - Modified property: type
                      - New enum values: [storage_folder_manager]
          - Modified property: resource_options
            - Properties changed
              - Modified property: options
                - AdditionalProperties changed
                  - Properties changed
                    - New property: storage_folder_config
                    - New property: validators
                    - Modified property: type
                      - New enum values: [storage_folder_manager]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: tags
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: storage_folder_config
                          - New property: validators
                          - Modified property: type
                            - New enum values: [storage_folder_manager]
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: slurm_periodic_policy_enabled
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: storage_folder_config
                          - New property: validators
                          - Modified property: type
                            - New enum values: [storage_folder_manager]

GET /api/marketplace-provider-offerings/groups/

- New query param: tag
- New query param: tag_name
- New query param: tag_names_and
- New query param: tags_and

HEAD /api/marketplace-provider-offerings/groups/

- New query param: tag
- New query param: tag_name
- New query param: tag_names_and
- New query param: tags_and

GET /api/marketplace-provider-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [tags]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: tags
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: storage_folder_config
                          - New property: validators
                          - Modified property: type
                            - New enum values: [storage_folder_manager]
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: slurm_periodic_policy_enabled
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: storage_folder_config
                          - New property: validators
                          - Modified property: type
                            - New enum values: [storage_folder_manager]

GET /api/marketplace-provider-offerings/{uuid}/component_stats/

- New query param: tag
- New query param: tag_name
- New query param: tag_names_and
- New query param: tags_and

GET /api/marketplace-provider-offerings/{uuid}/costs/

- New query param: tag
- New query param: tag_name
- New query param: tag_names_and
- New query param: tags_and

GET /api/marketplace-provider-offerings/{uuid}/customers/

- New query param: tag
- New query param: tag_name
- New query param: tag_names_and
- New query param: tags_and

POST /api/marketplace-provider-offerings/{uuid}/import_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_backend_id

GET /api/marketplace-provider-offerings/{uuid}/list_course_accounts/

- New query param: tag
- New query param: tag_name
- New query param: tag_names_and
- New query param: tags_and

GET /api/marketplace-provider-offerings/{uuid}/list_customer_service_accounts/

- New query param: tag
- New query param: tag_name
- New query param: tag_names_and
- New query param: tags_and

GET /api/marketplace-provider-offerings/{uuid}/list_customer_users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [country_of_residence eduperson_assurance gender nationalities nationality organization_country organization_type personal_title place_of_birth]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: country_of_residence
              - New property: eduperson_assurance
              - New property: gender
              - New property: nationalities
              - New property: nationality
              - New property: organization_country
              - New property: organization_type
              - New property: personal_title
              - New property: place_of_birth

GET /api/marketplace-provider-offerings/{uuid}/list_project_service_accounts/

- New query param: tag
- New query param: tag_name
- New query param: tag_names_and
- New query param: tags_and

POST /api/marketplace-provider-offerings/{uuid}/move_offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: is_accessible
            - New property: tags
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: storage_folder_config
                          - New property: validators
                          - Modified property: type
                            - New enum values: [storage_folder_manager]
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: slurm_periodic_policy_enabled
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: storage_folder_config
                          - New property: validators
                          - Modified property: type
                            - New enum values: [storage_folder_manager]

POST /api/marketplace-provider-offerings/{uuid}/update_integration/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: slurm_periodic_policy_enabled

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
                    - New property: storage_folder_config
                    - New property: validators
                    - Modified property: type
                      - New enum values: [storage_folder_manager]

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
                    - New property: storage_folder_config
                    - New property: validators
                    - Modified property: type
                      - New enum values: [storage_folder_manager]

GET /api/marketplace-provider-offerings/{uuid}/user_has_resource_access/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [tags]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: tags
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: storage_folder_config
                          - New property: validators
                          - Modified property: type
                            - New enum values: [storage_folder_manager]
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: slurm_periodic_policy_enabled
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: storage_folder_config
                          - New property: validators
                          - Modified property: type
                            - New enum values: [storage_folder_manager]

GET /api/marketplace-provider-resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_backend_id]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: offering_backend_id

GET /api/marketplace-provider-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_backend_id]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_backend_id

POST /api/marketplace-provider-resources/{uuid}/move_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_backend_id

GET /api/marketplace-provider-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: is_accessible
            - New property: tags
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: storage_folder_config
                          - New property: validators
                          - Modified property: type
                            - New enum values: [storage_folder_manager]
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: slurm_periodic_policy_enabled
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: storage_folder_config
                          - New property: validators
                          - Modified property: type
                            - New enum values: [storage_folder_manager]

POST /api/marketplace-provider-resources/{uuid}/restore/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_backend_id

GET /api/marketplace-public-offerings/

- New query param: tag
- New query param: tag_name
- New query param: tag_names_and
- New query param: tags_and
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [is_accessible tags]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: is_accessible
              - New property: tags
              - Modified property: options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - New property: storage_folder_config
                            - New property: validators
                            - Modified property: type
                              - New enum values: [storage_folder_manager]
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: slurm_periodic_policy_enabled
              - Modified property: resource_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - New property: storage_folder_config
                            - New property: validators
                            - Modified property: type
                              - New enum values: [storage_folder_manager]

HEAD /api/marketplace-public-offerings/

- New query param: tag
- New query param: tag_name
- New query param: tag_names_and
- New query param: tags_and

GET /api/marketplace-public-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [is_accessible tags]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: is_accessible
            - New property: tags
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: storage_folder_config
                          - New property: validators
                          - Modified property: type
                            - New enum values: [storage_folder_manager]
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: slurm_periodic_policy_enabled
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: storage_folder_config
                          - New property: validators
                          - Modified property: type
                            - New enum values: [storage_folder_manager]

GET /api/marketplace-resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_backend_id]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: offering_backend_id

GET /api/marketplace-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_backend_id]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_backend_id

POST /api/marketplace-resources/{uuid}/move_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_backend_id

GET /api/marketplace-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: is_accessible
            - New property: tags
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: storage_folder_config
                          - New property: validators
                          - Modified property: type
                            - New enum values: [storage_folder_manager]
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: slurm_periodic_policy_enabled
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: storage_folder_config
                          - New property: validators
                          - Modified property: type
                            - New enum values: [storage_folder_manager]

POST /api/marketplace-resources/{uuid}/renew/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: extension_months
            - Min changed from 1 to 12
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: extension_months
            - Min changed from 1 to 12
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: extension_months
            - Min changed from 1 to 12

POST /api/marketplace-resources/{uuid}/restore/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: offering_backend_id

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
                      - New property: slurm_periodic_policy_enabled

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
                    - New property: slurm_periodic_policy_enabled

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
                    - New property: slurm_periodic_policy_enabled

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
                    - New property: slurm_periodic_policy_enabled

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
                    - New property: slurm_periodic_policy_enabled

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
                    - New property: slurm_periodic_policy_enabled

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
                    - New property: slurm_periodic_policy_enabled

POST /api/marketplace-script-dry-run/{uuid}/async_run/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: is_accessible
            - New property: tags
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: storage_folder_config
                          - New property: validators
                          - Modified property: type
                            - New enum values: [storage_folder_manager]
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: slurm_periodic_policy_enabled
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: storage_folder_config
                          - New property: validators
                          - Modified property: type
                            - New enum values: [storage_folder_manager]

POST /api/marketplace-script-dry-run/{uuid}/run/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: is_accessible
            - New property: tags
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: storage_folder_config
                          - New property: validators
                          - Modified property: type
                            - New enum values: [storage_folder_manager]
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: slurm_periodic_policy_enabled
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: storage_folder_config
                          - New property: validators
                          - Modified property: type
                            - New enum values: [storage_folder_manager]

GET /api/marketplace-service-providers/{service_provider_uuid}/offerings/

- New query param: tag
- New query param: tag_name
- New query param: tag_names_and
- New query param: tags_and

GET /api/marketplace-slurm-periodic-usage-policies/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: carryover_factor
              - Deleted property: fairshare_decay_half_life
              - Modified property: period
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/PolicyPeriodEnum
                  - Schemas deleted: #/components/schemas/PeriodEnum

POST /api/marketplace-slurm-periodic-usage-policies/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: carryover_factor
          - Deleted property: fairshare_decay_half_life
          - Modified property: period
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/PolicyPeriodEnum
              - Schemas deleted: #/components/schemas/PeriodEnum
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: carryover_factor
            - Deleted property: fairshare_decay_half_life
            - Modified property: period
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/PolicyPeriodEnum
                - Schemas deleted: #/components/schemas/PeriodEnum

GET /api/marketplace-slurm-periodic-usage-policies/actions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: carryover_factor
            - Deleted property: fairshare_decay_half_life
            - Modified property: period
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/PolicyPeriodEnum
                - Schemas deleted: #/components/schemas/PeriodEnum

GET /api/marketplace-slurm-periodic-usage-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: carryover_factor
            - Deleted property: fairshare_decay_half_life
            - Modified property: period
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/PolicyPeriodEnum
                - Schemas deleted: #/components/schemas/PeriodEnum

PATCH /api/marketplace-slurm-periodic-usage-policies/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: carryover_factor
          - Deleted property: fairshare_decay_half_life
          - Modified property: period
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/PolicyPeriodEnum
              - Schemas deleted: #/components/schemas/PeriodEnum
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: carryover_factor
            - Deleted property: fairshare_decay_half_life
            - Modified property: period
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/PolicyPeriodEnum
                - Schemas deleted: #/components/schemas/PeriodEnum

PUT /api/marketplace-slurm-periodic-usage-policies/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: carryover_factor
          - Deleted property: fairshare_decay_half_life
          - Modified property: period
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/PolicyPeriodEnum
              - Schemas deleted: #/components/schemas/PeriodEnum
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: carryover_factor
            - Deleted property: fairshare_decay_half_life
            - Modified property: period
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/PolicyPeriodEnum
                - Schemas deleted: #/components/schemas/PeriodEnum

GET /api/marketplace-software-packages/

- New query param: extension_name
- New query param: extension_type
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: versions
                - Items changed
                  - Required changed
                    - New required property: extensions
                    - New required property: module
                    - New required property: required_modules
                    - New required property: toolchain
                    - New required property: toolchain_families_compatibility
                  - Properties changed
                    - New property: extensions
                    - New property: module
                    - New property: required_modules
                    - New property: toolchain
                    - New property: toolchain_families_compatibility

HEAD /api/marketplace-software-packages/

- New query param: extension_name
- New query param: extension_type

POST /api/marketplace-software-packages/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: versions
              - Items changed
                - Required changed
                  - New required property: extensions
                  - New required property: module
                  - New required property: required_modules
                  - New required property: toolchain
                  - New required property: toolchain_families_compatibility
                - Properties changed
                  - New property: extensions
                  - New property: module
                  - New property: required_modules
                  - New property: toolchain
                  - New property: toolchain_families_compatibility

GET /api/marketplace-software-packages/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: versions
              - Items changed
                - Required changed
                  - New required property: extensions
                  - New required property: module
                  - New required property: required_modules
                  - New required property: toolchain
                  - New required property: toolchain_families_compatibility
                - Properties changed
                  - New property: extensions
                  - New property: module
                  - New property: required_modules
                  - New property: toolchain
                  - New property: toolchain_families_compatibility

PATCH /api/marketplace-software-packages/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: versions
              - Items changed
                - Required changed
                  - New required property: extensions
                  - New required property: module
                  - New required property: required_modules
                  - New required property: toolchain
                  - New required property: toolchain_families_compatibility
                - Properties changed
                  - New property: extensions
                  - New property: module
                  - New property: required_modules
                  - New property: toolchain
                  - New property: toolchain_families_compatibility

PUT /api/marketplace-software-packages/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: versions
              - Items changed
                - Required changed
                  - New required property: extensions
                  - New required property: module
                  - New required property: required_modules
                  - New required property: toolchain
                  - New required property: toolchain_families_compatibility
                - Properties changed
                  - New property: extensions
                  - New property: module
                  - New property: required_modules
                  - New property: toolchain
                  - New property: toolchain_families_compatibility

GET /api/marketplace-software-versions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: extensions
              - New required property: module
              - New required property: required_modules
              - New required property: toolchain
              - New required property: toolchain_families_compatibility
            - Properties changed
              - New property: extensions
              - New property: module
              - New property: required_modules
              - New property: toolchain
              - New property: toolchain_families_compatibility

POST /api/marketplace-software-versions/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: extensions
            - New required property: module
            - New required property: required_modules
            - New required property: toolchain
            - New required property: toolchain_families_compatibility
          - Properties changed
            - New property: extensions
            - New property: module
            - New property: required_modules
            - New property: toolchain
            - New property: toolchain_families_compatibility

GET /api/marketplace-software-versions/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: extensions
            - New required property: module
            - New required property: required_modules
            - New required property: toolchain
            - New required property: toolchain_families_compatibility
          - Properties changed
            - New property: extensions
            - New property: module
            - New property: required_modules
            - New property: toolchain
            - New property: toolchain_families_compatibility

PATCH /api/marketplace-software-versions/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: extensions
            - New required property: module
            - New required property: required_modules
            - New required property: toolchain
            - New required property: toolchain_families_compatibility
          - Properties changed
            - New property: extensions
            - New property: module
            - New property: required_modules
            - New property: toolchain
            - New property: toolchain_families_compatibility

PUT /api/marketplace-software-versions/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: extensions
            - New required property: module
            - New required property: required_modules
            - New required property: toolchain
            - New required property: toolchain_families_compatibility
          - Properties changed
            - New property: extensions
            - New property: module
            - New property: required_modules
            - New property: toolchain
            - New property: toolchain_families_compatibility

GET /api/marketplace-user-offering-consents/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: collected_attributes
            - Properties changed
              - New property: collected_attributes

GET /api/marketplace-user-offering-consents/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: collected_attributes
          - Properties changed
            - New property: collected_attributes

PATCH /api/marketplace-user-offering-consents/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: collected_attributes
          - Properties changed
            - New property: collected_attributes

PUT /api/marketplace-user-offering-consents/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: collected_attributes
          - Properties changed
            - New property: collected_attributes

POST /api/marketplace-user-offering-consents/{uuid}/revoke/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: collected_attributes
          - Properties changed
            - New property: collected_attributes

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
                  - New enum values: [slurm_policy_evaluation user_data_accessed]

POST /api/openportal-allocations/{uuid}/pull/

- Responses changed
  - Modified response: 202
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
  - Modified response: 409
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

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
                            - New property: tags
                            - Modified property: options
                              - Property 'AllOf' changed
                                - Modified schema: #/components/schemas/OfferingOptions
                                  - Properties changed
                                    - Modified property: options
                                      - AdditionalProperties changed
                                        - Properties changed
                                          - New property: storage_folder_config
                                          - New property: validators
                                          - Modified property: type
                                            - New enum values: [storage_folder_manager]
                            - Modified property: plugin_options
                              - Property 'AllOf' changed
                                - Modified schema: #/components/schemas/MergedPluginOptions
                                  - Properties changed
                                    - New property: slurm_periodic_policy_enabled
                            - Modified property: resource_options
                              - Property 'AllOf' changed
                                - Modified schema: #/components/schemas/OfferingOptions
                                  - Properties changed
                                    - Modified property: options
                                      - AdditionalProperties changed
                                        - Properties changed
                                          - New property: storage_folder_config
                                          - New property: validators
                                          - Modified property: type
                                            - New enum values: [storage_folder_manager]

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
                          - New property: tags
                          - Modified property: options
                            - Property 'AllOf' changed
                              - Modified schema: #/components/schemas/OfferingOptions
                                - Properties changed
                                  - Modified property: options
                                    - AdditionalProperties changed
                                      - Properties changed
                                        - New property: storage_folder_config
                                        - New property: validators
                                        - Modified property: type
                                          - New enum values: [storage_folder_manager]
                          - Modified property: plugin_options
                            - Property 'AllOf' changed
                              - Modified schema: #/components/schemas/MergedPluginOptions
                                - Properties changed
                                  - New property: slurm_periodic_policy_enabled
                          - Modified property: resource_options
                            - Property 'AllOf' changed
                              - Modified schema: #/components/schemas/OfferingOptions
                                - Properties changed
                                  - Modified property: options
                                    - AdditionalProperties changed
                                      - Properties changed
                                        - New property: storage_folder_config
                                        - New property: validators
                                        - Modified property: type
                                          - New enum values: [storage_folder_manager]

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
                    - New property: tags
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: storage_folder_config
                                  - New property: validators
                                  - Modified property: type
                                    - New enum values: [storage_folder_manager]
                    - Modified property: plugin_options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/MergedPluginOptions
                          - Properties changed
                            - New property: slurm_periodic_policy_enabled
                    - Modified property: resource_options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: storage_folder_config
                                  - New property: validators
                                  - Modified property: type
                                    - New enum values: [storage_folder_manager]

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
                  - New property: tags
                  - Modified property: options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - New property: storage_folder_config
                                - New property: validators
                                - Modified property: type
                                  - New enum values: [storage_folder_manager]
                  - Modified property: plugin_options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/MergedPluginOptions
                        - Properties changed
                          - New property: slurm_periodic_policy_enabled
                  - Modified property: resource_options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - New property: storage_folder_config
                                - New property: validators
                                - Modified property: type
                                  - New enum values: [storage_folder_manager]

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
                  - New property: tags
                  - Modified property: options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - New property: storage_folder_config
                                - New property: validators
                                - Modified property: type
                                  - New enum values: [storage_folder_manager]
                  - Modified property: plugin_options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/MergedPluginOptions
                        - Properties changed
                          - New property: slurm_periodic_policy_enabled
                  - Modified property: resource_options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - New property: storage_folder_config
                                - New property: validators
                                - Modified property: type
                                  - New enum values: [storage_folder_manager]

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
                  - New property: tags
                  - Modified property: options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - New property: storage_folder_config
                                - New property: validators
                                - Modified property: type
                                  - New enum values: [storage_folder_manager]
                  - Modified property: plugin_options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/MergedPluginOptions
                        - Properties changed
                          - New property: slurm_periodic_policy_enabled
                  - Modified property: resource_options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - New property: storage_folder_config
                                - New property: validators
                                - Modified property: type
                                  - New enum values: [storage_folder_manager]

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
                  - New property: tags
                  - Modified property: options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - New property: storage_folder_config
                                - New property: validators
                                - Modified property: type
                                  - New enum values: [storage_folder_manager]
                  - Modified property: plugin_options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/MergedPluginOptions
                        - Properties changed
                          - New property: slurm_periodic_policy_enabled
                  - Modified property: resource_options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - New property: storage_folder_config
                                - New property: validators
                                - Modified property: type
                                  - New enum values: [storage_folder_manager]

POST /api/openportal-remote-allocations/{uuid}/pull/

- Responses changed
  - Modified response: 202
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
  - Modified response: 409
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/openstack-backups/{uuid}/pull/

- Responses changed
  - Modified response: 202
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
  - Modified response: 409
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/openstack-floating-ips/{uuid}/pull/

- Responses changed
  - Modified response: 202
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
  - Modified response: 409
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

GET /api/openstack-images/

- New query param: show_duplicate_names
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: backend_created_at

HEAD /api/openstack-images/

- New query param: show_duplicate_names

GET /api/openstack-images/usage_stats/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: backend_created_at

GET /api/openstack-images/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: backend_created_at

POST /api/openstack-instances/{uuid}/pull/

- Responses changed
  - Modified response: 202
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
  - Modified response: 409
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/openstack-networks/{uuid}/pull/

- Responses changed
  - Modified response: 202
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
  - Modified response: 409
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/openstack-ports/{uuid}/pull/

- Responses changed
  - Modified response: 202
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
  - Modified response: 409
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/openstack-security-groups/{uuid}/pull/

- Responses changed
  - Modified response: 202
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
  - Modified response: 409
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/openstack-server-groups/{uuid}/pull/

- Responses changed
  - Modified response: 202
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
  - Modified response: 409
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/openstack-snapshots/{uuid}/pull/

- Responses changed
  - Modified response: 202
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
  - Modified response: 409
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/openstack-subnets/{uuid}/pull/

- Responses changed
  - Modified response: 202
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
  - Modified response: 409
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/openstack-tenants/{uuid}/pull/

- Responses changed
  - Modified response: 202
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
  - Modified response: 409
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/openstack-tenants/{uuid}/set_quotas/

- Description changed from 'A quota can be set for a particular tenant. Only staff users can do that.
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

POST /api/openstack-volumes/{uuid}/pull/

- Responses changed
  - Modified response: 202
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
  - Modified response: 409
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

GET /api/override-settings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: ARROW_AUTO_RECONCILIATION
            - New property: ARROW_BILLING_CHECK_INTERVAL_HOURS
            - New property: ARROW_CONSUMPTION_SYNC_ENABLED
            - New property: ARROW_CONSUMPTION_SYNC_INTERVAL_HOURS
            - New property: ARROW_SYNC_INTERVAL_HOURS
            - New property: DEFAULT_OFFERING_USER_ATTRIBUTES
            - New property: ENABLED_USER_PROFILE_ATTRIBUTES
            - New property: ENFORCE_MANDATORY_USER_ATTRIBUTES
            - New property: INVITATION_ALLOWED_FIELDS
            - New property: LLM_TOKEN_LIMIT_DAILY
            - New property: LLM_TOKEN_LIMIT_MONTHLY
            - New property: LLM_TOKEN_LIMIT_WEEKLY
            - New property: MANDATORY_USER_ATTRIBUTES
            - New property: RESTRICTED_OFFERING_VISIBILITY_MODE
            - New property: SCIM_API_KEY
            - New property: SCIM_API_URL
            - New property: SCIM_MEMBERSHIP_SYNC_ENABLED
            - New property: SCIM_URN_NAMESPACE
            - New property: SLURM_POLICY_EVALUATION_LOG_RETENTION_DAYS
            - New property: TABLE_GROWTH_MIN_SIZE_BYTES
            - New property: TABLE_GROWTH_MONITORING_ENABLED
            - New property: TABLE_GROWTH_MONTHLY_THRESHOLD_PERCENT
            - New property: TABLE_GROWTH_RETENTION_DAYS
            - New property: TABLE_GROWTH_WEEKLY_THRESHOLD_PERCENT
            - New property: USER_DATA_ACCESS_LOGGING_ENABLED
            - New property: USER_DATA_ACCESS_LOG_RETENTION_DAYS
            - New property: USER_DATA_ACCESS_LOG_SELF_ACCESS

POST /api/override-settings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: ARROW_AUTO_RECONCILIATION
          - New property: ARROW_BILLING_CHECK_INTERVAL_HOURS
          - New property: ARROW_CONSUMPTION_SYNC_ENABLED
          - New property: ARROW_CONSUMPTION_SYNC_INTERVAL_HOURS
          - New property: ARROW_SYNC_INTERVAL_HOURS
          - New property: DEFAULT_OFFERING_USER_ATTRIBUTES
          - New property: ENABLED_USER_PROFILE_ATTRIBUTES
          - New property: ENFORCE_MANDATORY_USER_ATTRIBUTES
          - New property: INVITATION_ALLOWED_FIELDS
          - New property: LLM_TOKEN_LIMIT_DAILY
          - New property: LLM_TOKEN_LIMIT_MONTHLY
          - New property: LLM_TOKEN_LIMIT_WEEKLY
          - New property: MANDATORY_USER_ATTRIBUTES
          - New property: RESTRICTED_OFFERING_VISIBILITY_MODE
          - New property: SCIM_API_KEY
          - New property: SCIM_API_URL
          - New property: SCIM_MEMBERSHIP_SYNC_ENABLED
          - New property: SCIM_URN_NAMESPACE
          - New property: SLURM_POLICY_EVALUATION_LOG_RETENTION_DAYS
          - New property: TABLE_GROWTH_MIN_SIZE_BYTES
          - New property: TABLE_GROWTH_MONITORING_ENABLED
          - New property: TABLE_GROWTH_MONTHLY_THRESHOLD_PERCENT
          - New property: TABLE_GROWTH_RETENTION_DAYS
          - New property: TABLE_GROWTH_WEEKLY_THRESHOLD_PERCENT
          - New property: USER_DATA_ACCESS_LOGGING_ENABLED
          - New property: USER_DATA_ACCESS_LOG_RETENTION_DAYS
          - New property: USER_DATA_ACCESS_LOG_SELF_ACCESS
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: ARROW_AUTO_RECONCILIATION
          - New property: ARROW_BILLING_CHECK_INTERVAL_HOURS
          - New property: ARROW_CONSUMPTION_SYNC_ENABLED
          - New property: ARROW_CONSUMPTION_SYNC_INTERVAL_HOURS
          - New property: ARROW_SYNC_INTERVAL_HOURS
          - New property: DEFAULT_OFFERING_USER_ATTRIBUTES
          - New property: ENABLED_USER_PROFILE_ATTRIBUTES
          - New property: ENFORCE_MANDATORY_USER_ATTRIBUTES
          - New property: INVITATION_ALLOWED_FIELDS
          - New property: LLM_TOKEN_LIMIT_DAILY
          - New property: LLM_TOKEN_LIMIT_MONTHLY
          - New property: LLM_TOKEN_LIMIT_WEEKLY
          - New property: MANDATORY_USER_ATTRIBUTES
          - New property: RESTRICTED_OFFERING_VISIBILITY_MODE
          - New property: SCIM_API_KEY
          - New property: SCIM_API_URL
          - New property: SCIM_MEMBERSHIP_SYNC_ENABLED
          - New property: SCIM_URN_NAMESPACE
          - New property: SLURM_POLICY_EVALUATION_LOG_RETENTION_DAYS
          - New property: TABLE_GROWTH_MIN_SIZE_BYTES
          - New property: TABLE_GROWTH_MONITORING_ENABLED
          - New property: TABLE_GROWTH_MONTHLY_THRESHOLD_PERCENT
          - New property: TABLE_GROWTH_RETENTION_DAYS
          - New property: TABLE_GROWTH_WEEKLY_THRESHOLD_PERCENT
          - New property: USER_DATA_ACCESS_LOGGING_ENABLED
          - New property: USER_DATA_ACCESS_LOG_RETENTION_DAYS
          - New property: USER_DATA_ACCESS_LOG_SELF_ACCESS
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: ARROW_AUTO_RECONCILIATION
          - New property: ARROW_BILLING_CHECK_INTERVAL_HOURS
          - New property: ARROW_CONSUMPTION_SYNC_ENABLED
          - New property: ARROW_CONSUMPTION_SYNC_INTERVAL_HOURS
          - New property: ARROW_SYNC_INTERVAL_HOURS
          - New property: DEFAULT_OFFERING_USER_ATTRIBUTES
          - New property: ENABLED_USER_PROFILE_ATTRIBUTES
          - New property: ENFORCE_MANDATORY_USER_ATTRIBUTES
          - New property: INVITATION_ALLOWED_FIELDS
          - New property: LLM_TOKEN_LIMIT_DAILY
          - New property: LLM_TOKEN_LIMIT_MONTHLY
          - New property: LLM_TOKEN_LIMIT_WEEKLY
          - New property: MANDATORY_USER_ATTRIBUTES
          - New property: RESTRICTED_OFFERING_VISIBILITY_MODE
          - New property: SCIM_API_KEY
          - New property: SCIM_API_URL
          - New property: SCIM_MEMBERSHIP_SYNC_ENABLED
          - New property: SCIM_URN_NAMESPACE
          - New property: SLURM_POLICY_EVALUATION_LOG_RETENTION_DAYS
          - New property: TABLE_GROWTH_MIN_SIZE_BYTES
          - New property: TABLE_GROWTH_MONITORING_ENABLED
          - New property: TABLE_GROWTH_MONTHLY_THRESHOLD_PERCENT
          - New property: TABLE_GROWTH_RETENTION_DAYS
          - New property: TABLE_GROWTH_WEEKLY_THRESHOLD_PERCENT
          - New property: USER_DATA_ACCESS_LOGGING_ENABLED
          - New property: USER_DATA_ACCESS_LOG_RETENTION_DAYS
          - New property: USER_DATA_ACCESS_LOG_SELF_ACCESS

GET /api/promotions-campaigns/{uuid}/resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [offering_backend_id]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: offering_backend_id

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
                      - Modified property: options
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/OfferingOptions
                            - Properties changed
                              - Modified property: options
                                - AdditionalProperties changed
                                  - Properties changed
                                    - New property: storage_folder_config
                                    - New property: validators
                                    - Modified property: type
                                      - New enum values: [storage_folder_manager]

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
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: storage_folder_config
                                  - New property: validators
                                  - Modified property: type
                                    - New enum values: [storage_folder_manager]

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
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: storage_folder_config
                                  - New property: validators
                                  - Modified property: type
                                    - New enum values: [storage_folder_manager]

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
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: storage_folder_config
                                  - New property: validators
                                  - Modified property: type
                                    - New enum values: [storage_folder_manager]

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
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: storage_folder_config
                                  - New property: validators
                                  - Modified property: type
                                    - New enum values: [storage_folder_manager]

GET /api/proposal-protected-calls/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [has_eligibility_restrictions user_affiliations user_assurance_levels user_email_patterns user_identity_sources user_nationalities user_organization_types]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: has_eligibility_restrictions
              - New property: user_affiliations
              - New property: user_assurance_levels
              - New property: user_email_patterns
              - New property: user_identity_sources
              - New property: user_nationalities
              - New property: user_organization_types
              - Modified property: offerings
                - Items changed
                  - Properties changed
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: storage_folder_config
                                  - New property: validators
                                  - Modified property: type
                                    - New enum values: [storage_folder_manager]

POST /api/proposal-protected-calls/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: user_affiliations
          - New property: user_assurance_levels
          - New property: user_email_patterns
          - New property: user_identity_sources
          - New property: user_nationalities
          - New property: user_organization_types
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_eligibility_restrictions
            - New property: user_affiliations
            - New property: user_assurance_levels
            - New property: user_email_patterns
            - New property: user_identity_sources
            - New property: user_nationalities
            - New property: user_organization_types
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - New property: storage_folder_config
                                - New property: validators
                                - Modified property: type
                                  - New enum values: [storage_folder_manager]

GET /api/proposal-protected-calls/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [has_eligibility_restrictions user_affiliations user_assurance_levels user_email_patterns user_identity_sources user_nationalities user_organization_types]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_eligibility_restrictions
            - New property: user_affiliations
            - New property: user_assurance_levels
            - New property: user_email_patterns
            - New property: user_identity_sources
            - New property: user_nationalities
            - New property: user_organization_types
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - New property: storage_folder_config
                                - New property: validators
                                - Modified property: type
                                  - New enum values: [storage_folder_manager]

PATCH /api/proposal-protected-calls/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: user_affiliations
          - New property: user_assurance_levels
          - New property: user_email_patterns
          - New property: user_identity_sources
          - New property: user_nationalities
          - New property: user_organization_types
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_eligibility_restrictions
            - New property: user_affiliations
            - New property: user_assurance_levels
            - New property: user_email_patterns
            - New property: user_identity_sources
            - New property: user_nationalities
            - New property: user_organization_types
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - New property: storage_folder_config
                                - New property: validators
                                - Modified property: type
                                  - New enum values: [storage_folder_manager]

PUT /api/proposal-protected-calls/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: user_affiliations
          - New property: user_assurance_levels
          - New property: user_email_patterns
          - New property: user_identity_sources
          - New property: user_nationalities
          - New property: user_organization_types
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_eligibility_restrictions
            - New property: user_affiliations
            - New property: user_assurance_levels
            - New property: user_email_patterns
            - New property: user_identity_sources
            - New property: user_nationalities
            - New property: user_organization_types
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - New property: storage_folder_config
                                - New property: validators
                                - Modified property: type
                                  - New enum values: [storage_folder_manager]

POST /api/proposal-protected-calls/{uuid}/compute-affinities/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: user_affiliations
          - New property: user_assurance_levels
          - New property: user_email_patterns
          - New property: user_identity_sources
          - New property: user_nationalities
          - New property: user_organization_types

GET /api/proposal-protected-calls/{uuid}/offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - New property: storage_folder_config
                            - New property: validators
                            - Modified property: type
                              - New enum values: [storage_folder_manager]

POST /api/proposal-protected-calls/{uuid}/offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: storage_folder_config
                          - New property: validators
                          - Modified property: type
                            - New enum values: [storage_folder_manager]

GET /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: storage_folder_config
                          - New property: validators
                          - Modified property: type
                            - New enum values: [storage_folder_manager]

PATCH /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: storage_folder_config
                          - New property: validators
                          - Modified property: type
                            - New enum values: [storage_folder_manager]

PUT /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: storage_folder_config
                          - New property: validators
                          - Modified property: type
                            - New enum values: [storage_folder_manager]

POST /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/close/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: user_affiliations
          - New property: user_assurance_levels
          - New property: user_email_patterns
          - New property: user_identity_sources
          - New property: user_nationalities
          - New property: user_organization_types
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_eligibility_restrictions
            - New property: user_affiliations
            - New property: user_assurance_levels
            - New property: user_email_patterns
            - New property: user_identity_sources
            - New property: user_nationalities
            - New property: user_organization_types
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - New property: storage_folder_config
                                - New property: validators
                                - Modified property: type
                                  - New enum values: [storage_folder_manager]

GET /api/proposal-public-calls/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [has_eligibility_restrictions]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: has_eligibility_restrictions
              - Modified property: offerings
                - Items changed
                  - Properties changed
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: storage_folder_config
                                  - New property: validators
                                  - Modified property: type
                                    - New enum values: [storage_folder_manager]

GET /api/proposal-public-calls/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [has_eligibility_restrictions]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_eligibility_restrictions
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - New property: storage_folder_config
                                - New property: validators
                                - Modified property: type
                                  - New enum values: [storage_folder_manager]

GET /api/proposal-requested-offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - New property: storage_folder_config
                            - New property: validators
                            - Modified property: type
                              - New enum values: [storage_folder_manager]

GET /api/proposal-requested-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: storage_folder_config
                          - New property: validators
                          - Modified property: type
                            - New enum values: [storage_folder_manager]

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
                      - Modified property: options
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/OfferingOptions
                            - Properties changed
                              - Modified property: options
                                - AdditionalProperties changed
                                  - Properties changed
                                    - New property: storage_folder_config
                                    - New property: validators
                                    - Modified property: type
                                      - New enum values: [storage_folder_manager]

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
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: storage_folder_config
                                  - New property: validators
                                  - Modified property: type
                                    - New enum values: [storage_folder_manager]

POST /api/rancher-apps/{uuid}/pull/

- Responses changed
  - Modified response: 202
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
  - Modified response: 409
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/rancher-clusters/{uuid}/pull/

- Responses changed
  - Modified response: 202
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
  - Modified response: 409
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/rancher-hpas/{uuid}/pull/

- Responses changed
  - Modified response: 202
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
  - Modified response: 409
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/rancher-ingresses/{uuid}/pull/

- Responses changed
  - Modified response: 202
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
  - Modified response: 409
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/rancher-nodes/{uuid}/pull/

- Responses changed
  - Modified response: 202
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
  - Modified response: 409
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/rancher-services/{uuid}/pull/

- Responses changed
  - Modified response: 202
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
  - Modified response: 409
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/slurm-allocations/{uuid}/pull/

- Responses changed
  - Modified response: 202
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
  - Modified response: 409
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/slurm-jobs/{uuid}/pull/

- Responses changed
  - Modified response: 202
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
  - Modified response: 409
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

GET /api/users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [country_of_residence eduperson_assurance gender nationalities nationality organization_country organization_type personal_title place_of_birth]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: country_of_residence
              - New property: eduperson_assurance
              - New property: gender
              - New property: nationalities
              - New property: nationality
              - New property: organization_country
              - New property: organization_type
              - New property: personal_title
              - New property: place_of_birth

POST /api/users/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: country_of_residence
          - New property: eduperson_assurance
          - New property: gender
          - New property: nationalities
          - New property: nationality
          - New property: organization_country
          - New property: organization_type
          - New property: personal_title
          - New property: place_of_birth
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: country_of_residence
          - New property: eduperson_assurance
          - New property: gender
          - New property: nationalities
          - New property: nationality
          - New property: organization_country
          - New property: organization_type
          - New property: personal_title
          - New property: place_of_birth
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: country_of_residence
          - New property: eduperson_assurance
          - New property: gender
          - New property: nationalities
          - New property: nationality
          - New property: organization_country
          - New property: organization_type
          - New property: personal_title
          - New property: place_of_birth
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: country_of_residence
            - New property: eduperson_assurance
            - New property: gender
            - New property: nationalities
            - New property: nationality
            - New property: organization_country
            - New property: organization_type
            - New property: personal_title
            - New property: place_of_birth

GET /api/users/me/

- Description changed from 'Get current user details, including authentication token.' to 'Get current user details, including authentication token and profile completeness status.'
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [country_of_residence eduperson_assurance gender nationalities nationality organization_country organization_type personal_title place_of_birth]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: country_of_residence
            - New property: eduperson_assurance
            - New property: gender
            - New property: nationalities
            - New property: nationality
            - New property: organization_country
            - New property: organization_type
            - New property: personal_title
            - New property: place_of_birth

GET /api/users/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [country_of_residence eduperson_assurance gender nationalities nationality organization_country organization_type personal_title place_of_birth]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: country_of_residence
            - New property: eduperson_assurance
            - New property: gender
            - New property: nationalities
            - New property: nationality
            - New property: organization_country
            - New property: organization_type
            - New property: personal_title
            - New property: place_of_birth

PATCH /api/users/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: country_of_residence
          - New property: eduperson_assurance
          - New property: gender
          - New property: nationalities
          - New property: nationality
          - New property: organization_country
          - New property: organization_type
          - New property: personal_title
          - New property: place_of_birth
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: country_of_residence
          - New property: eduperson_assurance
          - New property: gender
          - New property: nationalities
          - New property: nationality
          - New property: organization_country
          - New property: organization_type
          - New property: personal_title
          - New property: place_of_birth
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: country_of_residence
          - New property: eduperson_assurance
          - New property: gender
          - New property: nationalities
          - New property: nationality
          - New property: organization_country
          - New property: organization_type
          - New property: personal_title
          - New property: place_of_birth
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: country_of_residence
            - New property: eduperson_assurance
            - New property: gender
            - New property: nationalities
            - New property: nationality
            - New property: organization_country
            - New property: organization_type
            - New property: personal_title
            - New property: place_of_birth

PUT /api/users/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: country_of_residence
          - New property: eduperson_assurance
          - New property: gender
          - New property: nationalities
          - New property: nationality
          - New property: organization_country
          - New property: organization_type
          - New property: personal_title
          - New property: place_of_birth
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: country_of_residence
          - New property: eduperson_assurance
          - New property: gender
          - New property: nationalities
          - New property: nationality
          - New property: organization_country
          - New property: organization_type
          - New property: personal_title
          - New property: place_of_birth
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: country_of_residence
          - New property: eduperson_assurance
          - New property: gender
          - New property: nationalities
          - New property: nationality
          - New property: organization_country
          - New property: organization_type
          - New property: personal_title
          - New property: place_of_birth
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: country_of_residence
            - New property: eduperson_assurance
            - New property: gender
            - New property: nationalities
            - New property: nationality
            - New property: organization_country
            - New property: organization_type
            - New property: personal_title
            - New property: place_of_birth

POST /api/vmware-disks/{uuid}/pull/

- Responses changed
  - Modified response: 202
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
  - Modified response: 409
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/vmware-ports/{uuid}/pull/

- Responses changed
  - Modified response: 202
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
  - Modified response: 409
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json

POST /api/vmware-virtual-machine/{uuid}/pull/

- Responses changed
  - Modified response: 202
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
  - Modified response: 409
    - Description changed from 'No response body' to ''
    - Content changed
      - New media type: application/json
