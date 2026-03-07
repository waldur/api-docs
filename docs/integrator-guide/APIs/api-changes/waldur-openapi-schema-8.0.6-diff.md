# OpenAPI schema diff - 8.0.6

## For version 8.0.6

### New Endpoints: 46

---------------------
POST /api/marketplace-slurm-periodic-usage-policies/{uuid}/force-period-reset/  
GET /api/marketplace-stats/openstack_instances/  
HEAD /api/marketplace-stats/openstack_instances/  
GET /api/marketplace-stats/openstack_instances_aggregate/  
HEAD /api/marketplace-stats/openstack_instances_aggregate/  
GET /api/openstack-health-monitors/  
HEAD /api/openstack-health-monitors/  
POST /api/openstack-health-monitors/  
DELETE /api/openstack-health-monitors/{uuid}/  
GET /api/openstack-health-monitors/{uuid}/  
PATCH /api/openstack-health-monitors/{uuid}/  
PUT /api/openstack-health-monitors/{uuid}/  
GET /api/openstack-listeners/  
HEAD /api/openstack-listeners/  
POST /api/openstack-listeners/  
DELETE /api/openstack-listeners/{uuid}/  
GET /api/openstack-listeners/{uuid}/  
PATCH /api/openstack-listeners/{uuid}/  
PUT /api/openstack-listeners/{uuid}/  
GET /api/openstack-loadbalancers/  
HEAD /api/openstack-loadbalancers/  
POST /api/openstack-loadbalancers/  
DELETE /api/openstack-loadbalancers/{uuid}/  
GET /api/openstack-loadbalancers/{uuid}/  
PATCH /api/openstack-loadbalancers/{uuid}/  
PUT /api/openstack-loadbalancers/{uuid}/  
POST /api/openstack-loadbalancers/{uuid}/attach_floating_ip/  
POST /api/openstack-loadbalancers/{uuid}/detach_floating_ip/  
POST /api/openstack-loadbalancers/{uuid}/update_vip_security_groups/  
GET /api/openstack-pool-members/  
HEAD /api/openstack-pool-members/  
POST /api/openstack-pool-members/  
DELETE /api/openstack-pool-members/{uuid}/  
GET /api/openstack-pool-members/{uuid}/  
PATCH /api/openstack-pool-members/{uuid}/  
PUT /api/openstack-pool-members/{uuid}/  
GET /api/openstack-pools/  
HEAD /api/openstack-pools/  
POST /api/openstack-pools/  
DELETE /api/openstack-pools/{uuid}/  
GET /api/openstack-pools/{uuid}/  
PATCH /api/openstack-pools/{uuid}/  
PUT /api/openstack-pools/{uuid}/  
POST /api/stats/table-growth/  
DELETE /api/user-permission-requests/{uuid}/  
POST /api/users/{uuid}/remove_password/  

### Deleted Endpoints: None

---------------------------

### Modified Endpoints: 303

---------------------------
GET /api/aws-instances/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: marketplace_offering_type

POST /api/aws-instances/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/aws-instances/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PATCH /api/aws-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PUT /api/aws-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/aws-volumes/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: marketplace_offering_type

POST /api/aws-volumes/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/aws-volumes/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PATCH /api/aws-volumes/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PUT /api/aws-volumes/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/azure-public-ips/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: marketplace_offering_type

POST /api/azure-public-ips/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/azure-public-ips/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PATCH /api/azure-public-ips/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PUT /api/azure-public-ips/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/azure-resource-groups/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: marketplace_offering_type

GET /api/azure-resource-groups/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/azure-sql-databases/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: marketplace_offering_type

POST /api/azure-sql-databases/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/azure-sql-databases/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PATCH /api/azure-sql-databases/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PUT /api/azure-sql-databases/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/azure-sql-servers/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: marketplace_offering_type

POST /api/azure-sql-servers/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/azure-sql-servers/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PATCH /api/azure-sql-servers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PUT /api/azure-sql-servers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/azure-virtualmachines/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: marketplace_offering_type

POST /api/azure-virtualmachines/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/azure-virtualmachines/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PATCH /api/azure-virtualmachines/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PUT /api/azure-virtualmachines/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/booking-offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: partitions
                - Items changed
                  - Properties changed
                    - New property: cpu_arch
                    - New property: gpu_arch
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: offering_user_auto_deletion
              - Modified property: software_catalogs
                - Items changed
                  - Properties changed
                    - Modified property: partition
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/PartitionSummary
                          - Properties changed
                            - New property: cpu_arch
                            - New property: gpu_arch

GET /api/booking-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: partitions
              - Items changed
                - Properties changed
                  - New property: cpu_arch
                  - New property: gpu_arch
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: offering_user_auto_deletion
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: partition
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/PartitionSummary
                        - Properties changed
                          - New property: cpu_arch
                          - New property: gpu_arch

GET /api/chat-messages/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: action_taken
              - New required property: pii_categories
              - New required property: severity
              - Deleted required property: injection_score
              - Deleted required property: injection_severity
            - Properties changed
              - New property: action_taken
              - New property: pii_categories
              - New property: severity
              - Deleted property: injection_score
              - Deleted property: injection_severity

POST /api/chat/stream/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: update_thread_name
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/x-ndjson
        - Schema changed
          - Properties changed
            - New property: w

GET /api/customer-quotas/

- New query param: quota_name

HEAD /api/customer-quotas/

- New query param: quota_name

GET /api/digitalocean-droplets/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: marketplace_offering_type

POST /api/digitalocean-droplets/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/digitalocean-droplets/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PATCH /api/digitalocean-droplets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PUT /api/digitalocean-droplets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/google-auth/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [allowed_domains]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: allowed_domains

GET /api/google-auth/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [allowed_domains]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: allowed_domains

GET /api/google-auth/{uuid}/authorize/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [allowed_domains]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: allowed_domains

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
                  - New enum values: [user_password_removed_by_staff chat_pii_detected]

POST /api/hooks-email/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [user_password_removed_by_staff chat_pii_detected]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [user_password_removed_by_staff chat_pii_detected]

GET /api/hooks-email/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [user_password_removed_by_staff chat_pii_detected]

PATCH /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [user_password_removed_by_staff chat_pii_detected]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [user_password_removed_by_staff chat_pii_detected]

