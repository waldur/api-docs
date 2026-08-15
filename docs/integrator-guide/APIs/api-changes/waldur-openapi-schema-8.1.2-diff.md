# OpenAPI schema diff - 8.1.2

## For version 8.1.2

### New Endpoints: 234

----------------------
GET /api/access-subnets/resource_impact/  
HEAD /api/access-subnets/resource_impact/  
GET /api/anonymous-chat-interactions/conversations/  
HEAD /api/call-managing-organisations/{uuid}/list_users/  
GET /api/chat-threads/stats/  
GET /api/credit-transactions/  
HEAD /api/credit-transactions/  
GET /api/credit-transactions/{uuid}/  
GET /api/customer-affiliates/  
HEAD /api/customer-affiliates/  
POST /api/customer-affiliates/  
DELETE /api/customer-affiliates/{uuid}/  
GET /api/customer-affiliates/{uuid}/  
PATCH /api/customer-affiliates/{uuid}/  
PUT /api/customer-affiliates/{uuid}/  
GET /api/customer-affiliates/{uuid}/accruals/  
GET /api/customer-affiliates/{uuid}/earnings/  
POST /api/customer-credits/{uuid}/adjust_withdrawable/  
GET /api/customer-role-concealments/  
HEAD /api/customer-role-concealments/  
POST /api/customer-role-concealments/  
DELETE /api/customer-role-concealments/{uuid}/  
GET /api/customer-role-concealments/{uuid}/  
HEAD /api/customers/{customer_uuid}/project-metadata-compliance-details/  
HEAD /api/customers/{customer_uuid}/project-metadata-compliance-overview/  
HEAD /api/customers/{customer_uuid}/project-metadata-compliance-projects/  
HEAD /api/customers/{customer_uuid}/project-metadata-question-answers/  
HEAD /api/customers/{customer_uuid}/users/  
HEAD /api/customers/{uuid}/list_users/  
GET /api/event-consumers/  
HEAD /api/event-consumers/  
POST /api/event-consumers/register/  
DELETE /api/event-consumers/{uuid}/  
GET /api/helpdesk-health/  
GET /api/helpdesk-stats/  
GET /api/marketplace-offering-access-subnets/  
HEAD /api/marketplace-offering-access-subnets/  
POST /api/marketplace-offering-access-subnets/  
DELETE /api/marketplace-offering-access-subnets/{uuid}/  
GET /api/marketplace-offering-access-subnets/{uuid}/  
PATCH /api/marketplace-offering-access-subnets/{uuid}/  
PUT /api/marketplace-offering-access-subnets/{uuid}/  
GET /api/marketplace-offering-users/posix_identities/  
HEAD /api/marketplace-offering-users/posix_identities/  
GET /api/marketplace-offering-users/{uuid}/posix_allocations/  
GET /api/marketplace-offering-users/{uuid}/posix_groups/  
POST /api/marketplace-offering-users/{uuid}/set_posix_attributes/  
GET /api/marketplace-openstack-duplicate-offerings/  
HEAD /api/marketplace-openstack-duplicate-offerings/  
POST /api/marketplace-openstack-duplicate-offerings/remediate/  
GET /api/marketplace-posix-id-pools/  
HEAD /api/marketplace-posix-id-pools/  
POST /api/marketplace-posix-id-pools/  
DELETE /api/marketplace-posix-id-pools/{uuid}/  
GET /api/marketplace-posix-id-pools/{uuid}/  
PATCH /api/marketplace-posix-id-pools/{uuid}/  
PUT /api/marketplace-posix-id-pools/{uuid}/  
GET /api/marketplace-posix-id-pools/{uuid}/stats/  
GET /api/marketplace-posix-identities/  
HEAD /api/marketplace-posix-identities/  
GET /api/marketplace-posix-identities/{uuid}/  
GET /api/marketplace-project-posix-groups/  
HEAD /api/marketplace-project-posix-groups/  
GET /api/marketplace-provider-offerings/aggregated_access_subnets/  
HEAD /api/marketplace-provider-offerings/aggregated_access_subnets/  
GET /api/marketplace-provider-offerings/{uuid}/access_subnets/  
POST /api/marketplace-provider-offerings/{uuid}/add_qos/  
GET /api/marketplace-provider-offerings/{uuid}/effective_posix_id_pool/  
HEAD /api/marketplace-provider-offerings/{uuid}/list_users/  
POST /api/marketplace-provider-offerings/{uuid}/remove_qos/  
POST /api/marketplace-provider-offerings/{uuid}/set_partition_qos/  
PATCH /api/marketplace-provider-offerings/{uuid}/update_qos/  
HEAD /api/marketplace-provider-resource-projects/{uuid}/list_users/  
HEAD /api/marketplace-provider-resources/{uuid}/list_users/  
POST /api/marketplace-provider-resources/{uuid}/set_membership_sync_statuses/  
POST /api/marketplace-provider-resources/{uuid}/sync_user_roles/  
GET /api/marketplace-resource-api-keys/  
HEAD /api/marketplace-resource-api-keys/  
POST /api/marketplace-resource-api-keys/report_created/  
GET /api/marketplace-resource-api-keys/{uuid}/  
GET /api/marketplace-resource-api-keys/{uuid}/reveal/  
POST /api/marketplace-resource-api-keys/{uuid}/rotate/  
POST /api/marketplace-resource-api-keys/{uuid}/set_erred/  
POST /api/marketplace-resource-api-keys/{uuid}/set_key/  
GET /api/marketplace-resource-end-date-change-requests/  
HEAD /api/marketplace-resource-end-date-change-requests/  
POST /api/marketplace-resource-end-date-change-requests/  
GET /api/marketplace-resource-end-date-change-requests/{uuid}/  
POST /api/marketplace-resource-end-date-change-requests/{uuid}/approve/  
POST /api/marketplace-resource-end-date-change-requests/{uuid}/cancel/  
POST /api/marketplace-resource-end-date-change-requests/{uuid}/reject/  
POST /api/marketplace-resource-end-date-change-requests/{uuid}/set_backend_id/  
HEAD /api/marketplace-resource-projects/{uuid}/list_users/  
HEAD /api/marketplace-resources/{uuid}/list_users/  
HEAD /api/marketplace-service-providers/{service_provider_uuid}/compliance/checklists_summary/  
HEAD /api/marketplace-service-providers/{service_provider_uuid}/compliance/compliance_overview/  
HEAD /api/marketplace-service-providers/{service_provider_uuid}/compliance/offering_users/  
HEAD /api/marketplace-service-providers/{service_provider_uuid}/course_accounts/  
HEAD /api/marketplace-service-providers/{service_provider_uuid}/customer_projects/  
HEAD /api/marketplace-service-providers/{service_provider_uuid}/customers/  
HEAD /api/marketplace-service-providers/{service_provider_uuid}/keys/  
HEAD /api/marketplace-service-providers/{service_provider_uuid}/offerings/  
HEAD /api/marketplace-service-providers/{service_provider_uuid}/offerings/types/  
HEAD /api/marketplace-service-providers/{service_provider_uuid}/project_permissions/  
HEAD /api/marketplace-service-providers/{service_provider_uuid}/project_service_accounts/  
HEAD /api/marketplace-service-providers/{service_provider_uuid}/projects/  
HEAD /api/marketplace-service-providers/{service_provider_uuid}/user_customers/  
HEAD /api/marketplace-service-providers/{service_provider_uuid}/users/  
HEAD /api/marketplace-service-providers/{uuid}/list_users/  
POST /api/marketplace-site-agent-identities/{uuid}/register_queue/  
GET /api/openportal-managed-project-audit/  
HEAD /api/openportal-managed-project-audit/  
GET /api/openportal-managed-project-audit/{id}/  
POST /api/openportal-managed-projects/{identifier}/{destination}/add-note/  
GET /api/openportal-remote-project-allocations/  
HEAD /api/openportal-remote-project-allocations/  
GET /api/openportal-remote-project-allocations/{id}/  
GET /api/openportal-remote-project-audit/  
HEAD /api/openportal-remote-project-audit/  
GET /api/openportal-remote-project-audit/{id}/  
GET /api/openportal-remote-projects/  
HEAD /api/openportal-remote-projects/  
GET /api/openportal-remote-projects/{uuid}/  
POST /api/openportal-remote-projects/{uuid}/add-note/  
POST /api/openportal-remote-projects/{uuid}/approve-now/  
POST /api/openportal-remote-projects/{uuid}/hold-indefinitely/  
POST /api/openportal-remote-projects/{uuid}/resend-request/  
POST /api/openportal-remote-projects/{uuid}/reset-to-pending/  
POST /api/openportal-remote-projects/{uuid}/set-allowed-domains/  
POST /api/openportal-remote-projects/{uuid}/set-earliest-approve/  
POST /api/openportal-remote-projects/{uuid}/set-links/  
POST /api/openportal-remote-projects/{uuid}/set-membership-control/  
GET /api/openportal-remote-projects/{uuid}/total-usage/  
HEAD /api/openportal-unmanaged-projects/{uuid}/list_users/  
GET /api/openportal/project_email_policy/{project_uuid}/  
POST /api/personal-access-tokens/{uuid}/set_network_acl/  
HEAD /api/projects/{project_uuid}/other_users/  
HEAD /api/projects/{uuid}/list_users/  
GET /api/proposal-my-requested-resources/  
HEAD /api/proposal-my-requested-resources/  
GET /api/proposal-my-requested-resources/{uuid}/  
HEAD /api/proposal-proposals/{uuid}/list_users/  
DELETE /api/proposal-proposals/{uuid}/resources/{obj_uuid}/purchase_order/  
POST /api/proposal-proposals/{uuid}/resources/{obj_uuid}/purchase_order/  
GET /api/proposal-proposals/{uuid}/step-checklist-responses/  
GET /api/proposal-proposals/{uuid}/step-checklist/  
POST /api/proposal-proposals/{uuid}/submit-step-checklist-answers/  
GET /api/proposal-protected-calls/step_checklists/  
HEAD /api/proposal-protected-calls/step_checklists/  
HEAD /api/proposal-protected-calls/{uuid}/list_users/  
GET /api/provider-canned-responses/  
HEAD /api/provider-canned-responses/  
POST /api/provider-canned-responses/  
DELETE /api/provider-canned-responses/{uuid}/  
GET /api/provider-canned-responses/{uuid}/  
PATCH /api/provider-canned-responses/{uuid}/  
PUT /api/provider-canned-responses/{uuid}/  
POST /api/provider-canned-responses/{uuid}/render/  
GET /api/provider-helpdesks/  
HEAD /api/provider-helpdesks/  
POST /api/provider-helpdesks/  
DELETE /api/provider-helpdesks/{uuid}/  
GET /api/provider-helpdesks/{uuid}/  
PATCH /api/provider-helpdesks/{uuid}/  
PUT /api/provider-helpdesks/{uuid}/  
POST /api/provider-helpdesks/{uuid}/validate/  
GET /api/provider-support-users/  
HEAD /api/provider-support-users/  
POST /api/provider-support-users/  
GET /api/provider-support-users/team_workload/  
HEAD /api/provider-support-users/team_workload/  
DELETE /api/provider-support-users/{uuid}/  
GET /api/provider-support-users/{uuid}/  
PATCH /api/provider-support-users/{uuid}/  
PUT /api/provider-support-users/{uuid}/  
GET /api/provider-tickets/  
HEAD /api/provider-tickets/  
GET /api/provider-tickets/stats/  
HEAD /api/provider-tickets/stats/  
GET /api/provider-tickets/{uuid}/  
PATCH /api/provider-tickets/{uuid}/  
PUT /api/provider-tickets/{uuid}/  
POST /api/provider-tickets/{uuid}/assign/  
POST /api/provider-tickets/{uuid}/claim/  
POST /api/provider-tickets/{uuid}/comment/  
GET /api/provider-tickets/{uuid}/customer_context/  
POST /api/provider-tickets/{uuid}/resolve/  
HEAD /api/reviewer-profiles/{reviewer_profile_uuid}/affiliations/  
HEAD /api/reviewer-profiles/{reviewer_profile_uuid}/expertise/  
HEAD /api/reviewer-profiles/{reviewer_profile_uuid}/publications/  
POST /api/roles/{uuid}/clone_to_customer/  
GET /api/support-canned-responses/  
HEAD /api/support-canned-responses/  
POST /api/support-canned-responses/  
DELETE /api/support-canned-responses/{uuid}/  
GET /api/support-canned-responses/{uuid}/  
PATCH /api/support-canned-responses/{uuid}/  
PUT /api/support-canned-responses/{uuid}/  
POST /api/support-canned-responses/{uuid}/render/  
GET /api/support-issue-links/  
HEAD /api/support-issue-links/  
POST /api/support-issue-links/  
DELETE /api/support-issue-links/{uuid}/  
GET /api/support-issue-links/{uuid}/  
PATCH /api/support-issue-links/{uuid}/  
PUT /api/support-issue-links/{uuid}/  
GET /api/support-issue-tags/  
HEAD /api/support-issue-tags/  
POST /api/support-issue-tags/  
DELETE /api/support-issue-tags/{uuid}/  
GET /api/support-issue-tags/{uuid}/  
PATCH /api/support-issue-tags/{uuid}/  
PUT /api/support-issue-tags/{uuid}/  
POST /api/support-issues/bulk_update/  
POST /api/support-issues/{uuid}/attach_resource/  
POST /api/support-issues/{uuid}/escalate/  
POST /api/support-issues/{uuid}/reroute/  
POST /api/support-issues/{uuid}/route_to_provider/  
POST /api/support-provider-webhook/{provider_uuid}/{backend_type}/  
GET /api/support-saved-filters/  
HEAD /api/support-saved-filters/  
POST /api/support-saved-filters/  
DELETE /api/support-saved-filters/{uuid}/  
GET /api/support-saved-filters/{uuid}/  
PATCH /api/support-saved-filters/{uuid}/  
PUT /api/support-saved-filters/{uuid}/  
POST /api/support-users/  
DELETE /api/support-users/{uuid}/  
PATCH /api/support-users/{uuid}/  
PUT /api/support-users/{uuid}/  
GET /api/support-users/{uuid}/connections/  
POST /api/support-users/{uuid}/merge/  
POST /api/user-permissions/{uuid}/restore/  
POST /api/user-permissions/{uuid}/revoke/  

### Deleted Endpoints: 2

------------------------
POST /api/proposal-proposals/{uuid}/approve/  
POST /api/proposal-proposals/{uuid}/reject/  

### Modified Endpoints: 2591

----------------------------
POST /api-auth/logout/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api-auth/password/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api-auth/saml2/providers/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api-auth/token-exchange/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/access-subnets/

- New query param: applies_to_portal
- New query param: is_staff_managed
- New query param: o
- New query param: offering_uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: is_staff_managed
              - New required property: scoped_offerings
            - Properties changed
              - New property: applies_to_portal
              - New property: is_staff_managed
              - New property: offerings
              - New property: scoped_offerings
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/access-subnets/

- New query param: applies_to_portal
- New query param: is_staff_managed
- New query param: o
- New query param: offering_uuid
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/access-subnets/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: applies_to_portal
          - New property: offerings
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: is_staff_managed
            - New required property: scoped_offerings
          - Properties changed
            - New property: applies_to_portal
            - New property: is_staff_managed
            - New property: offerings
            - New property: scoped_offerings
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/access-subnets/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/access-subnets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: is_staff_managed
            - New required property: scoped_offerings
          - Properties changed
            - New property: applies_to_portal
            - New property: is_staff_managed
            - New property: offerings
            - New property: scoped_offerings
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/access-subnets/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: applies_to_portal
          - New property: offerings
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: is_staff_managed
            - New required property: scoped_offerings
          - Properties changed
            - New property: applies_to_portal
            - New property: is_staff_managed
            - New property: offerings
            - New property: scoped_offerings
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/access-subnets/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: applies_to_portal
          - New property: offerings
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: is_staff_managed
            - New required property: scoped_offerings
          - Properties changed
            - New property: applies_to_portal
            - New property: is_staff_managed
            - New property: offerings
            - New property: scoped_offerings
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/admin-announcements/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/admin-announcements/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/admin-announcements/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/admin-announcements/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/admin-announcements/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/admin-announcements/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/admin-announcements/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/admin/arrow/billing-sync-items/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/admin/arrow/billing-sync-items/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/admin/arrow/billing-sync-items/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/admin/arrow/billing-syncs/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/admin/arrow/billing-syncs/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/admin/arrow/billing-syncs/cleanup_consumption/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/admin/arrow/billing-syncs/consumption_statistics/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/admin/arrow/billing-syncs/consumption_statistics/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/admin/arrow/billing-syncs/consumption_status/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/admin/arrow/billing-syncs/consumption_status/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/admin/arrow/billing-syncs/fetch_billing_export/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/admin/arrow/billing-syncs/fetch_consumption/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/admin/arrow/billing-syncs/fetch_license_info/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/admin/arrow/billing-syncs/pause_sync/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/admin/arrow/billing-syncs/pending_records/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/admin/arrow/billing-syncs/pending_records/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/admin/arrow/billing-syncs/reconcile/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/admin/arrow/billing-syncs/resume_sync/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/admin/arrow/billing-syncs/sync_resource_historical_consumption/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/admin/arrow/billing-syncs/sync_resources/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/admin/arrow/billing-syncs/trigger_consumption_sync/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/admin/arrow/billing-syncs/trigger_reconciliation/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/admin/arrow/billing-syncs/trigger_sync/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/admin/arrow/billing-syncs/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/admin/arrow/consumption-records/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/admin/arrow/consumption-records/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/admin/arrow/consumption-records/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/admin/arrow/customer-mappings/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/admin/arrow/customer-mappings/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/admin/arrow/customer-mappings/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/admin/arrow/customer-mappings/available_customers/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/admin/arrow/customer-mappings/available_customers/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/admin/arrow/customer-mappings/sync_from_arrow/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/admin/arrow/customer-mappings/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/admin/arrow/customer-mappings/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/admin/arrow/customer-mappings/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/admin/arrow/customer-mappings/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/admin/arrow/customer-mappings/{uuid}/billing_summary/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/admin/arrow/customer-mappings/{uuid}/discover_licenses/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/admin/arrow/customer-mappings/{uuid}/fetch_arrow_data/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/admin/arrow/customer-mappings/{uuid}/import_license/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/admin/arrow/customer-mappings/{uuid}/link_resource/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/admin/arrow/settings/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/admin/arrow/settings/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/admin/arrow/settings/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/admin/arrow/settings/discover_customers/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/admin/arrow/settings/preview_settings/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/admin/arrow/settings/save_settings/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/admin/arrow/settings/validate_credentials/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/admin/arrow/settings/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/admin/arrow/settings/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/admin/arrow/settings/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/admin/arrow/settings/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/admin/arrow/vendor-offering-mappings/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/admin/arrow/vendor-offering-mappings/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/admin/arrow/vendor-offering-mappings/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/admin/arrow/vendor-offering-mappings/vendor_choices/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/admin/arrow/vendor-offering-mappings/vendor_choices/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/admin/arrow/vendor-offering-mappings/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/admin/arrow/vendor-offering-mappings/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/admin/arrow/vendor-offering-mappings/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/admin/arrow/vendor-offering-mappings/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/admin/matrix-appservice/setup/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/admin/matrix-appservice/status/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/admin/matrix/diagnostics/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/admin/matrix/livekit/overview/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/admin/matrix/livekit/participants/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/admin/matrix/reprovision/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/affiliated-organizations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/affiliated-organizations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/affiliated-organizations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/affiliated-organizations/report/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/affiliated-organizations/report/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/affiliated-organizations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/affiliated-organizations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/affiliated-organizations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/affiliated-organizations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/affiliated-organizations/{uuid}/stats/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/anonymous-chat-feedbacks/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/anonymous-chat-feedbacks/{interaction_uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/anonymous-chat-interactions/

- New query param: created_after
- New query param: created_before
- New query param: has_feedback
- New query param: query
- Deleted query param: created_from
- Deleted query param: created_to
- Deleted query param: has_negative_feedback
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: click_count
              - New required property: input_tokens
              - New required property: output_tokens
            - Properties changed
              - New property: click_count
              - New property: input_tokens
              - New property: output_tokens
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/anonymous-chat-interactions/budget/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/anonymous-chat-interactions/by-session/{session_id}/

- New query param: created_after
- New query param: created_before
- New query param: has_feedback
- New query param: query
- Deleted query param: created_from
- Deleted query param: created_to
- Deleted query param: has_negative_feedback
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: click_count
              - New required property: input_tokens
              - New required property: output_tokens
            - Properties changed
              - New property: click_count
              - New property: input_tokens
              - New property: output_tokens
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/anonymous-chat-interactions/by-user/

- New query param: created_after
- New query param: created_before
- New query param: has_feedback
- New query param: query
- Deleted query param: created_from
- Deleted query param: created_to
- Deleted query param: has_negative_feedback
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/anonymous-chat-interactions/by-user/{user_slug}/

- New query param: created_after
- New query param: created_before
- New query param: has_feedback
- New query param: query
- Deleted query param: created_from
- Deleted query param: created_to
- Deleted query param: has_negative_feedback
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: click_count
              - New required property: input_tokens
              - New required property: output_tokens
            - Properties changed
              - New property: click_count
              - New property: input_tokens
              - New property: output_tokens
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/anonymous-chat-interactions/kpi/

- New query param: created_after
- New query param: created_before
- New query param: has_feedback
- New query param: input_tokens_max
- New query param: input_tokens_min
- New query param: is_flagged
- New query param: is_reviewed
- New query param: last_active_after
- New query param: last_active_before
- New query param: o
- New query param: output_tokens_max
- New query param: output_tokens_min
- New query param: query
- New query param: session_id
- New query param: severity
- New query param: total_tokens_max
- New query param: total_tokens_min
- New query param: user_slug
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: input_tokens_total
            - New required property: output_tokens_total
            - New required property: review_input_tokens_total
            - New required property: review_output_tokens_total
            - New required property: reviewed_total
          - Properties changed
            - New property: input_tokens_total
            - New property: output_tokens_total
            - New property: review_input_tokens_total
            - New property: review_output_tokens_total
            - New property: reviewed_total
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/anonymous-chat-interactions/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: click_count
            - New required property: input_tokens
            - New required property: output_tokens
          - Properties changed
            - New property: click_count
            - New property: input_tokens
            - New property: output_tokens
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/assignment-batches/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/assignment-batches/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/assignment-batches/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/assignment-batches/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/assignment-batches/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/assignment-batches/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/assignment-batches/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/assignment-batches/{uuid}/cancel/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/assignment-batches/{uuid}/extend-deadline/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/assignment-batches/{uuid}/send/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/assignment-items/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/assignment-items/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/assignment-items/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/assignment-items/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/assignment-items/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/assignment-items/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/assignment-items/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/assignment-items/{uuid}/accept/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/assignment-items/{uuid}/decline/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/assignment-items/{uuid}/force-unblock/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/assignment-items/{uuid}/reassign/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/assignment-items/{uuid}/suggest_alternatives/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/auth-tokens/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/auth-tokens/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/auth-tokens/{user_id}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/auth-tokens/{user_id}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/auth-valimo/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/auth-valimo/result/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/autoprovisioning-rules/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/autoprovisioning-rules/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/autoprovisioning-rules/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/autoprovisioning-rules/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/autoprovisioning-rules/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/autoprovisioning-rules/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/autoprovisioning-rules/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/autoprovisioning-rules/{uuid}/test-match/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/aws-images/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/aws-images/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/aws-images/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/aws-instances/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/aws-instances/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/aws-instances/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/aws-instances/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/aws-instances/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/aws-instances/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/aws-instances/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/aws-instances/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/aws-instances/{uuid}/resize/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/aws-instances/{uuid}/restart/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/aws-instances/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/aws-instances/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/aws-instances/{uuid}/start/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/aws-instances/{uuid}/stop/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/aws-instances/{uuid}/unlink/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/aws-regions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/aws-regions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/aws-regions/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/aws-sizes/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/aws-sizes/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/aws-sizes/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/aws-volumes/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/aws-volumes/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/aws-volumes/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/aws-volumes/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/aws-volumes/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/aws-volumes/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/aws-volumes/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/aws-volumes/{uuid}/attach/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/aws-volumes/{uuid}/detach/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/aws-volumes/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/aws-volumes/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/aws-volumes/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/aws-volumes/{uuid}/unlink/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/azure-images/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/azure-images/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/azure-images/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/azure-locations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/azure-locations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/azure-locations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/azure-public-ips/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/azure-public-ips/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/azure-public-ips/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/azure-public-ips/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/azure-public-ips/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/azure-public-ips/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/azure-public-ips/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/azure-public-ips/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/azure-public-ips/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/azure-public-ips/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/azure-public-ips/{uuid}/unlink/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/azure-resource-groups/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/azure-resource-groups/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/azure-resource-groups/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/azure-sizes/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/azure-sizes/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/azure-sizes/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/azure-sql-databases/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/azure-sql-databases/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/azure-sql-databases/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/azure-sql-databases/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/azure-sql-databases/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/azure-sql-databases/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/azure-sql-databases/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/azure-sql-databases/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/azure-sql-databases/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/azure-sql-databases/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/azure-sql-databases/{uuid}/unlink/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/azure-sql-servers/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/azure-sql-servers/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/azure-sql-servers/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/azure-sql-servers/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/azure-sql-servers/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/azure-sql-servers/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/azure-sql-servers/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/azure-sql-servers/{uuid}/create_database/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/azure-sql-servers/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/azure-sql-servers/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/azure-sql-servers/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/azure-sql-servers/{uuid}/unlink/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/azure-virtualmachines/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/azure-virtualmachines/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/azure-virtualmachines/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/azure-virtualmachines/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/azure-virtualmachines/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/azure-virtualmachines/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/azure-virtualmachines/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/azure-virtualmachines/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/azure-virtualmachines/{uuid}/restart/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/azure-virtualmachines/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/azure-virtualmachines/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/azure-virtualmachines/{uuid}/start/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/azure-virtualmachines/{uuid}/stop/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/azure-virtualmachines/{uuid}/unlink/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/backend-resource-requests/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/backend-resource-requests/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/backend-resource-requests/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/backend-resource-requests/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/backend-resource-requests/{uuid}/set_done/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/backend-resource-requests/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/backend-resource-requests/{uuid}/start_processing/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/backend-resources/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/backend-resources/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/backend-resources/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/backend-resources/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/backend-resources/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/backend-resources/{uuid}/import_resource/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_api_keys
            - New property: resource_effective_end_date
            - New property: usage_limit_restriction
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message_updated_at
                    - New property: created_by_organization_address
                    - New property: created_by_organization_country
                    - New property: created_by_organization_vat_code
                    - New property: provider_message_updated_at
            - Modified property: limit_usage
              - Description changed from 'Dictionary mapping limit-based component types to their consumed usage. For monthly periods, maps from current_usages; for longer periods, aggregates historical usage.' to 'Dictionary mapping limit-based component types to their consumed usage. Sums the ComponentUsage rows of the component's current period (the monthly billing period unless the component defines a longer limit_period), i.e. the period's high-watermark rather than the instantaneous current_usages value.'
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message_updated_at
                    - New property: created_by_organization_address
                    - New property: created_by_organization_country
                    - New property: created_by_organization_vat_code
                    - New property: provider_message_updated_at
            - Modified property: project_effective_end_date
              - Description changed from 'Effective project end date including grace period. After this date, resources will be terminated.' to 'Effective project end date including grace period. After this date, resources are terminated, except resources of offerings that disable the grace period — those are terminated on the raw project end date.'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/billing-total-cost/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/booking-offerings/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [default_access_subnets open_for_proposals qos_profiles]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: default_access_subnets
              - New property: open_for_proposals
              - New property: qos_profiles
              - Modified property: partitions
                - Items changed
                  - Properties changed
                    - New property: qos_options
              - Modified property: plans
                - Items changed
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: discount_aggregation
                          - New property: discount_formula
                          - Deleted property: discount_rate
                          - Deleted property: discount_threshold
                          - Deleted property: discounted_price
                    - Modified property: description
                      - MaxLength changed from null to 4096
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: action_on_usage_limit
                      - New property: auto_approve_for_roles
                      - New property: billing_source
                      - New property: conceal_subnet_restricted_resources
                      - New property: disable_grace_period
                      - New property: emit_display_name
                      - New property: emit_waldur_username
                      - New property: enable_membership_sync_status
                      - New property: enable_posix_account
                      - New property: enable_resource_access_subnets
                      - New property: enable_resource_end_date_change_requests
                      - New property: enforce_qos
                      - New property: gid_source
                      - New property: login_shell
                      - New property: resource_projects_limit_policy
                      - New property: restricted_to_roles
                      - New property: show_ssh_key_loss_warning
                      - New property: uid_source
                      - Deleted property: initial_primarygroup_number
                      - Deleted property: initial_rolegroup_number
                      - Deleted property: initial_uidnumber
                      - Deleted property: initial_usergroup_number
              - Modified property: software_catalogs
                - Items changed
                  - Properties changed
                    - Modified property: enabled_cpu_family
                      - Type changed from 'object' to 'array'
                      - AdditionalProperties changed from true to null
                      - Items changed
                        - Schema added
                    - Modified property: enabled_cpu_microarchitectures
                      - Type changed from 'object' to 'array'
                      - AdditionalProperties changed from true to null
                      - Items changed
                        - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/booking-offerings/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/booking-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [default_access_subnets open_for_proposals qos_profiles]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: default_access_subnets
            - New property: open_for_proposals
            - New property: qos_profiles
            - Modified property: partitions
              - Items changed
                - Properties changed
                  - New property: qos_options
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: discount_aggregation
                        - New property: discount_formula
                        - Deleted property: discount_rate
                        - Deleted property: discount_threshold
                        - Deleted property: discounted_price
                  - Modified property: description
                    - MaxLength changed from null to 4096
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: action_on_usage_limit
                    - New property: auto_approve_for_roles
                    - New property: billing_source
                    - New property: conceal_subnet_restricted_resources
                    - New property: disable_grace_period
                    - New property: emit_display_name
                    - New property: emit_waldur_username
                    - New property: enable_membership_sync_status
                    - New property: enable_posix_account
                    - New property: enable_resource_access_subnets
                    - New property: enable_resource_end_date_change_requests
                    - New property: enforce_qos
                    - New property: gid_source
                    - New property: login_shell
                    - New property: resource_projects_limit_policy
                    - New property: restricted_to_roles
                    - New property: show_ssh_key_loss_warning
                    - New property: uid_source
                    - Deleted property: initial_primarygroup_number
                    - Deleted property: initial_rolegroup_number
                    - Deleted property: initial_uidnumber
                    - Deleted property: initial_usergroup_number
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: enabled_cpu_family
                    - Type changed from 'object' to 'array'
                    - AdditionalProperties changed from true to null
                    - Items changed
                      - Schema added
                  - Modified property: enabled_cpu_microarchitectures
                    - Type changed from 'object' to 'array'
                    - AdditionalProperties changed from true to null
                    - Items changed
                      - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/booking-offerings/{uuid}/google_calendar_sync/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/booking-offerings/{uuid}/share_google_calendar/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/booking-offerings/{uuid}/unshare_google_calendar/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/booking-resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [has_api_keys resource_effective_end_date usage_limit_restriction]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: has_api_keys
              - New property: resource_effective_end_date
              - New property: usage_limit_restriction
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: consumer_message_updated_at
                      - New property: created_by_organization_address
                      - New property: created_by_organization_country
                      - New property: created_by_organization_vat_code
                      - New property: provider_message_updated_at
              - Modified property: limit_usage
                - Description changed from 'Dictionary mapping limit-based component types to their consumed usage. For monthly periods, maps from current_usages; for longer periods, aggregates historical usage.' to 'Dictionary mapping limit-based component types to their consumed usage. Sums the ComponentUsage rows of the component's current period (the monthly billing period unless the component defines a longer limit_period), i.e. the period's high-watermark rather than the instantaneous current_usages value.'
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: consumer_message_updated_at
                      - New property: created_by_organization_address
                      - New property: created_by_organization_country
                      - New property: created_by_organization_vat_code
                      - New property: provider_message_updated_at
              - Modified property: project_effective_end_date
                - Description changed from 'Effective project end date including grace period. After this date, resources will be terminated.' to 'Effective project end date including grace period. After this date, resources are terminated, except resources of offerings that disable the grace period — those are terminated on the raw project end date.'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/booking-resources/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/booking-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [has_api_keys resource_effective_end_date usage_limit_restriction]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_api_keys
            - New property: resource_effective_end_date
            - New property: usage_limit_restriction
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message_updated_at
                    - New property: created_by_organization_address
                    - New property: created_by_organization_country
                    - New property: created_by_organization_vat_code
                    - New property: provider_message_updated_at
            - Modified property: limit_usage
              - Description changed from 'Dictionary mapping limit-based component types to their consumed usage. For monthly periods, maps from current_usages; for longer periods, aggregates historical usage.' to 'Dictionary mapping limit-based component types to their consumed usage. Sums the ComponentUsage rows of the component's current period (the monthly billing period unless the component defines a longer limit_period), i.e. the period's high-watermark rather than the instantaneous current_usages value.'
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message_updated_at
                    - New property: created_by_organization_address
                    - New property: created_by_organization_country
                    - New property: created_by_organization_vat_code
                    - New property: provider_message_updated_at
            - Modified property: project_effective_end_date
              - Description changed from 'Effective project end date including grace period. After this date, resources will be terminated.' to 'Effective project end date including grace period. After this date, resources are terminated, except resources of offerings that disable the grace period — those are terminated on the raw project end date.'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/booking-resources/{uuid}/accept/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/booking-resources/{uuid}/reject/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/broadcast-message-templates/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/broadcast-message-templates/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/broadcast-message-templates/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/broadcast-message-templates/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/broadcast-message-templates/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/broadcast-message-templates/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/broadcast-message-templates/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/broadcast-messages/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/broadcast-messages/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/broadcast-messages/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/broadcast-messages/recipients/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/broadcast-messages/recipients/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/broadcast-messages/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/broadcast-messages/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/broadcast-messages/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/broadcast-messages/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/broadcast-messages/{uuid}/schedule/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/broadcast-messages/{uuid}/send/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/call-assignment-configurations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/call-assignment-configurations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/call-assignment-configurations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/call-assignment-configurations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/call-assignment-configurations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/call-assignment-configurations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/call-assignment-configurations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/call-managing-organisations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/call-managing-organisations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/call-managing-organisations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/call-managing-organisations/global_stats_performance/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/call-managing-organisations/global_stats_performance/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/call-managing-organisations/global_stats_resource_demand/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/call-managing-organisations/global_stats_resource_demand/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/call-managing-organisations/global_stats_review_progress/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/call-managing-organisations/global_stats_review_progress/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/call-managing-organisations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/call-managing-organisations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/call-managing-organisations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/call-managing-organisations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/call-managing-organisations/{uuid}/add_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/call-managing-organisations/{uuid}/delete_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/call-managing-organisations/{uuid}/list_users/

- Modified query param: role
  - Description changed from 'Role UUID or name' to 'Role UUID or name. Repeat to filter by several roles.'
  - Schema changed
    - Type changed from 'string' to 'array'
    - Format changed from 'uuid' to ''
    - Items changed
      - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/call-managing-organisations/{uuid}/stats/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/call-managing-organisations/{uuid}/update_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/call-proposal-project-role-mappings/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/call-proposal-project-role-mappings/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/call-proposal-project-role-mappings/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/call-proposal-project-role-mappings/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/call-proposal-project-role-mappings/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/call-proposal-project-role-mappings/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/call-proposal-project-role-mappings/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/call-reviewer-pools/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/call-reviewer-pools/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/call-reviewer-pools/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/call-reviewer-pools/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/call-reviewer-pools/{uuid}/accept/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/call-reviewer-pools/{uuid}/decline/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/call-reviewer-pools/{uuid}/force-accept/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/call-rounds/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/call-rounds/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/call-rounds/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/call-rounds/{uuid}/reviewers/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/celery-stats/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/chat-messages/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/chat-messages/{uuid}/feedback/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/chat-quota/set_quota/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/chat-quota/usage/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/chat-sessions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/chat-sessions/current/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/chat-sessions/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/chat-system-prompts/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/chat-system-prompts/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/chat-system-prompts/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/chat-system-prompts/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/chat-system-prompts/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/chat-system-prompts/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/chat-system-prompts/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/chat-system-prompts/{uuid}/activate/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/chat-system-prompts/{uuid}/deactivate/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/chat-threads/

- New query param: created_after
- New query param: created_before
- New query param: modified_after
- New query param: modified_before
- Deleted query param: created
- Deleted query param: modified
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [models_used]
- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-models_used models_used]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: models_used
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/chat-threads/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [models_used]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: models_used
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/chat-threads/{uuid}/archive/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/chat-threads/{uuid}/cancel/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/chat-threads/{uuid}/unarchive/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/chat-tools/execute/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/chat/stream/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/checklists-admin-question-dependencies/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/checklists-admin-question-dependencies/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/checklists-admin-question-dependencies/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/checklists-admin-question-dependencies/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/checklists-admin-question-dependencies/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/checklists-admin-question-dependencies/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/checklists-admin-question-dependencies/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/checklists-admin-question-options/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/checklists-admin-question-options/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/checklists-admin-question-options/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/checklists-admin-question-options/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/checklists-admin-question-options/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/checklists-admin-question-options/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/checklists-admin-question-options/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/checklists-admin-questions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/checklists-admin-questions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/checklists-admin-questions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/checklists-admin-questions/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/checklists-admin-questions/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/checklists-admin-questions/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/checklists-admin-questions/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/checklists-admin/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/checklists-admin/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/checklists-admin/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/checklists-admin/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/checklists-admin/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/checklists-admin/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/checklists-admin/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/checklists-admin/{uuid}/questions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/coi-detection-jobs/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/coi-detection-jobs/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/coi-detection-jobs/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/coi-disclosures/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/coi-disclosures/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/coi-disclosures/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/coi-disclosures/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/component-user-usage-limits/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/component-user-usage-limits/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/component-user-usage-limits/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/component-user-usage-limits/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/component-user-usage-limits/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/component-user-usage-limits/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/component-user-usage-limits/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/configuration/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/conflicts-of-interest/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/conflicts-of-interest/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/conflicts-of-interest/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/conflicts-of-interest/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/conflicts-of-interest/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/conflicts-of-interest/{uuid}/dismiss/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/conflicts-of-interest/{uuid}/recuse/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/conflicts-of-interest/{uuid}/waive/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/customer-credits/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: withdrawable_balance
            - Properties changed
              - New property: withdrawable_balance
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/customer-credits/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/customer-credits/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: withdrawable_balance
          - Properties changed
            - New property: withdrawable_balance
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/customer-credits/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/customer-credits/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: withdrawable_balance
          - Properties changed
            - New property: withdrawable_balance
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/customer-credits/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: withdrawable_balance
          - Properties changed
            - New property: withdrawable_balance
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/customer-credits/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: withdrawable_balance
          - Properties changed
            - New property: withdrawable_balance
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/customer-credits/{uuid}/apply_compensations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/customer-credits/{uuid}/clear_compensations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/customer-credits/{uuid}/consumptions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/customer-permissions-reviews/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/customer-permissions-reviews/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/customer-permissions-reviews/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/customer-permissions-reviews/{uuid}/close/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/customer-quotas/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/customer-quotas/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/customers/

