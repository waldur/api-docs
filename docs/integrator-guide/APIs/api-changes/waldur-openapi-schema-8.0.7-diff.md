# OpenAPI schema diff - 8.0.7

## For version 8.0.7

### New Endpoints: 60

---------------------
POST /api/assignment-items/{uuid}/force-unblock/  
GET /api/call-managing-organisations/global_stats_performance/  
HEAD /api/call-managing-organisations/global_stats_performance/  
GET /api/call-managing-organisations/global_stats_resource_demand/  
HEAD /api/call-managing-organisations/global_stats_resource_demand/  
GET /api/call-managing-organisations/global_stats_review_progress/  
HEAD /api/call-managing-organisations/global_stats_review_progress/  
POST /api/call-reviewer-pools/{uuid}/force-accept/  
POST /api/chat-threads/{uuid}/cancel/  
GET /api/identity-bridge/allowed-fields/  
POST /api/marketplace-article-code-update/apply/  
POST /api/marketplace-article-code-update/preview/  
GET /api/marketplace-attribute-options/  
HEAD /api/marketplace-attribute-options/  
POST /api/marketplace-attribute-options/  
DELETE /api/marketplace-attribute-options/{uuid}/  
GET /api/marketplace-attribute-options/{uuid}/  
PATCH /api/marketplace-attribute-options/{uuid}/  
PUT /api/marketplace-attribute-options/{uuid}/  
GET /api/marketplace-attributes/  
HEAD /api/marketplace-attributes/  
POST /api/marketplace-attributes/  
DELETE /api/marketplace-attributes/{uuid}/  
GET /api/marketplace-attributes/{uuid}/  
PATCH /api/marketplace-attributes/{uuid}/  
PUT /api/marketplace-attributes/{uuid}/  
POST /api/marketplace-course-accounts/{uuid}/retry/  
GET /api/marketplace-orders/{uuid}/resource/  
POST /api/marketplace-orders/{uuid}/retry/  
GET /api/marketplace-provider-offerings/{uuid}/state_counters/  
POST /api/marketplace-provider-offerings/{uuid}/switch_billing_mode/  
POST /api/marketplace-provider-resources/{uuid}/set_effective_id/  
POST /api/marketplace-provider-resources/{uuid}/set_end_date/  
POST /api/marketplace-resources/{uuid}/set_end_date/  
GET /api/marketplace-stats/project_creation_trend/  
HEAD /api/marketplace-stats/project_creation_trend/  
GET /api/marketplace-stats/resource_creation_trend/  
HEAD /api/marketplace-stats/resource_creation_trend/  
GET /api/marketplace-stats/top_service_providers_by_resources/  
HEAD /api/marketplace-stats/top_service_providers_by_resources/  
GET /api/marketplace-stats/user_nationality/  
HEAD /api/marketplace-stats/user_nationality/  
GET /api/marketplace-stats/user_residence_country/  
HEAD /api/marketplace-stats/user_residence_country/  
POST /api/openstack-loadbalancers/{uuid}/unlink/  
GET /api/personal-access-tokens/  
HEAD /api/personal-access-tokens/  
POST /api/personal-access-tokens/  
GET /api/personal-access-tokens/available_scopes/  
HEAD /api/personal-access-tokens/available_scopes/  
DELETE /api/personal-access-tokens/{uuid}/  
GET /api/personal-access-tokens/{uuid}/  
POST /api/personal-access-tokens/{uuid}/rotate/  
GET /api/project-end-date-change-requests/  
HEAD /api/project-end-date-change-requests/  
POST /api/project-end-date-change-requests/  
GET /api/project-end-date-change-requests/{uuid}/  
POST /api/project-end-date-change-requests/{uuid}/approve/  
POST /api/project-end-date-change-requests/{uuid}/cancel/  
POST /api/project-end-date-change-requests/{uuid}/reject/  

### Deleted Endpoints: 2

------------------------
POST /api/openstack-loadbalancers/{uuid}/update_vip_security_groups/  
POST /api/remote-waldur-api/pull_offering_invoices/{uuid}/  

### Modified Endpoints: 2338

----------------------------
POST /api-auth/logout/

- Security changed
  - New security requirements: waldurPATAuth

POST /api-auth/password/

- Security changed
  - New security requirements: waldurPATAuth

GET /api-auth/saml2/providers/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/access-subnets/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/access-subnets/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/access-subnets/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/access-subnets/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/access-subnets/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/access-subnets/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/access-subnets/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/admin-announcements/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/admin-announcements/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/admin-announcements/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/admin-announcements/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/admin-announcements/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/admin-announcements/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/admin-announcements/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/admin/arrow/billing-sync-items/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/admin/arrow/billing-sync-items/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/admin/arrow/billing-sync-items/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/admin/arrow/billing-syncs/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/admin/arrow/billing-syncs/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/admin/arrow/billing-syncs/cleanup_consumption/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/admin/arrow/billing-syncs/consumption_statistics/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/admin/arrow/billing-syncs/consumption_statistics/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/admin/arrow/billing-syncs/consumption_status/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/admin/arrow/billing-syncs/consumption_status/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/admin/arrow/billing-syncs/fetch_billing_export/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/admin/arrow/billing-syncs/fetch_consumption/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/admin/arrow/billing-syncs/fetch_license_info/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/admin/arrow/billing-syncs/pause_sync/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/admin/arrow/billing-syncs/pending_records/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/admin/arrow/billing-syncs/pending_records/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/admin/arrow/billing-syncs/reconcile/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/admin/arrow/billing-syncs/resume_sync/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/admin/arrow/billing-syncs/sync_resource_historical_consumption/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/admin/arrow/billing-syncs/sync_resources/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/admin/arrow/billing-syncs/trigger_consumption_sync/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/admin/arrow/billing-syncs/trigger_reconciliation/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/admin/arrow/billing-syncs/trigger_sync/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/admin/arrow/billing-syncs/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/admin/arrow/consumption-records/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/admin/arrow/consumption-records/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/admin/arrow/consumption-records/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/admin/arrow/customer-mappings/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/admin/arrow/customer-mappings/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/admin/arrow/customer-mappings/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/admin/arrow/customer-mappings/available_customers/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/admin/arrow/customer-mappings/available_customers/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/admin/arrow/customer-mappings/sync_from_arrow/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/admin/arrow/customer-mappings/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/admin/arrow/customer-mappings/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/admin/arrow/customer-mappings/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/admin/arrow/customer-mappings/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/admin/arrow/customer-mappings/{uuid}/billing_summary/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/admin/arrow/customer-mappings/{uuid}/discover_licenses/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/admin/arrow/customer-mappings/{uuid}/fetch_arrow_data/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/admin/arrow/customer-mappings/{uuid}/import_license/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/admin/arrow/customer-mappings/{uuid}/link_resource/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/admin/arrow/settings/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/admin/arrow/settings/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/admin/arrow/settings/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/admin/arrow/settings/discover_customers/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/admin/arrow/settings/preview_settings/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/admin/arrow/settings/save_settings/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/admin/arrow/settings/validate_credentials/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/admin/arrow/settings/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/admin/arrow/settings/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/admin/arrow/settings/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/admin/arrow/settings/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/admin/arrow/vendor-offering-mappings/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/admin/arrow/vendor-offering-mappings/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/admin/arrow/vendor-offering-mappings/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/admin/arrow/vendor-offering-mappings/vendor_choices/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/admin/arrow/vendor-offering-mappings/vendor_choices/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/admin/arrow/vendor-offering-mappings/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/admin/arrow/vendor-offering-mappings/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/admin/arrow/vendor-offering-mappings/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/admin/arrow/vendor-offering-mappings/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/assignment-batches/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/assignment-batches/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/assignment-batches/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: items
              - Items changed
                - Required changed
                  - New required property: overridden_at
                  - New required property: overridden_by_name
                  - New required property: override_reason
                - Properties changed
                  - New property: overridden_at
                  - New property: overridden_by_name
                  - New property: override_reason
- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/assignment-batches/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/assignment-batches/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: items
              - Items changed
                - Required changed
                  - New required property: overridden_at
                  - New required property: overridden_by_name
                  - New required property: override_reason
                - Properties changed
                  - New property: overridden_at
                  - New property: overridden_by_name
                  - New property: override_reason
- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/assignment-batches/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: items
              - Items changed
                - Required changed
                  - New required property: overridden_at
                  - New required property: overridden_by_name
                  - New required property: override_reason
                - Properties changed
                  - New property: overridden_at
                  - New property: overridden_by_name
                  - New property: override_reason
- Security changed
  - New security requirements: waldurPATAuth

PUT /api/assignment-batches/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: items
              - Items changed
                - Required changed
                  - New required property: overridden_at
                  - New required property: overridden_by_name
                  - New required property: override_reason
                - Properties changed
                  - New property: overridden_at
                  - New property: overridden_by_name
                  - New property: override_reason
- Security changed
  - New security requirements: waldurPATAuth

POST /api/assignment-batches/{uuid}/cancel/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/assignment-batches/{uuid}/extend-deadline/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/assignment-batches/{uuid}/send/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/assignment-items/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: overridden_at
              - New required property: overridden_by_name
              - New required property: override_reason
            - Properties changed
              - New property: overridden_at
              - New property: overridden_by_name
              - New property: override_reason
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/assignment-items/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/assignment-items/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: overridden_at
            - New required property: overridden_by_name
            - New required property: override_reason
          - Properties changed
            - New property: overridden_at
            - New property: overridden_by_name
            - New property: override_reason
- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/assignment-items/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/assignment-items/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: overridden_at
            - New required property: overridden_by_name
            - New required property: override_reason
          - Properties changed
            - New property: overridden_at
            - New property: overridden_by_name
            - New property: override_reason
- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/assignment-items/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: overridden_at
            - New required property: overridden_by_name
            - New required property: override_reason
          - Properties changed
            - New property: overridden_at
            - New property: overridden_by_name
            - New property: override_reason
- Security changed
  - New security requirements: waldurPATAuth

PUT /api/assignment-items/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: overridden_at
            - New required property: overridden_by_name
            - New required property: override_reason
          - Properties changed
            - New property: overridden_at
            - New property: overridden_by_name
            - New property: override_reason
- Security changed
  - New security requirements: waldurPATAuth

POST /api/assignment-items/{uuid}/accept/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/assignment-items/{uuid}/decline/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/assignment-items/{uuid}/reassign/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/assignment-items/{uuid}/suggest_alternatives/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/auth-tokens/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/auth-tokens/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/auth-tokens/{user_id}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/auth-tokens/{user_id}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/auth-valimo/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/auth-valimo/result/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/autoprovisioning-rules/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/autoprovisioning-rules/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/autoprovisioning-rules/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/autoprovisioning-rules/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/autoprovisioning-rules/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/autoprovisioning-rules/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/autoprovisioning-rules/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/aws-images/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/aws-images/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/aws-images/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/aws-instances/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/aws-instances/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/aws-instances/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/aws-instances/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/aws-instances/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/aws-instances/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/aws-instances/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/aws-instances/{uuid}/pull/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/aws-instances/{uuid}/resize/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/aws-instances/{uuid}/restart/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/aws-instances/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/aws-instances/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/aws-instances/{uuid}/start/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/aws-instances/{uuid}/stop/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/aws-instances/{uuid}/unlink/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/aws-regions/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/aws-regions/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/aws-regions/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/aws-sizes/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/aws-sizes/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/aws-sizes/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/aws-volumes/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/aws-volumes/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/aws-volumes/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/aws-volumes/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/aws-volumes/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/aws-volumes/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/aws-volumes/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/aws-volumes/{uuid}/attach/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/aws-volumes/{uuid}/detach/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/aws-volumes/{uuid}/pull/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/aws-volumes/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/aws-volumes/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/aws-volumes/{uuid}/unlink/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/azure-images/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/azure-images/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/azure-images/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/azure-locations/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/azure-locations/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/azure-locations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/azure-public-ips/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/azure-public-ips/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/azure-public-ips/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/azure-public-ips/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/azure-public-ips/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/azure-public-ips/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/azure-public-ips/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/azure-public-ips/{uuid}/pull/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/azure-public-ips/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/azure-public-ips/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/azure-public-ips/{uuid}/unlink/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/azure-resource-groups/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/azure-resource-groups/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/azure-resource-groups/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/azure-sizes/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/azure-sizes/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/azure-sizes/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/azure-sql-databases/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/azure-sql-databases/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/azure-sql-databases/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/azure-sql-databases/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/azure-sql-databases/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/azure-sql-databases/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/azure-sql-databases/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/azure-sql-databases/{uuid}/pull/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/azure-sql-databases/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/azure-sql-databases/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/azure-sql-databases/{uuid}/unlink/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/azure-sql-servers/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/azure-sql-servers/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/azure-sql-servers/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/azure-sql-servers/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/azure-sql-servers/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/azure-sql-servers/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/azure-sql-servers/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/azure-sql-servers/{uuid}/create_database/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/azure-sql-servers/{uuid}/pull/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/azure-sql-servers/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/azure-sql-servers/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/azure-sql-servers/{uuid}/unlink/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/azure-virtualmachines/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/azure-virtualmachines/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/azure-virtualmachines/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/azure-virtualmachines/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/azure-virtualmachines/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/azure-virtualmachines/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/azure-virtualmachines/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/azure-virtualmachines/{uuid}/pull/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/azure-virtualmachines/{uuid}/restart/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/azure-virtualmachines/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/azure-virtualmachines/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/azure-virtualmachines/{uuid}/start/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/azure-virtualmachines/{uuid}/stop/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/azure-virtualmachines/{uuid}/unlink/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/backend-resource-requests/

- New query param: created_before
- New query param: modified_before
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/backend-resource-requests/

- New query param: created_before
- New query param: modified_before
- Security changed
  - New security requirements: waldurPATAuth

POST /api/backend-resource-requests/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/backend-resource-requests/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/backend-resource-requests/{uuid}/set_done/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/backend-resource-requests/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/backend-resource-requests/{uuid}/start_processing/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/backend-resources/

- New query param: created_before
- New query param: modified_before
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/backend-resources/

- New query param: created_before
- New query param: modified_before
- Security changed
  - New security requirements: waldurPATAuth

POST /api/backend-resources/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/backend-resources/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/backend-resources/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/backend-resources/{uuid}/import_resource/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: project_effective_end_date
            - New property: provider_description
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_description
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: max_renewal_duration
                  - New property: min_renewal_duration
                  - New property: prepaid_duration_step
                  - New property: renewal_duration_step
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_description
            - Modified property: project_end_date_requested_by
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

GET /api/billing-total-cost/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/booking-offerings/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [documentation_url effective_available_limits helpdesk_url]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: documentation_url
              - New property: effective_available_limits
              - New property: helpdesk_url
              - Modified property: components
                - Items changed
                  - Properties changed
                    - New property: max_renewal_duration
                    - New property: min_renewal_duration
                    - New property: prepaid_duration_step
                    - New property: renewal_duration_step
              - Modified property: plans
                - Items changed
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: discount_description
                          - New property: discounted_price
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: lbaas_enabled
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/booking-offerings/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/booking-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [documentation_url effective_available_limits helpdesk_url]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: documentation_url
            - New property: effective_available_limits
            - New property: helpdesk_url
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: max_renewal_duration
                  - New property: min_renewal_duration
                  - New property: prepaid_duration_step
                  - New property: renewal_duration_step
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: discount_description
                        - New property: discounted_price
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: lbaas_enabled
- Security changed
  - New security requirements: waldurPATAuth

POST /api/booking-offerings/{uuid}/google_calendar_sync/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/booking-offerings/{uuid}/share_google_calendar/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/booking-offerings/{uuid}/unshare_google_calendar/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/booking-resources/

- New query param: created_before
- New query param: modified_before
- New query param: resource_attributes
- New query param: slug
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [project_effective_end_date provider_description]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: project_effective_end_date
              - New property: provider_description
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: provider_description
              - Modified property: offering_components
                - Items changed
                  - Properties changed
                    - New property: max_renewal_duration
                    - New property: min_renewal_duration
                    - New property: prepaid_duration_step
                    - New property: renewal_duration_step
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: provider_description
              - Modified property: project_end_date_requested_by
                - Nullable changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/booking-resources/

- New query param: created_before
- New query param: modified_before
- New query param: resource_attributes
- New query param: slug
- Security changed
  - New security requirements: waldurPATAuth

GET /api/booking-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [project_effective_end_date provider_description]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: project_effective_end_date
            - New property: provider_description
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_description
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: max_renewal_duration
                  - New property: min_renewal_duration
                  - New property: prepaid_duration_step
                  - New property: renewal_duration_step
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_description
            - Modified property: project_end_date_requested_by
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

POST /api/booking-resources/{uuid}/accept/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/booking-resources/{uuid}/reject/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/broadcast-message-templates/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/broadcast-message-templates/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/broadcast-message-templates/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/broadcast-message-templates/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/broadcast-message-templates/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/broadcast-message-templates/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/broadcast-message-templates/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/broadcast-messages/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/broadcast-messages/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/broadcast-messages/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/broadcast-messages/recipients/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/broadcast-messages/recipients/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/broadcast-messages/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/broadcast-messages/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/broadcast-messages/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/broadcast-messages/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/broadcast-messages/{uuid}/schedule/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/broadcast-messages/{uuid}/send/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/call-assignment-configurations/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/call-assignment-configurations/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/call-assignment-configurations/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/call-assignment-configurations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/call-assignment-configurations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/call-assignment-configurations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/call-assignment-configurations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/call-managing-organisations/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/call-managing-organisations/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/call-managing-organisations/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/call-managing-organisations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/call-managing-organisations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/call-managing-organisations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/call-managing-organisations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/call-managing-organisations/{uuid}/add_user/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/call-managing-organisations/{uuid}/delete_user/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/call-managing-organisations/{uuid}/list_users/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/call-managing-organisations/{uuid}/stats/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/call-managing-organisations/{uuid}/update_user/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/call-proposal-project-role-mappings/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/call-proposal-project-role-mappings/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/call-proposal-project-role-mappings/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/call-proposal-project-role-mappings/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/call-proposal-project-role-mappings/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/call-proposal-project-role-mappings/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/call-proposal-project-role-mappings/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/call-reviewer-pools/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: invitation_link
              - New required property: overridden_at
              - New required property: overridden_by_name
              - New required property: override_reason
              - Deleted required property: invitation_token
            - Properties changed
              - New property: invitation_link
              - New property: overridden_at
              - New property: overridden_by_name
              - New property: override_reason
              - Deleted property: invitation_token
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/call-reviewer-pools/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/call-reviewer-pools/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: invitation_link
            - New required property: overridden_at
            - New required property: overridden_by_name
            - New required property: override_reason
            - Deleted required property: invitation_token
          - Properties changed
            - New property: invitation_link
            - New property: overridden_at
            - New property: overridden_by_name
            - New property: override_reason
            - Deleted property: invitation_token
- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/call-reviewer-pools/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/call-reviewer-pools/{uuid}/accept/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/call-reviewer-pools/{uuid}/decline/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/call-rounds/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/call-rounds/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/call-rounds/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/call-rounds/{uuid}/reviewers/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/celery-stats/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/chat-messages/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: content_display
              - New required property: input_tokens
              - New required property: output_tokens
              - New required property: tool_calls
              - Deleted required property: content
            - Properties changed
              - New property: content_display
              - New property: input_tokens
              - New property: output_tokens
              - New property: tool_calls
              - Modified property: replaces
                - Nullable changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

POST /api/chat-quota/set_quota/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/chat-quota/usage/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/chat-sessions/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/chat-sessions/current/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/chat-sessions/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/chat-threads/

- New query param: input_tokens_max
- New query param: input_tokens_min
- New query param: output_tokens_max
- New query param: output_tokens_min
- New query param: total_tokens_max
- New query param: total_tokens_min
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [input_tokens output_tokens title_gen_input_tokens title_gen_output_tokens total_tokens]
- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-input_tokens -output_tokens -total_tokens input_tokens output_tokens total_tokens]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: input_tokens
              - New property: output_tokens
              - New property: title_gen_input_tokens
              - New property: title_gen_output_tokens
              - New property: total_tokens
- Security changed
  - New security requirements: waldurPATAuth

GET /api/chat-threads/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [input_tokens output_tokens title_gen_input_tokens title_gen_output_tokens total_tokens]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: input_tokens
            - New property: output_tokens
            - New property: title_gen_input_tokens
            - New property: title_gen_output_tokens
            - New property: total_tokens
- Security changed
  - New security requirements: waldurPATAuth