PUT /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [user_password_removed_by_staff chat_pii_detected]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [user_password_removed_by_staff chat_pii_detected]

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
                  - New enum values: [user_password_removed_by_staff chat_pii_detected]

POST /api/hooks-web/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [user_password_removed_by_staff chat_pii_detected]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [user_password_removed_by_staff chat_pii_detected]

GET /api/hooks-web/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [user_password_removed_by_staff chat_pii_detected]

PATCH /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [user_password_removed_by_staff chat_pii_detected]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [user_password_removed_by_staff chat_pii_detected]

PUT /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [user_password_removed_by_staff chat_pii_detected]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [user_password_removed_by_staff chat_pii_detected]

GET /api/marketplace-course-accounts/

- Modified query param: state
  - Schema changed
    - Items changed
      - New enum values: [Pending]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: state
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/CourseAccountStateEnum
                  - Schemas deleted: #/components/schemas/ServiceAccountState

HEAD /api/marketplace-course-accounts/

- Modified query param: state
  - Schema changed
    - Items changed
      - New enum values: [Pending]

POST /api/marketplace-course-accounts/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/CourseAccountStateEnum
                - Schemas deleted: #/components/schemas/ServiceAccountState

POST /api/marketplace-course-accounts/create_bulk/

- Modified query param: state
  - Schema changed
    - Items changed
      - New enum values: [Pending]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: state
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/CourseAccountStateEnum
                  - Schemas deleted: #/components/schemas/ServiceAccountState

GET /api/marketplace-course-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/CourseAccountStateEnum
                - Schemas deleted: #/components/schemas/ServiceAccountState

GET /api/marketplace-customer-service-accounts/

- Modified query param: state
  - Schema changed
    - Items changed
      - Type changed from '' to 'string'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: state
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/ServiceAccountState
                    - Type changed from '' to 'string'

HEAD /api/marketplace-customer-service-accounts/

- Modified query param: state
  - Schema changed
    - Items changed
      - Type changed from '' to 'string'

POST /api/marketplace-customer-service-accounts/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ServiceAccountState
                  - Type changed from '' to 'string'

GET /api/marketplace-customer-service-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ServiceAccountState
                  - Type changed from '' to 'string'

PATCH /api/marketplace-customer-service-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ServiceAccountState
                  - Type changed from '' to 'string'

PUT /api/marketplace-customer-service-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ServiceAccountState
                  - Type changed from '' to 'string'

POST /api/marketplace-customer-service-accounts/{uuid}/rotate_api_key/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ServiceAccountState
                  - Type changed from '' to 'string'

GET /api/marketplace-integration-statuses/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: agent_type
            - Properties changed
              - New property: agent_type

GET /api/marketplace-integration-statuses/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: agent_type
          - Properties changed
            - New property: agent_type

POST /api/marketplace-offering-users/{uuid}/begin_creating/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/scopes/- with value: 'offering'

GET /api/marketplace-offering-users/{uuid}/checklist_review/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/scopes/- with value: 'offering'

GET /api/marketplace-offering-users/{uuid}/completion_review_status/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/scopes/- with value: 'offering'

POST /api/marketplace-offering-users/{uuid}/request_deletion/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/scopes/- with value: 'offering'

POST /api/marketplace-offering-users/{uuid}/set_deleted/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/scopes/- with value: 'offering'

POST /api/marketplace-offering-users/{uuid}/set_deleting/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/scopes/- with value: 'offering'

POST /api/marketplace-offering-users/{uuid}/set_pending_account_linking/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/scopes/- with value: 'offering'

POST /api/marketplace-offering-users/{uuid}/set_pending_additional_validation/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/scopes/- with value: 'offering'

POST /api/marketplace-offering-users/{uuid}/set_validation_complete/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/scopes/- with value: 'offering'

POST /api/marketplace-orders/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: attributes
            - Property 'OneOf' changed
              - Schemas added: #/components/schemas/AzureVirtualMachineCreateOrderAttributes, #/components/schemas/AzureSQLServerCreateOrderAttributes, #/components/schemas/MarketplaceOpenPortalCreateOrderAttributes, #/components/schemas/MarketplaceOpenPortalRemoteCreateOrderAttributes, #/components/schemas/OpenStackTenantCreateOrderAttributes, #/components/schemas/OpenStackInstanceCreateOrderAttributes, #/components/schemas/OpenStackVolumeCreateOrderAttributes, #/components/schemas/SlurmInvoicesSlurmPackageCreateOrderAttributes, #/components/schemas/VMwareVirtualMachineCreateOrderAttributes

GET /api/marketplace-orders/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: partitions
              - Items changed
                - Properties changed
                  - New property: cpu_arch
                  - New property: gpu_arch
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: offering_user_auto_deletion
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: partition
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/PartitionSummary
                        - Properties changed
                          - New property: cpu_arch
                          - New property: gpu_arch

POST /api/marketplace-orders/{uuid}/set_state_done/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/scopes/- with value: 'offering'

POST /api/marketplace-orders/{uuid}/set_state_erred/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/scopes/- with value: 'offering'

POST /api/marketplace-orders/{uuid}/set_state_executing/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/scopes/- with value: 'offering'

GET /api/marketplace-project-service-accounts/

- Modified query param: state
  - Schema changed
    - Items changed
      - Type changed from '' to 'string'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: state
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/ServiceAccountState
                    - Type changed from '' to 'string'

HEAD /api/marketplace-project-service-accounts/

- Modified query param: state
  - Schema changed
    - Items changed
      - Type changed from '' to 'string'

POST /api/marketplace-project-service-accounts/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ServiceAccountState
                  - Type changed from '' to 'string'

GET /api/marketplace-project-service-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ServiceAccountState
                  - Type changed from '' to 'string'

PATCH /api/marketplace-project-service-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ServiceAccountState
                  - Type changed from '' to 'string'

PUT /api/marketplace-project-service-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ServiceAccountState
                  - Type changed from '' to 'string'

POST /api/marketplace-project-service-accounts/{uuid}/rotate_api_key/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: state
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ServiceAccountState
                  - Type changed from '' to 'string'