- New query param: current_user_has_role
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [has_active_helpdesk has_affiliate_links]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: has_active_helpdesk
              - New property: has_affiliate_links
              - Modified property: customer_credit
                - Type changed from 'number' to 'string'
                - Format changed from 'double' to ''
              - Modified property: customer_unallocated_credit
                - Type changed from 'number' to 'string'
                - Format changed from 'double' to ''
              - Modified property: payment_profiles
                - Items changed
                  - Properties changed
                    - Modified property: attributes
                      - Properties changed
                        - Modified property: contract_sum
                          - Type changed from 'integer' to 'string'
              - Modified property: user_affiliations
                - Type changed from 'object' to 'array'
                - AdditionalProperties changed from true to null
                - Items changed
                  - Schema added
              - Modified property: user_email_patterns
                - Type changed from 'object' to 'array'
                - AdditionalProperties changed from true to null
                - Items changed
                  - Schema added
              - Modified property: user_identity_sources
                - Type changed from 'object' to 'array'
                - Description changed from 'List of allowed identity sources (identity providers).' to ''
                - AdditionalProperties changed from true to null
                - Items changed
                  - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/customers/

- New query param: current_user_has_role
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/customers/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: user_affiliations
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_email_patterns
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_identity_sources
            - Type changed from 'object' to 'array'
            - Description changed from 'List of allowed identity sources (identity providers).' to ''
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: user_affiliations
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_email_patterns
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_identity_sources
            - Type changed from 'object' to 'array'
            - Description changed from 'List of allowed identity sources (identity providers).' to ''
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: user_affiliations
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_email_patterns
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_identity_sources
            - Type changed from 'object' to 'array'
            - Description changed from 'List of allowed identity sources (identity providers).' to ''
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_active_helpdesk
            - New property: has_affiliate_links
            - Modified property: customer_credit
              - Type changed from 'number' to 'string'
              - Format changed from 'double' to ''
            - Modified property: customer_unallocated_credit
              - Type changed from 'number' to 'string'
              - Format changed from 'double' to ''
            - Modified property: payment_profiles
              - Items changed
                - Properties changed
                  - Modified property: attributes
                    - Properties changed
                      - Modified property: contract_sum
                        - Type changed from 'integer' to 'string'
            - Modified property: user_affiliations
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_email_patterns
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_identity_sources
              - Type changed from 'object' to 'array'
              - Description changed from 'List of allowed identity sources (identity providers).' to ''
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/customers/countries/

- New query param: current_user_has_role
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/customers/countries/

- New query param: current_user_has_role
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/customers/{customer_uuid}/project-metadata-compliance-details/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/customers/{customer_uuid}/project-metadata-compliance-overview/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/customers/{customer_uuid}/project-metadata-compliance-projects/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/customers/{customer_uuid}/project-metadata-question-answers/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/customers/{customer_uuid}/users/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/customers/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/customers/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [has_active_helpdesk has_affiliate_links]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_active_helpdesk
            - New property: has_affiliate_links
            - Modified property: customer_credit
              - Type changed from 'number' to 'string'
              - Format changed from 'double' to ''
            - Modified property: customer_unallocated_credit
              - Type changed from 'number' to 'string'
              - Format changed from 'double' to ''
            - Modified property: payment_profiles
              - Items changed
                - Properties changed
                  - Modified property: attributes
                    - Properties changed
                      - Modified property: contract_sum
                        - Type changed from 'integer' to 'string'
            - Modified property: user_affiliations
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_email_patterns
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_identity_sources
              - Type changed from 'object' to 'array'
              - Description changed from 'List of allowed identity sources (identity providers).' to ''
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/customers/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: user_affiliations
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_email_patterns
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_identity_sources
            - Type changed from 'object' to 'array'
            - Description changed from 'List of allowed identity sources (identity providers).' to ''
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: user_affiliations
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_email_patterns
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_identity_sources
            - Type changed from 'object' to 'array'
            - Description changed from 'List of allowed identity sources (identity providers).' to ''
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: user_affiliations
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_email_patterns
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_identity_sources
            - Type changed from 'object' to 'array'
            - Description changed from 'List of allowed identity sources (identity providers).' to ''
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_active_helpdesk
            - New property: has_affiliate_links
            - Modified property: customer_credit
              - Type changed from 'number' to 'string'
              - Format changed from 'double' to ''
            - Modified property: customer_unallocated_credit
              - Type changed from 'number' to 'string'
              - Format changed from 'double' to ''
            - Modified property: payment_profiles
              - Items changed
                - Properties changed
                  - Modified property: attributes
                    - Properties changed
                      - Modified property: contract_sum
                        - Type changed from 'integer' to 'string'
            - Modified property: user_affiliations
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_email_patterns
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_identity_sources
              - Type changed from 'object' to 'array'
              - Description changed from 'List of allowed identity sources (identity providers).' to ''
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/customers/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: user_affiliations
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_email_patterns
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_identity_sources
            - Type changed from 'object' to 'array'
            - Description changed from 'List of allowed identity sources (identity providers).' to ''
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: user_affiliations
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_email_patterns
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_identity_sources
            - Type changed from 'object' to 'array'
            - Description changed from 'List of allowed identity sources (identity providers).' to ''
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: user_affiliations
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_email_patterns
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_identity_sources
            - Type changed from 'object' to 'array'
            - Description changed from 'List of allowed identity sources (identity providers).' to ''
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_active_helpdesk
            - New property: has_affiliate_links
            - Modified property: customer_credit
              - Type changed from 'number' to 'string'
              - Format changed from 'double' to ''
            - Modified property: customer_unallocated_credit
              - Type changed from 'number' to 'string'
              - Format changed from 'double' to ''
            - Modified property: payment_profiles
              - Items changed
                - Properties changed
                  - Modified property: attributes
                    - Properties changed
                      - Modified property: contract_sum
                        - Type changed from 'integer' to 'string'
            - Modified property: user_affiliations
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_email_patterns
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_identity_sources
              - Type changed from 'object' to 'array'
              - Description changed from 'List of allowed identity sources (identity providers).' to ''
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/customers/{uuid}/add_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/customers/{uuid}/contact/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/customers/{uuid}/delete_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/customers/{uuid}/history/

- New query param: current_user_has_role
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/customers/{uuid}/history/at/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/customers/{uuid}/list_users/

- Modified query param: role
  - Description changed from 'Role UUID or name' to 'Role UUID or name. Repeat to filter by several roles.'
  - Schema changed
    - Type changed from 'string' to 'array'
    - Format changed from 'uuid' to ''
    - Items changed
      - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/customers/{uuid}/project-digest-config/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/customers/{uuid}/project-digest-config/preview/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/customers/{uuid}/project-digest-config/send-test/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/customers/{uuid}/stats/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/customers/{uuid}/update-project-digest-config/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/customers/{uuid}/update-project-digest-config/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/customers/{uuid}/update_default_affiliations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/customers/{uuid}/update_organization_groups/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/customers/{uuid}/update_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/daily-quotas/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/data-access-logs/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/data-access-logs/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/data-access-logs/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/data-access-logs/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/database-stats/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/debug/pubsub/circuit_breaker/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/debug/pubsub/circuit_breaker_reset/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/debug/pubsub/dead_letter_queue/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/debug/pubsub/message_state_cache/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/debug/pubsub/metrics/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/debug/pubsub/metrics_reset/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/debug/pubsub/overview/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/debug/pubsub/queues/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/digitalocean-droplets/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/digitalocean-droplets/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/digitalocean-droplets/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/digitalocean-droplets/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/digitalocean-droplets/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/digitalocean-droplets/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/digitalocean-droplets/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/digitalocean-droplets/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/digitalocean-droplets/{uuid}/resize/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/digitalocean-droplets/{uuid}/restart/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/digitalocean-droplets/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/digitalocean-droplets/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/digitalocean-droplets/{uuid}/start/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/digitalocean-droplets/{uuid}/stop/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/digitalocean-droplets/{uuid}/unlink/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/digitalocean-images/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/digitalocean-images/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/digitalocean-images/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/digitalocean-regions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/digitalocean-regions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/digitalocean-regions/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/digitalocean-sizes/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/digitalocean-sizes/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/digitalocean-sizes/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/email-logs/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/email-logs/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/email-logs/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/event-subscription-queues/

- Deprecated changed from false to true
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/event-subscription-queues/

- Deprecated changed from false to true
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/event-subscription-queues/{uuid}/

- Deprecated changed from false to true
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/event-subscription-queues/{uuid}/

- Description changed from '' to 'DEPRECATED: superseded by the unified EventConsumer path (POST /api/event-consumers/register/). Removal tracked in WAL-10111.'
- Deprecated changed from false to true
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/event-subscriptions/

- Deprecated changed from false to true
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/event-subscriptions/

- Deprecated changed from false to true
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/event-subscriptions/

- Description changed from '' to 'DEPRECATED: superseded by the unified EventConsumer path (POST /api/event-consumers/register/). Removal tracked in WAL-10111.'
- Deprecated changed from false to true
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/event-subscriptions/{uuid}/

- Deprecated changed from false to true
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/event-subscriptions/{uuid}/

- Deprecated changed from false to true
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/event-subscriptions/{uuid}/create_queue/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: object_type
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/ObservableObjectTypeEnum
                - New enum values: [resource_api_key_rotation resource_end_date_change_request user_profile user_ssh_key user_lifecycle]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/events-stats/

- New query param: related_user_uuid
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/events-stats/

- New query param: related_user_uuid
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/events/

- New query param: auth_method
- New query param: pat_uuid
- New query param: related_user_uuid
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/events/

- New query param: auth_method
- New query param: pat_uuid
- New query param: related_user_uuid
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/events/count/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/events/count/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/events/event_groups/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/events/event_groups/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/events/scope_types/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/events/scope_types/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/events/{id}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/expertise-categories/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/expertise-categories/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/expertise-categories/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/external-links/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/external-links/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/external-links/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/external-links/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/external-links/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/external-links/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/external-links/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/feature-values/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/financial-reports/

- New query param: current_user_has_role
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: payment_profiles
                - Items changed
                  - Properties changed
                    - Modified property: attributes
                      - Properties changed
                        - Modified property: contract_sum
                          - Type changed from 'integer' to 'string'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/financial-reports/

- New query param: current_user_has_role
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/financial-reports/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: payment_profiles
              - Items changed
                - Properties changed
                  - Modified property: attributes
                    - Properties changed
                      - Modified property: contract_sum
                        - Type changed from 'integer' to 'string'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/freeipa-profiles/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/freeipa-profiles/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/freeipa-profiles/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/freeipa-profiles/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/freeipa-profiles/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/freeipa-profiles/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/freeipa-profiles/{uuid}/update_ssh_keys/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/google-auth/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: allowed_domains
                - Type changed from 'object' to 'array'
                - AdditionalProperties changed from true to null
                - Items changed
                  - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/google-auth/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/google-auth/callback/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/google-auth/callback/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/google-auth/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: allowed_domains
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/google-auth/{uuid}/authorize/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

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
                  - New enum values: [offering_access_subnet_creation_succeeded offering_access_subnet_deletion_succeeded offering_access_subnet_update_succeeded create_of_affiliate_by_staff marketplace_resource_api_key_rotated marketplace_resource_api_key_revealed marketplace_resource_project_created marketplace_resource_project_recovered marketplace_resource_project_removed marketplace_resource_end_date_change_request_created marketplace_resource_end_date_change_request_approved marketplace_resource_end_date_change_request_rejected marketplace_resource_end_date_change_request_canceled maintenance_announcement_cancelled maintenance_announcement_completed maintenance_announcement_created maintenance_announcement_deleted maintenance_announcement_scheduled maintenance_announcement_started maintenance_announcement_unscheduled maintenance_announcement_updated increase_of_customer_credit_due_to_affiliate_fee update_of_affiliate_by_staff user_blocked pat_access_denied_from_ip pat_network_acl_updated pat_authentication_rejected]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/hooks-email/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/hooks-email/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [offering_access_subnet_creation_succeeded offering_access_subnet_deletion_succeeded offering_access_subnet_update_succeeded create_of_affiliate_by_staff marketplace_resource_api_key_rotated marketplace_resource_api_key_revealed marketplace_resource_project_created marketplace_resource_project_recovered marketplace_resource_project_removed marketplace_resource_end_date_change_request_created marketplace_resource_end_date_change_request_approved marketplace_resource_end_date_change_request_rejected marketplace_resource_end_date_change_request_canceled maintenance_announcement_cancelled maintenance_announcement_completed maintenance_announcement_created maintenance_announcement_deleted maintenance_announcement_scheduled maintenance_announcement_started maintenance_announcement_unscheduled maintenance_announcement_updated increase_of_customer_credit_due_to_affiliate_fee update_of_affiliate_by_staff user_blocked pat_access_denied_from_ip pat_network_acl_updated pat_authentication_rejected]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [offering_access_subnet_creation_succeeded offering_access_subnet_deletion_succeeded offering_access_subnet_update_succeeded create_of_affiliate_by_staff marketplace_resource_api_key_rotated marketplace_resource_api_key_revealed marketplace_resource_project_created marketplace_resource_project_recovered marketplace_resource_project_removed marketplace_resource_end_date_change_request_created marketplace_resource_end_date_change_request_approved marketplace_resource_end_date_change_request_rejected marketplace_resource_end_date_change_request_canceled maintenance_announcement_cancelled maintenance_announcement_completed maintenance_announcement_created maintenance_announcement_deleted maintenance_announcement_scheduled maintenance_announcement_started maintenance_announcement_unscheduled maintenance_announcement_updated increase_of_customer_credit_due_to_affiliate_fee update_of_affiliate_by_staff user_blocked pat_access_denied_from_ip pat_network_acl_updated pat_authentication_rejected]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/hooks-email/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/hooks-email/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [offering_access_subnet_creation_succeeded offering_access_subnet_deletion_succeeded offering_access_subnet_update_succeeded create_of_affiliate_by_staff marketplace_resource_api_key_rotated marketplace_resource_api_key_revealed marketplace_resource_project_created marketplace_resource_project_recovered marketplace_resource_project_removed marketplace_resource_end_date_change_request_created marketplace_resource_end_date_change_request_approved marketplace_resource_end_date_change_request_rejected marketplace_resource_end_date_change_request_canceled maintenance_announcement_cancelled maintenance_announcement_completed maintenance_announcement_created maintenance_announcement_deleted maintenance_announcement_scheduled maintenance_announcement_started maintenance_announcement_unscheduled maintenance_announcement_updated increase_of_customer_credit_due_to_affiliate_fee update_of_affiliate_by_staff user_blocked pat_access_denied_from_ip pat_network_acl_updated pat_authentication_rejected]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [offering_access_subnet_creation_succeeded offering_access_subnet_deletion_succeeded offering_access_subnet_update_succeeded create_of_affiliate_by_staff marketplace_resource_api_key_rotated marketplace_resource_api_key_revealed marketplace_resource_project_created marketplace_resource_project_recovered marketplace_resource_project_removed marketplace_resource_end_date_change_request_created marketplace_resource_end_date_change_request_approved marketplace_resource_end_date_change_request_rejected marketplace_resource_end_date_change_request_canceled maintenance_announcement_cancelled maintenance_announcement_completed maintenance_announcement_created maintenance_announcement_deleted maintenance_announcement_scheduled maintenance_announcement_started maintenance_announcement_unscheduled maintenance_announcement_updated increase_of_customer_credit_due_to_affiliate_fee update_of_affiliate_by_staff user_blocked pat_access_denied_from_ip pat_network_acl_updated pat_authentication_rejected]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [offering_access_subnet_creation_succeeded offering_access_subnet_deletion_succeeded offering_access_subnet_update_succeeded create_of_affiliate_by_staff marketplace_resource_api_key_rotated marketplace_resource_api_key_revealed marketplace_resource_project_created marketplace_resource_project_recovered marketplace_resource_project_removed marketplace_resource_end_date_change_request_created marketplace_resource_end_date_change_request_approved marketplace_resource_end_date_change_request_rejected marketplace_resource_end_date_change_request_canceled maintenance_announcement_cancelled maintenance_announcement_completed maintenance_announcement_created maintenance_announcement_deleted maintenance_announcement_scheduled maintenance_announcement_started maintenance_announcement_unscheduled maintenance_announcement_updated increase_of_customer_credit_due_to_affiliate_fee update_of_affiliate_by_staff user_blocked pat_access_denied_from_ip pat_network_acl_updated pat_authentication_rejected]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/hooks-email/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [offering_access_subnet_creation_succeeded offering_access_subnet_deletion_succeeded offering_access_subnet_update_succeeded create_of_affiliate_by_staff marketplace_resource_api_key_rotated marketplace_resource_api_key_revealed marketplace_resource_project_created marketplace_resource_project_recovered marketplace_resource_project_removed marketplace_resource_end_date_change_request_created marketplace_resource_end_date_change_request_approved marketplace_resource_end_date_change_request_rejected marketplace_resource_end_date_change_request_canceled maintenance_announcement_cancelled maintenance_announcement_completed maintenance_announcement_created maintenance_announcement_deleted maintenance_announcement_scheduled maintenance_announcement_started maintenance_announcement_unscheduled maintenance_announcement_updated increase_of_customer_credit_due_to_affiliate_fee update_of_affiliate_by_staff user_blocked pat_access_denied_from_ip pat_network_acl_updated pat_authentication_rejected]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [offering_access_subnet_creation_succeeded offering_access_subnet_deletion_succeeded offering_access_subnet_update_succeeded create_of_affiliate_by_staff marketplace_resource_api_key_rotated marketplace_resource_api_key_revealed marketplace_resource_project_created marketplace_resource_project_recovered marketplace_resource_project_removed marketplace_resource_end_date_change_request_created marketplace_resource_end_date_change_request_approved marketplace_resource_end_date_change_request_rejected marketplace_resource_end_date_change_request_canceled maintenance_announcement_cancelled maintenance_announcement_completed maintenance_announcement_created maintenance_announcement_deleted maintenance_announcement_scheduled maintenance_announcement_started maintenance_announcement_unscheduled maintenance_announcement_updated increase_of_customer_credit_due_to_affiliate_fee update_of_affiliate_by_staff user_blocked pat_access_denied_from_ip pat_network_acl_updated pat_authentication_rejected]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

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
                  - New enum values: [offering_access_subnet_creation_succeeded offering_access_subnet_deletion_succeeded offering_access_subnet_update_succeeded create_of_affiliate_by_staff marketplace_resource_api_key_rotated marketplace_resource_api_key_revealed marketplace_resource_project_created marketplace_resource_project_recovered marketplace_resource_project_removed marketplace_resource_end_date_change_request_created marketplace_resource_end_date_change_request_approved marketplace_resource_end_date_change_request_rejected marketplace_resource_end_date_change_request_canceled maintenance_announcement_cancelled maintenance_announcement_completed maintenance_announcement_created maintenance_announcement_deleted maintenance_announcement_scheduled maintenance_announcement_started maintenance_announcement_unscheduled maintenance_announcement_updated increase_of_customer_credit_due_to_affiliate_fee update_of_affiliate_by_staff user_blocked pat_access_denied_from_ip pat_network_acl_updated pat_authentication_rejected]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/hooks-web/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/hooks-web/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [offering_access_subnet_creation_succeeded offering_access_subnet_deletion_succeeded offering_access_subnet_update_succeeded create_of_affiliate_by_staff marketplace_resource_api_key_rotated marketplace_resource_api_key_revealed marketplace_resource_project_created marketplace_resource_project_recovered marketplace_resource_project_removed marketplace_resource_end_date_change_request_created marketplace_resource_end_date_change_request_approved marketplace_resource_end_date_change_request_rejected marketplace_resource_end_date_change_request_canceled maintenance_announcement_cancelled maintenance_announcement_completed maintenance_announcement_created maintenance_announcement_deleted maintenance_announcement_scheduled maintenance_announcement_started maintenance_announcement_unscheduled maintenance_announcement_updated increase_of_customer_credit_due_to_affiliate_fee update_of_affiliate_by_staff user_blocked pat_access_denied_from_ip pat_network_acl_updated pat_authentication_rejected]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [offering_access_subnet_creation_succeeded offering_access_subnet_deletion_succeeded offering_access_subnet_update_succeeded create_of_affiliate_by_staff marketplace_resource_api_key_rotated marketplace_resource_api_key_revealed marketplace_resource_project_created marketplace_resource_project_recovered marketplace_resource_project_removed marketplace_resource_end_date_change_request_created marketplace_resource_end_date_change_request_approved marketplace_resource_end_date_change_request_rejected marketplace_resource_end_date_change_request_canceled maintenance_announcement_cancelled maintenance_announcement_completed maintenance_announcement_created maintenance_announcement_deleted maintenance_announcement_scheduled maintenance_announcement_started maintenance_announcement_unscheduled maintenance_announcement_updated increase_of_customer_credit_due_to_affiliate_fee update_of_affiliate_by_staff user_blocked pat_access_denied_from_ip pat_network_acl_updated pat_authentication_rejected]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/hooks-web/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/hooks-web/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [offering_access_subnet_creation_succeeded offering_access_subnet_deletion_succeeded offering_access_subnet_update_succeeded create_of_affiliate_by_staff marketplace_resource_api_key_rotated marketplace_resource_api_key_revealed marketplace_resource_project_created marketplace_resource_project_recovered marketplace_resource_project_removed marketplace_resource_end_date_change_request_created marketplace_resource_end_date_change_request_approved marketplace_resource_end_date_change_request_rejected marketplace_resource_end_date_change_request_canceled maintenance_announcement_cancelled maintenance_announcement_completed maintenance_announcement_created maintenance_announcement_deleted maintenance_announcement_scheduled maintenance_announcement_started maintenance_announcement_unscheduled maintenance_announcement_updated increase_of_customer_credit_due_to_affiliate_fee update_of_affiliate_by_staff user_blocked pat_access_denied_from_ip pat_network_acl_updated pat_authentication_rejected]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [offering_access_subnet_creation_succeeded offering_access_subnet_deletion_succeeded offering_access_subnet_update_succeeded create_of_affiliate_by_staff marketplace_resource_api_key_rotated marketplace_resource_api_key_revealed marketplace_resource_project_created marketplace_resource_project_recovered marketplace_resource_project_removed marketplace_resource_end_date_change_request_created marketplace_resource_end_date_change_request_approved marketplace_resource_end_date_change_request_rejected marketplace_resource_end_date_change_request_canceled maintenance_announcement_cancelled maintenance_announcement_completed maintenance_announcement_created maintenance_announcement_deleted maintenance_announcement_scheduled maintenance_announcement_started maintenance_announcement_unscheduled maintenance_announcement_updated increase_of_customer_credit_due_to_affiliate_fee update_of_affiliate_by_staff user_blocked pat_access_denied_from_ip pat_network_acl_updated pat_authentication_rejected]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [offering_access_subnet_creation_succeeded offering_access_subnet_deletion_succeeded offering_access_subnet_update_succeeded create_of_affiliate_by_staff marketplace_resource_api_key_rotated marketplace_resource_api_key_revealed marketplace_resource_project_created marketplace_resource_project_recovered marketplace_resource_project_removed marketplace_resource_end_date_change_request_created marketplace_resource_end_date_change_request_approved marketplace_resource_end_date_change_request_rejected marketplace_resource_end_date_change_request_canceled maintenance_announcement_cancelled maintenance_announcement_completed maintenance_announcement_created maintenance_announcement_deleted maintenance_announcement_scheduled maintenance_announcement_started maintenance_announcement_unscheduled maintenance_announcement_updated increase_of_customer_credit_due_to_affiliate_fee update_of_affiliate_by_staff user_blocked pat_access_denied_from_ip pat_network_acl_updated pat_authentication_rejected]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/hooks-web/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_types
            - Items changed
              - New enum values: [offering_access_subnet_creation_succeeded offering_access_subnet_deletion_succeeded offering_access_subnet_update_succeeded create_of_affiliate_by_staff marketplace_resource_api_key_rotated marketplace_resource_api_key_revealed marketplace_resource_project_created marketplace_resource_project_recovered marketplace_resource_project_removed marketplace_resource_end_date_change_request_created marketplace_resource_end_date_change_request_approved marketplace_resource_end_date_change_request_rejected marketplace_resource_end_date_change_request_canceled maintenance_announcement_cancelled maintenance_announcement_completed maintenance_announcement_created maintenance_announcement_deleted maintenance_announcement_scheduled maintenance_announcement_started maintenance_announcement_unscheduled maintenance_announcement_updated increase_of_customer_credit_due_to_affiliate_fee update_of_affiliate_by_staff user_blocked pat_access_denied_from_ip pat_network_acl_updated pat_authentication_rejected]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_types
              - Items changed
                - New enum values: [offering_access_subnet_creation_succeeded offering_access_subnet_deletion_succeeded offering_access_subnet_update_succeeded create_of_affiliate_by_staff marketplace_resource_api_key_rotated marketplace_resource_api_key_revealed marketplace_resource_project_created marketplace_resource_project_recovered marketplace_resource_project_removed marketplace_resource_end_date_change_request_created marketplace_resource_end_date_change_request_approved marketplace_resource_end_date_change_request_rejected marketplace_resource_end_date_change_request_canceled maintenance_announcement_cancelled maintenance_announcement_completed maintenance_announcement_created maintenance_announcement_deleted maintenance_announcement_scheduled maintenance_announcement_started maintenance_announcement_unscheduled maintenance_announcement_updated increase_of_customer_credit_due_to_affiliate_fee update_of_affiliate_by_staff user_blocked pat_access_denied_from_ip pat_network_acl_updated pat_authentication_rejected]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/hooks/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/hooks/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/identity-bridge/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/identity-bridge/allowed-fields/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/identity-bridge/remove/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/identity-bridge/stats/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/identity-providers/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/identity-providers/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/identity-providers/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/identity-providers/discover_metadata/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/identity-providers/generate-mapping/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/identity-providers/{provider}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/identity-providers/{provider}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/identity-providers/{provider}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/identity-providers/{provider}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/invoice-items/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/invoice-items/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/invoice-items/costs/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: compensation
              - New required property: incurred
            - Properties changed
              - New property: compensation
              - New property: incurred
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/invoice-items/costs/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/invoice-items/customer_costs_for_period/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/invoice-items/customer_costs_for_period/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/invoice-items/project_costs_for_period/

- New query param: resource_uuid
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/invoice-items/project_costs_for_period/

- New query param: resource_uuid
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/invoice-items/total_price/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/invoice-items/total_price/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/invoice-items/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/invoice-items/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/invoice-items/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/invoice-items/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/invoice-items/{uuid}/consumptions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/invoice-items/{uuid}/create_compensation/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/invoice-items/{uuid}/migrate_to/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/invoice/send-financial-report-by-mail/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/invoices/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/invoices/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/invoices/growth/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/invoices/growth/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/invoices/import_usage/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/invoices/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/invoices/{uuid}/history/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/invoices/{uuid}/history/at/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/invoices/{uuid}/items/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/invoices/{uuid}/paid/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/invoices/{uuid}/send_notification/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/invoices/{uuid}/set_backend_id/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/invoices/{uuid}/set_payment_url/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/invoices/{uuid}/set_reference_number/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/invoices/{uuid}/stats/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/keycloak-groups/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/keycloak-groups/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/keycloak-groups/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/keycloak-user-group-memberships/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/keycloak-user-group-memberships/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/keycloak-user-group-memberships/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/keycloak-user-group-memberships/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/keycloak-user-group-memberships/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/keycloak-user-group-memberships/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/keycloak-user-group-memberships/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/keys/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/keys/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/keys/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/keys/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/keys/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/keys/{uuid}/history/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/keys/{uuid}/history/at/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/lexis-links/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/lexis-links/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/lexis-links/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/lexis-links/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/lexis-links/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/lexis-links/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/lexis-links/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/maintenance-announcement-offerings/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/maintenance-announcement-offerings/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/maintenance-announcement-offerings/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/maintenance-announcement-offerings/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/maintenance-announcement-offerings/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/maintenance-announcement-offerings/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/maintenance-announcement-offerings/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/maintenance-announcement-template-offerings/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/maintenance-announcement-template-offerings/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/maintenance-announcement-template-offerings/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/maintenance-announcement-template-offerings/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/maintenance-announcement-template-offerings/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/maintenance-announcement-template-offerings/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/maintenance-announcement-template-offerings/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/maintenance-announcements-template/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/maintenance-announcements-template/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/maintenance-announcements-template/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/maintenance-announcements-template/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/maintenance-announcements-template/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/maintenance-announcements-template/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/maintenance-announcements-template/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/maintenance-announcements/

- New query param: timing_bucket
- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-overrun_minutes -start_delta_minutes overrun_minutes start_delta_minutes]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: overrun_minutes
              - New required property: start_delta_minutes
              - New required property: timing_bucket
            - Properties changed
              - New property: overrun_minutes
              - New property: start_delta_minutes
              - New property: timing_bucket
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/maintenance-announcements/

- New query param: timing_bucket
- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-overrun_minutes -start_delta_minutes overrun_minutes start_delta_minutes]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/maintenance-announcements/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: overrun_minutes
            - New required property: start_delta_minutes
            - New required property: timing_bucket
          - Properties changed
            - New property: overrun_minutes
            - New property: start_delta_minutes
            - New property: timing_bucket
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/maintenance-announcements/maintenance_stats/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: summary
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MaintenanceStatsSummary
                  - Required changed
                    - New required property: avg_overrun_hours
                    - New required property: emergency_count
                    - New required property: on_time_rate_15min
                  - Properties changed
                    - New property: avg_overrun_hours
                    - New property: emergency_count
                    - New property: on_time_rate_15min
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/maintenance-announcements/maintenance_stats/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/maintenance-announcements/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/maintenance-announcements/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: overrun_minutes
            - New required property: start_delta_minutes
            - New required property: timing_bucket
          - Properties changed
            - New property: overrun_minutes
            - New property: start_delta_minutes
            - New property: timing_bucket
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/maintenance-announcements/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: overrun_minutes
            - New required property: start_delta_minutes
            - New required property: timing_bucket
          - Properties changed
            - New property: overrun_minutes
            - New property: start_delta_minutes
            - New property: timing_bucket
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/maintenance-announcements/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: overrun_minutes
            - New required property: start_delta_minutes
            - New required property: timing_bucket
          - Properties changed
            - New property: overrun_minutes
            - New property: start_delta_minutes
            - New property: timing_bucket
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/maintenance-announcements/{uuid}/cancel_maintenance/

- Extensions changed
  - New extension: x-permissions
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/maintenance-announcements/{uuid}/complete_maintenance/

- Extensions changed
  - New extension: x-permissions
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/maintenance-announcements/{uuid}/schedule/

- Extensions changed
  - New extension: x-permissions
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/maintenance-announcements/{uuid}/start_maintenance/

- Extensions changed
  - New extension: x-permissions
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/maintenance-announcements/{uuid}/unschedule/

- Extensions changed
  - New extension: x-permissions
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/managed-rancher-cluster-resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [has_api_keys resource_effective_end_date usage_limit_restriction]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: has_api_keys
              - New property: resource_effective_end_date
              - New property: usage_limit_restriction
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: consumer_message_updated_at
                      - New property: created_by_organization_address
                      - New property: created_by_organization_country
                      - New property: created_by_organization_vat_code
                      - New property: provider_message_updated_at
              - Modified property: limit_usage
                - Description changed from 'Dictionary mapping limit-based component types to their consumed usage. For monthly periods, maps from current_usages; for longer periods, aggregates historical usage.' to 'Dictionary mapping limit-based component types to their consumed usage. Sums the ComponentUsage rows of the component's current period (the monthly billing period unless the component defines a longer limit_period), i.e. the period's high-watermark rather than the instantaneous current_usages value.'
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: consumer_message_updated_at
                      - New property: created_by_organization_address
                      - New property: created_by_organization_country
                      - New property: created_by_organization_vat_code
                      - New property: provider_message_updated_at
              - Modified property: project_effective_end_date
                - Description changed from 'Effective project end date including grace period. After this date, resources will be terminated.' to 'Effective project end date including grace period. After this date, resources are terminated, except resources of offerings that disable the grace period — those are terminated on the raw project end date.'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/managed-rancher-cluster-resources/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/managed-rancher-cluster-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [has_api_keys resource_effective_end_date usage_limit_restriction]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_api_keys
            - New property: resource_effective_end_date
            - New property: usage_limit_restriction
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message_updated_at
                    - New property: created_by_organization_address
                    - New property: created_by_organization_country
                    - New property: created_by_organization_vat_code
                    - New property: provider_message_updated_at
            - Modified property: limit_usage
              - Description changed from 'Dictionary mapping limit-based component types to their consumed usage. For monthly periods, maps from current_usages; for longer periods, aggregates historical usage.' to 'Dictionary mapping limit-based component types to their consumed usage. Sums the ComponentUsage rows of the component's current period (the monthly billing period unless the component defines a longer limit_period), i.e. the period's high-watermark rather than the instantaneous current_usages value.'
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message_updated_at
                    - New property: created_by_organization_address
                    - New property: created_by_organization_country
                    - New property: created_by_organization_vat_code
                    - New property: provider_message_updated_at
            - Modified property: project_effective_end_date
              - Description changed from 'Effective project end date including grace period. After this date, resources will be terminated.' to 'Effective project end date including grace period. After this date, resources are terminated, except resources of offerings that disable the grace period — those are terminated on the raw project end date.'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/managed-rancher-cluster-resources/{uuid}/add_node/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-article-code-update/apply/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-article-code-update/preview/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-attribute-options/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-attribute-options/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-attribute-options/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-attribute-options/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-attribute-options/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-attribute-options/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-attribute-options/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-attributes/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-attributes/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-attributes/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-attributes/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-attributes/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-attributes/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-attributes/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-bookings/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-categories/

- New query param: accessible
- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [default_tenant_category]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Deleted property: default_tenant_category
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-categories/