POST /api/chat-threads/{uuid}/archive/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/chat-threads/{uuid}/unarchive/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/chat-tools/execute/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/chat/stream/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/x-ndjson
        - Schema changed
          - Properties changed
            - New property: content
            - New property: error
            - New property: flavor
            - New property: flavors
            - New property: image
            - New property: images
            - New property: message
            - New property: name
            - New property: offerings
            - New property: order_id
            - New property: organization
            - New property: project
            - New property: project_uuid
            - New property: projects
            - New property: status
            - Modified property: k
              - Description changed from 'Component Alias (e.g. 'markdown', 'code', 'table').' to 'Component key (e.g. 'markdown', 'code', 'table', 'vm_order').'
            - Modified property: m
              - Description changed from 'System metadata.' to 'System metadata (thread_uuid, message UUIDs).'
- Security changed
  - New security requirements: waldurPATAuth

GET /api/checklists-admin-question-dependencies/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/checklists-admin-question-dependencies/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/checklists-admin-question-dependencies/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/checklists-admin-question-dependencies/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/checklists-admin-question-dependencies/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/checklists-admin-question-dependencies/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/checklists-admin-question-dependencies/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/checklists-admin-question-options/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/checklists-admin-question-options/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/checklists-admin-question-options/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/checklists-admin-question-options/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/checklists-admin-question-options/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/checklists-admin-question-options/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/checklists-admin-question-options/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/checklists-admin-questions/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/checklists-admin-questions/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/checklists-admin-questions/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/checklists-admin-questions/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/checklists-admin-questions/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/checklists-admin-questions/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/checklists-admin-questions/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/checklists-admin/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/checklists-admin/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/checklists-admin/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/checklists-admin/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/checklists-admin/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/checklists-admin/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/checklists-admin/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/checklists-admin/{uuid}/questions/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/coi-detection-jobs/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/coi-detection-jobs/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/coi-detection-jobs/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/coi-disclosures/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/coi-disclosures/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/coi-disclosures/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/coi-disclosures/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/component-user-usage-limits/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/component-user-usage-limits/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/component-user-usage-limits/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/component-user-usage-limits/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/component-user-usage-limits/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/component-user-usage-limits/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/component-user-usage-limits/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/configuration/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/conflicts-of-interest/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/conflicts-of-interest/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/conflicts-of-interest/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/conflicts-of-interest/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/conflicts-of-interest/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/conflicts-of-interest/{uuid}/dismiss/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/conflicts-of-interest/{uuid}/recuse/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/conflicts-of-interest/{uuid}/waive/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/customer-credits/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/customer-credits/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/customer-credits/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/customer-credits/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/customer-credits/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/customer-credits/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/customer-credits/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/customer-credits/{uuid}/apply_compensations/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/customer-credits/{uuid}/clear_compensations/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/customer-credits/{uuid}/consumptions/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/customer-permissions-reviews/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/customer-permissions-reviews/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/customer-permissions-reviews/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/customer-permissions-reviews/{uuid}/close/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/customer-quotas/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/customer-quotas/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/customers/

- New query param: slug
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [apartment_nr city house_nr household parish state street]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: apartment_nr
              - New property: city
              - New property: house_nr
              - New property: household
              - New property: parish
              - New property: state
              - New property: street
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/customers/

- New query param: slug
- Security changed
  - New security requirements: waldurPATAuth

POST /api/customers/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: apartment_nr
          - New property: city
          - New property: house_nr
          - New property: household
          - New property: parish
          - New property: state
          - New property: street
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: apartment_nr
          - New property: city
          - New property: house_nr
          - New property: household
          - New property: parish
          - New property: state
          - New property: street
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: apartment_nr
          - New property: city
          - New property: house_nr
          - New property: household
          - New property: parish
          - New property: state
          - New property: street
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: apartment_nr
            - New property: city
            - New property: house_nr
            - New property: household
            - New property: parish
            - New property: state
            - New property: street
- Security changed
  - New security requirements: waldurPATAuth

GET /api/customers/countries/

- New query param: slug
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/customers/countries/

- New query param: slug
- Security changed
  - New security requirements: waldurPATAuth

GET /api/customers/{customer_uuid}/project-metadata-compliance-details/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/customers/{customer_uuid}/project-metadata-compliance-overview/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/customers/{customer_uuid}/project-metadata-compliance-projects/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/customers/{customer_uuid}/project-metadata-question-answers/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/customers/{customer_uuid}/users/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/customers/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/customers/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [apartment_nr city house_nr household parish state street]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: apartment_nr
            - New property: city
            - New property: house_nr
            - New property: household
            - New property: parish
            - New property: state
            - New property: street
- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/customers/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: apartment_nr
          - New property: city
          - New property: house_nr
          - New property: household
          - New property: parish
          - New property: state
          - New property: street
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: apartment_nr
          - New property: city
          - New property: house_nr
          - New property: household
          - New property: parish
          - New property: state
          - New property: street
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: apartment_nr
          - New property: city
          - New property: house_nr
          - New property: household
          - New property: parish
          - New property: state
          - New property: street
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: apartment_nr
            - New property: city
            - New property: house_nr
            - New property: household
            - New property: parish
            - New property: state
            - New property: street
- Security changed
  - New security requirements: waldurPATAuth

PUT /api/customers/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: apartment_nr
          - New property: city
          - New property: house_nr
          - New property: household
          - New property: parish
          - New property: state
          - New property: street
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: apartment_nr
          - New property: city
          - New property: house_nr
          - New property: household
          - New property: parish
          - New property: state
          - New property: street
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: apartment_nr
          - New property: city
          - New property: house_nr
          - New property: household
          - New property: parish
          - New property: state
          - New property: street
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: apartment_nr
            - New property: city
            - New property: house_nr
            - New property: household
            - New property: parish
            - New property: state
            - New property: street
- Security changed
  - New security requirements: waldurPATAuth

POST /api/customers/{uuid}/add_user/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/customers/{uuid}/contact/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/customers/{uuid}/delete_user/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/customers/{uuid}/history/

- New query param: slug
- Security changed
  - New security requirements: waldurPATAuth

GET /api/customers/{uuid}/history/at/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/customers/{uuid}/list_users/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/customers/{uuid}/project-digest-config/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/customers/{uuid}/project-digest-config/preview/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/customers/{uuid}/project-digest-config/send-test/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/customers/{uuid}/stats/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/customers/{uuid}/update-project-digest-config/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/customers/{uuid}/update-project-digest-config/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/customers/{uuid}/update_organization_groups/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/customers/{uuid}/update_user/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/daily-quotas/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/data-access-logs/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/data-access-logs/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/data-access-logs/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/data-access-logs/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/database-stats/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/debug/pubsub/circuit_breaker/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/debug/pubsub/circuit_breaker_reset/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/debug/pubsub/dead_letter_queue/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/debug/pubsub/message_state_cache/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/debug/pubsub/metrics/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/debug/pubsub/metrics_reset/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/debug/pubsub/overview/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/debug/pubsub/queues/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/digitalocean-droplets/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/digitalocean-droplets/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/digitalocean-droplets/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/digitalocean-droplets/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/digitalocean-droplets/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/digitalocean-droplets/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/digitalocean-droplets/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/digitalocean-droplets/{uuid}/pull/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/digitalocean-droplets/{uuid}/resize/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/digitalocean-droplets/{uuid}/restart/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/digitalocean-droplets/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/digitalocean-droplets/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/digitalocean-droplets/{uuid}/start/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/digitalocean-droplets/{uuid}/stop/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/digitalocean-droplets/{uuid}/unlink/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/digitalocean-images/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/digitalocean-images/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/digitalocean-images/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/digitalocean-regions/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/digitalocean-regions/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/digitalocean-regions/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/digitalocean-sizes/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/digitalocean-sizes/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/digitalocean-sizes/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/email-logs/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/email-logs/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/email-logs/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/event-subscription-queues/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/event-subscription-queues/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/event-subscription-queues/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/event-subscription-queues/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/event-subscriptions/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/event-subscriptions/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/event-subscriptions/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/event-subscriptions/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/event-subscriptions/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/event-subscriptions/{uuid}/create_queue/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/events-stats/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/events-stats/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/events/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/events/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/events/count/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/events/count/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/events/event_groups/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/events/event_groups/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/events/scope_types/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/events/scope_types/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/events/{id}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/expertise-categories/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/expertise-categories/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/expertise-categories/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/external-links/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/external-links/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/external-links/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/external-links/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/external-links/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/external-links/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/external-links/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/feature-values/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/financial-reports/

- New query param: slug
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/financial-reports/

- New query param: slug
- Security changed
  - New security requirements: waldurPATAuth

GET /api/financial-reports/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/freeipa-profiles/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/freeipa-profiles/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/freeipa-profiles/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/freeipa-profiles/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/freeipa-profiles/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/freeipa-profiles/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/freeipa-profiles/{uuid}/update_ssh_keys/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/google-auth/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/google-auth/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/google-auth/callback/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/google-auth/callback/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/google-auth/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/google-auth/{uuid}/authorize/

- Security changed
  - New security requirements: waldurPATAuth

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
                  - New enum values: [create_of_project_credit_by_staff project_end_date_change_request_approved project_end_date_change_request_created project_end_date_change_request_rejected request_slurm_resource_downscaling request_slurm_resource_pausing reset_downscaling reset_member_restriction reset_pausing update_of_project_credit_by_staff pat_created pat_revoked pat_rotated pat_expired pat_used_from_new_ip]
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/hooks-email/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/hooks-email/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [create_of_project_credit_by_staff project_end_date_change_request_approved project_end_date_change_request_created project_end_date_change_request_rejected request_slurm_resource_downscaling request_slurm_resource_pausing reset_downscaling reset_member_restriction reset_pausing update_of_project_credit_by_staff pat_created pat_revoked pat_rotated pat_expired pat_used_from_new_ip]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [create_of_project_credit_by_staff project_end_date_change_request_approved project_end_date_change_request_created project_end_date_change_request_rejected request_slurm_resource_downscaling request_slurm_resource_pausing reset_downscaling reset_member_restriction reset_pausing update_of_project_credit_by_staff pat_created pat_revoked pat_rotated pat_expired pat_used_from_new_ip]
- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/hooks-email/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/hooks-email/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [create_of_project_credit_by_staff project_end_date_change_request_approved project_end_date_change_request_created project_end_date_change_request_rejected request_slurm_resource_downscaling request_slurm_resource_pausing reset_downscaling reset_member_restriction reset_pausing update_of_project_credit_by_staff pat_created pat_revoked pat_rotated pat_expired pat_used_from_new_ip]
- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [create_of_project_credit_by_staff project_end_date_change_request_approved project_end_date_change_request_created project_end_date_change_request_rejected request_slurm_resource_downscaling request_slurm_resource_pausing reset_downscaling reset_member_restriction reset_pausing update_of_project_credit_by_staff pat_created pat_revoked pat_rotated pat_expired pat_used_from_new_ip]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [create_of_project_credit_by_staff project_end_date_change_request_approved project_end_date_change_request_created project_end_date_change_request_rejected request_slurm_resource_downscaling request_slurm_resource_pausing reset_downscaling reset_member_restriction reset_pausing update_of_project_credit_by_staff pat_created pat_revoked pat_rotated pat_expired pat_used_from_new_ip]
- Security changed
  - New security requirements: waldurPATAuth

PUT /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [create_of_project_credit_by_staff project_end_date_change_request_approved project_end_date_change_request_created project_end_date_change_request_rejected request_slurm_resource_downscaling request_slurm_resource_pausing reset_downscaling reset_member_restriction reset_pausing update_of_project_credit_by_staff pat_created pat_revoked pat_rotated pat_expired pat_used_from_new_ip]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [create_of_project_credit_by_staff project_end_date_change_request_approved project_end_date_change_request_created project_end_date_change_request_rejected request_slurm_resource_downscaling request_slurm_resource_pausing reset_downscaling reset_member_restriction reset_pausing update_of_project_credit_by_staff pat_created pat_revoked pat_rotated pat_expired pat_used_from_new_ip]
- Security changed
  - New security requirements: waldurPATAuth

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
                  - New enum values: [create_of_project_credit_by_staff project_end_date_change_request_approved project_end_date_change_request_created project_end_date_change_request_rejected request_slurm_resource_downscaling request_slurm_resource_pausing reset_downscaling reset_member_restriction reset_pausing update_of_project_credit_by_staff pat_created pat_revoked pat_rotated pat_expired pat_used_from_new_ip]
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/hooks-web/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/hooks-web/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [create_of_project_credit_by_staff project_end_date_change_request_approved project_end_date_change_request_created project_end_date_change_request_rejected request_slurm_resource_downscaling request_slurm_resource_pausing reset_downscaling reset_member_restriction reset_pausing update_of_project_credit_by_staff pat_created pat_revoked pat_rotated pat_expired pat_used_from_new_ip]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [create_of_project_credit_by_staff project_end_date_change_request_approved project_end_date_change_request_created project_end_date_change_request_rejected request_slurm_resource_downscaling request_slurm_resource_pausing reset_downscaling reset_member_restriction reset_pausing update_of_project_credit_by_staff pat_created pat_revoked pat_rotated pat_expired pat_used_from_new_ip]
- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/hooks-web/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/hooks-web/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [create_of_project_credit_by_staff project_end_date_change_request_approved project_end_date_change_request_created project_end_date_change_request_rejected request_slurm_resource_downscaling request_slurm_resource_pausing reset_downscaling reset_member_restriction reset_pausing update_of_project_credit_by_staff pat_created pat_revoked pat_rotated pat_expired pat_used_from_new_ip]
- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [create_of_project_credit_by_staff project_end_date_change_request_approved project_end_date_change_request_created project_end_date_change_request_rejected request_slurm_resource_downscaling request_slurm_resource_pausing reset_downscaling reset_member_restriction reset_pausing update_of_project_credit_by_staff pat_created pat_revoked pat_rotated pat_expired pat_used_from_new_ip]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [create_of_project_credit_by_staff project_end_date_change_request_approved project_end_date_change_request_created project_end_date_change_request_rejected request_slurm_resource_downscaling request_slurm_resource_pausing reset_downscaling reset_member_restriction reset_pausing update_of_project_credit_by_staff pat_created pat_revoked pat_rotated pat_expired pat_used_from_new_ip]
- Security changed
  - New security requirements: waldurPATAuth

PUT /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [create_of_project_credit_by_staff project_end_date_change_request_approved project_end_date_change_request_created project_end_date_change_request_rejected request_slurm_resource_downscaling request_slurm_resource_pausing reset_downscaling reset_member_restriction reset_pausing update_of_project_credit_by_staff pat_created pat_revoked pat_rotated pat_expired pat_used_from_new_ip]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [create_of_project_credit_by_staff project_end_date_change_request_approved project_end_date_change_request_created project_end_date_change_request_rejected request_slurm_resource_downscaling request_slurm_resource_pausing reset_downscaling reset_member_restriction reset_pausing update_of_project_credit_by_staff pat_created pat_revoked pat_rotated pat_expired pat_used_from_new_ip]
- Security changed
  - New security requirements: waldurPATAuth

GET /api/hooks/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/hooks/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/identity-bridge/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/identity-bridge/remove/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/identity-bridge/stats/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/identity-providers/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/identity-providers/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/identity-providers/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/identity-providers/discover_metadata/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/identity-providers/generate-mapping/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/identity-providers/{provider}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/identity-providers/{provider}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/identity-providers/{provider}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/identity-providers/{provider}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/invoice-items/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/invoice-items/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/invoice-items/costs/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/invoice-items/costs/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/invoice-items/customer_costs_for_period/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/invoice-items/customer_costs_for_period/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/invoice-items/project_costs_for_period/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/invoice-items/project_costs_for_period/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/invoice-items/total_price/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/invoice-items/total_price/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/invoice-items/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/invoice-items/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/invoice-items/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/invoice-items/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/invoice-items/{uuid}/consumptions/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/invoice-items/{uuid}/create_compensation/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/invoice-items/{uuid}/migrate_to/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/invoice/send-financial-report-by-mail/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/invoices/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/invoices/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/invoices/growth/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/invoices/growth/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/invoices/import_usage/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/invoices/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/invoices/{uuid}/history/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/invoices/{uuid}/history/at/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/invoices/{uuid}/items/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/invoices/{uuid}/paid/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/invoices/{uuid}/send_notification/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/invoices/{uuid}/set_backend_id/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/invoices/{uuid}/set_payment_url/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/invoices/{uuid}/set_reference_number/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/invoices/{uuid}/stats/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/keycloak-groups/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/keycloak-groups/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/keycloak-groups/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/keycloak-user-group-memberships/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/keycloak-user-group-memberships/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/keycloak-user-group-memberships/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/keycloak-user-group-memberships/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/keycloak-user-group-memberships/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/keycloak-user-group-memberships/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/keycloak-user-group-memberships/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/keys/

- New query param: created_before
- New query param: modified_before
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/keys/

- New query param: created_before
- New query param: modified_before
- Security changed
  - New security requirements: waldurPATAuth

POST /api/keys/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/keys/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/keys/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/keys/{uuid}/history/

- New query param: modified_before
- Security changed
  - New security requirements: waldurPATAuth

GET /api/keys/{uuid}/history/at/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/lexis-links/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/lexis-links/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/lexis-links/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/lexis-links/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/lexis-links/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/lexis-links/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/lexis-links/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/maintenance-announcement-offerings/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/maintenance-announcement-offerings/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/maintenance-announcement-offerings/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/maintenance-announcement-offerings/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/maintenance-announcement-offerings/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/maintenance-announcement-offerings/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/maintenance-announcement-offerings/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/maintenance-announcement-template-offerings/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/maintenance-announcement-template-offerings/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/maintenance-announcement-template-offerings/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/maintenance-announcement-template-offerings/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/maintenance-announcement-template-offerings/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/maintenance-announcement-template-offerings/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/maintenance-announcement-template-offerings/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/maintenance-announcements-template/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/maintenance-announcements-template/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/maintenance-announcements-template/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/maintenance-announcements-template/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/maintenance-announcements-template/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/maintenance-announcements-template/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/maintenance-announcements-template/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/maintenance-announcements/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/maintenance-announcements/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/maintenance-announcements/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/maintenance-announcements/maintenance_stats/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/maintenance-announcements/maintenance_stats/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/maintenance-announcements/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/maintenance-announcements/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/maintenance-announcements/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/maintenance-announcements/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/maintenance-announcements/{uuid}/cancel_maintenance/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/maintenance-announcements/{uuid}/complete_maintenance/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/maintenance-announcements/{uuid}/schedule/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/maintenance-announcements/{uuid}/start_maintenance/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/maintenance-announcements/{uuid}/unschedule/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/managed-rancher-cluster-resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [project_effective_end_date provider_description]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: project_effective_end_date
              - New property: provider_description
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: provider_description
              - Modified property: offering_components
                - Items changed
                  - Properties changed
                    - New property: max_renewal_duration
                    - New property: min_renewal_duration
                    - New property: prepaid_duration_step
                    - New property: renewal_duration_step
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: provider_description
              - Modified property: project_end_date_requested_by
                - Nullable changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/managed-rancher-cluster-resources/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/managed-rancher-cluster-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [project_effective_end_date provider_description]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: project_effective_end_date
            - New property: provider_description
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_description
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: max_renewal_duration
                  - New property: min_renewal_duration
                  - New property: prepaid_duration_step
                  - New property: renewal_duration_step
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_description
            - Modified property: project_end_date_requested_by
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

POST /api/managed-rancher-cluster-resources/{uuid}/add_node/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-bookings/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-categories/

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
                          - New property: uuid
                          - Modified property: options
                            - Items changed
                              - Properties changed
                                - New property: is_default
                                - New property: uuid
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-categories/

- Security changed
  - New security requirements: waldurPATAuth

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
                        - New property: uuid
                        - Modified property: options
                          - Items changed
                            - Properties changed
                              - New property: is_default
                              - New property: uuid
- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-categories/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

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
                        - New property: uuid
                        - Modified property: options
                          - Items changed
                            - Properties changed
                              - New property: is_default
                              - New property: uuid
- Security changed
  - New security requirements: waldurPATAuth

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
                        - New property: uuid
                        - Modified property: options
                          - Items changed
                            - Properties changed
                              - New property: is_default
                              - New property: uuid