GET /api/marketplace-provider-offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: partitions
                - Items changed
                  - Properties changed
                    - New property: cpu_arch
                    - New property: gpu_arch
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: offering_user_auto_deletion
              - Modified property: software_catalogs
                - Items changed
                  - Properties changed
                    - Modified property: partition
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/PartitionSummary
                          - Properties changed
                            - New property: cpu_arch
                            - New property: gpu_arch

POST /api/marketplace-provider-offerings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: offering_user_auto_deletion
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: offering_user_auto_deletion
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: offering_user_auto_deletion
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: partitions
              - Items changed
                - Properties changed
                  - New property: cpu_arch
                  - New property: gpu_arch
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: offering_user_auto_deletion
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: partition
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/PartitionSummary
                        - Properties changed
                          - New property: cpu_arch
                          - New property: gpu_arch

GET /api/marketplace-provider-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: partitions
              - Items changed
                - Properties changed
                  - New property: cpu_arch
                  - New property: gpu_arch
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: offering_user_auto_deletion
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: partition
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/PartitionSummary
                        - Properties changed
                          - New property: cpu_arch
                          - New property: gpu_arch

POST /api/marketplace-provider-offerings/{uuid}/add_partition/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: cpu_arch
          - New property: gpu_arch
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: cpu_arch
            - New property: gpu_arch

GET /api/marketplace-provider-offerings/{uuid}/list_course_accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: state
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/CourseAccountStateEnum
                  - Schemas deleted: #/components/schemas/ServiceAccountState

GET /api/marketplace-provider-offerings/{uuid}/list_customer_service_accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: state
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/ServiceAccountState
                    - Type changed from '' to 'string'

GET /api/marketplace-provider-offerings/{uuid}/list_customer_users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [has_usable_password]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: has_usable_password

GET /api/marketplace-provider-offerings/{uuid}/list_project_service_accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: state
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/ServiceAccountState
                    - Type changed from '' to 'string'

POST /api/marketplace-provider-offerings/{uuid}/move_offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: partitions
              - Items changed
                - Properties changed
                  - New property: cpu_arch
                  - New property: gpu_arch
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: offering_user_auto_deletion
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: partition
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/PartitionSummary
                        - Properties changed
                          - New property: cpu_arch
                          - New property: gpu_arch

POST /api/marketplace-provider-offerings/{uuid}/update_integration/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: offering_user_auto_deletion

PATCH /api/marketplace-provider-offerings/{uuid}/update_partition/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: cpu_arch
          - New property: gpu_arch
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: cpu_arch
            - New property: gpu_arch

GET /api/marketplace-provider-offerings/{uuid}/user_has_resource_access/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: partitions
              - Items changed
                - Properties changed
                  - New property: cpu_arch
                  - New property: gpu_arch
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: offering_user_auto_deletion
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: partition
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/PartitionSummary
                        - Properties changed
                          - New property: cpu_arch
                          - New property: gpu_arch

GET /api/marketplace-provider-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: partitions
              - Items changed
                - Properties changed
                  - New property: cpu_arch
                  - New property: gpu_arch
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: offering_user_auto_deletion
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: partition
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/PartitionSummary
                        - Properties changed
                          - New property: cpu_arch
                          - New property: gpu_arch

GET /api/marketplace-public-offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: partitions
                - Items changed
                  - Properties changed
                    - New property: cpu_arch
                    - New property: gpu_arch
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: offering_user_auto_deletion
              - Modified property: software_catalogs
                - Items changed
                  - Properties changed
                    - Modified property: partition
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/PartitionSummary
                          - Properties changed
                            - New property: cpu_arch
                            - New property: gpu_arch

GET /api/marketplace-public-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: partitions
              - Items changed
                - Properties changed
                  - New property: cpu_arch
                  - New property: gpu_arch
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: offering_user_auto_deletion
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: partition
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/PartitionSummary
                        - Properties changed
                          - New property: cpu_arch
                          - New property: gpu_arch

GET /api/marketplace-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: partitions
              - Items changed
                - Properties changed
                  - New property: cpu_arch
                  - New property: gpu_arch
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: offering_user_auto_deletion
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: partition
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/PartitionSummary
                        - Properties changed
                          - New property: cpu_arch
                          - New property: gpu_arch

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
                      - New property: offering_user_auto_deletion

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
                    - New property: offering_user_auto_deletion

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
                    - New property: offering_user_auto_deletion

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
                    - New property: offering_user_auto_deletion

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
                    - New property: offering_user_auto_deletion

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
                    - New property: offering_user_auto_deletion

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
                    - New property: offering_user_auto_deletion

POST /api/marketplace-script-dry-run/{uuid}/async_run/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: partitions
              - Items changed
                - Properties changed
                  - New property: cpu_arch
                  - New property: gpu_arch
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: offering_user_auto_deletion
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: partition
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/PartitionSummary
                        - Properties changed
                          - New property: cpu_arch
                          - New property: gpu_arch

POST /api/marketplace-script-dry-run/{uuid}/run/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: partitions
              - Items changed
                - Properties changed
                  - New property: cpu_arch
                  - New property: gpu_arch
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: offering_user_auto_deletion
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: partition
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/PartitionSummary
                        - Properties changed
                          - New property: cpu_arch
                          - New property: gpu_arch

GET /api/marketplace-service-providers/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [allowed_domains]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: allowed_domains

POST /api/marketplace-service-providers/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: allowed_domains
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: allowed_domains
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: allowed_domains
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: allowed_domains

GET /api/marketplace-service-providers/{service_provider_uuid}/course_accounts/

- Modified query param: state
  - Schema changed
    - Items changed
      - New enum values: [Pending]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: state
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/CourseAccountStateEnum
                  - Schemas deleted: #/components/schemas/ServiceAccountState

GET /api/marketplace-service-providers/{service_provider_uuid}/customer_projects/

- New query param: user_uuid_with_active_role

GET /api/marketplace-service-providers/{service_provider_uuid}/project_service_accounts/

- Modified query param: state
  - Schema changed
    - Items changed
      - Type changed from '' to 'string'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: state
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/ServiceAccountState
                    - Type changed from '' to 'string'

GET /api/marketplace-service-providers/{service_provider_uuid}/projects/

- New query param: user_uuid_with_active_role