- New query param: accessible
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-categories/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: default_tenant_category
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Deleted property: default_tenant_category
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Deleted property: default_tenant_category
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: default_tenant_category
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-categories/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-categories/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [default_tenant_category]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: default_tenant_category
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-categories/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: default_tenant_category
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Deleted property: default_tenant_category
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Deleted property: default_tenant_category
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: default_tenant_category
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-categories/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: default_tenant_category
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Deleted property: default_tenant_category
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Deleted property: default_tenant_category
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: default_tenant_category
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-category-columns/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-category-columns/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-category-columns/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-category-columns/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-category-columns/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-category-columns/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-category-columns/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-category-component-usages/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-category-component-usages/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-category-component-usages/{id}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-category-components/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-category-components/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-category-components/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-category-components/{id}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-category-components/{id}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-category-components/{id}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-category-components/{id}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-category-groups/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-category-groups/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-category-groups/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-category-groups/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-category-groups/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-category-groups/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-category-groups/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-category-help-articles/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-category-help-articles/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-category-help-articles/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-category-help-articles/{id}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-category-help-articles/{id}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-category-help-articles/{id}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-category-help-articles/{id}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-chat/click/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-chat/feedback/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-chat/stream/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-component-usage-monthly/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-component-usage-monthly/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-component-usages/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-component-usages/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-component-usages/set_usage/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-component-usages/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-component-usages/{uuid}/set_user_usage/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-component-usages/{uuid}/set_user_usages/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-component-user-usages/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-component-user-usages/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-component-user-usages/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-course-accounts/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-course-accounts/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-course-accounts/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-course-accounts/create_bulk/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-course-accounts/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-course-accounts/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-course-accounts/{uuid}/retry/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-customer-component-usage-policies/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-customer-component-usage-policies/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-customer-component-usage-policies/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-customer-component-usage-policies/actions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-customer-component-usage-policies/actions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-customer-component-usage-policies/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-customer-component-usage-policies/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-customer-component-usage-policies/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-customer-component-usage-policies/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-customer-estimated-cost-policies/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-customer-estimated-cost-policies/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-customer-estimated-cost-policies/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-customer-estimated-cost-policies/actions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-customer-estimated-cost-policies/actions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-customer-estimated-cost-policies/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-customer-estimated-cost-policies/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-customer-estimated-cost-policies/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-customer-estimated-cost-policies/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-customer-service-accounts/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-customer-service-accounts/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-customer-service-accounts/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-customer-service-accounts/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-customer-service-accounts/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-customer-service-accounts/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-customer-service-accounts/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-customer-service-accounts/{uuid}/rotate_api_key/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-customer-usage/{uuid}/components-usage-by-project/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-customer-usage/{uuid}/components-usage-timeseries/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-customer-usage/{uuid}/components-usage/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-demo-presets/info/{name}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-demo-presets/info/{name}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-demo-presets/list/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-demo-presets/list/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-demo-presets/load/{name}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-global-categories/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-integration-statuses/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-integration-statuses/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-integration-statuses/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-offering-estimated-cost-policies/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-offering-estimated-cost-policies/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-offering-estimated-cost-policies/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-offering-estimated-cost-policies/actions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-offering-estimated-cost-policies/actions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-offering-estimated-cost-policies/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-offering-estimated-cost-policies/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-offering-estimated-cost-policies/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-offering-estimated-cost-policies/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-offering-files/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-offering-files/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-offering-files/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-offering-files/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-offering-files/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-offering-groups/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-offering-groups/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-offering-groups/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-offering-groups/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-offering-groups/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-offering-groups/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-offering-groups/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-offering-permissions-log/

- New query param: customer_uuid
- New query param: is_active
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-offering-permissions-log/

- New query param: customer_uuid
- New query param: is_active
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-offering-permissions-log/{id}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-offering-permissions/

- New query param: customer_uuid
- New query param: is_active
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-offering-permissions/

- New query param: customer_uuid
- New query param: is_active
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-offering-permissions/{id}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-offering-profiles/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-offering-profiles/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-offering-profiles/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-offering-profiles/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-offering-profiles/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-offering-profiles/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-offering-profiles/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-offering-profiles/{uuid}/add_role/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-offering-profiles/{uuid}/remove_role/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-offering-referrals/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-offering-referrals/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-offering-referrals/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-offering-roles/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-offering-roles/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-offering-roles/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-offering-roles/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-offering-roles/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-offering-roles/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-offering-roles/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-offering-terms-of-service/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-offering-terms-of-service/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-offering-terms-of-service/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-offering-terms-of-service/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-offering-terms-of-service/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-offering-terms-of-service/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-offering-terms-of-service/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-offering-usage-policies/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-offering-usage-policies/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-offering-usage-policies/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-offering-usage-policies/actions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-offering-usage-policies/actions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-offering-usage-policies/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-offering-usage-policies/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-offering-usage-policies/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-offering-usage-policies/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-offering-user-checklist-completions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-offering-user-checklist-completions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-offering-user-checklist-completions/{id}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-offering-users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [home_directory login_shell primarygroup uidnumber user_organization_address user_organization_vat_code user_primary_gid user_uid_number]
- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-user_first_name -user_last_name user_first_name user_last_name]
- Modified query param: query
  - Description changed from 'Search by offering name, username or user name' to 'Search by offering name, username, user name, UID or primary GID'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: home_directory
              - New property: login_shell
              - New property: primarygroup
              - New property: uidnumber
              - New property: user_organization_address
              - New property: user_organization_vat_code
              - New property: user_primary_gid
              - New property: user_uid_number
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-offering-users/

- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-user_first_name -user_last_name user_first_name user_last_name]
- Modified query param: query
  - Description changed from 'Search by offering name, username or user name' to 'Search by offering name, username, user name, UID or primary GID'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-offering-users/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: home_directory
            - New property: login_shell
            - New property: primarygroup
            - New property: uidnumber
            - New property: user_organization_address
            - New property: user_organization_vat_code
            - New property: user_primary_gid
            - New property: user_uid_number
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-offering-users/checklist-template/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-offering-users/checklist-template/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-offering-users/profile_field_warnings/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-offering-users/profile_field_warnings/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-offering-users/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-offering-users/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [home_directory login_shell primarygroup uidnumber user_organization_address user_organization_vat_code user_primary_gid user_uid_number]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: home_directory
            - New property: login_shell
            - New property: primarygroup
            - New property: uidnumber
            - New property: user_organization_address
            - New property: user_organization_vat_code
            - New property: user_primary_gid
            - New property: user_uid_number
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-offering-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: home_directory
            - New property: login_shell
            - New property: primarygroup
            - New property: uidnumber
            - New property: user_organization_address
            - New property: user_organization_vat_code
            - New property: user_primary_gid
            - New property: user_uid_number
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-offering-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: home_directory
            - New property: login_shell
            - New property: primarygroup
            - New property: uidnumber
            - New property: user_organization_address
            - New property: user_organization_vat_code
            - New property: user_primary_gid
            - New property: user_uid_number
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-offering-users/{uuid}/begin_creating/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-offering-users/{uuid}/checklist/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-offering-users/{uuid}/checklist_review/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-offering-users/{uuid}/completion_review_status/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-offering-users/{uuid}/completion_status/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-offering-users/{uuid}/request_deletion/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-offering-users/{uuid}/set_deleted/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-offering-users/{uuid}/set_deleting/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-offering-users/{uuid}/set_error_creating/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-offering-users/{uuid}/set_error_deleting/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-offering-users/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-offering-users/{uuid}/set_pending_account_linking/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-offering-users/{uuid}/set_pending_additional_validation/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-offering-users/{uuid}/set_validation_complete/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-offering-users/{uuid}/submit_answers/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-offering-users/{uuid}/update_comments/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-offering-users/{uuid}/update_restricted/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-offering-users/{uuid}/update_runtime_state/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-orders/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [consumer_message_updated_at created_by_organization_address created_by_organization_country created_by_organization_vat_code provider_message_updated_at]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: consumer_message_updated_at
              - New property: created_by_organization_address
              - New property: created_by_organization_country
              - New property: created_by_organization_vat_code
              - New property: provider_message_updated_at
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-orders/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-orders/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: type
          - Modified property: attributes
            - Property 'OneOf' changed
              - Modified schema: #/components/schemas/OpenStackInstanceCreateOrderAttributes
                - Properties changed
                  - Modified property: name
                    - MaxLength changed from 150 to 255
                  - Modified property: user_data
                    - Description changed from 'Additional data that will be added to instance on provisioning' to 'Cloud-init user data passed to the instance on provisioning. SECURITY: this value is stored and transmitted in plain text — it is kept unencrypted in Waldur's database, forwarded to OpenStack where any process on the instance can read it via the metadata service, and it may appear in logs. Do NOT put unencrypted secrets (passwords, private keys, API tokens) here; reference a secrets manager or inject them through an encrypted channel instead.'
              - Modified schema: #/components/schemas/OpenStackVolumeCreateOrderAttributes
                - Properties changed
                  - Modified property: name
                    - MaxLength changed from 150 to 255
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: consumer_message_updated_at
            - New property: created_by_organization_address
            - New property: created_by_organization_country
            - New property: created_by_organization_vat_code
            - New property: provider_message_updated_at
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-orders/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-orders/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [consumer_message_updated_at created_by_organization_address created_by_organization_country created_by_organization_vat_code provider_message_updated_at]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: consumer_message_updated_at
            - New property: created_by_organization_address
            - New property: created_by_organization_country
            - New property: created_by_organization_vat_code
            - New property: provider_message_updated_at
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-orders/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-orders/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-orders/{uuid}/approve_by_consumer/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-orders/{uuid}/approve_by_provider/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-orders/{uuid}/cancel/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-orders/{uuid}/delete_attachment/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-orders/{uuid}/offering/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [default_access_subnets open_for_proposals qos_profiles]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: default_access_subnets
            - New property: open_for_proposals
            - New property: qos_profiles
            - Modified property: partitions
              - Items changed
                - Properties changed
                  - New property: qos_options
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: discount_aggregation
                        - New property: discount_formula
                        - Deleted property: discount_rate
                        - Deleted property: discount_threshold
                        - Deleted property: discounted_price
                  - Modified property: description
                    - MaxLength changed from null to 4096
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: action_on_usage_limit
                    - New property: auto_approve_for_roles
                    - New property: billing_source
                    - New property: conceal_subnet_restricted_resources
                    - New property: disable_grace_period
                    - New property: emit_display_name
                    - New property: emit_waldur_username
                    - New property: enable_membership_sync_status
                    - New property: enable_posix_account
                    - New property: enable_resource_access_subnets
                    - New property: enable_resource_end_date_change_requests
                    - New property: enforce_qos
                    - New property: gid_source
                    - New property: login_shell
                    - New property: resource_projects_limit_policy
                    - New property: restricted_to_roles
                    - New property: show_ssh_key_loss_warning
                    - New property: uid_source
                    - Deleted property: initial_primarygroup_number
                    - Deleted property: initial_rolegroup_number
                    - Deleted property: initial_uidnumber
                    - Deleted property: initial_usergroup_number
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: enabled_cpu_family
                    - Type changed from 'object' to 'array'
                    - AdditionalProperties changed from true to null
                    - Items changed
                      - Schema added
                  - Modified property: enabled_cpu_microarchitectures
                    - Type changed from 'object' to 'array'
                    - AdditionalProperties changed from true to null
                    - Items changed
                      - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-orders/{uuid}/reject_by_consumer/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-orders/{uuid}/reject_by_provider/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-orders/{uuid}/resource/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [has_api_keys resource_effective_end_date usage_limit_restriction]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_api_keys
            - New property: resource_effective_end_date
            - New property: usage_limit_restriction
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message_updated_at
                    - New property: created_by_organization_address
                    - New property: created_by_organization_country
                    - New property: created_by_organization_vat_code
                    - New property: provider_message_updated_at
            - Modified property: limit_usage
              - Description changed from 'Dictionary mapping limit-based component types to their consumed usage. For monthly periods, maps from current_usages; for longer periods, aggregates historical usage.' to 'Dictionary mapping limit-based component types to their consumed usage. Sums the ComponentUsage rows of the component's current period (the monthly billing period unless the component defines a longer limit_period), i.e. the period's high-watermark rather than the instantaneous current_usages value.'
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message_updated_at
                    - New property: created_by_organization_address
                    - New property: created_by_organization_country
                    - New property: created_by_organization_vat_code
                    - New property: provider_message_updated_at
            - Modified property: project_effective_end_date
              - Description changed from 'Effective project end date including grace period. After this date, resources will be terminated.' to 'Effective project end date including grace period. After this date, resources are terminated, except resources of offerings that disable the grace period — those are terminated on the raw project end date.'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-orders/{uuid}/retry/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-orders/{uuid}/set_backend_id/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-orders/{uuid}/set_consumer_info/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-orders/{uuid}/set_provider_info/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-orders/{uuid}/set_state_done/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-orders/{uuid}/set_state_erred/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-orders/{uuid}/set_state_executing/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-orders/{uuid}/unlink/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-orders/{uuid}/update_attachment/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-plan-components/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: discount_aggregation
              - New property: discount_formula
              - Deleted property: discount_rate
              - Deleted property: discount_threshold
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-plan-components/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-plan-components/{id}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: discount_aggregation
            - New property: discount_formula
            - Deleted property: discount_rate
            - Deleted property: discount_threshold
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

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
                    - New property: discount_aggregation
                    - New property: discount_formula
                    - Deleted property: discount_rate
                    - Deleted property: discount_threshold
                    - Deleted property: discounted_price
              - Modified property: description
                - MaxLength changed from null to 4096
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-plans/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-plans/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from null to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: discount_aggregation
                  - New property: discount_formula
                  - Deleted property: discount_rate
                  - Deleted property: discount_threshold
                  - Deleted property: discounted_price
            - Modified property: description
              - MaxLength changed from null to 4096
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-plans/usage_stats/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-plans/usage_stats/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-plans/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

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
                  - New property: discount_aggregation
                  - New property: discount_formula
                  - Deleted property: discount_rate
                  - Deleted property: discount_threshold
                  - Deleted property: discounted_price
            - Modified property: description
              - MaxLength changed from null to 4096
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-plans/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from null to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: discount_aggregation
                  - New property: discount_formula
                  - Deleted property: discount_rate
                  - Deleted property: discount_threshold
                  - Deleted property: discounted_price
            - Modified property: description
              - MaxLength changed from null to 4096
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-plans/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from null to 4096
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: discount_aggregation
                  - New property: discount_formula
                  - Deleted property: discount_rate
                  - Deleted property: discount_threshold
                  - Deleted property: discounted_price
            - Modified property: description
              - MaxLength changed from null to 4096
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-plans/{uuid}/archive/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-plans/{uuid}/delete_organization_groups/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-plans/{uuid}/history/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-plans/{uuid}/history/at/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-plans/{uuid}/update_discounts/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: discounts
            - AdditionalProperties changed
              - Properties changed
                - New property: discount_aggregation
                - New property: discount_formula
                - Deleted property: discount_rate
                - Deleted property: discount_threshold
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-plans/{uuid}/update_organization_groups/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-plans/{uuid}/update_prices/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-plans/{uuid}/update_quotas/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-project-estimated-cost-policies/

- New query param: has_resource
- New query param: resource
- New query param: resource_uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: resource_name
            - Properties changed
              - New property: resource
              - New property: resource_name
              - New property: use_credit
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-project-estimated-cost-policies/

- New query param: has_resource
- New query param: resource
- New query param: resource_uuid
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-project-estimated-cost-policies/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: resource
          - New property: use_credit
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: resource_name
          - Properties changed
            - New property: resource
            - New property: resource_name
            - New property: use_credit
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-project-estimated-cost-policies/actions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-project-estimated-cost-policies/actions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-project-estimated-cost-policies/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-project-estimated-cost-policies/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: resource_name
          - Properties changed
            - New property: resource
            - New property: resource_name
            - New property: use_credit
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-project-estimated-cost-policies/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: resource
          - New property: use_credit
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: resource_name
          - Properties changed
            - New property: resource
            - New property: resource_name
            - New property: use_credit
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-project-estimated-cost-policies/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: resource
          - New property: use_credit
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: resource_name
          - Properties changed
            - New property: resource
            - New property: resource_name
            - New property: use_credit
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-project-order-auto-approvals/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-project-order-auto-approvals/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-project-order-auto-approvals/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-project-order-auto-approvals/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-project-order-auto-approvals/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-project-order-auto-approvals/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-project-order-auto-approvals/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-project-service-accounts/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-project-service-accounts/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-project-service-accounts/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-project-service-accounts/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-project-service-accounts/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-project-service-accounts/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-project-service-accounts/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-project-service-accounts/{uuid}/rotate_api_key/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-project-update-requests/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-project-update-requests/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-project-update-requests/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-project-update-requests/{uuid}/approve/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-project-update-requests/{uuid}/reject/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-project-usage/{uuid}/components-usage-timeseries/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-project-usage/{uuid}/components-usage/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-offerings/

- New query param: accessible
- New query param: consumer_customer_uuid
- New query param: open_for_proposals
- Modified query param: accessible_via_calls
  - Description changed from 'Accessible via calls' to 'Deprecated: offerings accepted on an active call, regardless of whether a proposal can actually be submitted for them. Use open_for_proposals instead.'
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [default_access_subnets qos_profiles]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: default_access_subnets
              - New property: qos_profiles
              - Modified property: partitions
                - Items changed
                  - Properties changed
                    - New property: qos_options
              - Modified property: plans
                - Items changed
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: discount_aggregation
                          - New property: discount_formula
                          - Deleted property: discount_rate
                          - Deleted property: discount_threshold
                          - Deleted property: discounted_price
                    - Modified property: description
                      - MaxLength changed from null to 4096
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: action_on_usage_limit
                      - New property: auto_approve_for_roles
                      - New property: billing_source
                      - New property: conceal_subnet_restricted_resources
                      - New property: disable_grace_period
                      - New property: emit_display_name
                      - New property: emit_waldur_username
                      - New property: enable_membership_sync_status
                      - New property: enable_posix_account
                      - New property: enable_resource_access_subnets
                      - New property: enable_resource_end_date_change_requests
                      - New property: enforce_qos
                      - New property: gid_source
                      - New property: login_shell
                      - New property: resource_projects_limit_policy
                      - New property: restricted_to_roles
                      - New property: show_ssh_key_loss_warning
                      - New property: uid_source
                      - Deleted property: initial_primarygroup_number
                      - Deleted property: initial_rolegroup_number
                      - Deleted property: initial_uidnumber
                      - Deleted property: initial_usergroup_number
              - Modified property: software_catalogs
                - Items changed
                  - Properties changed
                    - Modified property: enabled_cpu_family
                      - Type changed from 'object' to 'array'
                      - AdditionalProperties changed from true to null
                      - Items changed
                        - Schema added
                    - Modified property: enabled_cpu_microarchitectures
                      - Type changed from 'object' to 'array'
                      - AdditionalProperties changed from true to null
                      - Items changed
                        - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-provider-offerings/

- New query param: accessible
- New query param: consumer_customer_uuid
- New query param: open_for_proposals
- Modified query param: accessible_via_calls
  - Description changed from 'Accessible via calls' to 'Deprecated: offerings accepted on an active call, regardless of whether a proposal can actually be submitted for them. Use open_for_proposals instead.'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from null to 4096
          - Modified property: plans
            - Items changed
              - Properties changed
                - Modified property: description
                  - MaxLength changed from null to 4096
          - Modified property: plugin_options
            - Properties changed
              - New property: action_on_usage_limit
              - New property: auto_approve_for_roles
              - New property: billing_source
              - New property: conceal_subnet_restricted_resources
              - New property: disable_grace_period
              - New property: emit_display_name
              - New property: emit_waldur_username
              - New property: enable_membership_sync_status
              - New property: enable_posix_account
              - New property: enable_resource_access_subnets
              - New property: enable_resource_end_date_change_requests
              - New property: enforce_qos
              - New property: gid_source
              - New property: login_shell
              - New property: resource_projects_limit_policy
              - New property: restricted_to_roles
              - New property: show_ssh_key_loss_warning
              - New property: uid_source
              - Deleted property: initial_primarygroup_number
              - Deleted property: initial_rolegroup_number
              - Deleted property: initial_uidnumber
              - Deleted property: initial_usergroup_number
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from null to 4096
          - Modified property: plans
            - Items changed
              - Properties changed
                - Modified property: description
                  - MaxLength changed from null to 4096
          - Modified property: plugin_options
            - Properties changed
              - New property: action_on_usage_limit
              - New property: auto_approve_for_roles
              - New property: billing_source
              - New property: conceal_subnet_restricted_resources
              - New property: disable_grace_period
              - New property: emit_display_name
              - New property: emit_waldur_username
              - New property: enable_membership_sync_status
              - New property: enable_posix_account
              - New property: enable_resource_access_subnets
              - New property: enable_resource_end_date_change_requests
              - New property: enforce_qos
              - New property: gid_source
              - New property: login_shell
              - New property: resource_projects_limit_policy
              - New property: restricted_to_roles
              - New property: show_ssh_key_loss_warning
              - New property: uid_source
              - Deleted property: initial_primarygroup_number
              - Deleted property: initial_rolegroup_number
              - Deleted property: initial_uidnumber
              - Deleted property: initial_usergroup_number
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from null to 4096
          - Modified property: plans
            - Items changed
              - Properties changed
                - Modified property: description
                  - MaxLength changed from null to 4096
          - Modified property: plugin_options
            - Properties changed
              - New property: action_on_usage_limit
              - New property: auto_approve_for_roles
              - New property: billing_source
              - New property: conceal_subnet_restricted_resources
              - New property: disable_grace_period
              - New property: emit_display_name
              - New property: emit_waldur_username
              - New property: enable_membership_sync_status
              - New property: enable_posix_account
              - New property: enable_resource_access_subnets
              - New property: enable_resource_end_date_change_requests
              - New property: enforce_qos
              - New property: gid_source
              - New property: login_shell
              - New property: resource_projects_limit_policy
              - New property: restricted_to_roles
              - New property: show_ssh_key_loss_warning
              - New property: uid_source
              - Deleted property: initial_primarygroup_number
              - Deleted property: initial_rolegroup_number
              - Deleted property: initial_uidnumber
              - Deleted property: initial_usergroup_number
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: default_access_subnets
            - New property: qos_profiles
            - Modified property: partitions
              - Items changed
                - Properties changed
                  - New property: qos_options
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: discount_aggregation
                        - New property: discount_formula
                        - Deleted property: discount_rate
                        - Deleted property: discount_threshold
                        - Deleted property: discounted_price
                  - Modified property: description
                    - MaxLength changed from null to 4096
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: action_on_usage_limit
                    - New property: auto_approve_for_roles
                    - New property: billing_source
                    - New property: conceal_subnet_restricted_resources
                    - New property: disable_grace_period
                    - New property: emit_display_name
                    - New property: emit_waldur_username
                    - New property: enable_membership_sync_status
                    - New property: enable_posix_account
                    - New property: enable_resource_access_subnets
                    - New property: enable_resource_end_date_change_requests
                    - New property: enforce_qos
                    - New property: gid_source
                    - New property: login_shell
                    - New property: resource_projects_limit_policy
                    - New property: restricted_to_roles
                    - New property: show_ssh_key_loss_warning
                    - New property: uid_source
                    - Deleted property: initial_primarygroup_number
                    - Deleted property: initial_rolegroup_number
                    - Deleted property: initial_uidnumber
                    - Deleted property: initial_usergroup_number
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: enabled_cpu_family
                    - Type changed from 'object' to 'array'
                    - AdditionalProperties changed from true to null
                    - Items changed
                      - Schema added
                  - Modified property: enabled_cpu_microarchitectures
                    - Type changed from 'object' to 'array'
                    - AdditionalProperties changed from true to null
                    - Items changed
                      - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-offerings/groups/

- New query param: accessible
- New query param: consumer_customer_uuid
- New query param: open_for_proposals
- Modified query param: accessible_via_calls
  - Description changed from 'Accessible via calls' to 'Deprecated: offerings accepted on an active call, regardless of whether a proposal can actually be submitted for them. Use open_for_proposals instead.'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-provider-offerings/groups/

- New query param: accessible
- New query param: consumer_customer_uuid
- New query param: open_for_proposals
- Modified query param: accessible_via_calls
  - Description changed from 'Accessible via calls' to 'Deprecated: offerings accepted on an active call, regardless of whether a proposal can actually be submitted for them. Use open_for_proposals instead.'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/import_offering/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-provider-offerings/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [default_access_subnets qos_profiles]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: default_access_subnets
            - New property: qos_profiles
            - Modified property: partitions
              - Items changed
                - Properties changed
                  - New property: qos_options
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: discount_aggregation
                        - New property: discount_formula
                        - Deleted property: discount_rate
                        - Deleted property: discount_threshold
                        - Deleted property: discounted_price
                  - Modified property: description
                    - MaxLength changed from null to 4096
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: action_on_usage_limit
                    - New property: auto_approve_for_roles
                    - New property: billing_source
                    - New property: conceal_subnet_restricted_resources
                    - New property: disable_grace_period
                    - New property: emit_display_name
                    - New property: emit_waldur_username
                    - New property: enable_membership_sync_status
                    - New property: enable_posix_account
                    - New property: enable_resource_access_subnets
                    - New property: enable_resource_end_date_change_requests
                    - New property: enforce_qos
                    - New property: gid_source
                    - New property: login_shell
                    - New property: resource_projects_limit_policy
                    - New property: restricted_to_roles
                    - New property: show_ssh_key_loss_warning
                    - New property: uid_source
                    - Deleted property: initial_primarygroup_number
                    - Deleted property: initial_rolegroup_number
                    - Deleted property: initial_uidnumber
                    - Deleted property: initial_usergroup_number
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: enabled_cpu_family
                    - Type changed from 'object' to 'array'
                    - AdditionalProperties changed from true to null
                    - Items changed
                      - Schema added
                  - Modified property: enabled_cpu_microarchitectures
                    - Type changed from 'object' to 'array'
                    - AdditionalProperties changed from true to null
                    - Items changed
                      - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/activate/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/add_endpoint/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/add_partition/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: qos_options
          - Properties changed
            - New property: qos_options
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/add_software_catalog/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: enabled_cpu_family
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: enabled_cpu_microarchitectures
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/add_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/archive/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/check_unique_backend_id/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-offerings/{uuid}/component_stats/

- New query param: accessible
- New query param: consumer_customer_uuid
- New query param: open_for_proposals
- Modified query param: accessible_via_calls
  - Description changed from 'Accessible via calls' to 'Deprecated: offerings accepted on an active call, regardless of whether a proposal can actually be submitted for them. Use open_for_proposals instead.'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-offerings/{uuid}/costs/

- New query param: accessible
- New query param: consumer_customer_uuid
- New query param: open_for_proposals
- Modified query param: accessible_via_calls
  - Description changed from 'Accessible via calls' to 'Deprecated: offerings accepted on an active call, regardless of whether a proposal can actually be submitted for them. Use open_for_proposals instead.'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/create_offering_component/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-offerings/{uuid}/customers/

- New query param: accessible
- New query param: consumer_customer_uuid
- New query param: open_for_proposals
- Modified query param: accessible_via_calls
  - Description changed from 'Accessible via calls' to 'Deprecated: offerings accepted on an active call, regardless of whether a proposal can actually be submitted for them. Use open_for_proposals instead.'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-provider-offerings/{uuid}/delete-user-attribute-config/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/delete_endpoint/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/delete_image/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/delete_organization_groups/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/delete_tags/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/delete_thumbnail/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/delete_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/draft/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/export_offering/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-offerings/{uuid}/glauth_tree/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: groups
              - Items changed
                - Properties changed
                  - Modified property: kind
                    - New enum values: [personal]
                  - Modified property: scope
                    - Properties changed
                      - Modified property: type
                        - New enum values: [user]
            - Modified property: users
              - Items changed
                - Properties changed
                  - Modified property: memberships
                    - Items changed
                      - Properties changed
                        - Modified property: kind
                          - New enum values: [personal]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-offerings/{uuid}/glauth_users_config/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-offerings/{uuid}/history/

- New query param: accessible
- New query param: consumer_customer_uuid
- New query param: open_for_proposals
- Modified query param: accessible_via_calls
  - Description changed from 'Accessible via calls' to 'Deprecated: offerings accepted on an active call, regardless of whether a proposal can actually be submitted for them. Use open_for_proposals instead.'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-offerings/{uuid}/history/at/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/import_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_api_keys
            - New property: resource_effective_end_date
            - New property: usage_limit_restriction
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message_updated_at
                    - New property: created_by_organization_address
                    - New property: created_by_organization_country
                    - New property: created_by_organization_vat_code
                    - New property: provider_message_updated_at
            - Modified property: limit_usage
              - Description changed from 'Dictionary mapping limit-based component types to their consumed usage. For monthly periods, maps from current_usages; for longer periods, aggregates historical usage.' to 'Dictionary mapping limit-based component types to their consumed usage. Sums the ComponentUsage rows of the component's current period (the monthly billing period unless the component defines a longer limit_period), i.e. the period's high-watermark rather than the instantaneous current_usages value.'
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message_updated_at
                    - New property: created_by_organization_address
                    - New property: created_by_organization_country
                    - New property: created_by_organization_vat_code
                    - New property: provider_message_updated_at
            - Modified property: project_effective_end_date
              - Description changed from 'Effective project end date including grace period. After this date, resources will be terminated.' to 'Effective project end date including grace period. After this date, resources are terminated, except resources of offerings that disable the grace period — those are terminated on the raw project end date.'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-offerings/{uuid}/importable_resources/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-offerings/{uuid}/list_course_accounts/

- New query param: accessible
- New query param: consumer_customer_uuid
- New query param: open_for_proposals
- Modified query param: accessible_via_calls
  - Description changed from 'Accessible via calls' to 'Deprecated: offerings accepted on an active call, regardless of whether a proposal can actually be submitted for them. Use open_for_proposals instead.'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-offerings/{uuid}/list_customer_projects/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from null to 4096
              - Modified property: project_metadata
                - Items changed
                  - Properties changed
                    - Modified property: answer
                      - Type changed from 'object' to ''
                      - AdditionalProperties changed from true to null
              - Modified property: staff_notes
                - MaxLength changed from null to 4096
              - Modified property: user_affiliations
                - Type changed from 'object' to 'array'
                - AdditionalProperties changed from true to null
                - Items changed
                  - Schema added
              - Modified property: user_email_patterns
                - Type changed from 'object' to 'array'
                - AdditionalProperties changed from true to null
                - Items changed
                  - Schema added
              - Modified property: user_identity_sources
                - Type changed from 'object' to 'array'
                - Description changed from 'List of allowed identity sources (identity providers).' to ''
                - AdditionalProperties changed from true to null
                - Items changed
                  - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-offerings/{uuid}/list_customer_service_accounts/

- New query param: accessible
- New query param: consumer_customer_uuid
- New query param: open_for_proposals
- Modified query param: accessible_via_calls
  - Description changed from 'Accessible via calls' to 'Deprecated: offerings accepted on an active call, regardless of whether a proposal can actually be submitted for them. Use open_for_proposals instead.'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-offerings/{uuid}/list_customer_users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [organization_address organization_vat_code primary_gid uid_number]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: organization_address
              - New property: organization_vat_code
              - New property: primary_gid
              - New property: uid_number
              - Modified property: permissions
                - Items changed
                  - Properties changed
                    - New property: is_active
                    - New property: revoke_reason
                    - New property: revoked_by_full_name
                    - New property: revoked_by_username
                    - New property: scope_is_removed
                    - New property: user_email
                    - New property: user_username
                    - New property: uuid
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-offerings/{uuid}/list_project_service_accounts/

- New query param: accessible
- New query param: consumer_customer_uuid
- New query param: open_for_proposals
- Modified query param: accessible_via_calls
  - Description changed from 'Accessible via calls' to 'Deprecated: offerings accepted on an active call, regardless of whether a proposal can actually be submitted for them. Use open_for_proposals instead.'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-offerings/{uuid}/list_users/

- Modified query param: role
  - Description changed from 'Role UUID or name' to 'Role UUID or name. Repeat to filter by several roles.'
  - Schema changed
    - Type changed from 'string' to 'array'
    - Format changed from 'uuid' to ''
    - Items changed
      - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/make_available/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/make_unavailable/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/move_offering/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: default_access_subnets
            - New property: open_for_proposals
            - New property: qos_profiles
            - Modified property: partitions
              - Items changed
                - Properties changed
                  - New property: qos_options
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: discount_aggregation
                        - New property: discount_formula
                        - Deleted property: discount_rate
                        - Deleted property: discount_threshold
                        - Deleted property: discounted_price
                  - Modified property: description
                    - MaxLength changed from null to 4096
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: action_on_usage_limit
                    - New property: auto_approve_for_roles
                    - New property: billing_source
                    - New property: conceal_subnet_restricted_resources
                    - New property: disable_grace_period
                    - New property: emit_display_name
                    - New property: emit_waldur_username
                    - New property: enable_membership_sync_status
                    - New property: enable_posix_account
                    - New property: enable_resource_access_subnets
                    - New property: enable_resource_end_date_change_requests
                    - New property: enforce_qos
                    - New property: gid_source
                    - New property: login_shell
                    - New property: resource_projects_limit_policy
                    - New property: restricted_to_roles
                    - New property: show_ssh_key_loss_warning
                    - New property: uid_source
                    - Deleted property: initial_primarygroup_number
                    - Deleted property: initial_rolegroup_number
                    - Deleted property: initial_uidnumber
                    - Deleted property: initial_usergroup_number
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: enabled_cpu_family
                    - Type changed from 'object' to 'array'
                    - AdditionalProperties changed from true to null
                    - Items changed
                      - Schema added
                  - Modified property: enabled_cpu_microarchitectures
                    - Type changed from 'object' to 'array'
                    - AdditionalProperties changed from true to null
                    - Items changed
                      - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-offerings/{uuid}/orders/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [consumer_message_updated_at created_by_organization_address created_by_organization_country created_by_organization_vat_code provider_message_updated_at]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: consumer_message_updated_at
              - New property: created_by_organization_address
              - New property: created_by_organization_country
              - New property: created_by_organization_vat_code
              - New property: provider_message_updated_at
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-offerings/{uuid}/orders/{order_uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [consumer_message_updated_at created_by_organization_address created_by_organization_country created_by_organization_vat_code provider_message_updated_at]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: consumer_message_updated_at
            - New property: created_by_organization_address
            - New property: created_by_organization_country
            - New property: created_by_organization_vat_code
            - New property: provider_message_updated_at
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/pause/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/refresh_offering_usernames/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/remove_offering_component/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/remove_partition/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/remove_software_catalog/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/set_backend_metadata/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/set_offering_group/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/set_profile/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-offerings/{uuid}/state_counters/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-offerings/{uuid}/stats/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/switch_billing_mode/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/sync/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/sync_resources/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-offerings/{uuid}/tos_stats/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/unpause/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-provider-offerings/{uuid}/update-user-attribute-config/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: expose_organization_address
          - New property: expose_organization_vat_code
          - New property: expose_primary_gid
          - New property: expose_uid_number
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: expose_organization_address
            - New property: expose_organization_vat_code
            - New property: expose_primary_gid
            - New property: expose_uid_number
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/update-user-attribute-config/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: expose_organization_address
          - New property: expose_organization_vat_code
          - New property: expose_primary_gid
          - New property: expose_uid_number
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: expose_organization_address
            - New property: expose_organization_vat_code
            - New property: expose_primary_gid
            - New property: expose_uid_number
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-provider-offerings/{uuid}/update-user-attribute-config/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: expose_organization_address
          - New property: expose_organization_vat_code
          - New property: expose_primary_gid
          - New property: expose_uid_number
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: expose_organization_address
            - New property: expose_organization_vat_code
            - New property: expose_primary_gid
            - New property: expose_uid_number
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/update_attributes/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/update_backend_id_rules/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/update_compliance_checklist/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/update_description/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/update_image/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/update_integration/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: action_on_usage_limit
              - New property: auto_approve_for_roles
              - New property: billing_source
              - New property: conceal_subnet_restricted_resources
              - New property: disable_grace_period
              - New property: emit_display_name
              - New property: emit_waldur_username
              - New property: enable_membership_sync_status
              - New property: enable_posix_account
              - New property: enable_resource_access_subnets
              - New property: enable_resource_end_date_change_requests
              - New property: enforce_qos
              - New property: gid_source
              - New property: login_shell
              - New property: resource_projects_limit_policy
              - New property: restricted_to_roles
              - New property: show_ssh_key_loss_warning
              - New property: uid_source
              - Deleted property: initial_primarygroup_number
              - Deleted property: initial_rolegroup_number
              - Deleted property: initial_uidnumber
              - Deleted property: initial_usergroup_number
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/update_location/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/update_offering_component/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/update_options/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/update_organization_groups/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/update_overview/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from null to 4096
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-provider-offerings/{uuid}/update_partition/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: qos_options
          - Properties changed
            - New property: qos_options
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/update_resource_options/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-provider-offerings/{uuid}/update_software_catalog/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: enabled_cpu_family
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: enabled_cpu_microarchitectures
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: enabled_cpu_family
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: enabled_cpu_microarchitectures
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/update_tags/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/update_thumbnail/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/update_type/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/update_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-offerings/{uuid}/upload_markdown_image/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-offerings/{uuid}/user-attribute-config/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: expose_organization_address
            - New property: expose_organization_vat_code
            - New property: expose_primary_gid
            - New property: expose_uid_number
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-offerings/{uuid}/user_has_resource_access/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-resource-projects/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: created_by_username
            - Properties changed
              - New property: created_by_username
              - Modified property: removed_by_username
                - Description changed from 'Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters' to ''
                - Nullable changed from false to true
              - Modified property: termination_metadata
                - Nullable changed from false to true
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-provider-resource-projects/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-resource-projects/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: created_by_username
          - Properties changed
            - New property: created_by_username
            - Modified property: removed_by_username
              - Description changed from 'Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters' to ''
              - Nullable changed from false to true
            - Modified property: termination_metadata
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-provider-resource-projects/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: created_by_username
          - Properties changed
            - New property: created_by_username
            - Modified property: removed_by_username
              - Description changed from 'Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters' to ''
              - Nullable changed from false to true
            - Modified property: termination_metadata
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-provider-resource-projects/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: created_by_username
          - Properties changed
            - New property: created_by_username
            - Modified property: removed_by_username
              - Description changed from 'Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters' to ''
              - Nullable changed from false to true
            - Modified property: termination_metadata
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-resource-projects/{uuid}/add_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-resource-projects/{uuid}/delete_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-resource-projects/{uuid}/list_users/

- Modified query param: role
  - Description changed from 'Role UUID or name' to 'Role UUID or name. Repeat to filter by several roles.'
  - Schema changed
    - Type changed from 'string' to 'array'
    - Format changed from 'uuid' to ''
    - Items changed
      - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-resource-projects/{uuid}/set_backend_id/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-resource-projects/{uuid}/set_state_erred/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-resource-projects/{uuid}/set_state_ok/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-resource-projects/{uuid}/update_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [has_api_keys resource_effective_end_date usage_limit_restriction]
- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-backend_id -customer_name -offering_name -plan_name backend_id customer_name offering_name plan_name]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: has_api_keys
              - New property: resource_effective_end_date
              - New property: usage_limit_restriction
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: consumer_message_updated_at
                      - New property: created_by_organization_address
                      - New property: created_by_organization_country
                      - New property: created_by_organization_vat_code
                      - New property: provider_message_updated_at
              - Modified property: limit_usage
                - Description changed from 'Dictionary mapping limit-based component types to their consumed usage. For monthly periods, maps from current_usages; for longer periods, aggregates historical usage.' to 'Dictionary mapping limit-based component types to their consumed usage. Sums the ComponentUsage rows of the component's current period (the monthly billing period unless the component defines a longer limit_period), i.e. the period's high-watermark rather than the instantaneous current_usages value.'
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: consumer_message_updated_at
                      - New property: created_by_organization_address
                      - New property: created_by_organization_country
                      - New property: created_by_organization_vat_code
                      - New property: provider_message_updated_at
              - Modified property: project_effective_end_date
                - Description changed from 'Effective project end date including grace period. After this date, resources will be terminated.' to 'Effective project end date including grace period. After this date, resources are terminated, except resources of offerings that disable the grace period — those are terminated on the raw project end date.'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-provider-resources/

- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-backend_id -customer_name -offering_name -plan_name backend_id customer_name offering_name plan_name]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [has_api_keys resource_effective_end_date usage_limit_restriction]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_api_keys
            - New property: resource_effective_end_date
            - New property: usage_limit_restriction
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message_updated_at
                    - New property: created_by_organization_address
                    - New property: created_by_organization_country
                    - New property: created_by_organization_vat_code
                    - New property: provider_message_updated_at
            - Modified property: limit_usage
              - Description changed from 'Dictionary mapping limit-based component types to their consumed usage. For monthly periods, maps from current_usages; for longer periods, aggregates historical usage.' to 'Dictionary mapping limit-based component types to their consumed usage. Sums the ComponentUsage rows of the component's current period (the monthly billing period unless the component defines a longer limit_period), i.e. the period's high-watermark rather than the instantaneous current_usages value.'
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message_updated_at
                    - New property: created_by_organization_address
                    - New property: created_by_organization_country
                    - New property: created_by_organization_vat_code
                    - New property: provider_message_updated_at
            - Modified property: project_effective_end_date
              - Description changed from 'Effective project end date including grace period. After this date, resources will be terminated.' to 'Effective project end date including grace period. After this date, resources are terminated, except resources of offerings that disable the grace period — those are terminated on the raw project end date.'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-provider-resources/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-provider-resources/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-resources/{uuid}/add_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-resources/{uuid}/adjust_dates/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-resources/{uuid}/delete_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-resources/{uuid}/details/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-resources/{uuid}/glauth_tree/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: groups
              - Items changed
                - Properties changed
                  - Modified property: kind
                    - New enum values: [personal]
                  - Modified property: scope
                    - Properties changed
                      - Modified property: type
                        - New enum values: [user]
            - Modified property: users
              - Items changed
                - Properties changed
                  - Modified property: memberships
                    - Items changed
                      - Properties changed
                        - Modified property: kind
                          - New enum values: [personal]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-resources/{uuid}/glauth_users_config/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-resources/{uuid}/history/

- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-backend_id -customer_name -offering_name -plan_name backend_id customer_name offering_name plan_name]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-resources/{uuid}/history/at/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-resources/{uuid}/list_users/

- Modified query param: role
  - Description changed from 'Role UUID or name' to 'Role UUID or name. Repeat to filter by several roles.'
  - Schema changed
    - Type changed from 'string' to 'array'
    - Format changed from 'uuid' to ''
    - Items changed
      - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-resources/{uuid}/move_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_api_keys
            - New property: resource_effective_end_date
            - New property: usage_limit_restriction
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message_updated_at
                    - New property: created_by_organization_address
                    - New property: created_by_organization_country
                    - New property: created_by_organization_vat_code
                    - New property: provider_message_updated_at
            - Modified property: limit_usage
              - Description changed from 'Dictionary mapping limit-based component types to their consumed usage. For monthly periods, maps from current_usages; for longer periods, aggregates historical usage.' to 'Dictionary mapping limit-based component types to their consumed usage. Sums the ComponentUsage rows of the component's current period (the monthly billing period unless the component defines a longer limit_period), i.e. the period's high-watermark rather than the instantaneous current_usages value.'
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message_updated_at
                    - New property: created_by_organization_address
                    - New property: created_by_organization_country
                    - New property: created_by_organization_vat_code
                    - New property: provider_message_updated_at
            - Modified property: project_effective_end_date
              - Description changed from 'Effective project end date including grace period. After this date, resources will be terminated.' to 'Effective project end date including grace period. After this date, resources are terminated, except resources of offerings that disable the grace period — those are terminated on the raw project end date.'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-resources/{uuid}/offering/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [default_access_subnets open_for_proposals qos_profiles]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: default_access_subnets
            - New property: open_for_proposals
            - New property: qos_profiles
            - Modified property: partitions
              - Items changed
                - Properties changed
                  - New property: qos_options
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: discount_aggregation
                        - New property: discount_formula
                        - Deleted property: discount_rate
                        - Deleted property: discount_threshold
                        - Deleted property: discounted_price
                  - Modified property: description
                    - MaxLength changed from null to 4096
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: action_on_usage_limit
                    - New property: auto_approve_for_roles
                    - New property: billing_source
                    - New property: conceal_subnet_restricted_resources
                    - New property: disable_grace_period
                    - New property: emit_display_name
                    - New property: emit_waldur_username
                    - New property: enable_membership_sync_status
                    - New property: enable_posix_account
                    - New property: enable_resource_access_subnets
                    - New property: enable_resource_end_date_change_requests
                    - New property: enforce_qos
                    - New property: gid_source
                    - New property: login_shell
                    - New property: resource_projects_limit_policy
                    - New property: restricted_to_roles
                    - New property: show_ssh_key_loss_warning
                    - New property: uid_source
                    - Deleted property: initial_primarygroup_number
                    - Deleted property: initial_rolegroup_number
                    - Deleted property: initial_uidnumber
                    - Deleted property: initial_usergroup_number
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: enabled_cpu_family
                    - Type changed from 'object' to 'array'
                    - AdditionalProperties changed from true to null
                    - Items changed
                      - Schema added
                  - Modified property: enabled_cpu_microarchitectures
                    - Type changed from 'object' to 'array'
                    - AdditionalProperties changed from true to null
                    - Items changed
                      - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-resources/{uuid}/offering_for_subresources/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-resources/{uuid}/plan_periods/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-resources/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-resources/{uuid}/refresh_last_sync/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-resources/{uuid}/restore/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-resources/{uuid}/set_as_erred/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'offering.customer' to 'offering'
    - Added /0/scopes/- with value: 'offering.customer'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-resources/{uuid}/set_as_ok/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-resources/{uuid}/set_backend_id/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-resources/{uuid}/set_backend_metadata/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-resources/{uuid}/set_downscaled/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-resources/{uuid}/set_effective_id/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-resources/{uuid}/set_end_date/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-resources/{uuid}/set_end_date_by_provider/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-resources/{uuid}/set_end_date_by_staff/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-resources/{uuid}/set_endpoints/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-resources/{uuid}/set_limits/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-resources/{uuid}/set_paused/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-resources/{uuid}/set_restrict_member_access/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-resources/{uuid}/set_slug/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-resources/{uuid}/set_state_ok/

- Extensions changed
  - Modified extension: x-permissions
    - Modified /0/scopes/0 from 'offering.customer' to 'offering'
    - Added /0/scopes/- with value: 'offering.customer'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-resources/{uuid}/submit_report/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-provider-resources/{uuid}/team/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-resources/{uuid}/terminate/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-resources/{uuid}/unlink/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-resources/{uuid}/update_options/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-resources/{uuid}/update_options_direct/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-provider-resources/{uuid}/update_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-public-api/check_signature/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-public-api/set_usage/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-public-offerings/

- New query param: accessible
- New query param: consumer_customer_uuid
- New query param: open_for_proposals
- Modified query param: accessible_via_calls
  - Description changed from 'Accessible via calls' to 'Deprecated: offerings accepted on an active call, regardless of whether a proposal can actually be submitted for them. Use open_for_proposals instead.'
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [default_access_subnets open_for_proposals qos_profiles]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: default_access_subnets
              - New property: open_for_proposals
              - New property: qos_profiles
              - Modified property: partitions
                - Items changed
                  - Properties changed
                    - New property: qos_options
              - Modified property: plans
                - Items changed
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: discount_aggregation
                          - New property: discount_formula
                          - Deleted property: discount_rate
                          - Deleted property: discount_threshold
                          - Deleted property: discounted_price
                    - Modified property: description
                      - MaxLength changed from null to 4096
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: action_on_usage_limit
                      - New property: auto_approve_for_roles
                      - New property: billing_source
                      - New property: conceal_subnet_restricted_resources
                      - New property: disable_grace_period
                      - New property: emit_display_name
                      - New property: emit_waldur_username
                      - New property: enable_membership_sync_status
                      - New property: enable_posix_account
                      - New property: enable_resource_access_subnets
                      - New property: enable_resource_end_date_change_requests
                      - New property: enforce_qos
                      - New property: gid_source
                      - New property: login_shell
                      - New property: resource_projects_limit_policy
                      - New property: restricted_to_roles
                      - New property: show_ssh_key_loss_warning
                      - New property: uid_source
                      - Deleted property: initial_primarygroup_number
                      - Deleted property: initial_rolegroup_number
                      - Deleted property: initial_uidnumber
                      - Deleted property: initial_usergroup_number
              - Modified property: software_catalogs
                - Items changed
                  - Properties changed
                    - Modified property: enabled_cpu_family
                      - Type changed from 'object' to 'array'
                      - AdditionalProperties changed from true to null
                      - Items changed
                        - Schema added
                    - Modified property: enabled_cpu_microarchitectures
                      - Type changed from 'object' to 'array'
                      - AdditionalProperties changed from true to null
                      - Items changed
                        - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-public-offerings/

- New query param: accessible
- New query param: consumer_customer_uuid
- New query param: open_for_proposals
- Modified query param: accessible_via_calls
  - Description changed from 'Accessible via calls' to 'Deprecated: offerings accepted on an active call, regardless of whether a proposal can actually be submitted for them. Use open_for_proposals instead.'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-public-offerings/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [default_access_subnets open_for_proposals qos_profiles]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: default_access_subnets
            - New property: open_for_proposals
            - New property: qos_profiles
            - Modified property: partitions
              - Items changed
                - Properties changed
                  - New property: qos_options
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: discount_aggregation
                        - New property: discount_formula
                        - Deleted property: discount_rate
                        - Deleted property: discount_threshold
                        - Deleted property: discounted_price
                  - Modified property: description
                    - MaxLength changed from null to 4096
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: action_on_usage_limit
                    - New property: auto_approve_for_roles
                    - New property: billing_source
                    - New property: conceal_subnet_restricted_resources
                    - New property: disable_grace_period
                    - New property: emit_display_name
                    - New property: emit_waldur_username
                    - New property: enable_membership_sync_status
                    - New property: enable_posix_account
                    - New property: enable_resource_access_subnets
                    - New property: enable_resource_end_date_change_requests
                    - New property: enforce_qos
                    - New property: gid_source
                    - New property: login_shell
                    - New property: resource_projects_limit_policy
                    - New property: restricted_to_roles
                    - New property: show_ssh_key_loss_warning
                    - New property: uid_source
                    - Deleted property: initial_primarygroup_number
                    - Deleted property: initial_rolegroup_number
                    - Deleted property: initial_uidnumber
                    - Deleted property: initial_usergroup_number
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: enabled_cpu_family
                    - Type changed from 'object' to 'array'
                    - AdditionalProperties changed from true to null
                    - Items changed
                      - Schema added
                  - Modified property: enabled_cpu_microarchitectures
                    - Type changed from 'object' to 'array'
                    - AdditionalProperties changed from true to null
                    - Items changed
                      - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

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
                    - New property: discount_aggregation
                    - New property: discount_formula
                    - Deleted property: discount_rate
                    - Deleted property: discount_threshold
                    - Deleted property: discounted_price
              - Modified property: description
                - MaxLength changed from null to 4096
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

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
                  - New property: discount_aggregation
                  - New property: discount_formula
                  - Deleted property: discount_rate
                  - Deleted property: discount_threshold
                  - Deleted property: discounted_price
            - Modified property: description
              - MaxLength changed from null to 4096
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-related-customers/{customer_uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-remote-synchronisations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-remote-synchronisations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-remote-synchronisations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-remote-synchronisations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-remote-synchronisations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-remote-synchronisations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-remote-synchronisations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-remote-synchronisations/{uuid}/run_synchronisation/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-resource-limit-change-requests/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-resource-limit-change-requests/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-resource-limit-change-requests/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-resource-limit-change-requests/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-resource-limit-change-requests/{uuid}/approve/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-resource-limit-change-requests/{uuid}/cancel/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-resource-limit-change-requests/{uuid}/reject/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-resource-offerings/{category_uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-resource-projects/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: created_by_username
            - Properties changed
              - New property: created_by_username
              - Modified property: removed_by_username
                - Description changed from 'Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters' to ''
                - Nullable changed from false to true
              - Modified property: termination_metadata
                - Nullable changed from false to true
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-resource-projects/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-resource-projects/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: created_by_username
          - Properties changed
            - New property: created_by_username
            - Modified property: removed_by_username
              - Description changed from 'Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters' to ''
              - Nullable changed from false to true
            - Modified property: termination_metadata
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-resource-projects/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-resource-projects/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: created_by_username
          - Properties changed
            - New property: created_by_username
            - Modified property: removed_by_username
              - Description changed from 'Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters' to ''
              - Nullable changed from false to true
            - Modified property: termination_metadata
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-resource-projects/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: created_by_username
          - Properties changed
            - New property: created_by_username
            - Modified property: removed_by_username
              - Description changed from 'Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters' to ''
              - Nullable changed from false to true
            - Modified property: termination_metadata
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-resource-projects/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: created_by_username
          - Properties changed
            - New property: created_by_username
            - Modified property: removed_by_username
              - Description changed from 'Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters' to ''
              - Nullable changed from false to true
            - Modified property: termination_metadata
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-resource-projects/{uuid}/add_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-resource-projects/{uuid}/delete_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-resource-projects/{uuid}/list_users/

- Modified query param: role
  - Description changed from 'Role UUID or name' to 'Role UUID or name. Repeat to filter by several roles.'
  - Schema changed
    - Type changed from 'string' to 'array'
    - Format changed from 'uuid' to ''
    - Items changed
      - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-resource-projects/{uuid}/recover/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: created_by_username
          - Properties changed
            - New property: created_by_username
            - Modified property: removed_by_username
              - Description changed from 'Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters' to ''
              - Nullable changed from false to true
            - Modified property: termination_metadata
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-resource-projects/{uuid}/update_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [has_api_keys resource_effective_end_date usage_limit_restriction]
- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-backend_id -customer_name -offering_name -plan_name backend_id customer_name offering_name plan_name]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: has_api_keys
              - New property: resource_effective_end_date
              - New property: usage_limit_restriction
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: consumer_message_updated_at
                      - New property: created_by_organization_address
                      - New property: created_by_organization_country
                      - New property: created_by_organization_vat_code
                      - New property: provider_message_updated_at
              - Modified property: limit_usage
                - Description changed from 'Dictionary mapping limit-based component types to their consumed usage. For monthly periods, maps from current_usages; for longer periods, aggregates historical usage.' to 'Dictionary mapping limit-based component types to their consumed usage. Sums the ComponentUsage rows of the component's current period (the monthly billing period unless the component defines a longer limit_period), i.e. the period's high-watermark rather than the instantaneous current_usages value.'
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: consumer_message_updated_at
                      - New property: created_by_organization_address
                      - New property: created_by_organization_country
                      - New property: created_by_organization_vat_code
                      - New property: provider_message_updated_at
              - Modified property: project_effective_end_date
                - Description changed from 'Effective project end date including grace period. After this date, resources will be terminated.' to 'Effective project end date including grace period. After this date, resources are terminated, except resources of offerings that disable the grace period — those are terminated on the raw project end date.'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-resources/

- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-backend_id -customer_name -offering_name -plan_name backend_id customer_name offering_name plan_name]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-resources/suggest_name/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-resources/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [has_api_keys resource_effective_end_date usage_limit_restriction]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_api_keys
            - New property: resource_effective_end_date
            - New property: usage_limit_restriction
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message_updated_at
                    - New property: created_by_organization_address
                    - New property: created_by_organization_country
                    - New property: created_by_organization_vat_code
                    - New property: provider_message_updated_at
            - Modified property: limit_usage
              - Description changed from 'Dictionary mapping limit-based component types to their consumed usage. For monthly periods, maps from current_usages; for longer periods, aggregates historical usage.' to 'Dictionary mapping limit-based component types to their consumed usage. Sums the ComponentUsage rows of the component's current period (the monthly billing period unless the component defines a longer limit_period), i.e. the period's high-watermark rather than the instantaneous current_usages value.'
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message_updated_at
                    - New property: created_by_organization_address
                    - New property: created_by_organization_country
                    - New property: created_by_organization_vat_code
                    - New property: provider_message_updated_at
            - Modified property: project_effective_end_date
              - Description changed from 'Effective project end date including grace period. After this date, resources will be terminated.' to 'Effective project end date including grace period. After this date, resources are terminated, except resources of offerings that disable the grace period — those are terminated on the raw project end date.'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-resources/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-resources/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-resources/{uuid}/add_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-resources/{uuid}/adjust_dates/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-resources/{uuid}/delete_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-resources/{uuid}/details/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-resources/{uuid}/estimate_renewal/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-resources/{uuid}/glauth_tree/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: groups
              - Items changed
                - Properties changed
                  - Modified property: kind
                    - New enum values: [personal]
                  - Modified property: scope
                    - Properties changed
                      - Modified property: type
                        - New enum values: [user]
            - Modified property: users
              - Items changed
                - Properties changed
                  - Modified property: memberships
                    - Items changed
                      - Properties changed
                        - Modified property: kind
                          - New enum values: [personal]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-resources/{uuid}/glauth_users_config/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-resources/{uuid}/history/

- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-backend_id -customer_name -offering_name -plan_name backend_id customer_name offering_name plan_name]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-resources/{uuid}/history/at/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-resources/{uuid}/list_users/

- Modified query param: role
  - Description changed from 'Role UUID or name' to 'Role UUID or name. Repeat to filter by several roles.'
  - Schema changed
    - Type changed from 'string' to 'array'
    - Format changed from 'uuid' to ''
    - Items changed
      - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-resources/{uuid}/move_resource/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_api_keys
            - New property: resource_effective_end_date
            - New property: usage_limit_restriction
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message_updated_at
                    - New property: created_by_organization_address
                    - New property: created_by_organization_country
                    - New property: created_by_organization_vat_code
                    - New property: provider_message_updated_at
            - Modified property: limit_usage
              - Description changed from 'Dictionary mapping limit-based component types to their consumed usage. For monthly periods, maps from current_usages; for longer periods, aggregates historical usage.' to 'Dictionary mapping limit-based component types to their consumed usage. Sums the ComponentUsage rows of the component's current period (the monthly billing period unless the component defines a longer limit_period), i.e. the period's high-watermark rather than the instantaneous current_usages value.'
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - New property: consumer_message_updated_at
                    - New property: created_by_organization_address
                    - New property: created_by_organization_country
                    - New property: created_by_organization_vat_code
                    - New property: provider_message_updated_at
            - Modified property: project_effective_end_date
              - Description changed from 'Effective project end date including grace period. After this date, resources will be terminated.' to 'Effective project end date including grace period. After this date, resources are terminated, except resources of offerings that disable the grace period — those are terminated on the raw project end date.'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-resources/{uuid}/offering/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [default_access_subnets open_for_proposals qos_profiles]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: default_access_subnets
            - New property: open_for_proposals
            - New property: qos_profiles
            - Modified property: partitions
              - Items changed
                - Properties changed
                  - New property: qos_options
            - Modified property: plans
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: discount_aggregation
                        - New property: discount_formula
                        - Deleted property: discount_rate
                        - Deleted property: discount_threshold
                        - Deleted property: discounted_price
                  - Modified property: description
                    - MaxLength changed from null to 4096
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: action_on_usage_limit
                    - New property: auto_approve_for_roles
                    - New property: billing_source
                    - New property: conceal_subnet_restricted_resources
                    - New property: disable_grace_period
                    - New property: emit_display_name
                    - New property: emit_waldur_username
                    - New property: enable_membership_sync_status
                    - New property: enable_posix_account
                    - New property: enable_resource_access_subnets
                    - New property: enable_resource_end_date_change_requests
                    - New property: enforce_qos
                    - New property: gid_source
                    - New property: login_shell
                    - New property: resource_projects_limit_policy
                    - New property: restricted_to_roles
                    - New property: show_ssh_key_loss_warning
                    - New property: uid_source
                    - Deleted property: initial_primarygroup_number
                    - Deleted property: initial_rolegroup_number
                    - Deleted property: initial_uidnumber
                    - Deleted property: initial_usergroup_number
            - Modified property: software_catalogs
              - Items changed
                - Properties changed
                  - Modified property: enabled_cpu_family
                    - Type changed from 'object' to 'array'
                    - AdditionalProperties changed from true to null
                    - Items changed
                      - Schema added
                  - Modified property: enabled_cpu_microarchitectures
                    - Type changed from 'object' to 'array'
                    - AdditionalProperties changed from true to null
                    - Items changed
                      - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-resources/{uuid}/offering_for_subresources/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-resources/{uuid}/plan_periods/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-resources/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-resources/{uuid}/reallocate_limits/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-resources/{uuid}/renew/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-resources/{uuid}/restore/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-resources/{uuid}/set_downscaled/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-resources/{uuid}/set_end_date/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-resources/{uuid}/set_end_date_by_staff/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-resources/{uuid}/set_paused/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-resources/{uuid}/set_restrict_member_access/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-resources/{uuid}/set_slug/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-resources/{uuid}/switch_plan/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-resources/{uuid}/team/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-resources/{uuid}/team_members/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [roles]
- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-backend_id -customer_name -offering_name -plan_name backend_id customer_name offering_name plan_name]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: roles
              - Modified property: resource_projects
                - Items changed
                  - Properties changed
                    - New property: sync_message
                    - New property: sync_reported_at
                    - New property: sync_state
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-resources/{uuid}/terminate/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-resources/{uuid}/unlink/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-resources/{uuid}/update_limits/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-resources/{uuid}/update_options/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-resources/{uuid}/update_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

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
                      - New property: action_on_usage_limit
                      - New property: auto_approve_for_roles
                      - New property: billing_source
                      - New property: conceal_subnet_restricted_resources
                      - New property: disable_grace_period
                      - New property: emit_display_name
                      - New property: emit_waldur_username
                      - New property: enable_membership_sync_status
                      - New property: enable_posix_account
                      - New property: enable_resource_access_subnets
                      - New property: enable_resource_end_date_change_requests
                      - New property: enforce_qos
                      - New property: gid_source
                      - New property: login_shell
                      - New property: resource_projects_limit_policy
                      - New property: restricted_to_roles
                      - New property: show_ssh_key_loss_warning
                      - New property: uid_source
                      - Deleted property: initial_primarygroup_number
                      - Deleted property: initial_rolegroup_number
                      - Deleted property: initial_uidnumber
                      - Deleted property: initial_usergroup_number
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-robot-accounts/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-robot-accounts/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-robot-accounts/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

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
                    - New property: action_on_usage_limit
                    - New property: auto_approve_for_roles
                    - New property: billing_source
                    - New property: conceal_subnet_restricted_resources
                    - New property: disable_grace_period
                    - New property: emit_display_name
                    - New property: emit_waldur_username
                    - New property: enable_membership_sync_status
                    - New property: enable_posix_account
                    - New property: enable_resource_access_subnets
                    - New property: enable_resource_end_date_change_requests
                    - New property: enforce_qos
                    - New property: gid_source
                    - New property: login_shell
                    - New property: resource_projects_limit_policy
                    - New property: restricted_to_roles
                    - New property: show_ssh_key_loss_warning
                    - New property: uid_source
                    - Deleted property: initial_primarygroup_number
                    - Deleted property: initial_rolegroup_number
                    - Deleted property: initial_uidnumber
                    - Deleted property: initial_usergroup_number
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-robot-accounts/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-robot-accounts/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

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
                    - New property: action_on_usage_limit
                    - New property: auto_approve_for_roles
                    - New property: billing_source
                    - New property: conceal_subnet_restricted_resources
                    - New property: disable_grace_period
                    - New property: emit_display_name
                    - New property: emit_waldur_username
                    - New property: enable_membership_sync_status
                    - New property: enable_posix_account
                    - New property: enable_resource_access_subnets
                    - New property: enable_resource_end_date_change_requests
                    - New property: enforce_qos
                    - New property: gid_source
                    - New property: login_shell
                    - New property: resource_projects_limit_policy
                    - New property: restricted_to_roles
                    - New property: show_ssh_key_loss_warning
                    - New property: uid_source
                    - Deleted property: initial_primarygroup_number
                    - Deleted property: initial_rolegroup_number
                    - Deleted property: initial_uidnumber
                    - Deleted property: initial_usergroup_number
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

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
                    - New property: action_on_usage_limit
                    - New property: auto_approve_for_roles
                    - New property: billing_source
                    - New property: conceal_subnet_restricted_resources
                    - New property: disable_grace_period
                    - New property: emit_display_name
                    - New property: emit_waldur_username
                    - New property: enable_membership_sync_status
                    - New property: enable_posix_account
                    - New property: enable_resource_access_subnets
                    - New property: enable_resource_end_date_change_requests
                    - New property: enforce_qos
                    - New property: gid_source
                    - New property: login_shell
                    - New property: resource_projects_limit_policy
                    - New property: restricted_to_roles
                    - New property: show_ssh_key_loss_warning
                    - New property: uid_source
                    - Deleted property: initial_primarygroup_number
                    - Deleted property: initial_rolegroup_number
                    - Deleted property: initial_uidnumber
                    - Deleted property: initial_usergroup_number
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

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
                    - New property: action_on_usage_limit
                    - New property: auto_approve_for_roles
                    - New property: billing_source
                    - New property: conceal_subnet_restricted_resources
                    - New property: disable_grace_period
                    - New property: emit_display_name
                    - New property: emit_waldur_username
                    - New property: enable_membership_sync_status
                    - New property: enable_posix_account
                    - New property: enable_resource_access_subnets
                    - New property: enable_resource_end_date_change_requests
                    - New property: enforce_qos
                    - New property: gid_source
                    - New property: login_shell
                    - New property: resource_projects_limit_policy
                    - New property: restricted_to_roles
                    - New property: show_ssh_key_loss_warning
                    - New property: uid_source
                    - Deleted property: initial_primarygroup_number
                    - Deleted property: initial_rolegroup_number
                    - Deleted property: initial_uidnumber
                    - Deleted property: initial_usergroup_number
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

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
                    - New property: action_on_usage_limit
                    - New property: auto_approve_for_roles
                    - New property: billing_source
                    - New property: conceal_subnet_restricted_resources
                    - New property: disable_grace_period
                    - New property: emit_display_name
                    - New property: emit_waldur_username
                    - New property: enable_membership_sync_status
                    - New property: enable_posix_account
                    - New property: enable_resource_access_subnets
                    - New property: enable_resource_end_date_change_requests
                    - New property: enforce_qos
                    - New property: gid_source
                    - New property: login_shell
                    - New property: resource_projects_limit_policy
                    - New property: restricted_to_roles
                    - New property: show_ssh_key_loss_warning
                    - New property: uid_source
                    - Deleted property: initial_primarygroup_number
                    - Deleted property: initial_rolegroup_number
                    - Deleted property: initial_uidnumber
                    - Deleted property: initial_usergroup_number
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

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
                    - New property: action_on_usage_limit
                    - New property: auto_approve_for_roles
                    - New property: billing_source
                    - New property: conceal_subnet_restricted_resources
                    - New property: disable_grace_period
                    - New property: emit_display_name
                    - New property: emit_waldur_username
                    - New property: enable_membership_sync_status
                    - New property: enable_posix_account
                    - New property: enable_resource_access_subnets
                    - New property: enable_resource_end_date_change_requests
                    - New property: enforce_qos
                    - New property: gid_source
                    - New property: login_shell
                    - New property: resource_projects_limit_policy
                    - New property: restricted_to_roles
                    - New property: show_ssh_key_loss_warning
                    - New property: uid_source
                    - Deleted property: initial_primarygroup_number
                    - Deleted property: initial_rolegroup_number
                    - Deleted property: initial_uidnumber
                    - Deleted property: initial_usergroup_number
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-runtime-states/

- New query param: offering_uuid
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-screenshots/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-screenshots/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-screenshots/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-screenshots/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-screenshots/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-screenshots/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-screenshots/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-script-async-dry-run/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-script-async-dry-run/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-script-async-dry-run/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-script-dry-run/{uuid}/async_run/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-script-dry-run/{uuid}/run/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-script-sync-resource/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-sections/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-sections/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-sections/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-sections/{key}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-sections/{key}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-sections/{key}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-sections/{key}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-service-providers/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: allowed_domains
                - Type changed from 'object' to 'array'
                - AdditionalProperties changed from true to null
                - Items changed
                  - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-service-providers/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-service-providers/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: allowed_domains
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: allowed_domains
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: allowed_domains
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: allowed_domains
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-service-providers/{service_provider_uuid}/compliance/checklists_summary/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-service-providers/{service_provider_uuid}/compliance/compliance_overview/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-service-providers/{service_provider_uuid}/compliance/offering_users/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-service-providers/{service_provider_uuid}/course_accounts/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-service-providers/{service_provider_uuid}/customer_projects/

- New query param: current_user_has_role
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-service-providers/{service_provider_uuid}/customers/

- New query param: current_user_has_role
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: payment_profiles
                - Items changed
                  - Properties changed
                    - Modified property: attributes
                      - Properties changed
                        - Modified property: contract_sum
                          - Type changed from 'integer' to 'string'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-service-providers/{service_provider_uuid}/keys/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-service-providers/{service_provider_uuid}/offerings/

- New query param: accessible
- New query param: consumer_customer_uuid
- New query param: open_for_proposals
- Modified query param: accessible_via_calls
  - Description changed from 'Accessible via calls' to 'Deprecated: offerings accepted on an active call, regardless of whether a proposal can actually be submitted for them. Use open_for_proposals instead.'
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [service_provider_can_create_offering_user]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: service_provider_can_create_offering_user
              - Modified property: plans
                - Items changed
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: discount_aggregation
                          - New property: discount_formula
                          - Deleted property: discount_rate
                          - Deleted property: discount_threshold
                          - Deleted property: discounted_price
                    - Modified property: description
                      - MaxLength changed from null to 4096
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-service-providers/{service_provider_uuid}/offerings/types/

- New query param: accessible
- New query param: consumer_customer_uuid
- New query param: open_for_proposals
- Modified query param: accessible_via_calls
  - Description changed from 'Accessible via calls' to 'Deprecated: offerings accepted on an active call, regardless of whether a proposal can actually be submitted for them. Use open_for_proposals instead.'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-service-providers/{service_provider_uuid}/project_permissions/

- New query param: customer_uuid
- New query param: is_active
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-service-providers/{service_provider_uuid}/project_service_accounts/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-service-providers/{service_provider_uuid}/projects/

- New query param: current_user_has_role
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from null to 4096
              - Modified property: project_metadata
                - Items changed
                  - Properties changed
                    - Modified property: answer
                      - Type changed from 'object' to ''
                      - AdditionalProperties changed from true to null
              - Modified property: staff_notes
                - MaxLength changed from null to 4096
              - Modified property: user_affiliations
                - Type changed from 'object' to 'array'
                - AdditionalProperties changed from true to null
                - Items changed
                  - Schema added
              - Modified property: user_email_patterns
                - Type changed from 'object' to 'array'
                - AdditionalProperties changed from true to null
                - Items changed
                  - Schema added
              - Modified property: user_identity_sources
                - Type changed from 'object' to 'array'
                - Description changed from 'List of allowed identity sources (identity providers).' to ''
                - AdditionalProperties changed from true to null
                - Items changed
                  - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-service-providers/{service_provider_uuid}/user_customers/

- New query param: current_user_has_role
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: payment_profiles
                - Items changed
                  - Properties changed
                    - Modified property: attributes
                      - Properties changed
                        - Modified property: contract_sum
                          - Type changed from 'integer' to 'string'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-service-providers/{service_provider_uuid}/users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [organization_address organization_vat_code]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: organization_address
              - New property: organization_vat_code
              - Modified property: active_isds
                - Type changed from 'object' to 'array'
                - AdditionalProperties changed from true to null
                - Items changed
                  - Schema added
              - Modified property: affiliations
                - Type changed from 'object' to 'array'
                - AdditionalProperties changed from true to null
                - Items changed
                  - Schema added
              - Modified property: eduperson_assurance
                - Type changed from 'object' to 'array'
                - AdditionalProperties changed from true to null
                - Items changed
                  - Schema added
              - Modified property: nationalities
                - Type changed from 'object' to 'array'
                - AdditionalProperties changed from true to null
                - Items changed
                  - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-service-providers/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-service-providers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: allowed_domains
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-service-providers/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: allowed_domains
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: allowed_domains
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: allowed_domains
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: allowed_domains
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-service-providers/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: allowed_domains
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: allowed_domains
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: allowed_domains
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: allowed_domains
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-service-providers/{uuid}/add_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-service-providers/{uuid}/api_secret_code/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-service-providers/{uuid}/api_secret_code/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-service-providers/{uuid}/delete_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-service-providers/{uuid}/generate_site_agent_config/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-service-providers/{uuid}/list_users/