- Security changed
  - New security requirements: waldurPATAuth

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
                        - New property: uuid
                        - Modified property: options
                          - Items changed
                            - Properties changed
                              - New property: is_default
                              - New property: uuid
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-category-columns/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-category-columns/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-category-columns/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-category-columns/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-category-columns/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/marketplace-category-columns/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/marketplace-category-columns/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-category-component-usages/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-category-component-usages/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-category-component-usages/{id}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-category-components/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-category-components/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-category-components/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-category-components/{id}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-category-components/{id}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/marketplace-category-components/{id}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/marketplace-category-components/{id}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-category-groups/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-category-groups/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-category-groups/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-category-groups/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-category-groups/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/marketplace-category-groups/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/marketplace-category-groups/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-category-help-articles/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-category-help-articles/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-category-help-articles/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-category-help-articles/{id}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-category-help-articles/{id}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/marketplace-category-help-articles/{id}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/marketplace-category-help-articles/{id}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-component-usages/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-component-usages/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-component-usages/set_usage/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-component-usages/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-component-usages/{uuid}/set_user_usage/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-component-usages/{uuid}/set_user_usages/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-component-user-usages/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-component-user-usages/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-component-user-usages/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-course-accounts/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-course-accounts/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-course-accounts/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-course-accounts/create_bulk/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-course-accounts/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-course-accounts/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-customer-component-usage-policies/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: affected_resources_count
            - Properties changed
              - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-customer-component-usage-policies/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-customer-component-usage-policies/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: affected_resources_count
          - Properties changed
            - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-customer-component-usage-policies/actions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: affected_resources_count
          - Properties changed
            - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-customer-component-usage-policies/actions/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-customer-component-usage-policies/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-customer-component-usage-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: affected_resources_count
          - Properties changed
            - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/marketplace-customer-component-usage-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: affected_resources_count
          - Properties changed
            - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

PUT /api/marketplace-customer-component-usage-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: affected_resources_count
          - Properties changed
            - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-customer-estimated-cost-policies/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: affected_resources_count
            - Properties changed
              - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-customer-estimated-cost-policies/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-customer-estimated-cost-policies/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: affected_resources_count
          - Properties changed
            - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-customer-estimated-cost-policies/actions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: affected_resources_count
          - Properties changed
            - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-customer-estimated-cost-policies/actions/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-customer-estimated-cost-policies/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-customer-estimated-cost-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: affected_resources_count
          - Properties changed
            - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/marketplace-customer-estimated-cost-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: affected_resources_count
          - Properties changed
            - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

PUT /api/marketplace-customer-estimated-cost-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: affected_resources_count
          - Properties changed
            - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-customer-service-accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: customer
                - Nullable changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-customer-service-accounts/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-customer-service-accounts/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: customer
            - Nullable changed from false to true
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: customer
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-customer-service-accounts/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-customer-service-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: customer
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/marketplace-customer-service-accounts/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: customer
            - Nullable changed from false to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: customer
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

PUT /api/marketplace-customer-service-accounts/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: customer
            - Nullable changed from false to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: customer
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-customer-service-accounts/{uuid}/rotate_api_key/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: customer
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-demo-presets/info/{name}/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-demo-presets/info/{name}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-demo-presets/list/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-demo-presets/list/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-demo-presets/load/{name}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-global-categories/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-integration-statuses/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-integration-statuses/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-integration-statuses/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-offering-estimated-cost-policies/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: affected_resources_count
            - Properties changed
              - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-offering-estimated-cost-policies/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-offering-estimated-cost-policies/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: affected_resources_count
          - Properties changed
            - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-offering-estimated-cost-policies/actions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: affected_resources_count
          - Properties changed
            - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-offering-estimated-cost-policies/actions/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-offering-estimated-cost-policies/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-offering-estimated-cost-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: affected_resources_count
          - Properties changed
            - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/marketplace-offering-estimated-cost-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: affected_resources_count
          - Properties changed
            - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

PUT /api/marketplace-offering-estimated-cost-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: affected_resources_count
          - Properties changed
            - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-offering-files/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-offering-files/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-offering-files/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-offering-files/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-offering-files/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-offering-permissions-log/

- New query param: created_before
- New query param: modified_before
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-offering-permissions-log/

- New query param: created_before
- New query param: modified_before
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-offering-permissions-log/{id}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-offering-permissions/

- New query param: created_before
- New query param: modified_before
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-offering-permissions/

- New query param: created_before
- New query param: modified_before
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-offering-permissions/{id}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-offering-referrals/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-offering-referrals/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-offering-referrals/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-offering-terms-of-service/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-offering-terms-of-service/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-offering-terms-of-service/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-offering-terms-of-service/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-offering-terms-of-service/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/marketplace-offering-terms-of-service/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/marketplace-offering-terms-of-service/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-offering-usage-policies/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: affected_resources_count
            - Properties changed
              - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-offering-usage-policies/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-offering-usage-policies/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: affected_resources_count
          - Properties changed
            - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-offering-usage-policies/actions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: affected_resources_count
          - Properties changed
            - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-offering-usage-policies/actions/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-offering-usage-policies/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-offering-usage-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: affected_resources_count
          - Properties changed
            - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/marketplace-offering-usage-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: affected_resources_count
          - Properties changed
            - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

PUT /api/marketplace-offering-usage-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: affected_resources_count
          - Properties changed
            - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-offering-user-checklist-completions/

- New query param: created_before
- New query param: modified_before
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
                      - Modified property: user_gender
                        - Property 'OneOf' changed
                          - Schemas added: #/components/schemas/BlankEnum
                          - Modified schema: #/components/schemas/GenderEnum
                            - Type changed from 'integer' to 'string'
                            - New enum values: [male female unknown]
                            - Deleted enum values: [0 1 2 9]
                        - Description changed from 'ISO 5218 gender code' to 'User's gender (male, female, or unknown)'
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-offering-user-checklist-completions/

- New query param: created_before
- New query param: modified_before
- Security changed
  - New security requirements: waldurPATAuth

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
                    - Modified property: user_gender
                      - Property 'OneOf' changed
                        - Schemas added: #/components/schemas/BlankEnum
                        - Modified schema: #/components/schemas/GenderEnum
                          - Type changed from 'integer' to 'string'
                          - New enum values: [male female unknown]
                          - Deleted enum values: [0 1 2 9]
                      - Description changed from 'ISO 5218 gender code' to 'User's gender (male, female, or unknown)'
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-offering-user-roles/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-offering-user-roles/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-offering-user-roles/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-offering-user-roles/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-offering-user-roles/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/marketplace-offering-user-roles/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/marketplace-offering-user-roles/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-offering-users/

- New query param: created_before
- New query param: modified_before
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: user_gender
                - Property 'OneOf' changed
                  - Schemas added: #/components/schemas/BlankEnum
                  - Modified schema: #/components/schemas/GenderEnum
                    - Type changed from 'integer' to 'string'
                    - New enum values: [male female unknown]
                    - Deleted enum values: [0 1 2 9]
                - Description changed from 'ISO 5218 gender code' to 'User's gender (male, female, or unknown)'
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-offering-users/

- New query param: created_before
- New query param: modified_before
- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-offering-users/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: user_gender
              - Property 'OneOf' changed
                - Schemas added: #/components/schemas/BlankEnum
                - Modified schema: #/components/schemas/GenderEnum
                  - Type changed from 'integer' to 'string'
                  - New enum values: [male female unknown]
                  - Deleted enum values: [0 1 2 9]
              - Description changed from 'ISO 5218 gender code' to 'User's gender (male, female, or unknown)'
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-offering-users/checklist-template/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-offering-users/checklist-template/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-offering-users/profile_field_warnings/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-offering-users/profile_field_warnings/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-offering-users/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-offering-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: user_gender
              - Property 'OneOf' changed
                - Schemas added: #/components/schemas/BlankEnum
                - Modified schema: #/components/schemas/GenderEnum
                  - Type changed from 'integer' to 'string'
                  - New enum values: [male female unknown]
                  - Deleted enum values: [0 1 2 9]
              - Description changed from 'ISO 5218 gender code' to 'User's gender (male, female, or unknown)'
- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/marketplace-offering-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: user_gender
              - Property 'OneOf' changed
                - Schemas added: #/components/schemas/BlankEnum
                - Modified schema: #/components/schemas/GenderEnum
                  - Type changed from 'integer' to 'string'
                  - New enum values: [male female unknown]
                  - Deleted enum values: [0 1 2 9]
              - Description changed from 'ISO 5218 gender code' to 'User's gender (male, female, or unknown)'
- Security changed
  - New security requirements: waldurPATAuth

PUT /api/marketplace-offering-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: user_gender
              - Property 'OneOf' changed
                - Schemas added: #/components/schemas/BlankEnum
                - Modified schema: #/components/schemas/GenderEnum
                  - Type changed from 'integer' to 'string'
                  - New enum values: [male female unknown]
                  - Deleted enum values: [0 1 2 9]
              - Description changed from 'ISO 5218 gender code' to 'User's gender (male, female, or unknown)'
- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-offering-users/{uuid}/begin_creating/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-offering-users/{uuid}/checklist/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-offering-users/{uuid}/checklist_review/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-offering-users/{uuid}/completion_review_status/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-offering-users/{uuid}/completion_status/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-offering-users/{uuid}/request_deletion/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-offering-users/{uuid}/set_deleted/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-offering-users/{uuid}/set_deleting/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-offering-users/{uuid}/set_error_creating/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-offering-users/{uuid}/set_error_deleting/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-offering-users/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-offering-users/{uuid}/set_pending_account_linking/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-offering-users/{uuid}/set_pending_additional_validation/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-offering-users/{uuid}/set_validation_complete/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-offering-users/{uuid}/submit_answers/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/marketplace-offering-users/{uuid}/update_comments/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-offering-users/{uuid}/update_restricted/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-orders/

- New query param: created_before
- New query param: modified_before
- New query param: slug
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [provider_description]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: provider_description
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-orders/

- New query param: created_before
- New query param: modified_before
- New query param: slug
- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-orders/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: attributes
            - Property 'OneOf' changed
              - Modified schema: #/components/schemas/OpenStackInstanceCreateOrderAttributes
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - New property: port_security_enabled
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: provider_description
- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-orders/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-orders/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [provider_description]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: provider_description
- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/marketplace-orders/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/marketplace-orders/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-orders/{uuid}/approve_by_consumer/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-orders/{uuid}/approve_by_provider/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-orders/{uuid}/cancel/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-orders/{uuid}/delete_attachment/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-orders/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: documentation_url
            - New property: effective_available_limits
            - New property: helpdesk_url
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: max_renewal_duration
                  - New property: min_renewal_duration
                  - New property: prepaid_duration_step
                  - New property: renewal_duration_step
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: discount_description
                        - New property: discounted_price
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: lbaas_enabled
- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-orders/{uuid}/reject_by_consumer/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-orders/{uuid}/reject_by_provider/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-orders/{uuid}/set_backend_id/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-orders/{uuid}/set_consumer_info/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-orders/{uuid}/set_provider_info/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-orders/{uuid}/set_state_done/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-orders/{uuid}/set_state_erred/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-orders/{uuid}/set_state_executing/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-orders/{uuid}/unlink/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-orders/{uuid}/update_attachment/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-plan-components/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-plan-components/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-plan-components/{id}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-plans/

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
                    - New property: discount_description
                    - New property: discounted_price
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-plans/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-plans/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: discount_description
                  - New property: discounted_price
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-plans/usage_stats/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-plans/usage_stats/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-plans/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-plans/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: discount_description
                  - New property: discounted_price
- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/marketplace-plans/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: discount_description
                  - New property: discounted_price
- Security changed
  - New security requirements: waldurPATAuth

PUT /api/marketplace-plans/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: discount_description
                  - New property: discounted_price
- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-plans/{uuid}/archive/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-plans/{uuid}/delete_organization_groups/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-plans/{uuid}/history/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-plans/{uuid}/history/at/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-plans/{uuid}/update_discounts/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-plans/{uuid}/update_organization_groups/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-plans/{uuid}/update_prices/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-plans/{uuid}/update_quotas/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-project-estimated-cost-policies/

- New query param: query
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: affected_resources_count
            - Properties changed
              - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-project-estimated-cost-policies/

- New query param: query
- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-project-estimated-cost-policies/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: affected_resources_count
          - Properties changed
            - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-project-estimated-cost-policies/actions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: affected_resources_count
          - Properties changed
            - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-project-estimated-cost-policies/actions/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-project-estimated-cost-policies/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-project-estimated-cost-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: affected_resources_count
          - Properties changed
            - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/marketplace-project-estimated-cost-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: affected_resources_count
          - Properties changed
            - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

PUT /api/marketplace-project-estimated-cost-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: affected_resources_count
          - Properties changed
            - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-project-service-accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: project
                - Nullable changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-project-service-accounts/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-project-service-accounts/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: project
            - Nullable changed from false to true
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: project
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-project-service-accounts/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-project-service-accounts/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: project
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/marketplace-project-service-accounts/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: project
            - Nullable changed from false to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: project
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

PUT /api/marketplace-project-service-accounts/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: project
            - Nullable changed from false to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: project
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-project-service-accounts/{uuid}/rotate_api_key/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: project
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-project-update-requests/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-project-update-requests/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-project-update-requests/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-project-update-requests/{uuid}/approve/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-project-update-requests/{uuid}/reject/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-provider-offerings/

- New query param: created_before
- New query param: modified_before
- New query param: slug
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [documentation_url effective_available_limits helpdesk_url]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: documentation_url
              - New property: effective_available_limits
              - New property: helpdesk_url
              - Modified property: components
                - Items changed
                  - Properties changed
                    - New property: max_renewal_duration
                    - New property: min_renewal_duration
                    - New property: prepaid_duration_step
                    - New property: renewal_duration_step
              - Modified property: plans
                - Items changed
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: discount_description
                          - New property: discounted_price
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: lbaas_enabled
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-provider-offerings/

- New query param: created_before
- New query param: modified_before
- New query param: slug
- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: documentation_url
          - New property: helpdesk_url
          - Modified property: components
            - Items changed
              - Properties changed
                - New property: max_renewal_duration
                - New property: min_renewal_duration
                - New property: prepaid_duration_step
                - New property: renewal_duration_step
          - Modified property: plugin_options
            - Properties changed
              - New property: lbaas_enabled
              - Modified property: required_team_role_for_provisioning
                - MinLength changed from 1 to 0
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: documentation_url
          - New property: helpdesk_url
          - Modified property: components
            - Items changed
              - Properties changed
                - New property: max_renewal_duration
                - New property: min_renewal_duration
                - New property: prepaid_duration_step
                - New property: renewal_duration_step
          - Modified property: plugin_options
            - Properties changed
              - New property: lbaas_enabled
              - Modified property: required_team_role_for_provisioning
                - MinLength changed from 1 to 0
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: documentation_url
          - New property: helpdesk_url
          - Modified property: components
            - Items changed
              - Properties changed
                - New property: max_renewal_duration
                - New property: min_renewal_duration
                - New property: prepaid_duration_step
                - New property: renewal_duration_step
          - Modified property: plugin_options
            - Properties changed
              - New property: lbaas_enabled
              - Modified property: required_team_role_for_provisioning
                - MinLength changed from 1 to 0
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: documentation_url
            - New property: effective_available_limits
            - New property: helpdesk_url
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: max_renewal_duration
                  - New property: min_renewal_duration
                  - New property: prepaid_duration_step
                  - New property: renewal_duration_step
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: discount_description
                        - New property: discounted_price
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: lbaas_enabled
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-provider-offerings/groups/

- New query param: created_before
- New query param: modified_before
- New query param: slug
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-provider-offerings/groups/

- New query param: created_before
- New query param: modified_before
- New query param: slug
- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/import_offering/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-provider-offerings/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-provider-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [documentation_url effective_available_limits helpdesk_url]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: documentation_url
            - New property: effective_available_limits
            - New property: helpdesk_url
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: max_renewal_duration
                  - New property: min_renewal_duration
                  - New property: prepaid_duration_step
                  - New property: renewal_duration_step
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: discount_description
                        - New property: discounted_price
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: lbaas_enabled
- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/activate/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/add_endpoint/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/add_partition/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/add_software_catalog/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/add_user/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/archive/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/check_unique_backend_id/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-provider-offerings/{uuid}/component_stats/

- New query param: created_before
- New query param: modified_before
- New query param: slug
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-provider-offerings/{uuid}/costs/

- New query param: created_before
- New query param: modified_before
- New query param: slug
- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/create_offering_component/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: max_renewal_duration
          - New property: min_renewal_duration
          - New property: prepaid_duration_step
          - New property: renewal_duration_step
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-provider-offerings/{uuid}/customers/

- New query param: created_before
- New query param: modified_before
- New query param: slug
- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-provider-offerings/{uuid}/delete-user-attribute-config/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/delete_endpoint/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/delete_image/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/delete_organization_groups/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/delete_tags/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/delete_thumbnail/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/delete_user/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/draft/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/export_offering/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-provider-offerings/{uuid}/glauth_users_config/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-provider-offerings/{uuid}/history/

- New query param: modified_before
- New query param: slug
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-provider-offerings/{uuid}/history/at/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/import_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: project_effective_end_date
            - New property: provider_description
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_description
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: max_renewal_duration
                  - New property: min_renewal_duration
                  - New property: prepaid_duration_step
                  - New property: renewal_duration_step
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_description
            - Modified property: project_end_date_requested_by
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-provider-offerings/{uuid}/importable_resources/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-provider-offerings/{uuid}/list_course_accounts/

- New query param: created_before
- New query param: modified_before
- New query param: slug
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-provider-offerings/{uuid}/list_customer_projects/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_grace_period_days effective_end_date end_date_updated_at is_in_grace_period]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_grace_period_days
              - New property: effective_end_date
              - New property: end_date_updated_at
              - New property: is_in_grace_period
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-provider-offerings/{uuid}/list_customer_service_accounts/

- New query param: created_before
- New query param: modified_before
- New query param: slug
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: customer
                - Nullable changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-provider-offerings/{uuid}/list_customer_users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [deactivation_reason]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: deactivation_reason
              - Modified property: gender
                - Property 'OneOf' changed
                  - Schemas added: #/components/schemas/BlankEnum
                  - Modified schema: #/components/schemas/GenderEnum
                    - Type changed from 'integer' to 'string'
                    - New enum values: [male female unknown]
                    - Deleted enum values: [0 1 2 9]
                - Description changed from 'ISO 5218 gender code' to 'User's gender (male, female, or unknown)'
                - Min changed from 0 to null
                - Max changed from 32767 to null
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-provider-offerings/{uuid}/list_project_service_accounts/