GET /api/marketplace-service-providers/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [allowed_domains]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: allowed_domains

PATCH /api/marketplace-service-providers/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: allowed_domains
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: allowed_domains
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: allowed_domains
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: allowed_domains

PUT /api/marketplace-service-providers/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: allowed_domains
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: allowed_domains
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: allowed_domains
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: allowed_domains

GET /api/marketplace-site-agent-identities/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: created_by
            - Properties changed
              - New property: created_by

POST /api/marketplace-site-agent-identities/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: created_by
          - Properties changed
            - New property: created_by

DELETE /api/marketplace-site-agent-identities/{uuid}/

- Extensions changed
  - Deleted extension: x-permissions

GET /api/marketplace-site-agent-identities/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: created_by
          - Properties changed
            - New property: created_by

PUT /api/marketplace-site-agent-identities/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: created_by
          - Properties changed
            - New property: created_by

POST /api/marketplace-site-agent-identities/{uuid}/register_event_subscription/

- Extensions changed
  - Deleted extension: x-permissions

POST /api/marketplace-site-agent-identities/{uuid}/register_service/

- Extensions changed
  - Deleted extension: x-permissions

DELETE /api/marketplace-site-agent-processors/{uuid}/

- Extensions changed
  - Deleted extension: x-permissions

DELETE /api/marketplace-site-agent-services/{uuid}/

- Extensions changed
  - Deleted extension: x-permissions

POST /api/marketplace-site-agent-services/{uuid}/register_processor/

- Extensions changed
  - Deleted extension: x-permissions

POST /api/marketplace-site-agent-services/{uuid}/set_statistics/

- Extensions changed
  - Deleted extension: x-permissions

GET /api/marketplace-software-catalogs/

- New query param: auto_update_enabled
- New query param: catalog_type
- New query param: description
- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-catalog_type catalog_type]

HEAD /api/marketplace-software-catalogs/

- New query param: auto_update_enabled
- New query param: catalog_type
- New query param: description
- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-catalog_type catalog_type]

GET /api/marketplace-software-catalogs/discover/

- New query param: auto_update_enabled
- New query param: catalog_type
- New query param: description
- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-catalog_type catalog_type]

HEAD /api/marketplace-software-catalogs/discover/

- New query param: auto_update_enabled
- New query param: catalog_type
- New query param: description
- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-catalog_type catalog_type]

GET /api/marketplace-software-packages/

- New query param: catalog_type
- New query param: category
- New query param: gpu_arch
- New query param: has_gpu
- New query param: license
- New query param: parent_software_uuid
- New query param: toolchain_families_compatibility
- New query param: toolchain_name
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: parent_softwares
            - Properties changed
              - New property: parent_softwares
              - Deleted property: parent_software
              - Modified property: versions
                - Items changed
                  - Properties changed
                    - Modified property: targets
                      - Items changed
                        - Properties changed
                          - New property: gpu_architectures

HEAD /api/marketplace-software-packages/

- New query param: catalog_type
- New query param: category
- New query param: gpu_arch
- New query param: has_gpu
- New query param: license
- New query param: parent_software_uuid
- New query param: toolchain_families_compatibility
- New query param: toolchain_name

POST /api/marketplace-software-packages/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: parent_software
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: parent_softwares
          - Properties changed
            - New property: parent_softwares
            - Deleted property: parent_software
            - Modified property: versions
              - Items changed
                - Properties changed
                  - Modified property: targets
                    - Items changed
                      - Properties changed
                        - New property: gpu_architectures

GET /api/marketplace-software-packages/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: parent_softwares
          - Properties changed
            - New property: parent_softwares
            - Deleted property: parent_software
            - Modified property: versions
              - Items changed
                - Properties changed
                  - Modified property: targets
                    - Items changed
                      - Properties changed
                        - New property: gpu_architectures

PATCH /api/marketplace-software-packages/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: parent_software
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: parent_softwares
          - Properties changed
            - New property: parent_softwares
            - Deleted property: parent_software
            - Modified property: versions
              - Items changed
                - Properties changed
                  - Modified property: targets
                    - Items changed
                      - Properties changed
                        - New property: gpu_architectures

PUT /api/marketplace-software-packages/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: parent_software
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: parent_softwares
          - Properties changed
            - New property: parent_softwares
            - Deleted property: parent_software
            - Modified property: versions
              - Items changed
                - Properties changed
                  - Modified property: targets
                    - Items changed
                      - Properties changed
                        - New property: gpu_architectures

GET /api/marketplace-software-targets/

- New query param: gpu_arch
- New query param: has_gpu
- New query param: target_name
- New query param: target_subtype
- New query param: target_type
- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-target_name -target_type target_name target_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: gpu_architectures
            - Properties changed
              - New property: gpu_architectures

HEAD /api/marketplace-software-targets/

- New query param: gpu_arch
- New query param: has_gpu
- New query param: target_name
- New query param: target_subtype
- New query param: target_type
- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-target_name -target_type target_name target_type]

POST /api/marketplace-software-targets/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: gpu_architectures
          - Properties changed
            - New property: gpu_architectures

GET /api/marketplace-software-targets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: gpu_architectures
          - Properties changed
            - New property: gpu_architectures

PATCH /api/marketplace-software-targets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: gpu_architectures
          - Properties changed
            - New property: gpu_architectures

PUT /api/marketplace-software-targets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: gpu_architectures
          - Properties changed
            - New property: gpu_architectures

GET /api/marketplace-software-versions/

- New query param: catalog_type
- New query param: gpu_arch
- New query param: has_gpu
- New query param: release_date_after
- New query param: release_date_before
- New query param: toolchain_families_compatibility
- New query param: toolchain_name
- New query param: toolchain_version
- New query param: version_exact

HEAD /api/marketplace-software-versions/

- New query param: catalog_type
- New query param: gpu_arch
- New query param: has_gpu
- New query param: release_date_after
- New query param: release_date_before
- New query param: toolchain_families_compatibility
- New query param: toolchain_name
- New query param: toolchain_version
- New query param: version_exact

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
                  - New enum values: [user_password_removed_by_staff chat_pii_detected]

GET /api/offering-keycloak-groups/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - Deleted required property: resource

POST /api/offering-keycloak-groups/import_remote/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: resource