- Modified query param: role
  - Description changed from 'Role UUID or name' to 'Role UUID or name. Repeat to filter by several roles.'
  - Schema changed
    - Type changed from 'string' to 'array'
    - Format changed from 'uuid' to ''
    - Items changed
      - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-service-providers/{uuid}/revenue/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-service-providers/{uuid}/robot_account_customers/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-service-providers/{uuid}/robot_account_projects/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-service-providers/{uuid}/set_offerings_username/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-service-providers/{uuid}/stat/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-service-providers/{uuid}/update_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-site-agent-connection-stats/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-site-agent-identities/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-site-agent-identities/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-site-agent-identities/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-site-agent-identities/cleanup_orphaned/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-site-agent-identities/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-site-agent-identities/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-site-agent-identities/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-site-agent-identities/{uuid}/register_event_subscription/

- Description changed from 'Register an event subscription for the specified agent identity and observable object type. Returns existing subscription if already exists.' to 'DEPRECATED: use register_queue instead, which creates a single unified consumer queue. This per-object-type subscription path is kept only for the deprecation window; removal is tracked in WAL-10111. Register an event subscription for the specified agent identity and observable object type. Returns existing subscription if already exists.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: observable_object_type
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/ObservableObjectTypeEnum
                - New enum values: [resource_api_key_rotation resource_end_date_change_request user_profile user_ssh_key user_lifecycle]
- Deprecated changed from false to true
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-site-agent-identities/{uuid}/register_service/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-site-agent-logs/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-site-agent-logs/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-site-agent-logs/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-site-agent-processors/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-site-agent-processors/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-site-agent-processors/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-site-agent-processors/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-site-agent-services/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-site-agent-services/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-site-agent-services/cleanup_stale/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-site-agent-services/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-site-agent-services/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-site-agent-services/{uuid}/register_processor/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-site-agent-services/{uuid}/set_statistics/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-site-agent-stats/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-site-agent-task-stats/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-slurm-periodic-usage-policies/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-slurm-periodic-usage-policies/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-slurm-periodic-usage-policies/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-slurm-periodic-usage-policies/actions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-slurm-periodic-usage-policies/actions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-slurm-periodic-usage-policies/preview_impact/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-slurm-periodic-usage-policies/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-slurm-periodic-usage-policies/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-slurm-periodic-usage-policies/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-slurm-periodic-usage-policies/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-slurm-periodic-usage-policies/{uuid}/command-history/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-slurm-periodic-usage-policies/{uuid}/dry-run/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-slurm-periodic-usage-policies/{uuid}/evaluate/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-slurm-periodic-usage-policies/{uuid}/evaluation-logs/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-slurm-periodic-usage-policies/{uuid}/force-period-reset/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-slurm-periodic-usage-policies/{uuid}/report-command-result/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-software-catalogs/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-software-catalogs/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-software-catalogs/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-software-catalogs/discover/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-software-catalogs/discover/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-software-catalogs/import_catalog/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-software-catalogs/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-software-catalogs/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-software-catalogs/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-software-catalogs/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-software-catalogs/{uuid}/update_catalog/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-software-packages/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: versions
                - Items changed
                  - Properties changed
                    - Modified property: targets
                      - Items changed
                        - Properties changed
                          - Modified property: gpu_architectures
                            - Type changed from 'object' to 'array'
                            - AdditionalProperties changed from true to null
                            - Items changed
                              - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-software-packages/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-software-packages/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: versions
              - Items changed
                - Properties changed
                  - Modified property: targets
                    - Items changed
                      - Properties changed
                        - Modified property: gpu_architectures
                          - Type changed from 'object' to 'array'
                          - AdditionalProperties changed from true to null
                          - Items changed
                            - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-software-packages/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-software-packages/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: versions
              - Items changed
                - Properties changed
                  - Modified property: targets
                    - Items changed
                      - Properties changed
                        - Modified property: gpu_architectures
                          - Type changed from 'object' to 'array'
                          - AdditionalProperties changed from true to null
                          - Items changed
                            - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-software-packages/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: versions
              - Items changed
                - Properties changed
                  - Modified property: targets
                    - Items changed
                      - Properties changed
                        - Modified property: gpu_architectures
                          - Type changed from 'object' to 'array'
                          - AdditionalProperties changed from true to null
                          - Items changed
                            - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-software-packages/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: versions
              - Items changed
                - Properties changed
                  - Modified property: targets
                    - Items changed
                      - Properties changed
                        - Modified property: gpu_architectures
                          - Type changed from 'object' to 'array'
                          - AdditionalProperties changed from true to null
                          - Items changed
                            - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-software-targets/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: gpu_architectures
                - Type changed from 'object' to 'array'
                - AdditionalProperties changed from true to null
                - Items changed
                  - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-software-targets/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-software-targets/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: gpu_architectures
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-software-targets/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-software-targets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: gpu_architectures
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-software-targets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: gpu_architectures
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-software-targets/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: gpu_architectures
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-software-versions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-software-versions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-software-versions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-software-versions/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-software-versions/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-software-versions/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-software-versions/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/aggregated_usage_trends/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/aggregated_usage_trends/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/component_usages/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/component_usages/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/component_usages_per_month/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/component_usages_per_month/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/component_usages_per_project/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/component_usages_per_project/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/count_active_resources_grouped_by_offering/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/count_active_resources_grouped_by_offering/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/count_active_resources_grouped_by_offering_country/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/count_active_resources_grouped_by_offering_country/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/count_active_resources_grouped_by_organization_group/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/count_active_resources_grouped_by_organization_group/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/count_projects_grouped_by_provider_and_industry_flag/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/count_projects_grouped_by_provider_and_industry_flag/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/count_projects_grouped_by_provider_and_oecd/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/count_projects_grouped_by_provider_and_oecd/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/count_projects_of_service_providers/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/count_projects_of_service_providers/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/count_projects_of_service_providers_grouped_by_oecd/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/count_projects_of_service_providers_grouped_by_oecd/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/count_unique_users_connected_with_active_resources_of_service_provider/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/count_unique_users_connected_with_active_resources_of_service_provider/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/count_users_of_service_providers/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/count_users_of_service_providers/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/customer_member_count/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/customer_member_count/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/customer_member_summary/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/customer_member_summary/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/offering_costs_summary/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/offering_costs_summary/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/offerings_counter_stats/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/offerings_counter_stats/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/openstack_instances/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/openstack_instances/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/openstack_instances_aggregate/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/openstack_instances_aggregate/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/order_stats/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/order_stats/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/organization_project_count/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/organization_project_count/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/organization_resource_count/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/organization_resource_count/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/project_classification_summary/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/project_classification_summary/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/project_creation_trend/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/project_creation_trend/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/projects_limits_grouped_by_industry_flag/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/projects_limits_grouped_by_industry_flag/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/projects_limits_grouped_by_oecd/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/projects_limits_grouped_by_oecd/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/projects_usages_grouped_by_industry_flag/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/projects_usages_grouped_by_industry_flag/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/projects_usages_grouped_by_oecd/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/projects_usages_grouped_by_oecd/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/provider_customers/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/provider_customers/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/provider_offerings/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/provider_offerings/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/provider_resources/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/provider_resources/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/resource_creation_trend/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/resource_creation_trend/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/resource_provisioning_stats/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/resource_provisioning_stats/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/resource_usage_by_creator_affiliation/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/resource_usage_by_creator_affiliation/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/resource_usage_by_customer/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/resource_usage_by_customer/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/resource_usage_by_organization_type/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/resource_usage_by_organization_type/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/resources_geography_summary/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/resources_geography_summary/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/resources_limits/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/resources_limits/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/resources_missing_usage/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/resources_missing_usage/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/top_service_providers_by_resources/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/top_service_providers_by_resources/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/total_cost_of_active_resources_per_offering/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/total_cost_of_active_resources_per_offering/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/user_affiliation_count/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/user_affiliation_count/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/user_affiliation_details/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/user_affiliation_details/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/user_auth_method_count/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/user_auth_method_count/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/user_identity_source_count/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/user_identity_source_count/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/user_job_title_count/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/user_job_title_count/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/user_nationality/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/user_nationality/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/user_organization_count/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/user_organization_count/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/user_organization_type_count/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/user_organization_type_count/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-stats/user_residence_country/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-stats/user_residence_country/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-tags/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-tags/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-tags/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-tags/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-tags/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-tags/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-tags/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-user-offering-consents/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/marketplace-user-offering-consents/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-user-offering-consents/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/marketplace-user-offering-consents/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/marketplace-user-offering-consents/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/marketplace-user-offering-consents/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/marketplace-user-offering-consents/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/marketplace-user-offering-consents/{uuid}/revoke/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/matrix/credentials/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/matrix/exports/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/matrix/exports/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/matrix/exports/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/matrix/exports/{uuid}/download/{kind}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/matrix/rooms/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/matrix/rooms/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/matrix/rooms/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/matrix/rooms/eligible_projects/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/matrix/rooms/eligible_projects/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/matrix/rooms/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/matrix/rooms/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/matrix/rooms/{uuid}/disable/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/matrix/rooms/{uuid}/export_history/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/matrix/rooms/{uuid}/join/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/matrix/rooms/{uuid}/leave/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/matrix/rooms/{uuid}/members/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/matrix/rooms/{uuid}/reactivate/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/matrix/rooms/{uuid}/retry/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/matrix/rooms/{uuid}/sync_members/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/media/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

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
                  - New enum values: [offering_access_subnet_creation_succeeded offering_access_subnet_deletion_succeeded offering_access_subnet_update_succeeded create_of_affiliate_by_staff marketplace_resource_api_key_rotated marketplace_resource_api_key_revealed marketplace_resource_project_created marketplace_resource_project_recovered marketplace_resource_project_removed marketplace_resource_end_date_change_request_created marketplace_resource_end_date_change_request_approved marketplace_resource_end_date_change_request_rejected marketplace_resource_end_date_change_request_canceled maintenance_announcement_cancelled maintenance_announcement_completed maintenance_announcement_created maintenance_announcement_deleted maintenance_announcement_scheduled maintenance_announcement_started maintenance_announcement_unscheduled maintenance_announcement_updated increase_of_customer_credit_due_to_affiliate_fee update_of_affiliate_by_staff user_blocked pat_access_denied_from_ip pat_network_acl_updated pat_authentication_rejected]

GET /api/metadata/permissions/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: permission_descriptions
              - Items changed
                - Properties changed
                  - Modified property: options
                    - Items changed
                      - Properties changed
                        - Modified property: value
                          - Property 'AllOf' changed
                            - Modified schema: #/components/schemas/ValueEnum
                              - New enum values: [POSIX_ID_POOL.MANAGE RESOURCE.MANAGE_API_KEY SERVICE_PROVIDER.MANAGE_MAINTENANCE_ANNOUNCEMENT OFFERING_ACCESS_SUBNET.CREATE OFFERING_ACCESS_SUBNET.UPDATE OFFERING_ACCESS_SUBNET.DELETE]
            - Modified property: permission_map
              - AdditionalProperties changed
                - New enum values: [POSIX_ID_POOL.MANAGE RESOURCE.MANAGE_API_KEY SERVICE_PROVIDER.MANAGE_MAINTENANCE_ANNOUNCEMENT OFFERING_ACCESS_SUBNET.CREATE OFFERING_ACCESS_SUBNET.UPDATE OFFERING_ACCESS_SUBNET.DELETE]
            - Modified property: permissions
              - AdditionalProperties changed
                - New enum values: [POSIX_ID_POOL.MANAGE RESOURCE.MANAGE_API_KEY SERVICE_PROVIDER.MANAGE_MAINTENANCE_ANNOUNCEMENT OFFERING_ACCESS_SUBNET.CREATE OFFERING_ACCESS_SUBNET.UPDATE OFFERING_ACCESS_SUBNET.DELETE]
            - Modified property: roles
              - AdditionalProperties changed
                - New enum values: [CALL.PANEL_MEMBER]

GET /api/my-assignment-batches/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/my-assignment-batches/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/my-assignment-batches/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/notification-messages-templates/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/notification-messages-templates/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/notification-messages-templates/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/notification-messages-templates/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/notification-messages-templates/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/notification-messages-templates/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/notification-messages-templates/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/notification-messages-templates/{uuid}/override/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/notification-messages/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/notification-messages/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/notification-messages/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/notification-messages/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/notification-messages/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/notification-messages/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/notification-messages/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/notification-messages/{uuid}/disable/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/notification-messages/{uuid}/enable/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/onboarding-justifications/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/onboarding-justifications/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/onboarding-justifications/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/onboarding-justifications/create_justification/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/onboarding-justifications/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/onboarding-justifications/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/onboarding-justifications/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/onboarding-justifications/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/onboarding-justifications/{uuid}/approve/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/onboarding-justifications/{uuid}/attach_document/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/onboarding-justifications/{uuid}/reject/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/onboarding-question-metadata/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/onboarding-question-metadata/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/onboarding-question-metadata/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/onboarding-question-metadata/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/onboarding-question-metadata/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/onboarding-question-metadata/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/onboarding-question-metadata/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/onboarding-verifications/

- Modified query param: validation_method
  - Schema changed
    - Items changed
      - New enum values: [Dun & Bradstreet Denmark Dun & Bradstreet Finland Dun & Bradstreet Norway Dun & Bradstreet Sweden]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: validation_method
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/ValidationMethodEnum
                    - New enum values: [dnb_se dnb_no dnb_dk dnb_fi]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/onboarding-verifications/

- Modified query param: validation_method
  - Schema changed
    - Items changed
      - New enum values: [Dun & Bradstreet Denmark Dun & Bradstreet Finland Dun & Bradstreet Norway Dun & Bradstreet Sweden]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/onboarding-verifications/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: validation_method
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ValidationMethodEnum
                  - New enum values: [dnb_se dnb_no dnb_dk dnb_fi]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/onboarding-verifications/available_checklists/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/onboarding-verifications/available_checklists/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/onboarding-verifications/checklist-template/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/onboarding-verifications/checklist-template/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/onboarding-verifications/start_verification/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: validation_method
            - Property 'OneOf' changed
              - Modified schema: #/components/schemas/ValidationMethodEnum
                - New enum values: [dnb_se dnb_no dnb_dk dnb_fi]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: validation_method
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ValidationMethodEnum
                  - New enum values: [dnb_se dnb_no dnb_dk dnb_fi]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/onboarding-verifications/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/onboarding-verifications/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: validation_method
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ValidationMethodEnum
                  - New enum values: [dnb_se dnb_no dnb_dk dnb_fi]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/onboarding-verifications/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: validation_method
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ValidationMethodEnum
                  - New enum values: [dnb_se dnb_no dnb_dk dnb_fi]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/onboarding-verifications/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: validation_method
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ValidationMethodEnum
                  - New enum values: [dnb_se dnb_no dnb_dk dnb_fi]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/onboarding-verifications/{uuid}/checklist/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/onboarding-verifications/{uuid}/completion_status/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/onboarding-verifications/{uuid}/create_customer/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_active_helpdesk
            - New property: has_affiliate_links
            - Modified property: customer_credit
              - Type changed from 'number' to 'string'
              - Format changed from 'double' to ''
            - Modified property: customer_unallocated_credit
              - Type changed from 'number' to 'string'
              - Format changed from 'double' to ''
            - Modified property: payment_profiles
              - Items changed
                - Properties changed
                  - Modified property: attributes
                    - Properties changed
                      - Modified property: contract_sum
                        - Type changed from 'integer' to 'string'
            - Modified property: user_affiliations
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_email_patterns
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_identity_sources
              - Type changed from 'object' to 'array'
              - Description changed from 'List of allowed identity sources (identity providers).' to ''
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/onboarding-verifications/{uuid}/run_validation/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: validation_method
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ValidationMethodEnum
                  - New enum values: [dnb_se dnb_no dnb_dk dnb_fi]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/onboarding-verifications/{uuid}/submit_answers/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: validation_method
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ValidationMethodEnum
                  - New enum values: [dnb_se dnb_no dnb_dk dnb_fi]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/onboarding/person-identifier-fields/

- Modified query param: validation_method
  - Schema changed
    - New enum values: [dnb_se dnb_no dnb_dk dnb_fi]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/onboarding/supported-countries/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openportal-accounting-summary/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openportal-accounting-summary/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openportal-accounting-summary/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openportal-allocation-user-usage/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openportal-allocation-user-usage/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openportal-allocation-user-usage/{id}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openportal-allocations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openportal-allocations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openportal-allocations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/openportal-allocations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openportal-allocations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/openportal-allocations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/openportal-allocations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openportal-allocations/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openportal-allocations/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openportal-allocations/{uuid}/set_limits/

- Description changed from '' to 'Set limits for allocation'
- Responses changed
  - Modified response: 202
    - Description changed from '' to 'No response body'
    - Content changed
      - Deleted media type: application/json
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openportal-allocations/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openportal-allocations/{uuid}/unlink/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openportal-associations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openportal-associations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openportal-associations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openportal-managed-projects/

- New query param: hide_embargoed
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: details
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/AwardDetails
                  - Schemas deleted: #/components/schemas/ManagedProjectDetails
                - Description changed from '' to 'Details of the project as provided by the remote OpenPortal.'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openportal-managed-projects/

- New query param: hide_embargoed
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openportal-managed-projects/{identifier}/{destination}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: details
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/AwardDetails
                - Schemas deleted: #/components/schemas/ManagedProjectDetails
              - Description changed from '' to 'Details of the project as provided by the remote OpenPortal.'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openportal-managed-projects/{identifier}/{destination}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openportal-managed-projects/{identifier}/{destination}/approve/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openportal-managed-projects/{identifier}/{destination}/attach/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/openportal-managed-projects/{identifier}/{destination}/delete/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openportal-managed-projects/{identifier}/{destination}/detach/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openportal-managed-projects/{identifier}/{destination}/reject/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openportal-project-storage-reports/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openportal-project-storage-reports/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openportal-project-storage-reports/{id}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openportal-project-template/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openportal-project-template/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openportal-project-template/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/openportal-project-template/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openportal-project-template/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/openportal-project-template/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/openportal-project-template/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/openportal-project-template/{uuid}/delete/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openportal-project-usage-reports/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openportal-project-usage-reports/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openportal-project-usage-reports/{id}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openportal-projectinfo/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openportal-projectinfo/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openportal-projectinfo/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/openportal-projectinfo/{project}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openportal-projectinfo/{project}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/openportal-projectinfo/{project}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/openportal-projectinfo/{project}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/openportal-projectinfo/{project}/set_allowed_destinations/

- Description changed from '' to 'Set allowed destinations for project'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/openportal-projectinfo/{project}/set_shortname/

- Description changed from '' to 'Set shortname for project'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openportal-remote-allocations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openportal-remote-allocations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openportal-remote-allocations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/openportal-remote-allocations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openportal-remote-allocations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/openportal-remote-allocations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/openportal-remote-allocations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openportal-remote-allocations/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openportal-remote-allocations/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openportal-remote-allocations/{uuid}/set_limits/

- Description changed from '' to 'Set limits for allocation'
- Responses changed
  - Modified response: 202
    - Description changed from '' to 'No response body'
    - Content changed
      - Deleted media type: application/json
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openportal-remote-allocations/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openportal-remote-allocations/{uuid}/unlink/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openportal-remote-associations/

- Modified query param: allocation_uuid
  - Extensions changed
    - Modified extension: x-waldur-operation-id
      - Modified value from 'openportal_allocations_retrieve' to 'openportal_remote_allocations_retrieve'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openportal-remote-associations/

- Modified query param: allocation_uuid
  - Extensions changed
    - Modified extension: x-waldur-operation-id
      - Modified value from 'openportal_allocations_retrieve' to 'openportal_remote_allocations_retrieve'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openportal-remote-associations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openportal-unmanaged-projects/

- New query param: current_user_has_role
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from null to 4096
              - Modified property: project_metadata
                - Items changed
                  - Properties changed
                    - Modified property: answer
                      - Type changed from 'object' to ''
                      - AdditionalProperties changed from true to null
              - Modified property: staff_notes
                - MaxLength changed from null to 4096
              - Modified property: user_affiliations
                - Type changed from 'object' to 'array'
                - AdditionalProperties changed from true to null
                - Items changed
                  - Schema added
              - Modified property: user_email_patterns
                - Type changed from 'object' to 'array'
                - AdditionalProperties changed from true to null
                - Items changed
                  - Schema added
              - Modified property: user_identity_sources
                - Type changed from 'object' to 'array'
                - Description changed from 'List of allowed identity sources (identity providers).' to ''
                - AdditionalProperties changed from true to null
                - Items changed
                  - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openportal-unmanaged-projects/

- New query param: current_user_has_role
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openportal-unmanaged-projects/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from null to 4096
          - Modified property: staff_notes
            - MaxLength changed from null to 4096
          - Modified property: user_affiliations
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_email_patterns
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_identity_sources
            - Type changed from 'object' to 'array'
            - Description changed from 'List of allowed identity sources (identity providers).' to ''
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from null to 4096
          - Modified property: staff_notes
            - MaxLength changed from null to 4096
          - Modified property: user_affiliations
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_email_patterns
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_identity_sources
            - Type changed from 'object' to 'array'
            - Description changed from 'List of allowed identity sources (identity providers).' to ''
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from null to 4096
          - Modified property: staff_notes
            - MaxLength changed from null to 4096
          - Modified property: user_affiliations
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_email_patterns
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_identity_sources
            - Type changed from 'object' to 'array'
            - Description changed from 'List of allowed identity sources (identity providers).' to ''
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from null to 4096
            - Modified property: project_metadata
              - Items changed
                - Properties changed
                  - Modified property: answer
                    - Type changed from 'object' to ''
                    - AdditionalProperties changed from true to null
            - Modified property: staff_notes
              - MaxLength changed from null to 4096
            - Modified property: user_affiliations
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_email_patterns
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_identity_sources
              - Type changed from 'object' to 'array'
              - Description changed from 'List of allowed identity sources (identity providers).' to ''
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openportal-unmanaged-projects/checklist-template/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openportal-unmanaged-projects/checklist-template/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/openportal-unmanaged-projects/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openportal-unmanaged-projects/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from null to 4096
            - Modified property: project_metadata
              - Items changed
                - Properties changed
                  - Modified property: answer
                    - Type changed from 'object' to ''
                    - AdditionalProperties changed from true to null
            - Modified property: staff_notes
              - MaxLength changed from null to 4096
            - Modified property: user_affiliations
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_email_patterns
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_identity_sources
              - Type changed from 'object' to 'array'
              - Description changed from 'List of allowed identity sources (identity providers).' to ''
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/openportal-unmanaged-projects/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from null to 4096
          - Modified property: staff_notes
            - MaxLength changed from null to 4096
          - Modified property: user_affiliations
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_email_patterns
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_identity_sources
            - Type changed from 'object' to 'array'
            - Description changed from 'List of allowed identity sources (identity providers).' to ''
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from null to 4096
          - Modified property: staff_notes
            - MaxLength changed from null to 4096
          - Modified property: user_affiliations
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_email_patterns
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_identity_sources
            - Type changed from 'object' to 'array'
            - Description changed from 'List of allowed identity sources (identity providers).' to ''
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from null to 4096
          - Modified property: staff_notes
            - MaxLength changed from null to 4096
          - Modified property: user_affiliations
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_email_patterns
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_identity_sources
            - Type changed from 'object' to 'array'
            - Description changed from 'List of allowed identity sources (identity providers).' to ''
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from null to 4096
            - Modified property: project_metadata
              - Items changed
                - Properties changed
                  - Modified property: answer
                    - Type changed from 'object' to ''
                    - AdditionalProperties changed from true to null
            - Modified property: staff_notes
              - MaxLength changed from null to 4096
            - Modified property: user_affiliations
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_email_patterns
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_identity_sources
              - Type changed from 'object' to 'array'
              - Description changed from 'List of allowed identity sources (identity providers).' to ''
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/openportal-unmanaged-projects/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from null to 4096
          - Modified property: staff_notes
            - MaxLength changed from null to 4096
          - Modified property: user_affiliations
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_email_patterns
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_identity_sources
            - Type changed from 'object' to 'array'
            - Description changed from 'List of allowed identity sources (identity providers).' to ''
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from null to 4096
          - Modified property: staff_notes
            - MaxLength changed from null to 4096
          - Modified property: user_affiliations
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_email_patterns
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_identity_sources
            - Type changed from 'object' to 'array'
            - Description changed from 'List of allowed identity sources (identity providers).' to ''
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from null to 4096
          - Modified property: staff_notes
            - MaxLength changed from null to 4096
          - Modified property: user_affiliations
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_email_patterns
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_identity_sources
            - Type changed from 'object' to 'array'
            - Description changed from 'List of allowed identity sources (identity providers).' to ''
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from null to 4096
            - Modified property: project_metadata
              - Items changed
                - Properties changed
                  - Modified property: answer
                    - Type changed from 'object' to ''
                    - AdditionalProperties changed from true to null
            - Modified property: staff_notes
              - MaxLength changed from null to 4096
            - Modified property: user_affiliations
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_email_patterns
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_identity_sources
              - Type changed from 'object' to 'array'
              - Description changed from 'List of allowed identity sources (identity providers).' to ''
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openportal-unmanaged-projects/{uuid}/add_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openportal-unmanaged-projects/{uuid}/checklist/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openportal-unmanaged-projects/{uuid}/completion_status/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openportal-unmanaged-projects/{uuid}/delete_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openportal-unmanaged-projects/{uuid}/list_users/

- Modified query param: role
  - Description changed from 'Role UUID or name' to 'Role UUID or name. Repeat to filter by several roles.'
  - Schema changed
    - Type changed from 'string' to 'array'
    - Format changed from 'uuid' to ''
    - Items changed
      - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openportal-unmanaged-projects/{uuid}/move_project/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from null to 4096
            - Modified property: project_metadata
              - Items changed
                - Properties changed
                  - Modified property: answer
                    - Type changed from 'object' to ''
                    - AdditionalProperties changed from true to null
            - Modified property: staff_notes
              - MaxLength changed from null to 4096
            - Modified property: user_affiliations
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_email_patterns
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_identity_sources
              - Type changed from 'object' to 'array'
              - Description changed from 'List of allowed identity sources (identity providers).' to ''
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openportal-unmanaged-projects/{uuid}/recover/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from null to 4096
            - Modified property: project_metadata
              - Items changed
                - Properties changed
                  - Modified property: answer
                    - Type changed from 'object' to ''
                    - AdditionalProperties changed from true to null
            - Modified property: staff_notes
              - MaxLength changed from null to 4096
            - Modified property: user_affiliations
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_email_patterns
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_identity_sources
              - Type changed from 'object' to 'array'
              - Description changed from 'List of allowed identity sources (identity providers).' to ''
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openportal-unmanaged-projects/{uuid}/stats/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openportal-unmanaged-projects/{uuid}/submit_answers/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openportal-unmanaged-projects/{uuid}/update_affiliation/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openportal-unmanaged-projects/{uuid}/update_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openportal-userinfo/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openportal-userinfo/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openportal-userinfo/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openportal-userinfo/me/

- Description changed from '' to 'Retrieve UserInfo for current user'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openportal-userinfo/me/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/openportal-userinfo/{user}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openportal-userinfo/{user}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/openportal-userinfo/{user}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/openportal-userinfo/{user}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/openportal-userinfo/{user}/set_shortname/

- Description changed from '' to 'Set shortname for user'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openportal/access_for_email/

- Security changed
  - Deleted security requirements: waldurOIDCAuth
  - Deleted security requirements: waldurPATAuth