- New query param: created_before
- New query param: modified_before
- New query param: slug
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: project
                - Nullable changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-provider-offerings/{uuid}/list_users/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/make_available/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/make_unavailable/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/move_offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: documentation_url
            - New property: effective_available_limits
            - New property: helpdesk_url
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: max_renewal_duration
                  - New property: min_renewal_duration
                  - New property: prepaid_duration_step
                  - New property: renewal_duration_step
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: discount_description
                        - New property: discounted_price
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: lbaas_enabled
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-provider-offerings/{uuid}/orders/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [provider_description]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: provider_description
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-provider-offerings/{uuid}/orders/{order_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: provider_description
- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/pause/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/refresh_offering_usernames/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/remove_offering_component/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/remove_partition/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/remove_software_catalog/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/set_backend_metadata/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-provider-offerings/{uuid}/stats/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/sync/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-provider-offerings/{uuid}/tos_stats/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/unpause/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/marketplace-provider-offerings/{uuid}/update-user-attribute-config/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/update-user-attribute-config/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/marketplace-provider-offerings/{uuid}/update-user-attribute-config/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/update_attributes/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/update_backend_id_rules/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/update_compliance_checklist/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/update_description/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/update_image/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/update_integration/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: lbaas_enabled
              - Modified property: required_team_role_for_provisioning
                - MinLength changed from 1 to 0
- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/update_location/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/update_offering_component/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: max_renewal_duration
          - New property: min_renewal_duration
          - New property: prepaid_duration_step
          - New property: renewal_duration_step
- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/update_options/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/update_organization_groups/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/update_overview/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: documentation_url
          - New property: helpdesk_url
- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/marketplace-provider-offerings/{uuid}/update_partition/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/update_resource_options/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/marketplace-provider-offerings/{uuid}/update_software_catalog/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/update_tags/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/update_thumbnail/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-offerings/{uuid}/update_user/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-provider-offerings/{uuid}/user-attribute-config/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-provider-offerings/{uuid}/user_has_resource_access/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [documentation_url effective_available_limits helpdesk_url]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: documentation_url
            - New property: effective_available_limits
            - New property: helpdesk_url
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: max_renewal_duration
                  - New property: min_renewal_duration
                  - New property: prepaid_duration_step
                  - New property: renewal_duration_step
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: discount_description
                        - New property: discounted_price
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: lbaas_enabled
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-provider-resources/

- New query param: created_before
- New query param: modified_before
- New query param: resource_attributes
- New query param: slug
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [project_effective_end_date provider_description]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: project_effective_end_date
              - New property: provider_description
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: provider_description
              - Modified property: offering_components
                - Items changed
                  - Properties changed
                    - New property: max_renewal_duration
                    - New property: min_renewal_duration
                    - New property: prepaid_duration_step
                    - New property: renewal_duration_step
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: provider_description
              - Modified property: project_end_date_requested_by
                - Nullable changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-provider-resources/

- New query param: created_before
- New query param: modified_before
- New query param: resource_attributes
- New query param: slug
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-provider-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [project_effective_end_date provider_description]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: project_effective_end_date
            - New property: provider_description
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_description
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: max_renewal_duration
                  - New property: min_renewal_duration
                  - New property: prepaid_duration_step
                  - New property: renewal_duration_step
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_description
            - Modified property: project_end_date_requested_by
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/marketplace-provider-resources/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/marketplace-provider-resources/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-provider-resources/{uuid}/details/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-provider-resources/{uuid}/glauth_users_config/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-provider-resources/{uuid}/history/

- New query param: modified_before
- New query param: resource_attributes
- New query param: slug
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-provider-resources/{uuid}/history/at/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-resources/{uuid}/move_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: project_effective_end_date
            - New property: provider_description
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_description
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: max_renewal_duration
                  - New property: min_renewal_duration
                  - New property: prepaid_duration_step
                  - New property: renewal_duration_step
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_description
            - Modified property: project_end_date_requested_by
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-provider-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: documentation_url
            - New property: effective_available_limits
            - New property: helpdesk_url
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: max_renewal_duration
                  - New property: min_renewal_duration
                  - New property: prepaid_duration_step
                  - New property: renewal_duration_step
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: discount_description
                        - New property: discounted_price
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: lbaas_enabled
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-provider-resources/{uuid}/offering_for_subresources/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-provider-resources/{uuid}/plan_periods/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-resources/{uuid}/pull/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-resources/{uuid}/refresh_last_sync/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-resources/{uuid}/restore/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: project_effective_end_date
            - New property: provider_description
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_description
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: max_renewal_duration
                  - New property: min_renewal_duration
                  - New property: prepaid_duration_step
                  - New property: renewal_duration_step
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_description
            - Modified property: project_end_date_requested_by
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-resources/{uuid}/set_as_erred/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-resources/{uuid}/set_as_ok/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-resources/{uuid}/set_backend_id/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-resources/{uuid}/set_backend_metadata/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-resources/{uuid}/set_downscaled/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-resources/{uuid}/set_end_date_by_provider/

- Description changed from 'Allows a service provider to set or update the end date for a resource, scheduling it for termination. A notification is sent to the consumer.' to 'Deprecated: Use set_end_date instead. Allows a service provider to set or update the end date for a resource.'
- Deprecated changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-resources/{uuid}/set_end_date_by_staff/

- Description changed from 'Allows a staff user to set or update the end date for a resource, which will schedule it for termination.' to 'Deprecated: Use set_end_date instead. Allows a staff user to set or update the end date for a resource.'
- Deprecated changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-resources/{uuid}/set_keycloak_scopes/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-resources/{uuid}/set_limits/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-resources/{uuid}/set_paused/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-resources/{uuid}/set_restrict_member_access/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-resources/{uuid}/set_slug/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-resources/{uuid}/set_state_ok/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-resources/{uuid}/submit_report/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-provider-resources/{uuid}/team/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-resources/{uuid}/terminate/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-resources/{uuid}/unlink/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-resources/{uuid}/update_options/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-provider-resources/{uuid}/update_options_direct/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-public-api/check_signature/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-public-api/set_usage/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-public-offerings/

- New query param: created_before
- New query param: modified_before
- New query param: slug
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [documentation_url effective_available_limits helpdesk_url]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: documentation_url
              - New property: effective_available_limits
              - New property: helpdesk_url
              - Modified property: components
                - Items changed
                  - Properties changed
                    - New property: max_renewal_duration
                    - New property: min_renewal_duration
                    - New property: prepaid_duration_step
                    - New property: renewal_duration_step
              - Modified property: plans
                - Items changed
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: discount_description
                          - New property: discounted_price
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: lbaas_enabled
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-public-offerings/

- New query param: created_before
- New query param: modified_before
- New query param: slug
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-public-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [documentation_url effective_available_limits helpdesk_url]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: documentation_url
            - New property: effective_available_limits
            - New property: helpdesk_url
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: max_renewal_duration
                  - New property: min_renewal_duration
                  - New property: prepaid_duration_step
                  - New property: renewal_duration_step
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: discount_description
                        - New property: discounted_price
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: lbaas_enabled
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-public-offerings/{uuid}/plans/

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
                    - New property: discount_description
                    - New property: discounted_price
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-public-offerings/{uuid}/plans/{plan_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: discount_description
                  - New property: discounted_price
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-related-customers/{customer_uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-remote-synchronisations/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-remote-synchronisations/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-remote-synchronisations/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-remote-synchronisations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-remote-synchronisations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/marketplace-remote-synchronisations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/marketplace-remote-synchronisations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-remote-synchronisations/{uuid}/run_synchronisation/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-resource-offerings/{category_uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-resource-users/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-resource-users/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-resource-users/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-resource-users/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-resource-users/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-resources/

- New query param: created_before
- New query param: modified_before
- New query param: resource_attributes
- New query param: slug
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [project_effective_end_date provider_description]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: project_effective_end_date
              - New property: provider_description
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: provider_description
              - Modified property: offering_components
                - Items changed
                  - Properties changed
                    - New property: max_renewal_duration
                    - New property: min_renewal_duration
                    - New property: prepaid_duration_step
                    - New property: renewal_duration_step
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: provider_description
              - Modified property: project_end_date_requested_by
                - Nullable changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-resources/

- New query param: created_before
- New query param: modified_before
- New query param: resource_attributes
- New query param: slug
- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-resources/suggest_name/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [project_effective_end_date provider_description]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: project_effective_end_date
            - New property: provider_description
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_description
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: max_renewal_duration
                  - New property: min_renewal_duration
                  - New property: prepaid_duration_step
                  - New property: renewal_duration_step
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_description
            - Modified property: project_end_date_requested_by
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/marketplace-resources/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/marketplace-resources/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-resources/{uuid}/details/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-resources/{uuid}/estimate_renewal/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: extension_months
            - Max changed from 60 to 600
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-resources/{uuid}/glauth_users_config/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-resources/{uuid}/history/

- New query param: modified_before
- New query param: resource_attributes
- New query param: slug
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-resources/{uuid}/history/at/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-resources/{uuid}/move_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: project_effective_end_date
            - New property: provider_description
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_description
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: max_renewal_duration
                  - New property: min_renewal_duration
                  - New property: prepaid_duration_step
                  - New property: renewal_duration_step
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_description
            - Modified property: project_end_date_requested_by
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-resources/{uuid}/offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: documentation_url
            - New property: effective_available_limits
            - New property: helpdesk_url
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: max_renewal_duration
                  - New property: min_renewal_duration
                  - New property: prepaid_duration_step
                  - New property: renewal_duration_step
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: discount_description
                        - New property: discounted_price
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: lbaas_enabled
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-resources/{uuid}/offering_for_subresources/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-resources/{uuid}/plan_periods/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-resources/{uuid}/pull/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-resources/{uuid}/reallocate_limits/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-resources/{uuid}/renew/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: extension_months
            - Min changed from 12 to 1
            - Max changed from 60 to 600
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: extension_months
            - Min changed from 12 to 1
            - Max changed from 60 to 600
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: extension_months
            - Min changed from 12 to 1
            - Max changed from 60 to 600
- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-resources/{uuid}/restore/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: project_effective_end_date
            - New property: provider_description
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_description
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: max_renewal_duration
                  - New property: min_renewal_duration
                  - New property: prepaid_duration_step
                  - New property: renewal_duration_step
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: provider_description
            - Modified property: project_end_date_requested_by
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-resources/{uuid}/set_downscaled/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-resources/{uuid}/set_end_date_by_staff/

- Description changed from 'Allows a staff user to set or update the end date for a resource, which will schedule it for termination.' to 'Deprecated: Use set_end_date instead. Allows a staff user to set or update the end date for a resource.'
- Deprecated changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-resources/{uuid}/set_paused/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-resources/{uuid}/set_restrict_member_access/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-resources/{uuid}/set_slug/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-resources/{uuid}/switch_plan/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-resources/{uuid}/team/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-resources/{uuid}/terminate/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-resources/{uuid}/unlink/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-resources/{uuid}/update_limits/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-resources/{uuid}/update_options/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-robot-accounts/

- New query param: created_before
- New query param: modified_before
- New query param: responsible_user_uuid
- New query param: user_email
- New query param: username
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
                      - New property: lbaas_enabled
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-robot-accounts/

- New query param: created_before
- New query param: modified_before
- New query param: responsible_user_uuid
- New query param: user_email
- New query param: username
- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-robot-accounts/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-robot-accounts/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

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
                    - New property: lbaas_enabled
- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/marketplace-robot-accounts/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/marketplace-robot-accounts/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

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
                    - New property: lbaas_enabled
- Security changed
  - New security requirements: waldurPATAuth

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
                    - New property: lbaas_enabled
- Security changed
  - New security requirements: waldurPATAuth

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
                    - New property: lbaas_enabled
- Security changed
  - New security requirements: waldurPATAuth

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
                    - New property: lbaas_enabled
- Security changed
  - New security requirements: waldurPATAuth

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
                    - New property: lbaas_enabled
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-runtime-states/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-screenshots/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-screenshots/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-screenshots/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-screenshots/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-screenshots/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/marketplace-screenshots/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/marketplace-screenshots/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-script-async-dry-run/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-script-async-dry-run/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-script-async-dry-run/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-script-dry-run/{uuid}/async_run/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: documentation_url
            - New property: effective_available_limits
            - New property: helpdesk_url
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: max_renewal_duration
                  - New property: min_renewal_duration
                  - New property: prepaid_duration_step
                  - New property: renewal_duration_step
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: discount_description
                        - New property: discounted_price
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: lbaas_enabled
- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-script-dry-run/{uuid}/run/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: documentation_url
            - New property: effective_available_limits
            - New property: helpdesk_url
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: max_renewal_duration
                  - New property: min_renewal_duration
                  - New property: prepaid_duration_step
                  - New property: renewal_duration_step
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: discount_description
                        - New property: discounted_price
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: lbaas_enabled
- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-script-sync-resource/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-sections/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-sections/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-sections/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-sections/{key}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-sections/{key}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/marketplace-sections/{key}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/marketplace-sections/{key}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-service-providers/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-service-providers/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-service-providers/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-service-providers/{service_provider_uuid}/compliance/checklists_summary/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-service-providers/{service_provider_uuid}/compliance/compliance_overview/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-service-providers/{service_provider_uuid}/compliance/offering_users/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-service-providers/{service_provider_uuid}/course_accounts/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-service-providers/{service_provider_uuid}/customer_projects/

- New query param: created_before
- New query param: modified_before
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-service-providers/{service_provider_uuid}/customers/

- New query param: slug
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-service-providers/{service_provider_uuid}/keys/

- New query param: created_before
- New query param: modified_before
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-service-providers/{service_provider_uuid}/offerings/

- New query param: created_before
- New query param: modified_before
- New query param: slug
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
                    - New property: max_renewal_duration
                    - New property: min_renewal_duration
                    - New property: prepaid_duration_step
                    - New property: renewal_duration_step
              - Modified property: plans
                - Items changed
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: discount_description
                          - New property: discounted_price
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-service-providers/{service_provider_uuid}/project_permissions/

- New query param: created_before
- New query param: modified_before
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-service-providers/{service_provider_uuid}/project_service_accounts/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: project
                - Nullable changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-service-providers/{service_provider_uuid}/projects/

- New query param: created_before
- New query param: modified_before
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_grace_period_days effective_end_date end_date_updated_at is_in_grace_period]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_grace_period_days
              - New property: effective_end_date
              - New property: end_date_updated_at
              - New property: is_in_grace_period
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-service-providers/{service_provider_uuid}/user_customers/

- New query param: slug
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-service-providers/{service_provider_uuid}/users/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: gender
                - Property 'OneOf' changed
                  - Schemas added: #/components/schemas/BlankEnum
                  - Modified schema: #/components/schemas/GenderEnum
                    - Type changed from 'integer' to 'string'
                    - New enum values: [male female unknown]
                    - Deleted enum values: [0 1 2 9]
                - Description changed from 'ISO 5218 gender code' to 'User's gender (male, female, or unknown)'
                - Min changed from 0 to null
                - Max changed from 32767 to null
- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-service-providers/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-service-providers/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/marketplace-service-providers/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/marketplace-service-providers/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-service-providers/{uuid}/add_user/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-service-providers/{uuid}/api_secret_code/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-service-providers/{uuid}/api_secret_code/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-service-providers/{uuid}/delete_user/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-service-providers/{uuid}/generate_site_agent_config/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-service-providers/{uuid}/list_users/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-service-providers/{uuid}/revenue/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-service-providers/{uuid}/robot_account_customers/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-service-providers/{uuid}/robot_account_projects/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-service-providers/{uuid}/set_offerings_username/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-service-providers/{uuid}/stat/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-service-providers/{uuid}/update_user/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-site-agent-connection-stats/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-site-agent-identities/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: created_by
                - Nullable changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-site-agent-identities/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-site-agent-identities/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: created_by
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-site-agent-identities/cleanup_orphaned/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-site-agent-identities/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-site-agent-identities/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: created_by
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

PUT /api/marketplace-site-agent-identities/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: created_by
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-site-agent-identities/{uuid}/register_event_subscription/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-site-agent-identities/{uuid}/register_service/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-site-agent-processors/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-site-agent-processors/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-site-agent-processors/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-site-agent-processors/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-site-agent-services/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-site-agent-services/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-site-agent-services/cleanup_stale/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-site-agent-services/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-site-agent-services/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-site-agent-services/{uuid}/register_processor/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-site-agent-services/{uuid}/set_statistics/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-site-agent-stats/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-site-agent-task-stats/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-slurm-periodic-usage-policies/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: affected_resources_count
            - Properties changed
              - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-slurm-periodic-usage-policies/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-slurm-periodic-usage-policies/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: affected_resources_count
          - Properties changed
            - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-slurm-periodic-usage-policies/actions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: affected_resources_count
          - Properties changed
            - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-slurm-periodic-usage-policies/actions/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-slurm-periodic-usage-policies/preview_impact/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-slurm-periodic-usage-policies/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-slurm-periodic-usage-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: affected_resources_count
          - Properties changed
            - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/marketplace-slurm-periodic-usage-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: affected_resources_count
          - Properties changed
            - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

PUT /api/marketplace-slurm-periodic-usage-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: affected_resources_count
          - Properties changed
            - New property: affected_resources_count
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-slurm-periodic-usage-policies/{uuid}/command-history/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-slurm-periodic-usage-policies/{uuid}/dry-run/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-slurm-periodic-usage-policies/{uuid}/evaluate/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-slurm-periodic-usage-policies/{uuid}/evaluation-logs/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-slurm-periodic-usage-policies/{uuid}/force-period-reset/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-slurm-periodic-usage-policies/{uuid}/report-command-result/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-software-catalogs/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-software-catalogs/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-software-catalogs/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-software-catalogs/discover/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-software-catalogs/discover/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-software-catalogs/import_catalog/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-software-catalogs/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-software-catalogs/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/marketplace-software-catalogs/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/marketplace-software-catalogs/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-software-catalogs/{uuid}/update_catalog/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-software-packages/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: extensions
            - Properties changed
              - New property: extensions
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-software-packages/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-software-packages/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: extensions
          - Properties changed
            - New property: extensions
- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-software-packages/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-software-packages/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: extensions
          - Properties changed
            - New property: extensions
- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/marketplace-software-packages/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: extensions
          - Properties changed
            - New property: extensions
- Security changed
  - New security requirements: waldurPATAuth

PUT /api/marketplace-software-packages/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: extensions
          - Properties changed
            - New property: extensions
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-software-targets/

- Modified query param: o
  - Schema changed
    - Items changed
      - Deleted enum values: [-cpu_family cpu_family]
- Modified query param: path
  - Description changed from '' to 'Filter targets by location/path (case-insensitive partial match)'
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-software-targets/

- Modified query param: o
  - Schema changed
    - Items changed
      - Deleted enum values: [-cpu_family cpu_family]
- Modified query param: path
  - Description changed from '' to 'Filter targets by location/path (case-insensitive partial match)'
- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-software-targets/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-software-targets/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-software-targets/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/marketplace-software-targets/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/marketplace-software-targets/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-software-versions/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-software-versions/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-software-versions/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-software-versions/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-software-versions/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/marketplace-software-versions/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/marketplace-software-versions/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/aggregated_usage_trends/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/aggregated_usage_trends/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/component_usages/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/component_usages/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/component_usages_per_month/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/component_usages_per_month/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/component_usages_per_project/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/component_usages_per_project/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/count_active_resources_grouped_by_offering/

- New query param: limit
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/count_active_resources_grouped_by_offering/

- New query param: limit
- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/count_active_resources_grouped_by_offering_country/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/count_active_resources_grouped_by_offering_country/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/count_active_resources_grouped_by_organization_group/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/count_active_resources_grouped_by_organization_group/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/count_projects_grouped_by_provider_and_industry_flag/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/count_projects_grouped_by_provider_and_industry_flag/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/count_projects_grouped_by_provider_and_oecd/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/count_projects_grouped_by_provider_and_oecd/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/count_projects_of_service_providers/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/count_projects_of_service_providers/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/count_projects_of_service_providers_grouped_by_oecd/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/count_projects_of_service_providers_grouped_by_oecd/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/count_unique_users_connected_with_active_resources_of_service_provider/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/count_unique_users_connected_with_active_resources_of_service_provider/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/count_users_of_service_providers/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/count_users_of_service_providers/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/customer_member_count/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/customer_member_count/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/customer_member_summary/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/customer_member_summary/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/offering_costs_summary/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/offering_costs_summary/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/offerings_counter_stats/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/offerings_counter_stats/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/openstack_instances/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/openstack_instances/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/openstack_instances_aggregate/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/openstack_instances_aggregate/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/order_stats/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/order_stats/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/organization_project_count/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/organization_project_count/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/organization_resource_count/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/organization_resource_count/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/project_classification_summary/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/project_classification_summary/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/projects_limits_grouped_by_industry_flag/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/projects_limits_grouped_by_industry_flag/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/projects_limits_grouped_by_oecd/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/projects_limits_grouped_by_oecd/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/projects_usages_grouped_by_industry_flag/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/projects_usages_grouped_by_industry_flag/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/projects_usages_grouped_by_oecd/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/projects_usages_grouped_by_oecd/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/provider_customers/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/provider_customers/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/provider_offerings/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/provider_offerings/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/provider_resources/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/provider_resources/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/resource_provisioning_stats/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/resource_provisioning_stats/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/resource_usage_by_creator_affiliation/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/resource_usage_by_creator_affiliation/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/resource_usage_by_customer/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/resource_usage_by_customer/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/resource_usage_by_organization_type/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/resource_usage_by_organization_type/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/resources_geography_summary/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/resources_geography_summary/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/resources_limits/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/resources_limits/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/resources_missing_usage/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/resources_missing_usage/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/total_cost_of_active_resources_per_offering/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/total_cost_of_active_resources_per_offering/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/user_affiliation_count/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/user_affiliation_count/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/user_auth_method_count/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/user_auth_method_count/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/user_identity_source_count/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/user_identity_source_count/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/user_job_title_count/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/user_job_title_count/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/user_organization_count/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/user_organization_count/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-stats/user_organization_type_count/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-stats/user_organization_type_count/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-tags/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-tags/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-tags/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-tags/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-tags/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/marketplace-tags/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/marketplace-tags/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-user-offering-consents/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/marketplace-user-offering-consents/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-user-offering-consents/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/marketplace-user-offering-consents/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/marketplace-user-offering-consents/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/marketplace-user-offering-consents/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/marketplace-user-offering-consents/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/marketplace-user-offering-consents/{uuid}/revoke/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/media/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

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
                  - New enum values: [create_of_project_credit_by_staff project_end_date_change_request_approved project_end_date_change_request_created project_end_date_change_request_rejected request_slurm_resource_downscaling request_slurm_resource_pausing reset_downscaling reset_member_restriction reset_pausing update_of_project_credit_by_staff pat_created pat_revoked pat_rotated pat_expired pat_used_from_new_ip]

GET /api/metadata/permissions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: permission_map
              - AdditionalProperties changed
                - New enum values: [STAFF.ACCESS SUPPORT.ACCESS]
            - Modified property: permissions
              - AdditionalProperties changed
                - New enum values: [STAFF.ACCESS SUPPORT.ACCESS]

GET /api/my-assignment-batches/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/my-assignment-batches/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/my-assignment-batches/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/notification-messages-templates/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/notification-messages-templates/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/notification-messages-templates/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/notification-messages-templates/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/notification-messages-templates/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/notification-messages-templates/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/notification-messages-templates/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/notification-messages-templates/{uuid}/override/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/notification-messages/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/notification-messages/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/notification-messages/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/notification-messages/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/notification-messages/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/notification-messages/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/notification-messages/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/notification-messages/{uuid}/disable/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/notification-messages/{uuid}/enable/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/offering-keycloak-groups/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/offering-keycloak-groups/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/offering-keycloak-groups/import_remote/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/offering-keycloak-groups/remote_group_members/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/offering-keycloak-groups/remote_group_members/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/offering-keycloak-groups/remote_groups/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/offering-keycloak-groups/remote_groups/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/offering-keycloak-groups/search_remote_users/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/offering-keycloak-groups/search_remote_users/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/offering-keycloak-groups/sync_status/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/offering-keycloak-groups/sync_status/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/offering-keycloak-groups/test_connection/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/offering-keycloak-groups/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/offering-keycloak-groups/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/offering-keycloak-groups/{uuid}/pull_members/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/offering-keycloak-groups/{uuid}/set_backend_id/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/offering-keycloak-memberships/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/offering-keycloak-memberships/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/offering-keycloak-memberships/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/offering-keycloak-memberships/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/offering-keycloak-memberships/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/onboarding-justifications/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/onboarding-justifications/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/onboarding-justifications/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/onboarding-justifications/create_justification/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/onboarding-justifications/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/onboarding-justifications/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/onboarding-justifications/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/onboarding-justifications/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/onboarding-justifications/{uuid}/approve/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/onboarding-justifications/{uuid}/attach_document/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/onboarding-justifications/{uuid}/reject/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/onboarding-question-metadata/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/onboarding-question-metadata/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/onboarding-question-metadata/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/onboarding-question-metadata/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/onboarding-question-metadata/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/onboarding-question-metadata/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/onboarding-question-metadata/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/onboarding-verifications/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/onboarding-verifications/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/onboarding-verifications/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/onboarding-verifications/available_checklists/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/onboarding-verifications/available_checklists/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/onboarding-verifications/checklist-template/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/onboarding-verifications/checklist-template/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/onboarding-verifications/start_verification/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/onboarding-verifications/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/onboarding-verifications/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/onboarding-verifications/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/onboarding-verifications/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/onboarding-verifications/{uuid}/checklist/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/onboarding-verifications/{uuid}/completion_status/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/onboarding-verifications/{uuid}/create_customer/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: apartment_nr
            - New property: city
            - New property: house_nr
            - New property: household
            - New property: parish
            - New property: state
            - New property: street
- Security changed
  - New security requirements: waldurPATAuth

POST /api/onboarding-verifications/{uuid}/run_validation/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/onboarding-verifications/{uuid}/submit_answers/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/onboarding/person-identifier-fields/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/onboarding/supported-countries/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openportal-allocation-user-usage/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openportal-allocation-user-usage/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openportal-allocation-user-usage/{id}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openportal-allocations/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openportal-allocations/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openportal-allocations/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/openportal-allocations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openportal-allocations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/openportal-allocations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/openportal-allocations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openportal-allocations/{uuid}/pull/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openportal-allocations/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openportal-allocations/{uuid}/set_limits/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openportal-allocations/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openportal-allocations/{uuid}/unlink/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openportal-associations/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openportal-associations/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openportal-associations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openportal-managed-projects/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: project_data
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/Project
                    - Properties changed
                      - New property: customer_grace_period_days
                      - New property: effective_end_date
                      - New property: end_date_updated_at
                      - New property: is_in_grace_period
              - Modified property: project_template_data
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/ProjectTemplate
                    - Properties changed
                      - Modified property: customer_data
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/Customer
                            - Properties changed
                              - New property: apartment_nr
                              - New property: city
                              - New property: house_nr
                              - New property: household
                              - New property: parish
                              - New property: state
                              - New property: street
                      - Modified property: offerings_data
                        - Items changed
                          - Properties changed
                            - New property: documentation_url
                            - New property: effective_available_limits
                            - New property: helpdesk_url
                            - Modified property: components
                              - Items changed
                                - Properties changed
                                  - New property: max_renewal_duration
                                  - New property: min_renewal_duration
                                  - New property: prepaid_duration_step
                                  - New property: renewal_duration_step
                            - Modified property: plans
                              - Items changed
                                - Properties changed
                                  - Modified property: components
                                    - Items changed
                                      - Properties changed
                                        - New property: discount_description
                                        - New property: discounted_price
                            - Modified property: plugin_options
                              - Property 'AllOf' changed
                                - Modified schema: #/components/schemas/MergedPluginOptions
                                  - Properties changed
                                    - New property: lbaas_enabled
                      - Modified property: provider_data
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/Customer
                            - Properties changed
                              - New property: apartment_nr
                              - New property: city
                              - New property: house_nr
                              - New property: household
                              - New property: parish
                              - New property: state
                              - New property: street
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openportal-managed-projects/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openportal-managed-projects/{identifier}/{destination}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: project_data
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/Project
                  - Properties changed
                    - New property: customer_grace_period_days
                    - New property: effective_end_date
                    - New property: end_date_updated_at
                    - New property: is_in_grace_period
            - Modified property: project_template_data
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ProjectTemplate
                  - Properties changed
                    - Modified property: customer_data
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/Customer
                          - Properties changed
                            - New property: apartment_nr
                            - New property: city
                            - New property: house_nr
                            - New property: household
                            - New property: parish
                            - New property: state
                            - New property: street
                    - Modified property: offerings_data
                      - Items changed
                        - Properties changed
                          - New property: documentation_url
                          - New property: effective_available_limits
                          - New property: helpdesk_url
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: max_renewal_duration
                                - New property: min_renewal_duration
                                - New property: prepaid_duration_step
                                - New property: renewal_duration_step
                          - Modified property: plans
                            - Items changed
                              - Properties changed
                                - Modified property: components
                                  - Items changed
                                    - Properties changed
                                      - New property: discount_description
                                      - New property: discounted_price
                          - Modified property: plugin_options
                            - Property 'AllOf' changed
                              - Modified schema: #/components/schemas/MergedPluginOptions
                                - Properties changed
                                  - New property: lbaas_enabled
                    - Modified property: provider_data
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/Customer
                          - Properties changed
                            - New property: apartment_nr
                            - New property: city
                            - New property: house_nr
                            - New property: household
                            - New property: parish
                            - New property: state
                            - New property: street
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openportal-managed-projects/{identifier}/{destination}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openportal-managed-projects/{identifier}/{destination}/approve/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openportal-managed-projects/{identifier}/{destination}/attach/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/openportal-managed-projects/{identifier}/{destination}/delete/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openportal-managed-projects/{identifier}/{destination}/detach/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openportal-managed-projects/{identifier}/{destination}/reject/

- Security changed
  - New security requirements: waldurPATAuth

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
                  - Modified schema: #/components/schemas/Customer
                    - Properties changed
                      - New property: apartment_nr
                      - New property: city
                      - New property: house_nr
                      - New property: household
                      - New property: parish
                      - New property: state
                      - New property: street
              - Modified property: offerings_data
                - Items changed
                  - Properties changed
                    - New property: documentation_url
                    - New property: effective_available_limits
                    - New property: helpdesk_url
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: max_renewal_duration
                          - New property: min_renewal_duration
                          - New property: prepaid_duration_step
                          - New property: renewal_duration_step
                    - Modified property: plans
                      - Items changed
                        - Properties changed
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: discount_description
                                - New property: discounted_price
                    - Modified property: plugin_options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/MergedPluginOptions
                          - Properties changed
                            - New property: lbaas_enabled
              - Modified property: provider_data
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/Customer
                    - Properties changed
                      - New property: apartment_nr
                      - New property: city
                      - New property: house_nr
                      - New property: household
                      - New property: parish
                      - New property: state
                      - New property: street
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openportal-project-template/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openportal-project-template/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: customer_data
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/Customer
                  - Properties changed
                    - New property: apartment_nr
                    - New property: city
                    - New property: house_nr
                    - New property: household
                    - New property: parish
                    - New property: state
                    - New property: street
            - Modified property: offerings_data
              - Items changed
                - Properties changed
                  - New property: documentation_url
                  - New property: effective_available_limits
                  - New property: helpdesk_url
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: max_renewal_duration
                        - New property: min_renewal_duration
                        - New property: prepaid_duration_step
                        - New property: renewal_duration_step
                  - Modified property: plans
                    - Items changed
                      - Properties changed
                        - Modified property: components
                          - Items changed
                            - Properties changed
                              - New property: discount_description
                              - New property: discounted_price
                  - Modified property: plugin_options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/MergedPluginOptions
                        - Properties changed
                          - New property: lbaas_enabled
            - Modified property: provider_data
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/Customer
                  - Properties changed
                    - New property: apartment_nr
                    - New property: city
                    - New property: house_nr
                    - New property: household
                    - New property: parish
                    - New property: state
                    - New property: street
- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/openportal-project-template/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openportal-project-template/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: customer_data
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/Customer
                  - Properties changed
                    - New property: apartment_nr
                    - New property: city
                    - New property: house_nr
                    - New property: household
                    - New property: parish
                    - New property: state
                    - New property: street
            - Modified property: offerings_data
              - Items changed
                - Properties changed
                  - New property: documentation_url
                  - New property: effective_available_limits
                  - New property: helpdesk_url
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: max_renewal_duration
                        - New property: min_renewal_duration
                        - New property: prepaid_duration_step
                        - New property: renewal_duration_step
                  - Modified property: plans
                    - Items changed
                      - Properties changed
                        - Modified property: components
                          - Items changed
                            - Properties changed
                              - New property: discount_description
                              - New property: discounted_price
                  - Modified property: plugin_options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/MergedPluginOptions
                        - Properties changed
                          - New property: lbaas_enabled
            - Modified property: provider_data
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/Customer
                  - Properties changed
                    - New property: apartment_nr
                    - New property: city
                    - New property: house_nr
                    - New property: household
                    - New property: parish
                    - New property: state
                    - New property: street
- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/openportal-project-template/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: customer_data
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/Customer
                  - Properties changed
                    - New property: apartment_nr
                    - New property: city
                    - New property: house_nr
                    - New property: household
                    - New property: parish
                    - New property: state
                    - New property: street
            - Modified property: offerings_data
              - Items changed
                - Properties changed
                  - New property: documentation_url
                  - New property: effective_available_limits
                  - New property: helpdesk_url
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: max_renewal_duration
                        - New property: min_renewal_duration
                        - New property: prepaid_duration_step
                        - New property: renewal_duration_step
                  - Modified property: plans
                    - Items changed
                      - Properties changed
                        - Modified property: components
                          - Items changed
                            - Properties changed
                              - New property: discount_description
                              - New property: discounted_price
                  - Modified property: plugin_options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/MergedPluginOptions
                        - Properties changed
                          - New property: lbaas_enabled
            - Modified property: provider_data
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/Customer
                  - Properties changed
                    - New property: apartment_nr
                    - New property: city
                    - New property: house_nr
                    - New property: household
                    - New property: parish
                    - New property: state
                    - New property: street
- Security changed
  - New security requirements: waldurPATAuth

PUT /api/openportal-project-template/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: customer_data
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/Customer
                  - Properties changed
                    - New property: apartment_nr
                    - New property: city
                    - New property: house_nr
                    - New property: household
                    - New property: parish
                    - New property: state
                    - New property: street
            - Modified property: offerings_data
              - Items changed
                - Properties changed
                  - New property: documentation_url
                  - New property: effective_available_limits
                  - New property: helpdesk_url
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: max_renewal_duration
                        - New property: min_renewal_duration
                        - New property: prepaid_duration_step
                        - New property: renewal_duration_step
                  - Modified property: plans
                    - Items changed
                      - Properties changed
                        - Modified property: components
                          - Items changed
                            - Properties changed
                              - New property: discount_description
                              - New property: discounted_price
                  - Modified property: plugin_options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/MergedPluginOptions
                        - Properties changed
                          - New property: lbaas_enabled
            - Modified property: provider_data
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/Customer
                  - Properties changed
                    - New property: apartment_nr
                    - New property: city
                    - New property: house_nr
                    - New property: household
                    - New property: parish
                    - New property: state
                    - New property: street
- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/openportal-project-template/{uuid}/delete/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openportal-projectinfo/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openportal-projectinfo/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openportal-projectinfo/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/openportal-projectinfo/{project}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openportal-projectinfo/{project}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/openportal-projectinfo/{project}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/openportal-projectinfo/{project}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/openportal-projectinfo/{project}/set_allowed_destinations/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/openportal-projectinfo/{project}/set_shortname/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openportal-remote-allocations/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openportal-remote-allocations/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openportal-remote-allocations/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/openportal-remote-allocations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openportal-remote-allocations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/openportal-remote-allocations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/openportal-remote-allocations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openportal-remote-allocations/{uuid}/pull/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openportal-remote-allocations/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openportal-remote-allocations/{uuid}/set_limits/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openportal-remote-allocations/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openportal-remote-allocations/{uuid}/unlink/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openportal-remote-associations/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openportal-remote-associations/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openportal-remote-associations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openportal-unmanaged-projects/

- New query param: created_before
- New query param: modified_before
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_grace_period_days effective_end_date end_date_updated_at is_in_grace_period]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_grace_period_days
              - New property: effective_end_date
              - New property: end_date_updated_at
              - New property: is_in_grace_period
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openportal-unmanaged-projects/

- New query param: created_before
- New query param: modified_before
- Security changed
  - New security requirements: waldurPATAuth

POST /api/openportal-unmanaged-projects/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_grace_period_days
            - New property: effective_end_date
            - New property: end_date_updated_at
            - New property: is_in_grace_period
- Security changed
  - New security requirements: waldurPATAuth

GET /api/openportal-unmanaged-projects/checklist-template/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openportal-unmanaged-projects/checklist-template/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/openportal-unmanaged-projects/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openportal-unmanaged-projects/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_grace_period_days effective_end_date end_date_updated_at is_in_grace_period]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_grace_period_days
            - New property: effective_end_date
            - New property: end_date_updated_at
            - New property: is_in_grace_period
- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/openportal-unmanaged-projects/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_grace_period_days
            - New property: effective_end_date
            - New property: end_date_updated_at
            - New property: is_in_grace_period
- Security changed
  - New security requirements: waldurPATAuth

PUT /api/openportal-unmanaged-projects/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_grace_period_days
            - New property: effective_end_date
            - New property: end_date_updated_at
            - New property: is_in_grace_period
- Security changed
  - New security requirements: waldurPATAuth

POST /api/openportal-unmanaged-projects/{uuid}/add_user/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openportal-unmanaged-projects/{uuid}/checklist/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openportal-unmanaged-projects/{uuid}/completion_status/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openportal-unmanaged-projects/{uuid}/delete_user/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openportal-unmanaged-projects/{uuid}/list_users/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openportal-unmanaged-projects/{uuid}/move_project/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_grace_period_days
            - New property: effective_end_date
            - New property: end_date_updated_at
            - New property: is_in_grace_period
- Security changed
  - New security requirements: waldurPATAuth

POST /api/openportal-unmanaged-projects/{uuid}/recover/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_grace_period_days
            - New property: effective_end_date
            - New property: end_date_updated_at
            - New property: is_in_grace_period
- Security changed
  - New security requirements: waldurPATAuth

GET /api/openportal-unmanaged-projects/{uuid}/stats/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openportal-unmanaged-projects/{uuid}/submit_answers/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openportal-unmanaged-projects/{uuid}/update_user/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openportal-userinfo/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openportal-userinfo/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openportal-userinfo/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openportal-userinfo/me/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openportal-userinfo/me/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/openportal-userinfo/{user}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openportal-userinfo/{user}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/openportal-userinfo/{user}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/openportal-userinfo/{user}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/openportal-userinfo/{user}/set_shortname/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-backups/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openstack-backups/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/openstack-backups/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-backups/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/openstack-backups/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/openstack-backups/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-backups/{uuid}/pull/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-backups/{uuid}/restore/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-backups/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-backups/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-backups/{uuid}/unlink/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-external-networks/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openstack-external-networks/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-external-networks/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-flavors/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openstack-flavors/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-flavors/usage_stats/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openstack-flavors/usage_stats/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-flavors/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-floating-ips/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openstack-floating-ips/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/openstack-floating-ips/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-floating-ips/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-floating-ips/{uuid}/attach_to_port/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-floating-ips/{uuid}/detach_from_port/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-floating-ips/{uuid}/pull/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-floating-ips/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-floating-ips/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-floating-ips/{uuid}/unlink/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-floating-ips/{uuid}/update_description/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-health-monitors/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openstack-health-monitors/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-health-monitors/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: delay
          - Deleted required property: max_retries
          - Deleted required property: timeout
        - Properties changed
          - New property: max_retries_down
          - Modified property: delay
            - Default changed from null to 5
          - Modified property: max_retries
            - Description changed from 'Number of retries before marking member as down' to ''
            - Default changed from null to 3
          - Modified property: timeout
            - Default changed from null to 5
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: delay
            - Deleted required property: max_retries
            - Deleted required property: project
            - Deleted required property: service_settings
            - Deleted required property: timeout
          - Properties changed
            - New property: max_retries_down
            - Deleted property: project
            - Deleted property: service_settings
            - Modified property: delay
              - Default changed from null to 5
            - Modified property: max_retries
              - Description changed from 'Number of retries before marking member as down' to ''
              - Default changed from null to 3
            - Modified property: timeout
              - Default changed from null to 5
- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/openstack-health-monitors/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-health-monitors/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/openstack-health-monitors/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: max_retries_down
          - Modified property: delay
            - Description changed from '' to 'Interval between health checks in seconds'
            - Default changed from null to 5
          - Modified property: max_retries
            - Default changed from null to 3
          - Modified property: timeout
            - Description changed from '' to 'Time in seconds to timeout a health check'
            - Default changed from null to 5
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: url
            - New required property: uuid
          - Properties changed
            - New property: max_retries_down
            - New property: url
            - New property: uuid
            - Modified property: delay
              - Description changed from '' to 'Interval between health checks in seconds'
              - Default changed from null to 5
            - Modified property: max_retries
              - Default changed from null to 3
            - Modified property: timeout
              - Description changed from '' to 'Time in seconds to timeout a health check'
              - Default changed from null to 5
- Security changed
  - New security requirements: waldurPATAuth

PUT /api/openstack-health-monitors/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: max_retries_down
          - Modified property: delay
            - Description changed from '' to 'Interval between health checks in seconds'
            - Default changed from null to 5
          - Modified property: max_retries
            - Default changed from null to 3
          - Modified property: timeout
            - Description changed from '' to 'Time in seconds to timeout a health check'
            - Default changed from null to 5
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: url
            - New required property: uuid
          - Properties changed
            - New property: max_retries_down
            - New property: url
            - New property: uuid
            - Modified property: delay
              - Description changed from '' to 'Interval between health checks in seconds'
              - Default changed from null to 5
            - Modified property: max_retries
              - Default changed from null to 3
            - Modified property: timeout
              - Description changed from '' to 'Time in seconds to timeout a health check'
              - Default changed from null to 5
- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-images/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openstack-images/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-images/usage_stats/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openstack-images/usage_stats/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-images/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-instance-availability-zones/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openstack-instance-availability-zones/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-instance-availability-zones/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-instances/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openstack-instances/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-instances/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/openstack-instances/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/openstack-instances/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-instances/{uuid}/backup/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-instances/{uuid}/change_flavor/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-instances/{uuid}/console/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-instances/{uuid}/console_log/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-instances/{uuid}/floating_ips/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-instances/{uuid}/ports/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-instances/{uuid}/pull/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-instances/{uuid}/restart/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-instances/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-instances/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-instances/{uuid}/start/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-instances/{uuid}/stop/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-instances/{uuid}/unlink/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-instances/{uuid}/update_allowed_address_pairs/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-instances/{uuid}/update_floating_ips/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-instances/{uuid}/update_ports/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-instances/{uuid}/update_security_groups/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-listeners/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openstack-listeners/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-listeners/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: name
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: name
            - Deleted required property: project
            - Deleted required property: service_settings
          - Properties changed
            - Deleted property: project
            - Deleted property: service_settings
- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/openstack-listeners/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-listeners/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/openstack-listeners/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/openstack-listeners/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-loadbalancers/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [vip_port vip_subnet]
      - Deleted enum values: [vip_port_id vip_subnet_id]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: vip_port
              - New property: vip_subnet
              - Deleted property: vip_port_id
              - Deleted property: vip_subnet_id
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openstack-loadbalancers/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-loadbalancers/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - New required property: vip_subnet
          - Deleted required property: vip_subnet_id
        - Properties changed
          - New property: vip_subnet
          - Deleted property: vip_subnet_id
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: vip_subnet
            - Deleted required property: project
            - Deleted required property: service_settings
            - Deleted required property: vip_subnet_id
          - Properties changed
            - New property: vip_subnet
            - Deleted property: project
            - Deleted property: service_settings
            - Deleted property: vip_subnet_id
- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/openstack-loadbalancers/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-loadbalancers/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [vip_port vip_subnet]
      - Deleted enum values: [vip_port_id vip_subnet_id]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: vip_port
            - New property: vip_subnet
            - Deleted property: vip_port_id
            - Deleted property: vip_subnet_id
- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/openstack-loadbalancers/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: attached_floating_ip
          - Deleted property: backend_id
          - Deleted property: description
          - Deleted property: error_message
          - Deleted property: error_traceback
          - Deleted property: project
          - Deleted property: service_settings
          - Deleted property: tenant
          - Modified property: name
            - MaxLength changed from 150 to null
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: name
            - New required property: url
            - New required property: uuid
          - Properties changed
            - Deleted property: access_url
            - Deleted property: attached_floating_ip
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
            - Deleted property: operating_status
            - Deleted property: project
            - Deleted property: project_name
            - Deleted property: project_uuid
            - Deleted property: provider
            - Deleted property: provisioning_status
            - Deleted property: resource_type
            - Deleted property: service_name
            - Deleted property: service_settings
            - Deleted property: service_settings_error_message
            - Deleted property: service_settings_state
            - Deleted property: service_settings_uuid
            - Deleted property: state
            - Deleted property: tenant
            - Deleted property: tenant_name
            - Deleted property: tenant_uuid
            - Deleted property: vip_address
            - Deleted property: vip_port_id
            - Deleted property: vip_subnet_id
            - Modified property: name
              - MaxLength changed from 150 to null
- Security changed
  - New security requirements: waldurPATAuth

PUT /api/openstack-loadbalancers/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: project
          - Deleted required property: service_settings
          - Deleted required property: tenant
        - Properties changed
          - Deleted property: attached_floating_ip
          - Deleted property: backend_id
          - Deleted property: description
          - Deleted property: error_message
          - Deleted property: error_traceback
          - Deleted property: project
          - Deleted property: service_settings
          - Deleted property: tenant
          - Modified property: name
            - MaxLength changed from 150 to null
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: name
            - New required property: url
            - New required property: uuid
          - Properties changed
            - Deleted property: access_url
            - Deleted property: attached_floating_ip
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
            - Deleted property: operating_status
            - Deleted property: project
            - Deleted property: project_name
            - Deleted property: project_uuid
            - Deleted property: provider
            - Deleted property: provisioning_status
            - Deleted property: resource_type
            - Deleted property: service_name
            - Deleted property: service_settings
            - Deleted property: service_settings_error_message
            - Deleted property: service_settings_state
            - Deleted property: service_settings_uuid
            - Deleted property: state
            - Deleted property: tenant
            - Deleted property: tenant_name
            - Deleted property: tenant_uuid
            - Deleted property: vip_address
            - Deleted property: vip_port_id
            - Deleted property: vip_subnet_id
            - Modified property: name
              - MaxLength changed from 150 to null
- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-loadbalancers/{uuid}/attach_floating_ip/

- Responses changed
  - New response: 202
  - Deleted response: 200
- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-loadbalancers/{uuid}/detach_floating_ip/

- Responses changed
  - New response: 202
  - Deleted response: 200
- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-marketplace-tenants/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openstack-marketplace-tenants/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-marketplace-tenants/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-marketplace-tenants/{uuid}/create_image/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-marketplace-tenants/{uuid}/upload_image_data/{image_id}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-migrations/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openstack-migrations/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-migrations/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/openstack-migrations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-migrations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/openstack-migrations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/openstack-migrations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-network-rbac-policies/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openstack-network-rbac-policies/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-network-rbac-policies/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/openstack-network-rbac-policies/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-network-rbac-policies/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/openstack-network-rbac-policies/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/openstack-network-rbac-policies/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-networks/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openstack-networks/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/openstack-networks/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-networks/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/openstack-networks/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/openstack-networks/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-networks/{uuid}/create_subnet/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-networks/{uuid}/pull/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-networks/{uuid}/rbac_policy_create/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/openstack-networks/{uuid}/rbac_policy_delete/{rbac_policy_uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-networks/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-networks/{uuid}/set_mtu/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-networks/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-networks/{uuid}/unlink/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-pool-members/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [subnet]
      - Deleted enum values: [subnet_id]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: subnet
              - Deleted property: subnet_id
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openstack-pool-members/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-pool-members/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - New required property: subnet
          - Deleted required property: subnet_id
        - Properties changed
          - New property: subnet
          - Deleted property: subnet_id
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: subnet
            - Deleted required property: project
            - Deleted required property: service_settings
            - Deleted required property: subnet_id
          - Properties changed
            - New property: subnet
            - Deleted property: project
            - Deleted property: service_settings
            - Deleted property: subnet_id
- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/openstack-pool-members/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-pool-members/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [subnet]
      - Deleted enum values: [subnet_id]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: subnet
            - Deleted property: subnet_id
- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/openstack-pool-members/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: weight
            - Default changed from null to 1
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: url
            - New required property: uuid
          - Properties changed
            - New property: url
            - New property: uuid
            - Modified property: weight
              - Default changed from null to 1
- Security changed
  - New security requirements: waldurPATAuth

PUT /api/openstack-pool-members/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: weight
            - Default changed from null to 1
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: url
            - New required property: uuid
          - Properties changed
            - New property: url
            - New property: uuid
            - Modified property: weight
              - Default changed from null to 1
- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-pools/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openstack-pools/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-pools/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: lb_algorithm
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: project
            - Deleted required property: service_settings
          - Properties changed
            - Deleted property: lb_algorithm
            - Deleted property: project
            - Deleted property: service_settings
- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/openstack-pools/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-pools/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/openstack-pools/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: backend_id
          - Deleted property: description
          - Deleted property: error_message
          - Deleted property: error_traceback
          - Deleted property: load_balancer
          - Deleted property: project
          - Deleted property: service_settings
          - Modified property: name
            - MaxLength changed from 150 to null
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: name
            - New required property: url
            - New required property: uuid
          - Properties changed
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
            - Deleted property: lb_algorithm
            - Deleted property: load_balancer
            - Deleted property: load_balancer_name
            - Deleted property: load_balancer_uuid
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
            - Deleted property: operating_status
            - Deleted property: project
            - Deleted property: project_name
            - Deleted property: project_uuid
            - Deleted property: protocol
            - Deleted property: provisioning_status
            - Deleted property: resource_type
            - Deleted property: service_name
            - Deleted property: service_settings
            - Deleted property: service_settings_error_message
            - Deleted property: service_settings_state
            - Deleted property: service_settings_uuid
            - Deleted property: state
            - Modified property: name
              - MaxLength changed from 150 to null
- Security changed
  - New security requirements: waldurPATAuth

PUT /api/openstack-pools/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: load_balancer
          - Deleted required property: project
          - Deleted required property: service_settings
        - Properties changed
          - Deleted property: backend_id
          - Deleted property: description
          - Deleted property: error_message
          - Deleted property: error_traceback
          - Deleted property: load_balancer
          - Deleted property: project
          - Deleted property: service_settings
          - Modified property: name
            - MaxLength changed from 150 to null
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: name
            - New required property: url
            - New required property: uuid
          - Properties changed
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
            - Deleted property: lb_algorithm
            - Deleted property: load_balancer
            - Deleted property: load_balancer_name
            - Deleted property: load_balancer_uuid
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
            - Deleted property: operating_status
            - Deleted property: project
            - Deleted property: project_name
            - Deleted property: project_uuid
            - Deleted property: protocol
            - Deleted property: provisioning_status
            - Deleted property: resource_type
            - Deleted property: service_name
            - Deleted property: service_settings
            - Deleted property: service_settings_error_message
            - Deleted property: service_settings_state
            - Deleted property: service_settings_uuid
            - Deleted property: state
            - Modified property: name
              - MaxLength changed from 150 to null
- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-ports/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openstack-ports/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-ports/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/openstack-ports/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-ports/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/openstack-ports/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/openstack-ports/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-ports/{uuid}/disable_port/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-ports/{uuid}/disable_port_security/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-ports/{uuid}/enable_port/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-ports/{uuid}/enable_port_security/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-ports/{uuid}/pull/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-ports/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-ports/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-ports/{uuid}/unlink/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-ports/{uuid}/update_port_ip/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-ports/{uuid}/update_security_groups/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-routers/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openstack-routers/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-routers/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/openstack-routers/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-routers/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-routers/{uuid}/add_router_interface/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-routers/{uuid}/remove_router_interface/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-routers/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-routers/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-routers/{uuid}/set_routes/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-security-groups/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openstack-security-groups/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/openstack-security-groups/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-security-groups/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/openstack-security-groups/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/openstack-security-groups/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-security-groups/{uuid}/pull/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-security-groups/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-security-groups/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-security-groups/{uuid}/set_rules/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-security-groups/{uuid}/unlink/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-server-groups/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openstack-server-groups/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-server-groups/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/openstack-server-groups/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-server-groups/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-server-groups/{uuid}/pull/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-server-groups/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-server-groups/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-server-groups/{uuid}/unlink/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-snapshots/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openstack-snapshots/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/openstack-snapshots/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-snapshots/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/openstack-snapshots/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/openstack-snapshots/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-snapshots/{uuid}/pull/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-snapshots/{uuid}/restorations/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-snapshots/{uuid}/restore/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-snapshots/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-snapshots/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-snapshots/{uuid}/unlink/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-subnets/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openstack-subnets/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/openstack-subnets/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-subnets/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/openstack-subnets/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/openstack-subnets/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-subnets/{uuid}/connect/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-subnets/{uuid}/disconnect/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-subnets/{uuid}/pull/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-subnets/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-subnets/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-subnets/{uuid}/unlink/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-tenants/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openstack-tenants/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-tenants/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/openstack-tenants/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/openstack-tenants/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-tenants/{uuid}/backend_instances/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-tenants/{uuid}/backend_volumes/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-tenants/{uuid}/change_password/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-tenants/{uuid}/create_floating_ip/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-tenants/{uuid}/create_network/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-tenants/{uuid}/create_security_group/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-tenants/{uuid}/create_server_group/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-tenants/{uuid}/pull/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-tenants/{uuid}/pull_floating_ips/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-tenants/{uuid}/pull_quotas/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-tenants/{uuid}/pull_security_groups/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-tenants/{uuid}/pull_server_groups/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-tenants/{uuid}/push_security_groups/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-tenants/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-tenants/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-tenants/{uuid}/set_quotas/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-tenants/{uuid}/unlink/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-volume-availability-zones/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openstack-volume-availability-zones/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-volume-availability-zones/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-volume-types/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openstack-volume-types/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-volume-types/names/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openstack-volume-types/names/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-volume-types/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-volumes/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/openstack-volumes/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack-volumes/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/openstack-volumes/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/openstack-volumes/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-volumes/{uuid}/attach/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-volumes/{uuid}/detach/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-volumes/{uuid}/extend/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-volumes/{uuid}/pull/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-volumes/{uuid}/retype/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-volumes/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-volumes/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-volumes/{uuid}/snapshot/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack-volumes/{uuid}/unlink/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack/discovery/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack/discovery/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack/discovery/discover_external_networks/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack/discovery/discover_flavors/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack/discovery/discover_instance_availability_zones/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack/discovery/discover_volume_availability_zones/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack/discovery/discover_volume_types/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack/discovery/preview_service_attributes/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/openstack/discovery/validate_credentials/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/openstack/discovery/{id}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/openstack/discovery/{id}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/openstack/discovery/{id}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/openstack/discovery/{id}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/organization-groups/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/organization-groups/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/organization-groups/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/organization-groups/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/organization-groups/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/organization-groups/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/organization-groups/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/override-settings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: AI_ASSISTANT_API_TOKEN
            - New property: AI_ASSISTANT_API_URL
            - New property: AI_ASSISTANT_BACKEND_TYPE
            - New property: AI_ASSISTANT_COMPLETION_KWARGS
            - New property: AI_ASSISTANT_ENABLED
            - New property: AI_ASSISTANT_ENABLED_ROLES
            - New property: AI_ASSISTANT_HISTORY_LIMIT
            - New property: AI_ASSISTANT_INJECTION_ALLOWLIST
            - New property: AI_ASSISTANT_MODEL
            - New property: AI_ASSISTANT_NAME
            - New property: AI_ASSISTANT_SESSION_RETENTION_DAYS
            - New property: AI_ASSISTANT_TOKEN_LIMIT_DAILY
            - New property: AI_ASSISTANT_TOKEN_LIMIT_MONTHLY
            - New property: AI_ASSISTANT_TOKEN_LIMIT_WEEKLY
            - New property: ENABLED_REPORTING_SCREENS
            - New property: MARKETPLACE_CARD_STYLE
            - New property: MARKETPLACE_LAYOUT_MODE
            - New property: OIDC_BLOCK_CREATION_OF_UNINVITED_USERS_RESPONSE_MESSAGE
            - New property: PAT_ENABLED
            - New property: PAT_MAX_LIFETIME_DAYS
            - New property: PAT_MAX_TOKENS_PER_USER
            - Deleted property: LLM_CHAT_ENABLED
            - Deleted property: LLM_CHAT_HISTORY_LIMIT
            - Deleted property: LLM_CHAT_SESSION_RETENTION_DAYS
            - Deleted property: LLM_INFERENCES_API_TOKEN
            - Deleted property: LLM_INFERENCES_API_URL
            - Deleted property: LLM_INFERENCES_BACKEND_TYPE
            - Deleted property: LLM_INFERENCES_MODEL
            - Deleted property: LLM_INJECTION_ALLOWLIST
            - Deleted property: LLM_TOKEN_LIMIT_DAILY
            - Deleted property: LLM_TOKEN_LIMIT_MONTHLY
            - Deleted property: LLM_TOKEN_LIMIT_WEEKLY
- Security changed
  - New security requirements: waldurPATAuth

POST /api/override-settings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: AI_ASSISTANT_API_TOKEN
          - New property: AI_ASSISTANT_API_URL
          - New property: AI_ASSISTANT_BACKEND_TYPE
          - New property: AI_ASSISTANT_COMPLETION_KWARGS
          - New property: AI_ASSISTANT_ENABLED
          - New property: AI_ASSISTANT_ENABLED_ROLES
          - New property: AI_ASSISTANT_HISTORY_LIMIT
          - New property: AI_ASSISTANT_INJECTION_ALLOWLIST
          - New property: AI_ASSISTANT_MODEL
          - New property: AI_ASSISTANT_NAME
          - New property: AI_ASSISTANT_SESSION_RETENTION_DAYS
          - New property: AI_ASSISTANT_TOKEN_LIMIT_DAILY
          - New property: AI_ASSISTANT_TOKEN_LIMIT_MONTHLY
          - New property: AI_ASSISTANT_TOKEN_LIMIT_WEEKLY
          - New property: ENABLED_REPORTING_SCREENS
          - New property: MARKETPLACE_CARD_STYLE
          - New property: MARKETPLACE_LAYOUT_MODE
          - New property: OIDC_BLOCK_CREATION_OF_UNINVITED_USERS_RESPONSE_MESSAGE
          - New property: PAT_ENABLED
          - New property: PAT_MAX_LIFETIME_DAYS
          - New property: PAT_MAX_TOKENS_PER_USER
          - Deleted property: LLM_CHAT_ENABLED
          - Deleted property: LLM_CHAT_HISTORY_LIMIT
          - Deleted property: LLM_CHAT_SESSION_RETENTION_DAYS
          - Deleted property: LLM_INFERENCES_API_TOKEN
          - Deleted property: LLM_INFERENCES_API_URL
          - Deleted property: LLM_INFERENCES_BACKEND_TYPE
          - Deleted property: LLM_INFERENCES_MODEL
          - Deleted property: LLM_INJECTION_ALLOWLIST
          - Deleted property: LLM_TOKEN_LIMIT_DAILY
          - Deleted property: LLM_TOKEN_LIMIT_MONTHLY
          - Deleted property: LLM_TOKEN_LIMIT_WEEKLY
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: AI_ASSISTANT_API_TOKEN
          - New property: AI_ASSISTANT_API_URL
          - New property: AI_ASSISTANT_BACKEND_TYPE
          - New property: AI_ASSISTANT_COMPLETION_KWARGS
          - New property: AI_ASSISTANT_ENABLED
          - New property: AI_ASSISTANT_ENABLED_ROLES
          - New property: AI_ASSISTANT_HISTORY_LIMIT
          - New property: AI_ASSISTANT_INJECTION_ALLOWLIST
          - New property: AI_ASSISTANT_MODEL
          - New property: AI_ASSISTANT_NAME
          - New property: AI_ASSISTANT_SESSION_RETENTION_DAYS
          - New property: AI_ASSISTANT_TOKEN_LIMIT_DAILY
          - New property: AI_ASSISTANT_TOKEN_LIMIT_MONTHLY
          - New property: AI_ASSISTANT_TOKEN_LIMIT_WEEKLY
          - New property: ENABLED_REPORTING_SCREENS
          - New property: MARKETPLACE_CARD_STYLE
          - New property: MARKETPLACE_LAYOUT_MODE
          - New property: OIDC_BLOCK_CREATION_OF_UNINVITED_USERS_RESPONSE_MESSAGE
          - New property: PAT_ENABLED
          - New property: PAT_MAX_LIFETIME_DAYS
          - New property: PAT_MAX_TOKENS_PER_USER
          - Deleted property: LLM_CHAT_ENABLED
          - Deleted property: LLM_CHAT_HISTORY_LIMIT
          - Deleted property: LLM_CHAT_SESSION_RETENTION_DAYS
          - Deleted property: LLM_INFERENCES_API_TOKEN
          - Deleted property: LLM_INFERENCES_API_URL
          - Deleted property: LLM_INFERENCES_BACKEND_TYPE
          - Deleted property: LLM_INFERENCES_MODEL
          - Deleted property: LLM_INJECTION_ALLOWLIST
          - Deleted property: LLM_TOKEN_LIMIT_DAILY
          - Deleted property: LLM_TOKEN_LIMIT_MONTHLY
          - Deleted property: LLM_TOKEN_LIMIT_WEEKLY
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: AI_ASSISTANT_API_TOKEN
          - New property: AI_ASSISTANT_API_URL
          - New property: AI_ASSISTANT_BACKEND_TYPE
          - New property: AI_ASSISTANT_COMPLETION_KWARGS
          - New property: AI_ASSISTANT_ENABLED
          - New property: AI_ASSISTANT_ENABLED_ROLES
          - New property: AI_ASSISTANT_HISTORY_LIMIT
          - New property: AI_ASSISTANT_INJECTION_ALLOWLIST
          - New property: AI_ASSISTANT_MODEL
          - New property: AI_ASSISTANT_NAME
          - New property: AI_ASSISTANT_SESSION_RETENTION_DAYS
          - New property: AI_ASSISTANT_TOKEN_LIMIT_DAILY
          - New property: AI_ASSISTANT_TOKEN_LIMIT_MONTHLY
          - New property: AI_ASSISTANT_TOKEN_LIMIT_WEEKLY
          - New property: ENABLED_REPORTING_SCREENS
          - New property: MARKETPLACE_CARD_STYLE
          - New property: MARKETPLACE_LAYOUT_MODE
          - New property: OIDC_BLOCK_CREATION_OF_UNINVITED_USERS_RESPONSE_MESSAGE
          - New property: PAT_ENABLED
          - New property: PAT_MAX_LIFETIME_DAYS
          - New property: PAT_MAX_TOKENS_PER_USER
          - Deleted property: LLM_CHAT_ENABLED
          - Deleted property: LLM_CHAT_HISTORY_LIMIT
          - Deleted property: LLM_CHAT_SESSION_RETENTION_DAYS
          - Deleted property: LLM_INFERENCES_API_TOKEN
          - Deleted property: LLM_INFERENCES_API_URL
          - Deleted property: LLM_INFERENCES_BACKEND_TYPE
          - Deleted property: LLM_INFERENCES_MODEL
          - Deleted property: LLM_INJECTION_ALLOWLIST
          - Deleted property: LLM_TOKEN_LIMIT_DAILY
          - Deleted property: LLM_TOKEN_LIMIT_MONTHLY
          - Deleted property: LLM_TOKEN_LIMIT_WEEKLY
- Security changed
  - New security requirements: waldurPATAuth

GET /api/payment-profiles/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/payment-profiles/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/payment-profiles/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/payment-profiles/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/payment-profiles/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/payment-profiles/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/payment-profiles/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/payment-profiles/{uuid}/enable/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/payments/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/payments/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/payments/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/payments/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/payments/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/payments/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/payments/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/payments/{uuid}/link_to_invoice/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/payments/{uuid}/unlink_from_invoice/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/project-credits/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/project-credits/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/project-credits/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/project-credits/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/project-credits/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/project-credits/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/project-credits/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/project-permissions-reviews/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/project-permissions-reviews/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/project-permissions-reviews/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/project-permissions-reviews/{uuid}/close/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/project-quotas/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/project-quotas/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/project-types/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/project-types/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/project-types/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/projects/

- New query param: created_before
- New query param: modified_before
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_grace_period_days effective_end_date end_date_updated_at is_in_grace_period]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_grace_period_days
              - New property: effective_end_date
              - New property: end_date_updated_at
              - New property: is_in_grace_period
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/projects/

- New query param: created_before
- New query param: modified_before
- Security changed
  - New security requirements: waldurPATAuth

POST /api/projects/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_grace_period_days
            - New property: effective_end_date
            - New property: end_date_updated_at
            - New property: is_in_grace_period
- Security changed
  - New security requirements: waldurPATAuth

GET /api/projects/checklist-template/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/projects/checklist-template/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/projects/{project_uuid}/other_users/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/projects/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/projects/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_grace_period_days effective_end_date end_date_updated_at is_in_grace_period]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_grace_period_days
            - New property: effective_end_date
            - New property: end_date_updated_at
            - New property: is_in_grace_period
- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/projects/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_grace_period_days
            - New property: effective_end_date
            - New property: end_date_updated_at
            - New property: is_in_grace_period
- Security changed
  - New security requirements: waldurPATAuth

PUT /api/projects/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_grace_period_days
            - New property: effective_end_date
            - New property: end_date_updated_at
            - New property: is_in_grace_period
- Security changed
  - New security requirements: waldurPATAuth

POST /api/projects/{uuid}/add_user/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/projects/{uuid}/checklist/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/projects/{uuid}/completion_status/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/projects/{uuid}/delete_user/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/projects/{uuid}/list_users/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/projects/{uuid}/move_project/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_grace_period_days
            - New property: effective_end_date
            - New property: end_date_updated_at
            - New property: is_in_grace_period
- Security changed
  - New security requirements: waldurPATAuth

POST /api/projects/{uuid}/recover/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_grace_period_days
            - New property: effective_end_date
            - New property: end_date_updated_at
            - New property: is_in_grace_period
- Security changed
  - New security requirements: waldurPATAuth

GET /api/projects/{uuid}/stats/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/projects/{uuid}/submit_answers/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/projects/{uuid}/sync_user_roles/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/projects/{uuid}/update_user/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/promotions-campaigns/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/promotions-campaigns/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/promotions-campaigns/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/promotions-campaigns/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/promotions-campaigns/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/promotions-campaigns/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/promotions-campaigns/{uuid}/activate/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/promotions-campaigns/{uuid}/orders/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [provider_description]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: provider_description
- Security changed
  - New security requirements: waldurPATAuth