GET /api/offering-keycloak-groups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: resource

POST /api/offering-keycloak-groups/{uuid}/set_backend_id/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: resource

GET /api/openportal-allocations/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: marketplace_offering_type

POST /api/openportal-allocations/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/openportal-allocations/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PATCH /api/openportal-allocations/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PUT /api/openportal-allocations/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

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
                    - Required changed
                      - Deleted required property: offering
                    - Properties changed
                      - Modified property: offerings_data
                        - Items changed
                          - Properties changed
                            - Modified property: partitions
                              - Items changed
                                - Properties changed
                                  - New property: cpu_arch
                                  - New property: gpu_arch
                            - Modified property: plugin_options
                              - Property 'AllOf' changed
                                - Modified schema: #/components/schemas/MergedPluginOptions
                                  - Properties changed
                                    - New property: offering_user_auto_deletion
                            - Modified property: software_catalogs
                              - Items changed
                                - Properties changed
                                  - Modified property: partition
                                    - Property 'AllOf' changed
                                      - Modified schema: #/components/schemas/PartitionSummary
                                        - Properties changed
                                          - New property: cpu_arch
                                          - New property: gpu_arch

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
                  - Required changed
                    - Deleted required property: offering
                  - Properties changed
                    - Modified property: offerings_data
                      - Items changed
                        - Properties changed
                          - Modified property: partitions
                            - Items changed
                              - Properties changed
                                - New property: cpu_arch
                                - New property: gpu_arch
                          - Modified property: plugin_options
                            - Property 'AllOf' changed
                              - Modified schema: #/components/schemas/MergedPluginOptions
                                - Properties changed
                                  - New property: offering_user_auto_deletion
                          - Modified property: software_catalogs
                            - Items changed
                              - Properties changed
                                - Modified property: partition
                                  - Property 'AllOf' changed
                                    - Modified schema: #/components/schemas/PartitionSummary
                                      - Properties changed
                                        - New property: cpu_arch
                                        - New property: gpu_arch

GET /api/openportal-project-template/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - Deleted required property: offering
            - Properties changed
              - Modified property: offerings_data
                - Items changed
                  - Properties changed
                    - Modified property: partitions
                      - Items changed
                        - Properties changed
                          - New property: cpu_arch
                          - New property: gpu_arch
                    - Modified property: plugin_options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/MergedPluginOptions
                          - Properties changed
                            - New property: offering_user_auto_deletion
                    - Modified property: software_catalogs
                      - Items changed
                        - Properties changed
                          - Modified property: partition
                            - Property 'AllOf' changed
                              - Modified schema: #/components/schemas/PartitionSummary
                                - Properties changed
                                  - New property: cpu_arch
                                  - New property: gpu_arch

POST /api/openportal-project-template/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: offering
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: offering
          - Properties changed
            - Modified property: offerings_data
              - Items changed
                - Properties changed
                  - Modified property: partitions
                    - Items changed
                      - Properties changed
                        - New property: cpu_arch
                        - New property: gpu_arch
                  - Modified property: plugin_options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/MergedPluginOptions
                        - Properties changed
                          - New property: offering_user_auto_deletion
                  - Modified property: software_catalogs
                    - Items changed
                      - Properties changed
                        - Modified property: partition
                          - Property 'AllOf' changed
                            - Modified schema: #/components/schemas/PartitionSummary
                              - Properties changed
                                - New property: cpu_arch
                                - New property: gpu_arch

GET /api/openportal-project-template/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: offering
          - Properties changed
            - Modified property: offerings_data
              - Items changed
                - Properties changed
                  - Modified property: partitions
                    - Items changed
                      - Properties changed
                        - New property: cpu_arch
                        - New property: gpu_arch
                  - Modified property: plugin_options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/MergedPluginOptions
                        - Properties changed
                          - New property: offering_user_auto_deletion
                  - Modified property: software_catalogs
                    - Items changed
                      - Properties changed
                        - Modified property: partition
                          - Property 'AllOf' changed
                            - Modified schema: #/components/schemas/PartitionSummary
                              - Properties changed
                                - New property: cpu_arch
                                - New property: gpu_arch

PATCH /api/openportal-project-template/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: offering
          - Properties changed
            - Modified property: offerings_data
              - Items changed
                - Properties changed
                  - Modified property: partitions
                    - Items changed
                      - Properties changed
                        - New property: cpu_arch
                        - New property: gpu_arch
                  - Modified property: plugin_options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/MergedPluginOptions
                        - Properties changed
                          - New property: offering_user_auto_deletion
                  - Modified property: software_catalogs
                    - Items changed
                      - Properties changed
                        - Modified property: partition
                          - Property 'AllOf' changed
                            - Modified schema: #/components/schemas/PartitionSummary
                              - Properties changed
                                - New property: cpu_arch
                                - New property: gpu_arch

PUT /api/openportal-project-template/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: offering
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: offering
          - Properties changed
            - Modified property: offerings_data
              - Items changed
                - Properties changed
                  - Modified property: partitions
                    - Items changed
                      - Properties changed
                        - New property: cpu_arch
                        - New property: gpu_arch
                  - Modified property: plugin_options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/MergedPluginOptions
                        - Properties changed
                          - New property: offering_user_auto_deletion
                  - Modified property: software_catalogs
                    - Items changed
                      - Properties changed
                        - Modified property: partition
                          - Property 'AllOf' changed
                            - Modified schema: #/components/schemas/PartitionSummary
                              - Properties changed
                                - New property: cpu_arch
                                - New property: gpu_arch

GET /api/openportal-remote-allocations/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: marketplace_offering_type

POST /api/openportal-remote-allocations/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/openportal-remote-allocations/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PATCH /api/openportal-remote-allocations/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PUT /api/openportal-remote-allocations/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/openportal-unmanaged-projects/

- New query param: user_uuid_with_active_role

HEAD /api/openportal-unmanaged-projects/

- New query param: user_uuid_with_active_role

