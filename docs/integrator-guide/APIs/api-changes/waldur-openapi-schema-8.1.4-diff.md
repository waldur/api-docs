# OpenAPI schema diff - 8.1.4

## For version 8.1.4

### New Endpoints: 81

---------------------
POST /api/customer-credits/{uuid}/reclassify/  
POST /api/customer-credits/{uuid}/top_up/  
HEAD /api/debug/email/config/  
HEAD /api/debug/pubsub/circuit_breaker/  
HEAD /api/debug/pubsub/dead_letter_queue/  
HEAD /api/debug/pubsub/message_state_cache/  
HEAD /api/debug/pubsub/metrics/  
HEAD /api/debug/pubsub/overview/  
HEAD /api/debug/pubsub/queues/  
POST /api/event-consumers/register_webhook/  
POST /api/event-consumers/{uuid}/resync/  
POST /api/event-consumers/{uuid}/update_webhook/  
POST /api/export-pdf/  
GET /api/feedback-requests/  
HEAD /api/feedback-requests/  
GET /api/feedback-requests/{uuid}/  
GET /api/feedback-requests/{uuid}/checklist/  
GET /api/feedback-requests/{uuid}/completion_status/  
POST /api/feedback-requests/{uuid}/dismiss/  
POST /api/feedback-requests/{uuid}/later/  
POST /api/feedback-requests/{uuid}/submit_answers/  
GET /api/feedback-surveys/  
HEAD /api/feedback-surveys/  
POST /api/feedback-surveys/  
POST /api/feedback-surveys/prompt/  
DELETE /api/feedback-surveys/{uuid}/  
GET /api/feedback-surveys/{uuid}/  
PATCH /api/feedback-surveys/{uuid}/  
PUT /api/feedback-surveys/{uuid}/  
GET /api/feedback-surveys/{uuid}/summary/  
GET /api/global-user-roles/  
HEAD /api/global-user-roles/  
POST /api/global-user-roles/  
DELETE /api/global-user-roles/{uuid}/  
GET /api/global-user-roles/{uuid}/  
GET /api/hpc-workspaces/  
HEAD /api/hpc-workspaces/  
GET /api/hpc-workspaces/{uuid}/  
GET /api/hpc-workspaces/{uuid}/cluster_load/  
GET /api/hpc-workspaces/{uuid}/file_content/  
GET /api/hpc-workspaces/{uuid}/files/  
GET /api/hpc-workspaces/{uuid}/job_stats/  
GET /api/hpc-workspaces/{uuid}/jobs/  
POST /api/hpc-workspaces/{uuid}/jobs/  
GET /api/hpc-workspaces/{uuid}/jobs/{job_id}/  
POST /api/hpc-workspaces/{uuid}/jobs/{job_id}/cancel/  
GET /api/hpc-workspaces/{uuid}/jobs/{job_id}/output/  
GET /api/hpc-workspaces/{uuid}/jobs/{job_id}/performance/  
GET /api/hpc-workspaces/{uuid}/jobs/{job_id}/performance_pdf/  
GET /api/hpc-workspaces/{uuid}/output_series/  
GET /api/hpc-workspaces/{uuid}/partitions/  
POST /api/hpc-workspaces/{uuid}/preview_script/  
GET /api/hpc-workspaces/{uuid}/software/  
GET /api/hpc-workspaces/{uuid}/usage/  
GET /api/marketplace-customer-estimated-cost-policies/{uuid}/history/  
GET /api/marketplace-customer-estimated-cost-policies/{uuid}/history/at/  
GET /api/marketplace-offering-estimated-cost-policies/{uuid}/history/  
GET /api/marketplace-offering-estimated-cost-policies/{uuid}/history/at/  
GET /api/marketplace-openstack-instance-metrics/{uuid}/  
POST /api/marketplace-openstack-instance-metrics/{uuid}/faster_updates/  
POST /api/marketplace-openstack-instance-metrics/{uuid}/normal_updates/  
POST /api/marketplace-openstack-instance-metrics/{uuid}/update_now/  
GET /api/marketplace-project-estimated-cost-policies/{uuid}/history/  
GET /api/marketplace-project-estimated-cost-policies/{uuid}/history/at/  
POST /api/marketplace-provider-offerings/{uuid}/import_maintenance_reservations/  
GET /api/marketplace-provider-offerings/{uuid}/maintenance_reservations/  
POST /api/marketplace-provider-offerings/{uuid}/update_endpoint/  
POST /api/marketplace-resources/{uuid}/set_spending_limits/  
GET /api/matrix/rooms/{uuid}/commands/  
GET /api/matrix/ticket-drafts/{uuid}/  
POST /api/matrix/ticket-drafts/{uuid}/cancel/  
POST /api/matrix/ticket-drafts/{uuid}/create_issue/  
GET /api/openportal-unmanaged-projects/{uuid}/history/  
GET /api/openportal-unmanaged-projects/{uuid}/history/at/  
POST /api/openstack-instances/{uuid}/hard_reboot/  
GET /api/override-settings/sources/  
GET /api/project-credits/{uuid}/earlier_invoices/  
POST /api/project-credits/{uuid}/pay_earlier_invoices/  
GET /api/projects/{uuid}/history/  
GET /api/projects/{uuid}/history/at/  
GET /api/proposal-protected-calls/{uuid}/stats/  

### Deleted Endpoints: 52

-------------------------
POST /api/booking-offerings/{uuid}/google_calendar_sync/  
POST /api/booking-offerings/{uuid}/share_google_calendar/  
POST /api/booking-offerings/{uuid}/unshare_google_calendar/  
GET /api/google-auth/  
HEAD /api/google-auth/  
GET /api/google-auth/callback/  
HEAD /api/google-auth/callback/  
GET /api/google-auth/{uuid}/  
GET /api/google-auth/{uuid}/authorize/  
PATCH /api/keycloak-user-group-memberships/{uuid}/  
PUT /api/keycloak-user-group-memberships/{uuid}/  
PATCH /api/lexis-links/{uuid}/  
PUT /api/lexis-links/{uuid}/  
GET /api/marketplace-offering-users/checklist-template/  
HEAD /api/marketplace-offering-users/checklist-template/  
GET /api/marketplace-resources/{uuid}/glauth_tree/  
GET /api/marketplace-resources/{uuid}/glauth_users_config/  
DELETE /api/marketplace-user-offering-consents/{uuid}/  
PATCH /api/marketplace-user-offering-consents/{uuid}/  
PUT /api/marketplace-user-offering-consents/{uuid}/  
POST /api/onboarding-justifications/  
POST /api/onboarding-verifications/  
GET /api/onboarding-verifications/checklist-template/  
HEAD /api/onboarding-verifications/checklist-template/  
PATCH /api/openstack-migrations/{uuid}/  
PUT /api/openstack-migrations/{uuid}/  
PATCH /api/openstack-network-rbac-policies/{uuid}/  
PUT /api/openstack-network-rbac-policies/{uuid}/  
POST /api/openstack-server-groups/  
GET /api/openstack/discovery/  
POST /api/openstack/discovery/  
DELETE /api/openstack/discovery/{id}/  
GET /api/openstack/discovery/{id}/  
PATCH /api/openstack/discovery/{id}/  
PUT /api/openstack/discovery/{id}/  
GET /api/slurm-jobs/  
HEAD /api/slurm-jobs/  
POST /api/slurm-jobs/  
DELETE /api/slurm-jobs/{uuid}/  
GET /api/slurm-jobs/{uuid}/  
PATCH /api/slurm-jobs/{uuid}/  
PUT /api/slurm-jobs/{uuid}/  
POST /api/slurm-jobs/{uuid}/pull/  
POST /api/slurm-jobs/{uuid}/set_erred/  
POST /api/slurm-jobs/{uuid}/set_ok/  
POST /api/slurm-jobs/{uuid}/unlink/  
GET /api/support/settings/atlassian/  
POST /api/support/settings/atlassian/  
DELETE /api/support/settings/atlassian/{id}/  
GET /api/support/settings/atlassian/{id}/  
PATCH /api/support/settings/atlassian/{id}/  
PUT /api/support/settings/atlassian/{id}/  

### Modified Endpoints: 2879

----------------------------
POST /_matrix/app/v1/ping

- Extensions changed
  - New extension: x-permissions

PUT /_matrix/app/v1/transactions/{txn_id}

- Extensions changed
  - New extension: x-permissions

GET /api-auth/default/init/

- Extensions changed
  - New extension: x-permissions

GET /api-auth/eduteams/complete/

- Extensions changed
  - New extension: x-permissions

GET /api-auth/eduteams/init/

- Extensions changed
  - New extension: x-permissions

GET /api-auth/keycloak/complete/

- Extensions changed
  - New extension: x-permissions

GET /api-auth/keycloak/init/

- Extensions changed
  - New extension: x-permissions

POST /api-auth/logout/

- Extensions changed
  - New extension: x-permissions
- Description changed from 'Logs out the current user by deleting their authentication token. If single logout (SLO) is supported for the current authentication method (e.g., SAML2 or OIDC), this endpoint may return a logout URL to which the user should be redirected to complete the logout process on the identity provider side.' to 'Logs out the current user by deleting their authentication token and revoking the identity provider tokens Waldur keeps for them. If single logout (SLO) is supported for the current authentication method (e.g., SAML2 or OIDC), this endpoint may return a logout URL to which the user should be redirected to complete the logout process on the identity provider side.'

POST /api-auth/password/

- Extensions changed
  - New extension: x-permissions

POST /api-auth/saml2/login/

- Extensions changed
  - New extension: x-permissions

POST /api-auth/saml2/login/complete/

- Extensions changed
  - New extension: x-permissions

GET /api-auth/saml2/logout/

- Extensions changed
  - New extension: x-permissions

GET /api-auth/saml2/logout/complete/

- Extensions changed
  - New extension: x-permissions

POST /api-auth/saml2/logout/complete/

- Extensions changed
  - New extension: x-permissions

GET /api-auth/saml2/providers/

- Extensions changed
  - New extension: x-permissions

GET /api-auth/tara/complete/

- Extensions changed
  - New extension: x-permissions

GET /api-auth/tara/init/

- Extensions changed
  - New extension: x-permissions

POST /api-auth/token-exchange/

- Extensions changed
  - New extension: x-permissions

GET /api/access-subnets/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/access-subnets/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/access-subnets/

- Extensions changed
  - New extension: x-permissions

GET /api/access-subnets/resource_impact/

- Extensions changed
  - New extension: x-permissions

HEAD /api/access-subnets/resource_impact/

- Extensions changed
  - New extension: x-permissions

DELETE /api/access-subnets/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/access-subnets/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/access-subnets/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

PUT /api/access-subnets/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/admin-announcements/

- Extensions changed
  - New extension: x-permissions

HEAD /api/admin-announcements/

- Extensions changed
  - New extension: x-permissions

POST /api/admin-announcements/

- Extensions changed
  - New extension: x-permissions

DELETE /api/admin-announcements/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/admin-announcements/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/admin-announcements/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/admin-announcements/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/admin/arrow/billing-sync-items/

- Extensions changed
  - New extension: x-permissions

HEAD /api/admin/arrow/billing-sync-items/

- Extensions changed
  - New extension: x-permissions

GET /api/admin/arrow/billing-sync-items/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/admin/arrow/billing-syncs/

- Extensions changed
  - New extension: x-permissions

HEAD /api/admin/arrow/billing-syncs/

- Extensions changed
  - New extension: x-permissions

POST /api/admin/arrow/billing-syncs/cleanup_consumption/

- Extensions changed
  - New extension: x-permissions

GET /api/admin/arrow/billing-syncs/consumption_statistics/

- Extensions changed
  - New extension: x-permissions

HEAD /api/admin/arrow/billing-syncs/consumption_statistics/

- Extensions changed
  - New extension: x-permissions

GET /api/admin/arrow/billing-syncs/consumption_status/

- Extensions changed
  - New extension: x-permissions

HEAD /api/admin/arrow/billing-syncs/consumption_status/

- Extensions changed
  - New extension: x-permissions

POST /api/admin/arrow/billing-syncs/fetch_billing_export/

- Extensions changed
  - New extension: x-permissions

POST /api/admin/arrow/billing-syncs/fetch_consumption/

- Extensions changed
  - New extension: x-permissions

POST /api/admin/arrow/billing-syncs/fetch_license_info/

- Extensions changed
  - New extension: x-permissions

POST /api/admin/arrow/billing-syncs/pause_sync/

- Extensions changed
  - New extension: x-permissions

GET /api/admin/arrow/billing-syncs/pending_records/

- Extensions changed
  - New extension: x-permissions

HEAD /api/admin/arrow/billing-syncs/pending_records/

- Extensions changed
  - New extension: x-permissions

POST /api/admin/arrow/billing-syncs/reconcile/

- Extensions changed
  - New extension: x-permissions

POST /api/admin/arrow/billing-syncs/resume_sync/

- Extensions changed
  - New extension: x-permissions

POST /api/admin/arrow/billing-syncs/sync_resource_historical_consumption/

- Extensions changed
  - New extension: x-permissions

POST /api/admin/arrow/billing-syncs/sync_resources/

- Extensions changed
  - New extension: x-permissions

POST /api/admin/arrow/billing-syncs/trigger_consumption_sync/

- Extensions changed
  - New extension: x-permissions

POST /api/admin/arrow/billing-syncs/trigger_reconciliation/

- Extensions changed
  - New extension: x-permissions

POST /api/admin/arrow/billing-syncs/trigger_sync/

- Extensions changed
  - New extension: x-permissions

GET /api/admin/arrow/billing-syncs/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/admin/arrow/consumption-records/

- Extensions changed
  - New extension: x-permissions

HEAD /api/admin/arrow/consumption-records/

- Extensions changed
  - New extension: x-permissions

GET /api/admin/arrow/consumption-records/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/admin/arrow/customer-mappings/

- Extensions changed
  - New extension: x-permissions

HEAD /api/admin/arrow/customer-mappings/

- Extensions changed
  - New extension: x-permissions

POST /api/admin/arrow/customer-mappings/

- Extensions changed
  - New extension: x-permissions

GET /api/admin/arrow/customer-mappings/available_customers/

- Extensions changed
  - New extension: x-permissions

HEAD /api/admin/arrow/customer-mappings/available_customers/

- Extensions changed
  - New extension: x-permissions

POST /api/admin/arrow/customer-mappings/sync_from_arrow/

- Extensions changed
  - New extension: x-permissions

DELETE /api/admin/arrow/customer-mappings/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/admin/arrow/customer-mappings/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/admin/arrow/customer-mappings/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/admin/arrow/customer-mappings/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/admin/arrow/customer-mappings/{uuid}/billing_summary/

- Extensions changed
  - New extension: x-permissions

GET /api/admin/arrow/customer-mappings/{uuid}/discover_licenses/

- Extensions changed
  - New extension: x-permissions

GET /api/admin/arrow/customer-mappings/{uuid}/fetch_arrow_data/

- Extensions changed
  - New extension: x-permissions

POST /api/admin/arrow/customer-mappings/{uuid}/import_license/

- Extensions changed
  - New extension: x-permissions

POST /api/admin/arrow/customer-mappings/{uuid}/link_resource/

- Extensions changed
  - New extension: x-permissions

GET /api/admin/arrow/settings/

- Extensions changed
  - New extension: x-permissions

HEAD /api/admin/arrow/settings/

- Extensions changed
  - New extension: x-permissions

POST /api/admin/arrow/settings/

- Extensions changed
  - New extension: x-permissions

POST /api/admin/arrow/settings/discover_customers/

- Extensions changed
  - New extension: x-permissions

POST /api/admin/arrow/settings/preview_settings/

- Extensions changed
  - New extension: x-permissions

POST /api/admin/arrow/settings/save_settings/

- Extensions changed
  - New extension: x-permissions

POST /api/admin/arrow/settings/validate_credentials/

- Extensions changed
  - New extension: x-permissions

DELETE /api/admin/arrow/settings/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/admin/arrow/settings/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/admin/arrow/settings/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/admin/arrow/settings/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/admin/arrow/vendor-offering-mappings/

- Extensions changed
  - New extension: x-permissions

HEAD /api/admin/arrow/vendor-offering-mappings/

- Extensions changed
  - New extension: x-permissions

POST /api/admin/arrow/vendor-offering-mappings/

- Extensions changed
  - New extension: x-permissions

GET /api/admin/arrow/vendor-offering-mappings/vendor_choices/

- Extensions changed
  - New extension: x-permissions

HEAD /api/admin/arrow/vendor-offering-mappings/vendor_choices/

- Extensions changed
  - New extension: x-permissions

DELETE /api/admin/arrow/vendor-offering-mappings/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/admin/arrow/vendor-offering-mappings/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/admin/arrow/vendor-offering-mappings/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/admin/arrow/vendor-offering-mappings/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/admin/matrix-appservice/setup/

- Extensions changed
  - New extension: x-permissions

GET /api/admin/matrix-appservice/status/

- Extensions changed
  - New extension: x-permissions

GET /api/admin/matrix/diagnostics/

- Extensions changed
  - New extension: x-permissions

GET /api/admin/matrix/livekit/overview/

- Extensions changed
  - New extension: x-permissions

GET /api/admin/matrix/livekit/participants/

- Extensions changed
  - New extension: x-permissions

POST /api/admin/matrix/reprovision/

- Extensions changed
  - New extension: x-permissions

GET /api/affiliated-organizations/

- Extensions changed
  - New extension: x-permissions

HEAD /api/affiliated-organizations/

- Extensions changed
  - New extension: x-permissions

POST /api/affiliated-organizations/

- Extensions changed
  - New extension: x-permissions

GET /api/affiliated-organizations/report/

- Extensions changed
  - New extension: x-permissions

HEAD /api/affiliated-organizations/report/

- Extensions changed
  - New extension: x-permissions

DELETE /api/affiliated-organizations/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/affiliated-organizations/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/affiliated-organizations/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/affiliated-organizations/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/affiliated-organizations/{uuid}/stats/

- Extensions changed
  - New extension: x-permissions

GET /api/anonymous-chat-feedbacks/

- Extensions changed
  - New extension: x-permissions

GET /api/anonymous-chat-feedbacks/{interaction_uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/anonymous-chat-interactions/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: cache_read_tokens
              - New required property: cache_write_tokens
            - Properties changed
              - New property: cache_read_tokens
              - New property: cache_write_tokens

GET /api/anonymous-chat-interactions/budget/

- Extensions changed
  - New extension: x-permissions

GET /api/anonymous-chat-interactions/by-session/{session_id}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: cache_read_tokens
              - New required property: cache_write_tokens
            - Properties changed
              - New property: cache_read_tokens
              - New property: cache_write_tokens

GET /api/anonymous-chat-interactions/by-user/

- Extensions changed
  - New extension: x-permissions

GET /api/anonymous-chat-interactions/by-user/{user_slug}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: cache_read_tokens
              - New required property: cache_write_tokens
            - Properties changed
              - New property: cache_read_tokens
              - New property: cache_write_tokens

GET /api/anonymous-chat-interactions/conversations/

- Extensions changed
  - New extension: x-permissions
- Description changed from 'One row per anonymous conversation (``session_id``) with aggregate counters, mirroring the authenticated threads table. Honours the same filters as the list endpoint. Read a conversation's transcript via ``by-session/{session_id}``.' to 'One row per anonymous conversation (``session_id``) with aggregate counters, mirroring the authenticated threads table. Honors the same filters as the list endpoint. Read a conversation's transcript via ``by-session/{session_id}``.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: cache_ratio
              - New required property: cache_read_tokens
              - New required property: cache_write_tokens
            - Properties changed
              - New property: cache_ratio
              - New property: cache_read_tokens
              - New property: cache_write_tokens

GET /api/anonymous-chat-interactions/kpi/

- Extensions changed
  - New extension: x-permissions
- Description changed from 'Returns aggregate counters and rates for the anonymous chat flow. Filters are honoured (date range etc.) so the same parameters work as on the list endpoint.' to 'Returns aggregate counters and rates for the anonymous chat flow. Filters are honored (date range etc.) so the same parameters work as on the list endpoint.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: cache_ratio
            - New required property: cache_read_tokens_total
            - New required property: cache_write_tokens_total
            - New required property: no_result_rate
            - New required property: no_result_searches_total
            - New required property: searches_total
          - Properties changed
            - New property: cache_ratio
            - New property: cache_read_tokens_total
            - New property: cache_write_tokens_total
            - New property: no_result_rate
            - New property: no_result_searches_total
            - New property: searches_total

GET /api/anonymous-chat-interactions/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: cache_read_tokens
            - New required property: cache_write_tokens
          - Properties changed
            - New property: cache_read_tokens
            - New property: cache_write_tokens

GET /api/assignment-batches/

- Extensions changed
  - New extension: x-permissions

HEAD /api/assignment-batches/

- Extensions changed
  - New extension: x-permissions

DELETE /api/assignment-batches/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/assignment-batches/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/assignment-batches/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/assignment-batches/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/assignment-batches/{uuid}/cancel/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/assignment-batches/{uuid}/extend-deadline/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/assignment-batches/{uuid}/send/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/assignment-items/

- Extensions changed
  - New extension: x-permissions

HEAD /api/assignment-items/

- Extensions changed
  - New extension: x-permissions

DELETE /api/assignment-items/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/assignment-items/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/assignment-items/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/assignment-items/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/assignment-items/{uuid}/accept/

- Extensions changed
  - New extension: x-permissions

POST /api/assignment-items/{uuid}/decline/

- Extensions changed
  - New extension: x-permissions

POST /api/assignment-items/{uuid}/force-unblock/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/assignment-items/{uuid}/reassign/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/assignment-items/{uuid}/suggest_alternatives/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/auth-tokens/

- Extensions changed
  - New extension: x-permissions

HEAD /api/auth-tokens/

- Extensions changed
  - New extension: x-permissions

DELETE /api/auth-tokens/{user_id}/

- Extensions changed
  - New extension: x-permissions

GET /api/auth-tokens/{user_id}/

- Extensions changed
  - New extension: x-permissions

POST /api/auth-valimo/

- Extensions changed
  - New extension: x-permissions

POST /api/auth-valimo/result/

- Extensions changed
  - New extension: x-permissions

GET /api/autoprovisioning-rules/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/autoprovisioning-rules/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/autoprovisioning-rules/

- Extensions changed
  - New extension: x-permissions

DELETE /api/autoprovisioning-rules/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/autoprovisioning-rules/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/autoprovisioning-rules/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/autoprovisioning-rules/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/autoprovisioning-rules/{uuid}/test-match/

- Extensions changed
  - New extension: x-permissions

GET /api/aws-images/

- Extensions changed
  - New extension: x-permissions

HEAD /api/aws-images/

- Extensions changed
  - New extension: x-permissions

GET /api/aws-images/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/aws-instances/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/aws-instances/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/aws-instances/

- Extensions changed
  - New extension: x-permissions

DELETE /api/aws-instances/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/aws-instances/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/aws-instances/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/aws-instances/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/aws-instances/{uuid}/pull/

- Extensions changed
  - New extension: x-permissions

POST /api/aws-instances/{uuid}/resize/

- Extensions changed
  - New extension: x-permissions

POST /api/aws-instances/{uuid}/restart/

- Extensions changed
  - New extension: x-permissions

POST /api/aws-instances/{uuid}/set_erred/

- Extensions changed
  - New extension: x-permissions

POST /api/aws-instances/{uuid}/set_ok/

- Extensions changed
  - New extension: x-permissions

POST /api/aws-instances/{uuid}/start/

- Extensions changed
  - New extension: x-permissions

POST /api/aws-instances/{uuid}/stop/

- Extensions changed
  - New extension: x-permissions

POST /api/aws-instances/{uuid}/unlink/

- Extensions changed
  - New extension: x-permissions

GET /api/aws-regions/

- Extensions changed
  - New extension: x-permissions

HEAD /api/aws-regions/

- Extensions changed
  - New extension: x-permissions

GET /api/aws-regions/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/aws-sizes/

- Extensions changed
  - New extension: x-permissions

HEAD /api/aws-sizes/

- Extensions changed
  - New extension: x-permissions

GET /api/aws-sizes/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/aws-volumes/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/aws-volumes/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/aws-volumes/

- Extensions changed
  - New extension: x-permissions

DELETE /api/aws-volumes/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/aws-volumes/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/aws-volumes/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/aws-volumes/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/aws-volumes/{uuid}/attach/

- Extensions changed
  - New extension: x-permissions

POST /api/aws-volumes/{uuid}/detach/

- Extensions changed
  - New extension: x-permissions

POST /api/aws-volumes/{uuid}/pull/

- Extensions changed
  - New extension: x-permissions

POST /api/aws-volumes/{uuid}/set_erred/

- Extensions changed
  - New extension: x-permissions

POST /api/aws-volumes/{uuid}/set_ok/

- Extensions changed
  - New extension: x-permissions

POST /api/aws-volumes/{uuid}/unlink/

- Extensions changed
  - New extension: x-permissions

GET /api/backend-resource-requests/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/backend-resource-requests/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/backend-resource-requests/

- Extensions changed
  - New extension: x-permissions

GET /api/backend-resource-requests/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/backend-resource-requests/{uuid}/set_done/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/backend-resource-requests/{uuid}/set_erred/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/backend-resource-requests/{uuid}/start_processing/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/backend-resources/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/backend-resources/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/backend-resources/

- Extensions changed
  - New extension: x-permissions

DELETE /api/backend-resources/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/backend-resources/{uuid}/

- Extensions changed
  - New extension: x-visibility
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/backend-resources/{uuid}/import_resource/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: display_limits
            - New property: prepaid_total_component_types
            - New property: spending_limit_status
            - New property: spending_limits
            - New property: terminated_at
            - New property: usage_limit_resumes_at
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: callback_url
            - Modified property: endpoints
              - Items changed
                - Properties changed
                  - Modified property: url
                    - Format changed from '' to 'uri'
                    - MaxLength changed from null to 200
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: spending_limit_periods
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: callback_url

GET /api/billing-total-cost/

- Extensions changed
  - New extension: x-permissions

GET /api/booking-offerings/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [googlecalendar]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Deleted property: googlecalendar
              - Modified property: components
                - Items changed
                  - Properties changed
                    - New property: spending_limit_periods
              - Modified property: endpoints
                - Items changed
                  - Properties changed
                    - Modified property: url
                      - Format changed from '' to 'uri'
                      - MaxLength changed from null to 200
              - Modified property: options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - New property: display_limit_config
                            - New property: transform
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: api_key_daily_usage
                      - New property: api_key_limits
                      - New property: display_prepaid_limits_as_total
                      - New property: firecrest_api_url
                      - New property: firecrest_system_name
                      - New property: instance_metrics
                      - New property: instance_metrics_enabled
                      - New property: instance_metrics_poll_interval_minutes
                      - New property: slurm_maintenance_sync_enabled
                      - New property: slurm_monitor_api_url
                      - New property: slurm_monitor_cluster_name
                      - Modified property: account_scope
                        - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'
              - Modified property: qos_profiles
                - Items changed
                  - Properties changed
                    - New property: max_tres_mins_per_job
                    - Modified property: grp_tres
                      - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                    - Modified property: max_tres_per_job
                      - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                    - Modified property: max_tres_per_node
                      - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                    - Modified property: max_tres_per_user
                      - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                    - Modified property: min_tres_per_job
                      - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
              - Modified property: resource_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - New property: display_limit_config
                            - New property: transform

HEAD /api/booking-offerings/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/booking-offerings/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [googlecalendar]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: googlecalendar
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: spending_limit_periods
            - Modified property: endpoints
              - Items changed
                - Properties changed
                  - Modified property: url
                    - Format changed from '' to 'uri'
                    - MaxLength changed from null to 200
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: display_limit_config
                          - New property: transform
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: api_key_daily_usage
                    - New property: api_key_limits
                    - New property: display_prepaid_limits_as_total
                    - New property: firecrest_api_url
                    - New property: firecrest_system_name
                    - New property: instance_metrics
                    - New property: instance_metrics_enabled
                    - New property: instance_metrics_poll_interval_minutes
                    - New property: slurm_maintenance_sync_enabled
                    - New property: slurm_monitor_api_url
                    - New property: slurm_monitor_cluster_name
                    - Modified property: account_scope
                      - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'
            - Modified property: qos_profiles
              - Items changed
                - Properties changed
                  - New property: max_tres_mins_per_job
                  - Modified property: grp_tres
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                  - Modified property: max_tres_per_job
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                  - Modified property: max_tres_per_node
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                  - Modified property: max_tres_per_user
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                  - Modified property: min_tres_per_job
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: display_limit_config
                          - New property: transform

GET /api/booking-resources/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [display_limits prepaid_total_component_types spending_limit_status spending_limits terminated_at usage_limit_resumes_at]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: display_limits
              - New property: prepaid_total_component_types
              - New property: spending_limit_status
              - New property: spending_limits
              - New property: terminated_at
              - New property: usage_limit_resumes_at
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Deleted property: callback_url
              - Modified property: endpoints
                - Items changed
                  - Properties changed
                    - Modified property: url
                      - Format changed from '' to 'uri'
                      - MaxLength changed from null to 200
              - Modified property: offering_components
                - Items changed
                  - Properties changed
                    - New property: spending_limit_periods
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Deleted property: callback_url

HEAD /api/booking-resources/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/booking-resources/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [display_limits prepaid_total_component_types spending_limit_status spending_limits terminated_at usage_limit_resumes_at]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: display_limits
            - New property: prepaid_total_component_types
            - New property: spending_limit_status
            - New property: spending_limits
            - New property: terminated_at
            - New property: usage_limit_resumes_at
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: callback_url
            - Modified property: endpoints
              - Items changed
                - Properties changed
                  - Modified property: url
                    - Format changed from '' to 'uri'
                    - MaxLength changed from null to 200
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: spending_limit_periods
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: callback_url

POST /api/booking-resources/{uuid}/accept/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/booking-resources/{uuid}/reject/

- Extensions changed
  - New extension: x-permissions

GET /api/broadcast-message-templates/

- Extensions changed
  - New extension: x-permissions

HEAD /api/broadcast-message-templates/

- Extensions changed
  - New extension: x-permissions

POST /api/broadcast-message-templates/

- Extensions changed
  - New extension: x-permissions

DELETE /api/broadcast-message-templates/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/broadcast-message-templates/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/broadcast-message-templates/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/broadcast-message-templates/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/broadcast-messages/

- Extensions changed
  - New extension: x-permissions

HEAD /api/broadcast-messages/

- Extensions changed
  - New extension: x-permissions

POST /api/broadcast-messages/

- Extensions changed
  - New extension: x-permissions

GET /api/broadcast-messages/recipients/

- Extensions changed
  - New extension: x-permissions

HEAD /api/broadcast-messages/recipients/

- Extensions changed
  - New extension: x-permissions

DELETE /api/broadcast-messages/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/broadcast-messages/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/broadcast-messages/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/broadcast-messages/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/broadcast-messages/{uuid}/schedule/

- Extensions changed
  - New extension: x-permissions

POST /api/broadcast-messages/{uuid}/send/

- Extensions changed
  - New extension: x-permissions

GET /api/call-assignment-configurations/

- Extensions changed
  - New extension: x-permissions

HEAD /api/call-assignment-configurations/

- Extensions changed
  - New extension: x-permissions

DELETE /api/call-assignment-configurations/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/call-assignment-configurations/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/call-assignment-configurations/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/call-assignment-configurations/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/call-managing-organisations/

- Extensions changed
  - New extension: x-permissions

HEAD /api/call-managing-organisations/

- Extensions changed
  - New extension: x-permissions

POST /api/call-managing-organisations/

- Extensions changed
  - New extension: x-permissions

GET /api/call-managing-organisations/global_stats_performance/

- Extensions changed
  - New extension: x-permissions

HEAD /api/call-managing-organisations/global_stats_performance/

- Extensions changed
  - New extension: x-permissions

GET /api/call-managing-organisations/global_stats_resource_demand/

- Extensions changed
  - New extension: x-permissions

HEAD /api/call-managing-organisations/global_stats_resource_demand/

- Extensions changed
  - New extension: x-permissions

GET /api/call-managing-organisations/global_stats_review_progress/

- Extensions changed
  - New extension: x-permissions

HEAD /api/call-managing-organisations/global_stats_review_progress/

- Extensions changed
  - New extension: x-permissions

DELETE /api/call-managing-organisations/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/call-managing-organisations/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/call-managing-organisations/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/call-managing-organisations/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/call-managing-organisations/{uuid}/add_user/

- Extensions changed
  - New extension: x-permissions

POST /api/call-managing-organisations/{uuid}/delete_user/

- Extensions changed
  - New extension: x-permissions

GET /api/call-managing-organisations/{uuid}/list_users/

- Extensions changed
  - New extension: x-permissions
- New query param: role_template

HEAD /api/call-managing-organisations/{uuid}/list_users/

- Extensions changed
  - New extension: x-permissions
- New query param: role_template

GET /api/call-managing-organisations/{uuid}/stats/

- Extensions changed
  - New extension: x-permissions
- Description changed from 'Return statistics for call managing organisation.' to 'Return statistics for call managing organization.'

POST /api/call-managing-organisations/{uuid}/update_user/

- Extensions changed
  - New extension: x-permissions

GET /api/call-proposal-project-role-mappings/

- Extensions changed
  - New extension: x-permissions

HEAD /api/call-proposal-project-role-mappings/

- Extensions changed
  - New extension: x-permissions

POST /api/call-proposal-project-role-mappings/

- Extensions changed
  - New extension: x-permissions

DELETE /api/call-proposal-project-role-mappings/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/call-proposal-project-role-mappings/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/call-proposal-project-role-mappings/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/call-proposal-project-role-mappings/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/call-reviewer-pools/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: invited_email
                - Default changed from null to ''

HEAD /api/call-reviewer-pools/

- Extensions changed
  - New extension: x-permissions

GET /api/call-reviewer-pools/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: invited_email
              - Default changed from null to ''

PATCH /api/call-reviewer-pools/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/call-reviewer-pools/{uuid}/accept/

- Extensions changed
  - New extension: x-permissions

POST /api/call-reviewer-pools/{uuid}/decline/

- Extensions changed
  - New extension: x-permissions

POST /api/call-reviewer-pools/{uuid}/force-accept/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: invited_email
              - Default changed from null to ''

POST /api/call-reviewer-pools/{uuid}/resend-invitation/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: invited_email
              - Default changed from null to ''

GET /api/call-rounds/

- Extensions changed
  - New extension: x-permissions

HEAD /api/call-rounds/

- Extensions changed
  - New extension: x-permissions

GET /api/call-rounds/dashboard-deadlines/

- Extensions changed
  - New extension: x-permissions

HEAD /api/call-rounds/dashboard-deadlines/

- Extensions changed
  - New extension: x-permissions

GET /api/call-rounds/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/call-rounds/{uuid}/reviewers/

- Extensions changed
  - New extension: x-permissions

GET /api/call-workflow-step-notification-rules/

- Extensions changed
  - New extension: x-permissions

HEAD /api/call-workflow-step-notification-rules/

- Extensions changed
  - New extension: x-permissions

POST /api/call-workflow-step-notification-rules/

- Extensions changed
  - New extension: x-permissions

DELETE /api/call-workflow-step-notification-rules/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/call-workflow-step-notification-rules/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/call-workflow-step-notification-rules/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/call-workflow-step-notification-rules/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/celery-stats/

- Extensions changed
  - New extension: x-permissions
- Description changed from 'Provides a comprehensive snapshot of all Celery workers' status.

This endpoint returns detailed information about:

- **active**: Tasks currently being executed by workers
- **scheduled**: Tasks scheduled for future execution (with ETA)
- **reserved**: Tasks received by workers but not yet started
- **revoked**: Task IDs that have been cancelled/revoked
- **query_task**: Results of task queries (if any)
- **stats**: Detailed worker statistics including uptime, pool info, and broker connection

Each field is a dictionary where keys are worker names (e.g., 'celery@hostname').
If no workers are available, fields will be `null`.

Requires support user permissions.' to 'Provides a comprehensive snapshot of all Celery workers' status.

This endpoint returns detailed information about:

- **active**: Tasks currently being executed by workers
- **scheduled**: Tasks scheduled for future execution (with ETA)
- **reserved**: Tasks received by workers but not yet started
- **revoked**: Task IDs that have been canceled/revoked
- **query_task**: Results of task queries (if any)
- **stats**: Detailed worker statistics including uptime, pool info, and broker connection

Each field is a dictionary where keys are worker names (e.g., 'celery@hostname').
If no workers are available, fields will be `null`.

Requires support user permissions.'

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: revoked
              - Description changed from 'IDs of revoked (cancelled) tasks per worker. Keys are worker names, values are lists of task IDs.' to 'IDs of revoked (canceled) tasks per worker. Keys are worker names, values are lists of task IDs.'

GET /api/changelog-entries/

- Extensions changed
  - New extension: x-permissions

GET /api/changelog-upgrade-report/

- Extensions changed
  - New extension: x-permissions

GET /api/changelog/compare/{from_version}/{to_version}/

- Extensions changed
  - New extension: x-permissions

GET /api/changelog/pending/

- Extensions changed
  - New extension: x-permissions

GET /api/changelog/releases/

- Extensions changed
  - New extension: x-permissions

GET /api/changelog/{version}/

- Extensions changed
  - New extension: x-permissions

GET /api/changelog/{version}/delta/

- Extensions changed
  - New extension: x-permissions

GET /api/chat-messages/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: cache_read_tokens
              - New required property: cache_write_tokens
            - Properties changed
              - New property: cache_read_tokens
              - New property: cache_write_tokens
              - Modified property: blocks
                - Items changed
                  - Properties changed
                    - Modified property: key
                      - New enum values: [hpc_job chart]

POST /api/chat-messages/{uuid}/feedback/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: cache_read_tokens
            - New required property: cache_write_tokens
          - Properties changed
            - New property: cache_read_tokens
            - New property: cache_write_tokens
            - Modified property: blocks
              - Items changed
                - Properties changed
                  - Modified property: key
                    - New enum values: [hpc_job chart]

POST /api/chat-quota/set_quota/

- Extensions changed
  - New extension: x-permissions

GET /api/chat-quota/usage/

- Extensions changed
  - New extension: x-permissions
- Modified query param: user_uuid
  - Required changed from true to false

GET /api/chat-sessions/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/chat-sessions/current/

- Extensions changed
  - New extension: x-permissions

GET /api/chat-sessions/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/chat-system-prompts/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: custom_instructions
                - Description changed from 'Additional instructions injected into the system prompt. Use this for organisation-specific context, terminology, FAQ content, or behavioural guidelines. Supports {assistant_name} and {organization} placeholders.' to 'Additional instructions injected into the system prompt. Use this for organization-specific context, terminology, FAQ content, or behavioral guidelines. Supports {assistant_name} and {organization} placeholders.'

HEAD /api/chat-system-prompts/

- Extensions changed
  - New extension: x-permissions

POST /api/chat-system-prompts/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: custom_instructions
            - Description changed from 'Additional instructions injected into the system prompt. Use this for organisation-specific context, terminology, FAQ content, or behavioural guidelines. Supports {assistant_name} and {organization} placeholders.' to 'Additional instructions injected into the system prompt. Use this for organization-specific context, terminology, FAQ content, or behavioral guidelines. Supports {assistant_name} and {organization} placeholders.'
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: custom_instructions
              - Description changed from 'Additional instructions injected into the system prompt. Use this for organisation-specific context, terminology, FAQ content, or behavioural guidelines. Supports {assistant_name} and {organization} placeholders.' to 'Additional instructions injected into the system prompt. Use this for organization-specific context, terminology, FAQ content, or behavioral guidelines. Supports {assistant_name} and {organization} placeholders.'

DELETE /api/chat-system-prompts/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/chat-system-prompts/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: custom_instructions
              - Description changed from 'Additional instructions injected into the system prompt. Use this for organisation-specific context, terminology, FAQ content, or behavioural guidelines. Supports {assistant_name} and {organization} placeholders.' to 'Additional instructions injected into the system prompt. Use this for organization-specific context, terminology, FAQ content, or behavioral guidelines. Supports {assistant_name} and {organization} placeholders.'

PATCH /api/chat-system-prompts/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: custom_instructions
            - Description changed from 'Additional instructions injected into the system prompt. Use this for organisation-specific context, terminology, FAQ content, or behavioural guidelines. Supports {assistant_name} and {organization} placeholders.' to 'Additional instructions injected into the system prompt. Use this for organization-specific context, terminology, FAQ content, or behavioral guidelines. Supports {assistant_name} and {organization} placeholders.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: custom_instructions
              - Description changed from 'Additional instructions injected into the system prompt. Use this for organisation-specific context, terminology, FAQ content, or behavioural guidelines. Supports {assistant_name} and {organization} placeholders.' to 'Additional instructions injected into the system prompt. Use this for organization-specific context, terminology, FAQ content, or behavioral guidelines. Supports {assistant_name} and {organization} placeholders.'

PUT /api/chat-system-prompts/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: custom_instructions
            - Description changed from 'Additional instructions injected into the system prompt. Use this for organisation-specific context, terminology, FAQ content, or behavioural guidelines. Supports {assistant_name} and {organization} placeholders.' to 'Additional instructions injected into the system prompt. Use this for organization-specific context, terminology, FAQ content, or behavioral guidelines. Supports {assistant_name} and {organization} placeholders.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: custom_instructions
              - Description changed from 'Additional instructions injected into the system prompt. Use this for organisation-specific context, terminology, FAQ content, or behavioural guidelines. Supports {assistant_name} and {organization} placeholders.' to 'Additional instructions injected into the system prompt. Use this for organization-specific context, terminology, FAQ content, or behavioral guidelines. Supports {assistant_name} and {organization} placeholders.'

POST /api/chat-system-prompts/{uuid}/activate/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: custom_instructions
            - Description changed from 'Additional instructions injected into the system prompt. Use this for organisation-specific context, terminology, FAQ content, or behavioural guidelines. Supports {assistant_name} and {organization} placeholders.' to 'Additional instructions injected into the system prompt. Use this for organization-specific context, terminology, FAQ content, or behavioral guidelines. Supports {assistant_name} and {organization} placeholders.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: custom_instructions
              - Description changed from 'Additional instructions injected into the system prompt. Use this for organisation-specific context, terminology, FAQ content, or behavioural guidelines. Supports {assistant_name} and {organization} placeholders.' to 'Additional instructions injected into the system prompt. Use this for organization-specific context, terminology, FAQ content, or behavioral guidelines. Supports {assistant_name} and {organization} placeholders.'

POST /api/chat-system-prompts/{uuid}/deactivate/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: custom_instructions
            - Description changed from 'Additional instructions injected into the system prompt. Use this for organisation-specific context, terminology, FAQ content, or behavioural guidelines. Supports {assistant_name} and {organization} placeholders.' to 'Additional instructions injected into the system prompt. Use this for organization-specific context, terminology, FAQ content, or behavioral guidelines. Supports {assistant_name} and {organization} placeholders.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: custom_instructions
              - Description changed from 'Additional instructions injected into the system prompt. Use this for organisation-specific context, terminology, FAQ content, or behavioural guidelines. Supports {assistant_name} and {organization} placeholders.' to 'Additional instructions injected into the system prompt. Use this for organization-specific context, terminology, FAQ content, or behavioral guidelines. Supports {assistant_name} and {organization} placeholders.'

GET /api/chat-threads/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [cache_ratio cache_read_tokens cache_write_tokens title_gen_cache_read_tokens title_gen_cache_write_tokens]
- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-cache_ratio -cache_read_tokens -cache_write_tokens cache_ratio cache_read_tokens cache_write_tokens]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: cache_ratio
              - New property: cache_read_tokens
              - New property: cache_write_tokens
              - New property: title_gen_cache_read_tokens
              - New property: title_gen_cache_write_tokens

GET /api/chat-threads/stats/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Modified query param: o
  - Schema changed
    - Items changed
      - New enum values: [-cache_ratio -cache_read_tokens -cache_write_tokens cache_ratio cache_read_tokens cache_write_tokens]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: cache_ratio
            - New required property: cache_read_tokens_total
            - New required property: cache_write_tokens_total
          - Properties changed
            - New property: cache_ratio
            - New property: cache_read_tokens_total
            - New property: cache_write_tokens_total

GET /api/chat-threads/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [cache_ratio cache_read_tokens cache_write_tokens title_gen_cache_read_tokens title_gen_cache_write_tokens]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: cache_ratio
            - New property: cache_read_tokens
            - New property: cache_write_tokens
            - New property: title_gen_cache_read_tokens
            - New property: title_gen_cache_write_tokens

POST /api/chat-threads/{uuid}/archive/

- Extensions changed
  - New extension: x-permissions

POST /api/chat-threads/{uuid}/cancel/

- Extensions changed
  - New extension: x-permissions

POST /api/chat-threads/{uuid}/unarchive/

- Extensions changed
  - New extension: x-permissions

POST /api/chat-tools/execute/

- Extensions changed
  - New extension: x-permissions

POST /api/chat/stream/

- Extensions changed
  - New extension: x-permissions

GET /api/checklists-admin-question-dependencies/

- Extensions changed
  - New extension: x-permissions

HEAD /api/checklists-admin-question-dependencies/

- Extensions changed
  - New extension: x-permissions

POST /api/checklists-admin-question-dependencies/

- Extensions changed
  - New extension: x-permissions

DELETE /api/checklists-admin-question-dependencies/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/checklists-admin-question-dependencies/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/checklists-admin-question-dependencies/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/checklists-admin-question-dependencies/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/checklists-admin-question-options/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/checklists-admin-question-options/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/checklists-admin-question-options/

- Extensions changed
  - New extension: x-permissions

DELETE /api/checklists-admin-question-options/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/checklists-admin-question-options/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/checklists-admin-question-options/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/checklists-admin-question-options/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/checklists-admin-questions/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Modified query param: checklist_type
  - Schema changed
    - New enum values: [feedback]

HEAD /api/checklists-admin-questions/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Modified query param: checklist_type
  - Schema changed
    - New enum values: [feedback]

POST /api/checklists-admin-questions/

- Extensions changed
  - New extension: x-permissions

DELETE /api/checklists-admin-questions/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/checklists-admin-questions/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/checklists-admin-questions/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/checklists-admin-questions/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/checklists-admin/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Modified query param: checklist_type
  - Schema changed
    - New enum values: [feedback]
- Modified query param: checklist_type__in
  - Schema changed
    - Items changed
      - New enum values: [feedback]
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
                    - New enum values: [feedback]

HEAD /api/checklists-admin/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Modified query param: checklist_type
  - Schema changed
    - New enum values: [feedback]
- Modified query param: checklist_type__in
  - Schema changed
    - Items changed
      - New enum values: [feedback]

POST /api/checklists-admin/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: checklist_type
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/ChecklistTypeEnum
                - New enum values: [feedback]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: checklist_type
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ChecklistTypeEnum
                  - New enum values: [feedback]

DELETE /api/checklists-admin/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/checklists-admin/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: checklist_type
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ChecklistTypeEnum
                  - New enum values: [feedback]

PATCH /api/checklists-admin/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: checklist_type
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/ChecklistTypeEnum
                - New enum values: [feedback]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: checklist_type
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ChecklistTypeEnum
                  - New enum values: [feedback]

PUT /api/checklists-admin/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: checklist_type
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/ChecklistTypeEnum
                - New enum values: [feedback]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: checklist_type
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ChecklistTypeEnum
                  - New enum values: [feedback]

GET /api/checklists-admin/{uuid}/questions/

- Extensions changed
  - New extension: x-permissions
- Modified query param: checklist_type
  - Schema changed
    - New enum values: [feedback]
- Modified query param: checklist_type__in
  - Schema changed
    - Items changed
      - New enum values: [feedback]

GET /api/coi-detection-jobs/

- Extensions changed
  - New extension: x-permissions

HEAD /api/coi-detection-jobs/

- Extensions changed
  - New extension: x-permissions

GET /api/coi-detection-jobs/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/coi-disclosures/

- Extensions changed
  - New extension: x-permissions

HEAD /api/coi-disclosures/

- Extensions changed
  - New extension: x-permissions

POST /api/coi-disclosures/

- Extensions changed
  - New extension: x-permissions

GET /api/coi-disclosures/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/component-user-usage-limits/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/component-user-usage-limits/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/component-user-usage-limits/

- Extensions changed
  - New extension: x-permissions

DELETE /api/component-user-usage-limits/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/component-user-usage-limits/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/component-user-usage-limits/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

PUT /api/component-user-usage-limits/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/configuration/

- Extensions changed
  - New extension: x-permissions

GET /api/conflicts-of-interest/

- Extensions changed
  - New extension: x-permissions

HEAD /api/conflicts-of-interest/

- Extensions changed
  - New extension: x-permissions

GET /api/conflicts-of-interest/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/conflicts-of-interest/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

PUT /api/conflicts-of-interest/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/conflicts-of-interest/{uuid}/dismiss/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/conflicts-of-interest/{uuid}/recuse/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/conflicts-of-interest/{uuid}/waive/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/credit-transactions/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: earned_change
              - New required property: granted_change
              - New required property: paid_change
            - Properties changed
              - New property: earned_change
              - New property: granted_change
              - New property: paid_change
              - Modified property: transaction_type
                - New enum values: [top_up reclassification historical_compensation]

HEAD /api/credit-transactions/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/credit-transactions/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: earned_change
            - New required property: granted_change
            - New required property: paid_change
          - Properties changed
            - New property: earned_change
            - New property: granted_change
            - New property: paid_change
            - Modified property: transaction_type
              - New enum values: [top_up reclassification historical_compensation]

GET /api/customer-affiliates/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: is_active
                - Default changed from null to true

HEAD /api/customer-affiliates/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/customer-affiliates/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: is_active
            - Default changed from null to true
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: is_active
              - Default changed from null to true

DELETE /api/customer-affiliates/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/customer-affiliates/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: is_active
              - Default changed from null to true

PATCH /api/customer-affiliates/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: is_active
            - Default changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: is_active
              - Default changed from null to true

PUT /api/customer-affiliates/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: is_active
            - Default changed from null to true
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: is_active
              - Default changed from null to true

GET /api/customer-affiliates/{uuid}/accruals/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/customer-affiliates/{uuid}/earnings/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Description changed from 'Earnings summary of this affiliate link: lifetime total, per-month series and the affiliate organization's withdrawable credit balance.' to 'Earnings summary of this affiliate link: lifetime total, per-month series, the affiliate organization's withdrawable credit balance and the fee the current month is expected to earn.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: upcoming
          - Properties changed
            - New property: upcoming

GET /api/customer-credits/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: granted_balance
              - New required property: paid_balance
            - Properties changed
              - New property: granted_balance
              - New property: paid_balance
              - Modified property: withdrawable_balance
                - Description changed from 'Part of the credit that may leave the platform via payouts or
transfers: earnings-typed ledger inflows minus outflows, capped by
the current credit value so that staff-granted (promotional) credit
is never withdrawable and credit expiry wipes earnings too.' to 'Part of the credit that may leave the platform via payouts or
transfers: what is left of the earned lots. Granted and paid
credit is never withdrawable, and spending earnings on usage lowers
it for good, however much credit is granted afterwards.'

HEAD /api/customer-credits/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/customer-credits/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: granted_balance
            - New required property: paid_balance
          - Properties changed
            - New property: granted_balance
            - New property: paid_balance
            - Modified property: withdrawable_balance
              - Description changed from 'Part of the credit that may leave the platform via payouts or
transfers: earnings-typed ledger inflows minus outflows, capped by
the current credit value so that staff-granted (promotional) credit
is never withdrawable and credit expiry wipes earnings too.' to 'Part of the credit that may leave the platform via payouts or
transfers: what is left of the earned lots. Granted and paid
credit is never withdrawable, and spending earnings on usage lowers
it for good, however much credit is granted afterwards.'

DELETE /api/customer-credits/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/customer-credits/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: granted_balance
            - New required property: paid_balance
          - Properties changed
            - New property: granted_balance
            - New property: paid_balance
            - Modified property: withdrawable_balance
              - Description changed from 'Part of the credit that may leave the platform via payouts or
transfers: earnings-typed ledger inflows minus outflows, capped by
the current credit value so that staff-granted (promotional) credit
is never withdrawable and credit expiry wipes earnings too.' to 'Part of the credit that may leave the platform via payouts or
transfers: what is left of the earned lots. Granted and paid
credit is never withdrawable, and spending earnings on usage lowers
it for good, however much credit is granted afterwards.'

PATCH /api/customer-credits/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: granted_balance
            - New required property: paid_balance
          - Properties changed
            - New property: granted_balance
            - New property: paid_balance
            - Modified property: withdrawable_balance
              - Description changed from 'Part of the credit that may leave the platform via payouts or
transfers: earnings-typed ledger inflows minus outflows, capped by
the current credit value so that staff-granted (promotional) credit
is never withdrawable and credit expiry wipes earnings too.' to 'Part of the credit that may leave the platform via payouts or
transfers: what is left of the earned lots. Granted and paid
credit is never withdrawable, and spending earnings on usage lowers
it for good, however much credit is granted afterwards.'

PUT /api/customer-credits/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: granted_balance
            - New required property: paid_balance
          - Properties changed
            - New property: granted_balance
            - New property: paid_balance
            - Modified property: withdrawable_balance
              - Description changed from 'Part of the credit that may leave the platform via payouts or
transfers: earnings-typed ledger inflows minus outflows, capped by
the current credit value so that staff-granted (promotional) credit
is never withdrawable and credit expiry wipes earnings too.' to 'Part of the credit that may leave the platform via payouts or
transfers: what is left of the earned lots. Granted and paid
credit is never withdrawable, and spending earnings on usage lowers
it for good, however much credit is granted afterwards.'

POST /api/customer-credits/{uuid}/adjust_withdrawable/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: granted_balance
            - New required property: paid_balance
          - Properties changed
            - New property: granted_balance
            - New property: paid_balance
            - Modified property: withdrawable_balance
              - Description changed from 'Part of the credit that may leave the platform via payouts or
transfers: earnings-typed ledger inflows minus outflows, capped by
the current credit value so that staff-granted (promotional) credit
is never withdrawable and credit expiry wipes earnings too.' to 'Part of the credit that may leave the platform via payouts or
transfers: what is left of the earned lots. Granted and paid
credit is never withdrawable, and spending earnings on usage lowers
it for good, however much credit is granted afterwards.'

POST /api/customer-credits/{uuid}/apply_compensations/

- Extensions changed
  - New extension: x-permissions

POST /api/customer-credits/{uuid}/clear_compensations/

- Extensions changed
  - New extension: x-permissions

GET /api/customer-credits/{uuid}/consumptions/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/customer-permissions-reviews/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/customer-permissions-reviews/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/customer-permissions-reviews/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/customer-permissions-reviews/{uuid}/close/

- Extensions changed
  - New extension: x-permissions

GET /api/customer-quotas/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/customer-quotas/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/customer-role-concealments/

- Extensions changed
  - New extension: x-permissions

HEAD /api/customer-role-concealments/

- Extensions changed
  - New extension: x-permissions

POST /api/customer-role-concealments/

- Extensions changed
  - New extension: x-permissions

DELETE /api/customer-role-concealments/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/customer-role-concealments/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/customers/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Description changed from 'Retrieve a list of customers. The list is filtered based on the user's permissions. A user whose only link to an organization is a role on its service provider sees it with a restricted field set: url, uuid, name, native_name, display_name, abbreviation, slug, image, country, country_name, is_service_provider, service_provider and service_provider_uuid. All other fields are omitted for that row.' to 'Retrieve a list of customers. The list is filtered based on the user's permissions. A user whose only link to an organization is a role on its service provider sees it with a restricted field set: url, uuid, name, native_name, display_name, abbreviation, slug, image, country, country_name, is_service_provider, service_provider and service_provider_uuid. All other fields are omitted for that row. Except to staff and support, an organization that limits portal access to some networks is hidden from callers outside them; only a user whose sole link to it is a service provider role still finds it, with the restricted field set.'
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [invoice_emails is_private_person user_assurance_levels user_nationalities user_organization_types vat_code_verified vat_percent vat_rule]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: invoice_emails
              - New property: is_private_person
              - New property: user_assurance_levels
              - New property: user_nationalities
              - New property: user_organization_types
              - New property: vat_code_verified
              - New property: vat_percent
              - New property: vat_rule

HEAD /api/customers/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/customers/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: invoice_emails
          - New property: is_private_person
          - New property: user_assurance_levels
          - New property: user_nationalities
          - New property: user_organization_types
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: invoice_emails
          - New property: is_private_person
          - New property: user_assurance_levels
          - New property: user_nationalities
          - New property: user_organization_types
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: invoice_emails
          - New property: is_private_person
          - New property: user_assurance_levels
          - New property: user_nationalities
          - New property: user_organization_types
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: invoice_emails
            - New property: is_private_person
            - New property: user_assurance_levels
            - New property: user_nationalities
            - New property: user_organization_types
            - New property: vat_code_verified
            - New property: vat_percent
            - New property: vat_rule

GET /api/customers/countries/

- Extensions changed
  - New extension: x-permissions

HEAD /api/customers/countries/

- Extensions changed
  - New extension: x-permissions

GET /api/customers/{customer_uuid}/project-metadata-compliance-details/

- Extensions changed
  - New extension: x-permissions

HEAD /api/customers/{customer_uuid}/project-metadata-compliance-details/

- Extensions changed
  - New extension: x-permissions

GET /api/customers/{customer_uuid}/project-metadata-compliance-overview/

- Extensions changed
  - New extension: x-permissions

HEAD /api/customers/{customer_uuid}/project-metadata-compliance-overview/

- Extensions changed
  - New extension: x-permissions

GET /api/customers/{customer_uuid}/project-metadata-compliance-projects/

- Extensions changed
  - New extension: x-permissions

HEAD /api/customers/{customer_uuid}/project-metadata-compliance-projects/

- Extensions changed
  - New extension: x-permissions

GET /api/customers/{customer_uuid}/project-metadata-question-answers/

- Extensions changed
  - New extension: x-permissions

HEAD /api/customers/{customer_uuid}/project-metadata-question-answers/

- Extensions changed
  - New extension: x-permissions

GET /api/customers/{customer_uuid}/users/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/customers/{customer_uuid}/users/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

DELETE /api/customers/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/customers/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [invoice_emails is_private_person user_assurance_levels user_nationalities user_organization_types vat_code_verified vat_percent vat_rule]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: invoice_emails
            - New property: is_private_person
            - New property: user_assurance_levels
            - New property: user_nationalities
            - New property: user_organization_types
            - New property: vat_code_verified
            - New property: vat_percent
            - New property: vat_rule

PATCH /api/customers/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: invoice_emails
          - New property: is_private_person
          - New property: user_assurance_levels
          - New property: user_nationalities
          - New property: user_organization_types
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: invoice_emails
          - New property: is_private_person
          - New property: user_assurance_levels
          - New property: user_nationalities
          - New property: user_organization_types
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: invoice_emails
          - New property: is_private_person
          - New property: user_assurance_levels
          - New property: user_nationalities
          - New property: user_organization_types
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: invoice_emails
            - New property: is_private_person
            - New property: user_assurance_levels
            - New property: user_nationalities
            - New property: user_organization_types
            - New property: vat_code_verified
            - New property: vat_percent
            - New property: vat_rule

PUT /api/customers/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: invoice_emails
          - New property: is_private_person
          - New property: user_assurance_levels
          - New property: user_nationalities
          - New property: user_organization_types
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: invoice_emails
          - New property: is_private_person
          - New property: user_assurance_levels
          - New property: user_nationalities
          - New property: user_organization_types
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: invoice_emails
          - New property: is_private_person
          - New property: user_assurance_levels
          - New property: user_nationalities
          - New property: user_organization_types
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: invoice_emails
            - New property: is_private_person
            - New property: user_assurance_levels
            - New property: user_nationalities
            - New property: user_organization_types
            - New property: vat_code_verified
            - New property: vat_percent
            - New property: vat_rule

POST /api/customers/{uuid}/add_user/

- Extensions changed
  - New extension: x-permissions

POST /api/customers/{uuid}/contact/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: invoice_emails
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: invoice_emails

POST /api/customers/{uuid}/delete_user/

- Extensions changed
  - New extension: x-permissions

GET /api/customers/{uuid}/history/

- Extensions changed
  - New extension: x-permissions

GET /api/customers/{uuid}/history/at/

- Extensions changed
  - New extension: x-permissions

GET /api/customers/{uuid}/list_users/

- Extensions changed
  - New extension: x-permissions
- New query param: role_template

HEAD /api/customers/{uuid}/list_users/

- Extensions changed
  - New extension: x-permissions
- New query param: role_template

GET /api/customers/{uuid}/project-digest-config/

- Extensions changed
  - New extension: x-permissions

POST /api/customers/{uuid}/project-digest-config/preview/

- Extensions changed
  - New extension: x-permissions

POST /api/customers/{uuid}/project-digest-config/send-test/

- Extensions changed
  - New extension: x-permissions

GET /api/customers/{uuid}/providers/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: account_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/ProviderAccountOptions
                    - Properties changed
                      - Modified property: account_scope
                        - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'

GET /api/customers/{uuid}/stats/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/customers/{uuid}/update-project-digest-config/

- Extensions changed
  - New extension: x-permissions

PUT /api/customers/{uuid}/update-project-digest-config/

- Extensions changed
  - New extension: x-permissions

POST /api/customers/{uuid}/update_default_affiliations/

- Extensions changed
  - New extension: x-permissions

POST /api/customers/{uuid}/update_organization_groups/

- Extensions changed
  - New extension: x-permissions

POST /api/customers/{uuid}/update_user/

- Extensions changed
  - New extension: x-permissions

GET /api/daily-quotas/

- Extensions changed
  - New extension: x-permissions
- Modified query param: scope
  - Description changed from 'UUID of the scope object' to 'URL of the project or organization'
  - Required changed from false to true
  - Schema changed
    - Format changed from 'uuid' to 'uri'

GET /api/data-access-logs/

- Extensions changed
  - New extension: x-permissions

HEAD /api/data-access-logs/

- Extensions changed
  - New extension: x-permissions

DELETE /api/data-access-logs/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/data-access-logs/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/database-stats/

- Extensions changed
  - New extension: x-permissions

GET /api/debug/email/config/

- Extensions changed
  - New extension: x-permissions

POST /api/debug/email/probe/

- Extensions changed
  - New extension: x-permissions

POST /api/debug/email/send_test/

- Extensions changed
  - New extension: x-permissions

GET /api/debug/pubsub/circuit_breaker/

- Extensions changed
  - New extension: x-permissions

POST /api/debug/pubsub/circuit_breaker_reset/

- Extensions changed
  - New extension: x-permissions

GET /api/debug/pubsub/dead_letter_queue/

- Extensions changed
  - New extension: x-permissions

GET /api/debug/pubsub/message_state_cache/

- Extensions changed
  - New extension: x-permissions

GET /api/debug/pubsub/metrics/

- Extensions changed
  - New extension: x-permissions

POST /api/debug/pubsub/metrics_reset/

- Extensions changed
  - New extension: x-permissions

GET /api/debug/pubsub/overview/

- Extensions changed
  - New extension: x-permissions

GET /api/debug/pubsub/queues/

- Extensions changed
  - New extension: x-permissions

GET /api/digitalocean-droplets/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/digitalocean-droplets/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/digitalocean-droplets/

- Extensions changed
  - New extension: x-permissions

DELETE /api/digitalocean-droplets/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/digitalocean-droplets/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/digitalocean-droplets/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/digitalocean-droplets/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/digitalocean-droplets/{uuid}/pull/

- Extensions changed
  - New extension: x-permissions

POST /api/digitalocean-droplets/{uuid}/resize/

- Extensions changed
  - New extension: x-permissions

POST /api/digitalocean-droplets/{uuid}/restart/

- Extensions changed
  - New extension: x-permissions

POST /api/digitalocean-droplets/{uuid}/set_erred/

- Extensions changed
  - New extension: x-permissions

POST /api/digitalocean-droplets/{uuid}/set_ok/

- Extensions changed
  - New extension: x-permissions

POST /api/digitalocean-droplets/{uuid}/start/

- Extensions changed
  - New extension: x-permissions

POST /api/digitalocean-droplets/{uuid}/stop/

- Extensions changed
  - New extension: x-permissions

POST /api/digitalocean-droplets/{uuid}/unlink/

- Extensions changed
  - New extension: x-permissions

GET /api/digitalocean-images/

- Extensions changed
  - New extension: x-permissions

HEAD /api/digitalocean-images/

- Extensions changed
  - New extension: x-permissions

GET /api/digitalocean-images/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/digitalocean-regions/

- Extensions changed
  - New extension: x-permissions

HEAD /api/digitalocean-regions/

- Extensions changed
  - New extension: x-permissions

GET /api/digitalocean-regions/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/digitalocean-sizes/

- Extensions changed
  - New extension: x-permissions

HEAD /api/digitalocean-sizes/

- Extensions changed
  - New extension: x-permissions

GET /api/digitalocean-sizes/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/email-logs/

- Extensions changed
  - New extension: x-permissions

HEAD /api/email-logs/

- Extensions changed
  - New extension: x-permissions

GET /api/email-logs/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/event-consumers/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- New query param: delivery
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: delivery
              - New required property: ephemeral
              - New required property: last_delivered_at
              - New required property: last_error
              - New required property: last_error_at
              - New required property: payload_filters
              - New required property: unread_since
              - New required property: webhook_destination
            - Properties changed
              - New property: delivery
              - New property: ephemeral
              - New property: last_delivered_at
              - New property: last_error
              - New property: last_error_at
              - New property: payload_filters
              - New property: unread_since
              - New property: webhook_destination

HEAD /api/event-consumers/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- New query param: delivery

POST /api/event-consumers/register/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: ephemeral

DELETE /api/event-consumers/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/event-subscription-queues/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/event-subscription-queues/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

DELETE /api/event-subscription-queues/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/event-subscription-queues/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/event-subscriptions/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: source_ip
                - Property 'OneOf' changed
                  - Schemas deleted: subschema #1, subschema #2
                - Type changed from '' to 'string'
                - Format changed from '' to 'ipv4'
                - Description changed from 'An IPv4 or IPv6 address.' to ''

HEAD /api/event-subscriptions/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/event-subscriptions/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: source_ip
              - Property 'OneOf' changed
                - Schemas deleted: subschema #1, subschema #2
              - Type changed from '' to 'string'
              - Format changed from '' to 'ipv4'
              - Description changed from 'An IPv4 or IPv6 address.' to ''

DELETE /api/event-subscriptions/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/event-subscriptions/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: source_ip
              - Property 'OneOf' changed
                - Schemas deleted: subschema #1, subschema #2
              - Type changed from '' to 'string'
              - Format changed from '' to 'ipv4'
              - Description changed from 'An IPv4 or IPv6 address.' to ''

POST /api/event-subscriptions/{uuid}/create_queue/

- Extensions changed
  - New extension: x-permissions

GET /api/events-stats/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/events-stats/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/events/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/events/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/events/count/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/events/count/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/events/event_groups/

- Extensions changed
  - New extension: x-permissions

HEAD /api/events/event_groups/

- Extensions changed
  - New extension: x-permissions

GET /api/events/scope_types/

- Extensions changed
  - New extension: x-permissions

HEAD /api/events/scope_types/

- Extensions changed
  - New extension: x-permissions

GET /api/events/{id}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/expertise-categories/

- Extensions changed
  - New extension: x-permissions

HEAD /api/expertise-categories/

- Extensions changed
  - New extension: x-permissions

GET /api/expertise-categories/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/external-links/

- Extensions changed
  - New extension: x-permissions

HEAD /api/external-links/

- Extensions changed
  - New extension: x-permissions

POST /api/external-links/

- Extensions changed
  - New extension: x-permissions

DELETE /api/external-links/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/external-links/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/external-links/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/external-links/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/feature-values/

- Extensions changed
  - New extension: x-permissions

GET /api/financial-reports/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/financial-reports/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/financial-reports/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/freeipa-profiles/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/freeipa-profiles/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/freeipa-profiles/

- Extensions changed
  - New extension: x-permissions

GET /api/freeipa-profiles/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

PATCH /api/freeipa-profiles/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/freeipa-profiles/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/freeipa-profiles/{uuid}/update_ssh_keys/

- Extensions changed
  - New extension: x-permissions

GET /api/helpdesk-health/

- Extensions changed
  - New extension: x-permissions

GET /api/helpdesk-stats/

- Extensions changed
  - New extension: x-permissions

GET /api/hooks-email/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: event_groups
                - Items changed
                  - New enum values: [admin policies]
              - Modified property: event_types
                - Items changed
                  - New enum values: [admin_object_created admin_object_deleted admin_object_updated auth_logged_in_with_valimo auth_logged_in_to_admin_site auth_login_failed_with_oauth auth_login_failed_with_saml2 auth_login_failed_with_valimo auth_login_failed_to_admin_site credit_reclassified_as_paid credit_topped_up granted_credit_expired marketplace_offering_deleted marketplace_resource_spending_limits_updated policy_created policy_deleted policy_updated resource_hard_reboot_failed resource_hard_reboot_scheduled resource_hard_reboot_succeeded token_viewed user_terms_of_service_accepted feedback_survey_answered oidc_token_revoked oidc_token_refresh_failed event_consumer_webhook_updated event_consumer_resync_requested]

HEAD /api/hooks-email/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/hooks-email/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_groups
            - Items changed
              - New enum values: [admin policies]
          - Modified property: event_types
            - Items changed
              - New enum values: [admin_object_created admin_object_deleted admin_object_updated auth_logged_in_with_valimo auth_logged_in_to_admin_site auth_login_failed_with_oauth auth_login_failed_with_saml2 auth_login_failed_with_valimo auth_login_failed_to_admin_site credit_reclassified_as_paid credit_topped_up granted_credit_expired marketplace_offering_deleted marketplace_resource_spending_limits_updated policy_created policy_deleted policy_updated resource_hard_reboot_failed resource_hard_reboot_scheduled resource_hard_reboot_succeeded token_viewed user_terms_of_service_accepted feedback_survey_answered oidc_token_revoked oidc_token_refresh_failed event_consumer_webhook_updated event_consumer_resync_requested]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [admin policies]
            - Modified property: event_types
              - Items changed
                - New enum values: [admin_object_created admin_object_deleted admin_object_updated auth_logged_in_with_valimo auth_logged_in_to_admin_site auth_login_failed_with_oauth auth_login_failed_with_saml2 auth_login_failed_with_valimo auth_login_failed_to_admin_site credit_reclassified_as_paid credit_topped_up granted_credit_expired marketplace_offering_deleted marketplace_resource_spending_limits_updated policy_created policy_deleted policy_updated resource_hard_reboot_failed resource_hard_reboot_scheduled resource_hard_reboot_succeeded token_viewed user_terms_of_service_accepted feedback_survey_answered oidc_token_revoked oidc_token_refresh_failed event_consumer_webhook_updated event_consumer_resync_requested]

DELETE /api/hooks-email/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/hooks-email/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [admin policies]
            - Modified property: event_types
              - Items changed
                - New enum values: [admin_object_created admin_object_deleted admin_object_updated auth_logged_in_with_valimo auth_logged_in_to_admin_site auth_login_failed_with_oauth auth_login_failed_with_saml2 auth_login_failed_with_valimo auth_login_failed_to_admin_site credit_reclassified_as_paid credit_topped_up granted_credit_expired marketplace_offering_deleted marketplace_resource_spending_limits_updated policy_created policy_deleted policy_updated resource_hard_reboot_failed resource_hard_reboot_scheduled resource_hard_reboot_succeeded token_viewed user_terms_of_service_accepted feedback_survey_answered oidc_token_revoked oidc_token_refresh_failed event_consumer_webhook_updated event_consumer_resync_requested]

PATCH /api/hooks-email/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_groups
            - Items changed
              - New enum values: [admin policies]
          - Modified property: event_types
            - Items changed
              - New enum values: [admin_object_created admin_object_deleted admin_object_updated auth_logged_in_with_valimo auth_logged_in_to_admin_site auth_login_failed_with_oauth auth_login_failed_with_saml2 auth_login_failed_with_valimo auth_login_failed_to_admin_site credit_reclassified_as_paid credit_topped_up granted_credit_expired marketplace_offering_deleted marketplace_resource_spending_limits_updated policy_created policy_deleted policy_updated resource_hard_reboot_failed resource_hard_reboot_scheduled resource_hard_reboot_succeeded token_viewed user_terms_of_service_accepted feedback_survey_answered oidc_token_revoked oidc_token_refresh_failed event_consumer_webhook_updated event_consumer_resync_requested]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [admin policies]
            - Modified property: event_types
              - Items changed
                - New enum values: [admin_object_created admin_object_deleted admin_object_updated auth_logged_in_with_valimo auth_logged_in_to_admin_site auth_login_failed_with_oauth auth_login_failed_with_saml2 auth_login_failed_with_valimo auth_login_failed_to_admin_site credit_reclassified_as_paid credit_topped_up granted_credit_expired marketplace_offering_deleted marketplace_resource_spending_limits_updated policy_created policy_deleted policy_updated resource_hard_reboot_failed resource_hard_reboot_scheduled resource_hard_reboot_succeeded token_viewed user_terms_of_service_accepted feedback_survey_answered oidc_token_revoked oidc_token_refresh_failed event_consumer_webhook_updated event_consumer_resync_requested]

PUT /api/hooks-email/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_groups
            - Items changed
              - New enum values: [admin policies]
          - Modified property: event_types
            - Items changed
              - New enum values: [admin_object_created admin_object_deleted admin_object_updated auth_logged_in_with_valimo auth_logged_in_to_admin_site auth_login_failed_with_oauth auth_login_failed_with_saml2 auth_login_failed_with_valimo auth_login_failed_to_admin_site credit_reclassified_as_paid credit_topped_up granted_credit_expired marketplace_offering_deleted marketplace_resource_spending_limits_updated policy_created policy_deleted policy_updated resource_hard_reboot_failed resource_hard_reboot_scheduled resource_hard_reboot_succeeded token_viewed user_terms_of_service_accepted feedback_survey_answered oidc_token_revoked oidc_token_refresh_failed event_consumer_webhook_updated event_consumer_resync_requested]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [admin policies]
            - Modified property: event_types
              - Items changed
                - New enum values: [admin_object_created admin_object_deleted admin_object_updated auth_logged_in_with_valimo auth_logged_in_to_admin_site auth_login_failed_with_oauth auth_login_failed_with_saml2 auth_login_failed_with_valimo auth_login_failed_to_admin_site credit_reclassified_as_paid credit_topped_up granted_credit_expired marketplace_offering_deleted marketplace_resource_spending_limits_updated policy_created policy_deleted policy_updated resource_hard_reboot_failed resource_hard_reboot_scheduled resource_hard_reboot_succeeded token_viewed user_terms_of_service_accepted feedback_survey_answered oidc_token_revoked oidc_token_refresh_failed event_consumer_webhook_updated event_consumer_resync_requested]

GET /api/hooks-web/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: event_groups
                - Items changed
                  - New enum values: [admin policies]
              - Modified property: event_types
                - Items changed
                  - New enum values: [admin_object_created admin_object_deleted admin_object_updated auth_logged_in_with_valimo auth_logged_in_to_admin_site auth_login_failed_with_oauth auth_login_failed_with_saml2 auth_login_failed_with_valimo auth_login_failed_to_admin_site credit_reclassified_as_paid credit_topped_up granted_credit_expired marketplace_offering_deleted marketplace_resource_spending_limits_updated policy_created policy_deleted policy_updated resource_hard_reboot_failed resource_hard_reboot_scheduled resource_hard_reboot_succeeded token_viewed user_terms_of_service_accepted feedback_survey_answered oidc_token_revoked oidc_token_refresh_failed event_consumer_webhook_updated event_consumer_resync_requested]

HEAD /api/hooks-web/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/hooks-web/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_groups
            - Items changed
              - New enum values: [admin policies]
          - Modified property: event_types
            - Items changed
              - New enum values: [admin_object_created admin_object_deleted admin_object_updated auth_logged_in_with_valimo auth_logged_in_to_admin_site auth_login_failed_with_oauth auth_login_failed_with_saml2 auth_login_failed_with_valimo auth_login_failed_to_admin_site credit_reclassified_as_paid credit_topped_up granted_credit_expired marketplace_offering_deleted marketplace_resource_spending_limits_updated policy_created policy_deleted policy_updated resource_hard_reboot_failed resource_hard_reboot_scheduled resource_hard_reboot_succeeded token_viewed user_terms_of_service_accepted feedback_survey_answered oidc_token_revoked oidc_token_refresh_failed event_consumer_webhook_updated event_consumer_resync_requested]
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [admin policies]
            - Modified property: event_types
              - Items changed
                - New enum values: [admin_object_created admin_object_deleted admin_object_updated auth_logged_in_with_valimo auth_logged_in_to_admin_site auth_login_failed_with_oauth auth_login_failed_with_saml2 auth_login_failed_with_valimo auth_login_failed_to_admin_site credit_reclassified_as_paid credit_topped_up granted_credit_expired marketplace_offering_deleted marketplace_resource_spending_limits_updated policy_created policy_deleted policy_updated resource_hard_reboot_failed resource_hard_reboot_scheduled resource_hard_reboot_succeeded token_viewed user_terms_of_service_accepted feedback_survey_answered oidc_token_revoked oidc_token_refresh_failed event_consumer_webhook_updated event_consumer_resync_requested]

DELETE /api/hooks-web/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/hooks-web/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [admin policies]
            - Modified property: event_types
              - Items changed
                - New enum values: [admin_object_created admin_object_deleted admin_object_updated auth_logged_in_with_valimo auth_logged_in_to_admin_site auth_login_failed_with_oauth auth_login_failed_with_saml2 auth_login_failed_with_valimo auth_login_failed_to_admin_site credit_reclassified_as_paid credit_topped_up granted_credit_expired marketplace_offering_deleted marketplace_resource_spending_limits_updated policy_created policy_deleted policy_updated resource_hard_reboot_failed resource_hard_reboot_scheduled resource_hard_reboot_succeeded token_viewed user_terms_of_service_accepted feedback_survey_answered oidc_token_revoked oidc_token_refresh_failed event_consumer_webhook_updated event_consumer_resync_requested]

PATCH /api/hooks-web/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_groups
            - Items changed
              - New enum values: [admin policies]
          - Modified property: event_types
            - Items changed
              - New enum values: [admin_object_created admin_object_deleted admin_object_updated auth_logged_in_with_valimo auth_logged_in_to_admin_site auth_login_failed_with_oauth auth_login_failed_with_saml2 auth_login_failed_with_valimo auth_login_failed_to_admin_site credit_reclassified_as_paid credit_topped_up granted_credit_expired marketplace_offering_deleted marketplace_resource_spending_limits_updated policy_created policy_deleted policy_updated resource_hard_reboot_failed resource_hard_reboot_scheduled resource_hard_reboot_succeeded token_viewed user_terms_of_service_accepted feedback_survey_answered oidc_token_revoked oidc_token_refresh_failed event_consumer_webhook_updated event_consumer_resync_requested]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [admin policies]
            - Modified property: event_types
              - Items changed
                - New enum values: [admin_object_created admin_object_deleted admin_object_updated auth_logged_in_with_valimo auth_logged_in_to_admin_site auth_login_failed_with_oauth auth_login_failed_with_saml2 auth_login_failed_with_valimo auth_login_failed_to_admin_site credit_reclassified_as_paid credit_topped_up granted_credit_expired marketplace_offering_deleted marketplace_resource_spending_limits_updated policy_created policy_deleted policy_updated resource_hard_reboot_failed resource_hard_reboot_scheduled resource_hard_reboot_succeeded token_viewed user_terms_of_service_accepted feedback_survey_answered oidc_token_revoked oidc_token_refresh_failed event_consumer_webhook_updated event_consumer_resync_requested]

PUT /api/hooks-web/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: event_groups
            - Items changed
              - New enum values: [admin policies]
          - Modified property: event_types
            - Items changed
              - New enum values: [admin_object_created admin_object_deleted admin_object_updated auth_logged_in_with_valimo auth_logged_in_to_admin_site auth_login_failed_with_oauth auth_login_failed_with_saml2 auth_login_failed_with_valimo auth_login_failed_to_admin_site credit_reclassified_as_paid credit_topped_up granted_credit_expired marketplace_offering_deleted marketplace_resource_spending_limits_updated policy_created policy_deleted policy_updated resource_hard_reboot_failed resource_hard_reboot_scheduled resource_hard_reboot_succeeded token_viewed user_terms_of_service_accepted feedback_survey_answered oidc_token_revoked oidc_token_refresh_failed event_consumer_webhook_updated event_consumer_resync_requested]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - Items changed
                - New enum values: [admin policies]
            - Modified property: event_types
              - Items changed
                - New enum values: [admin_object_created admin_object_deleted admin_object_updated auth_logged_in_with_valimo auth_logged_in_to_admin_site auth_login_failed_with_oauth auth_login_failed_with_saml2 auth_login_failed_with_valimo auth_login_failed_to_admin_site credit_reclassified_as_paid credit_topped_up granted_credit_expired marketplace_offering_deleted marketplace_resource_spending_limits_updated policy_created policy_deleted policy_updated resource_hard_reboot_failed resource_hard_reboot_scheduled resource_hard_reboot_succeeded token_viewed user_terms_of_service_accepted feedback_survey_answered oidc_token_revoked oidc_token_refresh_failed event_consumer_webhook_updated event_consumer_resync_requested]

GET /api/hooks/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/hooks/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/identity-bridge/

- Extensions changed
  - New extension: x-permissions
- Description changed from 'Allows Identity Service Domains (ISDs) to push user attributes to Waldur. Creates or updates a user based on username (CUID). Requires FEDERATED_IDENTITY_SYNC_ENABLED to be True. Caller must be staff or an identity manager with the declared source in managed_isds.' to 'Allows Identity Service Domains (ISDs) to push user attributes to Waldur. Creates or updates a user based on username (CUID). Requires FEDERATED_IDENTITY_SYNC_ENABLED to be True. Caller must be staff or an identity manager with the declared source in managed_isds. Only staff may push staff, support or identity manager accounts.'

GET /api/identity-bridge/allowed-fields/

- Extensions changed
  - New extension: x-permissions

POST /api/identity-bridge/remove/

- Extensions changed
  - New extension: x-permissions
- Description changed from 'Signals that a user has been removed from an ISD. Removes the source from active_isds, clears attributes owned by that source, and deactivates the user if no ISDs remain (configurable via FEDERATED_IDENTITY_DEACTIVATION_POLICY). Requires FEDERATED_IDENTITY_SYNC_ENABLED to be True. Caller must be staff or an identity manager with the declared source in managed_isds.' to 'Signals that a user has been removed from an ISD. Removes the source from active_isds, clears attributes owned by that source, and deactivates the user if no ISDs remain (configurable via FEDERATED_IDENTITY_DEACTIVATION_POLICY). Requires FEDERATED_IDENTITY_SYNC_ENABLED to be True. Caller must be staff or an identity manager with the declared source in managed_isds. Only staff may remove staff, support or identity manager accounts. A user who is not in the source ISD is answered with 404 and left unchanged.'

GET /api/identity-bridge/stats/

- Extensions changed
  - New extension: x-permissions

GET /api/identity-providers/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: issuer
              - New required property: jwks_url
            - Properties changed
              - New property: issuer
              - New property: jwks_url
              - Modified property: client_secret
                - MaxLength changed from 200 to null

HEAD /api/identity-providers/

- Extensions changed
  - New extension: x-permissions

POST /api/identity-providers/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: client_secret
        - Properties changed
          - Modified property: client_secret
            - MaxLength changed from 200 to null
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: issuer
            - New required property: jwks_url
          - Properties changed
            - New property: issuer
            - New property: jwks_url
            - Modified property: client_secret
              - MaxLength changed from 200 to null

POST /api/identity-providers/discover_metadata/

- Extensions changed
  - New extension: x-permissions

POST /api/identity-providers/generate-mapping/

- Extensions changed
  - New extension: x-permissions

DELETE /api/identity-providers/{provider}/

- Extensions changed
  - New extension: x-permissions

GET /api/identity-providers/{provider}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: issuer
            - New required property: jwks_url
          - Properties changed
            - New property: issuer
            - New property: jwks_url
            - Modified property: client_secret
              - MaxLength changed from 200 to null

PATCH /api/identity-providers/{provider}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: client_secret
            - MaxLength changed from 200 to null
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: issuer
            - New required property: jwks_url
          - Properties changed
            - New property: issuer
            - New property: jwks_url
            - Modified property: client_secret
              - MaxLength changed from 200 to null

PUT /api/identity-providers/{provider}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: client_secret
        - Properties changed
          - Modified property: client_secret
            - MaxLength changed from 200 to null
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: issuer
            - New required property: jwks_url
          - Properties changed
            - New property: issuer
            - New property: jwks_url
            - Modified property: client_secret
              - MaxLength changed from 200 to null

GET /api/invoice-items/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/invoice-items/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/invoice-items/costs/

- Extensions changed
  - New extension: x-permissions

HEAD /api/invoice-items/costs/

- Extensions changed
  - New extension: x-permissions

GET /api/invoice-items/customer_costs_for_period/

- Extensions changed
  - New extension: x-permissions

HEAD /api/invoice-items/customer_costs_for_period/

- Extensions changed
  - New extension: x-permissions

GET /api/invoice-items/project_costs_for_period/

- Extensions changed
  - New extension: x-permissions

HEAD /api/invoice-items/project_costs_for_period/

- Extensions changed
  - New extension: x-permissions

GET /api/invoice-items/total_price/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/invoice-items/total_price/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

DELETE /api/invoice-items/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/invoice-items/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/invoice-items/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/invoice-items/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/invoice-items/{uuid}/consumptions/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/invoice-items/{uuid}/create_compensation/

- Extensions changed
  - New extension: x-permissions

POST /api/invoice-items/{uuid}/migrate_to/

- Extensions changed
  - New extension: x-permissions

POST /api/invoice/send-financial-report-by-mail/

- Extensions changed
  - New extension: x-permissions

GET /api/invoices/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [volume_discounts]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: volume_discounts

HEAD /api/invoices/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/invoices/growth/

- Extensions changed
  - New extension: x-permissions

HEAD /api/invoices/growth/

- Extensions changed
  - New extension: x-permissions

POST /api/invoices/import_usage/

- Extensions changed
  - New extension: x-permissions

GET /api/invoices/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [volume_discounts]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: volume_discounts

GET /api/invoices/{uuid}/history/

- Extensions changed
  - New extension: x-permissions

GET /api/invoices/{uuid}/history/at/

- Extensions changed
  - New extension: x-permissions

GET /api/invoices/{uuid}/items/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/invoices/{uuid}/paid/

- Extensions changed
  - New extension: x-permissions

POST /api/invoices/{uuid}/send_notification/

- Extensions changed
  - New extension: x-permissions

POST /api/invoices/{uuid}/set_backend_id/

- Extensions changed
  - New extension: x-permissions

POST /api/invoices/{uuid}/set_payment_url/

- Extensions changed
  - New extension: x-permissions

POST /api/invoices/{uuid}/set_reference_number/

- Extensions changed
  - New extension: x-permissions

GET /api/invoices/{uuid}/stats/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/keycloak-groups/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/keycloak-groups/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/keycloak-groups/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/keycloak-user-group-memberships/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/keycloak-user-group-memberships/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/keycloak-user-group-memberships/

- Extensions changed
  - New extension: x-permissions

DELETE /api/keycloak-user-group-memberships/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/keycloak-user-group-memberships/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/keys/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/keys/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/keys/

- Extensions changed
  - New extension: x-permissions

DELETE /api/keys/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/keys/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/keys/{uuid}/history/

- Extensions changed
  - New extension: x-permissions

GET /api/keys/{uuid}/history/at/

- Extensions changed
  - New extension: x-permissions

GET /api/lexis-links/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: heappe_project_id
            - Properties changed
              - Modified property: heappe_project_id
                - ReadOnly changed from false to true
                - Min changed from 0 to null
                - Max changed from 2.147483647e+09 to null

HEAD /api/lexis-links/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/lexis-links/

- Extensions changed
  - New extension: x-permissions

DELETE /api/lexis-links/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/lexis-links/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: heappe_project_id
          - Properties changed
            - Modified property: heappe_project_id
              - ReadOnly changed from false to true
              - Min changed from 0 to null
              - Max changed from 2.147483647e+09 to null

GET /api/maintenance-announcement-offerings/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: affected_partitions

HEAD /api/maintenance-announcement-offerings/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/maintenance-announcement-offerings/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: affected_partitions
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: affected_partitions

DELETE /api/maintenance-announcement-offerings/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/maintenance-announcement-offerings/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: affected_partitions

PATCH /api/maintenance-announcement-offerings/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: affected_partitions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: affected_partitions

PUT /api/maintenance-announcement-offerings/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: affected_partitions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: affected_partitions

GET /api/maintenance-announcement-template-offerings/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/maintenance-announcement-template-offerings/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/maintenance-announcement-template-offerings/

- Extensions changed
  - New extension: x-permissions

DELETE /api/maintenance-announcement-template-offerings/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/maintenance-announcement-template-offerings/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/maintenance-announcement-template-offerings/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

PUT /api/maintenance-announcement-template-offerings/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/maintenance-announcements-template/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/maintenance-announcements-template/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/maintenance-announcements-template/

- Extensions changed
  - New extension: x-permissions

DELETE /api/maintenance-announcements-template/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/maintenance-announcements-template/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/maintenance-announcements-template/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

PUT /api/maintenance-announcements-template/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/maintenance-announcements/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- New query param: offering_uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: affected_offerings
                - Items changed
                  - Properties changed
                    - New property: affected_partitions

HEAD /api/maintenance-announcements/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- New query param: offering_uuid

POST /api/maintenance-announcements/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: affected_offerings
              - Items changed
                - Properties changed
                  - New property: affected_partitions

GET /api/maintenance-announcements/maintenance_stats/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/maintenance-announcements/maintenance_stats/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

DELETE /api/maintenance-announcements/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/maintenance-announcements/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: affected_offerings
              - Items changed
                - Properties changed
                  - New property: affected_partitions

PATCH /api/maintenance-announcements/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: affected_offerings
              - Items changed
                - Properties changed
                  - New property: affected_partitions

PUT /api/maintenance-announcements/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: affected_offerings
              - Items changed
                - Properties changed
                  - New property: affected_partitions

POST /api/maintenance-announcements/{uuid}/cancel_maintenance/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/maintenance-announcements/{uuid}/complete_maintenance/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/maintenance-announcements/{uuid}/schedule/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/maintenance-announcements/{uuid}/start_maintenance/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/maintenance-announcements/{uuid}/unschedule/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/managed-rancher-cluster-resources/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [display_limits prepaid_total_component_types spending_limit_status spending_limits terminated_at usage_limit_resumes_at]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: display_limits
              - New property: prepaid_total_component_types
              - New property: spending_limit_status
              - New property: spending_limits
              - New property: terminated_at
              - New property: usage_limit_resumes_at
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Deleted property: callback_url
              - Modified property: endpoints
                - Items changed
                  - Properties changed
                    - Modified property: url
                      - Format changed from '' to 'uri'
                      - MaxLength changed from null to 200
              - Modified property: offering_components
                - Items changed
                  - Properties changed
                    - New property: spending_limit_periods
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Deleted property: callback_url

HEAD /api/managed-rancher-cluster-resources/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/managed-rancher-cluster-resources/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [display_limits prepaid_total_component_types spending_limit_status spending_limits terminated_at usage_limit_resumes_at]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: display_limits
            - New property: prepaid_total_component_types
            - New property: spending_limit_status
            - New property: spending_limits
            - New property: terminated_at
            - New property: usage_limit_resumes_at
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: callback_url
            - Modified property: endpoints
              - Items changed
                - Properties changed
                  - Modified property: url
                    - Format changed from '' to 'uri'
                    - MaxLength changed from null to 200
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: spending_limit_periods
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: callback_url

POST /api/managed-rancher-cluster-resources/{uuid}/add_node/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-article-code-update/apply/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-article-code-update/preview/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-attribute-options/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-attribute-options/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-attribute-options/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-attribute-options/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-attribute-options/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/marketplace-attribute-options/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/marketplace-attribute-options/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-attributes/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-attributes/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-attributes/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-attributes/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-attributes/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/marketplace-attributes/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/marketplace-attributes/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-bookings/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-categories/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: columns
                - Items changed
                  - Properties changed
                    - Modified property: widget
                      - Description changed from 'Widget field allows to customise table cell rendering.' to 'Widget field allows to customize table cell rendering.'

HEAD /api/marketplace-categories/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-categories/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: columns
              - Items changed
                - Properties changed
                  - Modified property: widget
                    - Description changed from 'Widget field allows to customise table cell rendering.' to 'Widget field allows to customize table cell rendering.'

DELETE /api/marketplace-categories/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-categories/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: columns
              - Items changed
                - Properties changed
                  - Modified property: widget
                    - Description changed from 'Widget field allows to customise table cell rendering.' to 'Widget field allows to customize table cell rendering.'

PATCH /api/marketplace-categories/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: columns
              - Items changed
                - Properties changed
                  - Modified property: widget
                    - Description changed from 'Widget field allows to customise table cell rendering.' to 'Widget field allows to customize table cell rendering.'

PUT /api/marketplace-categories/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: columns
              - Items changed
                - Properties changed
                  - Modified property: widget
                    - Description changed from 'Widget field allows to customise table cell rendering.' to 'Widget field allows to customize table cell rendering.'

GET /api/marketplace-category-columns/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: widget
                - Description changed from 'Widget field allows to customise table cell rendering.' to 'Widget field allows to customize table cell rendering.'

HEAD /api/marketplace-category-columns/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-category-columns/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: widget
            - Description changed from 'Widget field allows to customise table cell rendering.' to 'Widget field allows to customize table cell rendering.'
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: widget
              - Description changed from 'Widget field allows to customise table cell rendering.' to 'Widget field allows to customize table cell rendering.'

DELETE /api/marketplace-category-columns/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-category-columns/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: widget
              - Description changed from 'Widget field allows to customise table cell rendering.' to 'Widget field allows to customize table cell rendering.'

PATCH /api/marketplace-category-columns/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: widget
            - Description changed from 'Widget field allows to customise table cell rendering.' to 'Widget field allows to customize table cell rendering.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: widget
              - Description changed from 'Widget field allows to customise table cell rendering.' to 'Widget field allows to customize table cell rendering.'

PUT /api/marketplace-category-columns/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: widget
            - Description changed from 'Widget field allows to customise table cell rendering.' to 'Widget field allows to customize table cell rendering.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: widget
              - Description changed from 'Widget field allows to customise table cell rendering.' to 'Widget field allows to customize table cell rendering.'

GET /api/marketplace-category-component-usages/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/marketplace-category-component-usages/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/marketplace-category-component-usages/{id}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/marketplace-category-components/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-category-components/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-category-components/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-category-components/{id}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-category-components/{id}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/marketplace-category-components/{id}/

- Extensions changed
  - New extension: x-permissions

PUT /api/marketplace-category-components/{id}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-category-groups/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-category-groups/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-category-groups/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-category-groups/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-category-groups/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/marketplace-category-groups/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/marketplace-category-groups/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-category-help-articles/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-category-help-articles/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-category-help-articles/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-category-help-articles/{id}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-category-help-articles/{id}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/marketplace-category-help-articles/{id}/

- Extensions changed
  - New extension: x-permissions

PUT /api/marketplace-category-help-articles/{id}/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-chat/click/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-chat/feedback/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-chat/stream/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-component-usage-monthly/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/marketplace-component-usage-monthly/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/marketplace-component-usages/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/marketplace-component-usages/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/marketplace-component-usages/set_usage/

- Extensions changed
  - New extension: x-permissions
- Description changed from '
        Allows a service provider to report usage for one or more components of a specific resource.
        This endpoint is typically used by backend systems or agents to submit periodic usage data.

        - If a `plan_period` is provided, the usage is associated with that period.
        - If only a `resource` is provided, the system will determine the correct plan period based on the current date.
        - If a usage record for the same resource, component, and billing period already exists, it will be updated. Otherwise, a new record is created.
        ' to '
        Allows a service provider to report usage for one or more components of a specific resource.
        This endpoint is typically used by backend systems or agents to submit periodic usage data.

        - If a `plan_period` is provided, the usage is associated with that period.
        - If only a `resource` is provided, the system will determine the correct plan period based on the current date.
        - If a usage record for the same resource, component, and billing period already exists, it will be updated. Otherwise, a new record is created.
        - Usage-based components may be reported per UTC date in `daily_usages`. Each date replaces its previous amount, and the month's usage becomes the sum of its days. A month total for a month that has daily amounts is rejected. Day and week spending limits need daily amounts.
        '
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: daily_usages
          - Modified property: usages
            - Description changed from 'List of component usage items to report' to 'List of component usage items to report, each the total of the billing month so far. May be empty when daily_usages is given.'
      - Examples changed
        - New example: ReportUsagePerDay

GET /api/marketplace-component-usages/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/marketplace-component-usages/{uuid}/set_user_usage/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-component-usages/{uuid}/set_user_usages/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-component-user-usages/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/marketplace-component-user-usages/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/marketplace-component-user-usages/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/marketplace-course-accounts/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/marketplace-course-accounts/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/marketplace-course-accounts/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-course-accounts/create_bulk/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-course-accounts/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-course-accounts/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/marketplace-course-accounts/{uuid}/retry/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-customer-component-usage-policies/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/marketplace-customer-component-usage-policies/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/marketplace-customer-component-usage-policies/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-customer-component-usage-policies/actions/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-customer-component-usage-policies/actions/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-customer-component-usage-policies/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-customer-component-usage-policies/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/marketplace-customer-component-usage-policies/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/marketplace-customer-component-usage-policies/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-customer-estimated-cost-policies/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [cost_breakdown trigger_status]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: cost_breakdown
              - New property: trigger_status
              - Modified property: current_cost
                - Description changed from 'The cost this policy compares against limit_cost right now: the period's invoice total, less the credit already applied and the credit still to be drawn. Do not re-derive it — only the server can simulate the pending draw, and a figure computed from the invoice alone will not match what the policy evaluates.' to 'The cost this policy compares against limit_cost right now: the period's invoice total, less the credit already applied and the credit still to be drawn, or the full cost for a policy that does not take credit into account. Do not re-derive it — only the server can simulate the pending draw, and a figure computed from the invoice alone will not match what the policy evaluates.'
              - Modified property: eta_days
                - Description changed from 'Days until the policy fires, or null when no projection exists. 0 means the threshold is already crossed and the policy is triggered — measured, not projected. Null must be rendered as no date, never as 'now': it is the common case, and it is also what an unprojectable or more-than-a-year-away policy reports. Nothing is projected beyond 365 days, because the rate comes from the current month's spend. Note that a cost policy does not fire on cost alone — it also waits for the credit balance to fall to limit_cost — so a policy far over its cap can still report a future date or null.' to 'Days until the policy fires, or null when no projection exists. 0 means the threshold is already crossed and the policy is triggered — measured, not projected. Null must be rendered as no date, never as 'now': it is the common case, and it is also what an unprojectable or more-than-a-year-away policy reports. Nothing is projected beyond 365 days, because the rate comes from the current month's spend.'

HEAD /api/marketplace-customer-estimated-cost-policies/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/marketplace-customer-estimated-cost-policies/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: cost_breakdown
            - New property: trigger_status
            - Modified property: current_cost
              - Description changed from 'The cost this policy compares against limit_cost right now: the period's invoice total, less the credit already applied and the credit still to be drawn. Do not re-derive it — only the server can simulate the pending draw, and a figure computed from the invoice alone will not match what the policy evaluates.' to 'The cost this policy compares against limit_cost right now: the period's invoice total, less the credit already applied and the credit still to be drawn, or the full cost for a policy that does not take credit into account. Do not re-derive it — only the server can simulate the pending draw, and a figure computed from the invoice alone will not match what the policy evaluates.'
            - Modified property: eta_days
              - Description changed from 'Days until the policy fires, or null when no projection exists. 0 means the threshold is already crossed and the policy is triggered — measured, not projected. Null must be rendered as no date, never as 'now': it is the common case, and it is also what an unprojectable or more-than-a-year-away policy reports. Nothing is projected beyond 365 days, because the rate comes from the current month's spend. Note that a cost policy does not fire on cost alone — it also waits for the credit balance to fall to limit_cost — so a policy far over its cap can still report a future date or null.' to 'Days until the policy fires, or null when no projection exists. 0 means the threshold is already crossed and the policy is triggered — measured, not projected. Null must be rendered as no date, never as 'now': it is the common case, and it is also what an unprojectable or more-than-a-year-away policy reports. Nothing is projected beyond 365 days, because the rate comes from the current month's spend.'

GET /api/marketplace-customer-estimated-cost-policies/actions/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-customer-estimated-cost-policies/actions/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-customer-estimated-cost-policies/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-customer-estimated-cost-policies/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [cost_breakdown trigger_status]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: cost_breakdown
            - New property: trigger_status
            - Modified property: current_cost
              - Description changed from 'The cost this policy compares against limit_cost right now: the period's invoice total, less the credit already applied and the credit still to be drawn. Do not re-derive it — only the server can simulate the pending draw, and a figure computed from the invoice alone will not match what the policy evaluates.' to 'The cost this policy compares against limit_cost right now: the period's invoice total, less the credit already applied and the credit still to be drawn, or the full cost for a policy that does not take credit into account. Do not re-derive it — only the server can simulate the pending draw, and a figure computed from the invoice alone will not match what the policy evaluates.'
            - Modified property: eta_days
              - Description changed from 'Days until the policy fires, or null when no projection exists. 0 means the threshold is already crossed and the policy is triggered — measured, not projected. Null must be rendered as no date, never as 'now': it is the common case, and it is also what an unprojectable or more-than-a-year-away policy reports. Nothing is projected beyond 365 days, because the rate comes from the current month's spend. Note that a cost policy does not fire on cost alone — it also waits for the credit balance to fall to limit_cost — so a policy far over its cap can still report a future date or null.' to 'Days until the policy fires, or null when no projection exists. 0 means the threshold is already crossed and the policy is triggered — measured, not projected. Null must be rendered as no date, never as 'now': it is the common case, and it is also what an unprojectable or more-than-a-year-away policy reports. Nothing is projected beyond 365 days, because the rate comes from the current month's spend.'

PATCH /api/marketplace-customer-estimated-cost-policies/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: cost_breakdown
            - New property: trigger_status
            - Modified property: current_cost
              - Description changed from 'The cost this policy compares against limit_cost right now: the period's invoice total, less the credit already applied and the credit still to be drawn. Do not re-derive it — only the server can simulate the pending draw, and a figure computed from the invoice alone will not match what the policy evaluates.' to 'The cost this policy compares against limit_cost right now: the period's invoice total, less the credit already applied and the credit still to be drawn, or the full cost for a policy that does not take credit into account. Do not re-derive it — only the server can simulate the pending draw, and a figure computed from the invoice alone will not match what the policy evaluates.'
            - Modified property: eta_days
              - Description changed from 'Days until the policy fires, or null when no projection exists. 0 means the threshold is already crossed and the policy is triggered — measured, not projected. Null must be rendered as no date, never as 'now': it is the common case, and it is also what an unprojectable or more-than-a-year-away policy reports. Nothing is projected beyond 365 days, because the rate comes from the current month's spend. Note that a cost policy does not fire on cost alone — it also waits for the credit balance to fall to limit_cost — so a policy far over its cap can still report a future date or null.' to 'Days until the policy fires, or null when no projection exists. 0 means the threshold is already crossed and the policy is triggered — measured, not projected. Null must be rendered as no date, never as 'now': it is the common case, and it is also what an unprojectable or more-than-a-year-away policy reports. Nothing is projected beyond 365 days, because the rate comes from the current month's spend.'

PUT /api/marketplace-customer-estimated-cost-policies/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: cost_breakdown
            - New property: trigger_status
            - Modified property: current_cost
              - Description changed from 'The cost this policy compares against limit_cost right now: the period's invoice total, less the credit already applied and the credit still to be drawn. Do not re-derive it — only the server can simulate the pending draw, and a figure computed from the invoice alone will not match what the policy evaluates.' to 'The cost this policy compares against limit_cost right now: the period's invoice total, less the credit already applied and the credit still to be drawn, or the full cost for a policy that does not take credit into account. Do not re-derive it — only the server can simulate the pending draw, and a figure computed from the invoice alone will not match what the policy evaluates.'
            - Modified property: eta_days
              - Description changed from 'Days until the policy fires, or null when no projection exists. 0 means the threshold is already crossed and the policy is triggered — measured, not projected. Null must be rendered as no date, never as 'now': it is the common case, and it is also what an unprojectable or more-than-a-year-away policy reports. Nothing is projected beyond 365 days, because the rate comes from the current month's spend. Note that a cost policy does not fire on cost alone — it also waits for the credit balance to fall to limit_cost — so a policy far over its cap can still report a future date or null.' to 'Days until the policy fires, or null when no projection exists. 0 means the threshold is already crossed and the policy is triggered — measured, not projected. Null must be rendered as no date, never as 'now': it is the common case, and it is also what an unprojectable or more-than-a-year-away policy reports. Nothing is projected beyond 365 days, because the rate comes from the current month's spend.'

GET /api/marketplace-customer-service-accounts/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: error_traceback
              - New required property: username
            - Properties changed
              - Modified property: error_traceback
                - ReadOnly changed from false to true
              - Modified property: username
                - ReadOnly changed from false to true
                - MaxLength changed from 32 to null

HEAD /api/marketplace-customer-service-accounts/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/marketplace-customer-service-accounts/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: error_traceback
          - Deleted property: username
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: error_traceback
            - New required property: username
          - Properties changed
            - Modified property: error_traceback
              - ReadOnly changed from false to true
            - Modified property: username
              - ReadOnly changed from false to true
              - MaxLength changed from 32 to null

DELETE /api/marketplace-customer-service-accounts/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-customer-service-accounts/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: error_traceback
            - New required property: username
          - Properties changed
            - Modified property: error_traceback
              - ReadOnly changed from false to true
            - Modified property: username
              - ReadOnly changed from false to true
              - MaxLength changed from 32 to null

PATCH /api/marketplace-customer-service-accounts/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: error_traceback
          - Deleted property: username
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: error_traceback
            - New required property: username
          - Properties changed
            - Modified property: error_traceback
              - ReadOnly changed from false to true
            - Modified property: username
              - ReadOnly changed from false to true
              - MaxLength changed from 32 to null

PUT /api/marketplace-customer-service-accounts/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: error_traceback
          - Deleted property: username
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: error_traceback
            - New required property: username
          - Properties changed
            - Modified property: error_traceback
              - ReadOnly changed from false to true
            - Modified property: username
              - ReadOnly changed from false to true
              - MaxLength changed from 32 to null

POST /api/marketplace-customer-service-accounts/{uuid}/rotate_api_key/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: error_traceback
            - New required property: username
          - Properties changed
            - Modified property: error_traceback
              - ReadOnly changed from false to true
            - Modified property: username
              - ReadOnly changed from false to true
              - MaxLength changed from 32 to null

GET /api/marketplace-customer-usage/{uuid}/components-usage-by-project/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/marketplace-customer-usage/{uuid}/components-usage-timeseries/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/marketplace-customer-usage/{uuid}/components-usage/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/marketplace-demo-presets/info/{name}/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-demo-presets/info/{name}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-demo-presets/list/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-demo-presets/list/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-demo-presets/load/{name}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-global-categories/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-integration-statuses/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/marketplace-integration-statuses/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/marketplace-integration-statuses/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/marketplace-metric-breakdown/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-metric-definitions/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/marketplace-metric-definitions/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/marketplace-metric-definitions/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-metric-definitions/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-metric-definitions/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

PATCH /api/marketplace-metric-definitions/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/marketplace-metric-definitions/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-metric-goals/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/marketplace-metric-goals/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/marketplace-metric-goals/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-metric-goals/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-metric-goals/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

PATCH /api/marketplace-metric-goals/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/marketplace-metric-goals/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-metric-points/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-metric-retention-policies/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-metric-retention-policies/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-metric-retention-policies/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-metric-retention-policies/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-metric-retention-policies/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/marketplace-metric-retention-policies/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/marketplace-metric-retention-policies/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-metric-series/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-offering-access-subnets/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/marketplace-offering-access-subnets/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/marketplace-offering-access-subnets/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-offering-access-subnets/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-offering-access-subnets/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

PATCH /api/marketplace-offering-access-subnets/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

PUT /api/marketplace-offering-access-subnets/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-offering-estimated-cost-policies/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [cost_breakdown trigger_status]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: cost_breakdown
              - New property: trigger_status
              - Modified property: current_cost
                - Description changed from 'The cost this policy compares against limit_cost right now: the period's invoice total, less the credit already applied and the credit still to be drawn. Do not re-derive it — only the server can simulate the pending draw, and a figure computed from the invoice alone will not match what the policy evaluates.' to 'The cost this policy compares against limit_cost right now: the period's invoice total, less the credit already applied and the credit still to be drawn, or the full cost for a policy that does not take credit into account. Do not re-derive it — only the server can simulate the pending draw, and a figure computed from the invoice alone will not match what the policy evaluates.'
              - Modified property: eta_days
                - Description changed from 'Days until the policy fires, or null when no projection exists. 0 means the threshold is already crossed and the policy is triggered — measured, not projected. Null must be rendered as no date, never as 'now': it is the common case, and it is also what an unprojectable or more-than-a-year-away policy reports. Nothing is projected beyond 365 days, because the rate comes from the current month's spend. Note that a cost policy does not fire on cost alone — it also waits for the credit balance to fall to limit_cost — so a policy far over its cap can still report a future date or null.' to 'Days until the policy fires, or null when no projection exists. 0 means the threshold is already crossed and the policy is triggered — measured, not projected. Null must be rendered as no date, never as 'now': it is the common case, and it is also what an unprojectable or more-than-a-year-away policy reports. Nothing is projected beyond 365 days, because the rate comes from the current month's spend.'

HEAD /api/marketplace-offering-estimated-cost-policies/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/marketplace-offering-estimated-cost-policies/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: cost_breakdown
            - New property: trigger_status
            - Modified property: current_cost
              - Description changed from 'The cost this policy compares against limit_cost right now: the period's invoice total, less the credit already applied and the credit still to be drawn. Do not re-derive it — only the server can simulate the pending draw, and a figure computed from the invoice alone will not match what the policy evaluates.' to 'The cost this policy compares against limit_cost right now: the period's invoice total, less the credit already applied and the credit still to be drawn, or the full cost for a policy that does not take credit into account. Do not re-derive it — only the server can simulate the pending draw, and a figure computed from the invoice alone will not match what the policy evaluates.'
            - Modified property: eta_days
              - Description changed from 'Days until the policy fires, or null when no projection exists. 0 means the threshold is already crossed and the policy is triggered — measured, not projected. Null must be rendered as no date, never as 'now': it is the common case, and it is also what an unprojectable or more-than-a-year-away policy reports. Nothing is projected beyond 365 days, because the rate comes from the current month's spend. Note that a cost policy does not fire on cost alone — it also waits for the credit balance to fall to limit_cost — so a policy far over its cap can still report a future date or null.' to 'Days until the policy fires, or null when no projection exists. 0 means the threshold is already crossed and the policy is triggered — measured, not projected. Null must be rendered as no date, never as 'now': it is the common case, and it is also what an unprojectable or more-than-a-year-away policy reports. Nothing is projected beyond 365 days, because the rate comes from the current month's spend.'

GET /api/marketplace-offering-estimated-cost-policies/actions/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-offering-estimated-cost-policies/actions/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-offering-estimated-cost-policies/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-offering-estimated-cost-policies/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [cost_breakdown trigger_status]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: cost_breakdown
            - New property: trigger_status
            - Modified property: current_cost
              - Description changed from 'The cost this policy compares against limit_cost right now: the period's invoice total, less the credit already applied and the credit still to be drawn. Do not re-derive it — only the server can simulate the pending draw, and a figure computed from the invoice alone will not match what the policy evaluates.' to 'The cost this policy compares against limit_cost right now: the period's invoice total, less the credit already applied and the credit still to be drawn, or the full cost for a policy that does not take credit into account. Do not re-derive it — only the server can simulate the pending draw, and a figure computed from the invoice alone will not match what the policy evaluates.'
            - Modified property: eta_days
              - Description changed from 'Days until the policy fires, or null when no projection exists. 0 means the threshold is already crossed and the policy is triggered — measured, not projected. Null must be rendered as no date, never as 'now': it is the common case, and it is also what an unprojectable or more-than-a-year-away policy reports. Nothing is projected beyond 365 days, because the rate comes from the current month's spend. Note that a cost policy does not fire on cost alone — it also waits for the credit balance to fall to limit_cost — so a policy far over its cap can still report a future date or null.' to 'Days until the policy fires, or null when no projection exists. 0 means the threshold is already crossed and the policy is triggered — measured, not projected. Null must be rendered as no date, never as 'now': it is the common case, and it is also what an unprojectable or more-than-a-year-away policy reports. Nothing is projected beyond 365 days, because the rate comes from the current month's spend.'

PATCH /api/marketplace-offering-estimated-cost-policies/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: cost_breakdown
            - New property: trigger_status
            - Modified property: current_cost
              - Description changed from 'The cost this policy compares against limit_cost right now: the period's invoice total, less the credit already applied and the credit still to be drawn. Do not re-derive it — only the server can simulate the pending draw, and a figure computed from the invoice alone will not match what the policy evaluates.' to 'The cost this policy compares against limit_cost right now: the period's invoice total, less the credit already applied and the credit still to be drawn, or the full cost for a policy that does not take credit into account. Do not re-derive it — only the server can simulate the pending draw, and a figure computed from the invoice alone will not match what the policy evaluates.'
            - Modified property: eta_days
              - Description changed from 'Days until the policy fires, or null when no projection exists. 0 means the threshold is already crossed and the policy is triggered — measured, not projected. Null must be rendered as no date, never as 'now': it is the common case, and it is also what an unprojectable or more-than-a-year-away policy reports. Nothing is projected beyond 365 days, because the rate comes from the current month's spend. Note that a cost policy does not fire on cost alone — it also waits for the credit balance to fall to limit_cost — so a policy far over its cap can still report a future date or null.' to 'Days until the policy fires, or null when no projection exists. 0 means the threshold is already crossed and the policy is triggered — measured, not projected. Null must be rendered as no date, never as 'now': it is the common case, and it is also what an unprojectable or more-than-a-year-away policy reports. Nothing is projected beyond 365 days, because the rate comes from the current month's spend.'

PUT /api/marketplace-offering-estimated-cost-policies/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: cost_breakdown
            - New property: trigger_status
            - Modified property: current_cost
              - Description changed from 'The cost this policy compares against limit_cost right now: the period's invoice total, less the credit already applied and the credit still to be drawn. Do not re-derive it — only the server can simulate the pending draw, and a figure computed from the invoice alone will not match what the policy evaluates.' to 'The cost this policy compares against limit_cost right now: the period's invoice total, less the credit already applied and the credit still to be drawn, or the full cost for a policy that does not take credit into account. Do not re-derive it — only the server can simulate the pending draw, and a figure computed from the invoice alone will not match what the policy evaluates.'
            - Modified property: eta_days
              - Description changed from 'Days until the policy fires, or null when no projection exists. 0 means the threshold is already crossed and the policy is triggered — measured, not projected. Null must be rendered as no date, never as 'now': it is the common case, and it is also what an unprojectable or more-than-a-year-away policy reports. Nothing is projected beyond 365 days, because the rate comes from the current month's spend. Note that a cost policy does not fire on cost alone — it also waits for the credit balance to fall to limit_cost — so a policy far over its cap can still report a future date or null.' to 'Days until the policy fires, or null when no projection exists. 0 means the threshold is already crossed and the policy is triggered — measured, not projected. Null must be rendered as no date, never as 'now': it is the common case, and it is also what an unprojectable or more-than-a-year-away policy reports. Nothing is projected beyond 365 days, because the rate comes from the current month's spend.'

GET /api/marketplace-offering-files/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-offering-files/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-offering-files/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-offering-files/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-offering-files/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-offering-groups/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/marketplace-offering-groups/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/marketplace-offering-groups/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-offering-groups/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-offering-groups/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/marketplace-offering-groups/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

PUT /api/marketplace-offering-groups/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-offering-merges/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-offering-merges/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-offering-merges/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-offering-merges/suggest_mapping/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-offering-merges/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-offering-merges/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/marketplace-offering-merges/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-offering-merges/{uuid}/affected/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-offering-merges/{uuid}/execute/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-offering-merges/{uuid}/preview/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-offering-merges/{uuid}/undo/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-offering-metrics/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/marketplace-offering-metrics/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/marketplace-offering-metrics/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-offering-metrics/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-offering-metrics/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

PATCH /api/marketplace-offering-metrics/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

PUT /api/marketplace-offering-metrics/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-offering-metrics/{uuid}/archive/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-offering-metrics/{uuid}/pause/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-offering-metrics/{uuid}/purge/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-offering-metrics/{uuid}/resume/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-offering-permissions-log/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Modified query param: scope_type
  - Description changed from 'Scope type' to 'Scope type, as returned in scope_type: customer, project, offering, service_provider, call_organizer, call, proposal, resource, resource_project or global. A content type model name also matches.'

HEAD /api/marketplace-offering-permissions-log/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Modified query param: scope_type
  - Description changed from 'Scope type' to 'Scope type, as returned in scope_type: customer, project, offering, service_provider, call_organizer, call, proposal, resource, resource_project or global. A content type model name also matches.'

GET /api/marketplace-offering-permissions-log/{id}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/marketplace-offering-permissions/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Modified query param: scope_type
  - Description changed from 'Scope type' to 'Scope type, as returned in scope_type: customer, project, offering, service_provider, call_organizer, call, proposal, resource, resource_project or global. A content type model name also matches.'

HEAD /api/marketplace-offering-permissions/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Modified query param: scope_type
  - Description changed from 'Scope type' to 'Scope type, as returned in scope_type: customer, project, offering, service_provider, call_organizer, call, proposal, resource, resource_project or global. A content type model name also matches.'

GET /api/marketplace-offering-permissions/{id}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/marketplace-offering-profiles/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-offering-profiles/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-offering-profiles/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-offering-profiles/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-offering-profiles/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/marketplace-offering-profiles/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/marketplace-offering-profiles/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-offering-profiles/{uuid}/add_role/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-offering-profiles/{uuid}/remove_role/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-offering-referrals/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/marketplace-offering-referrals/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/marketplace-offering-referrals/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/marketplace-offering-roles/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/marketplace-offering-roles/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/marketplace-offering-roles/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-offering-roles/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-offering-roles/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

PATCH /api/marketplace-offering-roles/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/marketplace-offering-roles/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-offering-terms-of-service/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/marketplace-offering-terms-of-service/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/marketplace-offering-terms-of-service/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: is_active
            - Default changed from null to false
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: is_active
              - Default changed from null to false

DELETE /api/marketplace-offering-terms-of-service/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-offering-terms-of-service/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

PATCH /api/marketplace-offering-terms-of-service/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

PUT /api/marketplace-offering-terms-of-service/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-offering-usage-policies/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/marketplace-offering-usage-policies/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/marketplace-offering-usage-policies/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-offering-usage-policies/actions/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-offering-usage-policies/actions/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-offering-usage-policies/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-offering-usage-policies/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/marketplace-offering-usage-policies/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/marketplace-offering-usage-policies/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-offering-user-checklist-completions/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/marketplace-offering-user-checklist-completions/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/marketplace-offering-user-checklist-completions/{id}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/marketplace-offering-users/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/marketplace-offering-users/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/marketplace-offering-users/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-offering-users/posix_identities/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/marketplace-offering-users/posix_identities/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/marketplace-offering-users/profile_field_warnings/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-offering-users/profile_field_warnings/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-offering-users/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-offering-users/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

PATCH /api/marketplace-offering-users/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/marketplace-offering-users/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-offering-users/{uuid}/begin_creating/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-offering-users/{uuid}/checklist/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-offering-users/{uuid}/checklist_review/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-offering-users/{uuid}/completion_review_status/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-offering-users/{uuid}/completion_status/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-offering-users/{uuid}/posix_allocations/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-offering-users/{uuid}/posix_groups/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/marketplace-offering-users/{uuid}/request_deletion/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-offering-users/{uuid}/set_deleted/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-offering-users/{uuid}/set_deleting/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-offering-users/{uuid}/set_error_creating/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-offering-users/{uuid}/set_error_deleting/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-offering-users/{uuid}/set_ok/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-offering-users/{uuid}/set_pending_account_linking/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-offering-users/{uuid}/set_pending_additional_validation/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-offering-users/{uuid}/set_posix_attributes/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-offering-users/{uuid}/set_validation_complete/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-offering-users/{uuid}/submit_answers/

- Extensions changed
  - New extension: x-permissions

PATCH /api/marketplace-offering-users/{uuid}/update_comments/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-offering-users/{uuid}/update_restricted/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-offering-users/{uuid}/update_runtime_state/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-openstack-duplicate-offerings/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-openstack-duplicate-offerings/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-orders/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Deleted property: callback_url

HEAD /api/marketplace-orders/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/marketplace-orders/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: spending_limits
          - Modified property: callback_url
            - Description changed from '' to 'Sent by a Waldur that orders from this one through a remote offering: its public order pull endpoint (.../api/remote-waldur-api/pull_order/<its order uuid>). No other URL is accepted. Not stored: order callbacks are off.'
            - WriteOnly changed from false to true
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: callback_url

GET /api/marketplace-orders/dashboard-my-orders/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-orders/dashboard-my-orders/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-orders/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-orders/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: callback_url

PATCH /api/marketplace-orders/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

PUT /api/marketplace-orders/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-orders/{uuid}/approve_by_consumer/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-orders/{uuid}/approve_by_provider/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-orders/{uuid}/cancel/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-orders/{uuid}/delete_attachment/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-orders/{uuid}/offering/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [google_calendar_is_public google_calendar_link]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: google_calendar_is_public
            - Deleted property: google_calendar_link
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: spending_limit_periods
            - Modified property: endpoints
              - Items changed
                - Properties changed
                  - Modified property: url
                    - Format changed from '' to 'uri'
                    - MaxLength changed from null to 200
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: display_limit_config
                          - New property: transform
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: api_key_daily_usage
                    - New property: api_key_limits
                    - New property: display_prepaid_limits_as_total
                    - New property: firecrest_api_url
                    - New property: firecrest_system_name
                    - New property: instance_metrics
                    - New property: instance_metrics_enabled
                    - New property: instance_metrics_poll_interval_minutes
                    - New property: slurm_maintenance_sync_enabled
                    - New property: slurm_monitor_api_url
                    - New property: slurm_monitor_cluster_name
                    - Modified property: account_scope
                      - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'
            - Modified property: qos_profiles
              - Items changed
                - Properties changed
                  - New property: max_tres_mins_per_job
                  - Modified property: grp_tres
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                  - Modified property: max_tres_per_job
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                  - Modified property: max_tres_per_node
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                  - Modified property: max_tres_per_user
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                  - Modified property: min_tres_per_job
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: display_limit_config
                          - New property: transform

POST /api/marketplace-orders/{uuid}/reject_by_consumer/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-orders/{uuid}/reject_by_provider/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-orders/{uuid}/resource/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Description changed from 'Returns details of the resource connected to the requested object.' to 'Returns details of the resource connected to the requested object, if the consumer or provider resource view shows it to the caller; otherwise 404.'
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [display_limits prepaid_total_component_types spending_limit_status spending_limits terminated_at usage_limit_resumes_at]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: display_limits
            - New property: prepaid_total_component_types
            - New property: spending_limit_status
            - New property: spending_limits
            - New property: terminated_at
            - New property: usage_limit_resumes_at
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: callback_url
            - Modified property: endpoints
              - Items changed
                - Properties changed
                  - Modified property: url
                    - Format changed from '' to 'uri'
                    - MaxLength changed from null to 200
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: spending_limit_periods
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: callback_url

POST /api/marketplace-orders/{uuid}/retry/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-orders/{uuid}/set_backend_id/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-orders/{uuid}/set_consumer_info/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-orders/{uuid}/set_provider_info/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-orders/{uuid}/set_state_done/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-orders/{uuid}/set_state_erred/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-orders/{uuid}/set_state_executing/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-orders/{uuid}/unlink/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-orders/{uuid}/update_attachment/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-plan-components/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Description changed from 'Returns a paginated list of all plan components. A plan component defines the pricing and quotas for an offering component within a billing plan. The list is filtered based on the current user's access permissions and organization group memberships.' to 'Returns a paginated list of plan components. A plan component defines the pricing and quotas for an offering component within a billing plan. The list shows the components of plans of offerings the caller sees in public or provider offerings, narrowed by the plans' organization groups.'

HEAD /api/marketplace-plan-components/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/marketplace-plan-components/{id}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/marketplace-plans/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/marketplace-plans/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/marketplace-plans/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-plans/usage_stats/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/marketplace-plans/usage_stats/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

DELETE /api/marketplace-plans/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-plans/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

PATCH /api/marketplace-plans/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

PUT /api/marketplace-plans/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-plans/{uuid}/archive/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-plans/{uuid}/delete_organization_groups/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-plans/{uuid}/history/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-plans/{uuid}/history/at/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-plans/{uuid}/update_discounts/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-plans/{uuid}/update_organization_groups/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-plans/{uuid}/update_prices/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-plans/{uuid}/update_quotas/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-plugins/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Examples changed
          - Modified example: ExampleResponseForMarketplacePlugins
            - Value changed from [[map[available_limits:[] components:[map[billing_type:usage measured_unit:hours name:CPU type:cpu] map[billing_type:usage measured_unit:hours name:GPU type:gpu] map[billing_type:usage measured_unit:GB-hours name:RAM type:ram]] offering_type:Marketplace.Slurm]]] to [[map[available_limits:[] components:[map[billing_type:usage measured_unit:hours name:CPU type:cpu] map[billing_type:usage measured_unit:hours name:GPU type:gpu] map[billing_type:usage measured_unit:GB-hours name:RAM type:ram]] offering_type:Marketplace.SiteAgent]]]

GET /api/marketplace-posix-id-pools/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/marketplace-posix-id-pools/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/marketplace-posix-id-pools/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-posix-id-pools/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-posix-id-pools/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

PATCH /api/marketplace-posix-id-pools/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

PUT /api/marketplace-posix-id-pools/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-posix-id-pools/{uuid}/repoint/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-posix-id-pools/{uuid}/repoint_preview/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-posix-id-pools/{uuid}/stats/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/marketplace-posix-identities/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/marketplace-posix-identities/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/marketplace-posix-identities/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/marketplace-project-estimated-cost-policies/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [cost_breakdown trigger_status]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: cost_breakdown
              - New property: trigger_status
              - Modified property: current_cost
                - Description changed from 'The cost this policy compares against limit_cost right now: the period's invoice total, less the credit already applied and the credit still to be drawn. Do not re-derive it — only the server can simulate the pending draw, and a figure computed from the invoice alone will not match what the policy evaluates.' to 'The cost this policy compares against limit_cost right now: the period's invoice total, less the credit already applied and the credit still to be drawn, or the full cost for a policy that does not take credit into account. Do not re-derive it — only the server can simulate the pending draw, and a figure computed from the invoice alone will not match what the policy evaluates.'
              - Modified property: eta_days
                - Description changed from 'Days until the policy fires, or null when no projection exists. 0 means the threshold is already crossed and the policy is triggered — measured, not projected. Null must be rendered as no date, never as 'now': it is the common case, and it is also what an unprojectable or more-than-a-year-away policy reports. Nothing is projected beyond 365 days, because the rate comes from the current month's spend. Note that a cost policy does not fire on cost alone — it also waits for the credit balance to fall to limit_cost — so a policy far over its cap can still report a future date or null.' to 'Days until the policy fires, or null when no projection exists. 0 means the threshold is already crossed and the policy is triggered — measured, not projected. Null must be rendered as no date, never as 'now': it is the common case, and it is also what an unprojectable or more-than-a-year-away policy reports. Nothing is projected beyond 365 days, because the rate comes from the current month's spend.'

HEAD /api/marketplace-project-estimated-cost-policies/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/marketplace-project-estimated-cost-policies/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: cost_breakdown
            - New property: trigger_status
            - Modified property: current_cost
              - Description changed from 'The cost this policy compares against limit_cost right now: the period's invoice total, less the credit already applied and the credit still to be drawn. Do not re-derive it — only the server can simulate the pending draw, and a figure computed from the invoice alone will not match what the policy evaluates.' to 'The cost this policy compares against limit_cost right now: the period's invoice total, less the credit already applied and the credit still to be drawn, or the full cost for a policy that does not take credit into account. Do not re-derive it — only the server can simulate the pending draw, and a figure computed from the invoice alone will not match what the policy evaluates.'
            - Modified property: eta_days
              - Description changed from 'Days until the policy fires, or null when no projection exists. 0 means the threshold is already crossed and the policy is triggered — measured, not projected. Null must be rendered as no date, never as 'now': it is the common case, and it is also what an unprojectable or more-than-a-year-away policy reports. Nothing is projected beyond 365 days, because the rate comes from the current month's spend. Note that a cost policy does not fire on cost alone — it also waits for the credit balance to fall to limit_cost — so a policy far over its cap can still report a future date or null.' to 'Days until the policy fires, or null when no projection exists. 0 means the threshold is already crossed and the policy is triggered — measured, not projected. Null must be rendered as no date, never as 'now': it is the common case, and it is also what an unprojectable or more-than-a-year-away policy reports. Nothing is projected beyond 365 days, because the rate comes from the current month's spend.'

GET /api/marketplace-project-estimated-cost-policies/actions/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-project-estimated-cost-policies/actions/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-project-estimated-cost-policies/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-project-estimated-cost-policies/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [cost_breakdown trigger_status]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: cost_breakdown
            - New property: trigger_status
            - Modified property: current_cost
              - Description changed from 'The cost this policy compares against limit_cost right now: the period's invoice total, less the credit already applied and the credit still to be drawn. Do not re-derive it — only the server can simulate the pending draw, and a figure computed from the invoice alone will not match what the policy evaluates.' to 'The cost this policy compares against limit_cost right now: the period's invoice total, less the credit already applied and the credit still to be drawn, or the full cost for a policy that does not take credit into account. Do not re-derive it — only the server can simulate the pending draw, and a figure computed from the invoice alone will not match what the policy evaluates.'
            - Modified property: eta_days
              - Description changed from 'Days until the policy fires, or null when no projection exists. 0 means the threshold is already crossed and the policy is triggered — measured, not projected. Null must be rendered as no date, never as 'now': it is the common case, and it is also what an unprojectable or more-than-a-year-away policy reports. Nothing is projected beyond 365 days, because the rate comes from the current month's spend. Note that a cost policy does not fire on cost alone — it also waits for the credit balance to fall to limit_cost — so a policy far over its cap can still report a future date or null.' to 'Days until the policy fires, or null when no projection exists. 0 means the threshold is already crossed and the policy is triggered — measured, not projected. Null must be rendered as no date, never as 'now': it is the common case, and it is also what an unprojectable or more-than-a-year-away policy reports. Nothing is projected beyond 365 days, because the rate comes from the current month's spend.'

PATCH /api/marketplace-project-estimated-cost-policies/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: cost_breakdown
            - New property: trigger_status
            - Modified property: current_cost
              - Description changed from 'The cost this policy compares against limit_cost right now: the period's invoice total, less the credit already applied and the credit still to be drawn. Do not re-derive it — only the server can simulate the pending draw, and a figure computed from the invoice alone will not match what the policy evaluates.' to 'The cost this policy compares against limit_cost right now: the period's invoice total, less the credit already applied and the credit still to be drawn, or the full cost for a policy that does not take credit into account. Do not re-derive it — only the server can simulate the pending draw, and a figure computed from the invoice alone will not match what the policy evaluates.'
            - Modified property: eta_days
              - Description changed from 'Days until the policy fires, or null when no projection exists. 0 means the threshold is already crossed and the policy is triggered — measured, not projected. Null must be rendered as no date, never as 'now': it is the common case, and it is also what an unprojectable or more-than-a-year-away policy reports. Nothing is projected beyond 365 days, because the rate comes from the current month's spend. Note that a cost policy does not fire on cost alone — it also waits for the credit balance to fall to limit_cost — so a policy far over its cap can still report a future date or null.' to 'Days until the policy fires, or null when no projection exists. 0 means the threshold is already crossed and the policy is triggered — measured, not projected. Null must be rendered as no date, never as 'now': it is the common case, and it is also what an unprojectable or more-than-a-year-away policy reports. Nothing is projected beyond 365 days, because the rate comes from the current month's spend.'

PUT /api/marketplace-project-estimated-cost-policies/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: cost_breakdown
            - New property: trigger_status
            - Modified property: current_cost
              - Description changed from 'The cost this policy compares against limit_cost right now: the period's invoice total, less the credit already applied and the credit still to be drawn. Do not re-derive it — only the server can simulate the pending draw, and a figure computed from the invoice alone will not match what the policy evaluates.' to 'The cost this policy compares against limit_cost right now: the period's invoice total, less the credit already applied and the credit still to be drawn, or the full cost for a policy that does not take credit into account. Do not re-derive it — only the server can simulate the pending draw, and a figure computed from the invoice alone will not match what the policy evaluates.'
            - Modified property: eta_days
              - Description changed from 'Days until the policy fires, or null when no projection exists. 0 means the threshold is already crossed and the policy is triggered — measured, not projected. Null must be rendered as no date, never as 'now': it is the common case, and it is also what an unprojectable or more-than-a-year-away policy reports. Nothing is projected beyond 365 days, because the rate comes from the current month's spend. Note that a cost policy does not fire on cost alone — it also waits for the credit balance to fall to limit_cost — so a policy far over its cap can still report a future date or null.' to 'Days until the policy fires, or null when no projection exists. 0 means the threshold is already crossed and the policy is triggered — measured, not projected. Null must be rendered as no date, never as 'now': it is the common case, and it is also what an unprojectable or more-than-a-year-away policy reports. Nothing is projected beyond 365 days, because the rate comes from the current month's spend.'

GET /api/marketplace-project-metrics/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-project-order-auto-approvals/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/marketplace-project-order-auto-approvals/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/marketplace-project-order-auto-approvals/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-project-order-auto-approvals/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-project-order-auto-approvals/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/marketplace-project-order-auto-approvals/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

PUT /api/marketplace-project-order-auto-approvals/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-project-posix-groups/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-project-posix-groups/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-project-service-accounts/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: error_traceback
              - New required property: username
            - Properties changed
              - Modified property: error_traceback
                - ReadOnly changed from false to true
              - Modified property: username
                - ReadOnly changed from false to true
                - MaxLength changed from 32 to null

HEAD /api/marketplace-project-service-accounts/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/marketplace-project-service-accounts/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: error_traceback
          - Deleted property: username
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: error_traceback
            - New required property: username
          - Properties changed
            - Modified property: error_traceback
              - ReadOnly changed from false to true
            - Modified property: username
              - ReadOnly changed from false to true
              - MaxLength changed from 32 to null

DELETE /api/marketplace-project-service-accounts/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-project-service-accounts/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: error_traceback
            - New required property: username
          - Properties changed
            - Modified property: error_traceback
              - ReadOnly changed from false to true
            - Modified property: username
              - ReadOnly changed from false to true
              - MaxLength changed from 32 to null

PATCH /api/marketplace-project-service-accounts/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: error_traceback
          - Deleted property: username
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: error_traceback
            - New required property: username
          - Properties changed
            - Modified property: error_traceback
              - ReadOnly changed from false to true
            - Modified property: username
              - ReadOnly changed from false to true
              - MaxLength changed from 32 to null

PUT /api/marketplace-project-service-accounts/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: error_traceback
          - Deleted property: username
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: error_traceback
            - New required property: username
          - Properties changed
            - Modified property: error_traceback
              - ReadOnly changed from false to true
            - Modified property: username
              - ReadOnly changed from false to true
              - MaxLength changed from 32 to null

POST /api/marketplace-project-service-accounts/{uuid}/rotate_api_key/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: error_traceback
            - New required property: username
          - Properties changed
            - Modified property: error_traceback
              - ReadOnly changed from false to true
            - Modified property: username
              - ReadOnly changed from false to true
              - MaxLength changed from 32 to null

GET /api/marketplace-project-update-requests/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/marketplace-project-update-requests/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/marketplace-project-update-requests/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/marketplace-project-update-requests/{uuid}/approve/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-project-update-requests/{uuid}/reject/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-project-usage/{uuid}/components-usage-timeseries/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/marketplace-project-usage/{uuid}/components-usage/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/marketplace-provider-offerings/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [google_calendar_is_public google_calendar_link]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Deleted property: google_calendar_is_public
              - Deleted property: google_calendar_link
              - Modified property: components
                - Items changed
                  - Properties changed
                    - New property: spending_limit_periods
              - Modified property: endpoints
                - Items changed
                  - Properties changed
                    - Modified property: url
                      - Format changed from '' to 'uri'
                      - MaxLength changed from null to 200
              - Modified property: options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - New property: display_limit_config
                            - New property: transform
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: api_key_daily_usage
                      - New property: api_key_limits
                      - New property: display_prepaid_limits_as_total
                      - New property: firecrest_api_url
                      - New property: firecrest_system_name
                      - New property: instance_metrics
                      - New property: instance_metrics_enabled
                      - New property: instance_metrics_poll_interval_minutes
                      - New property: slurm_maintenance_sync_enabled
                      - New property: slurm_monitor_api_url
                      - New property: slurm_monitor_cluster_name
                      - Modified property: account_scope
                        - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'
              - Modified property: qos_profiles
                - Items changed
                  - Properties changed
                    - New property: max_tres_mins_per_job
                    - Modified property: grp_tres
                      - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                    - Modified property: max_tres_per_job
                      - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                    - Modified property: max_tres_per_node
                      - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                    - Modified property: max_tres_per_user
                      - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                    - Modified property: min_tres_per_job
                      - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
              - Modified property: resource_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - New property: display_limit_config
                            - New property: transform
              - Modified property: secret_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedSecretOptions
                    - Properties changed
                      - Modified property: backend_url
                        - Format changed from '' to 'uri'

HEAD /api/marketplace-provider-offerings/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/marketplace-provider-offerings/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: components
            - Items changed
              - Properties changed
                - New property: spending_limit_periods
          - Modified property: options
            - Properties changed
              - Modified property: options
                - AdditionalProperties changed
                  - Properties changed
                    - New property: display_limit_config
                    - New property: transform
          - Modified property: plugin_options
            - Properties changed
              - New property: api_key_daily_usage
              - New property: api_key_limits
              - New property: display_prepaid_limits_as_total
              - New property: firecrest_api_url
              - New property: firecrest_system_name
              - New property: instance_metrics
              - New property: instance_metrics_enabled
              - New property: instance_metrics_poll_interval_minutes
              - New property: slurm_maintenance_sync_enabled
              - New property: slurm_monitor_api_url
              - New property: slurm_monitor_cluster_name
              - Modified property: account_scope
                - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'
          - Modified property: resource_options
            - Properties changed
              - Modified property: options
                - AdditionalProperties changed
                  - Properties changed
                    - New property: display_limit_config
                    - New property: transform
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: components
            - Items changed
              - Properties changed
                - New property: spending_limit_periods
          - Modified property: options
            - Properties changed
              - Modified property: options
                - AdditionalProperties changed
                  - Properties changed
                    - New property: display_limit_config
                    - New property: transform
          - Modified property: plugin_options
            - Properties changed
              - New property: api_key_daily_usage
              - New property: api_key_limits
              - New property: display_prepaid_limits_as_total
              - New property: firecrest_api_url
              - New property: firecrest_system_name
              - New property: instance_metrics
              - New property: instance_metrics_enabled
              - New property: instance_metrics_poll_interval_minutes
              - New property: slurm_maintenance_sync_enabled
              - New property: slurm_monitor_api_url
              - New property: slurm_monitor_cluster_name
              - Modified property: account_scope
                - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'
          - Modified property: resource_options
            - Properties changed
              - Modified property: options
                - AdditionalProperties changed
                  - Properties changed
                    - New property: display_limit_config
                    - New property: transform
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: components
            - Items changed
              - Properties changed
                - New property: spending_limit_periods
          - Modified property: options
            - Properties changed
              - Modified property: options
                - AdditionalProperties changed
                  - Properties changed
                    - New property: display_limit_config
                    - New property: transform
          - Modified property: plugin_options
            - Properties changed
              - New property: api_key_daily_usage
              - New property: api_key_limits
              - New property: display_prepaid_limits_as_total
              - New property: firecrest_api_url
              - New property: firecrest_system_name
              - New property: instance_metrics
              - New property: instance_metrics_enabled
              - New property: instance_metrics_poll_interval_minutes
              - New property: slurm_maintenance_sync_enabled
              - New property: slurm_monitor_api_url
              - New property: slurm_monitor_cluster_name
              - Modified property: account_scope
                - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'
          - Modified property: resource_options
            - Properties changed
              - Modified property: options
                - AdditionalProperties changed
                  - Properties changed
                    - New property: display_limit_config
                    - New property: transform
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: google_calendar_is_public
            - Deleted property: google_calendar_link
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: spending_limit_periods
            - Modified property: endpoints
              - Items changed
                - Properties changed
                  - Modified property: url
                    - Format changed from '' to 'uri'
                    - MaxLength changed from null to 200
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: display_limit_config
                          - New property: transform
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: api_key_daily_usage
                    - New property: api_key_limits
                    - New property: display_prepaid_limits_as_total
                    - New property: firecrest_api_url
                    - New property: firecrest_system_name
                    - New property: instance_metrics
                    - New property: instance_metrics_enabled
                    - New property: instance_metrics_poll_interval_minutes
                    - New property: slurm_maintenance_sync_enabled
                    - New property: slurm_monitor_api_url
                    - New property: slurm_monitor_cluster_name
                    - Modified property: account_scope
                      - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'
            - Modified property: qos_profiles
              - Items changed
                - Properties changed
                  - New property: max_tres_mins_per_job
                  - Modified property: grp_tres
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                  - Modified property: max_tres_per_job
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                  - Modified property: max_tres_per_node
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                  - Modified property: max_tres_per_user
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                  - Modified property: min_tres_per_job
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: display_limit_config
                          - New property: transform
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - Modified property: backend_url
                      - Format changed from '' to 'uri'

GET /api/marketplace-provider-offerings/aggregated_access_subnets/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-provider-offerings/aggregated_access_subnets/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-provider-offerings/groups/

- Extensions changed
  - New extension: x-permissions
- Description changed from 'Returns a paginated list of active, shared offerings grouped by their service provider.' to 'Returns a paginated list of active, shared offerings grouped by their service provider. Only offerings the caller may see in the public offerings list are included.'

HEAD /api/marketplace-provider-offerings/groups/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/import_offering/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-provider-offerings/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/description with value: 'Check if non-staff users are allowed to manage offering lifecycle.'
    - Added /0/kind with value: 'custom'
    - Removed /0/permission with value: 'OFFERING.DELETE'
    - Removed /0/scopes with value: '[customer]'
    - Added /- with value: 'map[kind:permission permission:OFFERING.DELETE scopes:[customer]]'

GET /api/marketplace-provider-offerings/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [google_calendar_is_public google_calendar_link]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: google_calendar_is_public
            - Deleted property: google_calendar_link
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: spending_limit_periods
            - Modified property: endpoints
              - Items changed
                - Properties changed
                  - Modified property: url
                    - Format changed from '' to 'uri'
                    - MaxLength changed from null to 200
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: display_limit_config
                          - New property: transform
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: api_key_daily_usage
                    - New property: api_key_limits
                    - New property: display_prepaid_limits_as_total
                    - New property: firecrest_api_url
                    - New property: firecrest_system_name
                    - New property: instance_metrics
                    - New property: instance_metrics_enabled
                    - New property: instance_metrics_poll_interval_minutes
                    - New property: slurm_maintenance_sync_enabled
                    - New property: slurm_monitor_api_url
                    - New property: slurm_monitor_cluster_name
                    - Modified property: account_scope
                      - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'
            - Modified property: qos_profiles
              - Items changed
                - Properties changed
                  - New property: max_tres_mins_per_job
                  - Modified property: grp_tres
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                  - Modified property: max_tres_per_job
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                  - Modified property: max_tres_per_node
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                  - Modified property: max_tres_per_user
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                  - Modified property: min_tres_per_job
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: display_limit_config
                          - New property: transform
            - Modified property: secret_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedSecretOptions
                  - Properties changed
                    - Modified property: backend_url
                      - Format changed from '' to 'uri'

GET /api/marketplace-provider-offerings/{uuid}/access_subnets/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/activate/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/description with value: 'Check if non-staff users are allowed to manage offering lifecycle.'
    - Added /0/kind with value: 'custom'
    - Removed /0/permission with value: 'OFFERING.CREATE'
    - Removed /0/scopes with value: '[* customer customer.serviceprovider]'
    - Added /- with value: 'map[kind:permission permission:OFFERING.CREATE scopes:[* customer customer.serviceprovider]]'

POST /api/marketplace-provider-offerings/{uuid}/add_endpoint/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: url
            - Format changed from '' to 'uri'
            - MaxLength changed from null to 200

POST /api/marketplace-provider-offerings/{uuid}/add_partition/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-provider-offerings/{uuid}/add_qos/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: max_tres_mins_per_job
          - Modified property: grp_tres
            - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
          - Modified property: max_tres_per_job
            - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
          - Modified property: max_tres_per_node
            - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
          - Modified property: max_tres_per_user
            - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
          - Modified property: min_tres_per_job
            - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: max_tres_mins_per_job
            - Modified property: grp_tres
              - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
            - Modified property: max_tres_per_job
              - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
            - Modified property: max_tres_per_node
              - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
            - Modified property: max_tres_per_user
              - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
            - Modified property: min_tres_per_job
              - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'

POST /api/marketplace-provider-offerings/{uuid}/add_software_catalog/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-provider-offerings/{uuid}/add_user/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/archive/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/description with value: 'Check if non-staff users are allowed to manage offering lifecycle.'
    - Added /0/kind with value: 'custom'
    - Removed /0/permission with value: 'OFFERING.ARCHIVE'
    - Removed /0/scopes with value: '[* customer customer.serviceprovider]'
    - Added /- with value: 'map[kind:permission permission:OFFERING.ARCHIVE scopes:[* customer customer.serviceprovider]]'

POST /api/marketplace-provider-offerings/{uuid}/check_unique_backend_id/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-provider-offerings/{uuid}/component_stats/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-provider-offerings/{uuid}/costs/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'any_of'
    - Added /0/of with value: '[map[kind:staff_or_support] map[kind:permission permission:SERVICE_PROVIDER.GET_REVENUE scopes:[customer customer.serviceprovider]]]'
    - Removed /0/permission with value: 'SERVICE_PROVIDER.GET_REVENUE'
    - Removed /0/scopes with value: '[customer customer.serviceprovider]'

POST /api/marketplace-provider-offerings/{uuid}/create_offering_component/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: spending_limit_periods

GET /api/marketplace-provider-offerings/{uuid}/customers/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'any_of'
    - Added /0/of with value: '[map[kind:staff_or_support] map[kind:permission permission:SERVICE_PROVIDER.LIST_CUSTOMERS scopes:[customer customer.serviceprovider]]]'
    - Removed /0/permission with value: 'SERVICE_PROVIDER.LIST_CUSTOMERS'
    - Removed /0/scopes with value: '[customer customer.serviceprovider]'

DELETE /api/marketplace-provider-offerings/{uuid}/delete-user-attribute-config/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/delete_endpoint/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-provider-offerings/{uuid}/delete_image/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/delete_organization_groups/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/delete_tags/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/delete_thumbnail/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/delete_user/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/draft/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/description with value: 'Check if non-staff users are allowed to manage offering lifecycle.'
    - Added /0/kind with value: 'custom'
    - Removed /0/permission with value: 'OFFERING.CREATE'
    - Removed /0/scopes with value: '[* customer customer.serviceprovider]'
    - Added /- with value: 'map[kind:permission permission:OFFERING.CREATE scopes:[* customer customer.serviceprovider]]'

GET /api/marketplace-provider-offerings/{uuid}/effective_posix_id_pool/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/export_offering/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-provider-offerings/{uuid}/glauth_tree/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-provider-offerings/{uuid}/glauth_users_config/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-provider-offerings/{uuid}/history/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-provider-offerings/{uuid}/history/at/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/import_resource/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: display_limits
            - New property: prepaid_total_component_types
            - New property: spending_limit_status
            - New property: spending_limits
            - New property: terminated_at
            - New property: usage_limit_resumes_at
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: callback_url
            - Modified property: endpoints
              - Items changed
                - Properties changed
                  - Modified property: url
                    - Format changed from '' to 'uri'
                    - MaxLength changed from null to 200
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: spending_limit_periods
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: callback_url

GET /api/marketplace-provider-offerings/{uuid}/importable_resources/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-provider-offerings/{uuid}/list_course_accounts/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-provider-offerings/{uuid}/list_customer_projects/

- Extensions changed
  - New extension: x-permissions
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [user_assurance_levels user_nationalities user_organization_types]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: user_assurance_levels
              - New property: user_nationalities
              - New property: user_organization_types
              - Modified property: project_metadata
                - Items changed
                  - Properties changed
                    - New property: likert_high_label
                    - New property: likert_low_label
                    - New property: likert_scale_length
                    - New property: max_value
                    - New property: min_value

GET /api/marketplace-provider-offerings/{uuid}/list_customer_service_accounts/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: error_traceback
              - New required property: username
            - Properties changed
              - Modified property: error_traceback
                - ReadOnly changed from false to true
              - Modified property: username
                - ReadOnly changed from false to true
                - MaxLength changed from 32 to null

GET /api/marketplace-provider-offerings/{uuid}/list_customer_users/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-provider-offerings/{uuid}/list_project_service_accounts/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: error_traceback
              - New required property: username
            - Properties changed
              - Modified property: error_traceback
                - ReadOnly changed from false to true
              - Modified property: username
                - ReadOnly changed from false to true
                - MaxLength changed from 32 to null

GET /api/marketplace-provider-offerings/{uuid}/list_users/

- Extensions changed
  - New extension: x-permissions
- New query param: role_template

HEAD /api/marketplace-provider-offerings/{uuid}/list_users/

- Extensions changed
  - New extension: x-permissions
- New query param: role_template

POST /api/marketplace-provider-offerings/{uuid}/make_available/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/description with value: 'Check if non-staff users are allowed to manage offering lifecycle.'
    - Added /0/kind with value: 'custom'
    - Removed /0/permission with value: 'OFFERING.PAUSE'
    - Removed /0/scopes with value: '[* customer customer.serviceprovider]'
    - Added /- with value: 'map[kind:permission permission:OFFERING.PAUSE scopes:[* customer customer.serviceprovider]]'

POST /api/marketplace-provider-offerings/{uuid}/make_unavailable/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/description with value: 'Check if non-staff users are allowed to manage offering lifecycle.'
    - Added /0/kind with value: 'custom'
    - Removed /0/permission with value: 'OFFERING.PAUSE'
    - Removed /0/scopes with value: '[* customer customer.serviceprovider]'
    - Added /- with value: 'map[kind:permission permission:OFFERING.PAUSE scopes:[* customer customer.serviceprovider]]'

POST /api/marketplace-provider-offerings/{uuid}/move_offering/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: google_calendar_is_public
            - Deleted property: google_calendar_link
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: spending_limit_periods
            - Modified property: endpoints
              - Items changed
                - Properties changed
                  - Modified property: url
                    - Format changed from '' to 'uri'
                    - MaxLength changed from null to 200
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: display_limit_config
                          - New property: transform
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: api_key_daily_usage
                    - New property: api_key_limits
                    - New property: display_prepaid_limits_as_total
                    - New property: firecrest_api_url
                    - New property: firecrest_system_name
                    - New property: instance_metrics
                    - New property: instance_metrics_enabled
                    - New property: instance_metrics_poll_interval_minutes
                    - New property: slurm_maintenance_sync_enabled
                    - New property: slurm_monitor_api_url
                    - New property: slurm_monitor_cluster_name
                    - Modified property: account_scope
                      - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'
            - Modified property: qos_profiles
              - Items changed
                - Properties changed
                  - New property: max_tres_mins_per_job
                  - Modified property: grp_tres
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                  - Modified property: max_tres_per_job
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                  - Modified property: max_tres_per_node
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                  - Modified property: max_tres_per_user
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                  - Modified property: min_tres_per_job
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: display_limit_config
                          - New property: transform

GET /api/marketplace-provider-offerings/{uuid}/orders/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Deleted property: callback_url

GET /api/marketplace-provider-offerings/{uuid}/orders/{order_uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: callback_url

POST /api/marketplace-provider-offerings/{uuid}/pause/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/description with value: 'Check if non-staff users are allowed to manage offering lifecycle.'
    - Added /0/kind with value: 'custom'
    - Removed /0/permission with value: 'OFFERING.PAUSE'
    - Removed /0/scopes with value: '[* customer customer.serviceprovider]'
    - Added /- with value: 'map[kind:permission permission:OFFERING.PAUSE scopes:[* customer customer.serviceprovider]]'

POST /api/marketplace-provider-offerings/{uuid}/refresh_offering_usernames/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-provider-offerings/{uuid}/remove_offering_component/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-provider-offerings/{uuid}/remove_partition/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-provider-offerings/{uuid}/remove_qos/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-provider-offerings/{uuid}/remove_software_catalog/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-provider-offerings/{uuid}/set_backend_metadata/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-provider-offerings/{uuid}/set_offering_group/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/set_partition_qos/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-provider-offerings/{uuid}/set_profile/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-provider-offerings/{uuid}/state_counters/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-provider-offerings/{uuid}/stats/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'any_of'
    - Added /0/of with value: '[map[kind:staff_or_support] map[kind:permission permission:SERVICE_PROVIDER.GET_STATISTICS scopes:[customer customer.serviceprovider]]]'
    - Removed /0/permission with value: 'SERVICE_PROVIDER.GET_STATISTICS'
    - Removed /0/scopes with value: '[customer customer.serviceprovider]'

POST /api/marketplace-provider-offerings/{uuid}/switch_billing_mode/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-provider-offerings/{uuid}/sync/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-provider-offerings/{uuid}/sync_resources/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-provider-offerings/{uuid}/tos_stats/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/marketplace-provider-offerings/{uuid}/unpause/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/description with value: 'Check if non-staff users are allowed to manage offering lifecycle.'
    - Added /0/kind with value: 'custom'
    - Removed /0/permission with value: 'OFFERING.UNPAUSE'
    - Removed /0/scopes with value: '[* customer customer.serviceprovider]'
    - Added /- with value: 'map[kind:permission permission:OFFERING.UNPAUSE scopes:[* customer customer.serviceprovider]]'

PATCH /api/marketplace-provider-offerings/{uuid}/update-user-attribute-config/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/update-user-attribute-config/

- Extensions changed
  - New extension: x-permissions

PUT /api/marketplace-provider-offerings/{uuid}/update-user-attribute-config/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/update_attributes/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-provider-offerings/{uuid}/update_backend_id_rules/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-provider-offerings/{uuid}/update_compliance_checklist/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-provider-offerings/{uuid}/update_description/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-provider-offerings/{uuid}/update_image/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/update_integration/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: plugin_options
            - Properties changed
              - New property: api_key_daily_usage
              - New property: api_key_limits
              - New property: display_prepaid_limits_as_total
              - New property: firecrest_api_url
              - New property: firecrest_system_name
              - New property: instance_metrics
              - New property: instance_metrics_enabled
              - New property: instance_metrics_poll_interval_minutes
              - New property: slurm_maintenance_sync_enabled
              - New property: slurm_monitor_api_url
              - New property: slurm_monitor_cluster_name
              - Modified property: account_scope
                - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'
          - Modified property: secret_options
            - Properties changed
              - Modified property: backend_url
                - Format changed from '' to 'uri'

POST /api/marketplace-provider-offerings/{uuid}/update_location/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-provider-offerings/{uuid}/update_offering_component/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: spending_limit_periods

POST /api/marketplace-provider-offerings/{uuid}/update_options/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
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
                    - New property: display_limit_config
                    - New property: transform

POST /api/marketplace-provider-offerings/{uuid}/update_organization_groups/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/update_overview/

- Extensions changed
  - New extension: x-permissions

PATCH /api/marketplace-provider-offerings/{uuid}/update_partition/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

PATCH /api/marketplace-provider-offerings/{uuid}/update_qos/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: max_tres_mins_per_job
          - Modified property: grp_tres
            - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
          - Modified property: max_tres_per_job
            - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
          - Modified property: max_tres_per_node
            - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
          - Modified property: max_tres_per_user
            - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
          - Modified property: min_tres_per_job
            - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: max_tres_mins_per_job
            - Modified property: grp_tres
              - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
            - Modified property: max_tres_per_job
              - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
            - Modified property: max_tres_per_node
              - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
            - Modified property: max_tres_per_user
              - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
            - Modified property: min_tres_per_job
              - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'

POST /api/marketplace-provider-offerings/{uuid}/update_resource_options/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
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
                    - New property: display_limit_config
                    - New property: transform

PATCH /api/marketplace-provider-offerings/{uuid}/update_software_catalog/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-provider-offerings/{uuid}/update_tags/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/update_thumbnail/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/update_type/

- Extensions changed
  - New extension: x-permissions
- Description changed from 'Changes the offering's `type` between Marketplace.Basic and the site-agent type (Marketplace.Slurm). Both plugins share the same data shape (the site-agent processors inherit from Basic and only delegate the send paths to the external agent), so the swap is safe in either direction. Refused if the offering's current type is not in the swappable set.' to 'Changes the offering's `type` between Marketplace.Basic and the site-agent type (Marketplace.SiteAgent; the legacy name Marketplace.Slurm is accepted). Both plugins share the same data shape (the site-agent processors inherit from Basic and only delegate the send paths to the external agent), so the swap is safe in either direction. Refused if the offering's current type is not in the swappable set.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: type
            - New enum values: [Marketplace.SiteAgent]

POST /api/marketplace-provider-offerings/{uuid}/update_user/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-offerings/{uuid}/upload_markdown_image/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/description with value: 'The route is open only while ENABLE_MARKDOWN_IMAGE_UPLOAD is on.'
    - Added /0/kind with value: 'custom'
    - Removed /0/permission with value: 'OFFERING.UPDATE_DESCRIPTION'
    - Removed /0/scopes with value: '[* customer customer.serviceprovider]'
    - Added /- with value: 'map[kind:permission permission:OFFERING.UPDATE_DESCRIPTION scopes:[* customer customer.serviceprovider]]'

GET /api/marketplace-provider-offerings/{uuid}/user-attribute-config/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-provider-offerings/{uuid}/user_has_resource_access/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-provider-resource-projects/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/marketplace-provider-resource-projects/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/marketplace-provider-resource-projects/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

PATCH /api/marketplace-provider-resource-projects/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/marketplace-provider-resource-projects/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-resource-projects/{uuid}/add_user/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-resource-projects/{uuid}/delete_user/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-provider-resource-projects/{uuid}/list_users/

- Extensions changed
  - New extension: x-permissions
- New query param: role_template

HEAD /api/marketplace-provider-resource-projects/{uuid}/list_users/

- Extensions changed
  - New extension: x-permissions
- New query param: role_template

POST /api/marketplace-provider-resource-projects/{uuid}/set_backend_id/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-resource-projects/{uuid}/set_state_erred/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-resource-projects/{uuid}/set_state_ok/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-resource-projects/{uuid}/update_user/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-provider-resources/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [display_limits prepaid_total_component_types spending_limit_status spending_limits terminated_at usage_limit_resumes_at]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: display_limits
              - New property: prepaid_total_component_types
              - New property: spending_limit_status
              - New property: spending_limits
              - New property: terminated_at
              - New property: usage_limit_resumes_at
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Deleted property: callback_url
              - Modified property: endpoints
                - Items changed
                  - Properties changed
                    - Modified property: url
                      - Format changed from '' to 'uri'
                      - MaxLength changed from null to 200
              - Modified property: offering_components
                - Items changed
                  - Properties changed
                    - New property: spending_limit_periods
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Deleted property: callback_url

HEAD /api/marketplace-provider-resources/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/marketplace-provider-resources/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [display_limits prepaid_total_component_types spending_limit_status spending_limits terminated_at usage_limit_resumes_at]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: display_limits
            - New property: prepaid_total_component_types
            - New property: spending_limit_status
            - New property: spending_limits
            - New property: terminated_at
            - New property: usage_limit_resumes_at
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: callback_url
            - Modified property: endpoints
              - Items changed
                - Properties changed
                  - Modified property: url
                    - Format changed from '' to 'uri'
                    - MaxLength changed from null to 200
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: spending_limit_periods
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: callback_url

PATCH /api/marketplace-provider-resources/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

PUT /api/marketplace-provider-resources/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-provider-resources/{uuid}/add_user/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-resources/{uuid}/adjust_dates/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-resources/{uuid}/delete_user/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-provider-resources/{uuid}/details/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/marketplace-provider-resources/{uuid}/glauth_tree/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-provider-resources/{uuid}/glauth_users_config/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-provider-resources/{uuid}/history/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-provider-resources/{uuid}/history/at/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-provider-resources/{uuid}/list_users/

- Extensions changed
  - New extension: x-permissions
- New query param: role_template

HEAD /api/marketplace-provider-resources/{uuid}/list_users/

- Extensions changed
  - New extension: x-permissions
- New query param: role_template

POST /api/marketplace-provider-resources/{uuid}/move_resource/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: display_limits
            - New property: prepaid_total_component_types
            - New property: spending_limit_status
            - New property: spending_limits
            - New property: terminated_at
            - New property: usage_limit_resumes_at
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: callback_url
            - Modified property: endpoints
              - Items changed
                - Properties changed
                  - Modified property: url
                    - Format changed from '' to 'uri'
                    - MaxLength changed from null to 200
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: spending_limit_periods
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: callback_url

GET /api/marketplace-provider-resources/{uuid}/offering/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [google_calendar_is_public google_calendar_link]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: google_calendar_is_public
            - Deleted property: google_calendar_link
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: spending_limit_periods
            - Modified property: endpoints
              - Items changed
                - Properties changed
                  - Modified property: url
                    - Format changed from '' to 'uri'
                    - MaxLength changed from null to 200
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: display_limit_config
                          - New property: transform
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: api_key_daily_usage
                    - New property: api_key_limits
                    - New property: display_prepaid_limits_as_total
                    - New property: firecrest_api_url
                    - New property: firecrest_system_name
                    - New property: instance_metrics
                    - New property: instance_metrics_enabled
                    - New property: instance_metrics_poll_interval_minutes
                    - New property: slurm_maintenance_sync_enabled
                    - New property: slurm_monitor_api_url
                    - New property: slurm_monitor_cluster_name
                    - Modified property: account_scope
                      - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'
            - Modified property: qos_profiles
              - Items changed
                - Properties changed
                  - New property: max_tres_mins_per_job
                  - Modified property: grp_tres
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                  - Modified property: max_tres_per_job
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                  - Modified property: max_tres_per_node
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                  - Modified property: max_tres_per_user
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                  - Modified property: min_tres_per_job
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: display_limit_config
                          - New property: transform

GET /api/marketplace-provider-resources/{uuid}/offering_for_subresources/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/marketplace-provider-resources/{uuid}/plan_periods/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/marketplace-provider-resources/{uuid}/pull/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-resources/{uuid}/refresh_last_sync/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-provider-resources/{uuid}/restore/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-provider-resources/{uuid}/robot_account_users/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-resources/{uuid}/set_as_erred/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-provider-resources/{uuid}/set_as_ok/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-provider-resources/{uuid}/set_backend_id/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-provider-resources/{uuid}/set_backend_metadata/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-provider-resources/{uuid}/set_downscaled/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-resources/{uuid}/set_effective_id/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-provider-resources/{uuid}/set_end_date/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-provider-resources/{uuid}/set_end_date_by_provider/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-resources/{uuid}/set_end_date_by_staff/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-resources/{uuid}/set_endpoints/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: endpoints
            - Items changed
              - Properties changed
                - Modified property: url
                  - Format changed from '' to 'uri'
                  - MaxLength changed from null to 200

POST /api/marketplace-provider-resources/{uuid}/set_limits/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-provider-resources/{uuid}/set_membership_sync_statuses/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-provider-resources/{uuid}/set_paused/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-resources/{uuid}/set_restrict_member_access/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-provider-resources/{uuid}/set_slug/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-provider-resources/{uuid}/set_state_ok/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-provider-resources/{uuid}/submit_report/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-provider-resources/{uuid}/sync_user_roles/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-provider-resources/{uuid}/team/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/marketplace-provider-resources/{uuid}/terminate/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-provider-resources/{uuid}/unlink/

- Extensions changed
  - New extension: x-permissions
- Description changed from 'Forcefully deletes a marketplace resource and its related plugin resource from the database. This action does not schedule operations on the backend and is intended for cleaning up resources stuck in transitioning states. Requires staff permissions.' to 'Schedules forced deletion of a marketplace resource and its related plugin resource from the database. This action does not schedule operations on the backend and is intended for cleaning up resources stuck in transitioning states. The resource keeps its state until the deletion finishes. If the deletion fails, it is rolled back and the resource is left in the Erred state with the error recorded. Requires staff permissions.'
- Responses changed
  - New response: 202
  - Deleted response: 204

POST /api/marketplace-provider-resources/{uuid}/update_options/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/description with value: 'Check if user has consented to Terms of Service for the resource's offering.'
    - Added /0/kind with value: 'custom'
    - Removed /0/permission with value: 'RESOURCE.UPDATE_OPTIONS'
    - Removed /0/scopes with value: '[project project.customer offering.customer]'
    - Added /- with value: 'map[kind:permission permission:RESOURCE.UPDATE_OPTIONS scopes:[project project.customer offering.customer]]'
    - Added /- with value: 'map[description:Order authorization for resource option changes. kind:custom]'

POST /api/marketplace-provider-resources/{uuid}/update_options_direct/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-provider-resources/{uuid}/update_user/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-public-api/check_signature/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-public-api/set_usage/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-public-offerings/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [google_calendar_is_public google_calendar_link]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Deleted property: google_calendar_is_public
              - Deleted property: google_calendar_link
              - Modified property: components
                - Items changed
                  - Properties changed
                    - New property: spending_limit_periods
              - Modified property: endpoints
                - Items changed
                  - Properties changed
                    - Modified property: url
                      - Format changed from '' to 'uri'
                      - MaxLength changed from null to 200
              - Modified property: options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - New property: display_limit_config
                            - New property: transform
              - Modified property: plugin_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedPluginOptions
                    - Properties changed
                      - New property: api_key_daily_usage
                      - New property: api_key_limits
                      - New property: display_prepaid_limits_as_total
                      - New property: firecrest_api_url
                      - New property: firecrest_system_name
                      - New property: instance_metrics
                      - New property: instance_metrics_enabled
                      - New property: instance_metrics_poll_interval_minutes
                      - New property: slurm_maintenance_sync_enabled
                      - New property: slurm_monitor_api_url
                      - New property: slurm_monitor_cluster_name
                      - Modified property: account_scope
                        - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'
              - Modified property: qos_profiles
                - Items changed
                  - Properties changed
                    - New property: max_tres_mins_per_job
                    - Modified property: grp_tres
                      - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                    - Modified property: max_tres_per_job
                      - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                    - Modified property: max_tres_per_node
                      - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                    - Modified property: max_tres_per_user
                      - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                    - Modified property: min_tres_per_job
                      - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
              - Modified property: resource_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - New property: display_limit_config
                            - New property: transform

HEAD /api/marketplace-public-offerings/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/marketplace-public-offerings/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [google_calendar_is_public google_calendar_link]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: google_calendar_is_public
            - Deleted property: google_calendar_link
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: spending_limit_periods
            - Modified property: endpoints
              - Items changed
                - Properties changed
                  - Modified property: url
                    - Format changed from '' to 'uri'
                    - MaxLength changed from null to 200
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: display_limit_config
                          - New property: transform
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: api_key_daily_usage
                    - New property: api_key_limits
                    - New property: display_prepaid_limits_as_total
                    - New property: firecrest_api_url
                    - New property: firecrest_system_name
                    - New property: instance_metrics
                    - New property: instance_metrics_enabled
                    - New property: instance_metrics_poll_interval_minutes
                    - New property: slurm_maintenance_sync_enabled
                    - New property: slurm_monitor_api_url
                    - New property: slurm_monitor_cluster_name
                    - Modified property: account_scope
                      - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'
            - Modified property: qos_profiles
              - Items changed
                - Properties changed
                  - New property: max_tres_mins_per_job
                  - Modified property: grp_tres
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                  - Modified property: max_tres_per_job
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                  - Modified property: max_tres_per_node
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                  - Modified property: max_tres_per_user
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                  - Modified property: min_tres_per_job
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: display_limit_config
                          - New property: transform

GET /api/marketplace-public-offerings/{uuid}/plans/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/marketplace-public-offerings/{uuid}/plans/{plan_uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/marketplace-related-customers/{customer_uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-remote-synchronisations/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/marketplace-remote-synchronisations/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/marketplace-remote-synchronisations/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-remote-synchronisations/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-remote-synchronisations/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/marketplace-remote-synchronisations/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/marketplace-remote-synchronisations/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-remote-synchronisations/{uuid}/run_synchronisation/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-resource-api-keys/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: effective_models
              - New required property: limit_resumes_at
              - New required property: spending_limit_status
              - New required property: spending_limits
            - Properties changed
              - New property: description
              - New property: effective_models
              - New property: limit_resumes_at
              - New property: spending_limit_status
              - New property: spending_limits
              - Modified property: allowed_models
                - Description changed from '' to 'The key's own model list, as chosen.'
              - Modified property: limits
                - Description changed from '' to 'The month limits of spending_limits, per component type, for clients that know only monthly limits.'
              - Modified property: paused_by_limit
                - Description changed from '' to 'Waldur paused the key because its usage reached a limit. Such a key is resumed automatically once its usage is under its limits again: when the period of the limit resets, or when a limit is raised. A total limit never resets, so only raising or clearing it does.'

HEAD /api/marketplace-resource-api-keys/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/marketplace-resource-api-keys/

- Extensions changed
  - New extension: x-permissions
- Description changed from 'Asks the site agent to create a key for the resource. Waldur generates nothing: the key appears as Creating and turns OK once the agent reports it. Only on offerings with enable_api_key_provisioning.' to 'Asks the site agent to create a key for the resource. Waldur generates nothing: the key appears as Creating and turns OK once the agent reports it. Only on offerings with enable_api_key_provisioning, and refused with 409 until the agent has created the resource (it has no backend_id yet).'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: description
          - New property: spending_limits
          - Modified property: allowed_models
            - Description changed from 'Models the key may call; empty or absent allows every model.' to 'Models the key may call: ["*"] for every model, an empty list for none. Absent, a new key gets none and an edited one keeps its list.'
            - Nullable changed from true to false
          - Modified property: limits
            - Description changed from 'Limits per component type; zero or absent means no limit.' to 'Month limits per component type; zero or absent means no month limit. Replaces the month limits of spending_limits and keeps the other periods. Not together with spending_limits.'
          - Modified property: user
            - Description changed from 'Assignee. When set, only this user can reveal the key.' to 'Assignee. When set, only this user can reveal the key. It is held until the key is deleted.'
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: effective_models
            - New required property: limit_resumes_at
            - New required property: spending_limit_status
            - New required property: spending_limits
          - Properties changed
            - New property: description
            - New property: effective_models
            - New property: limit_resumes_at
            - New property: spending_limit_status
            - New property: spending_limits
            - Modified property: allowed_models
              - Description changed from '' to 'The key's own model list, as chosen.'
            - Modified property: limits
              - Description changed from '' to 'The month limits of spending_limits, per component type, for clients that know only monthly limits.'
            - Modified property: paused_by_limit
              - Description changed from '' to 'Waldur paused the key because its usage reached a limit. Such a key is resumed automatically once its usage is under its limits again: when the period of the limit resets, or when a limit is raised. A total limit never resets, so only raising or clearing it does.'

POST /api/marketplace-resource-api-keys/report_created/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: effective_models
            - New required property: limit_resumes_at
            - New required property: spending_limit_status
            - New required property: spending_limits
          - Properties changed
            - New property: description
            - New property: effective_models
            - New property: limit_resumes_at
            - New property: spending_limit_status
            - New property: spending_limits
            - Modified property: allowed_models
              - Description changed from '' to 'The key's own model list, as chosen.'
            - Modified property: limits
              - Description changed from '' to 'The month limits of spending_limits, per component type, for clients that know only monthly limits.'
            - Modified property: paused_by_limit
              - Description changed from '' to 'Waldur paused the key because its usage reached a limit. Such a key is resumed automatically once its usage is under its limits again: when the period of the limit resets, or when a limit is raised. A total limit never resets, so only raising or clearing it does.'

GET /api/marketplace-resource-api-keys/usage_totals/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/marketplace-resource-api-keys/usage_totals/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

DELETE /api/marketplace-resource-api-keys/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
    - Modified /0/permission from 'RESOURCE.MANAGE_USERS' to 'RESOURCE.MANAGE_CONSUMER_API_KEY'

GET /api/marketplace-resource-api-keys/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: effective_models
            - New required property: limit_resumes_at
            - New required property: spending_limit_status
            - New required property: spending_limits
          - Properties changed
            - New property: description
            - New property: effective_models
            - New property: limit_resumes_at
            - New property: spending_limit_status
            - New property: spending_limits
            - Modified property: allowed_models
              - Description changed from '' to 'The key's own model list, as chosen.'
            - Modified property: limits
              - Description changed from '' to 'The month limits of spending_limits, per component type, for clients that know only monthly limits.'
            - Modified property: paused_by_limit
              - Description changed from '' to 'Waldur paused the key because its usage reached a limit. Such a key is resumed automatically once its usage is under its limits again: when the period of the limit resets, or when a limit is raised. A total limit never resets, so only raising or clearing it does.'

PATCH /api/marketplace-resource-api-keys/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
    - Modified /0/permission from 'RESOURCE.MANAGE_USERS' to 'RESOURCE.MANAGE_CONSUMER_API_KEY'
- Description changed from 'Changes the key's assignee, limits or model allowlist. A change to limits or models is sent to the site agent as an update command, unless the key is paused: resuming it applies them. Only on offerings with enable_api_key_provisioning, except for unassigning the key ({"user": null}).' to 'Changes the key's limits, model allowlist or description. A change of limits or models is sent to the site agent as an update command, unless the key is paused: resuming it applies them. The key's assignee is set when the key is requested and cannot be changed: an edit that names user, null included, is refused with 400. To hand a key to someone else, request a key for them and delete this one. Only on offerings with enable_api_key_provisioning, except an edit of the description alone: that is saved at once on any offering and in any state but Deleted, sends no command and leaves the key's state as it is.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: description
          - New property: spending_limits
          - Deleted property: user
          - Modified property: allowed_models
            - Description changed from 'Models the key may call; empty or absent allows every model.' to 'Models the key may call: ["*"] for every model, an empty list for none. Absent, a new key gets none and an edited one keeps its list.'
            - Nullable changed from true to false
          - Modified property: limits
            - Description changed from 'Limits per component type; zero or absent means no limit.' to 'Month limits per component type; zero or absent means no month limit. Replaces the month limits of spending_limits and keeps the other periods. Not together with spending_limits.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: effective_models
            - New required property: limit_resumes_at
            - New required property: spending_limit_status
            - New required property: spending_limits
          - Properties changed
            - New property: description
            - New property: effective_models
            - New property: limit_resumes_at
            - New property: spending_limit_status
            - New property: spending_limits
            - Modified property: allowed_models
              - Description changed from '' to 'The key's own model list, as chosen.'
            - Modified property: limits
              - Description changed from '' to 'The month limits of spending_limits, per component type, for clients that know only monthly limits.'
            - Modified property: paused_by_limit
              - Description changed from '' to 'Waldur paused the key because its usage reached a limit. Such a key is resumed automatically once its usage is under its limits again: when the period of the limit resets, or when a limit is raised. A total limit never resets, so only raising or clearing it does.'

POST /api/marketplace-resource-api-keys/{uuid}/pause/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
    - Modified /0/permission from 'RESOURCE.MANAGE_USERS' to 'RESOURCE.MANAGE_CONSUMER_API_KEY'

POST /api/marketplace-resource-api-keys/{uuid}/report_usage/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
- Description changed from 'Used by the site agent to report a key's usage so far in a month, per component type. Merged into the key's usage for that month; a later month replaces it, and an earlier one is refused. A key whose usage reaches its limit is paused, and a key paused for its limit is resumed once under it again. Accepted for a deleted key too.' to 'Used by the site agent to report a key's usage so far in a month, per component type, and its usage per day. A month report is merged into the key's usage for that month; a later month replaces it, and an earlier one is refused. A date reported again replaces its amount, and the month's usage of a component with daily amounts is their sum. A key whose usage reaches a limit is paused, and a key paused for its limit is resumed once under it again. Accepted for a deleted key too.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: usages
        - Properties changed
          - New property: daily_usages
          - Modified property: billing_period
            - Description changed from 'Any day of the month the usage belongs to; the current month when omitted. Limits are monthly, so a later month starts them afresh.' to 'Any day of the month usages belongs to; the current month when omitted. A later month than the key holds starts afresh. An earlier one, from the start of the current year or of the previous month when that is earlier, raises that month's figure for a total limit; older ones are refused.'
          - Modified property: usages
            - Description changed from 'The key's usage so far in billing_period, per component type.' to 'The key's usage so far in billing_period, per component type. A figure never drops: one lower than the key holds for the month leaves the higher one. Rejected for a component that has daily amounts in that month.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: effective_models
            - New required property: limit_resumes_at
            - New required property: spending_limit_status
            - New required property: spending_limits
          - Properties changed
            - New property: description
            - New property: effective_models
            - New property: limit_resumes_at
            - New property: spending_limit_status
            - New property: spending_limits
            - Modified property: allowed_models
              - Description changed from '' to 'The key's own model list, as chosen.'
            - Modified property: limits
              - Description changed from '' to 'The month limits of spending_limits, per component type, for clients that know only monthly limits.'
            - Modified property: paused_by_limit
              - Description changed from '' to 'Waldur paused the key because its usage reached a limit. Such a key is resumed automatically once its usage is under its limits again: when the period of the limit resets, or when a limit is raised. A total limit never resets, so only raising or clearing it does.'

POST /api/marketplace-resource-api-keys/{uuid}/resume/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
    - Modified /0/permission from 'RESOURCE.MANAGE_USERS' to 'RESOURCE.MANAGE_CONSUMER_API_KEY'

POST /api/marketplace-resource-api-keys/{uuid}/retry/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'any_of'
    - Added /0/of with value: '[map[description:Admit the key's assignee, who is already trusted with its value. kind:custom] map[kind:permission permission:RESOURCE.MANAGE_CONSUMER_API_KEY scopes:[resource.project resource.project.customer]]]'
    - Removed /0/permission with value: 'RESOURCE.MANAGE_USERS'
    - Removed /0/scopes with value: '[resource.project resource.project.customer]'
- Description changed from 'Sends the command that left the key Erred to the site agent again, with the key's current limits and models. An Erred key accepts only this, the same command, or a delete.' to 'Sends the command that left the key Erred to the site agent again, with the key's current limits and models. An Erred key accepts only this, the same command, or a delete. The key's assignee can retry a failed rotation, and no other command.'

GET /api/marketplace-resource-api-keys/{uuid}/reveal/

- Extensions changed
  - New extension: x-permissions
- Description changed from 'Returns the decrypted key value. Available to users with resource access (except minimal-visibility viewers); a key with an assignee only to the assignee. Staff and support always. Audit-logged.' to 'Returns the decrypted key value. Available to members of the resource's project or organization (except minimal-visibility viewers); a key with an assignee only to the assignee. Staff and support are no exception: staff reveal a key by impersonating a user who may. Audit-logged; under impersonation the event names the impersonator.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: effective_models
            - New required property: limit_resumes_at
            - New required property: spending_limit_status
            - New required property: spending_limits
          - Properties changed
            - New property: description
            - New property: effective_models
            - New property: limit_resumes_at
            - New property: spending_limit_status
            - New property: spending_limits
            - Modified property: allowed_models
              - Description changed from '' to 'The key's own model list, as chosen.'
            - Modified property: limits
              - Description changed from '' to 'The month limits of spending_limits, per component type, for clients that know only monthly limits.'
            - Modified property: paused_by_limit
              - Description changed from '' to 'Waldur paused the key because its usage reached a limit. Such a key is resumed automatically once its usage is under its limits again: when the period of the limit resets, or when a limit is raised. A total limit never resets, so only raising or clearing it does.'

POST /api/marketplace-resource-api-keys/{uuid}/rotate/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'any_of'
    - Added /0/of with value: '[map[description:Admit the key's assignee, who is already trusted with its value. kind:custom] map[kind:permission permission:RESOURCE.MANAGE_CONSUMER_API_KEY scopes:[resource.project resource.project.customer]]]'
    - Removed /0/permission with value: 'RESOURCE.MANAGE_USERS'
    - Removed /0/scopes with value: '[resource.project resource.project.customer]'
- Description changed from 'Asks the site agent to replace this key's value at the backend. The other keys are untouched (zero downtime).' to 'Asks the site agent to replace this key's value at the backend. The other keys are untouched (zero downtime). Available to whoever manages the resource's API keys and to the key's assignee.'

POST /api/marketplace-resource-api-keys/{uuid}/set_deleted/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: effective_models
            - New required property: limit_resumes_at
            - New required property: spending_limit_status
            - New required property: spending_limits
          - Properties changed
            - New property: description
            - New property: effective_models
            - New property: limit_resumes_at
            - New property: spending_limit_status
            - New property: spending_limits
            - Modified property: allowed_models
              - Description changed from '' to 'The key's own model list, as chosen.'
            - Modified property: limits
              - Description changed from '' to 'The month limits of spending_limits, per component type, for clients that know only monthly limits.'
            - Modified property: paused_by_limit
              - Description changed from '' to 'Waldur paused the key because its usage reached a limit. Such a key is resumed automatically once its usage is under its limits again: when the period of the limit resets, or when a limit is raised. A total limit never resets, so only raising or clearing it does.'

POST /api/marketplace-resource-api-keys/{uuid}/set_erred/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: effective_models
            - New required property: limit_resumes_at
            - New required property: spending_limit_status
            - New required property: spending_limits
          - Properties changed
            - New property: description
            - New property: effective_models
            - New property: limit_resumes_at
            - New property: spending_limit_status
            - New property: spending_limits
            - Modified property: allowed_models
              - Description changed from '' to 'The key's own model list, as chosen.'
            - Modified property: limits
              - Description changed from '' to 'The month limits of spending_limits, per component type, for clients that know only monthly limits.'
            - Modified property: paused_by_limit
              - Description changed from '' to 'Waldur paused the key because its usage reached a limit. Such a key is resumed automatically once its usage is under its limits again: when the period of the limit resets, or when a limit is raised. A total limit never resets, so only raising or clearing it does.'

POST /api/marketplace-resource-api-keys/{uuid}/set_key/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: effective_models
            - New required property: limit_resumes_at
            - New required property: spending_limit_status
            - New required property: spending_limits
          - Properties changed
            - New property: description
            - New property: effective_models
            - New property: limit_resumes_at
            - New property: spending_limit_status
            - New property: spending_limits
            - Modified property: allowed_models
              - Description changed from '' to 'The key's own model list, as chosen.'
            - Modified property: limits
              - Description changed from '' to 'The month limits of spending_limits, per component type, for clients that know only monthly limits.'
            - Modified property: paused_by_limit
              - Description changed from '' to 'Waldur paused the key because its usage reached a limit. Such a key is resumed automatically once its usage is under its limits again: when the period of the limit resets, or when a limit is raised. A total limit never resets, so only raising or clearing it does.'

POST /api/marketplace-resource-api-keys/{uuid}/set_ok/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: effective_models
            - New required property: limit_resumes_at
            - New required property: spending_limit_status
            - New required property: spending_limits
          - Properties changed
            - New property: description
            - New property: effective_models
            - New property: limit_resumes_at
            - New property: spending_limit_status
            - New property: spending_limits
            - Modified property: allowed_models
              - Description changed from '' to 'The key's own model list, as chosen.'
            - Modified property: limits
              - Description changed from '' to 'The month limits of spending_limits, per component type, for clients that know only monthly limits.'
            - Modified property: paused_by_limit
              - Description changed from '' to 'Waldur paused the key because its usage reached a limit. Such a key is resumed automatically once its usage is under its limits again: when the period of the limit resets, or when a limit is raised. A total limit never resets, so only raising or clearing it does.'

POST /api/marketplace-resource-api-keys/{uuid}/set_paused/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: effective_models
            - New required property: limit_resumes_at
            - New required property: spending_limit_status
            - New required property: spending_limits
          - Properties changed
            - New property: description
            - New property: effective_models
            - New property: limit_resumes_at
            - New property: spending_limit_status
            - New property: spending_limits
            - Modified property: allowed_models
              - Description changed from '' to 'The key's own model list, as chosen.'
            - Modified property: limits
              - Description changed from '' to 'The month limits of spending_limits, per component type, for clients that know only monthly limits.'
            - Modified property: paused_by_limit
              - Description changed from '' to 'Waldur paused the key because its usage reached a limit. Such a key is resumed automatically once its usage is under its limits again: when the period of the limit resets, or when a limit is raised. A total limit never resets, so only raising or clearing it does.'

GET /api/marketplace-resource-end-date-change-requests/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/marketplace-resource-end-date-change-requests/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/marketplace-resource-end-date-change-requests/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-resource-end-date-change-requests/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/marketplace-resource-end-date-change-requests/{uuid}/approve/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-resource-end-date-change-requests/{uuid}/cancel/

- Extensions changed
  - New extension: x-permissions
- Request body changed

POST /api/marketplace-resource-end-date-change-requests/{uuid}/reject/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-resource-end-date-change-requests/{uuid}/set_backend_id/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-resource-limit-change-requests/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/marketplace-resource-limit-change-requests/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/marketplace-resource-limit-change-requests/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-resource-limit-change-requests/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/marketplace-resource-limit-change-requests/{uuid}/approve/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-resource-limit-change-requests/{uuid}/cancel/

- Extensions changed
  - New extension: x-permissions
- Request body changed

POST /api/marketplace-resource-limit-change-requests/{uuid}/reject/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-resource-metrics/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-resource-offerings/{category_uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-resource-projects/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/marketplace-resource-projects/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/marketplace-resource-projects/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-resource-projects/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-resource-projects/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

PATCH /api/marketplace-resource-projects/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

PUT /api/marketplace-resource-projects/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-resource-projects/{uuid}/add_user/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-resource-projects/{uuid}/delete_user/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-resource-projects/{uuid}/list_users/

- Extensions changed
  - New extension: x-permissions
- New query param: role_template

HEAD /api/marketplace-resource-projects/{uuid}/list_users/

- Extensions changed
  - New extension: x-permissions
- New query param: role_template

POST /api/marketplace-resource-projects/{uuid}/recover/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-resource-projects/{uuid}/update_user/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-resources/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [display_limits prepaid_total_component_types spending_limit_status spending_limits terminated_at usage_limit_resumes_at]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: display_limits
              - New property: prepaid_total_component_types
              - New property: spending_limit_status
              - New property: spending_limits
              - New property: terminated_at
              - New property: usage_limit_resumes_at
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Deleted property: callback_url
              - Modified property: endpoints
                - Items changed
                  - Properties changed
                    - Modified property: url
                      - Format changed from '' to 'uri'
                      - MaxLength changed from null to 200
              - Modified property: offering_components
                - Items changed
                  - Properties changed
                    - New property: spending_limit_periods
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Deleted property: callback_url

HEAD /api/marketplace-resources/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/marketplace-resources/suggest_name/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-resources/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [display_limits prepaid_total_component_types spending_limit_status spending_limits terminated_at usage_limit_resumes_at]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: display_limits
            - New property: prepaid_total_component_types
            - New property: spending_limit_status
            - New property: spending_limits
            - New property: terminated_at
            - New property: usage_limit_resumes_at
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: callback_url
            - Modified property: endpoints
              - Items changed
                - Properties changed
                  - Modified property: url
                    - Format changed from '' to 'uri'
                    - MaxLength changed from null to 200
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: spending_limit_periods
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: callback_url

PATCH /api/marketplace-resources/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

PUT /api/marketplace-resources/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-resources/{uuid}/add_user/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-resources/{uuid}/adjust_dates/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-resources/{uuid}/delete_user/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-resources/{uuid}/details/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/marketplace-resources/{uuid}/estimate_renewal/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-resources/{uuid}/history/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-resources/{uuid}/history/at/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-resources/{uuid}/list_users/

- Extensions changed
  - New extension: x-permissions
- New query param: role_template

HEAD /api/marketplace-resources/{uuid}/list_users/

- Extensions changed
  - New extension: x-permissions
- New query param: role_template

POST /api/marketplace-resources/{uuid}/move_resource/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: display_limits
            - New property: prepaid_total_component_types
            - New property: spending_limit_status
            - New property: spending_limits
            - New property: terminated_at
            - New property: usage_limit_resumes_at
            - Modified property: creation_order
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: callback_url
            - Modified property: endpoints
              - Items changed
                - Properties changed
                  - Modified property: url
                    - Format changed from '' to 'uri'
                    - MaxLength changed from null to 200
            - Modified property: offering_components
              - Items changed
                - Properties changed
                  - New property: spending_limit_periods
            - Modified property: order_in_progress
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OrderDetails
                  - Properties changed
                    - Deleted property: callback_url

GET /api/marketplace-resources/{uuid}/offering/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Modified query param: field
  - Schema changed
    - Items changed
      - Deleted enum values: [google_calendar_is_public google_calendar_link]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Deleted property: google_calendar_is_public
            - Deleted property: google_calendar_link
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: spending_limit_periods
            - Modified property: endpoints
              - Items changed
                - Properties changed
                  - Modified property: url
                    - Format changed from '' to 'uri'
                    - MaxLength changed from null to 200
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: display_limit_config
                          - New property: transform
            - Modified property: plugin_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/MergedPluginOptions
                  - Properties changed
                    - New property: api_key_daily_usage
                    - New property: api_key_limits
                    - New property: display_prepaid_limits_as_total
                    - New property: firecrest_api_url
                    - New property: firecrest_system_name
                    - New property: instance_metrics
                    - New property: instance_metrics_enabled
                    - New property: instance_metrics_poll_interval_minutes
                    - New property: slurm_maintenance_sync_enabled
                    - New property: slurm_monitor_api_url
                    - New property: slurm_monitor_cluster_name
                    - Modified property: account_scope
                      - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'
            - Modified property: qos_profiles
              - Items changed
                - Properties changed
                  - New property: max_tres_mins_per_job
                  - Modified property: grp_tres
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                  - Modified property: max_tres_per_job
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                  - Modified property: max_tres_per_node
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                  - Modified property: max_tres_per_user
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
                  - Modified property: min_tres_per_job
                    - Pattern changed from '' to '^([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?(,([A-Za-z][\w/:.@-]*|[1-9]\d*)=\d+[KMGTPkmgtp]?)*$'
            - Modified property: resource_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: display_limit_config
                          - New property: transform

GET /api/marketplace-resources/{uuid}/offering_for_subresources/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/marketplace-resources/{uuid}/plan_periods/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/marketplace-resources/{uuid}/pull/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-resources/{uuid}/reallocate_limits/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/description with value: 'Check if user has consented to Terms of Service for the resource's offering.'
    - Added /0/kind with value: 'custom'
    - Removed /0/permission with value: 'RESOURCE.SET_LIMITS'
    - Removed /0/scopes with value: '[project project.customer]'
    - Added /- with value: 'map[kind:permission permission:RESOURCE.SET_LIMITS scopes:[project project.customer]]'
    - Added /- with value: 'map[description:Authorize the order a resource action is about to create. kind:custom]'

POST /api/marketplace-resources/{uuid}/renew/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/description with value: 'Check if user has consented to Terms of Service for the resource's offering.'
    - Added /0/kind with value: 'custom'
    - Removed /0/permission with value: 'RESOURCE.SET_LIMITS'
    - Removed /0/scopes with value: '[project project.customer]'
    - Added /- with value: 'map[kind:permission permission:RESOURCE.SET_LIMITS scopes:[project project.customer]]'
    - Added /- with value: 'map[description:Authorize the order a resource action is about to create. kind:custom]'

POST /api/marketplace-resources/{uuid}/restore/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-resources/{uuid}/set_downscaled/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-resources/{uuid}/set_end_date/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-resources/{uuid}/set_end_date_by_staff/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-resources/{uuid}/set_paused/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-resources/{uuid}/set_restrict_member_access/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-resources/{uuid}/set_slug/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-resources/{uuid}/switch_plan/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/description with value: 'Check if user has consented to Terms of Service for the resource's offering.'
    - Added /0/kind with value: 'custom'
    - Removed /0/permission with value: 'RESOURCE.SET_PLAN'
    - Removed /0/scopes with value: '[project project.customer]'
    - Added /- with value: 'map[kind:permission permission:RESOURCE.SET_PLAN scopes:[project project.customer]]'
    - Added /- with value: 'map[description:Authorize the order a resource action is about to create. kind:custom]'

GET /api/marketplace-resources/{uuid}/team/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/marketplace-resources/{uuid}/team_members/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-resources/{uuid}/terminate/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-resources/{uuid}/unlink/

- Extensions changed
  - New extension: x-permissions
- Description changed from 'Forcefully deletes a marketplace resource and its related plugin resource from the database. This action does not schedule operations on the backend and is intended for cleaning up resources stuck in transitioning states. Requires staff permissions.' to 'Schedules forced deletion of a marketplace resource and its related plugin resource from the database. This action does not schedule operations on the backend and is intended for cleaning up resources stuck in transitioning states. The resource keeps its state until the deletion finishes. If the deletion fails, it is rolled back and the resource is left in the Erred state with the error recorded. Requires staff permissions.'
- Responses changed
  - New response: 202
  - Deleted response: 204

POST /api/marketplace-resources/{uuid}/update_limits/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/description with value: 'Check if user has consented to Terms of Service for the resource's offering.'
    - Added /0/kind with value: 'custom'
    - Removed /0/permission with value: 'RESOURCE.SET_LIMITS'
    - Removed /0/scopes with value: '[project project.customer]'
    - Added /- with value: 'map[kind:permission permission:RESOURCE.SET_LIMITS scopes:[project project.customer]]'
    - Added /- with value: 'map[description:Authorize the order a resource action is about to create. kind:custom]'

POST /api/marketplace-resources/{uuid}/update_options/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/description with value: 'Check if user has consented to Terms of Service for the resource's offering.'
    - Added /0/kind with value: 'custom'
    - Removed /0/permission with value: 'RESOURCE.UPDATE_OPTIONS'
    - Removed /0/scopes with value: '[project project.customer offering.customer]'
    - Added /- with value: 'map[kind:permission permission:RESOURCE.UPDATE_OPTIONS scopes:[project project.customer offering.customer]]'
    - Added /- with value: 'map[description:Order authorization for resource option changes. kind:custom]'

POST /api/marketplace-resources/{uuid}/update_user/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-robot-accounts/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
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
                      - New property: api_key_daily_usage
                      - New property: api_key_limits
                      - New property: display_prepaid_limits_as_total
                      - New property: firecrest_api_url
                      - New property: firecrest_system_name
                      - New property: instance_metrics
                      - New property: instance_metrics_enabled
                      - New property: instance_metrics_poll_interval_minutes
                      - New property: slurm_maintenance_sync_enabled
                      - New property: slurm_monitor_api_url
                      - New property: slurm_monitor_cluster_name
                      - Modified property: account_scope
                        - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'

HEAD /api/marketplace-robot-accounts/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/marketplace-robot-accounts/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-robot-accounts/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-robot-accounts/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
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
                    - New property: api_key_daily_usage
                    - New property: api_key_limits
                    - New property: display_prepaid_limits_as_total
                    - New property: firecrest_api_url
                    - New property: firecrest_system_name
                    - New property: instance_metrics
                    - New property: instance_metrics_enabled
                    - New property: instance_metrics_poll_interval_minutes
                    - New property: slurm_maintenance_sync_enabled
                    - New property: slurm_monitor_api_url
                    - New property: slurm_monitor_cluster_name
                    - Modified property: account_scope
                      - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'

PATCH /api/marketplace-robot-accounts/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/marketplace-robot-accounts/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-robot-accounts/{uuid}/set_state_creating/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
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
                    - New property: api_key_daily_usage
                    - New property: api_key_limits
                    - New property: display_prepaid_limits_as_total
                    - New property: firecrest_api_url
                    - New property: firecrest_system_name
                    - New property: instance_metrics
                    - New property: instance_metrics_enabled
                    - New property: instance_metrics_poll_interval_minutes
                    - New property: slurm_maintenance_sync_enabled
                    - New property: slurm_monitor_api_url
                    - New property: slurm_monitor_cluster_name
                    - Modified property: account_scope
                      - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'

POST /api/marketplace-robot-accounts/{uuid}/set_state_deleted/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
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
                    - New property: api_key_daily_usage
                    - New property: api_key_limits
                    - New property: display_prepaid_limits_as_total
                    - New property: firecrest_api_url
                    - New property: firecrest_system_name
                    - New property: instance_metrics
                    - New property: instance_metrics_enabled
                    - New property: instance_metrics_poll_interval_minutes
                    - New property: slurm_maintenance_sync_enabled
                    - New property: slurm_monitor_api_url
                    - New property: slurm_monitor_cluster_name
                    - Modified property: account_scope
                      - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'

POST /api/marketplace-robot-accounts/{uuid}/set_state_erred/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
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
                    - New property: api_key_daily_usage
                    - New property: api_key_limits
                    - New property: display_prepaid_limits_as_total
                    - New property: firecrest_api_url
                    - New property: firecrest_system_name
                    - New property: instance_metrics
                    - New property: instance_metrics_enabled
                    - New property: instance_metrics_poll_interval_minutes
                    - New property: slurm_maintenance_sync_enabled
                    - New property: slurm_monitor_api_url
                    - New property: slurm_monitor_cluster_name
                    - Modified property: account_scope
                      - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'

POST /api/marketplace-robot-accounts/{uuid}/set_state_ok/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
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
                    - New property: api_key_daily_usage
                    - New property: api_key_limits
                    - New property: display_prepaid_limits_as_total
                    - New property: firecrest_api_url
                    - New property: firecrest_system_name
                    - New property: instance_metrics
                    - New property: instance_metrics_enabled
                    - New property: instance_metrics_poll_interval_minutes
                    - New property: slurm_maintenance_sync_enabled
                    - New property: slurm_monitor_api_url
                    - New property: slurm_monitor_cluster_name
                    - Modified property: account_scope
                      - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'

POST /api/marketplace-robot-accounts/{uuid}/set_state_request_deletion/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
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
                    - New property: api_key_daily_usage
                    - New property: api_key_limits
                    - New property: display_prepaid_limits_as_total
                    - New property: firecrest_api_url
                    - New property: firecrest_system_name
                    - New property: instance_metrics
                    - New property: instance_metrics_enabled
                    - New property: instance_metrics_poll_interval_minutes
                    - New property: slurm_maintenance_sync_enabled
                    - New property: slurm_monitor_api_url
                    - New property: slurm_monitor_cluster_name
                    - Modified property: account_scope
                      - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'

GET /api/marketplace-runtime-states/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-screenshots/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-screenshots/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-screenshots/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-screenshots/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-screenshots/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/marketplace-screenshots/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/marketplace-screenshots/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-script-async-dry-run/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/marketplace-script-async-dry-run/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/marketplace-script-async-dry-run/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/marketplace-script-dry-run/{uuid}/async_run/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-script-dry-run/{uuid}/run/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-script-sync-resource/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-sections/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-sections/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-sections/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-sections/{key}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-sections/{key}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/marketplace-sections/{key}/

- Extensions changed
  - New extension: x-permissions

PUT /api/marketplace-sections/{key}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-service-provider-accounts/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/marketplace-service-provider-accounts/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

DELETE /api/marketplace-service-provider-accounts/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-service-provider-accounts/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

PATCH /api/marketplace-service-provider-accounts/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

PUT /api/marketplace-service-provider-accounts/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-service-provider-project-groups/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/marketplace-service-provider-project-groups/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/marketplace-service-provider-project-groups/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-service-provider-project-groups/adoptable_projects/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-service-provider-project-groups/adoptable_projects/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-service-provider-project-groups/import_groups/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-service-provider-project-groups/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/marketplace-service-provider-project-groups/{uuid}/set_gid/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-service-providers/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: account_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/ProviderAccountOptions
                    - Properties changed
                      - Modified property: account_scope
                        - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'

HEAD /api/marketplace-service-providers/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-service-providers/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: account_options
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/ProviderAccountOptionsRequest
                - Properties changed
                  - Modified property: account_scope
                    - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: account_options
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/ProviderAccountOptionsRequest
                - Properties changed
                  - Modified property: account_scope
                    - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: account_options
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/ProviderAccountOptionsRequest
                - Properties changed
                  - Modified property: account_scope
                    - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: account_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ProviderAccountOptions
                  - Properties changed
                    - Modified property: account_scope
                      - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'

GET /api/marketplace-service-providers/{service_provider_uuid}/compliance/checklists_summary/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-service-providers/{service_provider_uuid}/compliance/checklists_summary/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-service-providers/{service_provider_uuid}/compliance/compliance_overview/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-service-providers/{service_provider_uuid}/compliance/compliance_overview/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-service-providers/{service_provider_uuid}/compliance/offering_users/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-service-providers/{service_provider_uuid}/compliance/offering_users/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-service-providers/{service_provider_uuid}/course_accounts/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-service-providers/{service_provider_uuid}/course_accounts/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-service-providers/{service_provider_uuid}/customer_projects/

- Extensions changed
  - New extension: x-permissions
- New query param: user_role

HEAD /api/marketplace-service-providers/{service_provider_uuid}/customer_projects/

- Extensions changed
  - New extension: x-permissions
- New query param: user_role

GET /api/marketplace-service-providers/{service_provider_uuid}/customers/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-service-providers/{service_provider_uuid}/customers/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-service-providers/{service_provider_uuid}/keys/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-service-providers/{service_provider_uuid}/keys/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-service-providers/{service_provider_uuid}/offerings/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
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
                    - New property: spending_limit_periods
              - Modified property: secret_options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/MergedSecretOptions
                    - Properties changed
                      - Modified property: backend_url
                        - Format changed from '' to 'uri'

HEAD /api/marketplace-service-providers/{service_provider_uuid}/offerings/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/marketplace-service-providers/{service_provider_uuid}/offerings/types/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/marketplace-service-providers/{service_provider_uuid}/offerings/types/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/marketplace-service-providers/{service_provider_uuid}/project_permissions/

- Extensions changed
  - New extension: x-permissions
- Modified query param: scope_type
  - Description changed from 'Scope type' to 'Scope type, as returned in scope_type: customer, project, offering, service_provider, call_organizer, call, proposal, resource, resource_project or global. A content type model name also matches.'

HEAD /api/marketplace-service-providers/{service_provider_uuid}/project_permissions/

- Extensions changed
  - New extension: x-permissions
- Modified query param: scope_type
  - Description changed from 'Scope type' to 'Scope type, as returned in scope_type: customer, project, offering, service_provider, call_organizer, call, proposal, resource, resource_project or global. A content type model name also matches.'

GET /api/marketplace-service-providers/{service_provider_uuid}/project_service_accounts/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: error_traceback
              - New required property: username
            - Properties changed
              - Modified property: error_traceback
                - ReadOnly changed from false to true
              - Modified property: username
                - ReadOnly changed from false to true
                - MaxLength changed from 32 to null

HEAD /api/marketplace-service-providers/{service_provider_uuid}/project_service_accounts/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-service-providers/{service_provider_uuid}/projects/

- Extensions changed
  - New extension: x-permissions
- New query param: user_role
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [user_assurance_levels user_nationalities user_organization_types]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: user_assurance_levels
              - New property: user_nationalities
              - New property: user_organization_types
              - Modified property: project_metadata
                - Items changed
                  - Properties changed
                    - New property: likert_high_label
                    - New property: likert_low_label
                    - New property: likert_scale_length
                    - New property: max_value
                    - New property: min_value

HEAD /api/marketplace-service-providers/{service_provider_uuid}/projects/

- Extensions changed
  - New extension: x-permissions
- New query param: user_role

GET /api/marketplace-service-providers/{service_provider_uuid}/user_customers/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-service-providers/{service_provider_uuid}/user_customers/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-service-providers/{service_provider_uuid}/users/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-service-providers/{service_provider_uuid}/users/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-service-providers/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-service-providers/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: account_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ProviderAccountOptions
                  - Properties changed
                    - Modified property: account_scope
                      - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'

PATCH /api/marketplace-service-providers/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: account_options
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/ProviderAccountOptionsRequest
                - Properties changed
                  - Modified property: account_scope
                    - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: account_options
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/ProviderAccountOptionsRequest
                - Properties changed
                  - Modified property: account_scope
                    - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: account_options
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/ProviderAccountOptionsRequest
                - Properties changed
                  - Modified property: account_scope
                    - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: account_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ProviderAccountOptions
                  - Properties changed
                    - Modified property: account_scope
                      - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'

PUT /api/marketplace-service-providers/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: account_options
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/ProviderAccountOptionsRequest
                - Properties changed
                  - Modified property: account_scope
                    - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - Modified property: account_options
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/ProviderAccountOptionsRequest
                - Properties changed
                  - Modified property: account_scope
                    - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - Modified property: account_options
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/ProviderAccountOptionsRequest
                - Properties changed
                  - Modified property: account_scope
                    - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: account_options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/ProviderAccountOptions
                  - Properties changed
                    - Modified property: account_scope
                      - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'

POST /api/marketplace-service-providers/{uuid}/account_options_preview/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: account_options
            - Property 'AllOf' changed
              - Modified schema: #/components/schemas/ProviderAccountOptionsRequest
                - Properties changed
                  - Modified property: account_scope
                    - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: account_options
              - Properties changed
                - Modified property: current
                  - Properties changed
                    - Modified property: account_scope
                      - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'
                - Modified property: proposed
                  - Properties changed
                    - Modified property: account_scope
                      - Description changed from 'Where accounts are held: 'offering' keeps one account per offering (the historical behaviour); 'provider' shares one account per user across the provider's offerings.' to 'Where accounts are held: 'offering' keeps one account per offering (the historical behavior); 'provider' shares one account per user across the provider's offerings.'

POST /api/marketplace-service-providers/{uuid}/add_user/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-service-providers/{uuid}/adopt_provider_accounts/

- Extensions changed
  - New extension: x-permissions
- Description changed from 'Backs every offering account at this provider with one provider-level account per user, so a person resolves to a single username and POSIX identity across the provider's offerings.

Users whose accounts already agree are adopted without input. A user whose accounts disagree must be given a surviving username in 'resolutions', keyed by user UUID — see the 'username_conflicts' action. The call is refused while any conflict is unresolved, rather than adopting part of the provider and leaving the rest on the old per-offering behaviour.' to 'Backs every offering account at this provider with one provider-level account per user, so a person resolves to a single username and POSIX identity across the provider's offerings.

Users whose accounts already agree are adopted without input. A user whose accounts disagree must be given a surviving username in 'resolutions', keyed by user UUID — see the 'username_conflicts' action. The call is refused while any conflict is unresolved, rather than adopting part of the provider and leaving the rest on the old per-offering behavior.'

GET /api/marketplace-service-providers/{uuid}/api_secret_code/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-service-providers/{uuid}/api_secret_code/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-service-providers/{uuid}/delete_user/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-service-providers/{uuid}/generate_site_agent_config/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-service-providers/{uuid}/glauth_tree/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-service-providers/{uuid}/glauth_users_config/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-service-providers/{uuid}/list_users/

- Extensions changed
  - New extension: x-permissions
- New query param: role_template

HEAD /api/marketplace-service-providers/{uuid}/list_users/

- Extensions changed
  - New extension: x-permissions
- New query param: role_template

GET /api/marketplace-service-providers/{uuid}/revenue/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'any_of'
    - Added /0/of with value: '[map[kind:staff_or_support] map[kind:permission permission:SERVICE_PROVIDER.GET_REVENUE scopes:[* customer]]]'
    - Removed /0/permission with value: 'SERVICE_PROVIDER.GET_REVENUE'
    - Removed /0/scopes with value: '[* customer]'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: total
                - Type changed from 'integer' to 'number'
                - Format changed from '' to 'double'

GET /api/marketplace-service-providers/{uuid}/robot_account_customers/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-service-providers/{uuid}/robot_account_projects/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/marketplace-service-providers/{uuid}/set_offerings_username/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/marketplace-service-providers/{uuid}/stat/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'any_of'
    - Added /0/of with value: '[map[kind:staff_or_support] map[kind:permission permission:SERVICE_PROVIDER.GET_STATISTICS scopes:[* customer]]]'
    - Removed /0/permission with value: 'SERVICE_PROVIDER.GET_STATISTICS'
    - Removed /0/scopes with value: '[* customer]'

POST /api/marketplace-service-providers/{uuid}/update_user/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-service-providers/{uuid}/username_conflicts/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-site-agent-connection-stats/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: agents
              - Items changed
                - Properties changed
                  - Modified property: authorized_via
                    - Description changed from 'Permission branch that authorised the registration' to 'Permission branch that authorized the registration'

GET /api/marketplace-site-agent-identities/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: config_file_content
                - Description changed from '' to 'Returned only to staff, to who holds OFFERING.UPDATE on the identity's offering, its organization or its service provider, and to the identity manager who created the identity, while the offering is in an ISD-allowed state.'

HEAD /api/marketplace-site-agent-identities/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/marketplace-site-agent-identities/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: config_file_content
            - Description changed from '' to 'Returned only to staff, to who holds OFFERING.UPDATE on the identity's offering, its organization or its service provider, and to the identity manager who created the identity, while the offering is in an ISD-allowed state.'
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: config_file_content
              - Description changed from '' to 'Returned only to staff, to who holds OFFERING.UPDATE on the identity's offering, its organization or its service provider, and to the identity manager who created the identity, while the offering is in an ISD-allowed state.'

POST /api/marketplace-site-agent-identities/cleanup_orphaned/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-site-agent-identities/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-site-agent-identities/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: config_file_content
              - Description changed from '' to 'Returned only to staff, to who holds OFFERING.UPDATE on the identity's offering, its organization or its service provider, and to the identity manager who created the identity, while the offering is in an ISD-allowed state.'

PUT /api/marketplace-site-agent-identities/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: config_file_content
            - Description changed from '' to 'Returned only to staff, to who holds OFFERING.UPDATE on the identity's offering, its organization or its service provider, and to the identity manager who created the identity, while the offering is in an ISD-allowed state.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: config_file_content
              - Description changed from '' to 'Returned only to staff, to who holds OFFERING.UPDATE on the identity's offering, its organization or its service provider, and to the identity manager who created the identity, while the offering is in an ISD-allowed state.'

POST /api/marketplace-site-agent-identities/{uuid}/register_event_subscription/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: source_ip
              - Property 'OneOf' changed
                - Schemas deleted: subschema #1, subschema #2
              - Type changed from '' to 'string'
              - Format changed from '' to 'ipv4'
              - Description changed from 'An IPv4 or IPv6 address.' to ''
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: source_ip
              - Property 'OneOf' changed
                - Schemas deleted: subschema #1, subschema #2
              - Type changed from '' to 'string'
              - Format changed from '' to 'ipv4'
              - Description changed from 'An IPv4 or IPv6 address.' to ''

POST /api/marketplace-site-agent-identities/{uuid}/register_queue/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-site-agent-identities/{uuid}/register_service/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-site-agent-logs/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/marketplace-site-agent-logs/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/marketplace-site-agent-logs/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-site-agent-processors/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/marketplace-site-agent-processors/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

DELETE /api/marketplace-site-agent-processors/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-site-agent-processors/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/marketplace-site-agent-services/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/marketplace-site-agent-services/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/marketplace-site-agent-services/cleanup_stale/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-site-agent-services/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-site-agent-services/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/marketplace-site-agent-services/{uuid}/register_processor/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-site-agent-services/{uuid}/set_statistics/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-site-agent-stats/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-site-agent-task-stats/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-slurm-periodic-usage-policies/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/marketplace-slurm-periodic-usage-policies/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/marketplace-slurm-periodic-usage-policies/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-slurm-periodic-usage-policies/actions/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-slurm-periodic-usage-policies/actions/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-slurm-periodic-usage-policies/preview_impact/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-slurm-periodic-usage-policies/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-slurm-periodic-usage-policies/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/marketplace-slurm-periodic-usage-policies/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/marketplace-slurm-periodic-usage-policies/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-slurm-periodic-usage-policies/{uuid}/command-history/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-slurm-periodic-usage-policies/{uuid}/dry-run/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-slurm-periodic-usage-policies/{uuid}/evaluate/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-slurm-periodic-usage-policies/{uuid}/evaluation-logs/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-slurm-periodic-usage-policies/{uuid}/force-period-reset/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-slurm-periodic-usage-policies/{uuid}/report-command-result/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-software-catalogs/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-software-catalogs/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-software-catalogs/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-software-catalogs/discover/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-software-catalogs/discover/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-software-catalogs/import_catalog/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-software-catalogs/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-software-catalogs/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/marketplace-software-catalogs/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/marketplace-software-catalogs/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-software-catalogs/{uuid}/cpu_targets/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-software-catalogs/{uuid}/update_catalog/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-software-packages/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-software-packages/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-software-packages/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-software-packages/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-software-packages/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/marketplace-software-packages/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/marketplace-software-packages/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-software-targets/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-software-targets/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-software-targets/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-software-targets/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-software-targets/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/marketplace-software-targets/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/marketplace-software-targets/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-software-versions/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-software-versions/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-software-versions/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-software-versions/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-software-versions/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/marketplace-software-versions/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/marketplace-software-versions/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/aggregated_usage_trends/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/aggregated_usage_trends/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/component_usages/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/component_usages/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/component_usages_per_month/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/component_usages_per_month/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/component_usages_per_project/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/component_usages_per_project/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/count_active_resources_grouped_by_offering/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/count_active_resources_grouped_by_offering/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/count_active_resources_grouped_by_offering_country/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/count_active_resources_grouped_by_offering_country/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/count_active_resources_grouped_by_organization_group/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/count_active_resources_grouped_by_organization_group/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/count_projects_grouped_by_provider_and_industry_flag/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/count_projects_grouped_by_provider_and_industry_flag/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/count_projects_grouped_by_provider_and_oecd/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/count_projects_grouped_by_provider_and_oecd/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/count_projects_of_service_providers/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/count_projects_of_service_providers/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/count_projects_of_service_providers_grouped_by_oecd/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/count_projects_of_service_providers_grouped_by_oecd/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/count_unique_users_connected_with_active_resources_of_service_provider/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/count_unique_users_connected_with_active_resources_of_service_provider/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/count_users_of_service_providers/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/count_users_of_service_providers/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/customer_member_count/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/customer_member_count/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/customer_member_summary/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/customer_member_summary/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/offering_costs_summary/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/offering_costs_summary/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/offerings_counter_stats/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/offerings_counter_stats/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/openstack_instances/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/openstack_instances/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/openstack_instances_aggregate/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/openstack_instances_aggregate/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/order_stats/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/order_stats/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/organization_project_count/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/organization_project_count/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/organization_resource_count/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/organization_resource_count/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/project_classification_summary/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/project_classification_summary/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/project_creation_trend/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/project_creation_trend/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/projects_limits_grouped_by_industry_flag/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/projects_limits_grouped_by_industry_flag/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/projects_limits_grouped_by_oecd/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/projects_limits_grouped_by_oecd/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/projects_usages_grouped_by_industry_flag/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/projects_usages_grouped_by_industry_flag/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/projects_usages_grouped_by_oecd/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/projects_usages_grouped_by_oecd/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/provider_customers/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/provider_customers/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/provider_offerings/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/provider_offerings/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/provider_resources/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/provider_resources/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/resource_creation_trend/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/resource_creation_trend/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/resource_provisioning_stats/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/resource_provisioning_stats/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/resource_usage_by_creator_affiliation/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/resource_usage_by_creator_affiliation/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/resource_usage_by_customer/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/resource_usage_by_customer/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/resource_usage_by_organization_type/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/resource_usage_by_organization_type/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/resources_geography_summary/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/resources_geography_summary/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/resources_limits/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/resources_limits/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/resources_missing_usage/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/resources_missing_usage/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/top_service_providers_by_resources/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/top_service_providers_by_resources/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/total_cost_of_active_resources_per_offering/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/total_cost_of_active_resources_per_offering/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/user_affiliation_count/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/user_affiliation_count/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/user_affiliation_details/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/user_affiliation_details/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/user_auth_method_count/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/user_auth_method_count/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/user_identity_source_count/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/user_identity_source_count/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/user_job_title_count/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/user_job_title_count/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/user_nationality/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/user_nationality/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/user_organization_count/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/user_organization_count/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/user_organization_type_count/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/user_organization_type_count/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-stats/user_residence_country/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-stats/user_residence_country/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-tags/

- Extensions changed
  - New extension: x-permissions

HEAD /api/marketplace-tags/

- Extensions changed
  - New extension: x-permissions

POST /api/marketplace-tags/

- Extensions changed
  - New extension: x-permissions

DELETE /api/marketplace-tags/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-tags/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/marketplace-tags/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/marketplace-tags/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-user-offering-consents/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/marketplace-user-offering-consents/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/marketplace-user-offering-consents/

- Extensions changed
  - New extension: x-permissions

GET /api/marketplace-user-offering-consents/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/marketplace-user-offering-consents/{uuid}/revoke/

- Extensions changed
  - New extension: x-permissions

GET /api/matrix/credentials/

- Extensions changed
  - New extension: x-permissions

POST /api/matrix/credentials/password/

- Extensions changed
  - New extension: x-permissions

POST /api/matrix/credentials/recovery-key/

- Extensions changed
  - New extension: x-permissions

POST /api/matrix/crypto/escrow/

- Extensions changed
  - New extension: x-permissions

POST /api/matrix/crypto/lease/

- Extensions changed
  - New extension: x-permissions

POST /api/matrix/crypto/lease/release/

- Extensions changed
  - New extension: x-permissions

GET /api/matrix/exports/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/matrix/exports/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/matrix/exports/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/matrix/exports/{uuid}/download/{kind}/

- Extensions changed
  - New extension: x-permissions

GET /api/matrix/rooms/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: bot_user_id
            - Properties changed
              - New property: bot_user_id

HEAD /api/matrix/rooms/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/matrix/rooms/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: bot_user_id
          - Properties changed
            - New property: bot_user_id

GET /api/matrix/rooms/eligible_projects/

- Extensions changed
  - New extension: x-permissions

HEAD /api/matrix/rooms/eligible_projects/

- Extensions changed
  - New extension: x-permissions

DELETE /api/matrix/rooms/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/matrix/rooms/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: bot_user_id
          - Properties changed
            - New property: bot_user_id

POST /api/matrix/rooms/{uuid}/disable/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 202
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: bot_user_id
          - Properties changed
            - New property: bot_user_id

POST /api/matrix/rooms/{uuid}/export_history/

- Extensions changed
  - New extension: x-permissions

POST /api/matrix/rooms/{uuid}/join/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 202
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: bot_user_id
          - Properties changed
            - New property: bot_user_id

POST /api/matrix/rooms/{uuid}/leave/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 202
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: bot_user_id
          - Properties changed
            - New property: bot_user_id

GET /api/matrix/rooms/{uuid}/members/

- Extensions changed
  - New extension: x-permissions

POST /api/matrix/rooms/{uuid}/open/

- Extensions changed
  - New extension: x-permissions

POST /api/matrix/rooms/{uuid}/reactivate/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 202
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: bot_user_id
          - Properties changed
            - New property: bot_user_id

POST /api/matrix/rooms/{uuid}/retry/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 202
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: bot_user_id
          - Properties changed
            - New property: bot_user_id

POST /api/matrix/rooms/{uuid}/sync_members/

- Extensions changed
  - New extension: x-permissions

POST /api/matrix/session/

- Extensions changed
  - New extension: x-permissions

GET /api/media/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/metadata/events/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: event_groups
              - AdditionalProperties changed
                - Items changed
                  - New enum values: [admin_object_created admin_object_deleted admin_object_updated auth_logged_in_with_valimo auth_logged_in_to_admin_site auth_login_failed_with_oauth auth_login_failed_with_saml2 auth_login_failed_with_valimo auth_login_failed_to_admin_site credit_reclassified_as_paid credit_topped_up granted_credit_expired marketplace_offering_deleted marketplace_resource_spending_limits_updated policy_created policy_deleted policy_updated resource_hard_reboot_failed resource_hard_reboot_scheduled resource_hard_reboot_succeeded token_viewed user_terms_of_service_accepted feedback_survey_answered oidc_token_revoked oidc_token_refresh_failed event_consumer_webhook_updated event_consumer_resync_requested]

GET /api/metadata/features/

- Extensions changed
  - New extension: x-permissions

GET /api/metadata/permissions/

- Extensions changed
  - New extension: x-permissions
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
                              - New enum values: [OFFERING.LIST OFFERING.UPDATE_ENDPOINT RESOURCE.MANAGE_CONSUMER_API_KEY INVOICE.LIST CUSTOMER.VIEW_ACCOUNTING CUSTOMER.VIEW_REPORTING]
            - Modified property: permission_map
              - AdditionalProperties changed
                - New enum values: [OFFERING.LIST OFFERING.UPDATE_ENDPOINT RESOURCE.MANAGE_CONSUMER_API_KEY INVOICE.LIST CUSTOMER.VIEW_ACCOUNTING CUSTOMER.VIEW_REPORTING]
            - Modified property: permissions
              - AdditionalProperties changed
                - New enum values: [OFFERING.LIST OFFERING.UPDATE_ENDPOINT RESOURCE.MANAGE_CONSUMER_API_KEY INVOICE.LIST CUSTOMER.VIEW_ACCOUNTING CUSTOMER.VIEW_REPORTING]

GET /api/metadata/settings/

- Extensions changed
  - New extension: x-permissions
- Description changed from 'Retrieves metadata for all settings that can be configured via the Constance backend. This includes setting keys, human-readable descriptions, default values, and types. This endpoint is publicly accessible.' to 'Retrieves metadata for all settings that can be changed at runtime. This includes setting keys, human-readable descriptions, default values, and types. This endpoint is publicly accessible.'

GET /api/my-assignment-batches/

- Extensions changed
  - New extension: x-permissions

HEAD /api/my-assignment-batches/

- Extensions changed
  - New extension: x-permissions

GET /api/my-assignment-batches/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/notification-messages-templates/

- Extensions changed
  - New extension: x-permissions

HEAD /api/notification-messages-templates/

- Extensions changed
  - New extension: x-permissions

POST /api/notification-messages-templates/

- Extensions changed
  - New extension: x-permissions

DELETE /api/notification-messages-templates/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/notification-messages-templates/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/notification-messages-templates/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/notification-messages-templates/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/notification-messages-templates/{uuid}/override/

- Extensions changed
  - New extension: x-permissions

GET /api/notification-messages/

- Extensions changed
  - New extension: x-permissions

HEAD /api/notification-messages/

- Extensions changed
  - New extension: x-permissions

POST /api/notification-messages/

- Extensions changed
  - New extension: x-permissions

DELETE /api/notification-messages/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/notification-messages/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/notification-messages/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/notification-messages/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/notification-messages/{uuid}/disable/

- Extensions changed
  - New extension: x-permissions

POST /api/notification-messages/{uuid}/enable/

- Extensions changed
  - New extension: x-permissions

GET /api/onboarding-justifications/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/onboarding-justifications/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/onboarding-justifications/create_justification/

- Extensions changed
  - New extension: x-permissions

DELETE /api/onboarding-justifications/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/onboarding-justifications/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

PATCH /api/onboarding-justifications/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: verification

PUT /api/onboarding-justifications/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: verification
        - Properties changed
          - Deleted property: verification

POST /api/onboarding-justifications/{uuid}/approve/

- Extensions changed
  - New extension: x-permissions

POST /api/onboarding-justifications/{uuid}/attach_document/

- Extensions changed
  - New extension: x-permissions

POST /api/onboarding-justifications/{uuid}/reject/

- Extensions changed
  - New extension: x-permissions

GET /api/onboarding-question-metadata/

- Extensions changed
  - New extension: x-permissions

HEAD /api/onboarding-question-metadata/

- Extensions changed
  - New extension: x-permissions

POST /api/onboarding-question-metadata/

- Extensions changed
  - New extension: x-permissions

DELETE /api/onboarding-question-metadata/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/onboarding-question-metadata/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/onboarding-question-metadata/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/onboarding-question-metadata/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/onboarding-verifications/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/onboarding-verifications/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/onboarding-verifications/available_checklists/

- Extensions changed
  - New extension: x-permissions

HEAD /api/onboarding-verifications/available_checklists/

- Extensions changed
  - New extension: x-permissions

POST /api/onboarding-verifications/start_verification/

- Extensions changed
  - New extension: x-permissions

DELETE /api/onboarding-verifications/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/onboarding-verifications/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

PATCH /api/onboarding-verifications/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/onboarding-verifications/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/onboarding-verifications/{uuid}/checklist/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/onboarding-verifications/{uuid}/completion_status/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/onboarding-verifications/{uuid}/create_customer/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: invoice_emails
            - New property: is_private_person
            - New property: user_assurance_levels
            - New property: user_nationalities
            - New property: user_organization_types
            - New property: vat_code_verified
            - New property: vat_percent
            - New property: vat_rule

POST /api/onboarding-verifications/{uuid}/run_validation/

- Extensions changed
  - New extension: x-permissions

POST /api/onboarding-verifications/{uuid}/submit_answers/

- Extensions changed
  - New extension: x-permissions

GET /api/onboarding/person-identifier-fields/

- Extensions changed
  - New extension: x-permissions

GET /api/onboarding/supported-countries/

- Extensions changed
  - New extension: x-permissions

GET /api/openportal-accounting-summary/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/openportal-accounting-summary/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/openportal-accounting-summary/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/openportal-allocation-user-usage/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/openportal-allocation-user-usage/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/openportal-allocation-user-usage/{id}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/openportal-allocations/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/openportal-allocations/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/openportal-allocations/

- Extensions changed
  - New extension: x-permissions

DELETE /api/openportal-allocations/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/openportal-allocations/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/openportal-allocations/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/openportal-allocations/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/openportal-allocations/{uuid}/pull/

- Extensions changed
  - New extension: x-permissions

POST /api/openportal-allocations/{uuid}/set_erred/

- Extensions changed
  - New extension: x-permissions

POST /api/openportal-allocations/{uuid}/set_limits/

- Extensions changed
  - New extension: x-permissions

POST /api/openportal-allocations/{uuid}/set_ok/

- Extensions changed
  - New extension: x-permissions

POST /api/openportal-allocations/{uuid}/unlink/

- Extensions changed
  - New extension: x-permissions

GET /api/openportal-associations/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/openportal-associations/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/openportal-associations/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/openportal-managed-project-audit/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/openportal-managed-project-audit/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/openportal-managed-project-audit/{id}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/openportal-managed-projects/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/openportal-managed-projects/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/openportal-managed-projects/{identifier}/{destination}/

- Extensions changed
  - New extension: x-permissions

HEAD /api/openportal-managed-projects/{identifier}/{destination}/

- Extensions changed
  - New extension: x-permissions

POST /api/openportal-managed-projects/{identifier}/{destination}/add-note/

- Extensions changed
  - New extension: x-permissions

POST /api/openportal-managed-projects/{identifier}/{destination}/approve/

- Extensions changed
  - New extension: x-permissions

POST /api/openportal-managed-projects/{identifier}/{destination}/attach/

- Extensions changed
  - New extension: x-permissions

DELETE /api/openportal-managed-projects/{identifier}/{destination}/delete/

- Extensions changed
  - New extension: x-permissions

POST /api/openportal-managed-projects/{identifier}/{destination}/detach/

- Extensions changed
  - New extension: x-permissions

POST /api/openportal-managed-projects/{identifier}/{destination}/reject/

- Extensions changed
  - New extension: x-permissions

GET /api/openportal-project-storage-reports/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/openportal-project-storage-reports/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/openportal-project-storage-reports/{id}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/openportal-project-template/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/openportal-project-template/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/openportal-project-template/

- Extensions changed
  - New extension: x-permissions

DELETE /api/openportal-project-template/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/openportal-project-template/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/openportal-project-template/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/openportal-project-template/{uuid}/

- Extensions changed
  - New extension: x-permissions

DELETE /api/openportal-project-template/{uuid}/delete/

- Extensions changed
  - New extension: x-permissions

GET /api/openportal-project-usage-reports/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/openportal-project-usage-reports/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/openportal-project-usage-reports/{id}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/openportal-projectinfo/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/openportal-projectinfo/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/openportal-projectinfo/

- Extensions changed
  - New extension: x-permissions

DELETE /api/openportal-projectinfo/{project}/

- Extensions changed
  - New extension: x-permissions

GET /api/openportal-projectinfo/{project}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/openportal-projectinfo/{project}/

- Extensions changed
  - New extension: x-permissions

PUT /api/openportal-projectinfo/{project}/

- Extensions changed
  - New extension: x-permissions

PUT /api/openportal-projectinfo/{project}/set_allowed_destinations/

- Extensions changed
  - New extension: x-permissions

PUT /api/openportal-projectinfo/{project}/set_shortname/

- Extensions changed
  - New extension: x-permissions

GET /api/openportal-remote-allocations/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/openportal-remote-allocations/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/openportal-remote-allocations/

- Extensions changed
  - New extension: x-permissions

DELETE /api/openportal-remote-allocations/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/openportal-remote-allocations/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/openportal-remote-allocations/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/openportal-remote-allocations/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/openportal-remote-allocations/{uuid}/pull/

- Extensions changed
  - New extension: x-permissions

POST /api/openportal-remote-allocations/{uuid}/set_erred/

- Extensions changed
  - New extension: x-permissions

POST /api/openportal-remote-allocations/{uuid}/set_limits/

- Extensions changed
  - New extension: x-permissions

POST /api/openportal-remote-allocations/{uuid}/set_ok/

- Extensions changed
  - New extension: x-permissions

POST /api/openportal-remote-allocations/{uuid}/unlink/

- Extensions changed
  - New extension: x-permissions

GET /api/openportal-remote-associations/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/openportal-remote-associations/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/openportal-remote-associations/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/openportal-remote-project-allocations/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/openportal-remote-project-allocations/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/openportal-remote-project-allocations/{id}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/openportal-remote-project-audit/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/openportal-remote-project-audit/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/openportal-remote-project-audit/{id}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/openportal-remote-projects/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/openportal-remote-projects/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/openportal-remote-projects/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/openportal-remote-projects/{uuid}/add-note/

- Extensions changed
  - New extension: x-permissions

POST /api/openportal-remote-projects/{uuid}/approve-now/

- Extensions changed
  - New extension: x-permissions

POST /api/openportal-remote-projects/{uuid}/hold-indefinitely/

- Extensions changed
  - New extension: x-permissions

POST /api/openportal-remote-projects/{uuid}/resend-request/

- Extensions changed
  - New extension: x-permissions

POST /api/openportal-remote-projects/{uuid}/reset-to-pending/

- Extensions changed
  - New extension: x-permissions

POST /api/openportal-remote-projects/{uuid}/set-allowed-domains/

- Extensions changed
  - New extension: x-permissions

POST /api/openportal-remote-projects/{uuid}/set-earliest-approve/

- Extensions changed
  - New extension: x-permissions

POST /api/openportal-remote-projects/{uuid}/set-links/

- Extensions changed
  - New extension: x-permissions

POST /api/openportal-remote-projects/{uuid}/set-membership-control/

- Extensions changed
  - New extension: x-permissions

GET /api/openportal-remote-projects/{uuid}/total-usage/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/openportal-unmanaged-projects/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- New query param: user_role
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [user_assurance_levels user_nationalities user_organization_types]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: user_assurance_levels
              - New property: user_nationalities
              - New property: user_organization_types
              - Modified property: project_metadata
                - Items changed
                  - Properties changed
                    - New property: likert_high_label
                    - New property: likert_low_label
                    - New property: likert_scale_length
                    - New property: max_value
                    - New property: min_value

HEAD /api/openportal-unmanaged-projects/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- New query param: user_role

POST /api/openportal-unmanaged-projects/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: user_assurance_levels
          - New property: user_nationalities
          - New property: user_organization_types
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: user_assurance_levels
          - New property: user_nationalities
          - New property: user_organization_types
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: user_assurance_levels
          - New property: user_nationalities
          - New property: user_organization_types
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_assurance_levels
            - New property: user_nationalities
            - New property: user_organization_types
            - Modified property: project_metadata
              - Items changed
                - Properties changed
                  - New property: likert_high_label
                  - New property: likert_low_label
                  - New property: likert_scale_length
                  - New property: max_value
                  - New property: min_value

GET /api/openportal-unmanaged-projects/checklist-template/

- Extensions changed
  - New extension: x-permissions

HEAD /api/openportal-unmanaged-projects/checklist-template/

- Extensions changed
  - New extension: x-permissions

DELETE /api/openportal-unmanaged-projects/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/openportal-unmanaged-projects/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [user_assurance_levels user_nationalities user_organization_types]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_assurance_levels
            - New property: user_nationalities
            - New property: user_organization_types
            - Modified property: project_metadata
              - Items changed
                - Properties changed
                  - New property: likert_high_label
                  - New property: likert_low_label
                  - New property: likert_scale_length
                  - New property: max_value
                  - New property: min_value

PATCH /api/openportal-unmanaged-projects/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: user_assurance_levels
          - New property: user_nationalities
          - New property: user_organization_types
          - Deleted property: customer
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: user_assurance_levels
          - New property: user_nationalities
          - New property: user_organization_types
          - Deleted property: customer
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: user_assurance_levels
          - New property: user_nationalities
          - New property: user_organization_types
          - Deleted property: customer
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_assurance_levels
            - New property: user_nationalities
            - New property: user_organization_types
            - Modified property: project_metadata
              - Items changed
                - Properties changed
                  - New property: likert_high_label
                  - New property: likert_low_label
                  - New property: likert_scale_length
                  - New property: max_value
                  - New property: min_value

PUT /api/openportal-unmanaged-projects/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: user_assurance_levels
          - New property: user_nationalities
          - New property: user_organization_types
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: user_assurance_levels
          - New property: user_nationalities
          - New property: user_organization_types
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: user_assurance_levels
          - New property: user_nationalities
          - New property: user_organization_types
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_assurance_levels
            - New property: user_nationalities
            - New property: user_organization_types
            - Modified property: project_metadata
              - Items changed
                - Properties changed
                  - New property: likert_high_label
                  - New property: likert_low_label
                  - New property: likert_scale_length
                  - New property: max_value
                  - New property: min_value

POST /api/openportal-unmanaged-projects/{uuid}/add_user/

- Extensions changed
  - New extension: x-permissions

GET /api/openportal-unmanaged-projects/{uuid}/checklist/

- Extensions changed
  - New extension: x-permissions

GET /api/openportal-unmanaged-projects/{uuid}/completion_status/

- Extensions changed
  - New extension: x-permissions

POST /api/openportal-unmanaged-projects/{uuid}/delete_user/

- Extensions changed
  - New extension: x-permissions

GET /api/openportal-unmanaged-projects/{uuid}/list_users/

- Extensions changed
  - New extension: x-permissions
- New query param: role_template

HEAD /api/openportal-unmanaged-projects/{uuid}/list_users/

- Extensions changed
  - New extension: x-permissions
- New query param: role_template

POST /api/openportal-unmanaged-projects/{uuid}/move_project/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_assurance_levels
            - New property: user_nationalities
            - New property: user_organization_types
            - Modified property: project_metadata
              - Items changed
                - Properties changed
                  - New property: likert_high_label
                  - New property: likert_low_label
                  - New property: likert_scale_length
                  - New property: max_value
                  - New property: min_value

POST /api/openportal-unmanaged-projects/{uuid}/recover/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_assurance_levels
            - New property: user_nationalities
            - New property: user_organization_types
            - Modified property: project_metadata
              - Items changed
                - Properties changed
                  - New property: likert_high_label
                  - New property: likert_low_label
                  - New property: likert_scale_length
                  - New property: max_value
                  - New property: min_value

POST /api/openportal-unmanaged-projects/{uuid}/set_slug/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/openportal-unmanaged-projects/{uuid}/stats/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/openportal-unmanaged-projects/{uuid}/submit_answers/

- Extensions changed
  - New extension: x-permissions

POST /api/openportal-unmanaged-projects/{uuid}/update_affiliation/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/openportal-unmanaged-projects/{uuid}/update_user/

- Extensions changed
  - New extension: x-permissions

GET /api/openportal-userinfo/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/openportal-userinfo/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/openportal-userinfo/

- Extensions changed
  - New extension: x-permissions

GET /api/openportal-userinfo/me/

- Extensions changed
  - New extension: x-permissions

HEAD /api/openportal-userinfo/me/

- Extensions changed
  - New extension: x-permissions

DELETE /api/openportal-userinfo/{user}/

- Extensions changed
  - New extension: x-permissions

GET /api/openportal-userinfo/{user}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/openportal-userinfo/{user}/

- Extensions changed
  - New extension: x-permissions

PUT /api/openportal-userinfo/{user}/

- Extensions changed
  - New extension: x-permissions

PUT /api/openportal-userinfo/{user}/set_shortname/

- Extensions changed
  - New extension: x-permissions

GET /api/openportal/access_for_email/

- Extensions changed
  - New extension: x-permissions

GET /api/openportal/offering_mapping/

- Extensions changed
  - New extension: x-permissions

GET /api/openportal/project_email_policy/{project_uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/openportal/project_mapping/

- Extensions changed
  - New extension: x-permissions

GET /api/openportal/user_mapping/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-backups/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: instance_floating_ips
                - Items changed
                  - Properties changed
                    - Modified property: address
                      - Property 'OneOf' changed
                        - Schemas deleted: subschema #1, subschema #2
                      - Type changed from '' to 'string'
                      - Format changed from '' to 'ipv4'
              - Modified property: restorations
                - Items changed
                  - Properties changed
                    - Modified property: floating_ips
                      - Items changed
                        - Properties changed
                          - Modified property: address
                            - Property 'OneOf' changed
                              - Schemas deleted: subschema #1, subschema #2
                            - Type changed from '' to 'string'
                            - Format changed from '' to 'ipv4'

HEAD /api/openstack-backups/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

DELETE /api/openstack-backups/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-backups/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: instance_floating_ips
              - Items changed
                - Properties changed
                  - Modified property: address
                    - Property 'OneOf' changed
                      - Schemas deleted: subschema #1, subschema #2
                    - Type changed from '' to 'string'
                    - Format changed from '' to 'ipv4'
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: floating_ips
                    - Items changed
                      - Properties changed
                        - Modified property: address
                          - Property 'OneOf' changed
                            - Schemas deleted: subschema #1, subschema #2
                          - Type changed from '' to 'string'
                          - Format changed from '' to 'ipv4'

PATCH /api/openstack-backups/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: instance_floating_ips
              - Items changed
                - Properties changed
                  - Modified property: address
                    - Property 'OneOf' changed
                      - Schemas deleted: subschema #1, subschema #2
                    - Type changed from '' to 'string'
                    - Format changed from '' to 'ipv4'
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: floating_ips
                    - Items changed
                      - Properties changed
                        - Modified property: address
                          - Property 'OneOf' changed
                            - Schemas deleted: subschema #1, subschema #2
                          - Type changed from '' to 'string'
                          - Format changed from '' to 'ipv4'

PUT /api/openstack-backups/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: instance_floating_ips
              - Items changed
                - Properties changed
                  - Modified property: address
                    - Property 'OneOf' changed
                      - Schemas deleted: subschema #1, subschema #2
                    - Type changed from '' to 'string'
                    - Format changed from '' to 'ipv4'
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: floating_ips
                    - Items changed
                      - Properties changed
                        - Modified property: address
                          - Property 'OneOf' changed
                            - Schemas deleted: subschema #1, subschema #2
                          - Type changed from '' to 'string'
                          - Format changed from '' to 'ipv4'

POST /api/openstack-backups/{uuid}/pull/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-backups/{uuid}/restore/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: floating_ips
              - Items changed
                - Properties changed
                  - Modified property: address
                    - Property 'OneOf' changed
                      - Schemas deleted: subschema #1, subschema #2
                    - Type changed from '' to 'string'
                    - Format changed from '' to 'ipv4'
            - Modified property: server_group
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/OpenStackNestedServerGroup
              - Type changed from 'object' to ''
              - Nullable changed from false to true
              - Properties changed
                - Deleted property: name
                - Deleted property: policy
                - Deleted property: state
                - Deleted property: url

POST /api/openstack-backups/{uuid}/set_erred/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-backups/{uuid}/set_ok/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-backups/{uuid}/unlink/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-external-networks/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/openstack-external-networks/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/openstack-external-networks/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/openstack-flavors/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/openstack-flavors/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/openstack-flavors/usage_stats/

- Extensions changed
  - New extension: x-permissions

HEAD /api/openstack-flavors/usage_stats/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-flavors/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/openstack-floating-ips/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: address
                - Property 'OneOf' changed
                  - Schemas deleted: subschema #1, subschema #2
                - Type changed from '' to 'string'
                - Format changed from '' to 'ipv4'

HEAD /api/openstack-floating-ips/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

DELETE /api/openstack-floating-ips/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-floating-ips/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: address
              - Property 'OneOf' changed
                - Schemas deleted: subschema #1, subschema #2
              - Type changed from '' to 'string'
              - Format changed from '' to 'ipv4'

POST /api/openstack-floating-ips/{uuid}/attach_to_port/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-floating-ips/{uuid}/detach_from_port/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-floating-ips/{uuid}/pull/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-floating-ips/{uuid}/set_erred/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-floating-ips/{uuid}/set_ok/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-floating-ips/{uuid}/unlink/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-floating-ips/{uuid}/update_description/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-health-monitors/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/openstack-health-monitors/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/openstack-health-monitors/

- Extensions changed
  - New extension: x-permissions

DELETE /api/openstack-health-monitors/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-health-monitors/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/openstack-health-monitors/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/openstack-health-monitors/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-health-monitors/{uuid}/pull/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-hypervisor-inventories/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/openstack-hypervisor-inventories/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/openstack-hypervisor-inventories/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/openstack-hypervisors/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/openstack-hypervisors/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/openstack-hypervisors/allocation_candidates/

- Extensions changed
  - New extension: x-permissions

HEAD /api/openstack-hypervisors/allocation_candidates/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-hypervisors/summary/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/openstack-hypervisors/summary/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/openstack-hypervisors/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/openstack-images/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/openstack-images/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/openstack-images/usage_stats/

- Extensions changed
  - New extension: x-permissions

HEAD /api/openstack-images/usage_stats/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-images/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/openstack-instance-availability-zones/

- Extensions changed
  - New extension: x-permissions

HEAD /api/openstack-instance-availability-zones/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-instance-availability-zones/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-instances/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: floating_ips
                - Items changed
                  - Properties changed
                    - Modified property: address
                      - Property 'OneOf' changed
                        - Schemas deleted: subschema #1, subschema #2
                      - Type changed from '' to 'string'
                      - Format changed from '' to 'ipv4'
              - Modified property: server_group
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/OpenStackNestedServerGroup
                - Type changed from 'object' to ''
                - Nullable changed from false to true
                - Properties changed
                  - Deleted property: name
                  - Deleted property: policy
                  - Deleted property: state
                  - Deleted property: url

HEAD /api/openstack-instances/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/openstack-instances/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: floating_ips
              - Items changed
                - Properties changed
                  - Modified property: address
                    - Property 'OneOf' changed
                      - Schemas deleted: subschema #1, subschema #2
                    - Type changed from '' to 'string'
                    - Format changed from '' to 'ipv4'
            - Modified property: server_group
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/OpenStackNestedServerGroup
              - Type changed from 'object' to ''
              - Nullable changed from false to true
              - Properties changed
                - Deleted property: name
                - Deleted property: policy
                - Deleted property: state
                - Deleted property: url

PATCH /api/openstack-instances/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: floating_ips
              - Items changed
                - Properties changed
                  - Modified property: address
                    - Property 'OneOf' changed
                      - Schemas deleted: subschema #1, subschema #2
                    - Type changed from '' to 'string'
                    - Format changed from '' to 'ipv4'
            - Modified property: server_group
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/OpenStackNestedServerGroup
              - Type changed from 'object' to ''
              - Nullable changed from false to true
              - Properties changed
                - Deleted property: name
                - Deleted property: policy
                - Deleted property: state
                - Deleted property: url

PUT /api/openstack-instances/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: floating_ips
              - Items changed
                - Properties changed
                  - Modified property: address
                    - Property 'OneOf' changed
                      - Schemas deleted: subschema #1, subschema #2
                    - Type changed from '' to 'string'
                    - Format changed from '' to 'ipv4'
            - Modified property: server_group
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/OpenStackNestedServerGroup
              - Type changed from 'object' to ''
              - Nullable changed from false to true
              - Properties changed
                - Deleted property: name
                - Deleted property: policy
                - Deleted property: state
                - Deleted property: url

POST /api/openstack-instances/{uuid}/backup/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: instance_floating_ips
              - Items changed
                - Properties changed
                  - Modified property: address
                    - Property 'OneOf' changed
                      - Schemas deleted: subschema #1, subschema #2
                    - Type changed from '' to 'string'
                    - Format changed from '' to 'ipv4'
            - Modified property: restorations
              - Items changed
                - Properties changed
                  - Modified property: floating_ips
                    - Items changed
                      - Properties changed
                        - Modified property: address
                          - Property 'OneOf' changed
                            - Schemas deleted: subschema #1, subschema #2
                          - Type changed from '' to 'string'
                          - Format changed from '' to 'ipv4'

POST /api/openstack-instances/{uuid}/change_flavor/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-instances/{uuid}/console/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-instances/{uuid}/console_log/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-instances/{uuid}/console_log/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-instances/{uuid}/diagnose_connectivity/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-instances/{uuid}/floating_ips/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: address
                - Property 'OneOf' changed
                  - Schemas deleted: subschema #1, subschema #2
                - Type changed from '' to 'string'
                - Format changed from '' to 'ipv4'

GET /api/openstack-instances/{uuid}/placement_allocations/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-instances/{uuid}/ports/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/openstack-instances/{uuid}/pull/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-instances/{uuid}/rescue/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-instances/{uuid}/restart/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-instances/{uuid}/set_erred/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-instances/{uuid}/set_metadata/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-instances/{uuid}/set_ok/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-instances/{uuid}/start/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-instances/{uuid}/stop/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-instances/{uuid}/unlink/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-instances/{uuid}/unrescue/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-instances/{uuid}/update_allowed_address_pairs/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-instances/{uuid}/update_floating_ips/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-instances/{uuid}/update_ports/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-instances/{uuid}/update_security_groups/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-listeners/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/openstack-listeners/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/openstack-listeners/

- Extensions changed
  - New extension: x-permissions

DELETE /api/openstack-listeners/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-listeners/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/openstack-listeners/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/openstack-listeners/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-listeners/{uuid}/pull/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-loadbalancers/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/openstack-loadbalancers/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/openstack-loadbalancers/

- Extensions changed
  - New extension: x-permissions

DELETE /api/openstack-loadbalancers/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-loadbalancers/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/openstack-loadbalancers/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/openstack-loadbalancers/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-loadbalancers/{uuid}/attach_floating_ip/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-loadbalancers/{uuid}/detach_floating_ip/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-loadbalancers/{uuid}/pull/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-loadbalancers/{uuid}/set_security_groups/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-loadbalancers/{uuid}/unlink/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-marketplace-tenants/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/openstack-marketplace-tenants/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/openstack-marketplace-tenants/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/openstack-marketplace-tenants/{uuid}/create_image/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-marketplace-tenants/{uuid}/upload_image_data/{image_id}/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-migrations/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/openstack-migrations/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/openstack-migrations/

- Extensions changed
  - New extension: x-permissions

DELETE /api/openstack-migrations/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-migrations/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/openstack-network-rbac-policies/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/openstack-network-rbac-policies/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/openstack-network-rbac-policies/

- Extensions changed
  - New extension: x-permissions

DELETE /api/openstack-network-rbac-policies/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-network-rbac-policies/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/openstack-networks/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/openstack-networks/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

DELETE /api/openstack-networks/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-networks/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

PATCH /api/openstack-networks/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/openstack-networks/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-networks/{uuid}/create_subnet/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-networks/{uuid}/pull/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-networks/{uuid}/rbac_policy_create/

- Extensions changed
  - New extension: x-permissions

DELETE /api/openstack-networks/{uuid}/rbac_policy_delete/{rbac_policy_uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-networks/{uuid}/set_erred/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-networks/{uuid}/set_mtu/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-networks/{uuid}/set_ok/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-networks/{uuid}/unlink/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-pool-members/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/openstack-pool-members/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/openstack-pool-members/

- Extensions changed
  - New extension: x-permissions

DELETE /api/openstack-pool-members/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-pool-members/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/openstack-pool-members/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/openstack-pool-members/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-pool-members/{uuid}/pull/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-pools/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/openstack-pools/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/openstack-pools/

- Extensions changed
  - New extension: x-permissions

DELETE /api/openstack-pools/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-pools/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/openstack-pools/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/openstack-pools/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-pools/{uuid}/pull/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-ports/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: allowed_address_pairs
                - ReadOnly changed from false to true

HEAD /api/openstack-ports/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/openstack-ports/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: allowed_address_pairs
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: allowed_address_pairs
              - ReadOnly changed from false to true

DELETE /api/openstack-ports/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-ports/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: allowed_address_pairs
              - ReadOnly changed from false to true

PATCH /api/openstack-ports/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: allowed_address_pairs
              - ReadOnly changed from false to true

PUT /api/openstack-ports/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: allowed_address_pairs
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: allowed_address_pairs
              - ReadOnly changed from false to true

POST /api/openstack-ports/{uuid}/disable_port/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-ports/{uuid}/disable_port_security/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-ports/{uuid}/enable_port/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-ports/{uuid}/enable_port_security/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-ports/{uuid}/pull/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-ports/{uuid}/set_allowed_address_pairs/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: allowed_address_pairs
              - ReadOnly changed from false to true

POST /api/openstack-ports/{uuid}/set_erred/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-ports/{uuid}/set_ok/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-ports/{uuid}/unlink/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-ports/{uuid}/update_port_ip/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-ports/{uuid}/update_security_groups/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-routers/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/openstack-routers/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/openstack-routers/

- Extensions changed
  - New extension: x-permissions

DELETE /api/openstack-routers/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-routers/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/openstack-routers/{uuid}/add_router_interface/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-routers/{uuid}/available_external_networks/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-routers/{uuid}/effective_routes/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/openstack-routers/{uuid}/remove_external_gateway/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-routers/{uuid}/remove_router_interface/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-routers/{uuid}/set_erred/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-routers/{uuid}/set_external_gateway/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-routers/{uuid}/set_ok/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-routers/{uuid}/set_routes/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-security-groups/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/openstack-security-groups/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

DELETE /api/openstack-security-groups/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-security-groups/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/openstack-security-groups/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/openstack-security-groups/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-security-groups/{uuid}/pull/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-security-groups/{uuid}/set_erred/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-security-groups/{uuid}/set_ok/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-security-groups/{uuid}/set_rules/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-security-groups/{uuid}/unlink/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-server-groups/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/openstack-server-groups/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

DELETE /api/openstack-server-groups/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-server-groups/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/openstack-server-groups/{uuid}/pull/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-server-groups/{uuid}/set_erred/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-server-groups/{uuid}/set_ok/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-server-groups/{uuid}/unlink/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-snapshots/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/openstack-snapshots/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

DELETE /api/openstack-snapshots/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-snapshots/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/openstack-snapshots/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/openstack-snapshots/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-snapshots/{uuid}/pull/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-snapshots/{uuid}/restorations/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/openstack-snapshots/{uuid}/restore/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-snapshots/{uuid}/set_erred/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-snapshots/{uuid}/set_ok/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-snapshots/{uuid}/unlink/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-subnets/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/openstack-subnets/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

DELETE /api/openstack-subnets/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-subnets/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

PATCH /api/openstack-subnets/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/openstack-subnets/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-subnets/{uuid}/connect/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-subnets/{uuid}/disconnect/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-subnets/{uuid}/pull/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-subnets/{uuid}/set_erred/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-subnets/{uuid}/set_ok/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-subnets/{uuid}/unlink/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-tenants/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/openstack-tenants/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/openstack-tenants/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/openstack-tenants/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/openstack-tenants/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-tenants/{uuid}/backend_instances/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/openstack-tenants/{uuid}/backend_volumes/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/openstack-tenants/{uuid}/change_password/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-tenants/{uuid}/create_floating_ip/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: address
              - Property 'OneOf' changed
                - Schemas deleted: subschema #1, subschema #2
              - Type changed from '' to 'string'
              - Format changed from '' to 'ipv4'

POST /api/openstack-tenants/{uuid}/create_network/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-tenants/{uuid}/create_security_group/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-tenants/{uuid}/create_server_group/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-tenants/{uuid}/pull/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-tenants/{uuid}/pull_floating_ips/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-tenants/{uuid}/pull_quotas/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-tenants/{uuid}/pull_security_groups/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-tenants/{uuid}/pull_server_groups/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-tenants/{uuid}/push_security_groups/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-tenants/{uuid}/set_erred/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-tenants/{uuid}/set_ok/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-tenants/{uuid}/set_quotas/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-tenants/{uuid}/topology/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/openstack-tenants/{uuid}/unlink/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-volume-availability-zones/

- Extensions changed
  - New extension: x-permissions

HEAD /api/openstack-volume-availability-zones/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-volume-availability-zones/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-volume-types/

- Extensions changed
  - New extension: x-permissions

HEAD /api/openstack-volume-types/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-volume-types/names/

- Extensions changed
  - New extension: x-permissions

HEAD /api/openstack-volume-types/names/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-volume-types/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/openstack-volumes/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/openstack-volumes/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/openstack-volumes/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/openstack-volumes/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/openstack-volumes/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-volumes/{uuid}/attach/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-volumes/{uuid}/detach/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-volumes/{uuid}/extend/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-volumes/{uuid}/pull/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-volumes/{uuid}/retype/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-volumes/{uuid}/set_erred/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-volumes/{uuid}/set_ok/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-volumes/{uuid}/snapshot/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack-volumes/{uuid}/unlink/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack/discovery/discover_external_networks/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack/discovery/discover_flavors/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack/discovery/discover_instance_availability_zones/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack/discovery/discover_volume_availability_zones/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack/discovery/discover_volume_types/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack/discovery/preview_service_attributes/

- Extensions changed
  - New extension: x-permissions

POST /api/openstack/discovery/validate_credentials/

- Extensions changed
  - New extension: x-permissions

GET /api/organization-groups/

- Extensions changed
  - New extension: x-permissions

HEAD /api/organization-groups/

- Extensions changed
  - New extension: x-permissions

POST /api/organization-groups/

- Extensions changed
  - New extension: x-permissions

DELETE /api/organization-groups/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/organization-groups/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/organization-groups/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/organization-groups/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/otlp/v1/metrics/

- Extensions changed
  - New extension: x-permissions

GET /api/override-settings/

- Extensions changed
  - New extension: x-permissions
- Description changed from 'Returns all settings that can be overridden in the database via the Constance backend. Staff receive every value. Support users receive the same keys, with secret_field values blanked.' to 'Returns all settings that can be overridden in the database. Staff receive every value. Support users receive the same keys, with secret_field values blanked.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: API_TOKEN_MAX_LIFETIME_MINUTES
            - New property: EVENT_CONSUMER_EPHEMERAL_IDLE_HOURS
            - New property: FIRECREST_ALLOWED_API_URLS
            - New property: MATRIX_TICKET_CONTEXT_MESSAGES
            - New property: MATRIX_TICKET_DRAFT_TTL_MINUTES
            - New property: MCP_ENABLED
            - New property: MCP_RESOURCE_URLS
            - New property: OIDC_TOKEN_MAX_IDLE_DAYS
            - New property: SLURM_MONITOR_ALLOWED_API_URLS
            - New property: VAT_OSS_ENABLED
            - New property: VAT_TAXATION_ENABLED
            - Modified property: DISABLED_OFFERING_TYPES
              - Items changed
                - Property 'OneOf' changed
                  - Modified schema: #/components/schemas/OfferingTypeEnum
                    - New enum values: [Marketplace.SiteAgent]

POST /api/override-settings/

- Extensions changed
  - New extension: x-permissions
- Description changed from 'Updates one or more settings in the database via the Constance backend. Requires staff permissions. Support users cannot update settings.' to 'Updates one or more settings in the database. Requires staff permissions. Support users cannot update settings.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: API_TOKEN_MAX_LIFETIME_MINUTES
          - New property: EVENT_CONSUMER_EPHEMERAL_IDLE_HOURS
          - New property: FIRECREST_ALLOWED_API_URLS
          - New property: MATRIX_TICKET_CONTEXT_MESSAGES
          - New property: MATRIX_TICKET_DRAFT_TTL_MINUTES
          - New property: MCP_ENABLED
          - New property: MCP_RESOURCE_URLS
          - New property: OIDC_TOKEN_MAX_IDLE_DAYS
          - New property: SLURM_MONITOR_ALLOWED_API_URLS
          - New property: VAT_OSS_ENABLED
          - New property: VAT_TAXATION_ENABLED
          - Modified property: DISABLED_OFFERING_TYPES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/OfferingTypeEnum
                  - New enum values: [Marketplace.SiteAgent]
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: API_TOKEN_MAX_LIFETIME_MINUTES
          - New property: EVENT_CONSUMER_EPHEMERAL_IDLE_HOURS
          - New property: FIRECREST_ALLOWED_API_URLS
          - New property: MATRIX_TICKET_CONTEXT_MESSAGES
          - New property: MATRIX_TICKET_DRAFT_TTL_MINUTES
          - New property: MCP_ENABLED
          - New property: MCP_RESOURCE_URLS
          - New property: OIDC_TOKEN_MAX_IDLE_DAYS
          - New property: SLURM_MONITOR_ALLOWED_API_URLS
          - New property: VAT_OSS_ENABLED
          - New property: VAT_TAXATION_ENABLED
          - Modified property: DISABLED_OFFERING_TYPES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/OfferingTypeEnum
                  - New enum values: [Marketplace.SiteAgent]
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: API_TOKEN_MAX_LIFETIME_MINUTES
          - New property: EVENT_CONSUMER_EPHEMERAL_IDLE_HOURS
          - New property: FIRECREST_ALLOWED_API_URLS
          - New property: MATRIX_TICKET_CONTEXT_MESSAGES
          - New property: MATRIX_TICKET_DRAFT_TTL_MINUTES
          - New property: MCP_ENABLED
          - New property: MCP_RESOURCE_URLS
          - New property: OIDC_TOKEN_MAX_IDLE_DAYS
          - New property: SLURM_MONITOR_ALLOWED_API_URLS
          - New property: VAT_OSS_ENABLED
          - New property: VAT_TAXATION_ENABLED
          - Modified property: DISABLED_OFFERING_TYPES
            - Items changed
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/OfferingTypeEnum
                  - New enum values: [Marketplace.SiteAgent]

GET /api/passkeys/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/passkeys/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/passkeys/mfa/begin/

- Extensions changed
  - New extension: x-permissions

POST /api/passkeys/mfa/finish/

- Extensions changed
  - New extension: x-permissions

POST /api/passkeys/registration/begin/

- Extensions changed
  - New extension: x-permissions

POST /api/passkeys/registration/finish/

- Extensions changed
  - New extension: x-permissions

POST /api/passkeys/signin/begin/

- Extensions changed
  - New extension: x-permissions

POST /api/passkeys/signin/finish/

- Extensions changed
  - New extension: x-permissions

GET /api/passkeys/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

PATCH /api/passkeys/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/passkeys/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/passkeys/{uuid}/revoke/

- Extensions changed
  - New extension: x-permissions

GET /api/payment-profiles/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/payment-profiles/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/payment-profiles/

- Extensions changed
  - New extension: x-permissions

DELETE /api/payment-profiles/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/payment-profiles/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/payment-profiles/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/payment-profiles/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/payment-profiles/{uuid}/enable/

- Extensions changed
  - New extension: x-permissions

GET /api/payments/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/payments/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/payments/

- Extensions changed
  - New extension: x-permissions

DELETE /api/payments/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/payments/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/payments/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/payments/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/payments/{uuid}/link_to_invoice/

- Extensions changed
  - New extension: x-permissions

POST /api/payments/{uuid}/unlink_from_invoice/

- Extensions changed
  - New extension: x-permissions

GET /api/personal-access-tokens/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/personal-access-tokens/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/personal-access-tokens/

- Extensions changed
  - New extension: x-permissions

GET /api/personal-access-tokens/available_binding_targets/

- Extensions changed
  - New extension: x-permissions
- Description changed from 'For each permission, which TYPE_MAP keys the caller could bind a PAT to.

Drives the create-PAT frontend's type picker. For staff users every
type is offered for every permission (they bypass UserRole checks).
For other users we return only types where they hold an active role
granting the permission directly (the binding then inherits to
descendants at request time).' to 'For each permission, which scope types the caller could bind a PAT to.

Drives the create-PAT frontend's type picker. For staff users every
type is offered for every permission (they bypass UserRole checks).
For other users we return only types where they hold an active role
granting the permission directly (the binding then inherits to
descendants at request time).'

HEAD /api/personal-access-tokens/available_binding_targets/

- Extensions changed
  - New extension: x-permissions

GET /api/personal-access-tokens/available_scopes/

- Extensions changed
  - New extension: x-permissions

HEAD /api/personal-access-tokens/available_scopes/

- Extensions changed
  - New extension: x-permissions

DELETE /api/personal-access-tokens/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/personal-access-tokens/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/personal-access-tokens/{uuid}/rotate/

- Extensions changed
  - New extension: x-permissions

POST /api/personal-access-tokens/{uuid}/set_network_acl/

- Extensions changed
  - New extension: x-permissions

GET /api/project-credits/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: earlier_invoices_compensate_in
              - New property: earlier_invoices_from
              - New property: earlier_invoices_until
              - New property: pay_earlier_invoices

HEAD /api/project-credits/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/project-credits/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: earlier_invoices_compensate_in
          - New property: earlier_invoices_from
          - New property: earlier_invoices_until
          - New property: pay_earlier_invoices
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: earlier_invoices_compensate_in
            - New property: earlier_invoices_from
            - New property: earlier_invoices_until
            - New property: pay_earlier_invoices

DELETE /api/project-credits/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/project-credits/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: earlier_invoices_compensate_in
            - New property: earlier_invoices_from
            - New property: earlier_invoices_until
            - New property: pay_earlier_invoices

PATCH /api/project-credits/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: earlier_invoices_compensate_in
          - New property: earlier_invoices_from
          - New property: earlier_invoices_until
          - New property: pay_earlier_invoices
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: earlier_invoices_compensate_in
            - New property: earlier_invoices_from
            - New property: earlier_invoices_until
            - New property: pay_earlier_invoices

PUT /api/project-credits/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: earlier_invoices_compensate_in
          - New property: earlier_invoices_from
          - New property: earlier_invoices_until
          - New property: pay_earlier_invoices
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: earlier_invoices_compensate_in
            - New property: earlier_invoices_from
            - New property: earlier_invoices_until
            - New property: pay_earlier_invoices

GET /api/project-end-date-change-requests/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/project-end-date-change-requests/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/project-end-date-change-requests/

- Extensions changed
  - New extension: x-permissions

GET /api/project-end-date-change-requests/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/project-end-date-change-requests/{uuid}/approve/

- Extensions changed
  - New extension: x-permissions

POST /api/project-end-date-change-requests/{uuid}/cancel/

- Extensions changed
  - New extension: x-permissions

POST /api/project-end-date-change-requests/{uuid}/reject/

- Extensions changed
  - New extension: x-permissions

GET /api/project-permissions-reviews/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/project-permissions-reviews/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/project-permissions-reviews/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/project-permissions-reviews/{uuid}/close/

- Extensions changed
  - New extension: x-permissions

GET /api/project-quotas/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/project-quotas/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/project-types/

- Extensions changed
  - New extension: x-permissions

HEAD /api/project-types/

- Extensions changed
  - New extension: x-permissions

GET /api/project-types/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/projects/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- New query param: user_role
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [user_assurance_levels user_nationalities user_organization_types]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: user_assurance_levels
              - New property: user_nationalities
              - New property: user_organization_types
              - Modified property: project_metadata
                - Items changed
                  - Properties changed
                    - New property: likert_high_label
                    - New property: likert_low_label
                    - New property: likert_scale_length
                    - New property: max_value
                    - New property: min_value

HEAD /api/projects/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- New query param: user_role

POST /api/projects/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: user_assurance_levels
          - New property: user_nationalities
          - New property: user_organization_types
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: user_assurance_levels
          - New property: user_nationalities
          - New property: user_organization_types
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: user_assurance_levels
          - New property: user_nationalities
          - New property: user_organization_types
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_assurance_levels
            - New property: user_nationalities
            - New property: user_organization_types
            - Modified property: project_metadata
              - Items changed
                - Properties changed
                  - New property: likert_high_label
                  - New property: likert_low_label
                  - New property: likert_scale_length
                  - New property: max_value
                  - New property: min_value

GET /api/projects/checklist-template/

- Extensions changed
  - New extension: x-permissions

HEAD /api/projects/checklist-template/

- Extensions changed
  - New extension: x-permissions

GET /api/projects/{project_uuid}/other_users/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Description changed from 'A list of users which can be added to the current project from other projects of the same customer.' to 'Users with a role in the caller's other projects of the same organization, whom the caller may add to the current project. The current project must be one the caller can see; otherwise the response is 404. A personal access token lists only the users of projects its bindings reach.'

HEAD /api/projects/{project_uuid}/other_users/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

DELETE /api/projects/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/projects/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [user_assurance_levels user_nationalities user_organization_types]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_assurance_levels
            - New property: user_nationalities
            - New property: user_organization_types
            - Modified property: project_metadata
              - Items changed
                - Properties changed
                  - New property: likert_high_label
                  - New property: likert_low_label
                  - New property: likert_scale_length
                  - New property: max_value
                  - New property: min_value

PATCH /api/projects/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: user_assurance_levels
          - New property: user_nationalities
          - New property: user_organization_types
          - Deleted property: customer
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: user_assurance_levels
          - New property: user_nationalities
          - New property: user_organization_types
          - Deleted property: customer
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: user_assurance_levels
          - New property: user_nationalities
          - New property: user_organization_types
          - Deleted property: customer
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_assurance_levels
            - New property: user_nationalities
            - New property: user_organization_types
            - Modified property: project_metadata
              - Items changed
                - Properties changed
                  - New property: likert_high_label
                  - New property: likert_low_label
                  - New property: likert_scale_length
                  - New property: max_value
                  - New property: min_value

PUT /api/projects/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: user_assurance_levels
          - New property: user_nationalities
          - New property: user_organization_types
    - Modified media type: application/x-www-form-urlencoded
      - Schema changed
        - Properties changed
          - New property: user_assurance_levels
          - New property: user_nationalities
          - New property: user_organization_types
    - Modified media type: multipart/form-data
      - Schema changed
        - Properties changed
          - New property: user_assurance_levels
          - New property: user_nationalities
          - New property: user_organization_types
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_assurance_levels
            - New property: user_nationalities
            - New property: user_organization_types
            - Modified property: project_metadata
              - Items changed
                - Properties changed
                  - New property: likert_high_label
                  - New property: likert_low_label
                  - New property: likert_scale_length
                  - New property: max_value
                  - New property: min_value

POST /api/projects/{uuid}/add_user/

- Extensions changed
  - New extension: x-permissions

GET /api/projects/{uuid}/checklist/

- Extensions changed
  - New extension: x-permissions

GET /api/projects/{uuid}/completion_status/

- Extensions changed
  - New extension: x-permissions

POST /api/projects/{uuid}/delete_user/

- Extensions changed
  - New extension: x-permissions

GET /api/projects/{uuid}/list_users/

- Extensions changed
  - New extension: x-permissions
- New query param: role_template

HEAD /api/projects/{uuid}/list_users/

- Extensions changed
  - New extension: x-permissions
- New query param: role_template

POST /api/projects/{uuid}/move_project/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_assurance_levels
            - New property: user_nationalities
            - New property: user_organization_types
            - Modified property: project_metadata
              - Items changed
                - Properties changed
                  - New property: likert_high_label
                  - New property: likert_low_label
                  - New property: likert_scale_length
                  - New property: max_value
                  - New property: min_value

POST /api/projects/{uuid}/recover/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: user_assurance_levels
            - New property: user_nationalities
            - New property: user_organization_types
            - Modified property: project_metadata
              - Items changed
                - Properties changed
                  - New property: likert_high_label
                  - New property: likert_low_label
                  - New property: likert_scale_length
                  - New property: max_value
                  - New property: min_value

POST /api/projects/{uuid}/set_slug/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/projects/{uuid}/stats/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/projects/{uuid}/submit_answers/

- Extensions changed
  - New extension: x-permissions

POST /api/projects/{uuid}/sync_user_roles/

- Extensions changed
  - New extension: x-permissions

POST /api/projects/{uuid}/update_affiliation/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/projects/{uuid}/update_user/

- Extensions changed
  - New extension: x-permissions

GET /api/promotions-campaigns/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/promotions-campaigns/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/promotions-campaigns/

- Extensions changed
  - New extension: x-permissions

DELETE /api/promotions-campaigns/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/promotions-campaigns/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PUT /api/promotions-campaigns/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/promotions-campaigns/{uuid}/activate/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/promotions-campaigns/{uuid}/orders/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Deleted property: callback_url

GET /api/promotions-campaigns/{uuid}/resources/

- Extensions changed
  - New extension: x-permissions
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [display_limits prepaid_total_component_types spending_limit_status spending_limits terminated_at usage_limit_resumes_at]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: display_limits
              - New property: prepaid_total_component_types
              - New property: spending_limit_status
              - New property: spending_limits
              - New property: terminated_at
              - New property: usage_limit_resumes_at
              - Modified property: creation_order
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Deleted property: callback_url
              - Modified property: endpoints
                - Items changed
                  - Properties changed
                    - Modified property: url
                      - Format changed from '' to 'uri'
                      - MaxLength changed from null to 200
              - Modified property: offering_components
                - Items changed
                  - Properties changed
                    - New property: spending_limit_periods
              - Modified property: order_in_progress
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OrderDetails
                    - Properties changed
                      - Deleted property: callback_url

POST /api/promotions-campaigns/{uuid}/terminate/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/proposal-my-requested-resources/

- Extensions changed
  - New extension: x-permissions

HEAD /api/proposal-my-requested-resources/

- Extensions changed
  - New extension: x-permissions

GET /api/proposal-my-requested-resources/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/proposal-proposals/

- Extensions changed
  - New extension: x-permissions
- New query param: workflow_step
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: project_summary
                - MaxLength changed from null to 1000

HEAD /api/proposal-proposals/

- Extensions changed
  - New extension: x-permissions
- New query param: workflow_step

POST /api/proposal-proposals/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: project_summary
            - MaxLength changed from null to 1000
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: project_summary
              - MaxLength changed from null to 1000

GET /api/proposal-proposals/checklist-template/

- Extensions changed
  - New extension: x-permissions

HEAD /api/proposal-proposals/checklist-template/

- Extensions changed
  - New extension: x-permissions

GET /api/proposal-proposals/dashboard-stats/

- Extensions changed
  - New extension: x-permissions

DELETE /api/proposal-proposals/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/proposal-proposals/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: project_summary
              - MaxLength changed from null to 1000

POST /api/proposal-proposals/{uuid}/add_user/

- Extensions changed
  - New extension: x-permissions

POST /api/proposal-proposals/{uuid}/advance_workflow_step/

- Extensions changed
  - New extension: x-permissions

POST /api/proposal-proposals/{uuid}/attach_document/

- Extensions changed
  - New extension: x-permissions

GET /api/proposal-proposals/{uuid}/awarded_resources/

- Extensions changed
  - New extension: x-permissions
- Description changed from 'List what the allocation decision awards the proposal. Staff, support, the call's managers and organisers, and the managers of the offerings involved see it at any time; the applicant team once the decision is released.' to 'List what the allocation decision awards the proposal. Staff, support, the call's managers and organizers, and the managers of the offerings involved see it at any time; the applicant team once the decision is released.'
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
                            - New property: spending_limit_periods
                      - Modified property: options
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/OfferingOptions
                            - Properties changed
                              - Modified property: options
                                - AdditionalProperties changed
                                  - Properties changed
                                    - New property: display_limit_config
                                    - New property: transform

POST /api/proposal-proposals/{uuid}/awarded_resources/

- Extensions changed
  - New extension: x-permissions
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
                          - New property: spending_limit_periods
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: display_limit_config
                                  - New property: transform

DELETE /api/proposal-proposals/{uuid}/awarded_resources/{obj_uuid}/

- Extensions changed
  - New extension: x-permissions
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
                          - New property: spending_limit_periods
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: display_limit_config
                                  - New property: transform

GET /api/proposal-proposals/{uuid}/awarded_resources/{obj_uuid}/

- Extensions changed
  - New extension: x-permissions
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
                          - New property: spending_limit_periods
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: display_limit_config
                                  - New property: transform

PATCH /api/proposal-proposals/{uuid}/awarded_resources/{obj_uuid}/

- Extensions changed
  - New extension: x-permissions
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
                          - New property: spending_limit_periods
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: display_limit_config
                                  - New property: transform

PUT /api/proposal-proposals/{uuid}/awarded_resources/{obj_uuid}/

- Extensions changed
  - New extension: x-permissions
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
                          - New property: spending_limit_periods
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: display_limit_config
                                  - New property: transform

GET /api/proposal-proposals/{uuid}/checklist/

- Extensions changed
  - New extension: x-permissions

GET /api/proposal-proposals/{uuid}/checklist_review/

- Extensions changed
  - New extension: x-permissions

POST /api/proposal-proposals/{uuid}/complete_workflow_step/

- Extensions changed
  - New extension: x-permissions

GET /api/proposal-proposals/{uuid}/completion_review_status/

- Extensions changed
  - New extension: x-permissions

GET /api/proposal-proposals/{uuid}/completion_status/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/proposal-proposals/{uuid}/delete_user/

- Extensions changed
  - New extension: x-permissions

POST /api/proposal-proposals/{uuid}/detach_documents/

- Extensions changed
  - New extension: x-permissions

GET /api/proposal-proposals/{uuid}/list_users/

- Extensions changed
  - New extension: x-permissions
- New query param: role_template

HEAD /api/proposal-proposals/{uuid}/list_users/

- Extensions changed
  - New extension: x-permissions
- New query param: role_template

POST /api/proposal-proposals/{uuid}/reject_workflow_step/

- Extensions changed
  - New extension: x-permissions

POST /api/proposal-proposals/{uuid}/reopen_decision/

- Extensions changed
  - New extension: x-permissions

GET /api/proposal-proposals/{uuid}/resources/

- Extensions changed
  - New extension: x-permissions
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
                            - New property: spending_limit_periods
                      - Modified property: options
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/OfferingOptions
                            - Properties changed
                              - Modified property: options
                                - AdditionalProperties changed
                                  - Properties changed
                                    - New property: display_limit_config
                                    - New property: transform

POST /api/proposal-proposals/{uuid}/resources/

- Extensions changed
  - New extension: x-permissions
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
                          - New property: spending_limit_periods
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: display_limit_config
                                  - New property: transform

DELETE /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Extensions changed
  - New extension: x-permissions
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
                          - New property: spending_limit_periods
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: display_limit_config
                                  - New property: transform

GET /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Extensions changed
  - New extension: x-permissions
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
                          - New property: spending_limit_periods
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: display_limit_config
                                  - New property: transform

PATCH /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Extensions changed
  - New extension: x-permissions
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
                          - New property: spending_limit_periods
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: display_limit_config
                                  - New property: transform

PUT /api/proposal-proposals/{uuid}/resources/{obj_uuid}/

- Extensions changed
  - New extension: x-permissions
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
                          - New property: spending_limit_periods
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: display_limit_config
                                  - New property: transform

DELETE /api/proposal-proposals/{uuid}/resources/{obj_uuid}/purchase_order/

- Extensions changed
  - New extension: x-permissions

POST /api/proposal-proposals/{uuid}/resources/{obj_uuid}/purchase_order/

- Extensions changed
  - New extension: x-permissions

GET /api/proposal-proposals/{uuid}/step-checklist-responses/

- Extensions changed
  - New extension: x-permissions
- New query param: workflow_step

GET /api/proposal-proposals/{uuid}/step-checklist/

- Extensions changed
  - New extension: x-permissions

POST /api/proposal-proposals/{uuid}/submit-step-checklist-answers/

- Extensions changed
  - New extension: x-permissions

POST /api/proposal-proposals/{uuid}/submit/

- Extensions changed
  - New extension: x-permissions

POST /api/proposal-proposals/{uuid}/submit_answers/

- Extensions changed
  - New extension: x-permissions

POST /api/proposal-proposals/{uuid}/update_project_details/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: project_summary
            - MaxLength changed from null to 1000

POST /api/proposal-proposals/{uuid}/update_user/

- Extensions changed
  - New extension: x-permissions

GET /api/proposal-proposals/{uuid}/workflow_states/

- Extensions changed
  - New extension: x-permissions
- New query param: workflow_step

GET /api/proposal-protected-calls/

- Extensions changed
  - New extension: x-permissions
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [resource_template_selection_mode]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: resource_template_selection_mode
              - Modified property: carry_over_drafts
                - Description changed from 'Whether a draft still open when its round's cut-off passes moves on to the call's next round instead of being cancelled. Without a later round the draft is cancelled either way.' to 'Whether a draft still open when its round's cut-off passes moves on to the call's next round instead of being canceled. Without a later round the draft is canceled either way.'
              - Modified property: offerings
                - Items changed
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: spending_limit_periods
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: display_limit_config
                                  - New property: transform
              - Modified property: order_author_user
                - Description changed from 'The person orders are attributed to when the author is a named contact. Must hold a role on this call or on the organisation managing it.' to 'The person orders are attributed to when the author is a named contact. Must hold a role on this call or on the organization managing it.'
              - Modified property: resource_templates
                - Items changed
                  - Properties changed
                    - Modified property: requested_offering_components
                      - Items changed
                        - Properties changed
                          - New property: spending_limit_periods

HEAD /api/proposal-protected-calls/

- Extensions changed
  - New extension: x-permissions

POST /api/proposal-protected-calls/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: resource_template_selection_mode
          - Modified property: carry_over_drafts
            - Description changed from 'Whether a draft still open when its round's cut-off passes moves on to the call's next round instead of being cancelled. Without a later round the draft is cancelled either way.' to 'Whether a draft still open when its round's cut-off passes moves on to the call's next round instead of being canceled. Without a later round the draft is canceled either way.'
          - Modified property: order_author_user
            - Description changed from 'The person orders are attributed to when the author is a named contact. Must hold a role on this call or on the organisation managing it.' to 'The person orders are attributed to when the author is a named contact. Must hold a role on this call or on the organization managing it.'
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: resource_template_selection_mode
            - Modified property: carry_over_drafts
              - Description changed from 'Whether a draft still open when its round's cut-off passes moves on to the call's next round instead of being cancelled. Without a later round the draft is cancelled either way.' to 'Whether a draft still open when its round's cut-off passes moves on to the call's next round instead of being canceled. Without a later round the draft is canceled either way.'
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: spending_limit_periods
                  - Modified property: options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - New property: display_limit_config
                                - New property: transform
            - Modified property: order_author_user
              - Description changed from 'The person orders are attributed to when the author is a named contact. Must hold a role on this call or on the organisation managing it.' to 'The person orders are attributed to when the author is a named contact. Must hold a role on this call or on the organization managing it.'
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: requested_offering_components
                    - Items changed
                      - Properties changed
                        - New property: spending_limit_periods

GET /api/proposal-protected-calls/available_compliance_checklists/

- Extensions changed
  - New extension: x-permissions

HEAD /api/proposal-protected-calls/available_compliance_checklists/

- Extensions changed
  - New extension: x-permissions

GET /api/proposal-protected-calls/dashboard-stats/

- Extensions changed
  - New extension: x-permissions

POST /api/proposal-protected-calls/import_call/

- Extensions changed
  - New extension: x-permissions
- Description changed from 'Create a draft call under the given call managing organisation from a document produced by export_call. References that cannot be resolved by name on this portal are skipped and reported in warnings. The import is atomic.' to 'Create a draft call under the given call managing organization from a document produced by export_call. References that cannot be resolved by name on this portal are skipped and reported in warnings. The import is atomic.'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: manager
            - Description changed from 'Call managing organisation that will own the imported call.' to 'Call managing organization that will own the imported call.'

GET /api/proposal-protected-calls/step_checklists/

- Extensions changed
  - New extension: x-permissions

HEAD /api/proposal-protected-calls/step_checklists/

- Extensions changed
  - New extension: x-permissions

DELETE /api/proposal-protected-calls/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/proposal-protected-calls/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [resource_template_selection_mode]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: resource_template_selection_mode
            - Modified property: carry_over_drafts
              - Description changed from 'Whether a draft still open when its round's cut-off passes moves on to the call's next round instead of being cancelled. Without a later round the draft is cancelled either way.' to 'Whether a draft still open when its round's cut-off passes moves on to the call's next round instead of being canceled. Without a later round the draft is canceled either way.'
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: spending_limit_periods
                  - Modified property: options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - New property: display_limit_config
                                - New property: transform
            - Modified property: order_author_user
              - Description changed from 'The person orders are attributed to when the author is a named contact. Must hold a role on this call or on the organisation managing it.' to 'The person orders are attributed to when the author is a named contact. Must hold a role on this call or on the organization managing it.'
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: requested_offering_components
                    - Items changed
                      - Properties changed
                        - New property: spending_limit_periods

PATCH /api/proposal-protected-calls/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: resource_template_selection_mode
          - Modified property: carry_over_drafts
            - Description changed from 'Whether a draft still open when its round's cut-off passes moves on to the call's next round instead of being cancelled. Without a later round the draft is cancelled either way.' to 'Whether a draft still open when its round's cut-off passes moves on to the call's next round instead of being canceled. Without a later round the draft is canceled either way.'
          - Modified property: order_author_user
            - Description changed from 'The person orders are attributed to when the author is a named contact. Must hold a role on this call or on the organisation managing it.' to 'The person orders are attributed to when the author is a named contact. Must hold a role on this call or on the organization managing it.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: resource_template_selection_mode
            - Modified property: carry_over_drafts
              - Description changed from 'Whether a draft still open when its round's cut-off passes moves on to the call's next round instead of being cancelled. Without a later round the draft is cancelled either way.' to 'Whether a draft still open when its round's cut-off passes moves on to the call's next round instead of being canceled. Without a later round the draft is canceled either way.'
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: spending_limit_periods
                  - Modified property: options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - New property: display_limit_config
                                - New property: transform
            - Modified property: order_author_user
              - Description changed from 'The person orders are attributed to when the author is a named contact. Must hold a role on this call or on the organisation managing it.' to 'The person orders are attributed to when the author is a named contact. Must hold a role on this call or on the organization managing it.'
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: requested_offering_components
                    - Items changed
                      - Properties changed
                        - New property: spending_limit_periods

PUT /api/proposal-protected-calls/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: resource_template_selection_mode
          - Modified property: carry_over_drafts
            - Description changed from 'Whether a draft still open when its round's cut-off passes moves on to the call's next round instead of being cancelled. Without a later round the draft is cancelled either way.' to 'Whether a draft still open when its round's cut-off passes moves on to the call's next round instead of being canceled. Without a later round the draft is canceled either way.'
          - Modified property: order_author_user
            - Description changed from 'The person orders are attributed to when the author is a named contact. Must hold a role on this call or on the organisation managing it.' to 'The person orders are attributed to when the author is a named contact. Must hold a role on this call or on the organization managing it.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: resource_template_selection_mode
            - Modified property: carry_over_drafts
              - Description changed from 'Whether a draft still open when its round's cut-off passes moves on to the call's next round instead of being cancelled. Without a later round the draft is cancelled either way.' to 'Whether a draft still open when its round's cut-off passes moves on to the call's next round instead of being canceled. Without a later round the draft is canceled either way.'
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: spending_limit_periods
                  - Modified property: options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - New property: display_limit_config
                                - New property: transform
            - Modified property: order_author_user
              - Description changed from 'The person orders are attributed to when the author is a named contact. Must hold a role on this call or on the organisation managing it.' to 'The person orders are attributed to when the author is a named contact. Must hold a role on this call or on the organization managing it.'
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: requested_offering_components
                    - Items changed
                      - Properties changed
                        - New property: spending_limit_periods

POST /api/proposal-protected-calls/{uuid}/activate/

- Extensions changed
  - New extension: x-permissions

POST /api/proposal-protected-calls/{uuid}/add_user/

- Extensions changed
  - New extension: x-permissions

GET /api/proposal-protected-calls/{uuid}/affinity-matrix/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'any_of'
    - Added /0/of with value: '[map[description:Global support, for reads. kind:custom] map[kind:permission permission:PROPOSAL.MANAGE_REVIEW scopes:[* manager]]]'
    - Removed /0/permission with value: 'PROPOSAL.MANAGE_REVIEW'
    - Removed /0/scopes with value: '[* manager]'

POST /api/proposal-protected-calls/{uuid}/archive/

- Extensions changed
  - New extension: x-permissions

POST /api/proposal-protected-calls/{uuid}/attach_documents/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

GET /api/proposal-protected-calls/{uuid}/coi-configuration/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'any_of'
    - Added /0/of with value: '[map[description:Global support, for reads. kind:custom] map[kind:permission permission:PROPOSAL.MANAGE_REVIEW scopes:[* manager]]]'
    - Removed /0/permission with value: 'PROPOSAL.MANAGE_REVIEW'
    - Removed /0/scopes with value: '[* manager]'

PATCH /api/proposal-protected-calls/{uuid}/coi-configuration/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'any_of'
    - Added /0/of with value: '[map[description:Global support, for reads. kind:custom] map[kind:permission permission:PROPOSAL.MANAGE_REVIEW scopes:[* manager]]]'
    - Removed /0/permission with value: 'PROPOSAL.MANAGE_REVIEW'
    - Removed /0/scopes with value: '[* manager]'

GET /api/proposal-protected-calls/{uuid}/compliance_overview/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'any_of'
    - Added /0/of with value: '[map[description:Global support, for reads. kind:custom] map[kind:permission permission:CALL.UPDATE scopes:[* manager]]]'
    - Removed /0/permission with value: 'CALL.UPDATE'
    - Removed /0/scopes with value: '[* manager]'

POST /api/proposal-protected-calls/{uuid}/compute-affinities/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/proposal-protected-calls/{uuid}/conflict-summary/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'any_of'
    - Added /0/of with value: '[map[description:Global support, for reads. kind:custom] map[kind:permission permission:PROPOSAL.MANAGE_REVIEW scopes:[* manager]]]'
    - Removed /0/permission with value: 'PROPOSAL.MANAGE_REVIEW'
    - Removed /0/scopes with value: '[* manager]'

GET /api/proposal-protected-calls/{uuid}/conflicts/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'any_of'
    - Added /0/of with value: '[map[description:Global support, for reads. kind:custom] map[kind:permission permission:PROPOSAL.MANAGE_REVIEW scopes:[* manager]]]'
    - Removed /0/permission with value: 'PROPOSAL.MANAGE_REVIEW'
    - Removed /0/scopes with value: '[* manager]'

POST /api/proposal-protected-calls/{uuid}/create-manual-assignment/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/proposal-protected-calls/{uuid}/delete_user/

- Extensions changed
  - New extension: x-permissions

POST /api/proposal-protected-calls/{uuid}/detach_documents/

- Extensions changed
  - New extension: x-permissions

POST /api/proposal-protected-calls/{uuid}/detect-conflicts/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/proposal-protected-calls/{uuid}/duplicate/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: resource_template_selection_mode
            - Modified property: carry_over_drafts
              - Description changed from 'Whether a draft still open when its round's cut-off passes moves on to the call's next round instead of being cancelled. Without a later round the draft is cancelled either way.' to 'Whether a draft still open when its round's cut-off passes moves on to the call's next round instead of being canceled. Without a later round the draft is canceled either way.'
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: spending_limit_periods
                  - Modified property: options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - New property: display_limit_config
                                - New property: transform
            - Modified property: order_author_user
              - Description changed from 'The person orders are attributed to when the author is a named contact. Must hold a role on this call or on the organisation managing it.' to 'The person orders are attributed to when the author is a named contact. Must hold a role on this call or on the organization managing it.'
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: requested_offering_components
                    - Items changed
                      - Properties changed
                        - New property: spending_limit_periods

GET /api/proposal-protected-calls/{uuid}/export-proposals/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'any_of'
    - Added /0/of with value: '[map[description:Global support, for reads. kind:custom] map[kind:permission permission:CALL.UPDATE scopes:[* manager]]]'
    - Removed /0/permission with value: 'CALL.UPDATE'
    - Removed /0/scopes with value: '[* manager]'

GET /api/proposal-protected-calls/{uuid}/export-reviews/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'any_of'
    - Added /0/of with value: '[map[description:Global support, for reads. kind:custom] map[kind:permission permission:CALL.UPDATE scopes:[* manager]]]'
    - Removed /0/permission with value: 'CALL.UPDATE'
    - Removed /0/scopes with value: '[* manager]'

POST /api/proposal-protected-calls/{uuid}/export_call/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/proposal-protected-calls/{uuid}/generate-assignments/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/proposal-protected-calls/{uuid}/generate-suggestions/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/proposal-protected-calls/{uuid}/invite-by-email/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: invited_email
              - Default changed from null to ''

GET /api/proposal-protected-calls/{uuid}/list_users/

- Extensions changed
  - New extension: x-permissions
- New query param: role_template

HEAD /api/proposal-protected-calls/{uuid}/list_users/

- Extensions changed
  - New extension: x-permissions
- New query param: role_template

GET /api/proposal-protected-calls/{uuid}/matching-configuration/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'any_of'
    - Added /0/of with value: '[map[description:Global support, for reads. kind:custom] map[kind:permission permission:PROPOSAL.MANAGE_REVIEW scopes:[* manager]]]'
    - Removed /0/permission with value: 'PROPOSAL.MANAGE_REVIEW'
    - Removed /0/scopes with value: '[* manager]'

PATCH /api/proposal-protected-calls/{uuid}/matching-configuration/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'any_of'
    - Added /0/of with value: '[map[description:Global support, for reads. kind:custom] map[kind:permission permission:PROPOSAL.MANAGE_REVIEW scopes:[* manager]]]'
    - Removed /0/permission with value: 'PROPOSAL.MANAGE_REVIEW'
    - Removed /0/scopes with value: '[* manager]'

GET /api/proposal-protected-calls/{uuid}/offerings/

- Extensions changed
  - New extension: x-permissions
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
                    - New property: spending_limit_periods
              - Modified property: options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - New property: display_limit_config
                            - New property: transform

POST /api/proposal-protected-calls/{uuid}/offerings/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: spending_limit_periods
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: display_limit_config
                          - New property: transform

DELETE /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: spending_limit_periods
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: display_limit_config
                          - New property: transform

GET /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: spending_limit_periods
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: display_limit_config
                          - New property: transform

PATCH /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: spending_limit_periods
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: display_limit_config
                          - New property: transform

PUT /api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: spending_limit_periods
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: display_limit_config
                          - New property: transform

GET /api/proposal-protected-calls/{uuid}/proposals/{proposal_uuid}/compliance-answers/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/proposal-protected-calls/{uuid}/proposed-assignments/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'any_of'
    - Added /0/of with value: '[map[description:Global support, for reads. kind:custom] map[kind:permission permission:PROPOSAL.MANAGE_REVIEW scopes:[* manager]]]'
    - Removed /0/permission with value: 'PROPOSAL.MANAGE_REVIEW'
    - Removed /0/scopes with value: '[* manager]'

GET /api/proposal-protected-calls/{uuid}/resource_templates/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: requested_offering_components
                - Items changed
                  - Properties changed
                    - New property: spending_limit_periods

POST /api/proposal-protected-calls/{uuid}/resource_templates/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: requested_offering_components
              - Items changed
                - Properties changed
                  - New property: spending_limit_periods

DELETE /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: requested_offering_components
              - Items changed
                - Properties changed
                  - New property: spending_limit_periods

GET /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: requested_offering_components
              - Items changed
                - Properties changed
                  - New property: spending_limit_periods

PATCH /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: requested_offering_components
              - Items changed
                - Properties changed
                  - New property: spending_limit_periods

PUT /api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: requested_offering_components
              - Items changed
                - Properties changed
                  - New property: spending_limit_periods

POST /api/proposal-protected-calls/{uuid}/review_proposal_compliance/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/proposal-protected-calls/{uuid}/reviewer-pool/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'any_of'
    - Added /0/of with value: '[map[description:Global support, for reads. kind:custom] map[kind:permission permission:PROPOSAL.MANAGE_REVIEW scopes:[* manager]]]'
    - Removed /0/permission with value: 'PROPOSAL.MANAGE_REVIEW'
    - Removed /0/scopes with value: '[* manager]'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: invited_email
                - Default changed from null to ''

POST /api/proposal-protected-calls/{uuid}/reviewer-pool/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'any_of'
    - Added /0/of with value: '[map[description:Global support, for reads. kind:custom] map[kind:permission permission:PROPOSAL.MANAGE_REVIEW scopes:[* manager]]]'
    - Removed /0/permission with value: 'PROPOSAL.MANAGE_REVIEW'
    - Removed /0/scopes with value: '[* manager]'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: invited_email
                - Default changed from null to ''

POST /api/proposal-protected-calls/{uuid}/rounds-bulk-set/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/proposal-protected-calls/{uuid}/rounds/

- Extensions changed
  - New extension: x-permissions

POST /api/proposal-protected-calls/{uuid}/rounds/

- Extensions changed
  - New extension: x-permissions

DELETE /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/close/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: resource_template_selection_mode
          - Modified property: carry_over_drafts
            - Description changed from 'Whether a draft still open when its round's cut-off passes moves on to the call's next round instead of being cancelled. Without a later round the draft is cancelled either way.' to 'Whether a draft still open when its round's cut-off passes moves on to the call's next round instead of being canceled. Without a later round the draft is canceled either way.'
          - Modified property: order_author_user
            - Description changed from 'The person orders are attributed to when the author is a named contact. Must hold a role on this call or on the organisation managing it.' to 'The person orders are attributed to when the author is a named contact. Must hold a role on this call or on the organization managing it.'

POST /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/complete/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/publish_results/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/record_adoption/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/start_deciding/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/proposal-protected-calls/{uuid}/send-all-assignments/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/proposal-protected-calls/{uuid}/send-invitations/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/proposal-protected-calls/{uuid}/suggestions/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'any_of'
    - Added /0/of with value: '[map[description:Global support, for reads. kind:custom] map[kind:permission permission:PROPOSAL.MANAGE_REVIEW scopes:[* manager]]]'
    - Removed /0/permission with value: 'PROPOSAL.MANAGE_REVIEW'
    - Removed /0/scopes with value: '[* manager]'

POST /api/proposal-protected-calls/{uuid}/update_user/

- Extensions changed
  - New extension: x-permissions

GET /api/proposal-protected-calls/{uuid}/workflow_steps/

- Extensions changed
  - New extension: x-permissions

POST /api/proposal-protected-calls/{uuid}/workflow_steps/

- Extensions changed
  - New extension: x-permissions

DELETE /api/proposal-protected-calls/{uuid}/workflow_steps/{obj_uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/proposal-protected-calls/{uuid}/workflow_steps/{obj_uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/proposal-protected-calls/{uuid}/workflow_steps/{obj_uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/proposal-protected-calls/{uuid}/workflow_steps/{obj_uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/proposal-public-calls/

- Extensions changed
  - New extension: x-permissions
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [resource_template_selection_mode]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: resource_template_selection_mode
              - Modified property: offerings
                - Items changed
                  - Properties changed
                    - Modified property: components
                      - Items changed
                        - Properties changed
                          - New property: spending_limit_periods
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: display_limit_config
                                  - New property: transform
              - Modified property: resource_templates
                - Items changed
                  - Properties changed
                    - Modified property: requested_offering_components
                      - Items changed
                        - Properties changed
                          - New property: spending_limit_periods

HEAD /api/proposal-public-calls/

- Extensions changed
  - New extension: x-permissions

GET /api/proposal-public-calls/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [resource_template_selection_mode]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: resource_template_selection_mode
            - Modified property: offerings
              - Items changed
                - Properties changed
                  - Modified property: components
                    - Items changed
                      - Properties changed
                        - New property: spending_limit_periods
                  - Modified property: options
                    - Property 'AllOf' changed
                      - Modified schema: #/components/schemas/OfferingOptions
                        - Properties changed
                          - Modified property: options
                            - AdditionalProperties changed
                              - Properties changed
                                - New property: display_limit_config
                                - New property: transform
            - Modified property: resource_templates
              - Items changed
                - Properties changed
                  - Modified property: requested_offering_components
                    - Items changed
                      - Properties changed
                        - New property: spending_limit_periods

GET /api/proposal-public-calls/{uuid}/check_eligibility/

- Extensions changed
  - New extension: x-permissions

GET /api/proposal-requested-offerings/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
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
                    - New property: spending_limit_periods
              - Modified property: options
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/OfferingOptions
                    - Properties changed
                      - Modified property: options
                        - AdditionalProperties changed
                          - Properties changed
                            - New property: display_limit_config
                            - New property: transform

HEAD /api/proposal-requested-offerings/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/proposal-requested-offerings/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: components
              - Items changed
                - Properties changed
                  - New property: spending_limit_periods
            - Modified property: options
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/OfferingOptions
                  - Properties changed
                    - Modified property: options
                      - AdditionalProperties changed
                        - Properties changed
                          - New property: display_limit_config
                          - New property: transform

POST /api/proposal-requested-offerings/{uuid}/accept/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

POST /api/proposal-requested-offerings/{uuid}/cancel/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/proposal-requested-resources/

- Extensions changed
  - New extension: x-permissions
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
                            - New property: spending_limit_periods
                      - Modified property: options
                        - Property 'AllOf' changed
                          - Modified schema: #/components/schemas/OfferingOptions
                            - Properties changed
                              - Modified property: options
                                - AdditionalProperties changed
                                  - Properties changed
                                    - New property: display_limit_config
                                    - New property: transform

HEAD /api/proposal-requested-resources/

- Extensions changed
  - New extension: x-permissions

GET /api/proposal-requested-resources/{uuid}/

- Extensions changed
  - New extension: x-permissions
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
                          - New property: spending_limit_periods
                    - Modified property: options
                      - Property 'AllOf' changed
                        - Modified schema: #/components/schemas/OfferingOptions
                          - Properties changed
                            - Modified property: options
                              - AdditionalProperties changed
                                - Properties changed
                                  - New property: display_limit_config
                                  - New property: transform

GET /api/proposal-reviews/

- Extensions changed
  - New extension: x-permissions

HEAD /api/proposal-reviews/

- Extensions changed
  - New extension: x-permissions

POST /api/proposal-reviews/

- Extensions changed
  - New extension: x-permissions

GET /api/proposal-reviews/dashboard-stats/

- Extensions changed
  - New extension: x-permissions

DELETE /api/proposal-reviews/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/proposal-reviews/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/proposal-reviews/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/proposal-reviews/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/proposal-reviews/{uuid}/reject/

- Extensions changed
  - New extension: x-permissions

POST /api/proposal-reviews/{uuid}/submit/

- Extensions changed
  - New extension: x-permissions

GET /api/provider-canned-responses/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: provider_helpdesk
                - Description changed from '' to 'Helpdesk the response belongs to. Only staff can change it.'

HEAD /api/provider-canned-responses/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/provider-canned-responses/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: provider_helpdesk
            - Description changed from '' to 'Helpdesk the response belongs to. Only staff can change it.'
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: provider_helpdesk
              - Description changed from '' to 'Helpdesk the response belongs to. Only staff can change it.'

DELETE /api/provider-canned-responses/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/provider-canned-responses/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: provider_helpdesk
              - Description changed from '' to 'Helpdesk the response belongs to. Only staff can change it.'

PATCH /api/provider-canned-responses/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: provider_helpdesk
            - Description changed from '' to 'Helpdesk the response belongs to. Only staff can change it.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: provider_helpdesk
              - Description changed from '' to 'Helpdesk the response belongs to. Only staff can change it.'

PUT /api/provider-canned-responses/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: provider_helpdesk
            - Description changed from '' to 'Helpdesk the response belongs to. Only staff can change it.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: provider_helpdesk
              - Description changed from '' to 'Helpdesk the response belongs to. Only staff can change it.'

POST /api/provider-canned-responses/{uuid}/render/

- Extensions changed
  - New extension: x-permissions

GET /api/provider-helpdesks/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: backend_type
                - Property 'AllOf' changed
                  - Schemas added: #/components/schemas/BackendTypeEnum
                - Type changed from 'string' to ''
                - Description changed from '' to 'Helpdesk system the helpdesk connects to. Only staff can change it.'
                - Deleted enum values: [basic email atlassian zammad smax]
              - Modified property: service_provider
                - Description changed from '' to 'Service provider the helpdesk serves. Only staff can change it.'
              - Modified property: settings
                - Description changed from 'Backend-specific configuration.' to 'Backend-specific configuration. Only staff can change it, and only staff see the credentials in it.'

HEAD /api/provider-helpdesks/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/provider-helpdesks/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: backend_type
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/BackendTypeEnum
            - Type changed from 'string' to ''
            - Description changed from '' to 'Helpdesk system the helpdesk connects to. Only staff can change it.'
            - Deleted enum values: [basic email atlassian zammad smax]
          - Modified property: service_provider
            - Description changed from '' to 'Service provider the helpdesk serves. Only staff can change it.'
          - Modified property: settings
            - Description changed from 'Backend-specific configuration.' to 'Backend-specific configuration. Only staff can change it, and only staff see the credentials in it.'
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: backend_type
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/BackendTypeEnum
              - Type changed from 'string' to ''
              - Description changed from '' to 'Helpdesk system the helpdesk connects to. Only staff can change it.'
              - Deleted enum values: [basic email atlassian zammad smax]
            - Modified property: service_provider
              - Description changed from '' to 'Service provider the helpdesk serves. Only staff can change it.'
            - Modified property: settings
              - Description changed from 'Backend-specific configuration.' to 'Backend-specific configuration. Only staff can change it, and only staff see the credentials in it.'

DELETE /api/provider-helpdesks/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/provider-helpdesks/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: backend_type
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/BackendTypeEnum
              - Type changed from 'string' to ''
              - Description changed from '' to 'Helpdesk system the helpdesk connects to. Only staff can change it.'
              - Deleted enum values: [basic email atlassian zammad smax]
            - Modified property: service_provider
              - Description changed from '' to 'Service provider the helpdesk serves. Only staff can change it.'
            - Modified property: settings
              - Description changed from 'Backend-specific configuration.' to 'Backend-specific configuration. Only staff can change it, and only staff see the credentials in it.'

PATCH /api/provider-helpdesks/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: backend_type
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/BackendTypeEnum
            - Type changed from 'string' to ''
            - Description changed from '' to 'Helpdesk system the helpdesk connects to. Only staff can change it.'
            - Deleted enum values: [basic email atlassian zammad smax]
          - Modified property: service_provider
            - Description changed from '' to 'Service provider the helpdesk serves. Only staff can change it.'
          - Modified property: settings
            - Description changed from 'Backend-specific configuration.' to 'Backend-specific configuration. Only staff can change it, and only staff see the credentials in it.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: backend_type
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/BackendTypeEnum
              - Type changed from 'string' to ''
              - Description changed from '' to 'Helpdesk system the helpdesk connects to. Only staff can change it.'
              - Deleted enum values: [basic email atlassian zammad smax]
            - Modified property: service_provider
              - Description changed from '' to 'Service provider the helpdesk serves. Only staff can change it.'
            - Modified property: settings
              - Description changed from 'Backend-specific configuration.' to 'Backend-specific configuration. Only staff can change it, and only staff see the credentials in it.'

PUT /api/provider-helpdesks/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: backend_type
            - Property 'AllOf' changed
              - Schemas added: #/components/schemas/BackendTypeEnum
            - Type changed from 'string' to ''
            - Description changed from '' to 'Helpdesk system the helpdesk connects to. Only staff can change it.'
            - Deleted enum values: [basic email atlassian zammad smax]
          - Modified property: service_provider
            - Description changed from '' to 'Service provider the helpdesk serves. Only staff can change it.'
          - Modified property: settings
            - Description changed from 'Backend-specific configuration.' to 'Backend-specific configuration. Only staff can change it, and only staff see the credentials in it.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: backend_type
              - Property 'AllOf' changed
                - Schemas added: #/components/schemas/BackendTypeEnum
              - Type changed from 'string' to ''
              - Description changed from '' to 'Helpdesk system the helpdesk connects to. Only staff can change it.'
              - Deleted enum values: [basic email atlassian zammad smax]
            - Modified property: service_provider
              - Description changed from '' to 'Service provider the helpdesk serves. Only staff can change it.'
            - Modified property: settings
              - Description changed from 'Backend-specific configuration.' to 'Backend-specific configuration. Only staff can change it, and only staff see the credentials in it.'

POST /api/provider-helpdesks/{uuid}/validate/

- Extensions changed
  - New extension: x-permissions

GET /api/provider-invoice-items/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/provider-invoice-items/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/provider-invoice-items/{id}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/provider-support-users/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: provider_helpdesk
                - Description changed from '' to 'Helpdesk the agent answers for. Only staff can change it.'
              - Modified property: user
                - Description changed from '' to 'User who is the agent. Only staff can change it.'

HEAD /api/provider-support-users/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/provider-support-users/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: provider_helpdesk
            - Description changed from '' to 'Helpdesk the agent answers for. Only staff can change it.'
          - Modified property: user
            - Description changed from '' to 'User who is the agent. Only staff can change it.'
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: provider_helpdesk
              - Description changed from '' to 'Helpdesk the agent answers for. Only staff can change it.'
            - Modified property: user
              - Description changed from '' to 'User who is the agent. Only staff can change it.'

GET /api/provider-support-users/team_workload/

- Extensions changed
  - New extension: x-permissions

HEAD /api/provider-support-users/team_workload/

- Extensions changed
  - New extension: x-permissions

DELETE /api/provider-support-users/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/provider-support-users/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: provider_helpdesk
              - Description changed from '' to 'Helpdesk the agent answers for. Only staff can change it.'
            - Modified property: user
              - Description changed from '' to 'User who is the agent. Only staff can change it.'

PATCH /api/provider-support-users/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: provider_helpdesk
            - Description changed from '' to 'Helpdesk the agent answers for. Only staff can change it.'
          - Modified property: user
            - Description changed from '' to 'User who is the agent. Only staff can change it.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: provider_helpdesk
              - Description changed from '' to 'Helpdesk the agent answers for. Only staff can change it.'
            - Modified property: user
              - Description changed from '' to 'User who is the agent. Only staff can change it.'

PUT /api/provider-support-users/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: provider_helpdesk
            - Description changed from '' to 'Helpdesk the agent answers for. Only staff can change it.'
          - Modified property: user
            - Description changed from '' to 'User who is the agent. Only staff can change it.'
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: provider_helpdesk
              - Description changed from '' to 'Helpdesk the agent answers for. Only staff can change it.'
            - Modified property: user
              - Description changed from '' to 'User who is the agent. Only staff can change it.'

GET /api/provider-tickets/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - New required property: customer
              - New required property: escalated_at
              - New required property: project
            - Properties changed
              - Modified property: customer
                - ReadOnly changed from false to true
              - Modified property: escalated_at
                - ReadOnly changed from false to true
              - Modified property: project
                - ReadOnly changed from false to true

HEAD /api/provider-tickets/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/provider-tickets/stats/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/provider-tickets/stats/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/provider-tickets/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: customer
            - New required property: escalated_at
            - New required property: project
          - Properties changed
            - Modified property: customer
              - ReadOnly changed from false to true
            - Modified property: escalated_at
              - ReadOnly changed from false to true
            - Modified property: project
              - ReadOnly changed from false to true

PATCH /api/provider-tickets/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: customer
            - New required property: escalated_at
            - New required property: project
          - Properties changed
            - Modified property: customer
              - ReadOnly changed from false to true
            - Modified property: escalated_at
              - ReadOnly changed from false to true
            - Modified property: project
              - ReadOnly changed from false to true

PUT /api/provider-tickets/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: customer
            - New required property: escalated_at
            - New required property: project
          - Properties changed
            - Modified property: customer
              - ReadOnly changed from false to true
            - Modified property: escalated_at
              - ReadOnly changed from false to true
            - Modified property: project
              - ReadOnly changed from false to true

POST /api/provider-tickets/{uuid}/assign/

- Extensions changed
  - New extension: x-permissions

POST /api/provider-tickets/{uuid}/claim/

- Extensions changed
  - New extension: x-permissions
- Request body changed

POST /api/provider-tickets/{uuid}/comment/

- Extensions changed
  - New extension: x-permissions

GET /api/provider-tickets/{uuid}/customer_context/

- Extensions changed
  - New extension: x-permissions
- Description changed from '' to 'The original ticket's caller (full name, email and organization), its resource, and the caller's five latest other tickets among those the provider ticket list shows the requester: tickets routed to a helpdesk they speak for, as an owner of the service provider's organization or as an active agent. Staff and support see the caller's tickets routed to any provider. Tickets kept on the operator's own desk are not listed.'

POST /api/provider-tickets/{uuid}/resolve/

- Extensions changed
  - New extension: x-permissions

GET /api/public-maintenance-announcements/

- Extensions changed
  - New extension: x-permissions
- New query param: offering_uuid
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: affected_offerings
                - Items changed
                  - Properties changed
                    - New property: affected_partitions

HEAD /api/public-maintenance-announcements/

- Extensions changed
  - New extension: x-permissions
- New query param: offering_uuid

GET /api/public-maintenance-announcements/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: affected_offerings
              - Items changed
                - Properties changed
                  - New property: affected_partitions

POST /api/query/

- Extensions changed
  - New extension: x-permissions

GET /api/rabbitmq-overview/

- Extensions changed
  - New extension: x-permissions

GET /api/rabbitmq-stats/

- Extensions changed
  - New extension: x-permissions

POST /api/rabbitmq-stats/

- Extensions changed
  - New extension: x-permissions

GET /api/rabbitmq-user-stats/

- Extensions changed
  - New extension: x-permissions

GET /api/rabbitmq-vhost-stats/

- Extensions changed
  - New extension: x-permissions

GET /api/rancher-apps/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: backend_id
                - ReadOnly changed from false to true
                - MaxLength changed from 255 to null
              - Modified property: error_message
                - ReadOnly changed from false to true
              - Modified property: error_traceback
                - ReadOnly changed from false to true
              - Modified property: runtime_state
                - ReadOnly changed from false to true
                - MaxLength changed from 150 to null

HEAD /api/rancher-apps/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/rancher-apps/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: backend_id
          - Deleted property: error_message
          - Deleted property: error_traceback
          - Deleted property: runtime_state
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: backend_id
              - ReadOnly changed from false to true
              - MaxLength changed from 255 to null
            - Modified property: error_message
              - ReadOnly changed from false to true
            - Modified property: error_traceback
              - ReadOnly changed from false to true
            - Modified property: runtime_state
              - ReadOnly changed from false to true
              - MaxLength changed from 150 to null

DELETE /api/rancher-apps/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/rancher-apps/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: backend_id
              - ReadOnly changed from false to true
              - MaxLength changed from 255 to null
            - Modified property: error_message
              - ReadOnly changed from false to true
            - Modified property: error_traceback
              - ReadOnly changed from false to true
            - Modified property: runtime_state
              - ReadOnly changed from false to true
              - MaxLength changed from 150 to null

PATCH /api/rancher-apps/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: backend_id
          - Deleted property: error_message
          - Deleted property: error_traceback
          - Deleted property: namespace
          - Deleted property: namespace_name
          - Deleted property: project
          - Deleted property: rancher_project
          - Deleted property: runtime_state
          - Deleted property: service_settings
          - Deleted property: template
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: backend_id
              - ReadOnly changed from false to true
              - MaxLength changed from 255 to null
            - Modified property: error_message
              - ReadOnly changed from false to true
            - Modified property: error_traceback
              - ReadOnly changed from false to true
            - Modified property: runtime_state
              - ReadOnly changed from false to true
              - MaxLength changed from 150 to null

PUT /api/rancher-apps/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: backend_id
          - Deleted property: error_message
          - Deleted property: error_traceback
          - Deleted property: runtime_state
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: backend_id
              - ReadOnly changed from false to true
              - MaxLength changed from 255 to null
            - Modified property: error_message
              - ReadOnly changed from false to true
            - Modified property: error_traceback
              - ReadOnly changed from false to true
            - Modified property: runtime_state
              - ReadOnly changed from false to true
              - MaxLength changed from 150 to null

POST /api/rancher-apps/{uuid}/pull/

- Extensions changed
  - New extension: x-permissions

POST /api/rancher-apps/{uuid}/set_erred/

- Extensions changed
  - New extension: x-permissions

POST /api/rancher-apps/{uuid}/set_ok/

- Extensions changed
  - New extension: x-permissions

POST /api/rancher-apps/{uuid}/unlink/

- Extensions changed
  - New extension: x-permissions

GET /api/rancher-catalogs/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/rancher-catalogs/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/rancher-catalogs/

- Extensions changed
  - New extension: x-permissions

DELETE /api/rancher-catalogs/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/rancher-catalogs/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

PATCH /api/rancher-catalogs/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: scope
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: scope
              - ReadOnly changed from false to true

PUT /api/rancher-catalogs/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: scope
        - Properties changed
          - Deleted property: scope
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: scope
              - ReadOnly changed from false to true

POST /api/rancher-catalogs/{uuid}/refresh/

- Extensions changed
  - New extension: x-permissions

GET /api/rancher-cluster-security-groups/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/rancher-cluster-security-groups/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/rancher-cluster-security-groups/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/rancher-cluster-security-groups/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/rancher-cluster-security-groups/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/rancher-cluster-templates/

- Extensions changed
  - New extension: x-permissions

HEAD /api/rancher-cluster-templates/

- Extensions changed
  - New extension: x-permissions

GET /api/rancher-cluster-templates/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/rancher-clusters/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/rancher-clusters/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/rancher-clusters/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/rancher-clusters/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: vm_project

PUT /api/rancher-clusters/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: vm_project

POST /api/rancher-clusters/{uuid}/create_management_security_group/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: vm_project

POST /api/rancher-clusters/{uuid}/import_yaml/

- Extensions changed
  - New extension: x-permissions

POST /api/rancher-clusters/{uuid}/pull/

- Extensions changed
  - New extension: x-permissions

POST /api/rancher-clusters/{uuid}/set_erred/

- Extensions changed
  - New extension: x-permissions

POST /api/rancher-clusters/{uuid}/set_ok/

- Extensions changed
  - New extension: x-permissions

POST /api/rancher-clusters/{uuid}/unlink/

- Extensions changed
  - New extension: x-permissions

GET /api/rancher-hpas/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/rancher-hpas/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/rancher-hpas/

- Extensions changed
  - New extension: x-permissions

DELETE /api/rancher-hpas/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/rancher-hpas/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/rancher-hpas/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/rancher-hpas/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/rancher-hpas/{uuid}/pull/

- Extensions changed
  - New extension: x-permissions

POST /api/rancher-hpas/{uuid}/set_erred/

- Extensions changed
  - New extension: x-permissions

POST /api/rancher-hpas/{uuid}/set_ok/

- Extensions changed
  - New extension: x-permissions

POST /api/rancher-hpas/{uuid}/unlink/

- Extensions changed
  - New extension: x-permissions

GET /api/rancher-hpas/{uuid}/yaml/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PUT /api/rancher-hpas/{uuid}/yaml/

- Extensions changed
  - New extension: x-permissions

GET /api/rancher-ingresses/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: backend_id
                - ReadOnly changed from false to true
                - MaxLength changed from 255 to null
              - Modified property: error_message
                - ReadOnly changed from false to true
              - Modified property: error_traceback
                - ReadOnly changed from false to true
              - Modified property: runtime_state
                - ReadOnly changed from false to true
                - MaxLength changed from 150 to null

HEAD /api/rancher-ingresses/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/rancher-ingresses/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: backend_id
          - Deleted property: error_message
          - Deleted property: error_traceback
          - Deleted property: runtime_state
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: backend_id
              - ReadOnly changed from false to true
              - MaxLength changed from 255 to null
            - Modified property: error_message
              - ReadOnly changed from false to true
            - Modified property: error_traceback
              - ReadOnly changed from false to true
            - Modified property: runtime_state
              - ReadOnly changed from false to true
              - MaxLength changed from 150 to null

DELETE /api/rancher-ingresses/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/rancher-ingresses/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: backend_id
              - ReadOnly changed from false to true
              - MaxLength changed from 255 to null
            - Modified property: error_message
              - ReadOnly changed from false to true
            - Modified property: error_traceback
              - ReadOnly changed from false to true
            - Modified property: runtime_state
              - ReadOnly changed from false to true
              - MaxLength changed from 150 to null

PATCH /api/rancher-ingresses/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: backend_id
          - Deleted property: error_message
          - Deleted property: error_traceback
          - Deleted property: namespace
          - Deleted property: project
          - Deleted property: rancher_project
          - Deleted property: runtime_state
          - Deleted property: service_settings
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: backend_id
              - ReadOnly changed from false to true
              - MaxLength changed from 255 to null
            - Modified property: error_message
              - ReadOnly changed from false to true
            - Modified property: error_traceback
              - ReadOnly changed from false to true
            - Modified property: runtime_state
              - ReadOnly changed from false to true
              - MaxLength changed from 150 to null

PUT /api/rancher-ingresses/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: backend_id
          - Deleted property: error_message
          - Deleted property: error_traceback
          - Deleted property: runtime_state
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: backend_id
              - ReadOnly changed from false to true
              - MaxLength changed from 255 to null
            - Modified property: error_message
              - ReadOnly changed from false to true
            - Modified property: error_traceback
              - ReadOnly changed from false to true
            - Modified property: runtime_state
              - ReadOnly changed from false to true
              - MaxLength changed from 150 to null

POST /api/rancher-ingresses/{uuid}/pull/

- Extensions changed
  - New extension: x-permissions

POST /api/rancher-ingresses/{uuid}/set_erred/

- Extensions changed
  - New extension: x-permissions

POST /api/rancher-ingresses/{uuid}/set_ok/

- Extensions changed
  - New extension: x-permissions

POST /api/rancher-ingresses/{uuid}/unlink/

- Extensions changed
  - New extension: x-permissions

GET /api/rancher-ingresses/{uuid}/yaml/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PUT /api/rancher-ingresses/{uuid}/yaml/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: backend_id
          - Deleted property: error_message
          - Deleted property: error_traceback
          - Deleted property: runtime_state

GET /api/rancher-namespaces/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/rancher-namespaces/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/rancher-namespaces/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/rancher-nodes/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/rancher-nodes/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/rancher-nodes/

- Extensions changed
  - New extension: x-permissions

DELETE /api/rancher-nodes/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/rancher-nodes/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/rancher-nodes/{uuid}/console/

- Extensions changed
  - New extension: x-permissions

GET /api/rancher-nodes/{uuid}/console_log/

- Extensions changed
  - New extension: x-permissions

POST /api/rancher-nodes/{uuid}/link_openstack/

- Extensions changed
  - New extension: x-permissions

POST /api/rancher-nodes/{uuid}/pull/

- Extensions changed
  - New extension: x-permissions

POST /api/rancher-nodes/{uuid}/set_erred/

- Extensions changed
  - New extension: x-permissions

POST /api/rancher-nodes/{uuid}/set_ok/

- Extensions changed
  - New extension: x-permissions

POST /api/rancher-nodes/{uuid}/unlink/

- Extensions changed
  - New extension: x-permissions

POST /api/rancher-nodes/{uuid}/unlink_openstack/

- Extensions changed
  - New extension: x-permissions

GET /api/rancher-projects/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/rancher-projects/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/rancher-projects/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/rancher-projects/{uuid}/secrets/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/rancher-role-templates/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/rancher-role-templates/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/rancher-role-templates/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/rancher-services/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: backend_id
                - ReadOnly changed from false to true
                - MaxLength changed from 255 to null
              - Modified property: cluster_ip
                - Property 'OneOf' changed
                  - Schemas deleted: subschema #1, subschema #2
                - Type changed from '' to 'string'
                - Format changed from '' to 'ipv4'
                - Description changed from 'An IPv4 or IPv6 address.' to ''
              - Modified property: error_message
                - ReadOnly changed from false to true
              - Modified property: error_traceback
                - ReadOnly changed from false to true
              - Modified property: runtime_state
                - ReadOnly changed from false to true
                - MaxLength changed from 150 to null

HEAD /api/rancher-services/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/rancher-services/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: backend_id
          - Deleted property: error_message
          - Deleted property: error_traceback
          - Deleted property: runtime_state
          - Modified property: cluster_ip
            - Property 'OneOf' changed
              - Schemas deleted: subschema #1, subschema #2
            - Type changed from '' to 'string'
            - Format changed from '' to 'ipv4'
            - Description changed from 'An IPv4 or IPv6 address.' to ''
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - New required property: backend_id
            - New required property: error_message
            - New required property: error_traceback
            - New required property: runtime_state
          - Properties changed
            - Modified property: backend_id
              - ReadOnly changed from false to true
              - MaxLength changed from 255 to null
            - Modified property: cluster_ip
              - Property 'OneOf' changed
                - Schemas deleted: subschema #1, subschema #2
              - Type changed from '' to 'string'
              - Format changed from '' to 'ipv4'
              - Description changed from 'An IPv4 or IPv6 address.' to ''
            - Modified property: error_message
              - ReadOnly changed from false to true
            - Modified property: error_traceback
              - ReadOnly changed from false to true
            - Modified property: runtime_state
              - ReadOnly changed from false to true
              - MaxLength changed from 150 to null

DELETE /api/rancher-services/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/rancher-services/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: backend_id
              - ReadOnly changed from false to true
              - MaxLength changed from 255 to null
            - Modified property: cluster_ip
              - Property 'OneOf' changed
                - Schemas deleted: subschema #1, subschema #2
              - Type changed from '' to 'string'
              - Format changed from '' to 'ipv4'
              - Description changed from 'An IPv4 or IPv6 address.' to ''
            - Modified property: error_message
              - ReadOnly changed from false to true
            - Modified property: error_traceback
              - ReadOnly changed from false to true
            - Modified property: runtime_state
              - ReadOnly changed from false to true
              - MaxLength changed from 150 to null

PATCH /api/rancher-services/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Deleted property: backend_id
          - Deleted property: error_message
          - Deleted property: error_traceback
          - Deleted property: namespace
          - Deleted property: project
          - Deleted property: runtime_state
          - Deleted property: service_settings
          - Modified property: cluster_ip
            - Property 'OneOf' changed
              - Schemas deleted: subschema #1, subschema #2
            - Type changed from '' to 'string'
            - Format changed from '' to 'ipv4'
            - Description changed from 'An IPv4 or IPv6 address.' to ''
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: backend_id
              - ReadOnly changed from false to true
              - MaxLength changed from 255 to null
            - Modified property: cluster_ip
              - Property 'OneOf' changed
                - Schemas deleted: subschema #1, subschema #2
              - Type changed from '' to 'string'
              - Format changed from '' to 'ipv4'
              - Description changed from 'An IPv4 or IPv6 address.' to ''
            - Modified property: error_message
              - ReadOnly changed from false to true
            - Modified property: error_traceback
              - ReadOnly changed from false to true
            - Modified property: runtime_state
              - ReadOnly changed from false to true
              - MaxLength changed from 150 to null

PUT /api/rancher-services/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: project
          - Deleted required property: service_settings
        - Properties changed
          - Deleted property: backend_id
          - Deleted property: error_message
          - Deleted property: error_traceback
          - Deleted property: namespace
          - Deleted property: project
          - Deleted property: runtime_state
          - Deleted property: service_settings
          - Modified property: cluster_ip
            - Property 'OneOf' changed
              - Schemas deleted: subschema #1, subschema #2
            - Type changed from '' to 'string'
            - Format changed from '' to 'ipv4'
            - Description changed from 'An IPv4 or IPv6 address.' to ''
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: backend_id
              - ReadOnly changed from false to true
              - MaxLength changed from 255 to null
            - Modified property: cluster_ip
              - Property 'OneOf' changed
                - Schemas deleted: subschema #1, subschema #2
              - Type changed from '' to 'string'
              - Format changed from '' to 'ipv4'
              - Description changed from 'An IPv4 or IPv6 address.' to ''
            - Modified property: error_message
              - ReadOnly changed from false to true
            - Modified property: error_traceback
              - ReadOnly changed from false to true
            - Modified property: runtime_state
              - ReadOnly changed from false to true
              - MaxLength changed from 150 to null

POST /api/rancher-services/{uuid}/pull/

- Extensions changed
  - New extension: x-permissions

POST /api/rancher-services/{uuid}/set_erred/

- Extensions changed
  - New extension: x-permissions

POST /api/rancher-services/{uuid}/set_ok/

- Extensions changed
  - New extension: x-permissions

POST /api/rancher-services/{uuid}/unlink/

- Extensions changed
  - New extension: x-permissions

GET /api/rancher-services/{uuid}/yaml/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PUT /api/rancher-services/{uuid}/yaml/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: project
          - Deleted required property: service_settings
        - Properties changed
          - Deleted property: backend_id
          - Deleted property: error_message
          - Deleted property: error_traceback
          - Deleted property: namespace
          - Deleted property: project
          - Deleted property: runtime_state
          - Deleted property: service_settings
          - Modified property: cluster_ip
            - Property 'OneOf' changed
              - Schemas deleted: subschema #1, subschema #2
            - Type changed from '' to 'string'
            - Format changed from '' to 'ipv4'
            - Description changed from 'An IPv4 or IPv6 address.' to ''

GET /api/rancher-template-versions/{template_uuid}/{version}/

- Extensions changed
  - New extension: x-permissions

GET /api/rancher-templates/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/rancher-templates/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/rancher-templates/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/rancher-users/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/rancher-users/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/rancher-users/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/rancher-workloads/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/rancher-workloads/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/rancher-workloads/

- Extensions changed
  - New extension: x-permissions

DELETE /api/rancher-workloads/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/rancher-workloads/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/rancher-workloads/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/rancher-workloads/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/rancher-workloads/{uuid}/redeploy/

- Extensions changed
  - New extension: x-permissions

GET /api/rancher-workloads/{uuid}/yaml/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PUT /api/rancher-workloads/{uuid}/yaml/

- Extensions changed
  - New extension: x-permissions

POST /api/remote-eduteams/

- Extensions changed
  - New extension: x-permissions

POST /api/remote-waldur-api/cancel_termination/{uuid}

- Extensions changed
  - New extension: x-permissions

POST /api/remote-waldur-api/import_offering/

- Extensions changed
  - New extension: x-permissions

POST /api/remote-waldur-api/pull_offering_details/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/remote-waldur-api/pull_offering_orders/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/remote-waldur-api/pull_offering_resources/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/remote-waldur-api/pull_offering_robot_accounts/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/remote-waldur-api/pull_offering_usage/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/remote-waldur-api/pull_offering_users/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/remote-waldur-api/pull_order/{uuid}

- Extensions changed
  - New extension: x-permissions

POST /api/remote-waldur-api/pull_resource_robot_accounts/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/remote-waldur-api/push_project_data/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/remote-waldur-api/remote_categories/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: columns
                - Items changed
                  - Properties changed
                    - Modified property: widget
                      - Description changed from 'Widget field allows to customise table cell rendering.' to 'Widget field allows to customize table cell rendering.'

POST /api/remote-waldur-api/remote_customers/

- Extensions changed
  - New extension: x-permissions

GET /api/remote-waldur-api/remote_resource_order_status/{resource_uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/remote-waldur-api/remote_resource_status/{resource_uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/remote-waldur-api/remote_resource_team_status/{resource_uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/remote-waldur-api/shared_offerings/

- Extensions changed
  - New extension: x-permissions

POST /api/remote-waldur-api/sync_resource/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/remote-waldur-api/sync_resource_project_permissions/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Description changed from '' to 'Queue a push of the resource's project team to the remote Waldur.'
- Responses changed
  - New response: 202
  - Deleted response: 200

GET /api/reviewer-bids/

- Extensions changed
  - New extension: x-permissions

HEAD /api/reviewer-bids/

- Extensions changed
  - New extension: x-permissions

POST /api/reviewer-bids/

- Extensions changed
  - New extension: x-permissions

POST /api/reviewer-bids/bulk-submit/

- Extensions changed
  - New extension: x-permissions

GET /api/reviewer-bids/my-bids/

- Extensions changed
  - New extension: x-permissions

HEAD /api/reviewer-bids/my-bids/

- Extensions changed
  - New extension: x-permissions

POST /api/reviewer-bids/submit/

- Extensions changed
  - New extension: x-permissions

DELETE /api/reviewer-bids/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/reviewer-bids/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/reviewer-bids/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/reviewer-bids/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/reviewer-invitations/{token}/

- Extensions changed
  - New extension: x-permissions

POST /api/reviewer-invitations/{token}/accept/

- Extensions changed
  - New extension: x-permissions

POST /api/reviewer-invitations/{token}/decline/

- Extensions changed
  - New extension: x-permissions

GET /api/reviewer-profiles/

- Extensions changed
  - New extension: x-permissions

HEAD /api/reviewer-profiles/

- Extensions changed
  - New extension: x-permissions

POST /api/reviewer-profiles/

- Extensions changed
  - New extension: x-permissions

GET /api/reviewer-profiles/me/

- Extensions changed
  - New extension: x-permissions

HEAD /api/reviewer-profiles/me/

- Extensions changed
  - New extension: x-permissions

PATCH /api/reviewer-profiles/me/

- Extensions changed
  - New extension: x-permissions

POST /api/reviewer-profiles/me/

- Extensions changed
  - New extension: x-permissions

POST /api/reviewer-profiles/publish/

- Extensions changed
  - New extension: x-permissions

POST /api/reviewer-profiles/unpublish/

- Extensions changed
  - New extension: x-permissions

GET /api/reviewer-profiles/{reviewer_profile_uuid}/affiliations/

- Extensions changed
  - New extension: x-permissions

HEAD /api/reviewer-profiles/{reviewer_profile_uuid}/affiliations/

- Extensions changed
  - New extension: x-permissions

POST /api/reviewer-profiles/{reviewer_profile_uuid}/affiliations/

- Extensions changed
  - New extension: x-permissions

DELETE /api/reviewer-profiles/{reviewer_profile_uuid}/affiliations/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/reviewer-profiles/{reviewer_profile_uuid}/affiliations/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/reviewer-profiles/{reviewer_profile_uuid}/affiliations/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/reviewer-profiles/{reviewer_profile_uuid}/affiliations/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/reviewer-profiles/{reviewer_profile_uuid}/expertise/

- Extensions changed
  - New extension: x-permissions

HEAD /api/reviewer-profiles/{reviewer_profile_uuid}/expertise/

- Extensions changed
  - New extension: x-permissions

POST /api/reviewer-profiles/{reviewer_profile_uuid}/expertise/

- Extensions changed
  - New extension: x-permissions

DELETE /api/reviewer-profiles/{reviewer_profile_uuid}/expertise/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/reviewer-profiles/{reviewer_profile_uuid}/expertise/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/reviewer-profiles/{reviewer_profile_uuid}/expertise/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/reviewer-profiles/{reviewer_profile_uuid}/expertise/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/reviewer-profiles/{reviewer_profile_uuid}/publications/

- Extensions changed
  - New extension: x-permissions

HEAD /api/reviewer-profiles/{reviewer_profile_uuid}/publications/

- Extensions changed
  - New extension: x-permissions

POST /api/reviewer-profiles/{reviewer_profile_uuid}/publications/

- Extensions changed
  - New extension: x-permissions

DELETE /api/reviewer-profiles/{reviewer_profile_uuid}/publications/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/reviewer-profiles/{reviewer_profile_uuid}/publications/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/reviewer-profiles/{reviewer_profile_uuid}/publications/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/reviewer-profiles/{reviewer_profile_uuid}/publications/{uuid}/

- Extensions changed
  - New extension: x-permissions

DELETE /api/reviewer-profiles/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/reviewer-profiles/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/reviewer-profiles/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/reviewer-profiles/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/reviewer-profiles/{uuid}/connect-orcid/

- Extensions changed
  - New extension: x-permissions

POST /api/reviewer-profiles/{uuid}/connect-orcid/callback/

- Extensions changed
  - New extension: x-permissions

POST /api/reviewer-profiles/{uuid}/disconnect-orcid/

- Extensions changed
  - New extension: x-permissions

POST /api/reviewer-profiles/{uuid}/import-publications/

- Extensions changed
  - New extension: x-permissions

POST /api/reviewer-profiles/{uuid}/sync-orcid/

- Extensions changed
  - New extension: x-permissions

GET /api/reviewer-suggestions/

- Extensions changed
  - New extension: x-permissions

HEAD /api/reviewer-suggestions/

- Extensions changed
  - New extension: x-permissions

DELETE /api/reviewer-suggestions/{uuid}/

- Extensions changed
  - Modified extension: x-permissions
    - Added /0/kind with value: 'permission'

GET /api/reviewer-suggestions/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/reviewer-suggestions/{uuid}/confirm/

- Extensions changed
  - New extension: x-permissions

POST /api/reviewer-suggestions/{uuid}/reject/

- Extensions changed
  - New extension: x-permissions

GET /api/role-availabilities/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Modified query param: scope_type
  - Description changed from 'Scope content type (e.g. 'offering', 'customer')' to 'Scope type, as returned in scope_type: customer, project, offering, service_provider, call_organizer, call, proposal, resource, resource_project or global. A content type model name also matches.'

HEAD /api/role-availabilities/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Modified query param: scope_type
  - Description changed from 'Scope content type (e.g. 'offering', 'customer')' to 'Scope type, as returned in scope_type: customer, project, offering, service_provider, call_organizer, call, proposal, resource, resource_project or global. A content type model name also matches.'

DELETE /api/role-availabilities/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/role-availabilities/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/roles/

- Extensions changed
  - New extension: x-permissions
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [description_bg description_el description_en_gb description_mk description_sl description_sq]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: description_bg
              - New property: description_el
              - New property: description_en_gb
              - New property: description_mk
              - New property: description_sl
              - New property: description_sq
              - Modified property: content_type
                - Property 'AllOf' changed
                  - Modified schema: #/components/schemas/RoleType
                    - New enum values: [global]

HEAD /api/roles/

- Extensions changed
  - New extension: x-permissions

POST /api/roles/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: description_bg
          - New property: description_el
          - New property: description_en_gb
          - New property: description_mk
          - New property: description_sl
          - New property: description_sq
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: description_bg
            - New property: description_el
            - New property: description_en_gb
            - New property: description_mk
            - New property: description_sl
            - New property: description_sq
            - Modified property: content_type
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/RoleType
                  - New enum values: [global]

GET /api/roles/hygiene_report/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: findings
              - Items changed
                - Properties changed
                  - Modified property: scope_type
                    - Property 'OneOf' changed
                      - Modified schema: #/components/schemas/RoleType
                        - New enum values: [global]

HEAD /api/roles/hygiene_report/

- Extensions changed
  - New extension: x-permissions

DELETE /api/roles/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/roles/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [description_bg description_el description_en_gb description_mk description_sl description_sq]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: description_bg
            - New property: description_el
            - New property: description_en_gb
            - New property: description_mk
            - New property: description_sl
            - New property: description_sq
            - Modified property: content_type
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/RoleType
                  - New enum values: [global]

PATCH /api/roles/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: description_bg
          - New property: description_el
          - New property: description_en_gb
          - New property: description_mk
          - New property: description_sl
          - New property: description_sq
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: description_bg
            - New property: description_el
            - New property: description_en_gb
            - New property: description_mk
            - New property: description_sl
            - New property: description_sq
            - Modified property: content_type
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/RoleType
                  - New enum values: [global]

PUT /api/roles/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: description_bg
          - New property: description_el
          - New property: description_en_gb
          - New property: description_mk
          - New property: description_sl
          - New property: description_sq
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: description_bg
            - New property: description_el
            - New property: description_en_gb
            - New property: description_mk
            - New property: description_sl
            - New property: description_sq
            - Modified property: content_type
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/RoleType
                  - New enum values: [global]

POST /api/roles/{uuid}/clone_to_customer/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: description_bg
            - New property: description_el
            - New property: description_en_gb
            - New property: description_mk
            - New property: description_sl
            - New property: description_sq
            - Modified property: content_type
              - Property 'AllOf' changed
                - Modified schema: #/components/schemas/RoleType
                  - New enum values: [global]

POST /api/roles/{uuid}/disable/

- Extensions changed
  - New extension: x-permissions

POST /api/roles/{uuid}/enable/

- Extensions changed
  - New extension: x-permissions

PUT /api/roles/{uuid}/update_descriptions/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - New property: description_bg
          - New property: description_el
          - New property: description_en_gb
          - New property: description_mk
          - New property: description_sl
          - New property: description_sq
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: description_bg
            - New property: description_el
            - New property: description_en_gb
            - New property: description_mk
            - New property: description_sl
            - New property: description_sq

GET /api/science-domains/

- Extensions changed
  - New extension: x-permissions

HEAD /api/science-domains/

- Extensions changed
  - New extension: x-permissions

POST /api/science-domains/

- Extensions changed
  - New extension: x-permissions

POST /api/science-domains/load_preset/

- Extensions changed
  - New extension: x-permissions

GET /api/science-domains/presets/

- Extensions changed
  - New extension: x-permissions

HEAD /api/science-domains/presets/

- Extensions changed
  - New extension: x-permissions

DELETE /api/science-domains/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/science-domains/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/science-domains/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/science-domains/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/science-sub-domains/

- Extensions changed
  - New extension: x-permissions

HEAD /api/science-sub-domains/

- Extensions changed
  - New extension: x-permissions

POST /api/science-sub-domains/

- Extensions changed
  - New extension: x-permissions

DELETE /api/science-sub-domains/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/science-sub-domains/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/science-sub-domains/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/science-sub-domains/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/service-settings/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/service-settings/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/service-settings/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/sram-groups/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: urn
                - Description changed from 'SRAM global URN: '<organisation>:<co>' or '<organisation>:<co>:<group>'.' to 'SRAM global URN: '<organization>:<co>' or '<organization>:<co>:<group>'.'

HEAD /api/sram-groups/

- Extensions changed
  - New extension: x-permissions

GET /api/sram-groups/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: urn
              - Description changed from 'SRAM global URN: '<organisation>:<co>' or '<organisation>:<co>:<group>'.' to 'SRAM global URN: '<organization>:<co>' or '<organization>:<co>:<group>'.'

GET /api/sram-project-rules/

- Extensions changed
  - New extension: x-permissions

HEAD /api/sram-project-rules/

- Extensions changed
  - New extension: x-permissions

POST /api/sram-project-rules/

- Extensions changed
  - New extension: x-permissions

DELETE /api/sram-project-rules/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/sram-project-rules/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/sram-project-rules/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/sram-project-rules/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/sram-project-rules/{uuid}/preview/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - Modified property: group
                - Properties changed
                  - Modified property: urn
                    - Description changed from 'SRAM global URN: '<organisation>:<co>' or '<organisation>:<co>:<group>'.' to 'SRAM global URN: '<organization>:<co>' or '<organization>:<co>:<group>'.'

GET /api/staff-passkeys/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/staff-passkeys/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/staff-passkeys/{uuid}/revoke/

- Extensions changed
  - New extension: x-permissions

GET /api/stats/celery/

- Extensions changed
  - New extension: x-permissions
- Description changed from 'Provides a comprehensive snapshot of all Celery workers' status.

This endpoint returns detailed information about:

- **active**: Tasks currently being executed by workers
- **scheduled**: Tasks scheduled for future execution (with ETA)
- **reserved**: Tasks received by workers but not yet started
- **revoked**: Task IDs that have been cancelled/revoked
- **query_task**: Results of task queries (if any)
- **stats**: Detailed worker statistics including uptime, pool info, and broker connection

Each field is a dictionary where keys are worker names (e.g., 'celery@hostname').
If no workers are available, fields will be `null`.

Requires support user permissions.' to 'Provides a comprehensive snapshot of all Celery workers' status.

This endpoint returns detailed information about:

- **active**: Tasks currently being executed by workers
- **scheduled**: Tasks scheduled for future execution (with ETA)
- **reserved**: Tasks received by workers but not yet started
- **revoked**: Task IDs that have been canceled/revoked
- **query_task**: Results of task queries (if any)
- **stats**: Detailed worker statistics including uptime, pool info, and broker connection

Each field is a dictionary where keys are worker names (e.g., 'celery@hostname').
If no workers are available, fields will be `null`.

Requires support user permissions.'

- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: revoked
              - Description changed from 'IDs of revoked (cancelled) tasks per worker. Keys are worker names, values are lists of task IDs.' to 'IDs of revoked (canceled) tasks per worker. Keys are worker names, values are lists of task IDs.'

GET /api/stats/database/

- Extensions changed
  - New extension: x-permissions

POST /api/stats/query/

- Extensions changed
  - New extension: x-permissions

GET /api/stats/table-growth/

- Extensions changed
  - New extension: x-permissions

POST /api/stats/table-growth/

- Extensions changed
  - New extension: x-permissions

GET /api/support-attachments/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [can_delete delete_is_local_only]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Properties changed
              - New property: can_delete
              - New property: delete_is_local_only

HEAD /api/support-attachments/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/support-attachments/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: can_delete
            - New property: delete_is_local_only

DELETE /api/support-attachments/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/support-attachments/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
- Modified query param: field
  - Schema changed
    - Items changed
      - New enum values: [can_delete delete_is_local_only]
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - New property: can_delete
            - New property: delete_is_local_only

GET /api/support-canned-responses/

- Extensions changed
  - New extension: x-permissions

HEAD /api/support-canned-responses/

- Extensions changed
  - New extension: x-permissions

POST /api/support-canned-responses/

- Extensions changed
  - New extension: x-permissions

DELETE /api/support-canned-responses/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/support-canned-responses/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/support-canned-responses/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/support-canned-responses/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/support-canned-responses/{uuid}/render/

- Extensions changed
  - New extension: x-permissions

GET /api/support-comments/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/support-comments/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

DELETE /api/support-comments/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/support-comments/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/support-comments/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/support-comments/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/support-feedback-average-report/

- Extensions changed
  - New extension: x-permissions

GET /api/support-feedback-report/

- Extensions changed
  - New extension: x-permissions

GET /api/support-feedbacks/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/support-feedbacks/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/support-feedbacks/

- Extensions changed
  - New extension: x-permissions

GET /api/support-feedbacks/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

GET /api/support-issue-links/

- Extensions changed
  - New extension: x-permissions

HEAD /api/support-issue-links/

- Extensions changed
  - New extension: x-permissions

POST /api/support-issue-links/

- Extensions changed
  - New extension: x-permissions

DELETE /api/support-issue-links/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/support-issue-links/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/support-issue-links/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/support-issue-links/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/support-issue-statuses/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/support-issue-statuses/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/support-issue-statuses/

- Extensions changed
  - New extension: x-permissions

DELETE /api/support-issue-statuses/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/support-issue-statuses/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/support-issue-statuses/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/support-issue-statuses/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/support-issue-tags/

- Extensions changed
  - New extension: x-permissions

HEAD /api/support-issue-tags/

- Extensions changed
  - New extension: x-permissions

POST /api/support-issue-tags/

- Extensions changed
  - New extension: x-permissions

DELETE /api/support-issue-tags/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/support-issue-tags/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/support-issue-tags/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/support-issue-tags/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/support-issues/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/support-issues/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/support-issues/

- Extensions changed
  - New extension: x-permissions

POST /api/support-issues/bulk_update/

- Extensions changed
  - New extension: x-permissions

DELETE /api/support-issues/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/support-issues/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/support-issues/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/support-issues/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/support-issues/{uuid}/attach_resource/

- Extensions changed
  - New extension: x-permissions

POST /api/support-issues/{uuid}/comment/

- Extensions changed
  - New extension: x-permissions

POST /api/support-issues/{uuid}/escalate/

- Extensions changed
  - New extension: x-permissions

POST /api/support-issues/{uuid}/reroute/

- Extensions changed
  - New extension: x-permissions

POST /api/support-issues/{uuid}/route_to_provider/

- Extensions changed
  - New extension: x-permissions

POST /api/support-issues/{uuid}/set_status/

- Extensions changed
  - New extension: x-permissions

POST /api/support-issues/{uuid}/sync/

- Extensions changed
  - New extension: x-permissions

POST /api/support-jira-webhook/

- Extensions changed
  - New extension: x-permissions

GET /api/support-priorities/

- Extensions changed
  - New extension: x-permissions

HEAD /api/support-priorities/

- Extensions changed
  - New extension: x-permissions

GET /api/support-priorities/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/support-provider-webhook/{provider_uuid}/{backend_type}/

- Extensions changed
  - New extension: x-permissions

GET /api/support-request-types-admin/

- Extensions changed
  - New extension: x-permissions

HEAD /api/support-request-types-admin/

- Extensions changed
  - New extension: x-permissions

POST /api/support-request-types-admin/

- Extensions changed
  - New extension: x-permissions

POST /api/support-request-types-admin/reorder/

- Extensions changed
  - New extension: x-permissions

DELETE /api/support-request-types-admin/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/support-request-types-admin/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/support-request-types-admin/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/support-request-types-admin/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/support-request-types-admin/{uuid}/activate/

- Extensions changed
  - New extension: x-permissions

POST /api/support-request-types-admin/{uuid}/deactivate/

- Extensions changed
  - New extension: x-permissions

GET /api/support-request-types/

- Extensions changed
  - New extension: x-permissions

HEAD /api/support-request-types/

- Extensions changed
  - New extension: x-permissions

GET /api/support-request-types/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/support-saved-filters/

- Extensions changed
  - New extension: x-permissions

HEAD /api/support-saved-filters/

- Extensions changed
  - New extension: x-permissions

POST /api/support-saved-filters/

- Extensions changed
  - New extension: x-permissions

DELETE /api/support-saved-filters/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/support-saved-filters/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/support-saved-filters/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/support-saved-filters/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/support-smax-webhook/

- Extensions changed
  - New extension: x-permissions

GET /api/support-statistics/

- Extensions changed
  - New extension: x-permissions

GET /api/support-templates/

- Extensions changed
  - New extension: x-permissions

HEAD /api/support-templates/

- Extensions changed
  - New extension: x-permissions

POST /api/support-templates/

- Extensions changed
  - New extension: x-permissions

DELETE /api/support-templates/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/support-templates/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/support-templates/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/support-templates/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/support-templates/{uuid}/create_attachments/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - New media type: application/x-www-form-urlencoded
    - New media type: multipart/form-data

POST /api/support-templates/{uuid}/delete_attachments/

- Extensions changed
  - New extension: x-permissions

GET /api/support-users/

- Extensions changed
  - New extension: x-permissions

HEAD /api/support-users/

- Extensions changed
  - New extension: x-permissions

POST /api/support-users/

- Extensions changed
  - New extension: x-permissions

DELETE /api/support-users/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/support-users/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/support-users/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/support-users/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/support-users/{uuid}/connections/

- Extensions changed
  - New extension: x-permissions

POST /api/support-users/{uuid}/merge/

- Extensions changed
  - New extension: x-permissions

POST /api/support-zammad-webhook/

- Extensions changed
  - New extension: x-permissions

GET /api/support/settings/atlassian/current_settings/

- Extensions changed
  - New extension: x-permissions

POST /api/support/settings/atlassian/discover_custom_fields/

- Extensions changed
  - New extension: x-permissions

POST /api/support/settings/atlassian/discover_priorities/

- Extensions changed
  - New extension: x-permissions

POST /api/support/settings/atlassian/discover_projects/

- Extensions changed
  - New extension: x-permissions

POST /api/support/settings/atlassian/discover_request_types/

- Extensions changed
  - New extension: x-permissions

POST /api/support/settings/atlassian/preview_settings/

- Extensions changed
  - New extension: x-permissions

POST /api/support/settings/atlassian/save_settings/

- Extensions changed
  - New extension: x-permissions

POST /api/support/settings/atlassian/validate_credentials/

- Extensions changed
  - New extension: x-permissions

GET /api/sync-issues/

- Extensions changed
  - New extension: x-permissions

POST /api/sync-issues/

- Extensions changed
  - New extension: x-permissions

GET /api/system-logs/

- Extensions changed
  - New extension: x-permissions

HEAD /api/system-logs/

- Extensions changed
  - New extension: x-permissions

GET /api/system-logs/instances/

- Extensions changed
  - New extension: x-permissions

HEAD /api/system-logs/instances/

- Extensions changed
  - New extension: x-permissions

GET /api/system-logs/stats/

- Extensions changed
  - New extension: x-permissions

HEAD /api/system-logs/stats/

- Extensions changed
  - New extension: x-permissions

GET /api/system-logs/{id}/

- Extensions changed
  - New extension: x-permissions

GET /api/user-action-executions/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/user-action-executions/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/user-action-executions/{id}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/user-action-providers/

- Extensions changed
  - New extension: x-permissions

HEAD /api/user-action-providers/

- Extensions changed
  - New extension: x-permissions

GET /api/user-action-providers/{id}/

- Extensions changed
  - New extension: x-permissions

GET /api/user-actions/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/user-actions/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/user-actions/bulk_silence/

- Extensions changed
  - New extension: x-permissions

GET /api/user-actions/summary/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/user-actions/summary/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/user-actions/update_actions/

- Extensions changed
  - New extension: x-permissions
- Description changed from 'Trigger update of user actions' to 'Staff-only action to trigger recalculation of the actions of every user.'

GET /api/user-actions/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/user-actions/{uuid}/execute_action/

- Extensions changed
  - New extension: x-permissions

POST /api/user-actions/{uuid}/silence/

- Extensions changed
  - New extension: x-permissions

POST /api/user-actions/{uuid}/unsilence/

- Extensions changed
  - New extension: x-permissions

GET /api/user-agreements/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Items changed
            - Required changed
              - Deleted required property: language
            - Properties changed
              - Modified property: language
                - Default changed from null to ''

HEAD /api/user-agreements/

- Extensions changed
  - New extension: x-permissions

POST /api/user-agreements/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: language
        - Properties changed
          - Modified property: language
            - Default changed from null to ''
- Responses changed
  - Modified response: 201
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: language
          - Properties changed
            - Modified property: language
              - Default changed from null to ''

DELETE /api/user-agreements/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/user-agreements/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: language
          - Properties changed
            - Modified property: language
              - Default changed from null to ''

PATCH /api/user-agreements/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Properties changed
          - Modified property: language
            - Default changed from null to ''
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: language
          - Properties changed
            - Modified property: language
              - Default changed from null to ''

PUT /api/user-agreements/{uuid}/

- Extensions changed
  - New extension: x-permissions
- Request body changed
  - Content changed
    - Modified media type: application/json
      - Schema changed
        - Required changed
          - Deleted required property: language
        - Properties changed
          - Modified property: language
            - Default changed from null to ''
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Required changed
            - Deleted required property: language
          - Properties changed
            - Modified property: language
              - Default changed from null to ''

GET /api/user-group-invitations/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/user-group-invitations/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/user-group-invitations/

- Extensions changed
  - New extension: x-permissions

DELETE /api/user-group-invitations/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/user-group-invitations/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

PATCH /api/user-group-invitations/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/user-group-invitations/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/user-group-invitations/{uuid}/cancel/

- Extensions changed
  - New extension: x-permissions

GET /api/user-group-invitations/{uuid}/projects/

- Extensions changed
  - New extension: x-permissions

POST /api/user-group-invitations/{uuid}/submit_request/

- Extensions changed
  - New extension: x-permissions
- Responses changed
  - Modified response: 200
    - Content changed
      - Modified media type: application/json
        - Schema changed
          - Properties changed
            - Modified property: scope_type
              - Property 'OneOf' changed
                - Modified schema: #/components/schemas/RoleType
                  - New enum values: [global]

GET /api/user-invitations/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/user-invitations/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/user-invitations/

- Extensions changed
  - New extension: x-permissions

POST /api/user-invitations/approve/

- Extensions changed
  - New extension: x-permissions

POST /api/user-invitations/check-duplicates/

- Extensions changed
  - New extension: x-permissions

POST /api/user-invitations/reject/

- Extensions changed
  - New extension: x-permissions

DELETE /api/user-invitations/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/user-invitations/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

PATCH /api/user-invitations/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/user-invitations/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/user-invitations/{uuid}/accept/

- Extensions changed
  - New extension: x-permissions
- Description changed from 'Accepts an invitation for the currently authenticated user. This grants the user the specified role in the invitation's scope.' to 'Accepts an invitation for the currently authenticated user. This grants the user the specified role in the invitation's scope. Staff may pass `user` to accept it for that user instead, for example from a service account that registers users elsewhere; the user's email must match the invitation.'
- Request body changed

POST /api/user-invitations/{uuid}/cancel/

- Extensions changed
  - New extension: x-permissions

POST /api/user-invitations/{uuid}/check/

- Extensions changed
  - New extension: x-permissions

POST /api/user-invitations/{uuid}/delete/

- Extensions changed
  - New extension: x-permissions

GET /api/user-invitations/{uuid}/details/

- Extensions changed
  - New extension: x-permissions

POST /api/user-invitations/{uuid}/send/

- Extensions changed
  - New extension: x-permissions

GET /api/user-permission-requests/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/user-permission-requests/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

DELETE /api/user-permission-requests/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/user-permission-requests/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/user-permission-requests/{uuid}/approve/

- Extensions changed
  - New extension: x-permissions

POST /api/user-permission-requests/{uuid}/cancel_request/

- Extensions changed
  - New extension: x-permissions

POST /api/user-permission-requests/{uuid}/reject/

- Extensions changed
  - New extension: x-permissions

GET /api/user-permissions/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Modified query param: scope_type
  - Description changed from 'Scope type' to 'Scope type, as returned in scope_type: customer, project, offering, service_provider, call_organizer, call, proposal, resource, resource_project or global. A content type model name also matches.'

HEAD /api/user-permissions/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description
- Modified query param: scope_type
  - Description changed from 'Scope type' to 'Scope type, as returned in scope_type: customer, project, offering, service_provider, call_organizer, call, proposal, resource, resource_project or global. A content type model name also matches.'

GET /api/user-permissions/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

POST /api/user-permissions/{uuid}/restore/

- Extensions changed
  - New extension: x-permissions

POST /api/user-permissions/{uuid}/revoke/

- Extensions changed
  - New extension: x-permissions

GET /api/users/

- Extensions changed
  - New extension: x-permissions

HEAD /api/users/

- Extensions changed
  - New extension: x-permissions

POST /api/users/

- Extensions changed
  - New extension: x-permissions

POST /api/users/confirm_email/

- Extensions changed
  - New extension: x-permissions

GET /api/users/dashboard-general-stats/

- Extensions changed
  - New extension: x-permissions

GET /api/users/dashboard-pending-actions/

- Extensions changed
  - New extension: x-permissions

GET /api/users/me/

- Extensions changed
  - New extension: x-permissions

HEAD /api/users/me/

- Extensions changed
  - New extension: x-permissions

GET /api/users/profile_completeness/

- Extensions changed
  - New extension: x-permissions

HEAD /api/users/profile_completeness/

- Extensions changed
  - New extension: x-permissions

POST /api/users/scim_sync_all/

- Extensions changed
  - New extension: x-permissions

GET /api/users/user_active_status_count/

- Extensions changed
  - New extension: x-permissions

HEAD /api/users/user_active_status_count/

- Extensions changed
  - New extension: x-permissions

GET /api/users/user_language_count/

- Extensions changed
  - New extension: x-permissions

HEAD /api/users/user_language_count/

- Extensions changed
  - New extension: x-permissions

GET /api/users/user_registration_trend/

- Extensions changed
  - New extension: x-permissions

HEAD /api/users/user_registration_trend/

- Extensions changed
  - New extension: x-permissions

DELETE /api/users/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/users/{uuid}/

- Extensions changed
  - New extension: x-permissions

PATCH /api/users/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/users/{uuid}/

- Extensions changed
  - New extension: x-permissions

POST /api/users/{uuid}/cancel_change_email/

- Extensions changed
  - New extension: x-permissions

POST /api/users/{uuid}/change_email/

- Extensions changed
  - New extension: x-permissions

POST /api/users/{uuid}/change_password/

- Extensions changed
  - New extension: x-permissions

GET /api/users/{uuid}/data_access/

- Extensions changed
  - New extension: x-permissions

GET /api/users/{uuid}/data_access_history/

- Extensions changed
  - New extension: x-permissions

GET /api/users/{uuid}/history/

- Extensions changed
  - New extension: x-permissions

GET /api/users/{uuid}/history/at/

- Extensions changed
  - New extension: x-permissions

GET /api/users/{uuid}/identity_bridge_status/

- Extensions changed
  - New extension: x-permissions

POST /api/users/{uuid}/pull_remote_user/

- Extensions changed
  - New extension: x-permissions

POST /api/users/{uuid}/pull_scim_attributes/

- Extensions changed
  - New extension: x-permissions

POST /api/users/{uuid}/refresh_token/

- Extensions changed
  - New extension: x-permissions

POST /api/users/{uuid}/remove_password/

- Extensions changed
  - New extension: x-permissions

POST /api/users/{uuid}/send_notification/

- Extensions changed
  - New extension: x-permissions

GET /api/users/{uuid}/token/

- Extensions changed
  - New extension: x-permissions

POST /api/users/{uuid}/update_actions/

- Extensions changed
  - New extension: x-permissions

GET /api/version/

- Extensions changed
  - New extension: x-permissions

GET /api/vmware-clusters/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/vmware-clusters/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/vmware-clusters/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/vmware-datastores/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/vmware-datastores/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/vmware-datastores/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/vmware-disks/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/vmware-disks/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

DELETE /api/vmware-disks/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/vmware-disks/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/vmware-disks/{uuid}/extend/

- Extensions changed
  - New extension: x-permissions

POST /api/vmware-disks/{uuid}/pull/

- Extensions changed
  - New extension: x-permissions

POST /api/vmware-disks/{uuid}/set_erred/

- Extensions changed
  - New extension: x-permissions

POST /api/vmware-disks/{uuid}/set_ok/

- Extensions changed
  - New extension: x-permissions

POST /api/vmware-disks/{uuid}/unlink/

- Extensions changed
  - New extension: x-permissions

GET /api/vmware-folders/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/vmware-folders/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/vmware-folders/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/vmware-limits/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/vmware-networks/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/vmware-networks/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/vmware-networks/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/vmware-ports/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/vmware-ports/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

DELETE /api/vmware-ports/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/vmware-ports/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/vmware-ports/{uuid}/pull/

- Extensions changed
  - New extension: x-permissions

POST /api/vmware-ports/{uuid}/set_erred/

- Extensions changed
  - New extension: x-permissions

POST /api/vmware-ports/{uuid}/set_ok/

- Extensions changed
  - New extension: x-permissions

POST /api/vmware-ports/{uuid}/unlink/

- Extensions changed
  - New extension: x-permissions

GET /api/vmware-templates/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

HEAD /api/vmware-templates/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/vmware-templates/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility
  - New extension: x-visibility-description

GET /api/vmware-virtual-machine/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

HEAD /api/vmware-virtual-machine/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

POST /api/vmware-virtual-machine/

- Extensions changed
  - New extension: x-permissions

DELETE /api/vmware-virtual-machine/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/vmware-virtual-machine/{uuid}/

- Extensions changed
  - New extension: x-permissions
  - New extension: x-visibility

PATCH /api/vmware-virtual-machine/{uuid}/

- Extensions changed
  - New extension: x-permissions

PUT /api/vmware-virtual-machine/{uuid}/

- Extensions changed
  - New extension: x-permissions

GET /api/vmware-virtual-machine/{uuid}/console/

- Extensions changed
  - New extension: x-permissions

POST /api/vmware-virtual-machine/{uuid}/create_disk/

- Extensions changed
  - New extension: x-permissions

POST /api/vmware-virtual-machine/{uuid}/create_port/

- Extensions changed
  - New extension: x-permissions

POST /api/vmware-virtual-machine/{uuid}/pull/

- Extensions changed
  - New extension: x-permissions

POST /api/vmware-virtual-machine/{uuid}/reboot_guest/

- Extensions changed
  - New extension: x-permissions

POST /api/vmware-virtual-machine/{uuid}/reset/

- Extensions changed
  - New extension: x-permissions

POST /api/vmware-virtual-machine/{uuid}/set_erred/

- Extensions changed
  - New extension: x-permissions

POST /api/vmware-virtual-machine/{uuid}/set_ok/

- Extensions changed
  - New extension: x-permissions

POST /api/vmware-virtual-machine/{uuid}/shutdown_guest/

- Extensions changed
  - New extension: x-permissions

POST /api/vmware-virtual-machine/{uuid}/start/

- Extensions changed
  - New extension: x-permissions

POST /api/vmware-virtual-machine/{uuid}/stop/

- Extensions changed
  - New extension: x-permissions

POST /api/vmware-virtual-machine/{uuid}/suspend/

- Extensions changed
  - New extension: x-permissions

POST /api/vmware-virtual-machine/{uuid}/unlink/

- Extensions changed
  - New extension: x-permissions

GET /api/vmware-virtual-machine/{uuid}/web_console/

- Extensions changed
  - New extension: x-permissions

POST /api/web-shell-ticket/

- Extensions changed
  - New extension: x-permissions