GET /api/promotions-campaigns/{uuid}/resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [project_effective_end_date provider_description]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: project_effective_end_date
              - New property: provider_description
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: provider_description
              - Modified property: offering_components
                - Items changed
                  - Properties changed
                    - New property: max_renewal_duration
                    - New property: min_renewal_duration
                    - New property: prepaid_duration_step
                    - New property: renewal_duration_step
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: provider_description
              - Modified property: project_end_date_requested_by
                - Nullable changed from false to true
- Security changed
  - New security requirements: waldurPATAuth

POST /api/promotions-campaigns/{uuid}/terminate/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/proposal-proposals/

- New query param: slug
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/proposal-proposals/

- New query param: slug
- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-proposals/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/proposal-proposals/checklist-template/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/proposal-proposals/checklist-template/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/proposal-proposals/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/proposal-proposals/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-proposals/{uuid}/add_user/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-proposals/{uuid}/approve/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-proposals/{uuid}/attach_document/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/proposal-proposals/{uuid}/checklist/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/proposal-proposals/{uuid}/checklist_review/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/proposal-proposals/{uuid}/completion_review_status/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/proposal-proposals/{uuid}/completion_status/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-proposals/{uuid}/delete_user/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-proposals/{uuid}/detach_documents/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/proposal-proposals/{uuid}/list_users/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-proposals/{uuid}/reject/