GET /api/openstack-backups/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: marketplace_offering_type
              - Modified property: instance_ports
                - Items changed
                  - Properties changed
                    - Modified property: security_groups
                      - Items changed
                        - Properties changed
                          - New property: marketplace_offering_type
                          - Modified property: rules
                            - Items changed
                              - Properties changed
                                - Modified property: protocol
                                  - Property 'OneOf' changed
                                    - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                                    - Schemas deleted: #/components/schemas/ProtocolEnum
              - Modified property: instance_security_groups
                - Items changed
                  - Properties changed
                    - Modified property: rules
                      - Items changed
                        - Properties changed
                          - Modified property: protocol
                            - Property 'OneOf' changed
                              - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                              - Schemas deleted: #/components/schemas/ProtocolEnum
              - Modified property: restorations
                - Items changed
                  - Properties changed
                    - Modified property: ports
                      - Items changed
                        - Properties changed
                          - Modified property: security_groups
                            - Items changed
                              - Properties changed
                                - New property: marketplace_offering_type
                                - Modified property: rules
                                  - Items changed
                                    - Properties changed
                                      - Modified property: protocol
                                        - Property 'OneOf' changed
                                          - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                                          - Schemas deleted: #/components/schemas/ProtocolEnum
                    - Modified property: security_groups
                      - Items changed
                        - Properties changed
                          - Modified property: rules
                            - Items changed
                              - Properties changed
                                - Modified property: protocol
                                  - Property 'OneOf' changed
                                    - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                                    - Schemas deleted: #/components/schemas/ProtocolEnum

GET /api/openstack-backups/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - New property: marketplace_offering_type
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: protocol
                                - Property 'OneOf' changed
                                  - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                                  - Schemas deleted: #/components/schemas/ProtocolEnum
            - Modified property: instance_security_groups
              - Items changed
                - Properties changed
                  - Modified property: rules
                    - Items changed
                      - Properties changed
                        - Modified property: protocol
                          - Property 'OneOf' changed
                            - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                            - Schemas deleted: #/components/schemas/ProtocolEnum
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: security_groups
                          - Items changed
                            - Properties changed
                              - New property: marketplace_offering_type
                              - Modified property: rules
                                - Items changed
                                  - Properties changed
                                    - Modified property: protocol
                                      - Property 'OneOf' changed
                                        - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                                        - Schemas deleted: #/components/schemas/ProtocolEnum
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: protocol
                                - Property 'OneOf' changed
                                  - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                                  - Schemas deleted: #/components/schemas/ProtocolEnum

PATCH /api/openstack-backups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - New property: marketplace_offering_type
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: protocol
                                - Property 'OneOf' changed
                                  - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                                  - Schemas deleted: #/components/schemas/ProtocolEnum
            - Modified property: instance_security_groups
              - Items changed
                - Properties changed
                  - Modified property: rules
                    - Items changed
                      - Properties changed
                        - Modified property: protocol
                          - Property 'OneOf' changed
                            - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                            - Schemas deleted: #/components/schemas/ProtocolEnum
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: security_groups
                          - Items changed
                            - Properties changed
                              - New property: marketplace_offering_type
                              - Modified property: rules
                                - Items changed
                                  - Properties changed
                                    - Modified property: protocol
                                      - Property 'OneOf' changed
                                        - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                                        - Schemas deleted: #/components/schemas/ProtocolEnum
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: protocol
                                - Property 'OneOf' changed
                                  - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                                  - Schemas deleted: #/components/schemas/ProtocolEnum

PUT /api/openstack-backups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - New property: marketplace_offering_type
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: protocol
                                - Property 'OneOf' changed
                                  - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                                  - Schemas deleted: #/components/schemas/ProtocolEnum
            - Modified property: instance_security_groups
              - Items changed
                - Properties changed
                  - Modified property: rules
                    - Items changed
                      - Properties changed
                        - Modified property: protocol
                          - Property 'OneOf' changed
                            - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                            - Schemas deleted: #/components/schemas/ProtocolEnum
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: security_groups
                          - Items changed
                            - Properties changed
                              - New property: marketplace_offering_type
                              - Modified property: rules
                                - Items changed
                                  - Properties changed
                                    - Modified property: protocol
                                      - Property 'OneOf' changed
                                        - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                                        - Schemas deleted: #/components/schemas/ProtocolEnum
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: protocol
                                - Property 'OneOf' changed
                                  - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                                  - Schemas deleted: #/components/schemas/ProtocolEnum

POST /api/openstack-backups/{uuid}/restore/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - New property: marketplace_offering_type
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: protocol
                                - Property 'OneOf' changed
                                  - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                                  - Schemas deleted: #/components/schemas/ProtocolEnum
            - Modified property: security_groups
              - Items changed
                - Properties changed
                  - Modified property: rules
                    - Items changed
                      - Properties changed
                        - Modified property: protocol
                          - Property 'OneOf' changed
                            - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                            - Schemas deleted: #/components/schemas/ProtocolEnum

GET /api/openstack-floating-ips/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: marketplace_offering_type

GET /api/openstack-floating-ips/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/openstack-instances/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: marketplace_offering_type
              - Modified property: ports
                - Items changed
                  - Properties changed
                    - Modified property: security_groups
                      - Items changed
                        - Properties changed
                          - New property: marketplace_offering_type
                          - Modified property: rules
                            - Items changed
                              - Properties changed
                                - Modified property: protocol
                                  - Property 'OneOf' changed
                                    - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                                    - Schemas deleted: #/components/schemas/ProtocolEnum
              - Modified property: security_groups
                - Items changed
                  - Properties changed
                    - Modified property: rules
                      - Items changed
                        - Properties changed
                          - Modified property: protocol
                            - Property 'OneOf' changed
                              - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                              - Schemas deleted: #/components/schemas/ProtocolEnum

GET /api/openstack-instances/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - New property: marketplace_offering_type
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: protocol
                                - Property 'OneOf' changed
                                  - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                                  - Schemas deleted: #/components/schemas/ProtocolEnum
            - Modified property: security_groups
              - Items changed
                - Properties changed
                  - Modified property: rules
                    - Items changed
                      - Properties changed
                        - Modified property: protocol
                          - Property 'OneOf' changed
                            - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                            - Schemas deleted: #/components/schemas/ProtocolEnum