GET /api/openportal/offering_mapping/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openportal/project_mapping/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openportal/user_mapping/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

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
                    - Modified property: allowed_address_pairs
                      - Items changed
                        - Properties changed
                          - New property: ip_address
              - Modified property: restorations
                - Items changed
                  - Properties changed
                    - Modified property: ports
                      - Items changed
                        - Properties changed
                          - Modified property: allowed_address_pairs
                            - Items changed
                              - Properties changed
                                - New property: ip_address
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openstack-backups/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/openstack-backups/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

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
                  - Modified property: allowed_address_pairs
                    - Items changed
                      - Properties changed
                        - New property: ip_address
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: allowed_address_pairs
                          - Items changed
                            - Properties changed
                              - New property: ip_address
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

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
                  - Modified property: allowed_address_pairs
                    - Items changed
                      - Properties changed
                        - New property: ip_address
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: allowed_address_pairs
                          - Items changed
                            - Properties changed
                              - New property: ip_address
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

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
                  - Modified property: allowed_address_pairs
                    - Items changed
                      - Properties changed
                        - New property: ip_address
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: allowed_address_pairs
                          - Items changed
                            - Properties changed
                              - New property: ip_address
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-backups/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-backups/{uuid}/restore/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: name
              - MaxLength changed from 150 to 255
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: allowed_address_pairs
                    - Items changed
                      - Properties changed
                        - New property: ip_address
            - Modified property: user_data
              - Description changed from 'Additional data that will be added to instance on provisioning' to 'Cloud-init user data passed to the instance on provisioning. SECURITY: this value is stored and transmitted in plain text — it is kept unencrypted in Waldur's database, forwarded to OpenStack where any process on the instance can read it via the metadata service, and it may appear in logs. Do NOT put unencrypted secrets (passwords, private keys, API tokens) here; reference a secrets manager or inject them through an encrypted channel instead.'
            - Modified property: volumes
              - Items changed
                - Properties changed
                  - Modified property: image_name
                    - MaxLength changed from 150 to 255
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-backups/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-backups/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-backups/{uuid}/unlink/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-external-networks/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openstack-external-networks/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-external-networks/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-flavors/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openstack-flavors/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-flavors/usage_stats/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openstack-flavors/usage_stats/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-flavors/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-floating-ips/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openstack-floating-ips/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/openstack-floating-ips/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-floating-ips/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-floating-ips/{uuid}/attach_to_port/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-floating-ips/{uuid}/detach_from_port/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-floating-ips/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-floating-ips/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-floating-ips/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-floating-ips/{uuid}/unlink/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-floating-ips/{uuid}/update_description/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-health-monitors/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openstack-health-monitors/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-health-monitors/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/openstack-health-monitors/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-health-monitors/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/openstack-health-monitors/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/openstack-health-monitors/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-health-monitors/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-hypervisor-inventories/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openstack-hypervisor-inventories/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-hypervisor-inventories/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-hypervisors/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openstack-hypervisors/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-hypervisors/allocation_candidates/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openstack-hypervisors/allocation_candidates/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-hypervisors/summary/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openstack-hypervisors/summary/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-hypervisors/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-images/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openstack-images/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-images/usage_stats/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openstack-images/usage_stats/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-images/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-instance-availability-zones/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openstack-instance-availability-zones/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-instance-availability-zones/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-instances/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: name
                - MaxLength changed from 150 to 255
              - Modified property: ports
                - Items changed
                  - Properties changed
                    - Modified property: allowed_address_pairs
                      - Items changed
                        - Properties changed
                          - New property: ip_address
              - Modified property: user_data
                - Description changed from 'Additional data that will be added to instance on provisioning' to 'Cloud-init user data passed to the instance on provisioning. SECURITY: this value is stored and transmitted in plain text — it is kept unencrypted in Waldur's database, forwarded to OpenStack where any process on the instance can read it via the metadata service, and it may appear in logs. Do NOT put unencrypted secrets (passwords, private keys, API tokens) here; reference a secrets manager or inject them through an encrypted channel instead.'
              - Modified property: volumes
                - Items changed
                  - Properties changed
                    - Modified property: image_name
                      - MaxLength changed from 150 to 255
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openstack-instances/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-instances/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: name
              - MaxLength changed from 150 to 255
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: allowed_address_pairs
                    - Items changed
                      - Properties changed
                        - New property: ip_address
            - Modified property: user_data
              - Description changed from 'Additional data that will be added to instance on provisioning' to 'Cloud-init user data passed to the instance on provisioning. SECURITY: this value is stored and transmitted in plain text — it is kept unencrypted in Waldur's database, forwarded to OpenStack where any process on the instance can read it via the metadata service, and it may appear in logs. Do NOT put unencrypted secrets (passwords, private keys, API tokens) here; reference a secrets manager or inject them through an encrypted channel instead.'
            - Modified property: volumes
              - Items changed
                - Properties changed
                  - Modified property: image_name
                    - MaxLength changed from 150 to 255
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/openstack-instances/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: name
            - MaxLength changed from 150 to 255
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: name
              - MaxLength changed from 150 to 255
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: allowed_address_pairs
                    - Items changed
                      - Properties changed
                        - New property: ip_address
            - Modified property: user_data
              - Description changed from 'Additional data that will be added to instance on provisioning' to 'Cloud-init user data passed to the instance on provisioning. SECURITY: this value is stored and transmitted in plain text — it is kept unencrypted in Waldur's database, forwarded to OpenStack where any process on the instance can read it via the metadata service, and it may appear in logs. Do NOT put unencrypted secrets (passwords, private keys, API tokens) here; reference a secrets manager or inject them through an encrypted channel instead.'
            - Modified property: volumes
              - Items changed
                - Properties changed
                  - Modified property: image_name
                    - MaxLength changed from 150 to 255
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/openstack-instances/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: name
            - MaxLength changed from 150 to 255
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: name
              - MaxLength changed from 150 to 255
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: allowed_address_pairs
                    - Items changed
                      - Properties changed
                        - New property: ip_address
            - Modified property: user_data
              - Description changed from 'Additional data that will be added to instance on provisioning' to 'Cloud-init user data passed to the instance on provisioning. SECURITY: this value is stored and transmitted in plain text — it is kept unencrypted in Waldur's database, forwarded to OpenStack where any process on the instance can read it via the metadata service, and it may appear in logs. Do NOT put unencrypted secrets (passwords, private keys, API tokens) here; reference a secrets manager or inject them through an encrypted channel instead.'
            - Modified property: volumes
              - Items changed
                - Properties changed
                  - Modified property: image_name
                    - MaxLength changed from 150 to 255
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

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
                  - Modified property: allowed_address_pairs
                    - Items changed
                      - Properties changed
                        - New property: ip_address
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: ports
                    - Items changed
                      - Properties changed
                        - Modified property: allowed_address_pairs
                          - Items changed
                            - Properties changed
                              - New property: ip_address
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-instances/{uuid}/change_flavor/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-instances/{uuid}/console/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-instances/{uuid}/console_log/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-instances/{uuid}/diagnose_connectivity/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-instances/{uuid}/floating_ips/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-instances/{uuid}/placement_allocations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-instances/{uuid}/ports/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: allowed_address_pairs
                - Items changed
                  - Properties changed
                    - New property: ip_address
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-instances/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-instances/{uuid}/rescue/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-instances/{uuid}/restart/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-instances/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-instances/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-instances/{uuid}/start/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-instances/{uuid}/stop/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-instances/{uuid}/unlink/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-instances/{uuid}/unrescue/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-instances/{uuid}/update_allowed_address_pairs/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: allowed_address_pairs
            - Items changed
              - Properties changed
                - Modified property: ip_address
                  - WriteOnly changed from true to false
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-instances/{uuid}/update_floating_ips/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-instances/{uuid}/update_ports/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-instances/{uuid}/update_security_groups/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-listeners/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openstack-listeners/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-listeners/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/openstack-listeners/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-listeners/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/openstack-listeners/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/openstack-listeners/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-listeners/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-loadbalancers/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openstack-loadbalancers/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-loadbalancers/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/openstack-loadbalancers/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-loadbalancers/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/openstack-loadbalancers/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/openstack-loadbalancers/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-loadbalancers/{uuid}/attach_floating_ip/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-loadbalancers/{uuid}/detach_floating_ip/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-loadbalancers/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-loadbalancers/{uuid}/set_security_groups/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-loadbalancers/{uuid}/unlink/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-marketplace-tenants/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openstack-marketplace-tenants/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-marketplace-tenants/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-marketplace-tenants/{uuid}/create_image/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-marketplace-tenants/{uuid}/upload_image_data/{image_id}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-migrations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openstack-migrations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-migrations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/openstack-migrations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-migrations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/openstack-migrations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/openstack-migrations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-network-rbac-policies/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openstack-network-rbac-policies/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-network-rbac-policies/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/openstack-network-rbac-policies/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-network-rbac-policies/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/openstack-network-rbac-policies/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/openstack-network-rbac-policies/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-networks/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openstack-networks/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/openstack-networks/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-networks/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/openstack-networks/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/openstack-networks/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-networks/{uuid}/create_subnet/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-networks/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-networks/{uuid}/rbac_policy_create/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/openstack-networks/{uuid}/rbac_policy_delete/{rbac_policy_uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-networks/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-networks/{uuid}/set_mtu/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-networks/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-networks/{uuid}/unlink/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-pool-members/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openstack-pool-members/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-pool-members/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/openstack-pool-members/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-pool-members/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/openstack-pool-members/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/openstack-pool-members/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-pool-members/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-pools/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openstack-pools/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-pools/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/openstack-pools/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-pools/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/openstack-pools/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/openstack-pools/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-pools/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-ports/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: allowed_address_pairs
                - Items changed
                  - Properties changed
                    - New property: ip_address
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openstack-ports/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-ports/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: allowed_address_pairs
            - Items changed
              - Properties changed
                - Modified property: ip_address
                  - WriteOnly changed from true to false
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: allowed_address_pairs
              - Items changed
                - Properties changed
                  - New property: ip_address
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/openstack-ports/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-ports/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: allowed_address_pairs
              - Items changed
                - Properties changed
                  - New property: ip_address
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/openstack-ports/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: allowed_address_pairs
              - Items changed
                - Properties changed
                  - New property: ip_address
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/openstack-ports/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: allowed_address_pairs
            - Items changed
              - Properties changed
                - Modified property: ip_address
                  - WriteOnly changed from true to false
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: allowed_address_pairs
              - Items changed
                - Properties changed
                  - New property: ip_address
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-ports/{uuid}/disable_port/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-ports/{uuid}/disable_port_security/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-ports/{uuid}/enable_port/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-ports/{uuid}/enable_port_security/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-ports/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-ports/{uuid}/set_allowed_address_pairs/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: allowed_address_pairs
              - Items changed
                - Properties changed
                  - New property: ip_address
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-ports/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-ports/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-ports/{uuid}/unlink/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-ports/{uuid}/update_port_ip/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-ports/{uuid}/update_security_groups/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-routers/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: ports
                - Items changed
                  - Properties changed
                    - Modified property: allowed_address_pairs
                      - Items changed
                        - Properties changed
                          - New property: ip_address
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openstack-routers/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-routers/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/openstack-routers/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-routers/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: ports
              - Items changed
                - Properties changed
                  - Modified property: allowed_address_pairs
                    - Items changed
                      - Properties changed
                        - New property: ip_address
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-routers/{uuid}/add_router_interface/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-routers/{uuid}/available_external_networks/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-routers/{uuid}/effective_routes/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-routers/{uuid}/remove_external_gateway/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-routers/{uuid}/remove_router_interface/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-routers/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-routers/{uuid}/set_external_gateway/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-routers/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-routers/{uuid}/set_routes/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-security-groups/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openstack-security-groups/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/openstack-security-groups/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-security-groups/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/openstack-security-groups/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/openstack-security-groups/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-security-groups/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-security-groups/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-security-groups/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-security-groups/{uuid}/set_rules/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-security-groups/{uuid}/unlink/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-server-groups/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: instances
                - Items changed
                  - Properties changed
                    - Modified property: name
                      - MaxLength changed from 150 to 255
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openstack-server-groups/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-server-groups/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: instances
              - Items changed
                - Properties changed
                  - Modified property: name
                    - MaxLength changed from 150 to 255
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/openstack-server-groups/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-server-groups/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: instances
              - Items changed
                - Properties changed
                  - Modified property: name
                    - MaxLength changed from 150 to 255
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-server-groups/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-server-groups/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-server-groups/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-server-groups/{uuid}/unlink/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-snapshots/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openstack-snapshots/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/openstack-snapshots/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-snapshots/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/openstack-snapshots/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/openstack-snapshots/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-snapshots/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-snapshots/{uuid}/restorations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-snapshots/{uuid}/restore/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: name
              - MaxLength changed from 150 to 255
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-snapshots/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-snapshots/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-snapshots/{uuid}/unlink/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-subnets/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openstack-subnets/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/openstack-subnets/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-subnets/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/openstack-subnets/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/openstack-subnets/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-subnets/{uuid}/connect/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-subnets/{uuid}/disconnect/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-subnets/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-subnets/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-subnets/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-subnets/{uuid}/unlink/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-tenants/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openstack-tenants/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-tenants/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/openstack-tenants/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/openstack-tenants/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-tenants/{uuid}/backend_instances/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: name
                - MaxLength changed from 150 to 255
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-tenants/{uuid}/backend_volumes/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: name
                - MaxLength changed from 150 to 255
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-tenants/{uuid}/change_password/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-tenants/{uuid}/create_floating_ip/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-tenants/{uuid}/create_network/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-tenants/{uuid}/create_security_group/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-tenants/{uuid}/create_server_group/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: instances
              - Items changed
                - Properties changed
                  - Modified property: name
                    - MaxLength changed from 150 to 255
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-tenants/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-tenants/{uuid}/pull_floating_ips/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-tenants/{uuid}/pull_quotas/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-tenants/{uuid}/pull_security_groups/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-tenants/{uuid}/pull_server_groups/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-tenants/{uuid}/push_security_groups/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-tenants/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-tenants/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-tenants/{uuid}/set_quotas/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-tenants/{uuid}/topology/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-tenants/{uuid}/unlink/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-volume-availability-zones/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openstack-volume-availability-zones/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-volume-availability-zones/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-volume-types/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openstack-volume-types/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-volume-types/names/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openstack-volume-types/names/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-volume-types/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-volumes/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: name
                - MaxLength changed from 150 to 255
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/openstack-volumes/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack-volumes/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: name
              - MaxLength changed from 150 to 255
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/openstack-volumes/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: name
            - MaxLength changed from 150 to 255
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: name
              - MaxLength changed from 150 to 255
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/openstack-volumes/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: name
            - MaxLength changed from 150 to 255
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: name
              - MaxLength changed from 150 to 255
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-volumes/{uuid}/attach/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-volumes/{uuid}/detach/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-volumes/{uuid}/extend/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-volumes/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-volumes/{uuid}/retype/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-volumes/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-volumes/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-volumes/{uuid}/snapshot/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack-volumes/{uuid}/unlink/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack/discovery/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack/discovery/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack/discovery/discover_external_networks/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack/discovery/discover_flavors/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack/discovery/discover_instance_availability_zones/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack/discovery/discover_volume_availability_zones/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack/discovery/discover_volume_types/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack/discovery/preview_service_attributes/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/openstack/discovery/validate_credentials/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/openstack/discovery/{id}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/openstack/discovery/{id}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/openstack/discovery/{id}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/openstack/discovery/{id}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/organization-groups/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/organization-groups/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/organization-groups/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/organization-groups/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/organization-groups/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/organization-groups/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/organization-groups/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/override-settings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: AFFILIATES_ENABLED
            - New property: CHECK_FOR_UPDATES
            - New property: FEDERATED_IDENTITY_AUTHORITATIVE_ISD
            - New property: FEDERATED_IDENTITY_LOCKED_FIELDS
            - New property: OIDC_ALLOWED_USER_EMAIL_PATTERNS
            - New property: OIDC_BLOCKED_LOGIN_RESPONSE_MESSAGE
            - New property: ONBOARDING_DNB_API_URL
            - New property: ONBOARDING_DNB_CLIENT_ID
            - New property: ONBOARDING_DNB_CLIENT_SECRET
            - New property: ONBOARDING_DNB_RTS_API_URL
            - New property: ONBOARDING_DNB_TOKEN_URL
            - New property: OPENPORTAL_MEMBERSHIP_SYNC_MODE
            - New property: PAT_MAX_ACL_ENTRIES
            - New property: PAT_MAX_AUDIT_EVENTS_PER_HOUR
            - New property: POSIX_ID_POOL_UTILIZATION_THRESHOLD
            - New property: PROJECT_NAME_REGEX
            - New property: PROJECT_NAME_REGEX_ERROR_MESSAGE
            - New property: SCIM_INBOUND_SSH_KEYS_ENABLED
            - New property: SERVICE_ACCESS_MODE
            - New property: USER_REVISION_KEEP_MINIMUM
            - New property: USER_REVISION_RETENTION_DAYS
            - New property: WALDUR_SUPPORT_AUTO_ASSIGN
            - New property: WALDUR_SUPPORT_AUTO_ASSIGN_STRATEGY
            - New property: WALDUR_SUPPORT_PROVIDER_ROUTING_ENABLED
            - New property: WALDUR_SUPPORT_SLA_ENABLED
            - New property: WALDUR_SUPPORT_SLA_RESOLUTION_HOURS
            - New property: WALDUR_SUPPORT_SLA_RESPONSE_HOURS
            - Modified property: DEFAULT_CALL_USER_ATTRIBUTES
              - Items changed
                - Property 'OneOf' changed
                  - Modified schema: #/components/schemas/UserAttributeEnum
                    - New enum values: [address organization_vat_code organization_address active_isds uid_number primary_gid]
            - Modified property: DEFAULT_OFFERING_USER_ATTRIBUTES
              - Items changed
                - Property 'OneOf' changed
                  - Modified schema: #/components/schemas/UserAttributeEnum
                    - New enum values: [address organization_vat_code organization_address active_isds uid_number primary_gid]
            - Modified property: ENABLED_USER_PROFILE_ATTRIBUTES
              - Items changed
                - Property 'OneOf' changed
                  - Modified schema: #/components/schemas/UserAttributeEnum
                    - New enum values: [address organization_vat_code organization_address active_isds uid_number primary_gid]
            - Modified property: FEDERATED_IDENTITY_SYNC_ALLOWED_ATTRIBUTES
              - Items changed
                - Property 'OneOf' changed
                  - Modified schema: #/components/schemas/UserAttributeEnum
                    - New enum values: [address organization_vat_code organization_address active_isds uid_number primary_gid]
            - Modified property: INVITATION_ALLOWED_FIELDS
              - Items changed
                - Property 'OneOf' changed
                  - Modified schema: #/components/schemas/UserAttributeEnum
                    - New enum values: [address organization_vat_code organization_address active_isds uid_number primary_gid]
            - Modified property: MANDATORY_USER_ATTRIBUTES
              - Items changed
                - Property 'OneOf' changed
                  - Modified schema: #/components/schemas/UserAttributeEnum
                    - New enum values: [address organization_vat_code organization_address active_isds uid_number primary_gid]
            - Modified property: ONBOARDING_VALIDATION_METHODS
              - Items changed
                - Property 'OneOf' changed
                  - Modified schema: #/components/schemas/OnboardingValidationEnum
                    - New enum values: [dnb_se dnb_no dnb_dk dnb_fi]
            - Modified property: SCIM_INBOUND_ALLOWED_ATTRIBUTES
              - Items changed
                - Property 'OneOf' changed
                  - Modified schema: #/components/schemas/UserAttributeEnum
                    - New enum values: [address organization_vat_code organization_address active_isds uid_number primary_gid]
            - Modified property: WALDUR_SUPPORT_ACTIVE_BACKEND_TYPE
              - New enum values: [basic]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/override-settings/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: AFFILIATES_ENABLED
          - New property: CHECK_FOR_UPDATES
          - New property: FEDERATED_IDENTITY_AUTHORITATIVE_ISD
          - New property: FEDERATED_IDENTITY_LOCKED_FIELDS
          - New property: OIDC_ALLOWED_USER_EMAIL_PATTERNS
          - New property: OIDC_BLOCKED_LOGIN_RESPONSE_MESSAGE
          - New property: ONBOARDING_DNB_API_URL
          - New property: ONBOARDING_DNB_CLIENT_ID
          - New property: ONBOARDING_DNB_CLIENT_SECRET
          - New property: ONBOARDING_DNB_RTS_API_URL
          - New property: ONBOARDING_DNB_TOKEN_URL
          - New property: OPENPORTAL_MEMBERSHIP_SYNC_MODE
          - New property: PAT_MAX_ACL_ENTRIES
          - New property: PAT_MAX_AUDIT_EVENTS_PER_HOUR
          - New property: POSIX_ID_POOL_UTILIZATION_THRESHOLD
          - New property: PROJECT_NAME_REGEX
          - New property: PROJECT_NAME_REGEX_ERROR_MESSAGE
          - New property: SCIM_INBOUND_SSH_KEYS_ENABLED
          - New property: SERVICE_ACCESS_MODE
          - New property: USER_REVISION_KEEP_MINIMUM
          - New property: USER_REVISION_RETENTION_DAYS
          - New property: WALDUR_SUPPORT_AUTO_ASSIGN
          - New property: WALDUR_SUPPORT_AUTO_ASSIGN_STRATEGY
          - New property: WALDUR_SUPPORT_PROVIDER_ROUTING_ENABLED
          - New property: WALDUR_SUPPORT_SLA_ENABLED
          - New property: WALDUR_SUPPORT_SLA_RESOLUTION_HOURS
          - New property: WALDUR_SUPPORT_SLA_RESPONSE_HOURS
          - Modified property: DEFAULT_CALL_USER_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [address organization_vat_code organization_address active_isds uid_number primary_gid]
          - Modified property: DEFAULT_OFFERING_USER_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [address organization_vat_code organization_address active_isds uid_number primary_gid]
          - Modified property: ENABLED_USER_PROFILE_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [address organization_vat_code organization_address active_isds uid_number primary_gid]
          - Modified property: FEDERATED_IDENTITY_SYNC_ALLOWED_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [address organization_vat_code organization_address active_isds uid_number primary_gid]
          - Modified property: FREEIPA_GROUPNAME_PREFIX
            - MinLength changed from 0 to 1
          - Modified property: FREEIPA_USERNAME_PREFIX
            - MinLength changed from 0 to 1
          - Modified property: INVITATION_ALLOWED_FIELDS
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [address organization_vat_code organization_address active_isds uid_number primary_gid]
          - Modified property: MANDATORY_USER_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [address organization_vat_code organization_address active_isds uid_number primary_gid]
          - Modified property: ONBOARDING_VALIDATION_METHODS
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/OnboardingValidationEnum
                  - New enum values: [dnb_se dnb_no dnb_dk dnb_fi]
          - Modified property: SCIM_INBOUND_ALLOWED_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [address organization_vat_code organization_address active_isds uid_number primary_gid]
          - Modified property: WALDUR_SUPPORT_ACTIVE_BACKEND_TYPE
            - New enum values: [basic]
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: AFFILIATES_ENABLED
          - New property: CHECK_FOR_UPDATES
          - New property: FEDERATED_IDENTITY_AUTHORITATIVE_ISD
          - New property: FEDERATED_IDENTITY_LOCKED_FIELDS
          - New property: OIDC_ALLOWED_USER_EMAIL_PATTERNS
          - New property: OIDC_BLOCKED_LOGIN_RESPONSE_MESSAGE
          - New property: ONBOARDING_DNB_API_URL
          - New property: ONBOARDING_DNB_CLIENT_ID
          - New property: ONBOARDING_DNB_CLIENT_SECRET
          - New property: ONBOARDING_DNB_RTS_API_URL
          - New property: ONBOARDING_DNB_TOKEN_URL
          - New property: OPENPORTAL_MEMBERSHIP_SYNC_MODE
          - New property: PAT_MAX_ACL_ENTRIES
          - New property: PAT_MAX_AUDIT_EVENTS_PER_HOUR
          - New property: POSIX_ID_POOL_UTILIZATION_THRESHOLD
          - New property: PROJECT_NAME_REGEX
          - New property: PROJECT_NAME_REGEX_ERROR_MESSAGE
          - New property: SCIM_INBOUND_SSH_KEYS_ENABLED
          - New property: SERVICE_ACCESS_MODE
          - New property: USER_REVISION_KEEP_MINIMUM
          - New property: USER_REVISION_RETENTION_DAYS
          - New property: WALDUR_SUPPORT_AUTO_ASSIGN
          - New property: WALDUR_SUPPORT_AUTO_ASSIGN_STRATEGY
          - New property: WALDUR_SUPPORT_PROVIDER_ROUTING_ENABLED
          - New property: WALDUR_SUPPORT_SLA_ENABLED
          - New property: WALDUR_SUPPORT_SLA_RESOLUTION_HOURS
          - New property: WALDUR_SUPPORT_SLA_RESPONSE_HOURS
          - Modified property: DEFAULT_CALL_USER_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [address organization_vat_code organization_address active_isds uid_number primary_gid]
          - Modified property: DEFAULT_OFFERING_USER_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [address organization_vat_code organization_address active_isds uid_number primary_gid]
          - Modified property: ENABLED_USER_PROFILE_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [address organization_vat_code organization_address active_isds uid_number primary_gid]
          - Modified property: FEDERATED_IDENTITY_SYNC_ALLOWED_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [address organization_vat_code organization_address active_isds uid_number primary_gid]
          - Modified property: FREEIPA_GROUPNAME_PREFIX
            - MinLength changed from 0 to 1
          - Modified property: FREEIPA_USERNAME_PREFIX
            - MinLength changed from 0 to 1
          - Modified property: INVITATION_ALLOWED_FIELDS
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [address organization_vat_code organization_address active_isds uid_number primary_gid]
          - Modified property: MANDATORY_USER_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [address organization_vat_code organization_address active_isds uid_number primary_gid]
          - Modified property: ONBOARDING_VALIDATION_METHODS
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/OnboardingValidationEnum
                  - New enum values: [dnb_se dnb_no dnb_dk dnb_fi]
          - Modified property: SCIM_INBOUND_ALLOWED_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [address organization_vat_code organization_address active_isds uid_number primary_gid]
          - Modified property: WALDUR_SUPPORT_ACTIVE_BACKEND_TYPE
            - New enum values: [basic]
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: AFFILIATES_ENABLED
          - New property: CHECK_FOR_UPDATES
          - New property: FEDERATED_IDENTITY_AUTHORITATIVE_ISD
          - New property: FEDERATED_IDENTITY_LOCKED_FIELDS
          - New property: OIDC_ALLOWED_USER_EMAIL_PATTERNS
          - New property: OIDC_BLOCKED_LOGIN_RESPONSE_MESSAGE
          - New property: ONBOARDING_DNB_API_URL
          - New property: ONBOARDING_DNB_CLIENT_ID
          - New property: ONBOARDING_DNB_CLIENT_SECRET
          - New property: ONBOARDING_DNB_RTS_API_URL
          - New property: ONBOARDING_DNB_TOKEN_URL
          - New property: OPENPORTAL_MEMBERSHIP_SYNC_MODE
          - New property: PAT_MAX_ACL_ENTRIES
          - New property: PAT_MAX_AUDIT_EVENTS_PER_HOUR
          - New property: POSIX_ID_POOL_UTILIZATION_THRESHOLD
          - New property: PROJECT_NAME_REGEX
          - New property: PROJECT_NAME_REGEX_ERROR_MESSAGE
          - New property: SCIM_INBOUND_SSH_KEYS_ENABLED
          - New property: SERVICE_ACCESS_MODE
          - New property: USER_REVISION_KEEP_MINIMUM
          - New property: USER_REVISION_RETENTION_DAYS
          - New property: WALDUR_SUPPORT_AUTO_ASSIGN
          - New property: WALDUR_SUPPORT_AUTO_ASSIGN_STRATEGY
          - New property: WALDUR_SUPPORT_PROVIDER_ROUTING_ENABLED
          - New property: WALDUR_SUPPORT_SLA_ENABLED
          - New property: WALDUR_SUPPORT_SLA_RESOLUTION_HOURS
          - New property: WALDUR_SUPPORT_SLA_RESPONSE_HOURS
          - Modified property: DEFAULT_CALL_USER_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [address organization_vat_code organization_address active_isds uid_number primary_gid]
          - Modified property: DEFAULT_OFFERING_USER_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [address organization_vat_code organization_address active_isds uid_number primary_gid]
          - Modified property: ENABLED_USER_PROFILE_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [address organization_vat_code organization_address active_isds uid_number primary_gid]
          - Modified property: FEDERATED_IDENTITY_SYNC_ALLOWED_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [address organization_vat_code organization_address active_isds uid_number primary_gid]
          - Modified property: FREEIPA_GROUPNAME_PREFIX
            - MinLength changed from 0 to 1
          - Modified property: FREEIPA_USERNAME_PREFIX
            - MinLength changed from 0 to 1
          - Modified property: INVITATION_ALLOWED_FIELDS
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [address organization_vat_code organization_address active_isds uid_number primary_gid]
          - Modified property: MANDATORY_USER_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [address organization_vat_code organization_address active_isds uid_number primary_gid]
          - Modified property: ONBOARDING_VALIDATION_METHODS
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/OnboardingValidationEnum
                  - New enum values: [dnb_se dnb_no dnb_dk dnb_fi]
          - Modified property: SCIM_INBOUND_ALLOWED_ATTRIBUTES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/UserAttributeEnum
                  - New enum values: [address organization_vat_code organization_address active_isds uid_number primary_gid]
          - Modified property: WALDUR_SUPPORT_ACTIVE_BACKEND_TYPE
            - New enum values: [basic]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/payment-profiles/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: attributes
                - Properties changed
                  - Modified property: contract_sum
                    - Type changed from 'integer' to 'string'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/payment-profiles/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/payment-profiles/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: attributes
            - Properties changed
              - Modified property: contract_sum
                - Type changed from 'integer' to 'string'
                - MinLength changed from 0 to 1
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: attributes
              - Properties changed
                - Modified property: contract_sum
                  - Type changed from 'integer' to 'string'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/payment-profiles/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/payment-profiles/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: attributes
              - Properties changed
                - Modified property: contract_sum
                  - Type changed from 'integer' to 'string'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/payment-profiles/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: attributes
            - Properties changed
              - Modified property: contract_sum
                - Type changed from 'integer' to 'string'
                - MinLength changed from 0 to 1
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: attributes
              - Properties changed
                - Modified property: contract_sum
                  - Type changed from 'integer' to 'string'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/payment-profiles/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: attributes
            - Properties changed
              - Modified property: contract_sum
                - Type changed from 'integer' to 'string'
                - MinLength changed from 0 to 1
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: attributes
              - Properties changed
                - Modified property: contract_sum
                  - Type changed from 'integer' to 'string'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/payment-profiles/{uuid}/enable/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/payments/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/payments/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/payments/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/payments/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/payments/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/payments/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/payments/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/payments/{uuid}/link_to_invoice/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/payments/{uuid}/unlink_from_invoice/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/personal-access-tokens/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: allowed_networks
            - Properties changed
              - New property: allowed_networks
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/personal-access-tokens/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/personal-access-tokens/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: allowed_networks
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: allowed_networks
          - Properties changed
            - New property: allowed_networks
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/personal-access-tokens/available_binding_targets/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/personal-access-tokens/available_binding_targets/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/personal-access-tokens/available_scopes/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/personal-access-tokens/available_scopes/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/personal-access-tokens/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/personal-access-tokens/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: allowed_networks
          - Properties changed
            - New property: allowed_networks
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/personal-access-tokens/{uuid}/rotate/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: allowed_networks
          - Properties changed
            - New property: allowed_networks
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/project-credits/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: is_limited_by_organization_credit
              - New required property: spendable_value
            - Properties changed
              - New property: is_limited_by_organization_credit
              - New property: spendable_value
              - Modified property: allocated_customer_credit
                - Type changed from 'number' to 'string'
                - Format changed from 'double' to ''
                - Nullable changed from false to true
              - Modified property: consumption_last_month
                - Description changed from '' to 'Credit drawn by this project in the previous month.

None when that month has no invoice at all — no billing period is not
the same statement as "drew nothing", and callers should be able to
tell them apart.'
                - Nullable changed from false to true

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/project-credits/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/project-credits/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: is_limited_by_organization_credit
            - New required property: spendable_value
          - Properties changed
            - New property: is_limited_by_organization_credit
            - New property: spendable_value
            - Modified property: allocated_customer_credit
              - Type changed from 'number' to 'string'
              - Format changed from 'double' to ''
              - Nullable changed from false to true
            - Modified property: consumption_last_month
              - Description changed from '' to 'Credit drawn by this project in the previous month.

None when that month has no invoice at all — no billing period is not
the same statement as "drew nothing", and callers should be able to
tell them apart.'
              - Nullable changed from false to true

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/project-credits/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/project-credits/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: is_limited_by_organization_credit
            - New required property: spendable_value
          - Properties changed
            - New property: is_limited_by_organization_credit
            - New property: spendable_value
            - Modified property: allocated_customer_credit
              - Type changed from 'number' to 'string'
              - Format changed from 'double' to ''
              - Nullable changed from false to true
            - Modified property: consumption_last_month
              - Description changed from '' to 'Credit drawn by this project in the previous month.

None when that month has no invoice at all — no billing period is not
the same statement as "drew nothing", and callers should be able to
tell them apart.'
              - Nullable changed from false to true

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/project-credits/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: is_limited_by_organization_credit
            - New required property: spendable_value
          - Properties changed
            - New property: is_limited_by_organization_credit
            - New property: spendable_value
            - Modified property: allocated_customer_credit
              - Type changed from 'number' to 'string'
              - Format changed from 'double' to ''
              - Nullable changed from false to true
            - Modified property: consumption_last_month
              - Description changed from '' to 'Credit drawn by this project in the previous month.

None when that month has no invoice at all — no billing period is not
the same statement as "drew nothing", and callers should be able to
tell them apart.'
              - Nullable changed from false to true

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/project-credits/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: is_limited_by_organization_credit
            - New required property: spendable_value
          - Properties changed
            - New property: is_limited_by_organization_credit
            - New property: spendable_value
            - Modified property: allocated_customer_credit
              - Type changed from 'number' to 'string'
              - Format changed from 'double' to ''
              - Nullable changed from false to true
            - Modified property: consumption_last_month
              - Description changed from '' to 'Credit drawn by this project in the previous month.

None when that month has no invoice at all — no billing period is not
the same statement as "drew nothing", and callers should be able to
tell them apart.'
              - Nullable changed from false to true

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/project-end-date-change-requests/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/project-end-date-change-requests/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/project-end-date-change-requests/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/project-end-date-change-requests/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/project-end-date-change-requests/{uuid}/approve/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/project-end-date-change-requests/{uuid}/cancel/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/project-end-date-change-requests/{uuid}/reject/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/project-permissions-reviews/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/project-permissions-reviews/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/project-permissions-reviews/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/project-permissions-reviews/{uuid}/close/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/project-quotas/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/project-quotas/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/project-types/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/project-types/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/project-types/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/projects/

- New query param: current_user_has_role
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from null to 4096
              - Modified property: project_metadata
                - Items changed
                  - Properties changed
                    - Modified property: answer
                      - Type changed from 'object' to ''
                      - AdditionalProperties changed from true to null
              - Modified property: staff_notes
                - MaxLength changed from null to 4096
              - Modified property: user_affiliations
                - Type changed from 'object' to 'array'
                - AdditionalProperties changed from true to null
                - Items changed
                  - Schema added
              - Modified property: user_email_patterns
                - Type changed from 'object' to 'array'
                - AdditionalProperties changed from true to null
                - Items changed
                  - Schema added
              - Modified property: user_identity_sources
                - Type changed from 'object' to 'array'
                - Description changed from 'List of allowed identity sources (identity providers).' to ''
                - AdditionalProperties changed from true to null
                - Items changed
                  - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/projects/

- New query param: current_user_has_role
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/projects/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from null to 4096
          - Modified property: staff_notes
            - MaxLength changed from null to 4096
          - Modified property: user_affiliations
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_email_patterns
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_identity_sources
            - Type changed from 'object' to 'array'
            - Description changed from 'List of allowed identity sources (identity providers).' to ''
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from null to 4096
          - Modified property: staff_notes
            - MaxLength changed from null to 4096
          - Modified property: user_affiliations
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_email_patterns
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_identity_sources
            - Type changed from 'object' to 'array'
            - Description changed from 'List of allowed identity sources (identity providers).' to ''
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from null to 4096
          - Modified property: staff_notes
            - MaxLength changed from null to 4096
          - Modified property: user_affiliations
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_email_patterns
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_identity_sources
            - Type changed from 'object' to 'array'
            - Description changed from 'List of allowed identity sources (identity providers).' to ''
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from null to 4096
            - Modified property: project_metadata
              - Items changed
                - Properties changed
                  - Modified property: answer
                    - Type changed from 'object' to ''
                    - AdditionalProperties changed from true to null
            - Modified property: staff_notes
              - MaxLength changed from null to 4096
            - Modified property: user_affiliations
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_email_patterns
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_identity_sources
              - Type changed from 'object' to 'array'
              - Description changed from 'List of allowed identity sources (identity providers).' to ''
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/projects/checklist-template/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/projects/checklist-template/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/projects/{project_uuid}/other_users/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/projects/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/projects/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from null to 4096
            - Modified property: project_metadata
              - Items changed
                - Properties changed
                  - Modified property: answer
                    - Type changed from 'object' to ''
                    - AdditionalProperties changed from true to null
            - Modified property: staff_notes
              - MaxLength changed from null to 4096
            - Modified property: user_affiliations
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_email_patterns
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_identity_sources
              - Type changed from 'object' to 'array'
              - Description changed from 'List of allowed identity sources (identity providers).' to ''
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/projects/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from null to 4096
          - Modified property: staff_notes
            - MaxLength changed from null to 4096
          - Modified property: user_affiliations
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_email_patterns
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_identity_sources
            - Type changed from 'object' to 'array'
            - Description changed from 'List of allowed identity sources (identity providers).' to ''
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from null to 4096
          - Modified property: staff_notes
            - MaxLength changed from null to 4096
          - Modified property: user_affiliations
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_email_patterns
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_identity_sources
            - Type changed from 'object' to 'array'
            - Description changed from 'List of allowed identity sources (identity providers).' to ''
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from null to 4096
          - Modified property: staff_notes
            - MaxLength changed from null to 4096
          - Modified property: user_affiliations
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_email_patterns
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_identity_sources
            - Type changed from 'object' to 'array'
            - Description changed from 'List of allowed identity sources (identity providers).' to ''
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from null to 4096
            - Modified property: project_metadata
              - Items changed
                - Properties changed
                  - Modified property: answer
                    - Type changed from 'object' to ''
                    - AdditionalProperties changed from true to null
            - Modified property: staff_notes
              - MaxLength changed from null to 4096
            - Modified property: user_affiliations
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_email_patterns
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_identity_sources
              - Type changed from 'object' to 'array'
              - Description changed from 'List of allowed identity sources (identity providers).' to ''
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/projects/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from null to 4096
          - Modified property: staff_notes
            - MaxLength changed from null to 4096
          - Modified property: user_affiliations
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_email_patterns
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_identity_sources
            - Type changed from 'object' to 'array'
            - Description changed from 'List of allowed identity sources (identity providers).' to ''
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from null to 4096
          - Modified property: staff_notes
            - MaxLength changed from null to 4096
          - Modified property: user_affiliations
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_email_patterns
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_identity_sources
            - Type changed from 'object' to 'array'
            - Description changed from 'List of allowed identity sources (identity providers).' to ''
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from null to 4096
          - Modified property: staff_notes
            - MaxLength changed from null to 4096
          - Modified property: user_affiliations
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_email_patterns
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_identity_sources
            - Type changed from 'object' to 'array'
            - Description changed from 'List of allowed identity sources (identity providers).' to ''
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from null to 4096
            - Modified property: project_metadata
              - Items changed
                - Properties changed
                  - Modified property: answer
                    - Type changed from 'object' to ''
                    - AdditionalProperties changed from true to null
            - Modified property: staff_notes
              - MaxLength changed from null to 4096
            - Modified property: user_affiliations
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_email_patterns
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_identity_sources
              - Type changed from 'object' to 'array'
              - Description changed from 'List of allowed identity sources (identity providers).' to ''
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/projects/{uuid}/add_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/projects/{uuid}/checklist/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/projects/{uuid}/completion_status/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/projects/{uuid}/delete_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/projects/{uuid}/list_users/

- Modified query param: role
  - Description changed from 'Role UUID or name' to 'Role UUID or name. Repeat to filter by several roles.'
  - Schema changed
    - Type changed from 'string' to 'array'
    - Format changed from 'uuid' to ''
    - Items changed
      - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/projects/{uuid}/move_project/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from null to 4096
            - Modified property: project_metadata
              - Items changed
                - Properties changed
                  - Modified property: answer
                    - Type changed from 'object' to ''
                    - AdditionalProperties changed from true to null
            - Modified property: staff_notes
              - MaxLength changed from null to 4096
            - Modified property: user_affiliations
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_email_patterns
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_identity_sources
              - Type changed from 'object' to 'array'
              - Description changed from 'List of allowed identity sources (identity providers).' to ''
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/projects/{uuid}/recover/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from null to 4096
            - Modified property: project_metadata
              - Items changed
                - Properties changed
                  - Modified property: answer
                    - Type changed from 'object' to ''
                    - AdditionalProperties changed from true to null
            - Modified property: staff_notes
              - MaxLength changed from null to 4096
            - Modified property: user_affiliations
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_email_patterns
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_identity_sources
              - Type changed from 'object' to 'array'
              - Description changed from 'List of allowed identity sources (identity providers).' to ''
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/projects/{uuid}/stats/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/projects/{uuid}/submit_answers/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/projects/{uuid}/sync_user_roles/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/projects/{uuid}/update_affiliation/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/projects/{uuid}/update_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/promotions-campaigns/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/promotions-campaigns/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/promotions-campaigns/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/promotions-campaigns/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/promotions-campaigns/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/promotions-campaigns/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/promotions-campaigns/{uuid}/activate/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/promotions-campaigns/{uuid}/orders/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [consumer_message_updated_at created_by_organization_address created_by_organization_country created_by_organization_vat_code provider_message_updated_at]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: consumer_message_updated_at
              - New property: created_by_organization_address
              - New property: created_by_organization_country
              - New property: created_by_organization_vat_code
              - New property: provider_message_updated_at
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/promotions-campaigns/{uuid}/resources/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [has_api_keys resource_effective_end_date usage_limit_restriction]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: has_api_keys
              - New property: resource_effective_end_date
              - New property: usage_limit_restriction
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: consumer_message_updated_at
                      - New property: created_by_organization_address
                      - New property: created_by_organization_country
                      - New property: created_by_organization_vat_code
                      - New property: provider_message_updated_at
              - Modified property: limit_usage
                - Description changed from 'Dictionary mapping limit-based component types to their consumed usage. For monthly periods, maps from current_usages; for longer periods, aggregates historical usage.' to 'Dictionary mapping limit-based component types to their consumed usage. Sums the ComponentUsage rows of the component's current period (the monthly billing period unless the component defines a longer limit_period), i.e. the period's high-watermark rather than the instantaneous current_usages value.'
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - New property: consumer_message_updated_at
                      - New property: created_by_organization_address
                      - New property: created_by_organization_country
                      - New property: created_by_organization_vat_code
                      - New property: provider_message_updated_at
              - Modified property: project_effective_end_date
                - Description changed from 'Effective project end date including grace period. After this date, resources will be terminated.' to 'Effective project end date including grace period. After this date, resources are terminated, except resources of offerings that disable the grace period — those are terminated on the raw project end date.'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/promotions-campaigns/{uuid}/terminate/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-proposals/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: applicant_organization_address
              - New required property: applicant_organization_vat_code
              - New required property: workflow_step
            - Properties changed
              - New property: applicant_organization_address
              - New property: applicant_organization_vat_code
              - New property: workflow_step
              - Modified property: applicant_active_isds
                - Type changed from 'object' to 'array'
                - Description changed from 'List of ISDs that have asserted this user exists. User is deactivated when this becomes empty.' to ''
                - AdditionalProperties changed from true to null
                - Items changed
                  - Schema added
              - Modified property: applicant_affiliations
                - Type changed from 'object' to 'array'
                - Description changed from 'Person's affiliation within organization such as student, faculty, staff.' to ''
                - AdditionalProperties changed from true to null
                - Items changed
                  - Schema added
              - Modified property: applicant_eduperson_assurance
                - Type changed from 'object' to 'array'
                - Description changed from 'REFEDS assurance profile URIs from identity provider' to ''
                - AdditionalProperties changed from true to null
                - Items changed
                  - Schema added
              - Modified property: applicant_nationalities
                - Type changed from 'object' to 'array'
                - Description changed from 'List of all citizenships (ISO 3166-1 alpha-2 codes)' to ''
                - AdditionalProperties changed from true to null
                - Items changed
                  - Schema added
              - Modified property: description
                - MaxLength changed from null to 4096
              - Modified property: round
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/NestedRound
                    - Properties changed
                      - Deleted property: allocation_time
                      - Deleted property: deciding_entity
                      - Deleted property: minimal_average_scoring
                      - Deleted property: minimum_number_of_reviewers
                      - Deleted property: review_strategy
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/proposal-proposals/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-proposals/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: description
            - MaxLength changed from null to 4096
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: applicant_organization_address
            - New required property: applicant_organization_vat_code
            - New required property: workflow_step
          - Properties changed
            - New property: applicant_organization_address
            - New property: applicant_organization_vat_code
            - New property: workflow_step
            - Modified property: applicant_active_isds
              - Type changed from 'object' to 'array'
              - Description changed from 'List of ISDs that have asserted this user exists. User is deactivated when this becomes empty.' to ''
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: applicant_affiliations
              - Type changed from 'object' to 'array'
              - Description changed from 'Person's affiliation within organization such as student, faculty, staff.' to ''
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: applicant_eduperson_assurance
              - Type changed from 'object' to 'array'
              - Description changed from 'REFEDS assurance profile URIs from identity provider' to ''
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: applicant_nationalities
              - Type changed from 'object' to 'array'
              - Description changed from 'List of all citizenships (ISO 3166-1 alpha-2 codes)' to ''
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: description
              - MaxLength changed from null to 4096
            - Modified property: round
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRound
                  - Properties changed
                    - Deleted property: allocation_time
                    - Deleted property: deciding_entity
                    - Deleted property: minimal_average_scoring
                    - Deleted property: minimum_number_of_reviewers
                    - Deleted property: review_strategy
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-proposals/checklist-template/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/proposal-proposals/checklist-template/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/proposal-proposals/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-proposals/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: applicant_organization_address
            - New required property: applicant_organization_vat_code
            - New required property: workflow_step
          - Properties changed
            - New property: applicant_organization_address
            - New property: applicant_organization_vat_code
            - New property: workflow_step
            - Modified property: applicant_active_isds
              - Type changed from 'object' to 'array'
              - Description changed from 'List of ISDs that have asserted this user exists. User is deactivated when this becomes empty.' to ''
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: applicant_affiliations
              - Type changed from 'object' to 'array'
              - Description changed from 'Person's affiliation within organization such as student, faculty, staff.' to ''
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: applicant_eduperson_assurance
              - Type changed from 'object' to 'array'
              - Description changed from 'REFEDS assurance profile URIs from identity provider' to ''
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: applicant_nationalities
              - Type changed from 'object' to 'array'
              - Description changed from 'List of all citizenships (ISO 3166-1 alpha-2 codes)' to ''
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: description
              - MaxLength changed from null to 4096
            - Modified property: round
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRound
                  - Properties changed
                    - Deleted property: allocation_time
                    - Deleted property: deciding_entity
                    - Deleted property: minimal_average_scoring
                    - Deleted property: minimum_number_of_reviewers
                    - Deleted property: review_strategy
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-proposals/{uuid}/add_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-proposals/{uuid}/advance_workflow_step/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-proposals/{uuid}/attach_document/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-proposals/{uuid}/checklist/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-proposals/{uuid}/checklist_review/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-proposals/{uuid}/complete_workflow_step/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-proposals/{uuid}/completion_review_status/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-proposals/{uuid}/completion_status/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-proposals/{uuid}/delete_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-proposals/{uuid}/detach_documents/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-proposals/{uuid}/list_users/

- Modified query param: role
  - Description changed from 'Role UUID or name' to 'Role UUID or name. Repeat to filter by several roles.'
  - Schema changed
    - Type changed from 'string' to 'array'
    - Format changed from 'uuid' to ''
    - Items changed
      - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-proposals/{uuid}/reject_workflow_step/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-proposals/{uuid}/resources/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: attachment
              - New required property: has_purchase_order
              - New required property: purchase_order_required
            - Properties changed
              - New property: attachment
              - New property: has_purchase_order
              - New property: purchase_order_reference
              - New property: purchase_order_required
              - Modified property: requested_offering
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/NestedRequestedOffering
                    - Properties changed
                      - New property: offering_type
                      - New property: require_purchase_order
                      - Modified property: plan_details
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/BasePublicPlan
                            - Properties changed
                              - Modified property: components
                                - Items changed
                                  - Properties changed
                                    - New property: discount_aggregation
                                    - New property: discount_formula
                                    - Deleted property: discount_rate
                                    - Deleted property: discount_threshold
                                    - Deleted property: discounted_price
                              - Modified property: description
                                - MaxLength changed from null to 4096
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-proposals/{uuid}/resources/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: purchase_order_reference
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: attachment
            - New required property: has_purchase_order
            - New required property: purchase_order_required
          - Properties changed
            - New property: attachment
            - New property: has_purchase_order
            - New property: purchase_order_reference
            - New property: purchase_order_required
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - New property: offering_type
                    - New property: require_purchase_order
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: components
                              - Items changed
                                - Properties changed
                                  - New property: discount_aggregation
                                  - New property: discount_formula
                                  - Deleted property: discount_rate
                                  - Deleted property: discount_threshold
                                  - Deleted property: discounted_price
                            - Modified property: description
                              - MaxLength changed from null to 4096
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: attachment
            - New required property: has_purchase_order
            - New required property: purchase_order_required
          - Properties changed
            - New property: attachment
            - New property: has_purchase_order
            - New property: purchase_order_reference
            - New property: purchase_order_required
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - New property: offering_type
                    - New property: require_purchase_order
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: components
                              - Items changed
                                - Properties changed
                                  - New property: discount_aggregation
                                  - New property: discount_formula
                                  - Deleted property: discount_rate
                                  - Deleted property: discount_threshold
                                  - Deleted property: discounted_price
                            - Modified property: description
                              - MaxLength changed from null to 4096
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: attachment
            - New required property: has_purchase_order
            - New required property: purchase_order_required
          - Properties changed
            - New property: attachment
            - New property: has_purchase_order
            - New property: purchase_order_reference
            - New property: purchase_order_required
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - New property: offering_type
                    - New property: require_purchase_order
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: components
                              - Items changed
                                - Properties changed
                                  - New property: discount_aggregation
                                  - New property: discount_formula
                                  - Deleted property: discount_rate
                                  - Deleted property: discount_threshold
                                  - Deleted property: discounted_price
                            - Modified property: description
                              - MaxLength changed from null to 4096
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: purchase_order_reference
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: attachment
            - New required property: has_purchase_order
            - New required property: purchase_order_required
          - Properties changed
            - New property: attachment
            - New property: has_purchase_order
            - New property: purchase_order_reference
            - New property: purchase_order_required
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - New property: offering_type
                    - New property: require_purchase_order
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: components
                              - Items changed
                                - Properties changed
                                  - New property: discount_aggregation
                                  - New property: discount_formula
                                  - Deleted property: discount_rate
                                  - Deleted property: discount_threshold
                                  - Deleted property: discounted_price
                            - Modified property: description
                              - MaxLength changed from null to 4096
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: purchase_order_reference
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: attachment
            - New required property: has_purchase_order
            - New required property: purchase_order_required
          - Properties changed
            - New property: attachment
            - New property: has_purchase_order
            - New property: purchase_order_reference
            - New property: purchase_order_required
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - New property: offering_type
                    - New property: require_purchase_order
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: components
                              - Items changed
                                - Properties changed
                                  - New property: discount_aggregation
                                  - New property: discount_formula
                                  - Deleted property: discount_rate
                                  - Deleted property: discount_threshold
                                  - Deleted property: discounted_price
                            - Modified property: description
                              - MaxLength changed from null to 4096
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-proposals/{uuid}/submit/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-proposals/{uuid}/submit_answers/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-proposals/{uuid}/update_project_details/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-proposals/{uuid}/update_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-proposals/{uuid}/workflow_states/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: checklist_status
            - Properties changed
              - New property: checklist_status
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-protected-calls/

- New query param: open_for_offering_uuid
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [has_proposals]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: has_proposals
              - Modified property: applicant_visibility_config
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/CallApplicantVisibilityConfig
                    - Properties changed
                      - New property: expose_organization_address
                      - New property: expose_organization_vat_code
                      - New property: expose_primary_gid
                      - New property: expose_uid_number
              - Modified property: description
                - MaxLength changed from null to 4096
              - Modified property: offerings
                - Items changed
                  - Properties changed
                    - New property: offering_type
                    - New property: require_purchase_order
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: components
                              - Items changed
                                - Properties changed
                                  - New property: discount_aggregation
                                  - New property: discount_formula
                                  - Deleted property: discount_rate
                                  - Deleted property: discount_threshold
                                  - Deleted property: discounted_price
                            - Modified property: description
                              - MaxLength changed from null to 4096
              - Modified property: resource_templates
                - Items changed
                  - Properties changed
                    - New property: requested_offering_components
                    - New property: requested_offering_type
                    - Modified property: requested_offering_plan
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: components
                              - Items changed
                                - Properties changed
                                  - New property: discount_aggregation
                                  - New property: discount_formula
                                  - Deleted property: discount_rate
                                  - Deleted property: discount_threshold
                                  - Deleted property: discounted_price
                            - Modified property: description
                              - MaxLength changed from null to 4096
              - Modified property: rounds
                - Items changed
                  - Properties changed
                    - Deleted property: allocation_time
                    - Deleted property: deciding_entity
                    - Deleted property: minimal_average_scoring
                    - Deleted property: minimum_number_of_reviewers
                    - Deleted property: review_strategy
              - Modified property: user_affiliations
                - Type changed from 'object' to 'array'
                - AdditionalProperties changed from true to null
                - Items changed
                  - Schema added
              - Modified property: user_assurance_levels
                - Type changed from 'object' to 'array'
                - AdditionalProperties changed from true to null
                - Items changed
                  - Schema added
              - Modified property: user_email_patterns
                - Type changed from 'object' to 'array'
                - AdditionalProperties changed from true to null
                - Items changed
                  - Schema added
              - Modified property: user_identity_sources
                - Type changed from 'object' to 'array'
                - AdditionalProperties changed from true to null
                - Items changed
                  - Schema added
              - Modified property: user_nationalities
                - Type changed from 'object' to 'array'
                - AdditionalProperties changed from true to null
                - Items changed
                  - Schema added
              - Modified property: user_organization_types
                - Type changed from 'object' to 'array'
                - AdditionalProperties changed from true to null
                - Items changed
                  - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/proposal-protected-calls/

- New query param: open_for_offering_uuid
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-protected-calls/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: applicant_visibility_config
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/CallApplicantVisibilityConfigRequest
                - Properties changed
                  - New property: expose_organization_address
                  - New property: expose_organization_vat_code
                  - New property: expose_primary_gid
                  - New property: expose_uid_number
          - Modified property: description
            - MaxLength changed from null to 4096
          - Modified property: user_affiliations
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_assurance_levels
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_email_patterns
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_identity_sources
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_nationalities
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_organization_types
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_proposals
            - Modified property: applicant_visibility_config
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/CallApplicantVisibilityConfig
                  - Properties changed
                    - New property: expose_organization_address
                    - New property: expose_organization_vat_code
                    - New property: expose_primary_gid
                    - New property: expose_uid_number
            - Modified property: description
              - MaxLength changed from null to 4096
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - New property: offering_type
                  - New property: require_purchase_order
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: discount_aggregation
                                - New property: discount_formula
                                - Deleted property: discount_rate
                                - Deleted property: discount_threshold
                                - Deleted property: discounted_price
                          - Modified property: description
                            - MaxLength changed from null to 4096
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - New property: requested_offering_components
                  - New property: requested_offering_type
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: discount_aggregation
                                - New property: discount_formula
                                - Deleted property: discount_rate
                                - Deleted property: discount_threshold
                                - Deleted property: discounted_price
                          - Modified property: description
                            - MaxLength changed from null to 4096
            - Modified property: rounds
              - Items changed
                - Properties changed
                  - Deleted property: allocation_time
                  - Deleted property: deciding_entity
                  - Deleted property: minimal_average_scoring
                  - Deleted property: minimum_number_of_reviewers
                  - Deleted property: review_strategy
            - Modified property: user_affiliations
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_assurance_levels
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_email_patterns
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_identity_sources
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_nationalities
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_organization_types
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-protected-calls/available_compliance_checklists/

- New query param: open_for_offering_uuid
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/proposal-protected-calls/available_compliance_checklists/

- New query param: open_for_offering_uuid
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/proposal-protected-calls/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-protected-calls/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [has_proposals]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_proposals
            - Modified property: applicant_visibility_config
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/CallApplicantVisibilityConfig
                  - Properties changed
                    - New property: expose_organization_address
                    - New property: expose_organization_vat_code
                    - New property: expose_primary_gid
                    - New property: expose_uid_number
            - Modified property: description
              - MaxLength changed from null to 4096
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - New property: offering_type
                  - New property: require_purchase_order
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: discount_aggregation
                                - New property: discount_formula
                                - Deleted property: discount_rate
                                - Deleted property: discount_threshold
                                - Deleted property: discounted_price
                          - Modified property: description
                            - MaxLength changed from null to 4096
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - New property: requested_offering_components
                  - New property: requested_offering_type
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: discount_aggregation
                                - New property: discount_formula
                                - Deleted property: discount_rate
                                - Deleted property: discount_threshold
                                - Deleted property: discounted_price
                          - Modified property: description
                            - MaxLength changed from null to 4096
            - Modified property: rounds
              - Items changed
                - Properties changed
                  - Deleted property: allocation_time
                  - Deleted property: deciding_entity
                  - Deleted property: minimal_average_scoring
                  - Deleted property: minimum_number_of_reviewers
                  - Deleted property: review_strategy
            - Modified property: user_affiliations
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_assurance_levels
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_email_patterns
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_identity_sources
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_nationalities
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_organization_types
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/proposal-protected-calls/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: applicant_visibility_config
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/CallApplicantVisibilityConfigRequest
                - Properties changed
                  - New property: expose_organization_address
                  - New property: expose_organization_vat_code
                  - New property: expose_primary_gid
                  - New property: expose_uid_number
          - Modified property: description
            - MaxLength changed from null to 4096
          - Modified property: user_affiliations
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_assurance_levels
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_email_patterns
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_identity_sources
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_nationalities
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_organization_types
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_proposals
            - Modified property: applicant_visibility_config
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/CallApplicantVisibilityConfig
                  - Properties changed
                    - New property: expose_organization_address
                    - New property: expose_organization_vat_code
                    - New property: expose_primary_gid
                    - New property: expose_uid_number
            - Modified property: description
              - MaxLength changed from null to 4096
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - New property: offering_type
                  - New property: require_purchase_order
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: discount_aggregation
                                - New property: discount_formula
                                - Deleted property: discount_rate
                                - Deleted property: discount_threshold
                                - Deleted property: discounted_price
                          - Modified property: description
                            - MaxLength changed from null to 4096
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - New property: requested_offering_components
                  - New property: requested_offering_type
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: discount_aggregation
                                - New property: discount_formula
                                - Deleted property: discount_rate
                                - Deleted property: discount_threshold
                                - Deleted property: discounted_price
                          - Modified property: description
                            - MaxLength changed from null to 4096
            - Modified property: rounds
              - Items changed
                - Properties changed
                  - Deleted property: allocation_time
                  - Deleted property: deciding_entity
                  - Deleted property: minimal_average_scoring
                  - Deleted property: minimum_number_of_reviewers
                  - Deleted property: review_strategy
            - Modified property: user_affiliations
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_assurance_levels
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_email_patterns
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_identity_sources
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_nationalities
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_organization_types
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/proposal-protected-calls/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: applicant_visibility_config
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/CallApplicantVisibilityConfigRequest
                - Properties changed
                  - New property: expose_organization_address
                  - New property: expose_organization_vat_code
                  - New property: expose_primary_gid
                  - New property: expose_uid_number
          - Modified property: description
            - MaxLength changed from null to 4096
          - Modified property: user_affiliations
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_assurance_levels
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_email_patterns
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_identity_sources
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_nationalities
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_organization_types
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_proposals
            - Modified property: applicant_visibility_config
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/CallApplicantVisibilityConfig
                  - Properties changed
                    - New property: expose_organization_address
                    - New property: expose_organization_vat_code
                    - New property: expose_primary_gid
                    - New property: expose_uid_number
            - Modified property: description
              - MaxLength changed from null to 4096
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - New property: offering_type
                  - New property: require_purchase_order
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: discount_aggregation
                                - New property: discount_formula
                                - Deleted property: discount_rate
                                - Deleted property: discount_threshold
                                - Deleted property: discounted_price
                          - Modified property: description
                            - MaxLength changed from null to 4096
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - New property: requested_offering_components
                  - New property: requested_offering_type
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: discount_aggregation
                                - New property: discount_formula
                                - Deleted property: discount_rate
                                - Deleted property: discount_threshold
                                - Deleted property: discounted_price
                          - Modified property: description
                            - MaxLength changed from null to 4096
            - Modified property: rounds
              - Items changed
                - Properties changed
                  - Deleted property: allocation_time
                  - Deleted property: deciding_entity
                  - Deleted property: minimal_average_scoring
                  - Deleted property: minimum_number_of_reviewers
                  - Deleted property: review_strategy
            - Modified property: user_affiliations
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_assurance_levels
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_email_patterns
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_identity_sources
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_nationalities
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_organization_types
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-protected-calls/{uuid}/activate/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-protected-calls/{uuid}/add_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-protected-calls/{uuid}/affinity-matrix/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-protected-calls/{uuid}/archive/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-protected-calls/{uuid}/attach_documents/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-protected-calls/{uuid}/coi-configuration/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: disclosure_only_types
              - Items changed
                - New enum values: [INST_SAME FIN_DIRECT REL_FAMILY ROLE_NAMED COLLAB_ACTIVE REL_MENTOR REL_SUPERVISOR COAUTH_RECENT INST_DEPT INST_FORMER ROLE_CONF COLLAB_GRANT REL_EDITORIAL COMPET COAUTH_OLD INST_CONSORT CONF_ATTEND SOC_MEMBER]
            - Modified property: management_allowed_types
              - Items changed
                - New enum values: [INST_SAME FIN_DIRECT REL_FAMILY ROLE_NAMED COLLAB_ACTIVE REL_MENTOR REL_SUPERVISOR COAUTH_RECENT INST_DEPT INST_FORMER ROLE_CONF COLLAB_GRANT REL_EDITORIAL COMPET COAUTH_OLD INST_CONSORT CONF_ATTEND SOC_MEMBER]
            - Modified property: recusal_required_types
              - Items changed
                - New enum values: [INST_SAME FIN_DIRECT REL_FAMILY ROLE_NAMED COLLAB_ACTIVE REL_MENTOR REL_SUPERVISOR COAUTH_RECENT INST_DEPT INST_FORMER ROLE_CONF COLLAB_GRANT REL_EDITORIAL COMPET COAUTH_OLD INST_CONSORT CONF_ATTEND SOC_MEMBER]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/proposal-protected-calls/{uuid}/coi-configuration/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: disclosure_only_types
            - Items changed
              - New enum values: [INST_SAME FIN_DIRECT REL_FAMILY ROLE_NAMED COLLAB_ACTIVE REL_MENTOR REL_SUPERVISOR COAUTH_RECENT INST_DEPT INST_FORMER ROLE_CONF COLLAB_GRANT REL_EDITORIAL COMPET COAUTH_OLD INST_CONSORT CONF_ATTEND SOC_MEMBER]
              - MinLength changed from 1 to 0
          - Modified property: management_allowed_types
            - Items changed
              - New enum values: [INST_SAME FIN_DIRECT REL_FAMILY ROLE_NAMED COLLAB_ACTIVE REL_MENTOR REL_SUPERVISOR COAUTH_RECENT INST_DEPT INST_FORMER ROLE_CONF COLLAB_GRANT REL_EDITORIAL COMPET COAUTH_OLD INST_CONSORT CONF_ATTEND SOC_MEMBER]
              - MinLength changed from 1 to 0
          - Modified property: recusal_required_types
            - Items changed
              - New enum values: [INST_SAME FIN_DIRECT REL_FAMILY ROLE_NAMED COLLAB_ACTIVE REL_MENTOR REL_SUPERVISOR COAUTH_RECENT INST_DEPT INST_FORMER ROLE_CONF COLLAB_GRANT REL_EDITORIAL COMPET COAUTH_OLD INST_CONSORT CONF_ATTEND SOC_MEMBER]
              - MinLength changed from 1 to 0
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: disclosure_only_types
              - Items changed
                - New enum values: [INST_SAME FIN_DIRECT REL_FAMILY ROLE_NAMED COLLAB_ACTIVE REL_MENTOR REL_SUPERVISOR COAUTH_RECENT INST_DEPT INST_FORMER ROLE_CONF COLLAB_GRANT REL_EDITORIAL COMPET COAUTH_OLD INST_CONSORT CONF_ATTEND SOC_MEMBER]
            - Modified property: management_allowed_types
              - Items changed
                - New enum values: [INST_SAME FIN_DIRECT REL_FAMILY ROLE_NAMED COLLAB_ACTIVE REL_MENTOR REL_SUPERVISOR COAUTH_RECENT INST_DEPT INST_FORMER ROLE_CONF COLLAB_GRANT REL_EDITORIAL COMPET COAUTH_OLD INST_CONSORT CONF_ATTEND SOC_MEMBER]
            - Modified property: recusal_required_types
              - Items changed
                - New enum values: [INST_SAME FIN_DIRECT REL_FAMILY ROLE_NAMED COLLAB_ACTIVE REL_MENTOR REL_SUPERVISOR COAUTH_RECENT INST_DEPT INST_FORMER ROLE_CONF COLLAB_GRANT REL_EDITORIAL COMPET COAUTH_OLD INST_CONSORT CONF_ATTEND SOC_MEMBER]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-protected-calls/{uuid}/compliance_overview/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-protected-calls/{uuid}/compute-affinities/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-protected-calls/{uuid}/conflict-summary/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-protected-calls/{uuid}/conflicts/

- New query param: open_for_offering_uuid
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-protected-calls/{uuid}/create-manual-assignment/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-protected-calls/{uuid}/delete_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-protected-calls/{uuid}/detach_documents/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-protected-calls/{uuid}/detect-conflicts/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-protected-calls/{uuid}/duplicate/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: has_proposals
            - Modified property: applicant_visibility_config
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/CallApplicantVisibilityConfig
                  - Properties changed
                    - New property: expose_organization_address
                    - New property: expose_organization_vat_code
                    - New property: expose_primary_gid
                    - New property: expose_uid_number
            - Modified property: description
              - MaxLength changed from null to 4096
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - New property: offering_type
                  - New property: require_purchase_order
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: discount_aggregation
                                - New property: discount_formula
                                - Deleted property: discount_rate
                                - Deleted property: discount_threshold
                                - Deleted property: discounted_price
                          - Modified property: description
                            - MaxLength changed from null to 4096
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - New property: requested_offering_components
                  - New property: requested_offering_type
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: discount_aggregation
                                - New property: discount_formula
                                - Deleted property: discount_rate
                                - Deleted property: discount_threshold
                                - Deleted property: discounted_price
                          - Modified property: description
                            - MaxLength changed from null to 4096
            - Modified property: rounds
              - Items changed
                - Properties changed
                  - Deleted property: allocation_time
                  - Deleted property: deciding_entity
                  - Deleted property: minimal_average_scoring
                  - Deleted property: minimum_number_of_reviewers
                  - Deleted property: review_strategy
            - Modified property: user_affiliations
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_assurance_levels
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_email_patterns
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_identity_sources
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_nationalities
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: user_organization_types
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-protected-calls/{uuid}/generate-assignments/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-protected-calls/{uuid}/generate-suggestions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-protected-calls/{uuid}/invite-by-email/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-protected-calls/{uuid}/list_users/

- Modified query param: role
  - Description changed from 'Role UUID or name' to 'Role UUID or name. Repeat to filter by several roles.'
  - Schema changed
    - Type changed from 'string' to 'array'
    - Format changed from 'uuid' to ''
    - Items changed
      - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-protected-calls/{uuid}/matching-configuration/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/proposal-protected-calls/{uuid}/matching-configuration/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-protected-calls/{uuid}/offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: offering_type
              - New required property: require_purchase_order
            - Properties changed
              - New property: offering_type
              - New property: require_purchase_order
              - Modified property: plan_details
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/BasePublicPlan
                    - Properties changed
                      - Modified property: components
                        - Items changed
                          - Properties changed
                            - New property: discount_aggregation
                            - New property: discount_formula
                            - Deleted property: discount_rate
                            - Deleted property: discount_threshold
                            - Deleted property: discounted_price
                      - Modified property: description
                        - MaxLength changed from null to 4096
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-protected-calls/{uuid}/offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: offering_type
            - New required property: require_purchase_order
          - Properties changed
            - New property: offering_type
            - New property: require_purchase_order
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: discount_aggregation
                          - New property: discount_formula
                          - Deleted property: discount_rate
                          - Deleted property: discount_threshold
                          - Deleted property: discounted_price
                    - Modified property: description
                      - MaxLength changed from null to 4096
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: offering_type
            - New required property: require_purchase_order
          - Properties changed
            - New property: offering_type
            - New property: require_purchase_order
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: discount_aggregation
                          - New property: discount_formula
                          - Deleted property: discount_rate
                          - Deleted property: discount_threshold
                          - Deleted property: discounted_price
                    - Modified property: description
                      - MaxLength changed from null to 4096
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: offering_type
            - New required property: require_purchase_order
          - Properties changed
            - New property: offering_type
            - New property: require_purchase_order
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: discount_aggregation
                          - New property: discount_formula
                          - Deleted property: discount_rate
                          - Deleted property: discount_threshold
                          - Deleted property: discounted_price
                    - Modified property: description
                      - MaxLength changed from null to 4096
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: offering_type
            - New required property: require_purchase_order
          - Properties changed
            - New property: offering_type
            - New property: require_purchase_order
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: discount_aggregation
                          - New property: discount_formula
                          - Deleted property: discount_rate
                          - Deleted property: discount_threshold
                          - Deleted property: discounted_price
                    - Modified property: description
                      - MaxLength changed from null to 4096
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: offering_type
            - New required property: require_purchase_order
          - Properties changed
            - New property: offering_type
            - New property: require_purchase_order
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: discount_aggregation
                          - New property: discount_formula
                          - Deleted property: discount_rate
                          - Deleted property: discount_threshold
                          - Deleted property: discounted_price
                    - Modified property: description
                      - MaxLength changed from null to 4096
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-protected-calls/{uuid}/proposals/{proposal_uuid}/compliance-answers/

- New query param: open_for_offering_uuid
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-protected-calls/{uuid}/proposed-assignments/

- New query param: open_for_offering_uuid
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-protected-calls/{uuid}/resource_templates/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: requested_offering_components
              - New property: requested_offering_type
              - Modified property: requested_offering_plan
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/BasePublicPlan
                    - Properties changed
                      - Modified property: components
                        - Items changed
                          - Properties changed
                            - New property: discount_aggregation
                            - New property: discount_formula
                            - Deleted property: discount_rate
                            - Deleted property: discount_threshold
                            - Deleted property: discounted_price
                      - Modified property: description
                        - MaxLength changed from null to 4096
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-protected-calls/{uuid}/resource_templates/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: requested_offering_components
            - New property: requested_offering_type
            - Modified property: requested_offering_plan
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: discount_aggregation
                          - New property: discount_formula
                          - Deleted property: discount_rate
                          - Deleted property: discount_threshold
                          - Deleted property: discounted_price
                    - Modified property: description
                      - MaxLength changed from null to 4096
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: requested_offering_components
            - New property: requested_offering_type
            - Modified property: requested_offering_plan
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: discount_aggregation
                          - New property: discount_formula
                          - Deleted property: discount_rate
                          - Deleted property: discount_threshold
                          - Deleted property: discounted_price
                    - Modified property: description
                      - MaxLength changed from null to 4096
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: requested_offering_components
            - New property: requested_offering_type
            - Modified property: requested_offering_plan
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: discount_aggregation
                          - New property: discount_formula
                          - Deleted property: discount_rate
                          - Deleted property: discount_threshold
                          - Deleted property: discounted_price
                    - Modified property: description
                      - MaxLength changed from null to 4096
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: requested_offering_components
            - New property: requested_offering_type
            - Modified property: requested_offering_plan
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: discount_aggregation
                          - New property: discount_formula
                          - Deleted property: discount_rate
                          - Deleted property: discount_threshold
                          - Deleted property: discounted_price
                    - Modified property: description
                      - MaxLength changed from null to 4096
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: requested_offering_components
            - New property: requested_offering_type
            - Modified property: requested_offering_plan
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: discount_aggregation
                          - New property: discount_formula
                          - Deleted property: discount_rate
                          - Deleted property: discount_threshold
                          - Deleted property: discounted_price
                    - Modified property: description
                      - MaxLength changed from null to 4096
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-protected-calls/{uuid}/review_proposal_compliance/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-protected-calls/{uuid}/reviewer-pool/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-protected-calls/{uuid}/reviewer-pool/

- New query param: open_for_offering_uuid
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-protected-calls/{uuid}/rounds-bulk-set/

- New query param: open_for_offering_uuid
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: allocation_time
          - Deleted property: deciding_entity
          - Deleted property: minimal_average_scoring
          - Deleted property: minimum_number_of_reviewers
          - Deleted property: review_strategy
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Deleted property: allocation_time
              - Deleted property: deciding_entity
              - Deleted property: minimal_average_scoring
              - Deleted property: minimum_number_of_reviewers
              - Deleted property: review_strategy
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-protected-calls/{uuid}/rounds/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Deleted property: allocation_time
              - Deleted property: deciding_entity
              - Deleted property: minimal_average_scoring
              - Deleted property: minimum_number_of_reviewers
              - Deleted property: review_strategy
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-protected-calls/{uuid}/rounds/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: allocation_time
          - Deleted property: deciding_entity
          - Deleted property: minimal_average_scoring
          - Deleted property: minimum_number_of_reviewers
          - Deleted property: review_strategy
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: allocation_time
            - Deleted property: deciding_entity
            - Deleted property: minimal_average_scoring
            - Deleted property: minimum_number_of_reviewers
            - Deleted property: review_strategy
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: allocation_time
            - Deleted property: deciding_entity
            - Deleted property: minimal_average_scoring
            - Deleted property: minimum_number_of_reviewers
            - Deleted property: review_strategy
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: allocation_time
            - Deleted property: deciding_entity
            - Deleted property: minimal_average_scoring
            - Deleted property: minimum_number_of_reviewers
            - Deleted property: review_strategy
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: allocation_time
          - Deleted property: deciding_entity
          - Deleted property: minimal_average_scoring
          - Deleted property: minimum_number_of_reviewers
          - Deleted property: review_strategy
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: allocation_time
            - Deleted property: deciding_entity
            - Deleted property: minimal_average_scoring
            - Deleted property: minimum_number_of_reviewers
            - Deleted property: review_strategy
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: allocation_time
          - Deleted property: deciding_entity
          - Deleted property: minimal_average_scoring
          - Deleted property: minimum_number_of_reviewers
          - Deleted property: review_strategy
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: allocation_time
            - Deleted property: deciding_entity
            - Deleted property: minimal_average_scoring
            - Deleted property: minimum_number_of_reviewers
            - Deleted property: review_strategy
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/close/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: applicant_visibility_config
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/CallApplicantVisibilityConfigRequest
                - Properties changed
                  - New property: expose_organization_address
                  - New property: expose_organization_vat_code
                  - New property: expose_primary_gid
                  - New property: expose_uid_number
          - Modified property: description
            - MaxLength changed from null to 4096
          - Modified property: user_affiliations
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_assurance_levels
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_email_patterns
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_identity_sources
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_nationalities
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
          - Modified property: user_organization_types
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-protected-calls/{uuid}/send-all-assignments/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-protected-calls/{uuid}/send-invitations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-protected-calls/{uuid}/suggestions/

- New query param: open_for_offering_uuid
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-protected-calls/{uuid}/update_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-protected-calls/{uuid}/workflow_steps/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: is_mandatory
            - Properties changed
              - New property: allocation_time
              - New property: checklist_required
              - New property: is_mandatory
              - Modified property: min_score_threshold
                - Description changed from 'Minimum average score to pass this step.' to 'Minimum average score required before this step can complete (a completion gate; it does not auto-reject lower scores).'
              - Modified property: transition_mode
                - Description changed from 'How this step advances to the next.' to 'How this step advances once a human completes it. 'Automatic' advances to the next step immediately; 'Manual' waits for a separate advance action. Neither auto-decides from review scores.'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-protected-calls/{uuid}/workflow_steps/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: allocation_time
          - New property: checklist_required
          - Modified property: min_score_threshold
            - Description changed from 'Minimum average score to pass this step.' to 'Minimum average score required before this step can complete (a completion gate; it does not auto-reject lower scores).'
          - Modified property: transition_mode
            - Description changed from 'How this step advances to the next.' to 'How this step advances once a human completes it. 'Automatic' advances to the next step immediately; 'Manual' waits for a separate advance action. Neither auto-decides from review scores.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: is_mandatory
          - Properties changed
            - New property: allocation_time
            - New property: checklist_required
            - New property: is_mandatory
            - Modified property: min_score_threshold
              - Description changed from 'Minimum average score to pass this step.' to 'Minimum average score required before this step can complete (a completion gate; it does not auto-reject lower scores).'
            - Modified property: transition_mode
              - Description changed from 'How this step advances to the next.' to 'How this step advances once a human completes it. 'Automatic' advances to the next step immediately; 'Manual' waits for a separate advance action. Neither auto-decides from review scores.'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/proposal-protected-calls/{uuid}/workflow_steps/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: is_mandatory
          - Properties changed
            - New property: allocation_time
            - New property: checklist_required
            - New property: is_mandatory
            - Modified property: min_score_threshold
              - Description changed from 'Minimum average score to pass this step.' to 'Minimum average score required before this step can complete (a completion gate; it does not auto-reject lower scores).'
            - Modified property: transition_mode
              - Description changed from 'How this step advances to the next.' to 'How this step advances once a human completes it. 'Automatic' advances to the next step immediately; 'Manual' waits for a separate advance action. Neither auto-decides from review scores.'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-protected-calls/{uuid}/workflow_steps/{obj_uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: is_mandatory
          - Properties changed
            - New property: allocation_time
            - New property: checklist_required
            - New property: is_mandatory
            - Modified property: min_score_threshold
              - Description changed from 'Minimum average score to pass this step.' to 'Minimum average score required before this step can complete (a completion gate; it does not auto-reject lower scores).'
            - Modified property: transition_mode
              - Description changed from 'How this step advances to the next.' to 'How this step advances once a human completes it. 'Automatic' advances to the next step immediately; 'Manual' waits for a separate advance action. Neither auto-decides from review scores.'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/proposal-protected-calls/{uuid}/workflow_steps/{obj_uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: allocation_time
          - New property: checklist_required
          - Modified property: min_score_threshold
            - Description changed from 'Minimum average score to pass this step.' to 'Minimum average score required before this step can complete (a completion gate; it does not auto-reject lower scores).'
          - Modified property: transition_mode
            - Description changed from 'How this step advances to the next.' to 'How this step advances once a human completes it. 'Automatic' advances to the next step immediately; 'Manual' waits for a separate advance action. Neither auto-decides from review scores.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: is_mandatory
          - Properties changed
            - New property: allocation_time
            - New property: checklist_required
            - New property: is_mandatory
            - Modified property: min_score_threshold
              - Description changed from 'Minimum average score to pass this step.' to 'Minimum average score required before this step can complete (a completion gate; it does not auto-reject lower scores).'
            - Modified property: transition_mode
              - Description changed from 'How this step advances to the next.' to 'How this step advances once a human completes it. 'Automatic' advances to the next step immediately; 'Manual' waits for a separate advance action. Neither auto-decides from review scores.'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/proposal-protected-calls/{uuid}/workflow_steps/{obj_uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: allocation_time
          - New property: checklist_required
          - Modified property: min_score_threshold
            - Description changed from 'Minimum average score to pass this step.' to 'Minimum average score required before this step can complete (a completion gate; it does not auto-reject lower scores).'
          - Modified property: transition_mode
            - Description changed from 'How this step advances to the next.' to 'How this step advances once a human completes it. 'Automatic' advances to the next step immediately; 'Manual' waits for a separate advance action. Neither auto-decides from review scores.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: is_mandatory
          - Properties changed
            - New property: allocation_time
            - New property: checklist_required
            - New property: is_mandatory
            - Modified property: min_score_threshold
              - Description changed from 'Minimum average score to pass this step.' to 'Minimum average score required before this step can complete (a completion gate; it does not auto-reject lower scores).'
            - Modified property: transition_mode
              - Description changed from 'How this step advances to the next.' to 'How this step advances once a human completes it. 'Automatic' advances to the next step immediately; 'Manual' waits for a separate advance action. Neither auto-decides from review scores.'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-public-calls/

- New query param: open_for_offering_uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: description
                - MaxLength changed from null to 4096
              - Modified property: offerings
                - Items changed
                  - Properties changed
                    - New property: offering_type
                    - New property: require_purchase_order
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: components
                              - Items changed
                                - Properties changed
                                  - New property: discount_aggregation
                                  - New property: discount_formula
                                  - Deleted property: discount_rate
                                  - Deleted property: discount_threshold
                                  - Deleted property: discounted_price
                            - Modified property: description
                              - MaxLength changed from null to 4096
              - Modified property: resource_templates
                - Items changed
                  - Properties changed
                    - New property: requested_offering_components
                    - New property: requested_offering_type
                    - Modified property: requested_offering_plan
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: components
                              - Items changed
                                - Properties changed
                                  - New property: discount_aggregation
                                  - New property: discount_formula
                                  - Deleted property: discount_rate
                                  - Deleted property: discount_threshold
                                  - Deleted property: discounted_price
                            - Modified property: description
                              - MaxLength changed from null to 4096
              - Modified property: rounds
                - Items changed
                  - Properties changed
                    - Deleted property: allocation_time
                    - Deleted property: deciding_entity
                    - Deleted property: minimal_average_scoring
                    - Deleted property: minimum_number_of_reviewers
                    - Deleted property: review_strategy
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/proposal-public-calls/

- New query param: open_for_offering_uuid
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-public-calls/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: description
              - MaxLength changed from null to 4096
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - New property: offering_type
                  - New property: require_purchase_order
                  - Modified property: plan_details
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: discount_aggregation
                                - New property: discount_formula
                                - Deleted property: discount_rate
                                - Deleted property: discount_threshold
                                - Deleted property: discounted_price
                          - Modified property: description
                            - MaxLength changed from null to 4096
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - New property: requested_offering_components
                  - New property: requested_offering_type
                  - Modified property: requested_offering_plan
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/BasePublicPlan
                        - Properties changed
                          - Modified property: components
                            - Items changed
                              - Properties changed
                                - New property: discount_aggregation
                                - New property: discount_formula
                                - Deleted property: discount_rate
                                - Deleted property: discount_threshold
                                - Deleted property: discounted_price
                          - Modified property: description
                            - MaxLength changed from null to 4096
            - Modified property: rounds
              - Items changed
                - Properties changed
                  - Deleted property: allocation_time
                  - Deleted property: deciding_entity
                  - Deleted property: minimal_average_scoring
                  - Deleted property: minimum_number_of_reviewers
                  - Deleted property: review_strategy
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-public-calls/{uuid}/check_eligibility/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-requested-offerings/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: offering_type
            - Properties changed
              - New property: offering_type
              - New property: require_purchase_order
              - Modified property: plan_details
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/BasePublicPlan
                    - Properties changed
                      - Modified property: components
                        - Items changed
                          - Properties changed
                            - New property: discount_aggregation
                            - New property: discount_formula
                            - Deleted property: discount_rate
                            - Deleted property: discount_threshold
                            - Deleted property: discounted_price
                      - Modified property: description
                        - MaxLength changed from null to 4096
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/proposal-requested-offerings/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-requested-offerings/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: offering_type
          - Properties changed
            - New property: offering_type
            - New property: require_purchase_order
            - Modified property: plan_details
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/BasePublicPlan
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: discount_aggregation
                          - New property: discount_formula
                          - Deleted property: discount_rate
                          - Deleted property: discount_threshold
                          - Deleted property: discounted_price
                    - Modified property: description
                      - MaxLength changed from null to 4096
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-requested-offerings/{uuid}/accept/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-requested-offerings/{uuid}/cancel/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-requested-resources/

- New query param: proposal_state
- New query param: query
- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-call__name -proposal__state -resource__state call__name proposal__state resource__state]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: attachment
              - New required property: has_purchase_order
              - New required property: purchase_order_required
            - Properties changed
              - New property: attachment
              - New property: has_purchase_order
              - New property: purchase_order_reference
              - New property: purchase_order_required
              - Modified property: requested_offering
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/NestedRequestedOffering
                    - Properties changed
                      - New property: offering_type
                      - New property: require_purchase_order
                      - Modified property: plan_details
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/BasePublicPlan
                            - Properties changed
                              - Modified property: components
                                - Items changed
                                  - Properties changed
                                    - New property: discount_aggregation
                                    - New property: discount_formula
                                    - Deleted property: discount_rate
                                    - Deleted property: discount_threshold
                                    - Deleted property: discounted_price
                              - Modified property: description
                                - MaxLength changed from null to 4096
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/proposal-requested-resources/

- New query param: proposal_state
- New query param: query
- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-call__name -proposal__state -resource__state call__name proposal__state resource__state]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-requested-resources/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: attachment
            - New required property: has_purchase_order
            - New required property: purchase_order_required
          - Properties changed
            - New property: attachment
            - New property: has_purchase_order
            - New property: purchase_order_reference
            - New property: purchase_order_required
            - Modified property: requested_offering
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/NestedRequestedOffering
                  - Properties changed
                    - New property: offering_type
                    - New property: require_purchase_order
                    - Modified property: plan_details
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/BasePublicPlan
                          - Properties changed
                            - Modified property: components
                              - Items changed
                                - Properties changed
                                  - New property: discount_aggregation
                                  - New property: discount_formula
                                  - Deleted property: discount_rate
                                  - Deleted property: discount_threshold
                                  - Deleted property: discounted_price
                            - Modified property: description
                              - MaxLength changed from null to 4096
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-reviews/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: coi_confirmation_required
              - New required property: coi_confirmed
              - New required property: coi_confirmed_at
            - Properties changed
              - New property: coi_confirmation_required
              - New property: coi_confirmed
              - New property: coi_confirmed_at
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/proposal-reviews/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-reviews/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: coi_confirmation_required
            - New required property: coi_confirmed
            - New required property: coi_confirmed_at
          - Properties changed
            - New property: coi_confirmation_required
            - New property: coi_confirmed
            - New property: coi_confirmed_at
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/proposal-reviews/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/proposal-reviews/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: coi_confirmation_required
            - New required property: coi_confirmed
            - New required property: coi_confirmed_at
          - Properties changed
            - New property: coi_confirmation_required
            - New property: coi_confirmed
            - New property: coi_confirmed_at
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/proposal-reviews/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: coi_confirmation_required
            - New required property: coi_confirmed
            - New required property: coi_confirmed_at
          - Properties changed
            - New property: coi_confirmation_required
            - New property: coi_confirmed
            - New property: coi_confirmed_at
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/proposal-reviews/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: coi_confirmation_required
            - New required property: coi_confirmed
            - New required property: coi_confirmed_at
          - Properties changed
            - New property: coi_confirmation_required
            - New property: coi_confirmed
            - New property: coi_confirmed_at
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-reviews/{uuid}/reject/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/proposal-reviews/{uuid}/submit/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: coi_confirmed
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/provider-invoice-items/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/provider-invoice-items/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/provider-invoice-items/{id}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/public-maintenance-announcements/

- New query param: timing_bucket
- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-overrun_minutes -start_delta_minutes overrun_minutes start_delta_minutes]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/public-maintenance-announcements/

- New query param: timing_bucket
- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-overrun_minutes -start_delta_minutes overrun_minutes start_delta_minutes]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/public-maintenance-announcements/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/query/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rabbitmq-overview/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rabbitmq-stats/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rabbitmq-stats/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rabbitmq-user-stats/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rabbitmq-vhost-stats/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-apps/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/rancher-apps/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-apps/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/rancher-apps/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-apps/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/rancher-apps/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/rancher-apps/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-apps/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-apps/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-apps/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-apps/{uuid}/unlink/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-catalogs/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/rancher-catalogs/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-catalogs/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/rancher-catalogs/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-catalogs/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/rancher-catalogs/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/rancher-catalogs/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-catalogs/{uuid}/refresh/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-cluster-security-groups/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/rancher-cluster-security-groups/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-cluster-security-groups/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/rancher-cluster-security-groups/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/rancher-cluster-security-groups/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-cluster-templates/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/rancher-cluster-templates/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-cluster-templates/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-clusters/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/rancher-clusters/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-clusters/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/rancher-clusters/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/rancher-clusters/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-clusters/{uuid}/create_management_security_group/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-clusters/{uuid}/import_yaml/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-clusters/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-clusters/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-clusters/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-clusters/{uuid}/unlink/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-hpas/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/rancher-hpas/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-hpas/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/rancher-hpas/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-hpas/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/rancher-hpas/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/rancher-hpas/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-hpas/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-hpas/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-hpas/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-hpas/{uuid}/unlink/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-hpas/{uuid}/yaml/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/rancher-hpas/{uuid}/yaml/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-ingresses/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/rancher-ingresses/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-ingresses/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/rancher-ingresses/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-ingresses/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/rancher-ingresses/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/rancher-ingresses/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-ingresses/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-ingresses/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-ingresses/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-ingresses/{uuid}/unlink/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-ingresses/{uuid}/yaml/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/rancher-ingresses/{uuid}/yaml/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-namespaces/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/rancher-namespaces/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-namespaces/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-nodes/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/rancher-nodes/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-nodes/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/rancher-nodes/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-nodes/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-nodes/{uuid}/console/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-nodes/{uuid}/console_log/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-nodes/{uuid}/link_openstack/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-nodes/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-nodes/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-nodes/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-nodes/{uuid}/unlink/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-nodes/{uuid}/unlink_openstack/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-projects/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/rancher-projects/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-projects/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-projects/{uuid}/secrets/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-role-templates/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/rancher-role-templates/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-role-templates/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-services/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/rancher-services/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-services/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/rancher-services/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-services/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/rancher-services/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/rancher-services/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-services/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-services/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-services/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-services/{uuid}/unlink/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-services/{uuid}/yaml/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/rancher-services/{uuid}/yaml/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-template-versions/{template_uuid}/{version}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-templates/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/rancher-templates/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-templates/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-users/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/rancher-users/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-users/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-workloads/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/rancher-workloads/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-workloads/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/rancher-workloads/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-workloads/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/rancher-workloads/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/rancher-workloads/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/rancher-workloads/{uuid}/redeploy/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/rancher-workloads/{uuid}/yaml/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/rancher-workloads/{uuid}/yaml/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/remote-eduteams/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/remote-waldur-api/cancel_termination/{uuid}

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/remote-waldur-api/import_offering/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/remote-waldur-api/pull_offering_details/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/remote-waldur-api/pull_offering_orders/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/remote-waldur-api/pull_offering_resources/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/remote-waldur-api/pull_offering_robot_accounts/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/remote-waldur-api/pull_offering_usage/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/remote-waldur-api/pull_offering_users/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/remote-waldur-api/pull_order/{uuid}

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/remote-waldur-api/pull_resource_robot_accounts/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/remote-waldur-api/push_project_data/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/remote-waldur-api/remote_categories/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Deleted property: default_tenant_category
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/remote-waldur-api/remote_customers/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/remote-waldur-api/remote_resource_order_status/{resource_uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/remote-waldur-api/remote_resource_status/{resource_uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/remote-waldur-api/remote_resource_team_status/{resource_uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/remote-waldur-api/shared_offerings/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/remote-waldur-api/sync_resource/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/remote-waldur-api/sync_resource_project_permissions/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/reviewer-bids/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/reviewer-bids/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/reviewer-bids/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/reviewer-bids/bulk-submit/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/reviewer-bids/my-bids/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/reviewer-bids/my-bids/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/reviewer-bids/submit/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/reviewer-bids/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/reviewer-bids/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/reviewer-bids/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/reviewer-bids/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/reviewer-invitations/{token}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: coi_configuration
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/InvitationCOIConfiguration
                  - Properties changed
                    - Modified property: disclosure_only_types
                      - Items changed
                        - New enum values: [INST_SAME FIN_DIRECT REL_FAMILY ROLE_NAMED COLLAB_ACTIVE REL_MENTOR REL_SUPERVISOR COAUTH_RECENT INST_DEPT INST_FORMER ROLE_CONF COLLAB_GRANT REL_EDITORIAL COMPET COAUTH_OLD INST_CONSORT CONF_ATTEND SOC_MEMBER]
                    - Modified property: management_allowed_types
                      - Items changed
                        - New enum values: [INST_SAME FIN_DIRECT REL_FAMILY ROLE_NAMED COLLAB_ACTIVE REL_MENTOR REL_SUPERVISOR COAUTH_RECENT INST_DEPT INST_FORMER ROLE_CONF COLLAB_GRANT REL_EDITORIAL COMPET COAUTH_OLD INST_CONSORT CONF_ATTEND SOC_MEMBER]
                    - Modified property: recusal_required_types
                      - Items changed
                        - New enum values: [INST_SAME FIN_DIRECT REL_FAMILY ROLE_NAMED COLLAB_ACTIVE REL_MENTOR REL_SUPERVISOR COAUTH_RECENT INST_DEPT INST_FORMER ROLE_CONF COLLAB_GRANT REL_EDITORIAL COMPET COAUTH_OLD INST_CONSORT CONF_ATTEND SOC_MEMBER]
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/reviewer-invitations/{token}/accept/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/reviewer-invitations/{token}/decline/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/reviewer-profiles/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: alternative_names
                - Type changed from 'object' to 'array'
                - AdditionalProperties changed from true to null
                - Items changed
                  - Schema added
              - Modified property: publications
                - Items changed
                  - Properties changed
                    - Modified property: coauthors
                      - Type changed from 'object' to 'array'
                      - AdditionalProperties changed from true to null
                      - Items changed
                        - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/reviewer-profiles/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/reviewer-profiles/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: alternative_names
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: alternative_names
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: publications
              - Items changed
                - Properties changed
                  - Modified property: coauthors
                    - Type changed from 'object' to 'array'
                    - AdditionalProperties changed from true to null
                    - Items changed
                      - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/reviewer-profiles/me/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: alternative_names
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: publications
              - Items changed
                - Properties changed
                  - Modified property: coauthors
                    - Type changed from 'object' to 'array'
                    - AdditionalProperties changed from true to null
                    - Items changed
                      - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/reviewer-profiles/me/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/reviewer-profiles/me/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: alternative_names
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: alternative_names
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: publications
              - Items changed
                - Properties changed
                  - Modified property: coauthors
                    - Type changed from 'object' to 'array'
                    - AdditionalProperties changed from true to null
                    - Items changed
                      - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/reviewer-profiles/me/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: alternative_names
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: alternative_names
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: publications
              - Items changed
                - Properties changed
                  - Modified property: coauthors
                    - Type changed from 'object' to 'array'
                    - AdditionalProperties changed from true to null
                    - Items changed
                      - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/reviewer-profiles/publish/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: alternative_names
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/reviewer-profiles/unpublish/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: alternative_names
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/reviewer-profiles/{reviewer_profile_uuid}/affiliations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/reviewer-profiles/{reviewer_profile_uuid}/affiliations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/reviewer-profiles/{reviewer_profile_uuid}/affiliations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/reviewer-profiles/{reviewer_profile_uuid}/affiliations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/reviewer-profiles/{reviewer_profile_uuid}/affiliations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/reviewer-profiles/{reviewer_profile_uuid}/affiliations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/reviewer-profiles/{reviewer_profile_uuid}/expertise/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/reviewer-profiles/{reviewer_profile_uuid}/expertise/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/reviewer-profiles/{reviewer_profile_uuid}/expertise/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/reviewer-profiles/{reviewer_profile_uuid}/expertise/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/reviewer-profiles/{reviewer_profile_uuid}/expertise/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/reviewer-profiles/{reviewer_profile_uuid}/expertise/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/reviewer-profiles/{reviewer_profile_uuid}/publications/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: coauthors
                - Type changed from 'object' to 'array'
                - AdditionalProperties changed from true to null
                - Items changed
                  - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/reviewer-profiles/{reviewer_profile_uuid}/publications/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: coauthors
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: coauthors
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/reviewer-profiles/{reviewer_profile_uuid}/publications/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/reviewer-profiles/{reviewer_profile_uuid}/publications/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: coauthors
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/reviewer-profiles/{reviewer_profile_uuid}/publications/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: coauthors
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: coauthors
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/reviewer-profiles/{reviewer_profile_uuid}/publications/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: coauthors
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: coauthors
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/reviewer-profiles/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/reviewer-profiles/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: alternative_names
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: publications
              - Items changed
                - Properties changed
                  - Modified property: coauthors
                    - Type changed from 'object' to 'array'
                    - AdditionalProperties changed from true to null
                    - Items changed
                      - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/reviewer-profiles/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: alternative_names
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: alternative_names
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: publications
              - Items changed
                - Properties changed
                  - Modified property: coauthors
                    - Type changed from 'object' to 'array'
                    - AdditionalProperties changed from true to null
                    - Items changed
                      - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/reviewer-profiles/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: alternative_names
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: alternative_names
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: publications
              - Items changed
                - Properties changed
                  - Modified property: coauthors
                    - Type changed from 'object' to 'array'
                    - AdditionalProperties changed from true to null
                    - Items changed
                      - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/reviewer-profiles/{uuid}/connect-orcid/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/reviewer-profiles/{uuid}/connect-orcid/callback/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: alternative_names
              - Type changed from 'object' to 'array'
              - AdditionalProperties changed from true to null
              - Items changed
                - Schema added
            - Modified property: publications
              - Items changed
                - Properties changed
                  - Modified property: coauthors
                    - Type changed from 'object' to 'array'
                    - AdditionalProperties changed from true to null
                    - Items changed
                      - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/reviewer-profiles/{uuid}/disconnect-orcid/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: alternative_names
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/reviewer-profiles/{uuid}/import-publications/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/reviewer-profiles/{uuid}/sync-orcid/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: alternative_names
            - Type changed from 'object' to 'array'
            - AdditionalProperties changed from true to null
            - Items changed
              - Schema added
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/reviewer-suggestions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/reviewer-suggestions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/reviewer-suggestions/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/reviewer-suggestions/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/reviewer-suggestions/{uuid}/confirm/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/reviewer-suggestions/{uuid}/reject/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/role-availabilities/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/role-availabilities/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/role-availabilities/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/role-availabilities/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/roles/

- New query param: available_for_customer
- New query param: content_type
- New query param: include_concealed
- New query param: is_system_role
- New query param: o
- New query param: query
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_name customer_uuid description_km template_name template_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: customer_name
              - New property: customer_uuid
              - New property: description_km
              - New property: template_name
              - New property: template_uuid
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/roles/

- New query param: available_for_customer
- New query param: content_type
- New query param: include_concealed
- New query param: is_system_role
- New query param: o
- New query param: query
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/roles/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: description_km
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_name
            - New property: customer_uuid
            - New property: description_km
            - New property: template_name
            - New property: template_uuid
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/roles/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/roles/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [customer_name customer_uuid description_km template_name template_uuid]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_name
            - New property: customer_uuid
            - New property: description_km
            - New property: template_name
            - New property: template_uuid
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/roles/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: description_km
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_name
            - New property: customer_uuid
            - New property: description_km
            - New property: template_name
            - New property: template_uuid
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/roles/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: description_km
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: customer_name
            - New property: customer_uuid
            - New property: description_km
            - New property: template_name
            - New property: template_uuid
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/roles/{uuid}/disable/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/roles/{uuid}/enable/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/roles/{uuid}/update_descriptions/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: description_km
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: description_km
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/science-domains/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/science-domains/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/science-domains/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/science-domains/load_preset/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/science-domains/presets/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/science-domains/presets/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/science-domains/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/science-domains/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/science-domains/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/science-domains/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/science-sub-domains/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/science-sub-domains/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/science-sub-domains/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/science-sub-domains/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/science-sub-domains/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/science-sub-domains/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/science-sub-domains/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/service-settings/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/service-settings/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/service-settings/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/slurm-allocation-user-usage/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/slurm-allocation-user-usage/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/slurm-allocation-user-usage/{id}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/slurm-allocations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/slurm-allocations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/slurm-allocations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/slurm-allocations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/slurm-allocations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/slurm-allocations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/slurm-allocations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/slurm-allocations/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/slurm-allocations/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/slurm-allocations/{uuid}/set_limits/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/slurm-allocations/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/slurm-allocations/{uuid}/unlink/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/slurm-associations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/slurm-associations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/slurm-associations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/slurm-jobs/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/slurm-jobs/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/slurm-jobs/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/slurm-jobs/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/slurm-jobs/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/slurm-jobs/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/slurm-jobs/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/slurm-jobs/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/slurm-jobs/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/slurm-jobs/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/slurm-jobs/{uuid}/unlink/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/stats/celery/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/stats/database/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/stats/query/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/stats/table-growth/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/stats/table-growth/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/support-attachments/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/support-attachments/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/support-attachments/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/support-attachments/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/support-attachments/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/support-comments/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/support-comments/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/support-comments/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/support-comments/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/support-comments/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/support-comments/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/support-feedback-average-report/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/support-feedback-report/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/support-feedbacks/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/support-feedbacks/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/support-feedbacks/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/support-feedbacks/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/support-issue-statuses/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/support-issue-statuses/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/support-issue-statuses/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/support-issue-statuses/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/support-issue-statuses/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/support-issue-statuses/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/support-issue-statuses/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/support-issues/

- New query param: is_escalated
- New query param: is_parent
- New query param: is_routed
- New query param: provider_uuid
- New query param: sla_breached
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: escalated_at
              - New required property: escalation_reason
              - New required property: first_response_at
              - New required property: first_response_deadline
              - New required property: is_escalated
              - New required property: is_routed
              - New required property: parent_issue
              - New required property: provider_helpdesk
              - New required property: provider_ticket_info
              - New required property: resolution_deadline
              - New required property: sla_breached
              - New required property: sla_status
            - Properties changed
              - New property: escalated_at
              - New property: escalation_reason
              - New property: first_response_at
              - New property: first_response_deadline
              - New property: is_escalated
              - New property: is_routed
              - New property: offering
              - New property: parent_issue
              - New property: provider_helpdesk
              - New property: provider_ticket_info
              - New property: resolution_deadline
              - New property: sla_breached
              - New property: sla_status
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/support-issues/

- New query param: is_escalated
- New query param: is_parent
- New query param: is_routed
- New query param: provider_uuid
- New query param: sla_breached
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/support-issues/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: offering
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: escalated_at
            - New required property: escalation_reason
            - New required property: first_response_at
            - New required property: first_response_deadline
            - New required property: is_escalated
            - New required property: is_routed
            - New required property: parent_issue
            - New required property: provider_helpdesk
            - New required property: provider_ticket_info
            - New required property: resolution_deadline
            - New required property: sla_breached
            - New required property: sla_status
          - Properties changed
            - New property: escalated_at
            - New property: escalation_reason
            - New property: first_response_at
            - New property: first_response_deadline
            - New property: is_escalated
            - New property: is_routed
            - New property: offering
            - New property: parent_issue
            - New property: provider_helpdesk
            - New property: provider_ticket_info
            - New property: resolution_deadline
            - New property: sla_breached
            - New property: sla_status
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/support-issues/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/support-issues/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: escalated_at
            - New required property: escalation_reason
            - New required property: first_response_at
            - New required property: first_response_deadline
            - New required property: is_escalated
            - New required property: is_routed
            - New required property: parent_issue
            - New required property: provider_helpdesk
            - New required property: provider_ticket_info
            - New required property: resolution_deadline
            - New required property: sla_breached
            - New required property: sla_status
          - Properties changed
            - New property: escalated_at
            - New property: escalation_reason
            - New property: first_response_at
            - New property: first_response_deadline
            - New property: is_escalated
            - New property: is_routed
            - New property: offering
            - New property: parent_issue
            - New property: provider_helpdesk
            - New property: provider_ticket_info
            - New property: resolution_deadline
            - New property: sla_breached
            - New property: sla_status
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/support-issues/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: offering
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: escalated_at
            - New required property: escalation_reason
            - New required property: first_response_at
            - New required property: first_response_deadline
            - New required property: is_escalated
            - New required property: is_routed
            - New required property: parent_issue
            - New required property: provider_helpdesk
            - New required property: provider_ticket_info
            - New required property: resolution_deadline
            - New required property: sla_breached
            - New required property: sla_status
          - Properties changed
            - New property: escalated_at
            - New property: escalation_reason
            - New property: first_response_at
            - New property: first_response_deadline
            - New property: is_escalated
            - New property: is_routed
            - New property: offering
            - New property: parent_issue
            - New property: provider_helpdesk
            - New property: provider_ticket_info
            - New property: resolution_deadline
            - New property: sla_breached
            - New property: sla_status
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/support-issues/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: offering
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: escalated_at
            - New required property: escalation_reason
            - New required property: first_response_at
            - New required property: first_response_deadline
            - New required property: is_escalated
            - New required property: is_routed
            - New required property: parent_issue
            - New required property: provider_helpdesk
            - New required property: provider_ticket_info
            - New required property: resolution_deadline
            - New required property: sla_breached
            - New required property: sla_status
          - Properties changed
            - New property: escalated_at
            - New property: escalation_reason
            - New property: first_response_at
            - New property: first_response_deadline
            - New property: is_escalated
            - New property: is_routed
            - New property: offering
            - New property: parent_issue
            - New property: provider_helpdesk
            - New property: provider_ticket_info
            - New property: resolution_deadline
            - New property: sla_breached
            - New property: sla_status
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/support-issues/{uuid}/comment/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/support-issues/{uuid}/sync/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/support-priorities/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/support-priorities/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/support-priorities/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/support-request-types-admin/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/support-request-types-admin/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/support-request-types-admin/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/support-request-types-admin/reorder/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/support-request-types-admin/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/support-request-types-admin/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/support-request-types-admin/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/support-request-types-admin/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/support-request-types-admin/{uuid}/activate/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/support-request-types-admin/{uuid}/deactivate/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/support-request-types/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/support-request-types/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/support-request-types/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/support-statistics/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/support-templates/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/support-templates/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/support-templates/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/support-templates/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/support-templates/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/support-templates/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/support-templates/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/support-templates/{uuid}/create_attachments/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/support-templates/{uuid}/delete_attachments/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/support-users/

- New query param: backend_name
- New query param: is_active
- New query param: o
- New query param: query
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: assigned_issues_count
              - New required property: attachments_count
              - New required property: comments_count
              - New required property: reported_issues_count
              - New required property: user_email
              - New required property: user_full_name
            - Properties changed
              - New property: assigned_issues_count
              - New property: attachments_count
              - New property: comments_count
              - New property: is_active
              - New property: reported_issues_count
              - New property: user_email
              - New property: user_full_name
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/support-users/

- New query param: backend_name
- New query param: is_active
- New query param: o
- New query param: query
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/support-users/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: assigned_issues_count
            - New required property: attachments_count
            - New required property: comments_count
            - New required property: reported_issues_count
            - New required property: user_email
            - New required property: user_full_name
          - Properties changed
            - New property: assigned_issues_count
            - New property: attachments_count
            - New property: comments_count
            - New property: is_active
            - New property: reported_issues_count
            - New property: user_email
            - New property: user_full_name
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/support/settings/atlassian/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/support/settings/atlassian/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/support/settings/atlassian/current_settings/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/support/settings/atlassian/discover_custom_fields/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/support/settings/atlassian/discover_priorities/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/support/settings/atlassian/discover_projects/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/support/settings/atlassian/discover_request_types/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/support/settings/atlassian/preview_settings/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/support/settings/atlassian/save_settings/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/support/settings/atlassian/validate_credentials/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/support/settings/atlassian/{id}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/support/settings/atlassian/{id}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/support/settings/atlassian/{id}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/support/settings/atlassian/{id}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/sync-issues/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/sync-issues/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/system-logs/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/system-logs/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/system-logs/instances/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/system-logs/instances/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/system-logs/stats/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/system-logs/stats/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/system-logs/{id}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/user-action-executions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/user-action-executions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/user-action-executions/{id}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/user-action-providers/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/user-action-providers/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/user-action-providers/{id}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/user-actions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/user-actions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/user-actions/bulk_silence/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/user-actions/summary/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/user-actions/summary/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/user-actions/update_actions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/user-actions/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/user-actions/{uuid}/execute_action/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/user-actions/{uuid}/silence/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/user-actions/{uuid}/unsilence/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/user-agreements/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/user-agreements/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/user-agreements/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/user-agreements/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/user-agreements/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/user-agreements/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/user-agreements/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/user-group-invitations/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: created_by_image
                - Nullable changed from false to true
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/user-group-invitations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/user-group-invitations/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: created_by_image
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/user-group-invitations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/user-group-invitations/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: created_by_image
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/user-group-invitations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/user-group-invitations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/user-group-invitations/{uuid}/cancel/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/user-group-invitations/{uuid}/projects/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/user-group-invitations/{uuid}/submit_request/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: scope_type
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/user-invitations/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: created_by_image
                - Nullable changed from false to true
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/user-invitations/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/user-invitations/

- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: created_by_image
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/user-invitations/approve/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/user-invitations/check-duplicates/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/user-invitations/reject/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/user-invitations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/user-invitations/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: created_by_image
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/user-invitations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/user-invitations/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/user-invitations/{uuid}/accept/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/user-invitations/{uuid}/cancel/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/user-invitations/{uuid}/check/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/user-invitations/{uuid}/delete/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/user-invitations/{uuid}/details/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: created_by_image
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/user-invitations/{uuid}/send/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/user-permission-requests/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: reviewed_by_full_name
                - Nullable changed from false to true
              - Modified property: reviewed_by_username
                - Nullable changed from false to true
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/user-permission-requests/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/user-permission-requests/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/user-permission-requests/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: reviewed_by_full_name
              - Nullable changed from false to true
            - Modified property: reviewed_by_username
              - Nullable changed from false to true
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/user-permission-requests/{uuid}/approve/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/user-permission-requests/{uuid}/cancel_request/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/user-permission-requests/{uuid}/reject/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/user-permissions/

- Description changed from 'Get a list of all permissions for the current user. Staff and support users can view all user permissions. The list can be filtered by user, scope, role, etc.' to 'Get a list of all permissions for the current user. Staff and support users can view all user permissions. The list can be filtered by user, scope, role, etc. By default only active grants are returned; staff and support can pass show_inactive=true to include revoked grants (the full history).'
- New query param: customer_uuid
- New query param: is_active
- New query param: show_inactive
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: is_active
              - New property: revoke_reason
              - New property: revoked_by_full_name
              - New property: revoked_by_username
              - New property: scope_is_removed
              - New property: user_email
              - New property: user_username
              - New property: uuid
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/user-permissions/

- New query param: customer_uuid
- New query param: is_active
- New query param: show_inactive
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/user-permissions/{uuid}/

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: is_active
            - New property: revoke_reason
            - New property: revoked_by_full_name
            - New property: revoked_by_username
            - New property: scope_is_removed
            - New property: user_email
            - New property: user_username
            - New property: uuid
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/users/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [organization_address organization_vat_code primary_gid uid_number]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: organization_address
              - New property: organization_vat_code
              - New property: primary_gid
              - New property: uid_number
              - Modified property: permissions
                - Items changed
                  - Properties changed
                    - New property: is_active
                    - New property: revoke_reason
                    - New property: revoked_by_full_name
                    - New property: revoked_by_username
                    - New property: scope_is_removed
                    - New property: user_email
                    - New property: user_username
                    - New property: uuid
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/users/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/users/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: organization_address
          - New property: organization_vat_code
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: organization_address
          - New property: organization_vat_code
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: organization_address
          - New property: organization_vat_code
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: organization_address
            - New property: organization_vat_code
            - New property: primary_gid
            - New property: uid_number
            - Modified property: permissions
              - Items changed
                - Properties changed
                  - New property: is_active
                  - New property: revoke_reason
                  - New property: revoked_by_full_name
                  - New property: revoked_by_username
                  - New property: scope_is_removed
                  - New property: user_email
                  - New property: user_username
                  - New property: uuid
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/users/confirm_email/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/users/me/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [organization_address organization_vat_code primary_gid uid_number]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: organization_address
            - New property: organization_vat_code
            - New property: primary_gid
            - New property: uid_number
            - Modified property: permissions
              - Items changed
                - Properties changed
                  - Deleted property: created
                  - Deleted property: created_by_full_name
                  - Deleted property: created_by_username
                  - Deleted property: role_description
                  - Deleted property: user_name
                  - Deleted property: user_slug
                  - Deleted property: user_uuid
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/users/me/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/users/profile_completeness/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/users/profile_completeness/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/users/scim_sync_all/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/users/user_active_status_count/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/users/user_active_status_count/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/users/user_language_count/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/users/user_language_count/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/users/user_registration_trend/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/users/user_registration_trend/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/users/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/users/{uuid}/

- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [organization_address organization_vat_code primary_gid uid_number]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: organization_address
            - New property: organization_vat_code
            - New property: primary_gid
            - New property: uid_number
            - Modified property: permissions
              - Items changed
                - Properties changed
                  - New property: is_active
                  - New property: revoke_reason
                  - New property: revoked_by_full_name
                  - New property: revoked_by_username
                  - New property: scope_is_removed
                  - New property: user_email
                  - New property: user_username
                  - New property: uuid
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/users/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: organization_address
          - New property: organization_vat_code
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: organization_address
          - New property: organization_vat_code
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: organization_address
          - New property: organization_vat_code
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: organization_address
            - New property: organization_vat_code
            - New property: primary_gid
            - New property: uid_number
            - Modified property: permissions
              - Items changed
                - Properties changed
                  - New property: is_active
                  - New property: revoke_reason
                  - New property: revoked_by_full_name
                  - New property: revoked_by_username
                  - New property: scope_is_removed
                  - New property: user_email
                  - New property: user_username
                  - New property: uuid
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/users/{uuid}/

- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: organization_address
          - New property: organization_vat_code
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: organization_address
          - New property: organization_vat_code
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: organization_address
          - New property: organization_vat_code
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: organization_address
            - New property: organization_vat_code
            - New property: primary_gid
            - New property: uid_number
            - Modified property: permissions
              - Items changed
                - Properties changed
                  - New property: is_active
                  - New property: revoke_reason
                  - New property: revoked_by_full_name
                  - New property: revoked_by_username
                  - New property: scope_is_removed
                  - New property: user_email
                  - New property: user_username
                  - New property: uuid
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/users/{uuid}/cancel_change_email/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/users/{uuid}/change_email/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/users/{uuid}/change_password/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/users/{uuid}/data_access/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/users/{uuid}/data_access_history/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/users/{uuid}/history/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/users/{uuid}/history/at/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/users/{uuid}/identity_bridge_status/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/users/{uuid}/pull_remote_user/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/users/{uuid}/pull_scim_attributes/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/users/{uuid}/refresh_token/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/users/{uuid}/remove_password/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/users/{uuid}/send_notification/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/users/{uuid}/token/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/users/{uuid}/update_actions/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/version/

- Description changed from 'Retrieves the current installed version of the application and the latest available version from GitHub (if available). Requires staff or support user permissions.' to 'Retrieves the current installed version of the application. Staff and support users additionally receive the latest available version from GitHub when update checks are enabled.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: latest_version
              - Description changed from 'Latest available version from GitHub, if available.' to 'Latest available version from GitHub. Only included for staff or support users when update checks are enabled.'
- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/vmware-clusters/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/vmware-clusters/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/vmware-clusters/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/vmware-datastores/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/vmware-datastores/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/vmware-datastores/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/vmware-disks/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/vmware-disks/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/vmware-disks/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/vmware-disks/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/vmware-disks/{uuid}/extend/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/vmware-disks/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/vmware-disks/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/vmware-disks/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/vmware-disks/{uuid}/unlink/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/vmware-folders/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/vmware-folders/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/vmware-folders/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/vmware-limits/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/vmware-networks/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/vmware-networks/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/vmware-networks/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/vmware-ports/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/vmware-ports/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/vmware-ports/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/vmware-ports/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/vmware-ports/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/vmware-ports/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/vmware-ports/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/vmware-ports/{uuid}/unlink/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/vmware-templates/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/vmware-templates/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/vmware-templates/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/vmware-virtual-machine/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

HEAD /api/vmware-virtual-machine/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/vmware-virtual-machine/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

DELETE /api/vmware-virtual-machine/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/vmware-virtual-machine/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PATCH /api/vmware-virtual-machine/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

PUT /api/vmware-virtual-machine/{uuid}/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/vmware-virtual-machine/{uuid}/console/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/vmware-virtual-machine/{uuid}/create_disk/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/vmware-virtual-machine/{uuid}/create_port/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/vmware-virtual-machine/{uuid}/pull/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/vmware-virtual-machine/{uuid}/reboot_guest/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/vmware-virtual-machine/{uuid}/reset/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/vmware-virtual-machine/{uuid}/set_erred/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/vmware-virtual-machine/{uuid}/set_ok/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/vmware-virtual-machine/{uuid}/shutdown_guest/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/vmware-virtual-machine/{uuid}/start/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/vmware-virtual-machine/{uuid}/stop/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/vmware-virtual-machine/{uuid}/suspend/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

POST /api/vmware-virtual-machine/{uuid}/unlink/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth

GET /api/vmware-virtual-machine/{uuid}/web_console/

- Security changed
  - New security requirements: waldurTokenAuth
  - Deleted security requirements: tokenAuth