- Security changed
  - New security requirements: waldurPATAuth

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
                            - New property: max_renewal_duration
                            - New property: min_renewal_duration
                            - New property: prepaid_duration_step
                            - New property: renewal_duration_step
                      - Modified property: plan_details
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/BasePublicPlan
                            - Properties changed
                              - Modified property: components
                                - Items changed
                                  - Properties changed
                                    - New property: discount_description
                                    - New property: discounted_price
- Security changed
  - New security requirements: waldurPATAuth

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
                          - New property: max_renewal_duration
                          - New property: min_renewal_duration
                          - New property: prepaid_duration_step
                          - New property: renewal_duration_step
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: components
                              - Items changed
                                - Properties changed
                                  - New property: discount_description
                                  - New property: discounted_price
- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Security changed
  - New security requirements: waldurPATAuth

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
                          - New property: max_renewal_duration
                          - New property: min_renewal_duration
                          - New property: prepaid_duration_step
                          - New property: renewal_duration_step
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: components
                              - Items changed
                                - Properties changed
                                  - New property: discount_description
                                  - New property: discounted_price
- Security changed
  - New security requirements: waldurPATAuth

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
                          - New property: max_renewal_duration
                          - New property: min_renewal_duration
                          - New property: prepaid_duration_step
                          - New property: renewal_duration_step
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: components
                              - Items changed
                                - Properties changed
                                  - New property: discount_description
                                  - New property: discounted_price
- Security changed
  - New security requirements: waldurPATAuth

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
                          - New property: max_renewal_duration
                          - New property: min_renewal_duration
                          - New property: prepaid_duration_step
                          - New property: renewal_duration_step
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: components
                              - Items changed
                                - Properties changed
                                  - New property: discount_description
                                  - New property: discounted_price
- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-proposals/{uuid}/submit/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-proposals/{uuid}/submit_answers/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-proposals/{uuid}/update_project_details/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-proposals/{uuid}/update_user/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/proposal-protected-calls/

- New query param: slug
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
                          - New property: max_renewal_duration
                          - New property: min_renewal_duration
                          - New property: prepaid_duration_step
                          - New property: renewal_duration_step
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: components
                              - Items changed
                                - Properties changed
                                  - New property: discount_description
                                  - New property: discounted_price
              - Modified property: resource_templates
                - Items changed
                  - Properties changed
                    - Modified property: requested_offering_plan
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: components
                              - Items changed
                                - Properties changed
                                  - New property: discount_description
                                  - New property: discounted_price
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/proposal-protected-calls/

- New query param: slug
- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-protected-calls/

- Responses changed
  - Modified response: 201
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
                        - New property: max_renewal_duration
                        - New property: min_renewal_duration
                        - New property: prepaid_duration_step
                        - New property: renewal_duration_step
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: discount_description
                                - New property: discounted_price
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: discount_description
                                - New property: discounted_price
- Security changed
  - New security requirements: waldurPATAuth

GET /api/proposal-protected-calls/available_compliance_checklists/

- New query param: slug
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/proposal-protected-calls/available_compliance_checklists/

- New query param: slug
- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/proposal-protected-calls/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

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
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: max_renewal_duration
                        - New property: min_renewal_duration
                        - New property: prepaid_duration_step
                        - New property: renewal_duration_step
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: discount_description
                                - New property: discounted_price
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: discount_description
                                - New property: discounted_price
- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/proposal-protected-calls/{uuid}/

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
                        - New property: max_renewal_duration
                        - New property: min_renewal_duration
                        - New property: prepaid_duration_step
                        - New property: renewal_duration_step
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: discount_description
                                - New property: discounted_price
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: discount_description
                                - New property: discounted_price
- Security changed
  - New security requirements: waldurPATAuth

PUT /api/proposal-protected-calls/{uuid}/

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
                        - New property: max_renewal_duration
                        - New property: min_renewal_duration
                        - New property: prepaid_duration_step
                        - New property: renewal_duration_step
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: discount_description
                                - New property: discounted_price
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: discount_description
                                - New property: discounted_price
- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-protected-calls/{uuid}/activate/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-protected-calls/{uuid}/add_user/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/proposal-protected-calls/{uuid}/affinity-matrix/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/proposal-protected-calls/{uuid}/applicant_attribute_config/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-protected-calls/{uuid}/archive/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-protected-calls/{uuid}/attach_documents/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/proposal-protected-calls/{uuid}/coi-configuration/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/proposal-protected-calls/{uuid}/coi-configuration/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/proposal-protected-calls/{uuid}/compliance_overview/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-protected-calls/{uuid}/compute-affinities/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/proposal-protected-calls/{uuid}/conflict-summary/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/proposal-protected-calls/{uuid}/conflicts/

- New query param: slug
- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-protected-calls/{uuid}/create-manual-assignment/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/proposal-protected-calls/{uuid}/delete_applicant_attribute_config/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-protected-calls/{uuid}/delete_user/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-protected-calls/{uuid}/detach_documents/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-protected-calls/{uuid}/detect-conflicts/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-protected-calls/{uuid}/generate-assignments/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-protected-calls/{uuid}/generate-suggestions/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-protected-calls/{uuid}/invite-by-email/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: invitation_link
            - New required property: overridden_at
            - New required property: overridden_by_name
            - New required property: override_reason
            - Deleted required property: invitation_token
          - Properties changed
            - New property: invitation_link
            - New property: overridden_at
            - New property: overridden_by_name
            - New property: override_reason
            - Deleted property: invitation_token
- Security changed
  - New security requirements: waldurPATAuth

GET /api/proposal-protected-calls/{uuid}/list_users/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/proposal-protected-calls/{uuid}/matching-configuration/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/proposal-protected-calls/{uuid}/matching-configuration/

- Security changed
  - New security requirements: waldurPATAuth

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
                    - New property: max_renewal_duration
                    - New property: min_renewal_duration
                    - New property: prepaid_duration_step
                    - New property: renewal_duration_step
              - Modified property: plan_details
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/BasePublicPlan
                    - Properties changed
                      - Modified property: components
                        - Items changed
                          - Properties changed
                            - New property: discount_description
                            - New property: discounted_price
- Security changed
  - New security requirements: waldurPATAuth

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
                  - New property: max_renewal_duration
                  - New property: min_renewal_duration
                  - New property: prepaid_duration_step
                  - New property: renewal_duration_step
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: discount_description
                          - New property: discounted_price
- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Security changed
  - New security requirements: waldurPATAuth

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
                  - New property: max_renewal_duration
                  - New property: min_renewal_duration
                  - New property: prepaid_duration_step
                  - New property: renewal_duration_step
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: discount_description
                          - New property: discounted_price
- Security changed
  - New security requirements: waldurPATAuth

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
                  - New property: max_renewal_duration
                  - New property: min_renewal_duration
                  - New property: prepaid_duration_step
                  - New property: renewal_duration_step
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: discount_description
                          - New property: discounted_price
- Security changed
  - New security requirements: waldurPATAuth

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
                  - New property: max_renewal_duration
                  - New property: min_renewal_duration
                  - New property: prepaid_duration_step
                  - New property: renewal_duration_step
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: discount_description
                          - New property: discounted_price
- Security changed
  - New security requirements: waldurPATAuth

GET /api/proposal-protected-calls/{uuid}/proposals/{proposal_uuid}/compliance-answers/

- New query param: slug
- Security changed
  - New security requirements: waldurPATAuth

GET /api/proposal-protected-calls/{uuid}/proposed-assignments/

- New query param: slug
- Security changed
  - New security requirements: waldurPATAuth

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
                      - Modified property: components
                        - Items changed
                          - Properties changed
                            - New property: discount_description
                            - New property: discounted_price
- Security changed
  - New security requirements: waldurPATAuth

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
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: discount_description
                          - New property: discounted_price
- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/

- Security changed
  - New security requirements: waldurPATAuth

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
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: discount_description
                          - New property: discounted_price
- Security changed
  - New security requirements: waldurPATAuth

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
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: discount_description
                          - New property: discounted_price
- Security changed
  - New security requirements: waldurPATAuth

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
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: discount_description
                          - New property: discounted_price
- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-protected-calls/{uuid}/review_proposal_compliance/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/proposal-protected-calls/{uuid}/reviewer-pool/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: invitation_link
              - New required property: overridden_at
              - New required property: overridden_by_name
              - New required property: override_reason
              - Deleted required property: invitation_token
            - Properties changed
              - New property: invitation_link
              - New property: overridden_at
              - New property: overridden_by_name
              - New property: override_reason
              - Deleted property: invitation_token
- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-protected-calls/{uuid}/reviewer-pool/

- New query param: slug
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: invitation_link
              - New required property: overridden_at
              - New required property: overridden_by_name
              - New required property: override_reason
              - Deleted required property: invitation_token
            - Properties changed
              - New property: invitation_link
              - New property: overridden_at
              - New property: overridden_by_name
              - New property: override_reason
              - Deleted property: invitation_token
- Security changed
  - New security requirements: waldurPATAuth

GET /api/proposal-protected-calls/{uuid}/rounds/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-protected-calls/{uuid}/rounds/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/close/

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
                        - New property: max_renewal_duration
                        - New property: min_renewal_duration
                        - New property: prepaid_duration_step
                        - New property: renewal_duration_step
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: discount_description
                                - New property: discounted_price
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: discount_description
                                - New property: discounted_price
- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-protected-calls/{uuid}/send-all-assignments/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-protected-calls/{uuid}/send-invitations/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/proposal-protected-calls/{uuid}/suggestions/

- New query param: slug
- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/proposal-protected-calls/{uuid}/update_applicant_attribute_config/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-protected-calls/{uuid}/update_applicant_attribute_config/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-protected-calls/{uuid}/update_user/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/proposal-public-calls/

- New query param: slug
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
                          - New property: max_renewal_duration
                          - New property: min_renewal_duration
                          - New property: prepaid_duration_step
                          - New property: renewal_duration_step
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: components
                              - Items changed
                                - Properties changed
                                  - New property: discount_description
                                  - New property: discounted_price
              - Modified property: resource_templates
                - Items changed
                  - Properties changed
                    - Modified property: requested_offering_plan
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: components
                              - Items changed
                                - Properties changed
                                  - New property: discount_description
                                  - New property: discounted_price
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/proposal-public-calls/

- New query param: slug
- Security changed
  - New security requirements: waldurPATAuth

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
                        - New property: max_renewal_duration
                        - New property: min_renewal_duration
                        - New property: prepaid_duration_step
                        - New property: renewal_duration_step
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: discount_description
                                - New property: discounted_price
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: discount_description
                                - New property: discounted_price
- Security changed
  - New security requirements: waldurPATAuth

GET /api/proposal-public-calls/{uuid}/check_eligibility/

- Security changed
  - New security requirements: waldurPATAuth

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
                    - New property: max_renewal_duration
                    - New property: min_renewal_duration
                    - New property: prepaid_duration_step
                    - New property: renewal_duration_step
              - Modified property: plan_details
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/BasePublicPlan
                    - Properties changed
                      - Modified property: components
                        - Items changed
                          - Properties changed
                            - New property: discount_description
                            - New property: discounted_price
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/proposal-requested-offerings/

- Security changed
  - New security requirements: waldurPATAuth

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
                  - New property: max_renewal_duration
                  - New property: min_renewal_duration
                  - New property: prepaid_duration_step
                  - New property: renewal_duration_step
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: discount_description
                          - New property: discounted_price
- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-requested-offerings/{uuid}/accept/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-requested-offerings/{uuid}/cancel/

- Security changed
  - New security requirements: waldurPATAuth

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
                            - New property: max_renewal_duration
                            - New property: min_renewal_duration
                            - New property: prepaid_duration_step
                            - New property: renewal_duration_step
                      - Modified property: plan_details
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/BasePublicPlan
                            - Properties changed
                              - Modified property: components
                                - Items changed
                                  - Properties changed
                                    - New property: discount_description
                                    - New property: discounted_price
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/proposal-requested-resources/

- Security changed
  - New security requirements: waldurPATAuth

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
                          - New property: max_renewal_duration
                          - New property: min_renewal_duration
                          - New property: prepaid_duration_step
                          - New property: renewal_duration_step
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: components
                              - Items changed
                                - Properties changed
                                  - New property: discount_description
                                  - New property: discounted_price
- Security changed
  - New security requirements: waldurPATAuth

GET /api/proposal-reviews/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/proposal-reviews/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-reviews/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/proposal-reviews/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/proposal-reviews/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/proposal-reviews/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/proposal-reviews/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-reviews/{uuid}/reject/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/proposal-reviews/{uuid}/submit/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/provider-invoice-items/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/provider-invoice-items/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/provider-invoice-items/{id}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/public-maintenance-announcements/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/public-maintenance-announcements/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/public-maintenance-announcements/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/query/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rabbitmq-overview/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rabbitmq-stats/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rabbitmq-stats/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rabbitmq-user-stats/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rabbitmq-vhost-stats/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-apps/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/rancher-apps/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-apps/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/rancher-apps/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-apps/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/rancher-apps/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/rancher-apps/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-apps/{uuid}/pull/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-apps/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-apps/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-apps/{uuid}/unlink/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-catalogs/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/rancher-catalogs/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-catalogs/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/rancher-catalogs/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-catalogs/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/rancher-catalogs/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/rancher-catalogs/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-catalogs/{uuid}/refresh/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-cluster-security-groups/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/rancher-cluster-security-groups/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-cluster-security-groups/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/rancher-cluster-security-groups/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/rancher-cluster-security-groups/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-cluster-templates/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/rancher-cluster-templates/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-cluster-templates/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-clusters/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/rancher-clusters/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-clusters/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/rancher-clusters/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/rancher-clusters/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-clusters/{uuid}/create_management_security_group/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-clusters/{uuid}/import_yaml/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-clusters/{uuid}/pull/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-clusters/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-clusters/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-clusters/{uuid}/unlink/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-hpas/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/rancher-hpas/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-hpas/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/rancher-hpas/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-hpas/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/rancher-hpas/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/rancher-hpas/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-hpas/{uuid}/pull/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-hpas/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-hpas/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-hpas/{uuid}/unlink/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-hpas/{uuid}/yaml/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/rancher-hpas/{uuid}/yaml/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-ingresses/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/rancher-ingresses/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-ingresses/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/rancher-ingresses/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-ingresses/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/rancher-ingresses/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/rancher-ingresses/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-ingresses/{uuid}/pull/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-ingresses/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-ingresses/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-ingresses/{uuid}/unlink/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-ingresses/{uuid}/yaml/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/rancher-ingresses/{uuid}/yaml/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-namespaces/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/rancher-namespaces/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-namespaces/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-nodes/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/rancher-nodes/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-nodes/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/rancher-nodes/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-nodes/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-nodes/{uuid}/console/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-nodes/{uuid}/console_log/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-nodes/{uuid}/link_openstack/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-nodes/{uuid}/pull/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-nodes/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-nodes/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-nodes/{uuid}/unlink/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-nodes/{uuid}/unlink_openstack/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-projects/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/rancher-projects/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-projects/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-projects/{uuid}/secrets/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-role-templates/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/rancher-role-templates/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-role-templates/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-services/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/rancher-services/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-services/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/rancher-services/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-services/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/rancher-services/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/rancher-services/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-services/{uuid}/pull/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-services/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-services/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-services/{uuid}/unlink/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-services/{uuid}/yaml/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/rancher-services/{uuid}/yaml/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-template-versions/{template_uuid}/{version}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-templates/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/rancher-templates/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-templates/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-users/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/rancher-users/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-users/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-workloads/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/rancher-workloads/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-workloads/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/rancher-workloads/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-workloads/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/rancher-workloads/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/rancher-workloads/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/rancher-workloads/{uuid}/redeploy/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/rancher-workloads/{uuid}/yaml/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/rancher-workloads/{uuid}/yaml/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/remote-eduteams/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/remote-waldur-api/cancel_termination/{uuid}