PATCH /api/openstack-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - New property: marketplace_offering_type
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: protocol
                                - Property 'OneOf' changed
                                  - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                                  - Schemas deleted: #/components/schemas/ProtocolEnum
            - Modified property: security_groups
              - Items changed
                - Properties changed
                  - Modified property: rules
                    - Items changed
                      - Properties changed
                        - Modified property: protocol
                          - Property 'OneOf' changed
                            - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                            - Schemas deleted: #/components/schemas/ProtocolEnum

PUT /api/openstack-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - New property: marketplace_offering_type
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: protocol
                                - Property 'OneOf' changed
                                  - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                                  - Schemas deleted: #/components/schemas/ProtocolEnum
            - Modified property: security_groups
              - Items changed
                - Properties changed
                  - Modified property: rules
                    - Items changed
                      - Properties changed
                        - Modified property: protocol
                          - Property 'OneOf' changed
                            - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                            - Schemas deleted: #/components/schemas/ProtocolEnum

POST /api/openstack-instances/{uuid}/backup/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type
            - Modified property: instance_ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - New property: marketplace_offering_type
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: protocol
                                - Property 'OneOf' changed
                                  - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                                  - Schemas deleted: #/components/schemas/ProtocolEnum
            - Modified property: instance_security_groups
              - Items changed
                - Properties changed
                  - Modified property: rules
                    - Items changed
                      - Properties changed
                        - Modified property: protocol
                          - Property 'OneOf' changed
                            - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                            - Schemas deleted: #/components/schemas/ProtocolEnum
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: security_groups
                          - Items changed
                            - Properties changed
                              - New property: marketplace_offering_type
                              - Modified property: rules
                                - Items changed
                                  - Properties changed
                                    - Modified property: protocol
                                      - Property 'OneOf' changed
                                        - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                                        - Schemas deleted: #/components/schemas/ProtocolEnum
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: protocol
                                - Property 'OneOf' changed
                                  - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                                  - Schemas deleted: #/components/schemas/ProtocolEnum

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
                    - New property: marketplace_offering_type
                    - Modified property: rules
                      - Items changed
                        - Properties changed
                          - Modified property: protocol
                            - Property 'OneOf' changed
                              - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                              - Schemas deleted: #/components/schemas/ProtocolEnum

GET /api/openstack-networks/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: marketplace_offering_type

GET /api/openstack-networks/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PATCH /api/openstack-networks/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PUT /api/openstack-networks/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

POST /api/openstack-networks/{uuid}/create_subnet/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/openstack-ports/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: marketplace_offering_type

POST /api/openstack-ports/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/openstack-ports/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PATCH /api/openstack-ports/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PUT /api/openstack-ports/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/openstack-routers/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: marketplace_offering_type
              - Modified property: ports
                - Items changed
                  - Properties changed
                    - Modified property: security_groups
                      - Items changed
                        - Properties changed
                          - New property: marketplace_offering_type
                          - Modified property: rules
                            - Items changed
                              - Properties changed
                                - Modified property: protocol
                                  - Property 'OneOf' changed
                                    - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                                    - Schemas deleted: #/components/schemas/ProtocolEnum

GET /api/openstack-routers/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: security_groups
                    - Items changed
                      - Properties changed
                        - New property: marketplace_offering_type
                        - Modified property: rules
                          - Items changed
                            - Properties changed
                              - Modified property: protocol
                                - Property 'OneOf' changed
                                  - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                                  - Schemas deleted: #/components/schemas/ProtocolEnum

GET /api/openstack-security-groups/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: marketplace_offering_type
              - Modified property: rules
                - Items changed
                  - Properties changed
                    - Modified property: protocol
                      - Property 'OneOf' changed
                        - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                        - Schemas deleted: #/components/schemas/ProtocolEnum

GET /api/openstack-security-groups/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type
            - Modified property: rules
              - Items changed
                - Properties changed
                  - Modified property: protocol
                    - Property 'OneOf' changed
                      - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                      - Schemas deleted: #/components/schemas/ProtocolEnum

POST /api/openstack-security-groups/{uuid}/set_rules/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Items changed
          - Properties changed
            - Modified property: protocol
              - Property 'OneOf' changed
                - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                - Schemas deleted: #/components/schemas/ProtocolEnum

GET /api/openstack-server-groups/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: marketplace_offering_type

POST /api/openstack-server-groups/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/openstack-server-groups/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/openstack-snapshots/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: marketplace_offering_type

GET /api/openstack-snapshots/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PATCH /api/openstack-snapshots/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PUT /api/openstack-snapshots/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

POST /api/openstack-snapshots/{uuid}/restore/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/openstack-subnets/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: marketplace_offering_type

GET /api/openstack-subnets/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PATCH /api/openstack-subnets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PUT /api/openstack-subnets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/openstack-tenants/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: marketplace_offering_type

GET /api/openstack-tenants/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

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
                      - Modified property: protocol
                        - Property 'OneOf' changed
                          - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                          - Schemas deleted: #/components/schemas/ProtocolEnum
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

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
                      - Modified property: protocol
                        - Property 'OneOf' changed
                          - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                          - Schemas deleted: #/components/schemas/ProtocolEnum
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

POST /api/openstack-tenants/{uuid}/create_floating_ip/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

POST /api/openstack-tenants/{uuid}/create_network/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

POST /api/openstack-tenants/{uuid}/create_security_group/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: rules
            - Items changed
              - Properties changed
                - Modified property: protocol
                  - Property 'OneOf' changed
                    - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                    - Schemas deleted: #/components/schemas/ProtocolEnum
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type
            - Modified property: rules
              - Items changed
                - Properties changed
                  - Modified property: protocol
                    - Property 'OneOf' changed
                      - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                      - Schemas deleted: #/components/schemas/ProtocolEnum

POST /api/openstack-tenants/{uuid}/create_server_group/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

POST /api/openstack-tenants/{uuid}/pull_security_groups/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

POST /api/openstack-tenants/{uuid}/pull_server_groups/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

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
                  - Modified property: protocol
                    - Property 'OneOf' changed
                      - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                      - Schemas deleted: #/components/schemas/ProtocolEnum

GET /api/openstack-volumes/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: marketplace_offering_type

GET /api/openstack-volumes/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PATCH /api/openstack-volumes/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PUT /api/openstack-volumes/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

POST /api/openstack-volumes/{uuid}/snapshot/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

POST /api/openstack/discovery/discover_external_networks/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: auth_type

POST /api/openstack/discovery/discover_flavors/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: auth_type

POST /api/openstack/discovery/discover_instance_availability_zones/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: auth_type

POST /api/openstack/discovery/discover_volume_availability_zones/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: auth_type

POST /api/openstack/discovery/discover_volume_types/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: auth_type

POST /api/openstack/discovery/preview_service_attributes/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: auth_type

POST /api/openstack/discovery/validate_credentials/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: auth_type

GET /api/override-settings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: ENABLE_ISSUES_FOR_USER_SSH_KEY_CHANGES
            - New property: OIDC_DEFAULT_LOGOUT_URL
            - New property: SSH_KEY_ALLOWED_TYPES
            - New property: SSH_KEY_MIN_RSA_KEY_SIZE

POST /api/override-settings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: ENABLE_ISSUES_FOR_USER_SSH_KEY_CHANGES
          - New property: OIDC_DEFAULT_LOGOUT_URL
          - New property: SSH_KEY_ALLOWED_TYPES
          - New property: SSH_KEY_MIN_RSA_KEY_SIZE
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: ENABLE_ISSUES_FOR_USER_SSH_KEY_CHANGES
          - New property: OIDC_DEFAULT_LOGOUT_URL
          - New property: SSH_KEY_ALLOWED_TYPES
          - New property: SSH_KEY_MIN_RSA_KEY_SIZE
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: ENABLE_ISSUES_FOR_USER_SSH_KEY_CHANGES
          - New property: OIDC_DEFAULT_LOGOUT_URL
          - New property: SSH_KEY_ALLOWED_TYPES
          - New property: SSH_KEY_MIN_RSA_KEY_SIZE

GET /api/project-quotas/

- New query param: quota_name

HEAD /api/project-quotas/

- New query param: quota_name

GET /api/projects/

- New query param: user_uuid_with_active_role

HEAD /api/projects/

- New query param: user_uuid_with_active_role

GET /api/rabbitmq-user-stats/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: connections
                - Items changed
                  - Properties changed
                    - Modified property: client_properties
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/RmqClientProperties
                          - Properties changed
                            - Modified property: platform
                              - Description changed from 'Client platform (e.g., 'Python 3.11')' to 'Client platform (e.g., 'Python 3.12')'

GET /api/rancher-apps/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: marketplace_offering_type

POST /api/rancher-apps/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/rancher-apps/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PATCH /api/rancher-apps/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PUT /api/rancher-apps/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

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
                    - Modified property: protocol
                      - Property 'OneOf' changed
                        - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                        - Schemas deleted: #/components/schemas/ProtocolEnum

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
                  - Modified property: protocol
                    - Property 'OneOf' changed
                      - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                      - Schemas deleted: #/components/schemas/ProtocolEnum

PATCH /api/rancher-cluster-security-groups/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: rules
            - Items changed
              - Properties changed
                - Modified property: protocol
                  - Property 'OneOf' changed
                    - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                    - Schemas deleted: #/components/schemas/ProtocolEnum
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: rules
              - Items changed
                - Properties changed
                  - Modified property: protocol
                    - Property 'OneOf' changed
                      - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                      - Schemas deleted: #/components/schemas/ProtocolEnum

PUT /api/rancher-cluster-security-groups/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: rules
            - Items changed
              - Properties changed
                - Modified property: protocol
                  - Property 'OneOf' changed
                    - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                    - Schemas deleted: #/components/schemas/ProtocolEnum
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: rules
              - Items changed
                - Properties changed
                  - Modified property: protocol
                    - Property 'OneOf' changed
                      - Schemas added: #/components/schemas/SecurityGroupRuleProtocolEnum
                      - Schemas deleted: #/components/schemas/ProtocolEnum

GET /api/rancher-clusters/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: marketplace_offering_type

GET /api/rancher-clusters/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PATCH /api/rancher-clusters/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PUT /api/rancher-clusters/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

POST /api/rancher-clusters/{uuid}/create_management_security_group/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/rancher-ingresses/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: marketplace_offering_type

POST /api/rancher-ingresses/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/rancher-ingresses/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PATCH /api/rancher-ingresses/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PUT /api/rancher-ingresses/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/rancher-ingresses/{uuid}/yaml/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PUT /api/rancher-ingresses/{uuid}/yaml/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/rancher-services/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: marketplace_offering_type

POST /api/rancher-services/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: marketplace_offering_type
          - Properties changed
            - New property: marketplace_offering_type

GET /api/rancher-services/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PATCH /api/rancher-services/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PUT /api/rancher-services/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/rancher-services/{uuid}/yaml/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PUT /api/rancher-services/{uuid}/yaml/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/slurm-allocations/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: marketplace_offering_type

POST /api/slurm-allocations/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/slurm-allocations/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PATCH /api/slurm-allocations/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PUT /api/slurm-allocations/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/support-users/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - Deleted required property: backend_id
              - Deleted required property: user

GET /api/support-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: backend_id
            - Deleted required property: user

GET /api/user-invitations/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: extra_invitation_text
                - MaxLength changed from 250 to 2000

POST /api/user-invitations/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: extra_invitation_text
            - MaxLength changed from 250 to 2000
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: extra_invitation_text
              - MaxLength changed from 250 to 2000

GET /api/user-invitations/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: extra_invitation_text
              - MaxLength changed from 250 to 2000

GET /api/users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [has_usable_password]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: has_usable_password

POST /api/users/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_usable_password

GET /api/users/me/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [has_usable_password]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_usable_password

GET /api/users/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [has_usable_password]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_usable_password

PATCH /api/users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_usable_password

PUT /api/users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_usable_password

GET /api/vmware-disks/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: marketplace_offering_type

GET /api/vmware-disks/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/vmware-ports/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: marketplace_offering_type

GET /api/vmware-ports/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/vmware-virtual-machine/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: marketplace_offering_type

POST /api/vmware-virtual-machine/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

GET /api/vmware-virtual-machine/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [marketplace_offering_type]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PATCH /api/vmware-virtual-machine/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

PUT /api/vmware-virtual-machine/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

POST /api/vmware-virtual-machine/{uuid}/create_disk/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type

POST /api/vmware-virtual-machine/{uuid}/create_port/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: marketplace_offering_type