- Security changed
  - New security requirements: waldurPATAuth

POST /api/remote-waldur-api/import_offering/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/remote-waldur-api/pull_offering_details/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/remote-waldur-api/pull_offering_orders/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/remote-waldur-api/pull_offering_resources/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/remote-waldur-api/pull_offering_robot_accounts/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/remote-waldur-api/pull_offering_usage/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/remote-waldur-api/pull_offering_users/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/remote-waldur-api/pull_order/{uuid}

- Security changed
  - New security requirements: waldurPATAuth

POST /api/remote-waldur-api/pull_resource_robot_accounts/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/remote-waldur-api/push_project_data/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

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
                          - New property: uuid
                          - Modified property: options
                            - Items changed
                              - Properties changed
                                - New property: is_default
                                - New property: uuid
- Security changed
  - New security requirements: waldurPATAuth

POST /api/remote-waldur-api/remote_customers/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/remote-waldur-api/remote_resource_order_status/{resource_uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/remote-waldur-api/remote_resource_status/{resource_uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/remote-waldur-api/remote_resource_team_status/{resource_uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/remote-waldur-api/shared_offerings/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/remote-waldur-api/sync_resource/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/remote-waldur-api/sync_resource_project_permissions/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/reviewer-bids/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/reviewer-bids/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/reviewer-bids/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/reviewer-bids/bulk-submit/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/reviewer-bids/my-bids/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/reviewer-bids/my-bids/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/reviewer-bids/submit/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/reviewer-bids/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/reviewer-bids/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/reviewer-bids/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/reviewer-bids/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/reviewer-invitations/{token}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/reviewer-invitations/{token}/accept/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/reviewer-invitations/{token}/decline/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/reviewer-profiles/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/reviewer-profiles/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/reviewer-profiles/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/reviewer-profiles/me/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/reviewer-profiles/me/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/reviewer-profiles/me/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/reviewer-profiles/me/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/reviewer-profiles/publish/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/reviewer-profiles/unpublish/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/reviewer-profiles/{reviewer_profile_uuid}/affiliations/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/reviewer-profiles/{reviewer_profile_uuid}/affiliations/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/reviewer-profiles/{reviewer_profile_uuid}/affiliations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/reviewer-profiles/{reviewer_profile_uuid}/affiliations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/reviewer-profiles/{reviewer_profile_uuid}/affiliations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/reviewer-profiles/{reviewer_profile_uuid}/affiliations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/reviewer-profiles/{reviewer_profile_uuid}/expertise/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/reviewer-profiles/{reviewer_profile_uuid}/expertise/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/reviewer-profiles/{reviewer_profile_uuid}/expertise/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/reviewer-profiles/{reviewer_profile_uuid}/expertise/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/reviewer-profiles/{reviewer_profile_uuid}/expertise/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/reviewer-profiles/{reviewer_profile_uuid}/expertise/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/reviewer-profiles/{reviewer_profile_uuid}/publications/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/reviewer-profiles/{reviewer_profile_uuid}/publications/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/reviewer-profiles/{reviewer_profile_uuid}/publications/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/reviewer-profiles/{reviewer_profile_uuid}/publications/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/reviewer-profiles/{reviewer_profile_uuid}/publications/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/reviewer-profiles/{reviewer_profile_uuid}/publications/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/reviewer-profiles/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/reviewer-profiles/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/reviewer-profiles/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/reviewer-profiles/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/reviewer-profiles/{uuid}/connect-orcid/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/reviewer-profiles/{uuid}/connect-orcid/callback/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/reviewer-profiles/{uuid}/disconnect-orcid/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/reviewer-profiles/{uuid}/import-publications/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/reviewer-profiles/{uuid}/sync-orcid/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/reviewer-suggestions/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/reviewer-suggestions/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/reviewer-suggestions/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/reviewer-suggestions/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/reviewer-suggestions/{uuid}/confirm/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/reviewer-suggestions/{uuid}/reject/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/roles/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/roles/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/roles/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/roles/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/roles/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/roles/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/roles/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/roles/{uuid}/disable/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/roles/{uuid}/enable/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/roles/{uuid}/update_descriptions/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/service-settings/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/service-settings/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/service-settings/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/slurm-allocation-user-usage/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/slurm-allocation-user-usage/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/slurm-allocation-user-usage/{id}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/slurm-allocations/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/slurm-allocations/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/slurm-allocations/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/slurm-allocations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/slurm-allocations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/slurm-allocations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/slurm-allocations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/slurm-allocations/{uuid}/pull/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/slurm-allocations/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/slurm-allocations/{uuid}/set_limits/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/slurm-allocations/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/slurm-allocations/{uuid}/unlink/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/slurm-associations/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/slurm-associations/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/slurm-associations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/slurm-jobs/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/slurm-jobs/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/slurm-jobs/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/slurm-jobs/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/slurm-jobs/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/slurm-jobs/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/slurm-jobs/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/slurm-jobs/{uuid}/pull/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/slurm-jobs/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/slurm-jobs/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/slurm-jobs/{uuid}/unlink/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/stats/celery/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/stats/database/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/stats/query/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/stats/table-growth/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/stats/table-growth/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/support-attachments/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/support-attachments/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/support-attachments/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/support-attachments/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/support-attachments/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/support-comments/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/support-comments/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/support-comments/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/support-comments/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/support-comments/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/support-comments/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/support-feedback-average-report/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/support-feedback-report/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/support-feedbacks/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/support-feedbacks/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/support-feedbacks/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/support-feedbacks/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/support-issue-statuses/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/support-issue-statuses/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/support-issue-statuses/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/support-issue-statuses/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/support-issue-statuses/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/support-issue-statuses/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/support-issue-statuses/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/support-issues/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/support-issues/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/support-issues/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/support-issues/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/support-issues/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/support-issues/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/support-issues/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/support-issues/{uuid}/comment/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/support-issues/{uuid}/sync/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/support-priorities/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/support-priorities/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/support-priorities/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/support-request-types-admin/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/support-request-types-admin/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/support-request-types-admin/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/support-request-types-admin/reorder/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/support-request-types-admin/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/support-request-types-admin/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/support-request-types-admin/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/support-request-types-admin/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/support-request-types-admin/{uuid}/activate/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/support-request-types-admin/{uuid}/deactivate/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/support-request-types/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/support-request-types/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/support-request-types/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/support-statistics/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/support-templates/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/support-templates/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/support-templates/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/support-templates/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/support-templates/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/support-templates/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/support-templates/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/support-templates/{uuid}/create_attachments/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/support-templates/{uuid}/delete_attachments/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/support-users/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/support-users/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/support-users/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/support/settings/atlassian/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/support/settings/atlassian/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/support/settings/atlassian/current_settings/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/support/settings/atlassian/discover_custom_fields/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/support/settings/atlassian/discover_priorities/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/support/settings/atlassian/discover_projects/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/support/settings/atlassian/discover_request_types/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/support/settings/atlassian/preview_settings/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/support/settings/atlassian/save_settings/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/support/settings/atlassian/validate_credentials/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/support/settings/atlassian/{id}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/support/settings/atlassian/{id}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/support/settings/atlassian/{id}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/support/settings/atlassian/{id}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/sync-issues/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/sync-issues/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/system-logs/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/system-logs/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/system-logs/instances/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/system-logs/instances/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/system-logs/stats/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/system-logs/stats/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/system-logs/{id}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/user-action-executions/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/user-action-executions/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/user-action-executions/{id}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/user-action-providers/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/user-action-providers/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/user-action-providers/{id}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/user-actions/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/user-actions/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/user-actions/bulk_silence/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/user-actions/summary/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/user-actions/summary/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/user-actions/update_actions/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/user-actions/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/user-actions/{uuid}/execute_action/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/user-actions/{uuid}/silence/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/user-actions/{uuid}/unsilence/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/user-agreements/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/user-agreements/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/user-agreements/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/user-agreements/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/user-agreements/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/user-agreements/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/user-agreements/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/user-group-invitations/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: allow_custom_project_details
              - New property: allow_multiple_requests
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/user-group-invitations/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/user-group-invitations/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: allow_custom_project_details
          - New property: allow_multiple_requests
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: allow_custom_project_details
            - New property: allow_multiple_requests
- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/user-group-invitations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/user-group-invitations/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: allow_custom_project_details
            - New property: allow_multiple_requests
- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/user-group-invitations/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: allow_custom_project_details
          - New property: allow_multiple_requests
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: allow_custom_project_details
            - New property: allow_multiple_requests
- Security changed
  - New security requirements: waldurPATAuth

PUT /api/user-group-invitations/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: allow_custom_project_details
          - New property: allow_multiple_requests
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: allow_custom_project_details
            - New property: allow_multiple_requests
- Security changed
  - New security requirements: waldurPATAuth

POST /api/user-group-invitations/{uuid}/cancel/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/user-group-invitations/{uuid}/projects/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/user-group-invitations/{uuid}/submit_request/

- Request body changed
- Security changed
  - New security requirements: waldurPATAuth

GET /api/user-invitations/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/user-invitations/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/user-invitations/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/user-invitations/approve/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/user-invitations/check-duplicates/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/user-invitations/reject/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/user-invitations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/user-invitations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/user-invitations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/user-invitations/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/user-invitations/{uuid}/accept/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/user-invitations/{uuid}/cancel/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/user-invitations/{uuid}/check/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/user-invitations/{uuid}/delete/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/user-invitations/{uuid}/details/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/user-invitations/{uuid}/send/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/user-permission-requests/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: project_description
              - New property: project_name
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/user-permission-requests/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/user-permission-requests/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/user-permission-requests/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: project_description
            - New property: project_name
- Security changed
  - New security requirements: waldurPATAuth

POST /api/user-permission-requests/{uuid}/approve/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/user-permission-requests/{uuid}/cancel_request/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/user-permission-requests/{uuid}/reject/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/user-permissions/

- New query param: created_before
- New query param: modified_before
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/user-permissions/

- New query param: created_before
- New query param: modified_before
- Security changed
  - New security requirements: waldurPATAuth

GET /api/user-permissions/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [deactivation_reason]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: deactivation_reason
              - Modified property: gender
                - Property 'OneOf' changed
                  - Schemas added: #/components/schemas/BlankEnum
                  - Modified schema: #/components/schemas/GenderEnum
                    - Type changed from 'integer' to 'string'
                    - New enum values: [male female unknown]
                    - Deleted enum values: [0 1 2 9]
                - Description changed from 'ISO 5218 gender code' to 'User's gender (male, female, or unknown)'
                - Min changed from 0 to null
                - Max changed from 32767 to null
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/users/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/users/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: deactivation_reason
          - Modified property: gender
            - Property 'OneOf' changed
              - Schemas added: #/components/schemas/BlankEnum
              - Modified schema: #/components/schemas/GenderEnum
                - Type changed from 'integer' to 'string'
                - New enum values: [male female unknown]
                - Deleted enum values: [0 1 2 9]
            - Description changed from 'ISO 5218 gender code' to 'User's gender (male, female, or unknown)'
            - Min changed from 0 to null
            - Max changed from 32767 to null
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: deactivation_reason
          - Modified property: gender
            - Property 'OneOf' changed
              - Schemas added: #/components/schemas/BlankEnum
              - Modified schema: #/components/schemas/GenderEnum
                - Type changed from 'integer' to 'string'
                - New enum values: [male female unknown]
                - Deleted enum values: [0 1 2 9]
            - Description changed from 'ISO 5218 gender code' to 'User's gender (male, female, or unknown)'
            - Min changed from 0 to null
            - Max changed from 32767 to null
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: deactivation_reason
          - Modified property: gender
            - Property 'OneOf' changed
              - Schemas added: #/components/schemas/BlankEnum
              - Modified schema: #/components/schemas/GenderEnum
                - Type changed from 'integer' to 'string'
                - New enum values: [male female unknown]
                - Deleted enum values: [0 1 2 9]
            - Description changed from 'ISO 5218 gender code' to 'User's gender (male, female, or unknown)'
            - Min changed from 0 to null
            - Max changed from 32767 to null
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: deactivation_reason
            - Modified property: gender
              - Property 'OneOf' changed
                - Schemas added: #/components/schemas/BlankEnum
                - Modified schema: #/components/schemas/GenderEnum
                  - Type changed from 'integer' to 'string'
                  - New enum values: [male female unknown]
                  - Deleted enum values: [0 1 2 9]
              - Description changed from 'ISO 5218 gender code' to 'User's gender (male, female, or unknown)'
              - Min changed from 0 to null
              - Max changed from 32767 to null
- Security changed
  - New security requirements: waldurPATAuth

POST /api/users/confirm_email/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/users/me/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [deactivation_reason]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: deactivation_reason
            - Modified property: gender
              - Property 'OneOf' changed
                - Schemas added: #/components/schemas/BlankEnum
                - Modified schema: #/components/schemas/GenderEnum
                  - Type changed from 'integer' to 'string'
                  - New enum values: [male female unknown]
                  - Deleted enum values: [0 1 2 9]
              - Description changed from 'ISO 5218 gender code' to 'User's gender (male, female, or unknown)'
              - Min changed from 0 to null
              - Max changed from 32767 to null
- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/users/me/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/users/profile_completeness/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/users/profile_completeness/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/users/scim_sync_all/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/users/user_active_status_count/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/users/user_active_status_count/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/users/user_language_count/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/users/user_language_count/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/users/user_registration_trend/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/users/user_registration_trend/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/users/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/users/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [deactivation_reason]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: deactivation_reason
            - Modified property: gender
              - Property 'OneOf' changed
                - Schemas added: #/components/schemas/BlankEnum
                - Modified schema: #/components/schemas/GenderEnum
                  - Type changed from 'integer' to 'string'
                  - New enum values: [male female unknown]
                  - Deleted enum values: [0 1 2 9]
              - Description changed from 'ISO 5218 gender code' to 'User's gender (male, female, or unknown)'
              - Min changed from 0 to null
              - Max changed from 32767 to null
- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/users/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: deactivation_reason
          - Modified property: gender
            - Property 'OneOf' changed
              - Schemas added: #/components/schemas/BlankEnum
              - Modified schema: #/components/schemas/GenderEnum
                - Type changed from 'integer' to 'string'
                - New enum values: [male female unknown]
                - Deleted enum values: [0 1 2 9]
            - Description changed from 'ISO 5218 gender code' to 'User's gender (male, female, or unknown)'
            - Min changed from 0 to null
            - Max changed from 32767 to null
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: deactivation_reason
          - Modified property: gender
            - Property 'OneOf' changed
              - Schemas added: #/components/schemas/BlankEnum
              - Modified schema: #/components/schemas/GenderEnum
                - Type changed from 'integer' to 'string'
                - New enum values: [male female unknown]
                - Deleted enum values: [0 1 2 9]
            - Description changed from 'ISO 5218 gender code' to 'User's gender (male, female, or unknown)'
            - Min changed from 0 to null
            - Max changed from 32767 to null
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: deactivation_reason
          - Modified property: gender
            - Property 'OneOf' changed
              - Schemas added: #/components/schemas/BlankEnum
              - Modified schema: #/components/schemas/GenderEnum
                - Type changed from 'integer' to 'string'
                - New enum values: [male female unknown]
                - Deleted enum values: [0 1 2 9]
            - Description changed from 'ISO 5218 gender code' to 'User's gender (male, female, or unknown)'
            - Min changed from 0 to null
            - Max changed from 32767 to null
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: deactivation_reason
            - Modified property: gender
              - Property 'OneOf' changed
                - Schemas added: #/components/schemas/BlankEnum
                - Modified schema: #/components/schemas/GenderEnum
                  - Type changed from 'integer' to 'string'
                  - New enum values: [male female unknown]
                  - Deleted enum values: [0 1 2 9]
              - Description changed from 'ISO 5218 gender code' to 'User's gender (male, female, or unknown)'
              - Min changed from 0 to null
              - Max changed from 32767 to null
- Security changed
  - New security requirements: waldurPATAuth

PUT /api/users/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: deactivation_reason
          - Modified property: gender
            - Property 'OneOf' changed
              - Schemas added: #/components/schemas/BlankEnum
              - Modified schema: #/components/schemas/GenderEnum
                - Type changed from 'integer' to 'string'
                - New enum values: [male female unknown]
                - Deleted enum values: [0 1 2 9]
            - Description changed from 'ISO 5218 gender code' to 'User's gender (male, female, or unknown)'
            - Min changed from 0 to null
            - Max changed from 32767 to null
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: deactivation_reason
          - Modified property: gender
            - Property 'OneOf' changed
              - Schemas added: #/components/schemas/BlankEnum
              - Modified schema: #/components/schemas/GenderEnum
                - Type changed from 'integer' to 'string'
                - New enum values: [male female unknown]
                - Deleted enum values: [0 1 2 9]
            - Description changed from 'ISO 5218 gender code' to 'User's gender (male, female, or unknown)'
            - Min changed from 0 to null
            - Max changed from 32767 to null
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: deactivation_reason
          - Modified property: gender
            - Property 'OneOf' changed
              - Schemas added: #/components/schemas/BlankEnum
              - Modified schema: #/components/schemas/GenderEnum
                - Type changed from 'integer' to 'string'
                - New enum values: [male female unknown]
                - Deleted enum values: [0 1 2 9]
            - Description changed from 'ISO 5218 gender code' to 'User's gender (male, female, or unknown)'
            - Min changed from 0 to null
            - Max changed from 32767 to null
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: deactivation_reason
            - Modified property: gender
              - Property 'OneOf' changed
                - Schemas added: #/components/schemas/BlankEnum
                - Modified schema: #/components/schemas/GenderEnum
                  - Type changed from 'integer' to 'string'
                  - New enum values: [male female unknown]
                  - Deleted enum values: [0 1 2 9]
              - Description changed from 'ISO 5218 gender code' to 'User's gender (male, female, or unknown)'
              - Min changed from 0 to null
              - Max changed from 32767 to null
- Security changed
  - New security requirements: waldurPATAuth

POST /api/users/{uuid}/cancel_change_email/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/users/{uuid}/change_email/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/users/{uuid}/change_password/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/users/{uuid}/data_access/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/users/{uuid}/data_access_history/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/users/{uuid}/history/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/users/{uuid}/history/at/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/users/{uuid}/identity_bridge_status/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/users/{uuid}/pull_remote_user/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/users/{uuid}/refresh_token/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/users/{uuid}/remove_password/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/users/{uuid}/send_notification/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/users/{uuid}/token/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/users/{uuid}/update_actions/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/version/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/vmware-clusters/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/vmware-clusters/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/vmware-clusters/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/vmware-datastores/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/vmware-datastores/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/vmware-datastores/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/vmware-disks/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/vmware-disks/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/vmware-disks/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/vmware-disks/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/vmware-disks/{uuid}/extend/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/vmware-disks/{uuid}/pull/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/vmware-disks/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/vmware-disks/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/vmware-disks/{uuid}/unlink/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/vmware-folders/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/vmware-folders/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/vmware-folders/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/vmware-limits/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/vmware-networks/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/vmware-networks/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/vmware-networks/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/vmware-ports/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/vmware-ports/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/vmware-ports/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/vmware-ports/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/vmware-ports/{uuid}/pull/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/vmware-ports/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/vmware-ports/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/vmware-ports/{uuid}/unlink/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/vmware-templates/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/vmware-templates/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/vmware-templates/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/vmware-virtual-machine/

- Security changed
  - New security requirements: waldurPATAuth

HEAD /api/vmware-virtual-machine/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/vmware-virtual-machine/

- Security changed
  - New security requirements: waldurPATAuth

DELETE /api/vmware-virtual-machine/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/vmware-virtual-machine/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PATCH /api/vmware-virtual-machine/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

PUT /api/vmware-virtual-machine/{uuid}/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/vmware-virtual-machine/{uuid}/console/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/vmware-virtual-machine/{uuid}/create_disk/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/vmware-virtual-machine/{uuid}/create_port/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/vmware-virtual-machine/{uuid}/pull/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/vmware-virtual-machine/{uuid}/reboot_guest/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/vmware-virtual-machine/{uuid}/reset/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/vmware-virtual-machine/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/vmware-virtual-machine/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/vmware-virtual-machine/{uuid}/shutdown_guest/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/vmware-virtual-machine/{uuid}/start/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/vmware-virtual-machine/{uuid}/stop/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/vmware-virtual-machine/{uuid}/suspend/

- Security changed
  - New security requirements: waldurPATAuth

POST /api/vmware-virtual-machine/{uuid}/unlink/

- Security changed
  - New security requirements: waldurPATAuth

GET /api/vmware-virtual-machine/{uuid}/web_console/

- Security changed
  - New security requirements: waldurPATAuth
